# Reorganisation Map

**Purpose**: Track all chapter/section renames and block moves so that broken
downstream references (labels, `uses[]`, Lean imports, computation scripts)
can be traced to their current location.

---

## Directory renames (R5 — 2026-04)

All chapter directories had their `ch#-` prefix removed.  The paper manifest
`chapters[]` array defines the canonical order; chapter numbers are
auto-derived at runtime.

| Old directory | New directory | Old ch# | Auto-number |
|---------------|---------------|---------|-------------|
| `ch0-introduction` | `introduction` | 0 | — (tabLabel "I") |
| `ch1-quantum-observable-universe` | `quantum-universes` | 1 | 1 |
| `ch2-quantum-geometry` | `quantum-observable-universes` | 2 | 2 |
| `ch3-lifting-of-quantum-torsion` | `lifting-and-descent` | 3 | 3 |
| `ch4-path-integrals-and-braiding` | `braids-and-knots` | 4 | 4 |
| `ch5-brings-surface` | `descartes-universe` | 5 | 9 |
| `ch6-descartes-universe` | `models-of-qous` | 6 | 5 |
| `ch7-observations` | `observations` | 7 | 10 |
| `ch8-algebraic-substrate` | `algebraic-substrate` | 8 | 6 |
| `ch8-glossary` | `glossary` | 8g | — (tabLabel "G") |
| `ch9-information-theory` | `information-theory` | 9 | 8 |
| `ch10-fluid-dynamics` | `fluid-dynamics` | 10 | 7 |
| `ch10-organic-chemistry` | `organic-chemistry` | 10b | 11 |
| `ch11-q-geometric-langlands` | `q-geometric-langlands` | 11 | 12 |

### Other paper directories

| Old | New |
|-----|-----|
| `bach2013-double-slit/ch0-*` | `bach2013-double-slit/<slug>/` |
| `fred2005-formal-groups/ch0-*` | `fred2005-formal-groups/<slug>/` |
| `unital-groebner-bases/ch0-*, ch1-*, ch2-*` | `unital-groebner-bases/<slug>/` |
| `visualizer/ch0-*` | `visualizer/<slug>/` |

---

## Block moves (R1 — 2026-03)

| Block label | From chapter/section | To chapter/section | Reason |
|-------------|---------------------|--------------------|--------|
| `orbital-space-normal-bundle` | quantum-observable-universes | descartes-universe/sec:orbital-space | Forward-ref to braids-and-knots |
| `orbital-fourier-decomposition` | quantum-observable-universes | descartes-universe/sec:orbital-space | Forward-ref to braids-and-knots |
| `fivefold-symmetry` | quantum-observable-universes | descartes-universe/sec:fivefold-symmetry | Forward-ref to braids-and-knots |
| `cohomological-embedding` | quantum-observable-universes | descartes-universe/sec:fivefold-symmetry | Forward-ref to braids-and-knots |

---

## Block moves (R4, file moves — 2026-04)

| Block file set | From directory | To directory | Reason |
|----------------|---------------|--------------|--------|
| `orbital-space-normal-bundle.*` | quantum-observable-universes/ | descartes-universe/ | Manifest pointed here |
| `orbital-fourier-decomposition.*` | quantum-observable-universes/ | descartes-universe/ | Manifest pointed here |
| `fivefold-symmetry.*` | quantum-observable-universes/ | descartes-universe/ | Manifest pointed here |
| `cohomological-embedding.*` | quantum-observable-universes/ | descartes-universe/ | Manifest pointed here |
| 12 organic-chemistry blocks | observations/ | organic-chemistry/ | New organic-chemistry chapter |

---

## Section splits (proposals from content-graph analysis — 2026-04)

### P5 — `sec:brings-geometry` → 4 sections (descartes-universe)

| Old section | New section | Blocks |
|-------------|-------------|--------|
| `sec:brings-geometry` (31 blocks) | `sec:brings-surface-qou` | brings-surface, brings-surface-example, brings-realisations, brings-physics-interpretations, brings-is-qou, brings-is-qou-proof, brings-qou-4tuple, brings-qou-axiom-map, braid-group-action |
| | `sec:color-tube-coords` | color-tube-coordinates, aggregate-color-quantities, color-tube-constraints, color-tube-interpretation, c5-color-tube, intrinsic-color-cubic-pairing |
| | `sec:coral-fibration-elliptic` | coral-elliptic, coral-elliptic-proof, t-duality-elliptic, color-tube-cubic, color-tube-fibers, t-duality-color-tube, color-tube-subloci, pure-colour-sublocus |
| | `sec:brings-smoothness` | coral-bundles, brings-smoothness-resolution, brings-smoothness, briggs-klein-chart, radial-projection, four-colourability, four-colour-theorem, cyclotomic-reduction |

### P1 — `sec:vertex-operators-markov` → 4 sections (braids-and-knots)

| Old section | New section | Blocks |
|-------------|-------------|--------|
| `sec:vertex-operators-markov` (19 blocks) | `sec:exceptional-divisor-reeb` | exceptional-divisor, reeb-bundle, reeb-exceptional-divisor, vertex-operator, vertex-operator-dictionary |
| | `sec:vertex-factorisation` | vertex-is-exceptional-divisor, vertex-is-exceptional-divisor-proof, markov-trace-product, markov-trace-product-interpretation |
| | `sec:transfer-matrix-mass` | categorical-transfer-matrix, transfer-matrix-level-independence, transfer-matrix-level-independence-proof, topological-mass-formula, skein-decomposition, topological-field-ansatz |
| | `sec:braiding-relations` | skein-archimedean-shadow, vertex-algebra-relations, vertex-algebra-jet-relations, t211-ideal-annihilation |

### P2 — `sec:hadrons-knot-composites` → 3 sections (braids-and-knots)

| Old section | New section | Blocks |
|-------------|-------------|--------|
| `sec:hadrons-knot-composites` (20 blocks) | `sec:hadron-algebra` | hadron, hadron-interpretation, hadron-operations-closure, hadron-operations, knot-factorization, localized-hadron, hadron-fibre-embedding |
| | `sec:skein-particle-generation` | skein-generation, skein-generation-proof, knot-particle-generation, knot-particle-generation-interpretation, knot-particle-correspondence, knot-particle-dictionary |
| | `sec:bundle-observation` | quarks-borromean-picture, bundle-initial-conditions, observation-braid, sorting-color-energy, bundle-isotopy-equivalence, torsion-knot-flow, bundle-category |

### P4 — `sec:brane-fluid` → 3 sections (fluid-dynamics)

| Old section | New section | Blocks |
|-------------|-------------|--------|
| `sec:brane-fluid` (19 blocks) | `sec:q-hydrodynamics` | brane-fluid, madelung-fluid, hamilton-jacobi-phase, q-navier-stokes, geodesic-vortices, braid-fluid, planck-reynolds |
| | `sec:vortex-spectrum` | vortex-intensity-modes, discrete-vortex-spectrum, discrete-vortex-physical, helicity-conservation, helicity-physical, vortex-reconnection |
| | `sec:turbulence-acoustics` | q-turbulence-spectrum, q-turbulence-prediction, berry-vortex-moduli, kelvin-dispersion-derivation, kelvin-classical-limit, acoustic-horizon-conditions |

### P8 — `sec:small-scale` → 3 sections (observations)

| Old section | New section | Blocks |
|-------------|-------------|--------|
| `sec:small-scale` (21 blocks) | `sec:precision-tests` | photonic-hall, photonic-hall-data, fine-structure-observation, fine-structure-data, color-confinement-observation, lepton-discrepancies, lepton-anomalies-data |
| | `sec:proton-gravity-tests` | proton-radius-puzzle, proton-radius-data, entropic-gravity, entropic-gravity-data, local-substrate-q, local-substrate-q-proof |
| | `sec:crystal-resonance` | crystal-probe-q, substrate-telescope, magnetic-friction, crystal-resonance-data, lattice-layout, crystal-resonance-planned, crystal-resonance-experiments, bec-vortex-data |

### P9 — Merge `sec:orbital-space` + `sec:fivefold-symmetry` (descartes-universe)

| Old sections | New section | Blocks |
|-------------|-------------|--------|
| `sec:orbital-space` (2) + `sec:fivefold-symmetry` (2) | `sec:orbital-symmetry-embedding` | orbital-space-normal-bundle, orbital-fourier-decomposition, fivefold-symmetry, cohomological-embedding |

---

## Section merges (R2, R3 — 2026-03)

| Kind | Description |
|------|-------------|
| R2 | 4 single-block sparse sections → `sec:non-archimedean-models` in Models |
| R3 | `sec:jones-polynomials` (1 block) merged into `sec:finite-fields` in Models |

---

## How to use this map

If you encounter a broken reference like `ch5-brings-surface/foo`, look up:
1. `ch5-brings-surface` → `descartes-universe` (directory rename table)
2. Check if `foo` was moved to a different chapter (block moves table)
3. Check if its section was split/merged (section splits table)
