import{slice}from'./model.mjs';
let pixels,width,height;
self.onmessage=({data:m})=>{try{if(m.type==='image'){pixels=new Uint8ClampedArray(m.pixels);width=m.width;height=m.height;}if(!pixels)throw Error('Open a sheet first.');const result=slice(pixels,width,height,m.options);self.postMessage({id:m.id,result});}catch(e){self.postMessage({id:m.id,error:e.message});}};
