import { chromium } from 'playwright';
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('http://localhost:8080/simulators/beta_decay_halflife.html', { waitUntil: 'domcontentloaded' });
  const q = await page.locator('#sl-q').inputValue();
  const nuc = await page.locator('#sel-nuc').inputValue();
  console.log('Default q:', q, 'nuc:', nuc);

  await page.goto('http://localhost:8080/simulators/beta_decay_halflife.html?q=1.234&nucleus=He6&mode=from-Qexp&showShellCorrection=false', { waitUntil: 'domcontentloaded' });
  const q2 = await page.locator('#sl-q').inputValue();
  const nuc2 = await page.locator('#sel-nuc').inputValue();
  console.log('Custom q2:', q2, 'nuc2:', nuc2);
  
  await browser.close();
})();
