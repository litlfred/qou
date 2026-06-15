import { chromium } from 'playwright';
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('http://localhost:8080/simulators/brings_surface.html?rmin=0.25&rmax=3.2&dr=0.08&dzeta=0.15&qN=12&projection=sp1', { waitUntil: 'domcontentloaded' });
  const val = await page.locator('#rmin').inputValue();
  console.log('rmin:', val);
  const search = await page.evaluate(() => location.search);
  console.log('search:', search);
  await browser.close();
})();
