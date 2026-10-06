"""Create a narrated 120-second demonstration from actual hosted-site captures.
Requires Pillow, ffmpeg, ffprobe and macOS say (Samantha). No fabricated UI.
"""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,subprocess,textwrap
root=Path(__file__).resolve().parents[1];tmp=root/'.sites-runtime/demo-final';tmp.mkdir(exist_ok=True)
scenes=json.loads((root/'data/demo-scenes.json').read_text())
fontpath='/System/Library/Fonts/Supplemental/Arial.ttf'
def font(size):return ImageFont.truetype(fontpath,size)
def run(args):subprocess.run(args,check=True)
def wrap(draw,text,f,width):
 lines=[];line=''
 for word in text.split():
  cand=(line+' '+word).strip()
  if draw.textlength(cand,font=f)>width and line:lines.append(line);line=word
  else:line=cand
 if line:lines.append(line)
 return lines
start=0;transcript=[]
for n,s in enumerate(scenes):
 d=s['duration'];frame=Image.new('RGB',(1440,1080),'#f5f6f0');dr=ImageDraw.Draw(frame)
 shot=Image.open(root/'data/demo-captures'/s['capture']).convert('RGB')
 if n==4: # Landscape diagram gets the full width; narration caption sits below.
  shot.thumbnail((1352,850));frame.paste(shot,((1440-shot.width)//2,65));panelY=870
  dr.text((44,panelY),f'{n+1:02} / {s["caption"]}',font=font(30),fill='#193d30')
  dr.text((44,panelY+52),s['takeaway'],font=font(26),fill='#487257')
 else:
  shot.thumbnail((890,984));frame.paste(shot,(32+(890-shot.width)//2,40+(984-shot.height)//2))
  dr.rounded_rectangle((956,40,1408,1024),radius=20,fill='#193d30')
  dr.text((988,78),'COMPUTE COMMONS',font=font(20),fill='#d3decf')
  dr.text((988,140),f'{n+1:02} / 09',font=font(38),fill='white');y=235
  for line in wrap(dr,s['caption'],font(38),380):dr.text((988,y),line,font=font(38),fill='white');y+=49
  y+=42
  for line in wrap(dr,s['takeaway'],font(27),380):dr.text((988,y),line,font=font(27),fill='#e2eacb');y+=38
  dr.text((988,906),'REAL WEBSITE CAPTURE',font=font(18),fill='#d3decf')
  dr.text((988,940),'English synthetic narration',font=font(17),fill='#d3decf')
 dr.text((32,1042),'PS3 / Initial design concept / Actual website captures; not a continuous screen recording',font=font(18),fill='#68766c')
 frame.save(tmp/f'{n}.png')
 (tmp/f'{n}.txt').write_text(s['text']);run(['say','-v','Samantha','-r','178','-f',str(tmp/f'{n}.txt'),'-o',str(tmp/f'{n}.aiff')])
 duration=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',str(tmp/f'{n}.aiff')]))
 speed=max(1,duration/(d-.4));audio=f'atempo={speed:.5f},apad'
 run(['ffmpeg','-y','-loglevel','error','-loop','1','-framerate','24','-i',str(tmp/f'{n}.png'),'-i',str(tmp/f'{n}.aiff'),'-af',audio,'-t',str(d),'-c:v','libx264','-preset','fast','-crf','22','-pix_fmt','yuv420p','-c:a','aac','-ar','44100','-ac','2',str(tmp/f'{n}.mp4')])
 transcript.append(f'## {start:03d}-{start+d:03d} seconds: {s["caption"]}\n\n{s["text"]}');start+=d
(tmp/'segments.txt').write_text(''.join(f"file '{tmp}/{n}.mp4'\n" for n in range(len(scenes))))
run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',str(tmp/'segments.txt'),'-t','120','-c','copy','-movflags','+faststart',str(root/'public/deliverables/demo.mp4')])
(root/'docs/DEMO.md').write_text('# Two-minute website demonstration\n\n120-second edited sequence of actual hosted website screenshots and the website system diagram, captured during authenticated testing. It is not a continuous screen recording. English voice is synthetic (macOS Samantha), not the student\'s voice. Captures show real model results, a real successful API refresh, and real OpenAI answers. The temporary PUE test was restored to 1.25 before final baseline captures.\n\n'+'\n\n'.join(transcript)+'\n')
print('Created narrated demonstration: 120 seconds, 1440 x 1080.')
