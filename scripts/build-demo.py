"""Render a two-minute edited walkthrough with the student's supplied recording.
Usage: python scripts/build-demo.py /absolute/path/to/narration.m4a
Requires Pillow, ffmpeg and ffprobe. The source recording stays outside Git.
Actual website captures are used; this is not a continuous screen recording.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json, subprocess, sys, re, wave
root=Path(__file__).resolve().parents[1]
tmp=root/'.sites-runtime/demo-student';tmp.mkdir(parents=True,exist_ok=True)
source=Path(sys.argv[1]).resolve()
def run(args): subprocess.run(args,check=True)
run(['ffmpeg','-y','-loglevel','error','-i',str(source),'-ar','48000','-ac','1',str(tmp/'original.wav')])
probe=subprocess.run(['ffmpeg','-hide_banner','-i',str(tmp/'original.wav'),'-af','silencedetect=noise=-35dB:d=0.45','-f','null','-'],capture_output=True,text=True,check=True)
starts=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',probe.stderr)]
ends=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',probe.stderr)]
# Retain 300 ms within detected pauses, cutting only their middle.
cuts=[(a+.15,b-.15) for a,b in zip(starts,ends) if b-a>.45]
with wave.open(str(tmp/'original.wav'),'rb') as w: params=w.getparams();raw=w.readframes(w.getnframes())
end=153.45;begin=.45
cuts=[(max(begin,a),min(end,b)) for a,b in cuts if b>begin and a<end]
spans=[];cursor=begin
for a,b in cuts:
 if a>cursor:spans.append((cursor,a))
 cursor=max(cursor,b)
if cursor<end:spans.append((cursor,end))
rate=params.framerate;unit=params.sampwidth*params.nchannels
with wave.open(str(tmp/'trimmed.wav'),'wb') as w:
 w.setparams(params)
 for a,b in spans:w.writeframes(raw[round(a*rate)*unit:round(b*rate)*unit])
duration=sum(b-a for a,b in spans);speed=duration/119.5
run(['ffmpeg','-y','-loglevel','error','-i',str(tmp/'trimmed.wav'),'-af',f'atempo={speed:.8f},loudnorm=I=-16:TP=-1.5:LRA=11,apad','-t','120',str(tmp/'voice.wav')])
def mapped(t):return sum(max(0,min(t,b)-a) for a,b in spans if t>a)/speed
scenes=json.loads((root/'data/demo-scenes.json').read_text())
# Paragraph boundaries are aligned to the supplied recording.
bounds=[begin,21.8,37.6,60.2,79.15,104.25,125.3,134.8,142.7,end]
times=[0]+[mapped(x) for x in bounds[1:-1]]+[120]
fontpath='/System/Library/Fonts/Supplemental/Arial.ttf'
def font(size):return ImageFont.truetype(fontpath,size)
def wrap(draw,text,f,width):
 lines=[];line=''
 for word in text.split():
  candidate=(line+' '+word).strip()
  if draw.textlength(candidate,font=f)>width and line:lines.append(line);line=word
  else:line=candidate
 if line:lines.append(line)
 return lines
for n,s in enumerate(scenes):
 frame=Image.new('RGB',(1440,1080),'#f5f6f0');dr=ImageDraw.Draw(frame)
 shot=Image.open(root/'data/demo-captures'/s['capture']).convert('RGB')
 if n==8:shot=shot.crop((0,0,shot.width,640)) # Focus on the package and diagram links.
 if n==4:
  shot.thumbnail((1352,850));frame.paste(shot,((1440-shot.width)//2,65))
  dr.text((44,870),f'{n+1:02} / {s["caption"]}',font=font(30),fill='#193d30')
  dr.text((44,922),s['takeaway'],font=font(26),fill='#487257')
 else:
  shot.thumbnail((890,984));frame.paste(shot,(32+(890-shot.width)//2,40+(984-shot.height)//2))
  dr.rounded_rectangle((956,40,1408,1024),radius=20,fill='#193d30')
  dr.text((988,78),'COMPUTE COMMONS',font=font(20),fill='#d3decf')
  dr.text((988,140),f'{n+1:02} / 09',font=font(38),fill='white');y=235
  for line in wrap(dr,s['caption'],font(38),380):dr.text((988,y),line,font=font(38),fill='white');y+=49
  y+=42
  for line in wrap(dr,s['takeaway'],font(27),380):dr.text((988,y),line,font=font(27),fill='#e2eacb');y+=38
  dr.text((988,906),'ACTUAL WEBSITE CAPTURE',font=font(17),fill='#d3decf')
  dr.text((988,940),'Student-recorded narration',font=font(17),fill='#d3decf')
 dr.text((32,1042),'PS3 / Initial design concept / Edited website captures with student narration',font=font(18),fill='#68766c')
 frame.save(tmp/f'{n}.png')
 s['start']=round(times[n],3);s['duration']=round(times[n+1]-times[n],3)
(root/'data/demo-scenes.json').write_text(json.dumps(scenes,indent=2)+'\n')
(tmp/'frames.txt').write_text(''.join(f"file '{tmp}/{n}.png'\nduration {times[n+1]-times[n]:.8f}\n" for n in range(9))+f"file '{tmp}/8.png'\n")
run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',str(tmp/'frames.txt'),'-i',str(tmp/'voice.wav'),'-t','120','-r','24','-c:v','libx264','-preset','fast','-crf','22','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-movflags','+faststart',str(root/'public/deliverables/demo.mp4')])
meta={'source_duration_seconds':154.688,'trimmed_duration_seconds':round(duration,3),'speech_speed_factor':round(speed,5),'output_seconds':120,'narration':'Student-supplied recording; no synthesized speech','visuals':'Edited authentic website screenshots; not continuous screen recording','cut_intervals_seconds':cuts}
(root/'data/demo-edit-metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
(root/'docs/DEMO.md').write_text('# Two-minute website demonstration\n\nThe video uses the student’s supplied English recording. Long pauses are shortened and speech is accelerated by '+f'{speed:.3f}x'+' with pitch preserved to fit 120 seconds. No synthetic voice is used.\n\nThe visuals are an edited sequence of actual hosted website screenshots and the system diagram, not a continuous screen recording. Captures show earlier real testing; their timestamps are historical. The website and GitHub repository are now public. Native recording controls did not respond during this revision, so existing captures were retained.\n\n## Reading script and scene timing\n\nThe following is the intended reading script, not a verbatim transcription of pronunciation, hesitations, or repetitions in the recording.\n\n'+'\n\n'.join(f'### {times[n]:.1f}–{times[n+1]:.1f} seconds: {s["caption"]}\n\n{s["text"]}' for n,s in enumerate(scenes))+'\n\n## Rebuild\n\nRun `python scripts/build-demo.py /absolute/path/to/narration.m4a` with the supplied source recording, Pillow, ffmpeg and ffprobe. The original personal recording is kept outside the repository; its voice appears in the public finished video. Timing/edit metadata is in `data/demo-edit-metadata.json`.\n')
print(json.dumps(meta))
