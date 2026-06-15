# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: simulators.spec.ts >> Tier 1: Feature Coverage & Parameter Parsing >> Brings Surface >> Custom Parameters Parsing
- Location: tests/simulators.spec.ts:59:5

# Error details

```
Test timeout of 180000ms exceeded.
```

```
Error: page.goto: Test timeout of 180000ms exceeded.
Call log:
  - navigating to "http://127.0.0.1:8080/simulators/brings_surface.html?rmin=0.25&rmax=3.2&dr=0.08&dzeta=0.15&qN=12&mode=sp1", waiting until "domcontentloaded"

```

# Test source

```ts
  1   | import { test, expect } from '@playwright/test';
  2   | 
  3   | // Global error listener configuration to catch console errors and crashes
  4   | test.beforeEach(async ({ page }) => {
  5   |   // We need to allow external requests for CDNs like cdnjs and jsdelivr.
  6   |   // Not intercepting network requests.
  7   | 
  8   |   const consoleErrors: string[] = [];
  9   |   page.on('console', msg => {
  10  |     if (msg.type() === 'error') {
  11  |       const text = msg.text();
  12  |       // Ignore benign Three.js errors that don't affect layout
  13  |       if (text.includes('computeBoundingSphere')) return;
  14  |       // Ignore "Failed to fetch" errors that happen when the page closes/navigates
  15  |       if (text.includes('Failed to fetch CODATA masses')) return;
  16  |       consoleErrors.push(`[Console Error] ${text}`);
  17  |     }
  18  |   });
  19  |   page.on('pageerror', err => {
  20  |     consoleErrors.push(`[Page Error] ${err.message}\nStack: ${err.stack}`);
  21  |   });
  22  |   page.on('crash', () => {
  23  |     consoleErrors.push('[Crash] The page crashed!');
  24  |   });
  25  |   
  26  |   (page as any)._consoleErrors = consoleErrors;
  27  | });
  28  | 
  29  | test.afterEach(async ({ page }) => {
  30  |   const consoleErrors = (page as any)._consoleErrors || [];
  31  |   if (consoleErrors.length > 0) {
  32  |     console.error('Test failed due to console errors:', consoleErrors);
  33  |   }
  34  |   expect(consoleErrors, 'Expected no console errors or page crashes').toEqual([]);
  35  | });
  36  | 
  37  | // Paths to simulator files
  38  | const BRINGS_SURFACE_URL = '/simulators/brings_surface.html';
  39  | const QUANTUM_BRINGS_SURFACE_URL = '/simulators/quantum_brings_surface.html';
  40  | const BETA_DECAY_HALFLIFE_URL = '/simulators/beta_decay_halflife.html';
  41  | const KNOT_PERIODIC_TABLE_URL = '/simulators/knot_periodic_table.html';
  42  | 
  43  | // ── TIER 1: FEATURE COVERAGE ──────────────────────────────────────────
  44  | test.describe('Tier 1: Feature Coverage & Parameter Parsing', () => {
  45  | 
  46  |   test.describe('Brings Surface', () => {
  47  |     test('Default Happy-Path Load', async ({ page }) => {
  48  |       await page.goto(BRINGS_SURFACE_URL, { waitUntil: 'domcontentloaded' });
  49  |       await expect(page.locator('body')).toBeAttached();
  50  |       // Verify default values in controls
  51  |       await expect(page.locator('#rmin')).toHaveValue('0.12');
  52  |       await expect(page.locator('#rmax')).toHaveValue('2.5');
  53  |       await expect(page.locator('#dr')).toHaveValue('0.14');
  54  |       await expect(page.locator('#dzeta')).toHaveValue('0.09');
  55  |       await expect(page.locator('#qN')).toHaveValue('18');
  56  |       await expect(page.locator('#mode-row .pill.active')).toHaveAttribute('data-mode', 'omega');
  57  |     });
  58  | 
  59  |     test('Custom Parameters Parsing', async ({ page }) => {
  60  |       const query = '?rmin=0.25&rmax=3.2&dr=0.08&dzeta=0.15&qN=12&mode=sp1';
> 61  |       await page.goto(`${BRINGS_SURFACE_URL}${query}`, { waitUntil: 'domcontentloaded' });
      |                  ^ Error: page.goto: Test timeout of 180000ms exceeded.
  62  |       
  63  |       // Verify that controls reflect parsed URL parameters
  64  |       await expect(page.locator('#rmin')).toHaveValue('0.25');
  65  |       await expect(page.locator('#rmax')).toHaveValue('3.2');
  66  |       await expect(page.locator('#dr')).toHaveValue('0.08');
  67  |       await expect(page.locator('#dzeta')).toHaveValue('0.15');
  68  |       await expect(page.locator('#qN')).toHaveValue('12');
  69  |       await expect(page.locator('#mode-row .pill.active')).toHaveAttribute('data-mode', 'sp1');
  70  |     });
  71  |   });
  72  | 
  73  |   test.describe('Quantum Brings Surface (Placeholders)', () => {
  74  |     test('Default Happy-Path Load', async ({ page }) => {
  75  |       await page.goto(QUANTUM_BRINGS_SURFACE_URL, { waitUntil: 'domcontentloaded' });
  76  |       await expect(page.locator('body')).toBeAttached();
  77  |     });
  78  | 
  79  |     test('Custom Parameters Parsing (Placeholder Assertions)', async ({ page }) => {
  80  |       const query = '?rMin=0.35&rMax=2.8&deltaR=0.05&deltaZeta=0.08&N=15&projection=polar';
  81  |       await page.goto(`${QUANTUM_BRINGS_SURFACE_URL}${query}`, { waitUntil: 'domcontentloaded' });
  82  | 
  83  |       // Placeholder assertions that should fail if the elements are not present/implemented
  84  |       await expect(page.locator('#rMin')).toHaveValue('0.35');
  85  |       await expect(page.locator('#rMax')).toHaveValue('2.8');
  86  |       await expect(page.locator('#deltaR')).toHaveValue('0.05');
  87  |       await expect(page.locator('#deltaZeta')).toHaveValue('0.08');
  88  |       await expect(page.locator('#N')).toHaveValue('15');
  89  |       await expect(page.locator('#projection')).toHaveValue('polar');
  90  |     });
  91  |   });
  92  | 
  93  |   test.describe('Beta Decay Half-Life', () => {
  94  |     test('Default Happy-Path Load', async ({ page }) => {
  95  |       await page.goto(BETA_DECAY_HALFLIFE_URL, { waitUntil: 'domcontentloaded' });
  96  |       await expect(page.locator('body')).toBeAttached();
  97  |       await expect(page.locator('#sl-q')).toHaveValue('1.11');
  98  |       await expect(page.locator('#sel-nuc')).toHaveValue('0');
  99  |       await expect(page.locator('input[name=mode]:checked')).toHaveValue('from-q');
  100 |       await expect(page.locator('#cb-shell')).toBeChecked();
  101 |     });
  102 | 
  103 |     test('Custom Parameters Parsing', async ({ page }) => {
  104 |       const query = '?q=1.234&nucleus=1&mode=from-Qexp&shell=false';
  105 |       await page.goto(`${BETA_DECAY_HALFLIFE_URL}${query}`, { waitUntil: 'domcontentloaded' });
  106 | 
  107 |       await expect(page.locator('#sl-q')).toHaveValue('1.234');
  108 |       await expect(page.locator('#sel-nuc')).toHaveValue('1');
  109 |       await expect(page.locator('input[name=mode]:checked')).toHaveValue('from-Qexp');
  110 |       await expect(page.locator('#cb-shell')).not.toBeChecked();
  111 |     });
  112 |   });
  113 | 
  114 |   test.describe('Knot Periodic Table', () => {
  115 |     test('Default Happy-Path Load', async ({ page }) => {
  116 |       await page.goto(KNOT_PERIODIC_TABLE_URL, { waitUntil: 'domcontentloaded' });
  117 |       await expect(page.locator('body')).toBeAttached();
  118 |       await expect(page.locator('#color-mode')).toHaveValue('block');
  119 |       await expect(page.locator('#sl-q')).toHaveValue('1.11');
  120 |     });
  121 | 
  122 |     test('Custom Parameters & Placeholders Parsing', async ({ page }) => {
  123 |       const query = '?color=alexander&q=1.450&layout=grid&columns=8&filter=alternating';
  124 |       await page.goto(`${KNOT_PERIODIC_TABLE_URL}${query}`, { waitUntil: 'domcontentloaded' });
  125 | 
  126 |       await expect(page.locator('#color-mode')).toHaveValue('alexander');
  127 |       await expect(page.locator('#sl-q')).toHaveValue('1.45');
  128 | 
  129 |       // Placeholder assertions for layout, columns, filter to be implemented by other tracks
  130 |       await expect(page.locator('#layout-mode')).toHaveValue('grid');
  131 |       await expect(page.locator('#columns-input')).toHaveValue('8');
  132 |       await expect(page.locator('#filter-mode')).toHaveValue('alternating');
  133 |     });
  134 |   });
  135 | 
  136 | });
  137 | 
  138 | // ── TIER 2: BOUNDARY & CORNER CASES ────────────────────────────────────
  139 | test.describe('Tier 2: Boundary & Corner Cases', () => {
  140 | 
  141 |   test.describe('Brings Surface Boundary Checks', () => {
  142 |     test('Extremely Small Value & Clamping', async ({ page }) => {
  143 |       const query = '?rmin=0.0001&dr=0.00001';
  144 |       await page.goto(`${BRINGS_SURFACE_URL}${query}`, { waitUntil: 'domcontentloaded' });
  145 |       await expect(page.locator('#rmin')).toHaveValue('0.02');
  146 |       await expect(page.locator('#dr')).toHaveValue('0.02');
  147 |     });
  148 | 
  149 |     test('Invalid Parameter Types', async ({ page }) => {
  150 |       const query = '?rmin=banana&qN=xyz';
  151 |       await page.goto(`${BRINGS_SURFACE_URL}${query}`, { waitUntil: 'domcontentloaded' });
  152 |       await expect(page.locator('#rmin')).toHaveValue('0.12');
  153 |       await expect(page.locator('#qN')).toHaveValue('18');
  154 |     });
  155 |   });
  156 | 
  157 |   test.describe('Beta Decay Half-Life Boundary Checks', () => {
  158 |     test('Out of Bound Deformation Parameter', async ({ page }) => {
  159 |       await page.goto(`${BETA_DECAY_HALFLIFE_URL}?q=5.0`, { waitUntil: 'domcontentloaded' });
  160 |       await expect(page.locator('#sl-q')).toHaveValue('2');
  161 | 
```