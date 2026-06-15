const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  await page.exposeFunction('logTrace', (stack) => console.log('TRACE:', stack));
  await page.addInitScript(() => {
    Object.defineProperty(window, 'THREE', {
      set: function(val) {
        this._THREE = val;
        const orig = val.BufferGeometry.prototype.computeBoundingSphere;
        val.BufferGeometry.prototype.computeBoundingSphere = function() {
          orig.call(this);
          if (isNaN(this.boundingSphere.radius)) {
             window.logTrace(new Error().stack);
             console.log("NaN geometry pos:", this.attributes.position.array);
          }
        };
      },
      get: function() { return this._THREE; }
    });
  });
  console.log('Navigating...');
  try {
    await page.goto('http://127.0.0.1:8080/simulators/brings_surface.html', { waitUntil: 'domcontentloaded' });
    console.log('Loaded!');
  } catch(e) {
    console.error(e);
  }
  await browser.close();
})();
