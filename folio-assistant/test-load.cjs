const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  console.time('goto');
  await page.goto('http://127.0.0.1:8080/simulators/brings_surface.html', { waitUntil: 'domcontentloaded' });
  console.timeEnd('goto');
  await browser.close();
})();
