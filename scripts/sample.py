"""Original Mossling walk demo; deterministic RGBA pixels, no external inputs."""
import struct,zlib,pathlib
w,h=106,54;p=bytearray(w*h*4)
colors={'dark':(50,76,63,255),'body':(125,159,109,255),'light':(178,197,137,255),'eye':(25,40,35,255),'shine':(225,232,190,255),'leaf':(83,121,82,255),'shadow':(30,40,32,95)}
def rect(x,y,rw,rh,c):
 for yy in range(y,y+rh):
  for xx in range(x,x+rw):p[(yy*w+xx)*4:(yy*w+xx)*4+4]=bytes(colors[c])
for i in range(8):
 ox=2+(i%4)*26;oy=2+(i//4)*26;b=[0,-1,-2,-1,0,1,0,-1][i];s=[-1,0,1,0,-1,0,1,0][i]
 def r(x,y,ww,hh,c):rect(ox+x,oy+y,ww,hh,c)
 r(5,20,14,2,'shadow');r(5,10+b,14,9,'dark');r(3,12+b,18,5,'dark');r(5,10+b,14,7,'body');r(4,12+b,16,4,'body');r(7,8+b,10,3,'body');r(8,8+b,8,2,'light');r(6,11+b,4,2,'light');r(7,13+b,2,3,'eye');r(15,13+b,2,3,'eye');r(7,13+b,1,1,'shine');r(15,13+b,1,1,'shine');r(11,16+b,2,1,'dark');r(10,5+b,2,4,'leaf');r(12,4+b,4,2,'light');r(12,6+b,2,2,'leaf');r(5+s,18+b,4,2,'body');r(15-s,18+b,4,2,'body')
def chunk(k,v):return struct.pack('>I',len(v))+k+v+struct.pack('>I',zlib.crc32(k+v)&0xffffffff)
raw=b''.join(b'\0'+p[y*w*4:(y+1)*w*4] for y in range(h))
png=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',w,h,8,6,0,0,0))+chunk(b'IDAT',zlib.compress(raw))+chunk(b'IEND',b'')
(pathlib.Path(__file__).resolve().parents[1]/'web/sample.png').write_bytes(png)
