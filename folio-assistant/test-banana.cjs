const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setContent('<input type="range" id="rmin" min="0.02" max="2.0" step="0.01" value="0.12">');
  await page.evaluate(() => {
    document.getElementById('rmin').value = "banana";
  });
  const val = await page.evaluate(() => document.getElementById('rmin').value);
  console.log('Banana value:', val);
  await browser.close();
})();
