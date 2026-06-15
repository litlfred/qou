import { chromium } from 'playwright';

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  page.on('console', msg => console.log('CONSOLE:', msg.type(), msg.text()));
  page.on('pageerror', err => console.log('PAGE ERROR:', err));
  await page.goto('file:///home/litlfred/space_cats/qou/folio-assistant/simulators/brings_surface.html', { waitUntil: 'domcontentloaded' });
  await browser.close();
})();
