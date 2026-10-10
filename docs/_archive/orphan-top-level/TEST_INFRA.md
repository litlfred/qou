# Simulator E2E Test Infrastructure & Test Plan

This document outlines the 4-tier E2E test plan for the physical simulators in the Folio:
1. **Brings Surface** (`brings_surface.html`)
2. **Quantum Brings Surface** (`quantum_brings_surface.html`)
3. **Beta Decay Half-Life** (`beta_decay_halflife.html`)
4. **Knot Periodic Table** (`knot_periodic_table.html`)

---

## 4-Tier Test Plan

### Tier 1: Feature Coverage (Happy-Paths & Parameter Parsing)
Verify that each simulator loads successfully without Javascript errors or page crashes, and correctly reflects default and custom URL query parameters in the UI components.

#### A. Brings Surface
1. **Load Default**: Loads the page with no parameters; UI matches defaults, no errors.
2. **Custom Limits (`rmin`/`rmax`)**: Parses `rmin=0.1` and `rmax=2.5` and reflects them in the corresponding inputs.
3. **Custom Step (`dr`)**: Parses `dr=0.05` and sets the radial step.
4. **Custom Angle Step (`dzeta`)**: Parses `dzeta=0.1` and sets the zeta step.
5. **Custom Coefficient (`qN`)**: Parses `qN=5` and sets the surface order multiplier.
6. **Projection Mode (`projection`)**: Parses projection mode (`data-mode` under `#mode-row`).

#### B. Quantum Brings Surface
1. **Load Default**: Loads the page; UI matches defaults, no errors.
2. **Custom Limits (`rMin`/`rMax`)**: Parses custom `rMin=0.2` and `rMax=3.0` (reflected in UI).
3. **Custom Grid Steps (`deltaR`/`deltaZeta`)**: Parses steps for integration grid.
4. **Custom Dimension (`N`)**: Parses dimension/matrix size parameter.
5. **Projection Mode (`projection`)**: Sets the visualization projection style.

#### C. Beta Decay Half-Life
1. **Load Default**: Loads the page; UI matches defaults, no errors.
2. **Deformation Parameter (`q`)**: Parses `q=0.95` and sets the `#sl-q` slider.
3. **Target Nucleus (`nucleus`)**: Parses `nucleus=He6` and updates the `#sel-nuc` selector.
4. **Decay Mode (`mode`)**: Parses `mode=beta-minus` or `beta-plus` and updates the radio buttons.
5. **Shell Correction Toggle (`showShellCorrection`)**: Parses `showShellCorrection=true`/`false` and toggles `#cb-shell`.

#### D. Knot Periodic Table
1. **Load Default**: Loads the page; UI matches defaults, no errors.
2. **Color Mode (`color`)**: Parses `color=signature` and updates `#color-mode`.
3. **Parameter (`q`)**: Parses `q=0.98` and updates `#sl-q`.
4. **Layout Grid (`layout`)**: Parses grid/flex display layout.
5. **Columns Count (`columns`)**: Parses number of columns for grid.
6. **Filter Category (`filter`)**: Parses filter criterion (e.g. alternating, prime).

---

### Tier 2: Boundary & Corner Cases
Verify the resilience of simulators to extreme, out-of-bound, or malformed inputs.

#### A. Brings Surface
1. **Extremely small values**: `rmin=0.0001`, `dr=0.00001` (boundary precision test).
2. **Negative values**: `rmin=-1.0`, `dr=-0.1` (should clamp to minimum valid defaults or show error bounds).
3. **Invalid parameter types**: `rmin=banana`, `qN=xyz` (should fall back gracefully to default values).
4. **Out-of-bounds parameter**: `qN=9999` (extremely large order, should be clamped/restricted).
5. **Empty parameters**: `rmin=&rmax=&dr=` (should parse empty strings as defaults).

#### B. Quantum Brings Surface
1. **Extremely small steps**: `deltaR=0.0001`, `deltaZeta=0.0001`.
2. **Dimension bounds**: `N=0` or `N=-5` (dimension must be positive).
3. **Type mismatch**: `rMin=not-a-number`.
4. **Reversed limits**: `rMin=5.0&rMax=1.0` (should swap/correct or clamp limits).
5. **Extreme dimension**: `N=1000` (very high computational load; tests clamp/safety mechanisms).

#### C. Beta Decay Half-Life
1. **Extremely small deformation**: `q=0.000001`.
2. **Deformation out-of-bounds**: `q=50.0` or `q=-5.0` (should clamp within physical range $[0, 2]$).
3. **Non-existent nucleus**: `nucleus=Unobtainium250` (should default to standard nucleus).
4. **Invalid decay mode**: `mode=fission` (should default to `beta-minus` or default mode).
5. **Type mismatch shell correction**: `showShellCorrection=maybe` (should parse as false or default).

#### D. Knot Periodic Table
1. **Unsupported color mode**: `color=rainbow` (should default to standard color scheme).
2. **Deformation boundary**: `q=0.0` and `q=2.0` (extreme limits of deformation).
3. **Invalid column count**: `columns=-10` or `columns=1000` (should fall back to default or maximum/minimum columns).
4. **Invalid layout**: `layout=circular` (should default to standard layout).
5. **Non-existent filter**: `filter=complex-knots` (should not apply any filter or fall back to all).

---

### Tier 3: Cross-Feature / Pairwise Combinations
Verify behavior when multiple interrelated query parameters are specified simultaneously.

#### A. Brings Surface
- Combined: `rmin=0.5&rmax=1.5&dr=0.1&dzeta=0.2&qN=4&projection=isometric`
  Assert that all parameters are applied in unison and the surface renders correctly under custom resolution.

#### B. Quantum Brings Surface
- Combined: `rMin=0.3&rMax=2.2&deltaR=0.02&deltaZeta=0.05&N=10&projection=polar`
  Assert that the quantum state solver resolves with the specified grid resolution.

#### C. Beta Decay Half-Life
- Combined: `q=0.85&nucleus=C14&mode=beta-minus&showShellCorrection=true`
  Assert that the calculation computes half-life using shell correction and the specified nucleus.

#### D. Knot Periodic Table
- Combined: `color=alexander&q=0.9&layout=grid&columns=6&filter=alternating`
  Assert that only alternating knots are rendered in a 6-column grid using Alexander-polynomial-based coloring.

---

### Tier 4: Real-World Application Scenarios
Simulate sequential user actions and workflows.

1. **Simulated Teaching Session**:
   - User loads `brings_surface.html` with an isometric projection.
   - User updates the radial steps and notes rendering performance.
   - User toggles projection styles.
2. **Isotope Stability Investigation**:
   - User compares half-lives of Carbon-14, Hydrogen-3, and Helium-6.
   - The test loads the simulator successively with different `nucleus` parameters and toggles `showShellCorrection` to verify recalculated values in the UI.
3. **Knot Classification Session**:
   - User filters the table to show prime knots, then alters the $q$-deformation parameter.
   - The test verifies the UI layout updates dynamically as filters and $q$-slider are manipulated.

---

## Infrastructure Setup

Tests are run using **Playwright** via **Bun**.

### Commands
- Run E2E tests: `bun run test:e2e`
- Interactive UI mode: `bunx playwright test --ui`
