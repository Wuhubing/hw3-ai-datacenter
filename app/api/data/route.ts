import {getEvidence} from '@/lib/data';
import {failure} from '@/lib/auth';
export async function GET(){try{return Response.json(await getEvidence(),{headers:{'Cache-Control':'no-store'}})}catch(e){console.error('Evidence unavailable');return failure(e)}}
