import {getChatGPTUser,chatGPTSignInPath} from '@/app/chatgpt-auth';
import {member,failure} from '@/lib/auth';
import {env} from 'cloudflare:workers';
export async function GET(){try{const u=await getChatGPTUser();if(!u)return Response.json({signedIn:false,signIn:chatGPTSignInPath('/?view=adviser')});let role=null;try{role=(await member()).role}catch{}return Response.json({signedIn:true,registered:!!role,role,userId:u.userId,displayName:u.displayName,aiConfigured:!!(env as any).OPENAI_API_KEY},{headers:{'Cache-Control':'no-store'}})}catch(e){return failure(e)}}
