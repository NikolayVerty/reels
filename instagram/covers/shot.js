const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
for(const c of (process.argv[3]||'sp01,sp02,sp03,sp04').split(',')){await p.goto('file://'+process.argv[2]+'/'+c+'.html');await p.waitForTimeout(400);await p.screenshot({path:process.argv[2]+'/cover-'+c+'.png'});}
await b.close();})();
