import {originCheck,member,failure} from '@/lib/auth';
import {db,audit,seed} from '@/lib/data';
import {refreshRecords} from '@/lib/external';
export async function POST(req:Request){try{originCheck(req);const u=await member(['editor','admin']);await seed();const result=await refreshRecords(db());await audit(u.userId,'refresh',result.updatedAt);return Response.json({ok:true,...result})}catch(e){return failure(e)}}
