import { test, expect } from '@playwright/test';

// Global error listener configuration to catch console errors and crashes
test.beforeEach(async ({ page }) => {
  // We need to allow external requests for CDNs like cdnjs and jsdelivr.
  // Not intercepting network requests.

  const consoleErrors: string[] = [];
  page.on('console', msg => {
    if (msg.type() === 'error') {
      const text = msg.text();
      // Ignore benign Three.js errors that don't affect layout
      if (text.includes('computeBoundingSphere')) return;
      // Ignore "Failed to fetch" errors that happen when the page closes/navigates
      if (text.includes('Failed to fetch CODATA masses')) return;
      consoleErrors.push(`[Console Error] ${text}`);
    }
  });
  page.on('pageerror', err => {
    consoleErrors.push(`[Page Error] ${err.message}\nStack: ${err.stack}`);
  });
  page.on('crash', () => {
    consoleErrors.push('[Crash] The page crashed!');
  });
  
  (page as any)._consoleErrors = consoleErrors;
});

test.afterEach(async ({ page }) => {
  const consoleErrors = (page as any)._consoleErrors || [];
  if (consoleErrors.length > 0) {
    console.error('Test failed due to console errors:', consoleErrors);
  }
  expect(consoleErrors, 'Expected no console errors or page crashes').toEqual([]);
});

// Paths to simulator files
const BRINGS_SURFACE_URL = '/simulators/brings_surface.html';
const QUANTUM_BRINGS_SURFACE_URL = '/simulators/quantum_brings_surface.html';
const BETA_DECAY_HALFLIFE_URL = '/simulators/beta_decay_halflife.html';
const KNOT_PERIODIC_TABLE_URL = '/simulators/knot_periodic_table.html';

// ── TIER 1: FEATURE COVERAGE ──────────────────────────────────────────
test.describe('Tier 1: Feature Coverage & Parameter Parsing', () => {

  test.describe('Brings Surface', () => {
    test('Default Happy-Path Load', async ({ page }) => {
      await page.goto(BRINGS_SURFACE_URL, { waitUntil: 'domcontentloaded' });
      await expect(page.locator('body')).toBeAttached();
      // Verify default values in controls
      await expect(page.locator('#rmin')).toHaveValue('0.12');
      await expect(page.locator('#rmax')).toHaveValue('2.5');
      await expect(page.locator('#dr')).toHaveValue('0.14');
      await expect(page.locator('#dzeta')).toHaveValue('0.09');
      await expect(page.locator('#qN')).toHaveValue('18');
      await expect(page.locator('#mode-row .pill.active')).toHaveAttribute('data-mode', 'omega');
    });

    test('Custom Parameters Parsing', async ({ page }) => {
      const query = '?rmin=0.25&rmax=3.2&dr=0.08&dzeta=0.15&qN=12&mode=sp1';
      await page.goto(`${BRINGS_SURFACE_URL}${query}`, { waitUntil: 'domcontentloaded' });
      
      // Verify that controls reflect parsed URL parameters
      await expect(page.locator('#rmin')).toHaveValue('0.25');
      await expect(page.locator('#rmax')).toHaveValue('3.2');
      await expect(page.locator('#dr')).toHaveValue('0.08');
      await expect(page.locator('#dzeta')).toHaveValue('0.15');
      await expect(page.locator('#qN')).toHaveValue('12');
      await expect(page.locator('#mode-row .pill.active')).toHaveAttribute('data-mode', 'sp1');
    });
  });

  test.describe('Quantum Brings Surface (Placeholders)', () => {
    test('Default Happy-Path Load', async ({ page }) => {
      await page.goto(QUANTUM_BRINGS_SURFACE_URL, { waitUntil: 'domcontentloaded' });
      await expect(page.locator('body')).toBeAttached();
    });

    test('Custom Parameters Parsing (Placeholder Assertions)', async ({ page }) => {
      const query = '?rMin=0.35&rMax=2.8&deltaR=0.05&deltaZeta=0.08&N=15&projection=polar';
      await page.goto(`${QUANTUM_BRINGS_SURFACE_URL}${query}`, { waitUntil: 'domcontentloaded' });

      // Placeholder assertions that should fail if the elements are not present/implemented
      await expect(page.locator('#rMin')).toHaveValue('0.35');
      await expect(page.locator('#rMax')).toHaveValue('2.8');
      await expect(page.locator('#deltaR')).toHaveValue('0.05');
      await expect(page.locator('#deltaZeta')).toHaveValue('0.08');
      await expect(page.locator('#N')).toHaveValue('15');
      await expect(page.locator('#projection')).toHaveValue('polar');
    });
  });

  test.describe('Beta Decay Half-Life', () => {
    test('Default Happy-Path Load', async ({ page }) => {
      await page.goto(BETA_DECAY_HALFLIFE_URL, { waitUntil: 'domcontentloaded' });
      await expect(page.locator('body')).toBeAttached();
      await expect(page.locator('#sl-q')).toHaveValue('1.11');
      await expect(page.locator('#sel-nuc')).toHaveValue('0');
      await expect(page.locator('input[name=mode]:checked')).toHaveValue('from-q');
      await expect(page.locator('#cb-shell')).toBeChecked();
    });

    test('Custom Parameters Parsing', async ({ page }) => {
      const query = '?q=1.234&nucleus=1&mode=from-Qexp&shell=false';
      await page.goto(`${BETA_DECAY_HALFLIFE_URL}${query}`, { waitUntil: 'domcontentloaded' });

      await expect(page.locator('#sl-q')).toHaveValue('1.234');
      await expect(page.locator('#sel-nuc')).toHaveValue('1');
      await expect(page.locator('input[name=mode]:checked')).toHaveValue('from-Qexp');
      await expect(page.locator('#cb-shell')).not.toBeChecked();
    });
  });

  test.describe('Knot Periodic Table', () => {
    test('Default Happy-Path Load', async ({ page }) => {
      await page.goto(KNOT_PERIODIC_TABLE_URL, { waitUntil: 'domcontentloaded' });
      await expect(page.locator('body')).toBeAttached();
      await expect(page.locator('#color-mode')).toHaveValue('block');
      await expect(page.locator('#sl-q')).toHaveValue('1.11');
    });

    test('Custom Parameters & Placeholders Parsing', async ({ page }) => {
      const query = '?color=alexander&q=1.450&layout=grid&columns=8&filter=alternating';
      await page.goto(`${KNOT_PERIODIC_TABLE_URL}${query}`, { waitUntil: 'domcontentloaded' });

      await expect(page.locator('#color-mode')).toHaveValue('alexander');
      await expect(page.locator('#sl-q')).toHaveValue('1.45');

      // Placeholder assertions for layout, columns, filter to be implemented by other tracks
      await expect(page.locator('#layout-mode')).toHaveValue('grid');
      await expect(page.locator('#columns-input')).toHaveValue('8');
      await expect(page.locator('#filter-mode')).toHaveValue('alternating');
    });
  });

});

// ── TIER 2: BOUNDARY & CORNER CASES ────────────────────────────────────
test.describe('Tier 2: Boundary & Corner Cases', () => {

  test.describe('Brings Surface Boundary Checks', () => {
    test('Extremely Small Value & Clamping', async ({ page }) => {
      const query = '?rmin=0.0001&dr=0.00001';
      await page.goto(`${BRINGS_SURFACE_URL}${query}`, { waitUntil: 'domcontentloaded' });
      await expect(page.locator('#rmin')).toHaveValue('0.02');
      await expect(page.locator('#dr')).toHaveValue('0.02');
    });

    test('Invalid Parameter Types', async ({ page }) => {
      const query = '?rmin=banana&qN=xyz';
      await page.goto(`${BRINGS_SURFACE_URL}${query}`, { waitUntil: 'domcontentloaded' });
      await expect(page.locator('#rmin')).toHaveValue('0.12');
      await expect(page.locator('#qN')).toHaveValue('18');
    });
  });

  test.describe('Beta Decay Half-Life Boundary Checks', () => {
    test('Out of Bound Deformation Parameter', async ({ page }) => {
      await page.goto(`${BETA_DECAY_HALFLIFE_URL}?q=5.0`, { waitUntil: 'domcontentloaded' });
      await expect(page.locator('#sl-q')).toHaveValue('2');

      await page.goto(`${BETA_DECAY_HALFLIFE_URL}?q=0.5`, { waitUntil: 'domcontentloaded' });
      await expect(page.locator('#sl-q')).toHaveValue('1.005');
    });

    test('Non-existent Nucleus Fallback', async ({ page }) => {
      await page.goto(`${BETA_DECAY_HALFLIFE_URL}?nucleus=Unobtainium999`, { waitUntil: 'domcontentloaded' });
      await expect(page.locator('#sel-nuc')).toHaveValue('0');
    });
  });

  test.describe('Knot Periodic Table Boundary Checks', () => {
    test('Unsupported Color Mode Fallback', async ({ page }) => {
      await page.goto(`${KNOT_PERIODIC_TABLE_URL}?color=non-existent-color-mode`, { waitUntil: 'domcontentloaded' });
      await expect(page.locator('#color-mode')).toHaveValue('block');
    });

    test('Invalid Slider Parameter q', async ({ page }) => {
      await page.goto(`${KNOT_PERIODIC_TABLE_URL}?q=0.5`, { waitUntil: 'domcontentloaded' });
      await expect(page.locator('#sl-q')).toHaveValue('1.001');
    });
  });

});

// ── TIER 3: CROSS-FEATURE / PAIRWISE COMBINATIONS ──────────────────────
test.describe('Tier 3: Cross-Feature / Pairwise Combinations', () => {

  test('Brings Surface Combined Custom State', async ({ page }) => {
    const query = '?rmin=0.5&rmax=1.5&dr=0.1&dzeta=0.2&qN=4&projection=raw';
    await page.goto(`${BRINGS_SURFACE_URL}${query}`, { waitUntil: 'domcontentloaded' });

    await expect(page.locator('#rmin')).toHaveValue('0.5');
    await expect(page.locator('#rmax')).toHaveValue('1.5');
    await expect(page.locator('#dr')).toHaveValue('0.1');
    await expect(page.locator('#dzeta')).toHaveValue('0.2');
    await expect(page.locator('#qN')).toHaveValue('4');
    await expect(page.locator('#mode-row .pill.active')).toHaveAttribute('data-mode', 'raw');
  });

  test('Beta Decay Combined Custom State', async ({ page }) => {
    const query = '?q=1.500&nucleus=1&mode=from-Qexp&shell=false';
    await page.goto(`${BETA_DECAY_HALFLIFE_URL}${query}`, { waitUntil: 'domcontentloaded' });

    await expect(page.locator('#sl-q')).toHaveValue('1.5');
    await expect(page.locator('#sel-nuc')).toHaveValue('1');
    await expect(page.locator('input[name=mode]:checked')).toHaveValue('from-Qexp');
    await expect(page.locator('#cb-shell')).not.toBeChecked();
  });

});

// ── TIER 4: REAL-WORLD APPLICATION SCENARIOS ──────────────────────────
test.describe('Tier 4: Real-World Application Scenarios', () => {

  test('Simulated Teaching & Analysis Session', async ({ page }) => {
    await page.goto(`${BRINGS_SURFACE_URL}?rmin=0.2&rmax=3.0&dr=0.1`, { waitUntil: 'domcontentloaded' });
    
    const dzetaSlider = page.locator('#dzeta');
    await dzetaSlider.fill('0.2');
    await dzetaSlider.dispatchEvent('input');

    await expect(page.locator('#v_dzeta')).toHaveText('0.200');

    await page.locator('.pill[data-mode="raw"]').click();
    await expect(page.locator('.pill.active')).toHaveAttribute('data-mode', 'raw');

    const surfCheckbox = page.locator('#cb_surf');
    await surfCheckbox.uncheck({ force: true });
    await expect(surfCheckbox).not.toBeChecked();
  });

  test('Isotope Stability Investigation Flow', async ({ page }) => {
    await page.goto(`${BETA_DECAY_HALFLIFE_URL}?nucleus=1&q=1.200`, { waitUntil: 'domcontentloaded' });
    await expect(page.locator('#sel-nuc')).toHaveValue('1');
    await expect(page.locator('#sl-q')).toHaveValue('1.2');

    await page.locator('#cb-shell').click();
    await expect(page.locator('#cb-shell')).not.toBeChecked();

    await page.locator('#sel-nuc').selectOption('0');
    await expect(page.locator('#sel-nuc')).toHaveValue('0');
  });

});
