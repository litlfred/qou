const { chromium } = require('@playwright/test');
(async () => {
  const browser = await chromium.launch();
  console.log('Browser launched!');
  const context = await browser.newContext();
  console.log('Context created!');
  const page = await context.newPage();
  console.log('Page created!');
  await page.goto('http://127.0.0.1:8080/simulators/brings_surface.html');
  console.log('Page loaded!');
  await browser.close();
})();
