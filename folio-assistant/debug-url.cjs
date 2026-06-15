const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  const fileUrl = 'file://' + path.resolve('simulators/brings_surface.html') + '?rmin=0.25&rmax=3.2&dr=0.08&dzeta=0.15&qN=12&mode=sp1';
  console.log('Navigating to', fileUrl);
  await page.goto(fileUrl);
  const rmin = await page.locator('#rmin').inputValue();
  console.log('rmin:', rmin);
  await browser.close();
})();
