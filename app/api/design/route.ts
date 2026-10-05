import {originCheck,member,body,failure,HttpError} from '@/lib/auth';
import {saveDesign} from '@/lib/data';
import {defaults,validateInputs} from '@/lib/model';
export async function POST(req:Request){try{originCheck(req);const u=await member(['admin']);const b=await body(req);if(!b.inputs||Object.keys(defaults).some(k=>typeof b.inputs[k]!=='number')||Object.keys(b.inputs).some(k=>!(k in defaults)))throw new HttpError(400,'Provide all model inputs.');try{validateInputs(b.inputs)}catch(e){throw new HttpError(400,(e as Error).message)}await saveDesign(b.inputs,u.userId,b.version);return Response.json({ok:true})}catch(e){return failure(e)}}
