import { chromium } from 'playwright';

(async () => {
  const browser = await chromium.launch({ headless: true, args: ['--no-sandbox'] });
  const context = await browser.newContext();
  const page = await context.newPage();
  page.on('console', msg => console.log(msg.text()));
  page.on('pageerror', err => console.log(err));
  
  console.log('Navigating...');
  await page.goto('http://127.0.0.1:8080/simulators/brings_surface.html', { waitUntil: 'domcontentloaded' });
  console.log('Navigated!');
  await browser.close();
})();
