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

## Block moves (R6 — 2026-05-22, detangler P30 + P34 + P35)

### P30 — `thm:topological-mass` moved earlier (braids-and-knots → lifting-and-descent)

- **Source:** `braids-and-knots/sec:categorical-mass-foundations`.
- **Target:** `lifting-and-descent/sec:archimedean-lifting`, between `quantum-dilogarithm-proof` and `topological-mass-conjecture`.
- **Files moved:** `topological-mass.ts`, `topological-mass.md`, `topological-mass.lean`, `topological-mass.qa.json` (via `git mv`, history preserved).
- **Story:** the section already houses the theorem's proof (`topological-mass-proof`), conjecture-extension (`topological-mass-conjecture`), and a full family of eigenspace / holonomy / transient / dilogarithm variants. Reuniting the theorem statement with its proof and variants is the canonical home. Eliminates 8 H1 forward refs.
- **Wall-direction:** `lifting-and-descent` sits before `braids-and-knots` in the paper manifest, so this is a move-earlier. The theorem's `uses[]` has no dependency back into `braids-and-knots`, so no new H2 forward edges emitted.
- **Lean:** the `.lean` namespace `QOU.Torsion` stays unchanged; Lake builds the library tree under `content/quantum-observable-universe/lean/`, not chapter-dir siblings, so the file move is transparent to the Lake build.
- **Watcher:** detangler-integration-watcher, branch `claude/amazing-hopper-c0MLc`, PR #884.

### P34 — `def:motivic-substrate` moved earlier (braids-and-knots → lifting-and-descent)

- **Source:** `braids-and-knots/sec:classical-limit`.
- **Target:** `lifting-and-descent/sec:yekutieli-lifting`, immediately before `motivic-galois-character`.
- **Files moved:** `motivic-substrate.ts`, `motivic-substrate.md`, `motivic-substrate.lean`, `motivic-substrate.qa.json` (via `git mv`).
- **Story:** the substrate of the classical-limit functor naturally lives alongside its motivic-Galois consumers (`motivic-galois-character`, `qou-motivic-galois-instance`) which already sit in `sec:yekutieli-lifting`. Eliminates 7 H1 forward refs.
- **Wall-direction:** move-earlier; the definition's `uses[]` are all in chapters before `lifting-and-descent`, so no new H2 emitted.
- **Lean:** namespace preserved across the file move.
- **Watcher:** detangler-integration-watcher, branch `claude/amazing-hopper-c0MLc`, PR #884.

### P35 — `conj:gb-depth-period-correspondence` moved earlier within braids-and-knots

- **Source:** `braids-and-knots/sec:classical-limit` (graded-Mikusiński / joint-Galois-braid machinery sub-section).
- **Target:** `braids-and-knots/sec:archimedean-realization-kashaev`, immediately before `vc-as-depth-2-instance`.
- **Story:** the conjecture is the keystone (depth-period correspondence between GS-depth and Goncharov periods); its downstream consumers in §D-archimedean-realization (`vc-as-depth-2-instance`, `bring-figure-eight-depth-2-witness`) plus the §classical-limit graded-Mikusiński machinery (`hq-bi-filtration`, `joint-galois-braid-action`, `two-filtration-bridge`, …) all sit AFTER it now. Eliminates 7 H1 forward refs.
- **Wall-direction:** intra-chapter, no cross-wall move. The conjecture's `uses[]` (`def:archimedean-realization-functor`, `prop:archimedean-functor-uniqueness`, `prop:q-dilogarithm-exists`, `prop:quantum-dilogarithm-stratified`, `prop:curvature-rank-gb-stratification`, `prop:categorical-laplace-unique`, `def:q-resolvent`, `lem:surreal-squeeze`, `rem:figure-8-archimedean-illustration`, `rem:algebraic-core-survives`) all live in earlier §D-§E sections within the same chapter, so no new H2 emitted.
- **Watcher:** detangler-integration-watcher, branch `claude/amazing-hopper-c0MLc`, PR #884.

### P28, P29, P31, P32, P33, P36, P37 — executed with new H2 accepted as architectural

After Slot F batch ask (2026-05-22), all 7 risky cluster-1 moves executed with their new H2 forward edges recorded as `wontfix:architectural` in [`2026-05-19-detangler-architectural-acceptances.md §5`](coordination/2026-05-19-detangler-architectural-acceptances.md). Files moved: the four content-pipeline siblings (`.ts`, `.md`, `.lean`, `.qa.json`) per block via `git mv` to preserve history.

| PID | Block | From | To | H1↓ proposal | Cited deps now backward |
|---|---|---|---|---:|---|
| **P28** | `prop:operator-selection-lp` | particle-interactions/sec:confinement-selection | braids-and-knots/sec:hoefsmit-convergence-atomic | 14 | `prop:confinement-lp` @ particle-interactions |
| **P29** | `prop:gb-spectral-sequence` | braids-and-knots/sec:spectral-sequence-chirality-confinement | lifting-and-descent/sec:mass-brane | 12 | `prop:graded-trace-residue-split`, `thm:knot-mass-formula-unified` @ braids-and-knots |
| **P31** | `thm:markov-trace-factorization` | particle-interactions/sec:groebner-engine | braids-and-knots/sec:phi-q-markov-schur-weyl-tower | 8 | `prop:generator-volume-decomposition` @ particle-interactions |
| **P32** | `def:atomic-braid` | particle-interactions/sec:atomic-braid-mass | braids-and-knots/sec:skein-particle-generation | 8 | `def:transfer-matrix-operator`, `def:derived-atom` @ particle-interactions |
| **P33** | `prop:confinement-sdp` | particle-interactions/sec:confinement-selection | braids-and-knots/sec:alpha-k-procedure | 7 | `prop:confinement-lp` @ particle-interactions |
| **P36** | `prop:sw-period-thimble-equivalence` | descartes-universe/sec:topological-mass-spectrum | braids-and-knots/sec:kashiwara-jones-quantum-dilog | 6 | `rem:picard-lefschetz-thimble`, `prop:baryon-product-from-alt`, +1 @ descartes-universe |
| **P37** | `prop:lagrange-resolvent-transform` | descartes-universe/sec:bring-algebraic-substructure | braids-and-knots/sec:braid-involutions | 6 | `def:brings-surface` @ descartes-universe |

**Actual graph delta (post-execution):** H1 685 → 620 (↓65 combined with P30/P34/P35); H2 unchanged (the predicted 11 new H2 edges did not surface as findings — likely the analyzer's H2 detector applies a filter that absorbs the consumer→producer reference pattern these moves create, or the cited deps are themselves earlier than the new home in the cross-chapter order). Either way: net positive on H1, no new H2 violations introduced. Acceptance §5 stands as a documented exception in case future analyzer changes re-surface the edges.

**Lean:** namespaces preserved across all 7 file moves; Lake builds the library tree under `content/quantum-observable-universe/lean/` independently of chapter-dir siblings.

**Watcher:** detangler-integration-watcher, branch `claude/amazing-hopper-c0MLc`, PR #884.

---

## Section splits (R6 — 2026-05-23, detangler cluster-4 closure)

After Slot F batch approval (2026-05-23), the 13 remaining cluster-4 dense sections were split (12 executed here + P12 sec:archimedean-models already done on main via ch5/audit Rec 1-3 commits `2c722cae0` + `737deea6f` + `b2dea4d5b` + `4829571fc`). Each split adds 1-2 new opening prose blocks per Slot F template and replaces the dense section with K new sections each in the 3-18 block band.

| PID | Original section | Chapter | Split | New sections |
|---|---|---|---|---|
| P1 | sec:differential-structures (20) | quantum-observable-universes | 2-way | -reeb (11) + -fiber-adjoint (10) |
| P2 | sec:q-special-functions (19) | quantum-observable-universes | 2-way | -exp-log (13) + -dilog (7) |
| P3 | sec:yekutieli-lifting (22) | lifting-and-descent | 2-way | -construction (14) + -kummer-motivic (9) |
| P4 | sec:archimedean-lifting (25) | lifting-and-descent | 3-way | -foundations (10) + -topological-mass-formula (5) + -topological-mass-variants (12) |
| P5 | sec:categorical-braiding (19) | braids-and-knots | 2-way | -action (8) + -hecke-eigenbasis (12) |
| P6 | sec:vertex-factorisation (23) | braids-and-knots | 2-way | -markov (12) + -feynman (13) |
| P7 | sec:categorical-mass-foundations (22) | braids-and-knots | 2-way | -eigenspaces (14) + -markov-trace-endomorphism (9) |
| P8 | sec:hoefsmit-convergence-atomic (21) | braids-and-knots | 2-way | -construction (11) + -magic-shells (11) |
| P9 | sec:phi-q-markov-schur-weyl-tower (20) | braids-and-knots | 2-way | -foundations (11) + -residue-habiro (10) |
| P10 | sec:plancherel-alpha-ribbon (19) | braids-and-knots | 2-way | -spectral (10) + -knot-factor-mass-tower (10) |
| P14 | sec:atomic-shells (22) | descartes-universe | 2-way | -foundations (14) + -element-instances (9) |
| P16 | sec:atomic-braid-mass (21) | particle-interactions | 2-way | -foundations (13) + -crossing-locality-cpt (10) |
| P12 | sec:archimedean-models (22) | models-of-qous | **done on main** (ch5/audit Rec 1-3, 2026-05-22) — split into 8 sub-sections (sec:physical-interpretation, sec:headline-conjectures, sec:archimedean-witnesses, sec:categorical-differential-bridge, sec:non-archimedean-models, sec:witt-vector-lifting, sec:finite-fields, sec:archimedean-encounter) + 4 blocks moved to descartes-universe/sec:physical-regimes | — |

**Cross-ref fix:** `exceptional-divisor-reeb-intro.md` updated `#sec:vertex-factorisation` → `#sec:vertex-factorisation-markov` after P6 split renamed the target.

**Naming convention:** all 24 new section labels above use descriptive suffixes (`-foundations`, `-construction`, `-implications`, `-curvature`, `-spectral`, `-magic-shells`, `-eigenspaces`, `-element-instances`, `-crossing-locality-cpt`, etc.), satisfying the Slot I "No new `generic-section-name`" invariant.

**Graph delta vs the pre-PR-#948 baseline (post-rebase onto current main):**
- H5 dense sections: 12 → 0 (**↓12** — full cluster-4 closure across this PR + PR #884's 5 splits + ch5/audit's P12)
- H7 remark-ratio: 45 → 50 (↑5 from 13 new opening prose blocks; within ±20% Slot E defer band)
- H1 / H2 / H3 / H4 / H6: unchanged (splits are intra-chapter manifest restructures only)

**Watcher:** detangler-integration-watcher, branch `claude/detangler-cluster4-remaining-2026-05-23`, PR #948.

**Cluster-4 closure:** 18 of 18 cluster-4 H5 dense findings now resolved.

---

## Section splits (proposals from content-graph analysis — 2026-04)

### P5 — `sec:brings-geometry` → 4 sections (descartes-universe)

| Old section | New section | Blocks |
|-------------|-------------|--------|
| `sec:brings-geometry` (31 blocks) | `sec:brings-surface-qou` | brings-surface, brings-surface-example, brings-realisations, brings-physics-interpretations, brings-is-qou, brings-is-qou-proof, brings-qou-4tuple, brings-qou-axiom-map, braid-group-action |
| | `sec:color-tube-coords` | color-tube-coordinates, aggregate-color-quantities, color-tube-constraints, color-tube-interpretation, c5-color-tube, intrinsic-color-cubic-pairing |
| | `sec:color-fibration-elliptic` | color-elliptic, color-elliptic-proof, t-duality-elliptic, color-tube-cubic, color-tube-fibers, t-duality-color-tube, color-tube-subloci, pure-colour-sublocus |
| | `sec:brings-smoothness` | color-bundles, brings-smoothness-resolution, brings-smoothness, briggs-klein-chart, radial-projection, four-colourability, four-colour-theorem, cyclotomic-reduction |

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

## Chapter dissolutions (D1, D2 — 2026-05)

Two chapters dissolved entirely; their blocks redistributed across
other chapters to reduce cross-chapter coupling and place content
with its natural consumers.

### D1 — `encounter` chapter dissolved (8 blocks)

`encounter` was a narrative bridge between `particle-interactions`
and `descartes-universe`. Zero reverse refs from the rest of the
paper, so redistribution was trivial.

| Block | Destination |
|-------|-------------|
| `encounter-intro` (prose)             | DROPPED |
| `approach-to-exceptional-divisor`     | `descartes-universe / sec:brings-smoothness` |
| `thurston-relaxation`                 | `descartes-universe / sec:brings-smoothness` |
| `sdp-as-thimble-flow`                 | `particle-interactions / sec:confinement-selection` |
| `prop:mostow-confinement`             | `models-of-qous / sec:archimedean-encounter` (new) |
| `rem:algebraic-geometric-rigidity-pairing` | `models-of-qous / sec:archimedean-encounter` |
| `rem:encounter-literature-bridge`     | `models-of-qous / sec:archimedean-encounter` |
| `rem:pre-tau-vs-post-tau`             | `braids-and-knots / sec:calibration-algebraic-mass` |

### D2 — `algebraic-substrate` chapter dissolved (49 blocks + 2 orphans)

5 loosely-linked sections under an "algebraic substrate" umbrella
that did not tell a single story.

| Source section | Blocks | Destination |
|----------------|-------:|-------------|
| §1 `sec:algebraic-substrate-reeb` | 12 | `quantum-observable-universes / sec:algebraic-substrate-reeb` (new) |
| §2 `sec:cohomological-defect` | 7 | `descartes-universe / sec:cohomological-defect` (new) |
| §3 `sec:spectral-trace-tannaka` | 7 | `q-geometric-langlands / sec:q-gl-spectral-trace-tannaka` (new) |
| §4 `sec:weil-bound-stability` | 6 | `q-geometric-langlands / sec:q-gl-weil-bound-stability` (new) |
| §5 surreal-bound subset | 17 | `appendix-surreals / sec:surreal-rate-calculus` + `sec:millennium-bounds-via-surreals` (new) |
| §5 non-surreal subset | 23 | `braids-and-knots / sec:classical-limit` (new) |
| (orphan files: `categorical-higgs-idempotent`, `g-action-on-substrate`) | 2 | `quantum-observable-universes/` (orphan files, not wired into manifest pending dependency resolution) |

`appendix-surreals.ts` was patched to add `label:` fields to its 10
existing sections (previously invisible to the content-graph audit).
A new **surreal-notation cheat-sheet remark**
(`rem:surreal-notation-cheat-sheet`) was added at
`braids-and-knots / sec:classical-limit`, immediately before
`def:reeb-epsilon`, with a one-page reading aid for $\omega$,
$\varepsilon$, $\mathrm{st}$, $b(x)$, $\{L\mid R\}$,
$\mathrm{ord}_\omega$, $\sim$, $\prec$ — sufficient for substrate-
level uses in the main paper. The remark forwards to `app:surreals`
for the full formalism.

### Result

- Total chapters: 25 → 23
- Cross-chapter forward edges: 215 → **205** (−10)
- Forward-edge energy (Σ spans): 872 → **603** (**−31%**)

Achieved by (a) dissolution placing blocks with their consumers
(§5 → braids where it has 32 outgoing edges; §3+§4 → q-GL where
Tannaka-Krein is natural; §1 → QOU where readers first need
substrate parameter), and (b) the parallel chapter reorder
(intro before notation, physics narrative
braids → models → descartes → particles → observations →
mol → organic placed sequentially, fluid/info/q-GL moved to
trailing part).

## How to use this map

If you encounter a broken reference like `ch5-brings-surface/foo`, look up:
1. `ch5-brings-surface` → `descartes-universe` (directory rename table)
2. Check if `foo` was moved to a different chapter (block moves table)
3. Check if its section was split/merged (section splits table)
