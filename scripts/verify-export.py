"""Compare exported PNGs to the original source, including trim reconstruction."""
import argparse,zipfile,json,io,pathlib,hashlib
from PIL import Image
p=argparse.ArgumentParser();p.add_argument('zip');p.add_argument('--output',default='evidence/export.json');args=p.parse_args()
source=Image.open('web/sample.png').convert('RGBA')
with zipfile.ZipFile(args.zip) as z:
 assert z.testzip() is None
 m=json.loads(z.read('manifest.json'));assert m['format']=='ink-sprites';assert len(m['frames'])==8
 for f in m['frames']:
  r=f['sourceRect'];t=f['spriteSourceSize'];out=Image.open(io.BytesIO(z.read(f['filename']))).convert('RGBA')
  expected=source.crop((r['x']+t['x'],r['y']+t['y'],r['x']+t['x']+t['w'],r['y']+t['y']+t['h']))
  assert out.size==expected.size and out.tobytes()==expected.tobytes(),f['filename']
  reconstructed=Image.new('RGBA',(f['sourceSize']['w'],f['sourceSize']['h']));reconstructed.paste(out,(t['x'],t['y']))
  original=source.crop((r['x'],r['y'],r['x']+r['w'],r['y']+r['h']))
  assert reconstructed.tobytes()==original.tobytes(),f['filename']+' reconstruction'
 proof={'frames':len(m['frames']),'crcVerified':True,'pixelExact':True,'trimOffsetsReconstructSource':True,'sourceFileId':m['source']['fileId'],'trim':m['grid']['trim'],'sizes':[f['spriteSourceSize'] for f in m['frames']],'sha256':hashlib.sha256(pathlib.Path(args.zip).read_bytes()).hexdigest()}
 pathlib.Path(args.output).write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof))
