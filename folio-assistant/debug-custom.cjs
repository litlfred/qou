const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  console.log('Navigating...');
  await page.goto('http://127.0.0.1:8080/simulators/brings_surface.html?rmin=0.25&rmax=3.2&dr=0.08&dzeta=0.15&qN=12&mode=sp1', { waitUntil: 'domcontentloaded' });
  console.log('Loaded!');
  const dzetaVal = await page.evaluate(() => {
     const el = document.getElementById('dzeta');
     return el ? el.value : 'ELEMENT NOT FOUND';
  });
  console.log('dzeta value:', dzetaVal);
  await browser.close();
})();
