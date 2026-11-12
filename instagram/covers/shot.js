const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
for(const c of ['sp01','sp02','sp03']){await p.goto('file://'+process.argv[2]+'/'+c+'.html');await p.waitForTimeout(400);await p.screenshot({path:process.argv[2]+'/cover-'+c+'.png'});}
await b.close();})();
