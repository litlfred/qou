const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  page.on('pageerror', err => console.log('PAGE ERROR:', err.message));
  page.on('request', req => console.log('REQ:', req.url()));
  console.log('Navigating...');
  try {
    await page.goto('http://127.0.0.1:8080/simulators/beta_decay_halflife.html', { waitUntil: 'domcontentloaded' });
    console.log('Loaded!');
  } catch(e) {
    console.error(e);
  }
  await browser.close();
})();
