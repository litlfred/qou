# Lean 4 Knowledge-Graph Detangler & Reservoir `lean_lib` Architecture Options (`qou-kgdt` + `qou-mlib`)

- **Date:** `2026-11-23`
- **Epic / Beans:** `qou-lnkg` (`qou-kgdt`, `qou-lskl`, `qou-mlib`; gates `qou-lref` & `qou-lanx`)
- **Instrument:** `scripts/lean-kg-detangler.py` (deterministic static DAG + §7c + QOU-purity analyzer, `16.969s` wall time)
- **Machine-readable companion:** `docs/audits/2026-11-23-lean-kg-detangler-and-reservoir-audit.json`
- **Scope Gate:** Stage 1 + Stage 1b + Stage 2 options readiness ONLY — **zero `.lean` files moved or renamed** pending owner selection via `AskUserQuestion`.

---

## 1. Executive Summary & `Process_GraphDetanglement` Gate Measurements

Following `cat-harness/processes/kg/graph-detanglement.bpmn` (`Process_GraphDetanglement`), we measure the **unassigned column FIRST** before reading cross-edge counts:

| Gate / Metric | Measured Value | Status / Interpretation |
|---|---:|---|
| Total `.lean` files in `folio/quantum-observable-universe/` | **4,775** | `3,866` in `lean/` + `909` content-block siblings (`+47` `UGB`, `+3` `Fred2005`) |
| Fragmented `lean/QOU/*` subdirectories + loose root files | **84 dirs + 106 loose** | Grew from `78` to `83` ad-hoc dirs under `QOU/` (`3,864` library modules, `69,872` decls) |
| `Task_Declare` — Unassigned library modules | **0** | `declared` (100% of `3,864` modules mapped to Tier-A, 6 Tier-B, or 12 `QOU.*` subgraphs) |
| `Task_Measure` — Unassigned resolved `import` edges | **0** | `5,428` internal `QOU` + `6,927` `Mathlib` + `2` `UGB` (`0` dangling) |
| Module-level `import` cycles (Tarjan SCC) | **0** | Module graph is strictly acyclic (`0` Lean module cycles) |
| Directory-level nontrivial SCCs across `83` `QOU/*` dirs | **1** |Largest directory SCC tangles `40` folders via `68` bidirectional folder pairs |
| Orphaned modules not reachable from `QOU.lean` | **1,781** (`46.09%`) | Built by `globs = ["QOU.+"]` (`qou-rc7b`), `34` reached by chapter `.lean` siblings, `1,163` unimported leaves |
| Intrinsically pure-math library modules (`0` QOU coupling) | **2,931** | **2,729** already cone-pure (`0` QOU deps transitively); **202** blocked only by cut-edges |
| Outbound cut-edges (`Tier-A / Tier-B -> QOU.*`) | **0** | Exact edges to prune/factor before zero-`QOU.*` `lean_lib` isolation (`GW_Detangled`) |
| Current `Mathlib`/`MathlibExt`/`MathlibInfra` upward leaks | **51** | Existing staging modules importing non-staging `QOU.*` directories |
| Library `sorry` / custom `axiom` counts | `0` body / `0` class / `3` `axiom` | Siblings: `9` body `sorry`, `0` §3b-cond class `sorry`, `39` `axiom` |

## 2. Purity & §7c Base-Ring Stratification

### 2.1 Mathematical vs. QOU-Physics Coupling (`3,840` Library Modules + `909` Siblings)

| Purity Tier | Library Modules | Transitive Cone Status | Content-Block Siblings | Definition |
|---|---:|---|---:|---|
| `pure_math` | **2,931** | `2,729` cone-pure + `202` cut-blocked | 555 | Zero `q0`/`substrate_q`, zero CODATA/decimals, zero particle/QOU-axiom types |
| `qou_categorical_core` | **818** | `818` | 295 | Uses QOU categorical/particle structures over generic rings; zero `q0` or CODATA |
| `qou_archimedean_model` | **33** | `33` | 6 | Evaluates at `substrate_q` / `q0` / `AlphaEM` without empirical decimal tables |
| `qou_empirical_comparison` | **82** | `82` | 53 | CODATA / MeV / decimal literals / experimental comparison boundaries |

### 2.2 §7c Base-Ring Generality Distribution

| §7c Ring Regime | Library Modules | Content-Block Siblings | Upstreaming / Hygiene Action |
|---|---:|---:|---|
| `pure_generic` (`[CommRing R]` / `[Field R]`) | **1,406** | 235 | Gold-standard §7c algebraic generality |
| `ordered_generic` (`[LinearOrderedField R]`, etc.) | **189** | 18 | Gold-standard §7c ordered generality (no `ℝ` lock-in) |
| `ring_agnostic` (combinatorics / `ℕ` / `ℤ` / categories) | **894** | 325 | Clean combinatorial / discrete / categorical modules |
| `archimedean_real` (justified `Real.sqrt`/`exp`/`log`/decimals) | **581** | 124 | Legitimate post-wall Archimedean analysis |
| `gratuitous_real_candidate` (`: ℝ` without transcendental ops) | **543** | 175 | Generalize `: ℝ` → `[CommRing R]` / `[LinearOrderedField R]` during Tier-A/B curation |
| `mixed_generic_and_real` (both `[CommRing R]` & `: ℝ` in 1 file) | **251** | 32 | Split generic theorem from `(R := ℝ)` instantiation per §7c wall rule |

## 3. Tier-A (`Mathlib4` Core) & Tier-B (6 Standalone Lean Reservoir `lean_lib` Packages)

| Target Library | Total Modules | Cone-Pure Ready Now | Cut-Blocked Pure | Decls (`thm`/`lem`) | Body `sorry` / `axiom` | Outbound Cut-Edges to `QOU.*` | Inbound `QOU` Consumers | `.ts` `lean.ref`s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `TierA.MathlibExt` | **301** | **301** | 0 | 4,062 (3,109) | 0 / 0 | **0** | 281 | 5 |
| `TierB.HeckeTemperleyLieb` | **493** | **493** | 0 | 6,699 (4,829) | 0 / 0 | **0** | 437 | 8 |
| `TierB.TwistedFrobeniusHopf` | **24** | **24** | 0 | 420 (268) | 0 / 0 | **0** | 16 | 0 |
| `TierB.ToricConicOpt` | **19** | **19** | 0 | 300 (191) | 0 / 0 | **0** | 9 | 5 |
| `TierB.CompactQuantumMetrics` | **16** | **16** | 0 | 287 (210) | 0 / 0 | **0** | 12 | 1 |
| `TierB.QCalculus` | **91** | **91** | 0 | 928 (769) | 0 / 0 | **0** | 47 | 3 |
| `TierB.BraidKnotOctonion` | **830** | **830** | 0 | 16,029 (11,129) | 0 / 0 | **0** | 227 | 31 |

> **Companion Already-Extracted Reservoir Package:** `folio/unital-groebner-bases/lean/` (`UGB`, **47 `.lean` files**) already provides standalone Gröbner–Shirshov / Kang–Lee–Lee–Oh / Splay PBW infrastructure with zero `QOU.*` imports (`qou` requires `ugb` via `[[require]]`). `HeckeTemperleyLieb` either layers cleanly on `ugb` or re-exports its `HeckeGS` bridge.

### 3.1 Package Scope & Representative Modules

- **`TierA.MathlibExt`** (301 modules; 301 immediately zero-`QOU` cone-pure): Selective Mathlib4 Core PR Staging (List/sort/foldl, general matrix/trace, ordered-field/sqrt/convexity, Borel/Dirichlet/Cech general lemmas).
  - *Primary current folders:* `{"Mathlib": 118, "MathlibExt": 95, "QBeta": 19, "Archimedean": 16, "Mass": 14, "Common": 6, "MassTheory": 6, "RiemannSurface": 5, "<QOU-root-loose>": 4, "Infra": 4}`
  - *Sample modules:* `QOU.Archimedean.BlochWignerLobachevsky`, `QOU.Archimedean.ClausenFunctionMathlibFiller`, `QOU.Archimedean.ConstantOffOnePoint`, `QOU.Archimedean.DilogPartAConvergence`, `QOU.Archimedean.DilogPartARiemannSum`, `QOU.Archimedean.DilogPartBBoundarySeed`
- **`TierB.HeckeTemperleyLieb`** (493 modules; 493 immediately zero-`QOU` cone-pure): Iwahori-Hecke H_n(q), Temperley-Lieb TL_n(q), Jones/Markov/Ocneanu traces, Hoefsmit seminormal irreps, Young/SYT & Grobner-Shirshov normal forms.
  - *Primary current folders:* `{"BraidKnot": 76, "Machinery": 72, "Hecke": 66, "SchurWeyl": 63, "MathlibExt": 60, "Mathlib": 36, "Mass": 22, "QBeta": 20, "IwahoriHecke": 17, "Archimedean": 10}`
  - *Sample modules:* `QOU.Archimedean.GroundRing`, `QOU.Archimedean.HeckeBraidingSubstrateNonSymmetric`, `QOU.Archimedean.MarkovGramRealSymm`, `QOU.Archimedean.MarkovWeightValueTransport`, `QOU.Archimedean.MatrixSchurCommutant`, `QOU.Archimedean.OcneanuTwoThreeSubstrate`
  - *Inter-community `lean_lib` deps:* `{"TierA.MathlibExt": 42, "TierB.CompactQuantumMetrics": 2, "TierB.TwistedFrobeniusHopf": 1}`
- **`TierB.TwistedFrobeniusHopf`** (24 modules; 24 immediately zero-`QOU` cone-pure): Nakayama-twisted Frobenius algebras, Sweedler H_4 & Taft Hopf algebras, Higman norm map, ambidextrous & tower adjunctions.
  - *Primary current folders:* `{"LiftingDescent": 4, "BraidKnot": 3, "FrobeniusHopfData": 3, "MassTheory": 3, "AlgebraicSubstrate": 2, "ParticleInteractions": 2, "QuantumObservableUniverse": 2, "<QOU-root-loose>": 2, "Archimedean": 1, "FormalGroups": 1}`
  - *Sample modules:* `QOU.AlgebraicSubstrate.FrobeniusSchurExpectationCancellation`, `QOU.AlgebraicSubstrate.TwistedAmbidextrousAdjunction`, `QOU.Archimedean.frobenius_gram_matrix`, `QOU.BraidKnot.DepthStratifiedFrobeniusReciprocity`, `QOU.BraidKnot.NakayamaGradingObstruction`, `QOU.BraidKnot.frobenius_antipode_unifies`
  - *Inter-community `lean_lib` deps:* `{"TierA.MathlibExt": 2}`
- **`TierB.ToricConicOpt`** (19 modules; 19 immediately zero-`QOU` cone-pure): Sturmfels-Thomas toric Grobner chambers, Graver/universal Grobner bases, Birch toric equilibria, symmetry-reduced LP/SDP dual certificates & kinks.
  - *Primary current folders:* `{"Optimization": 9, "MathlibInfra": 3, "Knot": 2, "Mathlib": 2, "Archimedean": 1, "BraidKnot": 1, "MathlibExt": 1}`
  - *Sample modules:* `QOU.Archimedean.TypeBFoldedCrystalCombinatorics`, `QOU.BraidKnot.LpDualityHypothesisClass`, `QOU.Knot.L6a4AngleStructure`, `QOU.Knot.M004AngleStructure`, `QOU.Mathlib.LPDuality`, `QOU.Mathlib.SDPDuality`
  - *Inter-community `lean_lib` deps:* `{"TierA.MathlibExt": 2}`
- **`TierB.CompactQuantumMetrics`** (16 modules; 16 immediately zero-`QOU` cone-pure): Finite-dimensional Rieffel-Connes compact quantum metric spaces, Lipschitz seminorms, Kantorovich-Rubinstein duality, Woronowicz O_q(SU(2)) calculus.
  - *Primary current folders:* `{"MathlibExt": 11, "AlgebraicSubstrate": 1, "InformationTheory": 1, "MassTheory": 1, "Mathlib": 1, "Observations": 1}`
  - *Sample modules:* `QOU.AlgebraicSubstrate.OqSU2ModularNakayama`, `QOU.InformationTheory.FiniteRieffelQuantumMetric`, `QOU.MassTheory.BlockSDPNondegeneracy`, `QOU.Mathlib.SDPStrongDuality`, `QOU.MathlibExt.Bicommutant`, `QOU.MathlibExt.DerivationIterateLeibniz`
  - *Inter-community `lean_lib` deps:* `{"TierA.MathlibExt": 1, "TierB.ToricConicOpt": 1}`
- **`TierB.QCalculus`** (91 modules; 91 immediately zero-`QOU` cone-pure): q-numbers [n]_q, Gaussian binomials, Thomae-Jackson q-integrals & lattices, q-exponentials, Faddeev/quantum dilogarithms, Habiro cyclotomic rings.
  - *Primary current folders:* `{"QBeta": 35, "MathlibExt": 22, "Mathlib": 7, "BraidKnot": 6, "Mass": 6, "Machinery": 4, "Archimedean": 3, "Habiro": 3, "BraidsAndKnots": 1, "LiftingDescent": 1}`
  - *Sample modules:* `QOU.Archimedean.ComplexDilogBridge`, `QOU.Archimedean.DilogPartBFaddeevScaling`, `QOU.Archimedean.LiTwoNegOne`, `QOU.BraidKnot.BWVacuumRowHabiroBoundaryData`, `QOU.BraidKnot.BWVacuumRowHabiroRigidity`, `QOU.BraidKnot.HabiroDomainVanishing`
  - *Inter-community `lean_lib` deps:* `{"TierA.MathlibExt": 31}`
- **`TierB.BraidKnotOctonion`** (830 modules; 830 immediately zero-`QOU` cone-pure): Artin braid groups B_n, Burau/Lawrence-Krammer/Alexander invariants, PL knot Delta-equivalence & Moise assembly, octonion/Hurwitz/G_2 & Bring curve.
  - *Primary current folders:* `{"BraidKnot": 236, "Knot": 99, "MathlibExt": 98, "SchurWeyl": 84, "Mathlib": 66, "BraidsAndKnots": 48, "Mass": 42, "IwahoriHecke": 21, "OrientedSkein": 21, "BringsSurface": 19}`
  - *Sample modules:* `QOU.Archimedean.BlochWignerNonneg`, `QOU.Archimedean.BlochWignerPositive`, `QOU.Archimedean.BringEllipticFactor`, `QOU.Archimedean.BringHauptmodulGate`, `QOU.Archimedean.ForceCarrierBringUniqueness`, `QOU.Archimedean.IdealTetrahedronVolumeConcave`
  - *Inter-community `lean_lib` deps:* `{"TierA.MathlibExt": 87, "TierB.CompactQuantumMetrics": 1, "TierB.HeckeTemperleyLieb": 217, "TierB.QCalculus": 7, "TierB.ToricConicOpt": 3}`

### 3.2 Exact Cut-Edges Blocking Zero-`QOU.*` Extraction (`GW_Detangled` Action List)

Zero outbound cut-edges from Tier-A/Tier-B into `QOU.*`!

## 4. Directory-Level Tangle & Consolidation (`83` `QOU/*` Dirs -> `12` Canonical `QOU.*` Subgraphs)

### 4.1 Synonym-Directory Merge Clusters

| Synonym Cluster | Current Directories (`#`) | Total Files | Pure-Math Files Inside | Cross-Synonym Edges Eliminated | Remaining External Edges |
|---|---|---:|---:|---:|---:|
| `Braid_Knot_7dirs` | `BraidKnot` (468), `BraidsAndKnots` (113), `Knot` (103), `Braiding` (35), `KnotTheory` (9), `BraidsKnots` (7), `Knots` (1) | **736** | 543 | **23** | 210 |
| `Mass_7dirs` | `Mass` (312), `MassTheory` (247), `MassEndomorphism` (10), `WedderburnMass` (5), `TopologicalMass` (3), `HadronicMass` (2), `AtomicMass` (2) | **581** | 408 | **5** | 120 |
| `Hecke_3dirs` | `Hecke` (103), `IwahoriHecke` (38), `HeckeAlgebra` (14) | **155** | 131 | **3** | 63 |
| `Bring_3dirs` | `BringsSurface` (19), `Brings` (15), `HyperellipticQuintic` (4) | **38** | 35 | **0** | 4 |
| `QOU_Core_4dirs` | `QuantumObservableUniverse` (37), `QuantumObservableUniverses` (18), `QuantumUniverse` (1), `CommutativeQOU` (1) | **57** | 26 | **1** | 16 |
| `Eightfold_2dirs` | `Eightfold` (52), `EightfoldWay` (2) | **54** | 40 | **1** | 10 |
| `Information_2dirs` | `Information` (44), `InformationTheory` (2) | **46** | 30 | **0** | 10 |
| `Archimedean_2dirs` | `Archimedean` (277), `ArchimedeanUniverse` (5) | **282** | 214 | **0** | 59 |
| `Interactions_2dirs` | `Interactions` (39), `ParticleInteractions` (36) | **75** | 29 | **0** | 40 |
| `Fluid_2dirs` | `FluidDynamics` (45), `GaugeFieldFluidDynamics` (1) | **46** | 29 | **0** | 4 |
| `MathlibStaging_4dirs` | `MathlibExt` (302), `Mathlib` (235), `MathlibInfra` (6), `Infra` (4) | **547** | 540 | **16** | 51 |

### 4.2 Directory-Level SCC Tangles & Top Bidirectional Folder Pairs

- **Directory SCC #1 (40 directories mutually coupled):** `<QOU-root-loose>`, `AlgebraicSubstrate`, `AppendixSurreals`, `Archimedean`, `BraidKnot`, `Braiding`, `BraidsAndKnots`, `BringsSurface`, `Conjectures`, `Eightfold`, `Encounter`, `FlavorDressing`, `FluidDynamics`, `GaugeFieldFluidDynamics`, `Hecke`, `HeckeAlgebra`, `Information`, `Interactions`, `IwahoriHecke`, `KZ`, `Knot`, `LiftingDescent`, `Machinery`, `Mass`, `MassEndomorphism`, `MassTheory`, `Mathlib`, `MathlibExt`, `Optimization`, `ParticleInteractions`, `QBeta`, `QuantumBloch`, `QuantumObservableUniverse`, `QuantumObservableUniverses`, `QuarkState`, `Resurgence`, `SchurWeyl`, `Shared`, `StandardModel`, `Torsion`

| Dir A | Dir B | `A -> B` Imports | `B -> A` Imports | Min-Cut Back-Edges |
|---|---|---:|---:|---:|
| `<QOU-root-loose>` | `BraidKnot` | 164 | 12 | **12** |
| `Archimedean` | `Knot` | 12 | 10 | **10** |
| `<QOU-root-loose>` | `Archimedean` | 40 | 9 | **9** |
| `BraidKnot` | `Mathlib` | 20 | 9 | **9** |
| `Mathlib` | `MathlibExt` | 7 | 9 | **7** |
| `BraidKnot` | `MathlibExt` | 39 | 6 | **6** |
| `Mass` | `QBeta` | 6 | 10 | **6** |
| `BraidKnot` | `SchurWeyl` | 8 | 6 | **6** |
| `<QOU-root-loose>` | `QuantumObservableUniverse` | 19 | 5 | **5** |
| `MathlibExt` | `QBeta` | 4 | 29 | **4** |
| `Mass` | `MathlibExt` | 21 | 4 | **4** |
| `Archimedean` | `MathlibExt` | 19 | 4 | **4** |
| `MathlibExt` | `SchurWeyl` | 4 | 12 | **4** |
| `<QOU-root-loose>` | `FlavorDressing` | 6 | 4 | **4** |
| `Mathlib` | `SchurWeyl` | 3 | 34 | **3** |

### 4.3 Target `12` Canonical Monograph-Aligned `QOU.<Subgraph>` Partitions (After Extracting Tier-A & Tier-B)

| Canonical `QOU.*` Subgraph | Layer | QOU-Coupled Modules | Decls (`thm`/`lem`) | Body `sorry` / `axiom` | Inbound Edges | `.ts` `lean.ref`s | Consolidated Source Folders (Top) |
|---|---:|---:|---:|---:|---:|---:|---|
| `QOU.Core` | L8 | **120** | 1,259 (804) | 0 / 0 | 103 | 54 | `QuantumObservableUniverse`:34, `<QOU-root-loose>`:26, `QuantumObservableUniverses`:17, `MathlibExt`:15, `Shared`:6 |
| `QOU.LiftingDescent` | L9 | **62** | 777 (490) | 0 / 0 | 12 | 45 | `LiftingDescent`:27, `Torsion`:23, `FormalGroups`:8, `<QOU-root-loose>`:3, `Descent`:1 |
| `QOU.BraidsAndKnots` | L10 | **347** | 18,029 (3,350) | 0 / 1 | 45 | 182 | `BraidKnot`:146, `BraidsAndKnots`:55, `KZ`:46, `Hecke`:28, `Machinery`:22 |
| `QOU.BringsSurface` | L11 | **62** | 669 (469) | 0 / 0 | 32 | 11 | `AlgebraicSubstrate`:43, `<QOU-root-loose>`:12, `RiemannSurface`:3, `HyperellipticQuintic`:2, `Brings`:1 |
| `QOU.Confinement` | L12 | **132** | 2,469 (1,741) | 0 / 0 | 14 | 22 | `QuarkState`:43, `Interactions`:37, `ParticleInteractions`:32, `<QOU-root-loose>`:6, `OptionE`:5 |
| `QOU.EightfoldWay` | L12 | **52** | 784 (518) | 0 / 0 | 6 | 13 | `Eightfold`:43, `FlavorDressing`:6, `EightfoldWay`:2, `BaryonWeight`:1 |
| `QOU.MassTheory` | L13 | **707** | 8,707 (6,069) | 0 / 1 | 59 | 131 | `Archimedean`:230, `Mass`:228, `MassTheory`:211, `<QOU-root-loose>`:13, `MassEndomorphism`:9 |
| `QOU.Nuclear` | L14 | **332** | 4,971 (3,510) | 0 / 0 | 15 | 31 | `QBeta`:321, `Nuclear`:4, `ShellCondensation`:4, `AppendixQValues`:1, `MagicShell`:1 |
| `QOU.StandardModel` | L14 | **85** | 1,488 (928) | 0 / 0 | 20 | 14 | `StandardModel`:42, `AlphaEM`:17, `<QOU-root-loose>`:13, `QFTMath`:5, `Resurgence`:4 |
| `QOU.FluidDynamics` | L14 | **45** | 463 (313) | 0 / 0 | 2 | 2 | `FluidDynamics`:43, `<QOU-root-loose>`:1, `GaugeFieldFluidDynamics`:1 |
| `QOU.InformationTheory` | L14 | **54** | 393 (266) | 0 / 0 | 3 | 9 | `Information`:41, `<QOU-root-loose>`:9, `QGeometricLanglands`:2, `InformationTheory`:1, `QuantumComputationalUniversality`:1 |
| `QOU.Observations` | L15 | **92** | 1,138 (796) | 0 / 1 | 3 | 35 | `AppendixSurreals`:52, `Observations`:19, `Molecular`:15, `<QOU-root-loose>`:3, `Experimental`:2 |

## 5. Comparison of 3 Concrete Refactor Options (Ready for Coordinator `AskUserQuestion`)

| Dimension | **Option 1 (Recommended): Multi-`lean_lib` in `lakefile.toml`** | **Option 2: 6 Separate Lake Packages (`folio/lean-contrib/*`)** | **Option 3: Single-Lib Mirror (`QOU/Contrib/<Pkg>/*`)** |
|---|---|---|---|
| **Lake Target Architecture** | `MathlibExt` + 6 Tier-B `[[lean_lib]]` + `QOU` in `folio/quantum-observable-universe/lean/lakefile.toml` | 6 standalone `lakefile.toml` packages under `folio/lean-contrib/<pkg>/lean/` via `[[require]]` | Single `[[lean_lib]] name = "QOU"` with `QOU/Contrib/<Pkg>/*` folders |
| **`Process_GraphDetanglement` Stage** | **Stage 3 (`Isolate` in-place)** — 1-folder `git mv` away from Stage 4 extraction | **Stage 4 (`Extract` immediately)** — full multi-package split now | **Stage 2 (`Detangle` only)** — keeps `QOU.` namespace prefix |
| **Tier-B Reservoir Modules** | **1473** modules in root namespaces (`HeckeTemperleyLieb.*`, etc.) | **1473** modules in 6 new Lake packages | **1473** modules under `QOU.Contrib.<Pkg>.*` |
| **Tier-A `MathlibExt` Modules** | **301** modules (`MathlibExt.*`) | **301** modules (`MathlibExt.*`) | **301** modules (`QOU.MathlibExt.*`) |
| **Collapsed `QOU.*` Subgraphs** | `83 dirs + 106 loose` → **12 canonical `QOU.<Chapter>` dirs** (**2090** modules) | `83 dirs + 106 loose` → **12 canonical `QOU.<Chapter>` dirs** (**2090** modules) | `83 dirs + 106 loose` → **12 canonical `QOU.<Chapter>` dirs** (**2090** modules) |
| **Blocking Cut-Edges to Prune/Factor** | **0** (`Tier-A/B -> QOU.*`) | **0** (`Tier-A/B -> QOU.*`) | **0** (`Tier-A/B -> QOU.*`) |
| **Zero-`QOU.*` Boundary Enforcement** | `lake build <TierBLib>` + `lean-best-practices-lint.py --package` | Physical Lake package DAG (impossible to import `QOU.*`) + linter | Python linter (`lean-best-practices-lint.py`) only |
| **`import` Lines Rewritten (Codemod)** | ~5,841 (`QOU` + siblings) | ~5,841 (`QOU` + siblings) | ~5,841 (`QOU` + siblings) |
| **`.ts` `lean.ref` Updates** | ~1,316 (keeps `qou:<Decl>` package URI!) | ~1,316 + **6 new URI prefixes** in `schemas/lean-packages.ts` | ~1,316 (keeps `qou:QOU.Contrib...` URI) |
| **`.olean` Cache / Overlay Blast Radius** | **Low** (`0` new `.lake/build` roots; `lean-overlay-env.sh` works unchanged!) | **High** (`+6` `.lake/build/lib/lean` roots in `lean-env.sh`, overlay, & cache seeders) | **Lowest** (`0` new roots, single `QOU/` folder) |
| **Second Rename Needed for Reservoir?** | **No (0 files)** — namespaces are already Reservoir-final | **No (0 files)** | **Yes (1473 files)** must drop `QOU.Contrib.` later |
| **Estimated Effort** | **Medium (3-4 PR tranches after active Lean PRs land; 1 automated codemod + single olean reseed)** | High (5-6 PR tranches; requires updating `schemas/lean-packages.ts`, `lean-env.sh`, `lean-overlay-env.sh`, `lean-olean-cache-seed.sh`, and CI workflows for 6 new Lake build roots) | Low-Medium now (2-3 PR tranches), but incurs technical debt: every Tier-B declaration keeps a `QOU.Contrib.` prefix and requires a second breaking rename before Lean Reservoir publication. |

### Recommended Phased Execution Strategy (`qou-lref` -> `qou-lanx`)

1. **Adopt Option 1 now (`Isolate in-place`)** once active Lean PRs settle and the owner confirms via `AskUserQuestion`:
   - **Step 1 (Cut-edge surgical prep):** Resolve the **0** outbound `Tier-A/B -> QOU.*` cut-edges (`Task_Move`: factor pure base definitions out of `QOU.*` or reclassify pure targets) and re-run `scripts/lean-kg-detangler.py` until `community_to_qou_cut_edges == 0`.
   - **Step 2 (Atomic codemod + `[[lean_lib]]` isolation):** Move the 6 Tier-B subgraphs to top-level namespaces (`HeckeTemperleyLieb/`, `TwistedFrobeniusHopf/`, `ToricConicOpt/`, `CompactQuantumMetrics/`, `QCalculus/`, `BraidKnotOctonion/`) + `MathlibExt/` inside `folio/quantum-observable-universe/lean/`, collapse the remaining `QOU/*` tree into the `12` canonical chapter subgraphs, rewrite `import` and `lean.ref` strings atomically, and verify with `LEAN_NUM_THREADS=1 nice -n 15 bash scripts/lean-direct-cone.sh -j 1` + `scripts/lean-best-practices-lint.py`.
   - **Step 3 (Optional Stage 4 `Extract` to Option 2 per-library):** Whenever an individual Tier-B library (e.g., `TwistedFrobeniusHopf` or `CompactQuantumMetrics`) is ready for public Lean Reservoir indexing, `Task_Extract` lifts its already-isolated folder into a standalone repo with **zero namespace or theorem-name churn**.

