"""Reproducible PDF exports of existing reviewed slides and the concept diagram."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
import xml.etree.ElementTree as ET
import re,math
root=Path(__file__).resolve().parents[1];out=root/'public/deliverables'
c=canvas.Canvas(str(out/'presentation.pdf'),pagesize=(960,540));c.setTitle('Compute Commons - Investment Committee Presentation')
for n in range(1,6):
 c.drawImage(str(root/f'.sites-runtime/artifacts/slide-{n}.png'),0,0,width=960,height=540);c.showPage()
c.save()
# Exact simple shapes/text from the repository SVG, with native vector PDF content.
c=canvas.Canvas(str(out/'system-diagram.pdf'),pagesize=(1200,760));c.setTitle('Compute Commons - First-phase System Diagram')
def paint(el,parent={}):
 tag=el.tag.split('}')[-1];a={**parent,**el.attrib}
 if tag in ['defs','marker']:return
 fill=a.get('fill','#193d30');stroke=a.get('stroke','none')
 if fill!='none':c.setFillColor(HexColor(fill) if fill.startswith('#') else {'white':HexColor('#ffffff')}[fill])
 if stroke!='none':c.setStrokeColor(HexColor(stroke))
 c.setLineWidth(float(a.get('stroke-width',1)));c.setDash([float(x) for x in a.get('stroke-dasharray','').split()] or [])
 if tag=='rect':c.roundRect(float(a.get('x',0)),760-float(a.get('y',0))-float(a['height']),float(a['width']),float(a['height']),float(a.get('rx',0)),stroke=int(stroke!='none'),fill=int(fill!='none'))
 if tag=='text':
  c.setFont('Helvetica',float(a.get('font-size',14)));c.drawString(float(a['x']),760-float(a['y']),''.join(el.itertext()).replace('≥','>='))
 if tag=='path':
  parts=re.findall(r'[MHV]|-?\d+(?:\.\d+)?',a['d']);p=c.beginPath();j=0;x=y=0;prev=(0,0)
  while j<len(parts):
   cmd=parts[j];j+=1;prev=(x,y)
   if cmd=='M':x=float(parts[j]);y=float(parts[j+1]);j+=2;p.moveTo(x,760-y)
   elif cmd=='H':x=float(parts[j]);j+=1;p.lineTo(x,760-y)
   elif cmd=='V':y=float(parts[j]);j+=1;p.lineTo(x,760-y)
   else:raise ValueError(a['d'])
  c.drawPath(p,stroke=int(stroke!='none'),fill=0)
  if a.get('marker-end'):
   dx=x-prev[0];dy=y-prev[1];d=math.hypot(dx,dy);ux=dx/d;uy=dy/d;c.setDash([])
   c.line(x,760-y,x-7*ux+4*uy,760-(y-7*uy-4*ux));c.line(x,760-y,x-7*ux-4*uy,760-(y-7*uy+4*ux))
 for child in el:paint(child,a)
paint(ET.parse(root/'public/system-diagram.svg').getroot());c.save()
# Request flow: a readable actual architecture diagram rather than numbered prose alone.
c=canvas.Canvas(str(out/'architecture.pdf'),pagesize=(612,792));c.setTitle('Compute Commons - Browser to D1 to OpenAI')
c.setFillColor(HexColor('#193d30'));c.setFont('Helvetica',25);c.drawString(40,744,'Evidence to answer')
c.setFont('Helvetica',11);c.drawString(40,721,'Server-side request flow / PS3 / 06 OCT 2026')
style=ParagraphStyle('body',fontName='Helvetica',fontSize=9,leading=12,textColor=HexColor('#34483b'))
def box(y,title,text):
 c.setFillColor(HexColor('#eef2e8'));c.setStrokeColor(HexColor('#bdcdbf'));c.roundRect(40,y,532,68,7,fill=1,stroke=1)
 c.setFillColor(HexColor('#193d30'));c.setFont('Helvetica-Bold',11);c.drawString(53,y+48,title)
 p=Paragraph(text,style);w,h=p.wrap(502,40);p.drawOn(c,53,y+38-h)
def arrow(y):
 c.setStrokeColor(HexColor('#487257'));c.line(306,y,306,y-13);c.line(302,y-9,306,y-13);c.line(310,y-9,306,y-13)
steps=[('1 / Browser + ChatGPT sign-in','Question only; no API key or chosen role. Registration follows authenticated identity. Public application pages read /api/data; hosted audience controls access.'),('2 / Sites backend checks access','Trusted identity header -> D1 users -> registration/role check -> same-origin check -> atomic rate limit. Anonymous and unregistered adviser calls are rejected.'),('3 / D1 supplies current evidence','Prepared queries read saved model inputs, 19 claims, metrics and source records. First-phase engineering assumptions are persisted. Missing values remain NULL.'),('4 / OpenAI + controlled tools','Server-only secret; current D1 evidence is untrusted data, not instructions. Tools read design/country data or calculate energy/scenarios; at most three model turns.'),('5 / Approved external API','World Bank fixed historical endpoint. Editor/admin refresh validates country, indicator, year, unit, range and complete response before an atomic D1 batch. Failure retains data.'),('6 / Validate -> audit -> browser','Answer schema restricts citation IDs to real sources. Server checks output, records token totals, and returns answer, source links, assumptions and uncertainty. No question text is audited.')]
for i,(title,text) in enumerate(steps):
 y=626-i*83;box(y,title,text)
 if i<5:arrow(y)
p=Paragraph('<b>Storage:</b> users, countries, sources, metrics, designs, design_claims, events, rate_limits. Schema migrations and separate idempotent seeds preserve saved data.<br/><br/><b>Verification boundary:</b> real model tests cover saved-input changes, missing facts, source citations, certification refusal and one malicious-source fixture. These are finite tests, not a general safety or engineering guarantee. Teacher access remains a separate submission step.',style);w,h=p.wrap(532,150);p.drawOn(c,40,186-h)
c.setFont('Helvetica',8);c.drawString(40,35,'COMPUTE COMMONS / Individual request-chain explanation is included in the repository.');c.save()
print('Created presentation.pdf (5 pages), system-diagram.pdf (1), architecture.pdf (1).')
