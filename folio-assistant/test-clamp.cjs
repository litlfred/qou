const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setContent('<input type="range" id="dr" min="0.01" max="1.0" step="0.01" value="0.14">');
  await page.evaluate(() => {
    document.getElementById('dr').value = "0.00001";
  });
  const val = await page.evaluate(() => document.getElementById('dr').value);
  console.log('Clamped value:', val);
  await browser.close();
})();
