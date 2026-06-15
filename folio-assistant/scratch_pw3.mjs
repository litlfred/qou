import { chromium } from 'playwright';
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  page.on('pageerror', err => console.log('Page error:', err.message));
  page.on('console', msg => console.log('Console:', msg.text()));
  await page.goto('http://localhost:8080/simulators/beta_decay_halflife.html?q=1.234&nucleus=He6&mode=from-Qexp&showShellCorrection=false', { waitUntil: 'domcontentloaded' });
  const q2 = await page.locator('#sl-q').inputValue();
  console.log('Custom q2:', q2);
  await browser.close();
})();
