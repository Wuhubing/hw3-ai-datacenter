"""Local integration checks. Uses the starter's loopback-only test identity."""
import json,urllib.request,urllib.error,http.cookiejar
base='http://127.0.0.1:5173'
jar=http.cookiejar.CookieJar(); user=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
def call(path,payload=None,opener=None,origin=True):
    headers={'Content-Type':'application/json'}
    if origin: headers['Origin']=base
    req=urllib.request.Request(base+path,data=None if payload is None else json.dumps(payload).encode(),headers=headers)
    try:
        r=(opener or urllib.request.build_opener()).open(req,timeout=25)
        raw=r.read();return r.status,json.loads(raw) if r.headers.get_content_type()=='application/json' else raw.decode()
    except urllib.error.HTTPError as e:return e.code,json.loads(e.read())
results=[]
def check(name,ok):
    assert ok,name
    results.append({'test':name,'result':'pass'})
status,e=call('/api/data');check('Public evidence and seeded D1',status==200 and len(e['countries'])==3 and len(e['sources'])>=3)
for path in ['adviser','refresh','design','roles']:
    status,_=call('/api/'+path,{'question':'Current PUE?'});check('Anonymous denied: '+path,status==401)
call('/signin-with-chatgpt?return_to=/',opener=user)
status,session=call('/api/session',opener=user);check('Local mock sign-in',session.get('signedIn'))
status,_=call('/api/register',{'agreed':False},user);check('Registration requires consent',status==400)
status,_=call('/api/register',{'agreed':True},user);check('Registration persists',status==200)
status,session=call('/api/session',opener=user);check('Registered access',session.get('registered'))
status,_=call('/api/design',{},user,origin=False);check('Cross-origin writes denied',status==403)
status,_=call('/api/adviser',{'question':'What is the PUE?'},user);check('Missing AI key returns explicit unavailable',status==503)
if session.get('role')=='admin':
    saved=e['design']['inputs'];edited=dict(saved,pue=1.3)
    status,_=call('/api/design',{'inputs':edited,'version':e['design']['updated_at']},user);check('Admin can persist PUE',status==200)
    _,changed=call('/api/data');check('Reload reads changed PUE',changed['design']['inputs']['pue']==1.3)
    status,_=call('/api/design',{'inputs':saved,'version':e['design']['updated_at']},user);check('Stale edits rejected',status!=200)
    status,_=call('/api/design',{'inputs':saved,'version':changed['design']['updated_at']},user);check('Baseline restored',status==200)
    status,r=call('/api/refresh',{},user)
    if status==200:check('Real external API refresh',r['count']==3)
    else:
        _,after=call('/api/data');check('External failure preserves evidence',len(after['metrics'])==len(e['metrics']))
        results.append({'test':'Live external refresh','result':'unavailable','detail':r})
print(json.dumps(results,indent=2))
open('docs/api-test-results.json','w').write(json.dumps(results,indent=2)+'\n')
