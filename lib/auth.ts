import {env} from 'cloudflare:workers';
import {getChatGPTUser} from '@/app/chatgpt-auth';
import {db} from './data';
export class HttpError extends Error{constructor(public status:number,message:string){super(message)}}
export async function identity(){const u=await getChatGPTUser();if(!u)throw new HttpError(401,'Sign in with ChatGPT to continue.');return u;}
export async function member(roles?:string[]){const u=await identity();const r=await db().prepare('SELECT * FROM users WHERE authenticated_user_id=?').bind(u.userId).first<any>();if(!r)throw new HttpError(403,'Complete registration before using this feature.');const configured=((env as any).ADMIN_USER_IDS??'').split(',').map((x:string)=>x.trim());const role=configured.includes(u.userId)?'admin':r.role;if(roles&&!roles.includes(role))throw new HttpError(403,'An authorized editor or administrator is required.');return {...u,role};}
export function originCheck(req:Request){const origin=req.headers.get('origin');if(!origin||origin!==new URL(req.url).origin)throw new HttpError(403,'A same-origin request is required.');}
export function failure(e:unknown){const status=e instanceof HttpError?e.status:503;return Response.json({error:e instanceof HttpError?e.message:'This operation is unavailable. Your last saved data has been preserved.'},{status});}
export async function body(req:Request){if(Number(req.headers.get('content-length')??0)>12000)throw new HttpError(413,'Request too large.');const text=await req.text();if(text.length>12000)throw new HttpError(413,'Request too large.');try{return JSON.parse(text)}catch{throw new HttpError(400,'Invalid request.')}}
