const { chromium } = require('@playwright/test');
(async () => {
  console.log('Launching browser...');
  const browser = await chromium.launch();
  console.log('Browser launched!');
  await browser.close();
  console.log('Browser closed!');
})();
