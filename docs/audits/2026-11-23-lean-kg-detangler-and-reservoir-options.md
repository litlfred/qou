# Lean 4 Knowledge-Graph Detangler & Reservoir `lean_lib` Architecture Options (`qou-kgdt` + `qou-mlib`)

- **Date:** `2026-11-23`
- **Epic / Beans:** `qou-lnkg` (`qou-kgdt`, `qou-lskl`, `qou-mlib`; gates `qou-lref` & `qou-lanx`)
- **Instrument:** `scripts/lean-kg-detangler.py` (deterministic static DAG + §7c + QOU-purity analyzer, `11.692s` wall time)
- **Machine-readable companion:** `docs/audits/2026-11-23-lean-kg-detangler-and-reservoir-audit.json`
- **Scope Gate:** Stage 1 + Stage 1b + Stage 2 options readiness ONLY — **zero `.lean` files moved or renamed** pending owner selection via `AskUserQuestion`.

---

## 1. Executive Summary & `Process_GraphDetanglement` Gate Measurements

Following `cat-harness/processes/kg/graph-detanglement.bpmn` (`Process_GraphDetanglement`), we measure the **unassigned column FIRST** before reading cross-edge counts:

| Gate / Metric | Measured Value | Status / Interpretation |
|---|---:|---|
| Total `.lean` files in `folio/quantum-observable-universe/` | **4,804** | `3,897` in `lean/` + `907` content-block siblings (`+47` `UGB`, `+3` `Fred2005`) |
| Fragmented `lean/QOU/*` subdirectories + loose root files | **19 dirs + 0 loose** | Grew from `78` to `83` ad-hoc dirs under `QOU/` (`3,888` library modules, `70,915` decls) |
| `Task_Declare` — Unassigned library modules | **0** | `declared` (100% of `3,888` modules mapped to Tier-A, 6 Tier-B, or 12 `QOU.*` subgraphs) |
| `Task_Measure` — Unassigned resolved `import` edges | **0** | `5,441` internal `QOU` + `7,048` `Mathlib` + `2` `UGB` (`0` dangling) |
| Module-level `import` cycles (Tarjan SCC) | **0** | Module graph is strictly acyclic (`0` Lean module cycles) |
| Directory-level nontrivial SCCs across `83` `QOU/*` dirs | **1** |Largest directory SCC tangles `12` folders via `21` bidirectional folder pairs |
| Orphaned modules not reachable from `QOU.lean` | **1,851** (`47.61%`) | Built by `globs = ["QOU.+"]` (`qou-rc7b`), `41` reached by chapter `.lean` siblings, `1,176` unimported leaves |
| Intrinsically pure-math library modules (`0` QOU coupling) | **2,943** | **2,741** already cone-pure (`0` QOU deps transitively); **202** blocked only by cut-edges |
| Outbound cut-edges (`Tier-A / Tier-B -> QOU.*`) | **0** | Exact edges to prune/factor before zero-`QOU.*` `lean_lib` isolation (`GW_Detangled`) |
| Current `Mathlib`/`MathlibExt`/`MathlibInfra` upward leaks | **0** | Existing staging modules importing non-staging `QOU.*` directories |
| Library `sorry` / custom `axiom` counts | `0` body / `0` class / `3` `axiom` | Siblings: `9` body `sorry`, `0` §3b-cond class `sorry`, `39` `axiom` |

## 2. Purity & §7c Base-Ring Stratification

### 2.1 Mathematical vs. QOU-Physics Coupling (`3,840` Library Modules + `909` Siblings)

| Purity Tier | Library Modules | Transitive Cone Status | Content-Block Siblings | Definition |
|---|---:|---|---:|---|
| `pure_math` | **2,943** | `2,741` cone-pure + `202` cut-blocked | 554 | Zero `q0`/`substrate_q`, zero CODATA/decimals, zero particle/QOU-axiom types |
| `qou_categorical_core` | **830** | `830` | 294 | Uses QOU categorical/particle structures over generic rings; zero `q0` or CODATA |
| `qou_archimedean_model` | **33** | `33` | 6 | Evaluates at `substrate_q` / `q0` / `AlphaEM` without empirical decimal tables |
| `qou_empirical_comparison` | **82** | `82` | 53 | CODATA / MeV / decimal literals / experimental comparison boundaries |

### 2.2 §7c Base-Ring Generality Distribution

| §7c Ring Regime | Library Modules | Content-Block Siblings | Upstreaming / Hygiene Action |
|---|---:|---:|---|
| `pure_generic` (`[CommRing R]` / `[Field R]`) | **1,411** | 235 | Gold-standard §7c algebraic generality |
| `ordered_generic` (`[LinearOrderedField R]`, etc.) | **197** | 18 | Gold-standard §7c ordered generality (no `ℝ` lock-in) |
| `ring_agnostic` (combinatorics / `ℕ` / `ℤ` / categories) | **896** | 325 | Clean combinatorial / discrete / categorical modules |
| `archimedean_real` (justified `Real.sqrt`/`exp`/`log`/decimals) | **582** | 124 | Legitimate post-wall Archimedean analysis |
| `gratuitous_real_candidate` (`: ℝ` without transcendental ops) | **544** | 173 | Generalize `: ℝ` → `[CommRing R]` / `[LinearOrderedField R]` during Tier-A/B curation |
| `mixed_generic_and_real` (both `[CommRing R]` & `: ℝ` in 1 file) | **258** | 32 | Split generic theorem from `(R := ℝ)` instantiation per §7c wall rule |

## 3. Tier-A (`Mathlib4` Core) & Tier-B (6 Standalone Lean Reservoir `lean_lib` Packages)

| Target Library | Total Modules | Cone-Pure Ready Now | Cut-Blocked Pure | Decls (`thm`/`lem`) | Body `sorry` / `axiom` | Outbound Cut-Edges to `QOU.*` | Inbound `QOU` Consumers | `.ts` `lean.ref`s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `TierA.MathlibExt` | **301** | **301** | 0 | 4,062 (3,109) | 0 / 0 | **0** | 281 | 0 |
| `TierB.HeckeTemperleyLieb` | **495** | **495** | 0 | 6,733 (4,860) | 0 / 0 | **0** | 439 | 0 |
| `TierB.TwistedFrobeniusHopf` | **24** | **24** | 0 | 420 (268) | 0 / 0 | **0** | 16 | 0 |
| `TierB.ToricConicOpt` | **19** | **19** | 0 | 300 (191) | 0 / 0 | **0** | 8 | 0 |
| `TierB.CompactQuantumMetrics` | **17** | **17** | 0 | 327 (230) | 0 / 0 | **0** | 13 | 0 |
| `TierB.QCalculus` | **91** | **91** | 0 | 928 (769) | 0 / 0 | **0** | 47 | 0 |
| `TierB.BraidKnotOctonion` | **833** | **833** | 0 | 16,201 (11,254) | 0 / 0 | **0** | 229 | 0 |

> **Companion Already-Extracted Reservoir Package:** `folio/unital-groebner-bases/lean/` (`UGB`, **47 `.lean` files**) already provides standalone Gröbner–Shirshov / Kang–Lee–Lee–Oh / Splay PBW infrastructure with zero `QOU.*` imports (`qou` requires `ugb` via `[[require]]`). `HeckeTemperleyLieb` either layers cleanly on `ugb` or re-exports its `HeckeGS` bridge.

### 3.1 Package Scope & Representative Modules

- **`TierA.MathlibExt`** (301 modules; 301 immediately zero-`QOU` cone-pure): Selective Mathlib4 Core PR Staging (List/sort/foldl, general matrix/trace, ordered-field/sqrt/convexity, Borel/Dirichlet/Cech general lemmas).
  - *Primary current folders:* `{"MathlibExt": 301}`
  - *Sample modules:* `MathlibExt.AlgebraTowerColimit`, `MathlibExt.AlienBridgeEquation`, `MathlibExt.AlienDerivation`, `MathlibExt.AlternatingZetaTwo`, `MathlibExt.AntiInvolutionPalindrome`, `MathlibExt.ArgumentPrinciple`
- **`TierB.HeckeTemperleyLieb`** (495 modules; 495 immediately zero-`QOU` cone-pure): Iwahori-Hecke H_n(q), Temperley-Lieb TL_n(q), Jones/Markov/Ocneanu traces, Hoefsmit seminormal irreps, Young/SYT & Grobner-Shirshov normal forms.
  - *Primary current folders:* `{"HeckeTemperleyLieb": 495}`
  - *Sample modules:* `HeckeTemperleyLieb.A3BranchingModulusReflection`, `HeckeTemperleyLieb.AddableBoxHookOneRow`, `HeckeTemperleyLieb.Algebra`, `HeckeTemperleyLieb.AntisymmetricCasimirIsTwoBody`, `HeckeTemperleyLieb.AvgCrossing`, `HeckeTemperleyLieb.AxialDistanceBound`
  - *Inter-community `lean_lib` deps:* `{"TierA.MathlibExt": 42, "TierB.CompactQuantumMetrics": 2, "TierB.TwistedFrobeniusHopf": 1}`
- **`TierB.TwistedFrobeniusHopf`** (24 modules; 24 immediately zero-`QOU` cone-pure): Nakayama-twisted Frobenius algebras, Sweedler H_4 & Taft Hopf algebras, Higman norm map, ambidextrous & tower adjunctions.
  - *Primary current folders:* `{"TwistedFrobeniusHopf": 24}`
  - *Sample modules:* `TwistedFrobeniusHopf.BlockMeasureFromFrobeniusPairing`, `TwistedFrobeniusHopf.DepthStratifiedFrobeniusReciprocity`, `TwistedFrobeniusHopf.FrobeniusFormScaleFree`, `TwistedFrobeniusHopf.FrobeniusPairingCategorical`, `TwistedFrobeniusHopf.FrobeniusPositivityPredicate`, `TwistedFrobeniusHopf.FrobeniusSchurExpectationCancellation`
  - *Inter-community `lean_lib` deps:* `{"TierA.MathlibExt": 2}`
- **`TierB.ToricConicOpt`** (19 modules; 19 immediately zero-`QOU` cone-pure): Sturmfels-Thomas toric Grobner chambers, Graver/universal Grobner bases, Birch toric equilibria, symmetry-reduced LP/SDP dual certificates & kinks.
  - *Primary current folders:* `{"ToricConicOpt": 19}`
  - *Sample modules:* `ToricConicOpt.ChainReaction`, `ToricConicOpt.ConcaveOnSum`, `ToricConicOpt.ConfinementLayerTower`, `ToricConicOpt.EDMultiplier`, `ToricConicOpt.GramNearness`, `ToricConicOpt.L6a4AngleStructure`
  - *Inter-community `lean_lib` deps:* `{"TierA.MathlibExt": 2}`
- **`TierB.CompactQuantumMetrics`** (17 modules; 17 immediately zero-`QOU` cone-pure): Finite-dimensional Rieffel-Connes compact quantum metric spaces, Lipschitz seminorms, Kantorovich-Rubinstein duality, Woronowicz O_q(SU(2)) calculus.
  - *Primary current folders:* `{"CompactQuantumMetrics": 17}`
  - *Sample modules:* `CompactQuantumMetrics.AlgebraicGnsEmbedding`, `CompactQuantumMetrics.Bicommutant`, `CompactQuantumMetrics.BlockSDPNondegeneracy`, `CompactQuantumMetrics.DerivationIterateLeibniz`, `CompactQuantumMetrics.DerivationRankNullity`, `CompactQuantumMetrics.FiniteRieffelQuantumMetric`
  - *Inter-community `lean_lib` deps:* `{"TierA.MathlibExt": 1, "TierB.ToricConicOpt": 1}`
- **`TierB.QCalculus`** (91 modules; 91 immediately zero-`QOU` cone-pure): q-numbers [n]_q, Gaussian binomials, Thomae-Jackson q-integrals & lattices, q-exponentials, Faddeev/quantum dilogarithms, Habiro cyclotomic rings.
  - *Primary current folders:* `{"QCalculus": 91}`
  - *Sample modules:* `QCalculus.BWVacuumRowHabiroBoundaryData`, `QCalculus.BWVacuumRowHabiroRigidity`, `QCalculus.BindingHabiroDenominators`, `QCalculus.BindingHabiroNumeratorTower`, `QCalculus.BindingQGaussianHabiro`, `QCalculus.BraidKnot.QuantumDilogarithm`
  - *Inter-community `lean_lib` deps:* `{"TierA.MathlibExt": 31}`
- **`TierB.BraidKnotOctonion`** (833 modules; 833 immediately zero-`QOU` cone-pure): Artin braid groups B_n, Burau/Lawrence-Krammer/Alexander invariants, PL knot Delta-equivalence & Moise assembly, octonion/Hurwitz/G_2 & Bring curve.
  - *Primary current folders:* `{"BraidKnotOctonion": 833}`
  - *Sample modules:* `BraidKnotOctonion.A3OperatorCombinerMagnitude`, `BraidKnotOctonion.A5NoSixDim`, `BraidKnotOctonion.AJFigureEight`, `BraidKnotOctonion.AJFigureEightAnnihilation`, `BraidKnotOctonion.AJFigureEightCertificate`, `BraidKnotOctonion.AJFigureEightTelescope`
  - *Inter-community `lean_lib` deps:* `{"TierA.MathlibExt": 87, "TierB.CompactQuantumMetrics": 1, "TierB.HeckeTemperleyLieb": 217, "TierB.QCalculus": 7, "TierB.ToricConicOpt": 3}`

### 3.2 Exact Cut-Edges Blocking Zero-`QOU.*` Extraction (`GW_Detangled` Action List)

Zero outbound cut-edges from Tier-A/Tier-B into `QOU.*`!

## 4. Directory-Level Tangle & Consolidation (`83` `QOU/*` Dirs -> `12` Canonical `QOU.*` Subgraphs)

### 4.1 Synonym-Directory Merge Clusters

| Synonym Cluster | Current Directories (`#`) | Total Files | Pure-Math Files Inside | Cross-Synonym Edges Eliminated | Remaining External Edges |
|---|---|---:|---:|---:|---:|
| `Braid_Knot_7dirs` | `BraidKnot` (0), `BraidsAndKnots` (347), `Knot` (0), `Braiding` (0), `KnotTheory` (0), `BraidsKnots` (0), `Knots` (0) | **347** | 118 | **0** | 281 |
| `Mass_7dirs` | `Mass` (0), `MassTheory` (712), `MassEndomorphism` (0), `WedderburnMass` (0), `TopologicalMass` (0), `HadronicMass` (0), `AtomicMass` (0) | **712** | 462 | **0** | 258 |
| `Hecke_3dirs` | `Hecke` (0), `IwahoriHecke` (0), `HeckeAlgebra` (0) | **0** | 0 | **0** | 0 |
| `Bring_3dirs` | `BringsSurface` (62), `Brings` (0), `HyperellipticQuintic` (0) | **62** | 35 | **0** | 7 |
| `QOU_Core_4dirs` | `QuantumObservableUniverse` (0), `QuantumObservableUniverses` (0), `QuantumUniverse` (0), `CommutativeQOU` (0) | **0** | 0 | **0** | 0 |
| `Eightfold_2dirs` | `Eightfold` (0), `EightfoldWay` (52) | **52** | 31 | **0** | 11 |
| `Information_2dirs` | `Information` (0), `InformationTheory` (54) | **54** | 31 | **0** | 19 |
| `Archimedean_2dirs` | `Archimedean` (0), `ArchimedeanUniverse` (0) | **0** | 0 | **0** | 0 |
| `Interactions_2dirs` | `Interactions` (0), `ParticleInteractions` (0) | **0** | 0 | **0** | 0 |
| `Fluid_2dirs` | `FluidDynamics` (45), `GaugeFieldFluidDynamics` (0) | **45** | 27 | **0** | 7 |
| `MathlibStaging_4dirs` | `MathlibExt` (301), `Mathlib` (0), `MathlibInfra` (0), `Infra` (0) | **301** | 301 | **0** | 0 |

### 4.2 Directory-Level SCC Tangles & Top Bidirectional Folder Pairs

- **Directory SCC #1 (12 directories mutually coupled):** `BraidsAndKnots`, `BringsSurface`, `Confinement`, `Core`, `EightfoldWay`, `FluidDynamics`, `InformationTheory`, `LiftingDescent`, `MassTheory`, `Nuclear`, `Observations`, `StandardModel`

| Dir A | Dir B | `A -> B` Imports | `B -> A` Imports | Min-Cut Back-Edges |
|---|---|---:|---:|---:|
| `BraidsAndKnots` | `MassTheory` | 9 | 20 | **9** |
| `MassTheory` | `Nuclear` | 9 | 16 | **9** |
| `Core` | `MassTheory` | 7 | 20 | **7** |
| `MassTheory` | `StandardModel` | 7 | 6 | **6** |
| `BraidsAndKnots` | `StandardModel` | 5 | 8 | **5** |
| `Confinement` | `MassTheory` | 14 | 4 | **4** |
| `BraidsAndKnots` | `Confinement` | 4 | 5 | **4** |
| `BraidsAndKnots` | `Core` | 29 | 3 | **3** |
| `BringsSurface` | `Core` | 3 | 20 | **3** |
| `Core` | `StandardModel` | 3 | 13 | **3** |
| `Nuclear` | `StandardModel` | 3 | 4 | **3** |
| `Core` | `LiftingDescent` | 2 | 10 | **2** |
| `LiftingDescent` | `MassTheory` | 2 | 3 | **2** |
| `Core` | `InformationTheory` | 1 | 10 | **1** |
| `BraidsAndKnots` | `Nuclear` | 1 | 8 | **1** |

### 4.3 Target `12` Canonical Monograph-Aligned `QOU.<Subgraph>` Partitions (After Extracting Tier-A & Tier-B)

| Canonical `QOU.*` Subgraph | Layer | QOU-Coupled Modules | Decls (`thm`/`lem`) | Body `sorry` / `axiom` | Inbound Edges | `.ts` `lean.ref`s | Consolidated Source Folders (Top) |
|---|---:|---:|---:|---:|---:|---:|---|
| `QOU.Core` | L8 | **253** | 3,770 (2,565) | 0 / 0 | 112 | 57 | `Confinement`:132, `Core`:121 |
| `QOU.LiftingDescent` | L9 | **63** | 791 (500) | 0 / 0 | 12 | 31 | `LiftingDescent`:63 |
| `QOU.BraidsAndKnots` | L10 | **347** | 18,031 (3,351) | 0 / 1 | 48 | 128 | `BraidsAndKnots`:347 |
| `QOU.BringsSurface` | L11 | **62** | 669 (469) | 0 / 0 | 32 | 11 | `BringsSurface`:62 |
| `QOU.Confinement` | L12 | **0** | 0 (0) | 0 / 0 | 0 | 0 |  |
| `QOU.EightfoldWay` | L12 | **52** | 784 (518) | 0 / 0 | 8 | 13 | `EightfoldWay`:52 |
| `QOU.MassTheory` | L13 | **712** | 8,811 (6,151) | 0 / 1 | 61 | 97 | `MassTheory`:712 |
| `QOU.Nuclear` | L14 | **336** | 5,160 (3,633) | 0 / 0 | 18 | 32 | `Nuclear`:336 |
| `QOU.StandardModel` | L14 | **92** | 1,931 (1,189) | 0 / 0 | 20 | 15 | `StandardModel`:92 |
| `QOU.FluidDynamics` | L14 | **45** | 463 (313) | 0 / 0 | 2 | 4 | `FluidDynamics`:45 |
| `QOU.InformationTheory` | L14 | **54** | 393 (266) | 0 / 0 | 3 | 8 | `InformationTheory`:54 |
| `QOU.Observations` | L15 | **92** | 1,141 (798) | 0 / 1 | 6 | 27 | `Observations`:92 |

## 5. Comparison of 3 Concrete Refactor Options (Ready for Coordinator `AskUserQuestion`)

| Dimension | **Option 1 (Recommended): Multi-`lean_lib` in `lakefile.toml`** | **Option 2: 6 Separate Lake Packages (`folio/lean-contrib/*`)** | **Option 3: Single-Lib Mirror (`QOU/Contrib/<Pkg>/*`)** |
|---|---|---|---|
| **Lake Target Architecture** | `MathlibExt` + 6 Tier-B `[[lean_lib]]` + `QOU` in `folio/quantum-observable-universe/lean/lakefile.toml` | 6 standalone `lakefile.toml` packages under `folio/lean-contrib/<pkg>/lean/` via `[[require]]` | Single `[[lean_lib]] name = "QOU"` with `QOU/Contrib/<Pkg>/*` folders |
| **`Process_GraphDetanglement` Stage** | **Stage 3 (`Isolate` in-place)** — 1-folder `git mv` away from Stage 4 extraction | **Stage 4 (`Extract` immediately)** — full multi-package split now | **Stage 2 (`Detangle` only)** — keeps `QOU.` namespace prefix |
| **Tier-B Reservoir Modules** | **1479** modules in root namespaces (`HeckeTemperleyLieb.*`, etc.) | **1479** modules in 6 new Lake packages | **1479** modules under `QOU.Contrib.<Pkg>.*` |
| **Tier-A `MathlibExt` Modules** | **301** modules (`MathlibExt.*`) | **301** modules (`MathlibExt.*`) | **301** modules (`QOU.MathlibExt.*`) |
| **Collapsed `QOU.*` Subgraphs** | `83 dirs + 106 loose` → **12 canonical `QOU.<Chapter>` dirs** (**2108** modules) | `83 dirs + 106 loose` → **12 canonical `QOU.<Chapter>` dirs** (**2108** modules) | `83 dirs + 106 loose` → **12 canonical `QOU.<Chapter>` dirs** (**2108** modules) |
| **Blocking Cut-Edges to Prune/Factor** | **0** (`Tier-A/B -> QOU.*`) | **0** (`Tier-A/B -> QOU.*`) | **0** (`Tier-A/B -> QOU.*`) |
| **Zero-`QOU.*` Boundary Enforcement** | `lake build <TierBLib>` + `lean-best-practices-lint.py --package` | Physical Lake package DAG (impossible to import `QOU.*`) + linter | Python linter (`lean-best-practices-lint.py`) only |
| **`import` Lines Rewritten (Codemod)** | ~5,854 (`QOU` + siblings) | ~5,854 (`QOU` + siblings) | ~5,854 (`QOU` + siblings) |
| **`.ts` `lean.ref` Updates** | ~1,324 (keeps `qou:<Decl>` package URI!) | ~1,324 + **6 new URI prefixes** in `schemas/lean-packages.ts` | ~1,324 (keeps `qou:QOU.Contrib...` URI) |
| **`.olean` Cache / Overlay Blast Radius** | **Low** (`0` new `.lake/build` roots; `lean-overlay-env.sh` works unchanged!) | **High** (`+6` `.lake/build/lib/lean` roots in `lean-env.sh`, overlay, & cache seeders) | **Lowest** (`0` new roots, single `QOU/` folder) |
| **Second Rename Needed for Reservoir?** | **No (0 files)** — namespaces are already Reservoir-final | **No (0 files)** | **Yes (1479 files)** must drop `QOU.Contrib.` later |
| **Estimated Effort** | **Medium (3-4 PR tranches after active Lean PRs land; 1 automated codemod + single olean reseed)** | High (5-6 PR tranches; requires updating `schemas/lean-packages.ts`, `lean-env.sh`, `lean-overlay-env.sh`, `lean-olean-cache-seed.sh`, and CI workflows for 6 new Lake build roots) | Low-Medium now (2-3 PR tranches), but incurs technical debt: every Tier-B declaration keeps a `QOU.Contrib.` prefix and requires a second breaking rename before Lean Reservoir publication. |

### Recommended Phased Execution Strategy (`qou-lref` -> `qou-lanx`)

1. **Adopt Option 1 now (`Isolate in-place`)** once active Lean PRs settle and the owner confirms via `AskUserQuestion`:
   - **Step 1 (Cut-edge surgical prep):** Resolve the **0** outbound `Tier-A/B -> QOU.*` cut-edges (`Task_Move`: factor pure base definitions out of `QOU.*` or reclassify pure targets) and re-run `scripts/lean-kg-detangler.py` until `community_to_qou_cut_edges == 0`.
   - **Step 2 (Atomic codemod + `[[lean_lib]]` isolation):** Move the 6 Tier-B subgraphs to top-level namespaces (`HeckeTemperleyLieb/`, `TwistedFrobeniusHopf/`, `ToricConicOpt/`, `CompactQuantumMetrics/`, `QCalculus/`, `BraidKnotOctonion/`) + `MathlibExt/` inside `folio/quantum-observable-universe/lean/`, collapse the remaining `QOU/*` tree into the `12` canonical chapter subgraphs, rewrite `import` and `lean.ref` strings atomically, and verify with `LEAN_NUM_THREADS=1 nice -n 15 bash scripts/lean-direct-cone.sh -j 1` + `scripts/lean-best-practices-lint.py`.
   - **Step 3 (Optional Stage 4 `Extract` to Option 2 per-library):** Whenever an individual Tier-B library (e.g., `TwistedFrobeniusHopf` or `CompactQuantumMetrics`) is ready for public Lean Reservoir indexing, `Task_Extract` lifts its already-isolated folder into a standalone repo with **zero namespace or theorem-name churn**.

