"""Package course deliverables and inspectable engineering evidence; exclude secrets/runtime."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import re
root=Path(__file__).resolve().parents[1]
files=[root/'README.md',root/'public/system-diagram.svg',root/'.openai/hosting.json']
for folder in ['docs','db','drizzle','lib','tests','app/api']:
 files.extend(p for p in (root/folder).rglob('*') if p.is_file())
files.extend(p for p in (root/'public/deliverables').iterdir() if p.is_file() and p.suffix in ['.pdf','.pptx','.mp4','.txt'])
for name in ['verify-complete.mjs','verify-api.py','build-submission-pdfs.py','build-demo.py','package-submission.py']:files.append(root/'scripts'/name)
files.extend(p for p in (root/'data').rglob('*') if p.is_file())
out=root/'public/deliverables/submission.zip'
with ZipFile(out,'w',ZIP_DEFLATED) as z:
 for p in sorted(set(files)):z.write(p,'HW3/'+str(p.relative_to(root)))
with ZipFile(out) as z:
 assert z.testzip() is None
 assert not any('.dev.vars' in n or 'token.txt' in n or 'node_modules' in n or '.env' in n for n in z.namelist())
print('Submission package:',len(files),'files;',out.stat().st_size,'bytes')
for link in set(re.findall(r'href="(/deliverables/[^"?]+)"',(root/'app/explorer.tsx').read_text())):
 assert (root/'public'/link.lstrip('/')).is_file(),link
print('Every local deliverable download link has a file.')
