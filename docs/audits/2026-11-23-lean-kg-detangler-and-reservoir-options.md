# Lean 4 Knowledge-Graph Detangler & Reservoir `lean_lib` Architecture Options (`qou-kgdt` + `qou-mlib`)

- **Date:** `2026-11-23`
- **Epic / Beans:** `qou-lnkg` (`qou-kgdt`, `qou-lskl`, `qou-mlib`; gates `qou-lref` & `qou-lanx`)
- **Instrument:** `scripts/lean-kg-detangler.py` (deterministic static DAG + §7c + QOU-purity analyzer, `11.355s` wall time)
- **Machine-readable companion:** `docs/audits/2026-11-23-lean-kg-detangler-and-reservoir-audit.json`
- **Scope Gate:** Stage 1 + Stage 1b + Stage 2 options readiness ONLY — **zero `.lean` files moved or renamed** pending owner selection via `AskUserQuestion`.

---

## 1. Executive Summary & `Process_GraphDetanglement` Gate Measurements

Following `cat-harness/processes/kg/graph-detanglement.bpmn` (`Process_GraphDetanglement`), we measure the **unassigned column FIRST** before reading cross-edge counts:

| Gate / Metric | Measured Value | Status / Interpretation |
|---|---:|---|
| Total `.lean` files in `folio/quantum-observable-universe/` | **4,751** | `3,842` in `lean/` + `909` content-block siblings (`+47` `UGB`, `+3` `Fred2005`) |
| Fragmented `lean/QOU/*` subdirectories + loose root files | **83 dirs + 106 loose** | Grew from `78` to `83` ad-hoc dirs under `QOU/` (`3,840` library modules, `68,855` decls) |
| `Task_Declare` — Unassigned library modules | **0** | `declared` (100% of `3,840` modules mapped to Tier-A, 6 Tier-B, or 12 `QOU.*` subgraphs) |
| `Task_Measure` — Unassigned resolved `import` edges | **0** | `5,352` internal `QOU` + `6,840` `Mathlib` + `2` `UGB` (`0` dangling) |
| Module-level `import` cycles (Tarjan SCC) | **0** | Module graph is strictly acyclic (`0` Lean module cycles) |
| Directory-level nontrivial SCCs across `83` `QOU/*` dirs | **1** |Largest directory SCC tangles `40` folders via `63` bidirectional folder pairs |
| Orphaned modules not reachable from `QOU.lean` | **1,799** (`46.85%`) | Built by `globs = ["QOU.+"]` (`qou-rc7b`), `34` reached by chapter `.lean` siblings, `1,171` unimported leaves |
| Intrinsically pure-math library modules (`0` QOU coupling) | **2,624** | **2,304** already cone-pure (`0` QOU deps transitively); **320** blocked only by cut-edges |
| Outbound cut-edges (`Tier-A / Tier-B -> QOU.*`) | **188** | Exact edges to prune/factor before zero-`QOU.*` `lean_lib` isolation (`GW_Detangled`) |
| Current `Mathlib`/`MathlibExt`/`MathlibInfra` upward leaks | **51** | Existing staging modules importing non-staging `QOU.*` directories |
| Library `sorry` / custom `axiom` counts | `0` body / `0` class / `3` `axiom` | Siblings: `9` body `sorry`, `0` §3b-cond class `sorry`, `39` `axiom` |

## 2. Purity & §7c Base-Ring Stratification

### 2.1 Mathematical vs. QOU-Physics Coupling (`3,840` Library Modules + `909` Siblings)

| Purity Tier | Library Modules | Transitive Cone Status | Content-Block Siblings | Definition |
|---|---:|---|---:|---|
| `pure_math` | **2,624** | `2,304` cone-pure + `320` cut-blocked | 602 | Zero `q0`/`substrate_q`, zero CODATA/decimals, zero particle/QOU-axiom types |
| `qou_categorical_core` | **1,098** | `1,098` | 248 | Uses QOU categorical/particle structures over generic rings; zero `q0` or CODATA |
| `qou_archimedean_model` | **32** | `32` | 6 | Evaluates at `substrate_q` / `q0` / `AlphaEM` without empirical decimal tables |
| `qou_empirical_comparison` | **86** | `86` | 53 | CODATA / MeV / decimal literals / experimental comparison boundaries |

### 2.2 §7c Base-Ring Generality Distribution

| §7c Ring Regime | Library Modules | Content-Block Siblings | Upstreaming / Hygiene Action |
|---|---:|---:|---|
| `pure_generic` (`[CommRing R]` / `[Field R]`) | **1,402** | 235 | Gold-standard §7c algebraic generality |
| `ordered_generic` (`[LinearOrderedField R]`, etc.) | **185** | 18 | Gold-standard §7c ordered generality (no `ℝ` lock-in) |
| `ring_agnostic` (combinatorics / `ℕ` / `ℤ` / categories) | **890** | 325 | Clean combinatorial / discrete / categorical modules |
| `archimedean_real` (justified `Real.sqrt`/`exp`/`log`/decimals) | **581** | 124 | Legitimate post-wall Archimedean analysis |
| `gratuitous_real_candidate` (`: ℝ` without transcendental ops) | **541** | 175 | Generalize `: ℝ` → `[CommRing R]` / `[LinearOrderedField R]` during Tier-A/B curation |
| `mixed_generic_and_real` (both `[CommRing R]` & `: ℝ` in 1 file) | **241** | 32 | Split generic theorem from `(R := ℝ)` instantiation per §7c wall rule |

## 3. Tier-A (`Mathlib4` Core) & Tier-B (6 Standalone Lean Reservoir `lean_lib` Packages)

| Target Library | Total Modules | Cone-Pure Ready Now | Cut-Blocked Pure | Decls (`thm`/`lem`) | Body `sorry` / `axiom` | Outbound Cut-Edges to `QOU.*` | Inbound `QOU` Consumers | `.ts` `lean.ref`s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `TierA.MathlibExt` | **321** | **312** | 9 | 4,247 (3,292) | 0 / 0 | **11** | 184 | 0 |
| `TierB.HeckeTemperleyLieb` | **635** | **556** | 79 | 8,737 (6,420) | 0 / 1 | **73** | 313 | 6 |
| `TierB.TwistedFrobeniusHopf` | **38** | **30** | 8 | 611 (408) | 0 / 0 | **10** | 17 | 1 |
| `TierB.ToricConicOpt` | **33** | **32** | 1 | 539 (368) | 0 / 0 | **7** | 34 | 5 |
| `TierB.CompactQuantumMetrics` | **10** | **10** | 0 | 170 (122) | 0 / 0 | **0** | 6 | 1 |
| `TierB.QCalculus` | **58** | **57** | 1 | 637 (509) | 0 / 0 | **11** | 89 | 0 |
| `TierB.BraidKnotOctonion` | **585** | **492** | 93 | 12,058 (7,946) | 0 / 0 | **76** | 279 | 29 |

> **Companion Already-Extracted Reservoir Package:** `folio/unital-groebner-bases/lean/` (`UGB`, **47 `.lean` files**) already provides standalone Gröbner–Shirshov / Kang–Lee–Lee–Oh / Splay PBW infrastructure with zero `QOU.*` imports (`qou` requires `ugb` via `[[require]]`). `HeckeTemperleyLieb` either layers cleanly on `ugb` or re-exports its `HeckeGS` bridge.

### 3.1 Package Scope & Representative Modules

- **`TierA.MathlibExt`** (321 modules; 312 immediately zero-`QOU` cone-pure): Selective Mathlib4 Core PR Staging (List/sort/foldl, general matrix/trace, ordered-field/sqrt/convexity, Borel/Dirichlet/Cech general lemmas).
  - *Primary current folders:* `{"Mathlib": 161, "MathlibExt": 146, "Common": 7, "Infra": 4, "MathlibInfra": 2, "<QOU-root-loose>": 1}`
  - *Sample modules:* `QOU.Common.AntiInvolutionPalindrome`, `QOU.Common.BalancedQuantumTwist`, `QOU.Common.CyclotomicValueTruncates`, `QOU.Common.FormalResidue`, `QOU.Common.MagicNumbers`, `QOU.Common.PeriodicDense`
  - *Inter-community `lean_lib` deps:* `{"TierB.BraidKnotOctonion": 10, "TierB.CompactQuantumMetrics": 1, "TierB.HeckeTemperleyLieb": 27, "TierB.QCalculus": 5, "TierB.ToricConicOpt": 4}`
- **`TierB.HeckeTemperleyLieb`** (635 modules; 556 immediately zero-`QOU` cone-pure): Iwahori-Hecke H_n(q), Temperley-Lieb TL_n(q), Jones/Markov/Ocneanu traces, Hoefsmit seminormal irreps, Young/SYT & Grobner-Shirshov normal forms.
  - *Primary current folders:* `{"SchurWeyl": 122, "BraidKnot": 110, "Hecke": 83, "Machinery": 72, "Mathlib": 61, "MathlibExt": 44, "IwahoriHecke": 37, "Mass": 19, "BraidsAndKnots": 17, "Archimedean": 13}`
  - *Sample modules:* `QOU.Archimedean.CatalanClausenBridge`, `QOU.Archimedean.HeckeBraidingSubstrateNonSymmetric`, `QOU.Archimedean.HeckeRep`, `QOU.Archimedean.MarkovGramRealSymm`, `QOU.Archimedean.MarkovWeightValueTransport`, `QOU.Archimedean.MatrixSchurCommutant`
  - *Inter-community `lean_lib` deps:* `{"TierA.MathlibExt": 57, "TierB.BraidKnotOctonion": 61, "TierB.QCalculus": 10, "TierB.ToricConicOpt": 6, "TierB.TwistedFrobeniusHopf": 2}`
- **`TierB.TwistedFrobeniusHopf`** (38 modules; 30 immediately zero-`QOU` cone-pure): Nakayama-twisted Frobenius algebras, Sweedler H_4 & Taft Hopf algebras, Higman norm map, ambidextrous & tower adjunctions.
  - *Primary current folders:* `{"QuantumObservableUniverse": 7, "BraidKnot": 5, "MassTheory": 5, "LiftingDescent": 4, "FrobeniusHopfData": 3, "<QOU-root-loose>": 3, "ParticleInteractions": 3, "AlgebraicSubstrate": 2, "Mathlib": 2, "Archimedean": 1}`
  - *Sample modules:* `QOU.AlgebraicSubstrate.FrobeniusSchurExpectationCancellation`, `QOU.AlgebraicSubstrate.TwistedAmbidextrousAdjunction`, `QOU.Archimedean.frobenius_gram_matrix`, `QOU.BraidKnot.DepthStratifiedFrobeniusReciprocity`, `QOU.BraidKnot.KnotFactorFrobeniusPairing`, `QOU.BraidKnot.NakayamaGradingObstruction`
  - *Inter-community `lean_lib` deps:* `{"TierB.BraidKnotOctonion": 2, "TierB.HeckeTemperleyLieb": 3, "TierB.QCalculus": 1}`
- **`TierB.ToricConicOpt`** (33 modules; 32 immediately zero-`QOU` cone-pure): Sturmfels-Thomas toric Grobner chambers, Graver/universal Grobner bases, Birch toric equilibria, symmetry-reduced LP/SDP dual certificates & kinks.
  - *Primary current folders:* `{"Optimization": 10, "MathlibExt": 7, "Knot": 4, "BraidKnot": 3, "Mathlib": 3, "MathlibInfra": 3, "Archimedean": 1, "Interactions": 1, "MassTheory": 1}`
  - *Sample modules:* `QOU.Archimedean.TypeBFoldedCrystalCombinatorics`, `QOU.BraidKnot.CanonicalKnotIdSDPUniqueness`, `QOU.BraidKnot.LpDualityHypothesisClass`, `QOU.BraidKnot.joint_tower_sdp_confinement`, `QOU.Interactions.ConfinementSDP`, `QOU.Knot.AngleStructureUniqueness`
  - *Inter-community `lean_lib` deps:* `{"TierA.MathlibExt": 7, "TierB.BraidKnotOctonion": 3, "TierB.HeckeTemperleyLieb": 2, "TierB.QCalculus": 1}`
- **`TierB.CompactQuantumMetrics`** (10 modules; 10 immediately zero-`QOU` cone-pure): Finite-dimensional Rieffel-Connes compact quantum metric spaces, Lipschitz seminorms, Kantorovich-Rubinstein duality, Woronowicz O_q(SU(2)) calculus.
  - *Primary current folders:* `{"MathlibExt": 7, "AlgebraicSubstrate": 1, "InformationTheory": 1, "Observations": 1}`
  - *Sample modules:* `QOU.AlgebraicSubstrate.OqSU2ModularNakayama`, `QOU.InformationTheory.FiniteRieffelQuantumMetric`, `QOU.MathlibExt.Bicommutant`, `QOU.MathlibExt.DerivationIterateLeibniz`, `QOU.MathlibExt.DerivationRankNullity`, `QOU.MathlibExt.FrobeniusInnerProduct`
  - *Inter-community `lean_lib` deps:* `{"TierB.BraidKnotOctonion": 2}`
- **`TierB.QCalculus`** (58 modules; 57 immediately zero-`QOU` cone-pure): q-numbers [n]_q, Gaussian binomials, Thomae-Jackson q-integrals & lattices, q-exponentials, Faddeev/quantum dilogarithms, Habiro cyclotomic rings.
  - *Primary current folders:* `{"MathlibExt": 22, "BraidKnot": 9, "Mass": 9, "Habiro": 4, "Machinery": 4, "Archimedean": 2, "MassTheory": 2, "Mathlib": 2, "BraidsAndKnots": 1, "LiftingDescent": 1}`
  - *Sample modules:* `QOU.Archimedean.DilogPartBFaddeevScaling`, `QOU.Archimedean.SWJacksonMomentFactorization`, `QOU.BraidKnot.BWVacuumRowHabiroBoundaryData`, `QOU.BraidKnot.BWVacuumRowHabiroRigidity`, `QOU.BraidKnot.HabiroDomainVanishing`, `QOU.BraidKnot.HabiroNewtonLadder`
  - *Inter-community `lean_lib` deps:* `{"TierA.MathlibExt": 2, "TierB.BraidKnotOctonion": 2, "TierB.HeckeTemperleyLieb": 5, "TierB.ToricConicOpt": 1}`
- **`TierB.BraidKnotOctonion`** (585 modules; 492 immediately zero-`QOU` cone-pure): Artin braid groups B_n, Burau/Lawrence-Krammer/Alexander invariants, PL knot Delta-equivalence & Moise assembly, octonion/Hurwitz/G_2 & Bring curve.
  - *Primary current folders:* `{"BraidKnot": 229, "Knot": 89, "MathlibExt": 68, "BraidsAndKnots": 60, "OrientedSkein": 21, "BringsSurface": 19, "Braiding": 16, "Brings": 15, "MassTheory": 13, "Mass": 12}`
  - *Sample modules:* `QOU.Archimedean.BringEllipticFactor`, `QOU.Archimedean.BringHauptmodulGate`, `QOU.Archimedean.ForceCarrierBringUniqueness`, `QOU.Archimedean.TorusKnot`, `QOU.Archimedean.TorusKnotGenusFourUnique`, `QOU.ArchimedeanUniverse.s5_bring_hodge_depth`
  - *Inter-community `lean_lib` deps:* `{"TierA.MathlibExt": 45, "TierB.CompactQuantumMetrics": 3, "TierB.HeckeTemperleyLieb": 74, "TierB.QCalculus": 9, "TierB.ToricConicOpt": 7}`

### 3.2 Exact Cut-Edges Blocking Zero-`QOU.*` Extraction (`GW_Detangled` Action List)

There are exactly **188** directed `import` edges from intrinsically pure Tier-A/Tier-B candidate modules into QOU-coupled modules. Pruning or factoring the pure base definition out of these targets brings `community_to_qou_cut_edges` to **0**:

| # | Pure Candidate Module (`src`) | Candidate Lib | Imported `QOU.*` Target (`dst`) | Target Subgraph | Recommended Detangle Move |
|---:|---|---|---|---|---|
| 1 | `QOU.Archimedean.CatalanClausenBridge` | `TierB.HeckeTemperleyLieb` | `QOU.Archimedean.ClausenFunctionMathlibFiller` | `QOU.MassTheory` | `reclassify_target_to_community` |
| 2 | `QOU.Archimedean.CatalanClausenBridge` | `TierB.HeckeTemperleyLieb` | `QOU.Archimedean.HyperbolicVolumeTranscendence` | `QOU.MassTheory` | `factor_pure_base_lemma_or_prune_import` |
| 3 | `QOU.Archimedean.DilogPartBFaddeevScaling` | `TierB.QCalculus` | `QOU.Archimedean.DilogPartBIteratedLimit` | `QOU.MassTheory` | `reclassify_target_to_community` |
| 4 | `QOU.Archimedean.DilogPartBFaddeevScaling` | `TierB.QCalculus` | `QOU.Archimedean.DilogPartBWP1Capstone` | `QOU.MassTheory` | `reclassify_target_to_community` |
| 5 | `QOU.Archimedean.HeckeBraidingSubstrateNonSymmetric` | `TierB.HeckeTemperleyLieb` | `QOU.MassTheory.TraceSignFlipRegime` | `QOU.MassTheory` | `reclassify_target_to_community` |
| 6 | `QOU.Archimedean.HeckeRep` | `TierB.HeckeTemperleyLieb` | `QOU.Archimedean.GroundRing` | `QOU.MassTheory` | `reclassify_target_to_community` |
| 7 | `QOU.Archimedean.HeckeRep` | `TierB.HeckeTemperleyLieb` | `QOU.Archimedean.TransferMatrix` | `QOU.MassTheory` | `factor_pure_base_lemma_or_prune_import` |
| 8 | `QOU.Archimedean.MarkovGramRealSymm` | `TierB.HeckeTemperleyLieb` | `QOU.Archimedean.LoopWeightRealSymmReduction` | `QOU.MassTheory` | `reclassify_target_to_community` |
| 9 | `QOU.Archimedean.QHookBound` | `TierB.HeckeTemperleyLieb` | `QOU.Archimedean.GroundRing` | `QOU.MassTheory` | `reclassify_target_to_community` |
| 10 | `QOU.Archimedean.SWJacksonMomentFactorization` | `TierB.QCalculus` | `QOU.Archimedean.BalancedMomentConfluence` | `QOU.MassTheory` | `factor_pure_base_lemma_or_prune_import` |
| 11 | `QOU.Archimedean.SchurWeylTrace` | `TierB.HeckeTemperleyLieb` | `QOU.Archimedean.RossoJonesTorusLink` | `QOU.MassTheory` | `reclassify_target_to_community` |
| 12 | `QOU.Archimedean.TorusKnot` | `TierB.BraidKnotOctonion` | `QOU.Archimedean.GroundRing` | `QOU.MassTheory` | `reclassify_target_to_community` |
| 13 | `QOU.BraidKnot.CasimirShared` | `TierB.HeckeTemperleyLieb` | `QOU.Basic` | `QOU.Core` | `reclassify_target_to_community` |
| 14 | `QOU.BraidKnot.CemeteryGroupEmergence` | `TierB.BraidKnotOctonion` | `QOU.Basic` | `QOU.Core` | `reclassify_target_to_community` |
| 15 | `QOU.BraidKnot.ConfinedParticle` | `TierB.BraidKnotOctonion` | `QOU.Archimedean.GroundRing` | `QOU.MassTheory` | `reclassify_target_to_community` |
| 16 | `QOU.BraidKnot.ConfinementGradingCorrespondence` | `TierB.BraidKnotOctonion` | `QOU.Basic` | `QOU.Core` | `reclassify_target_to_community` |
| 17 | `QOU.BraidKnot.ConfinementLevel` | `TierB.BraidKnotOctonion` | `QOU.Basic` | `QOU.Core` | `reclassify_target_to_community` |
| 18 | `QOU.BraidKnot.ConfinementPhaseStratification` | `TierB.BraidKnotOctonion` | `QOU.BraidKnot.DressedParticle` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 19 | `QOU.BraidKnot.EigenbasisStructuralLemmas` | `TierB.BraidKnotOctonion` | `QOU.BraidKnot.ChiralityWritheRibbon` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 20 | `QOU.BraidKnot.GSReductionOrder` | `TierB.BraidKnotOctonion` | `QOU.Basic` | `QOU.Core` | `reclassify_target_to_community` |
| 21 | `QOU.BraidKnot.HeckeAnyonicSubstrate` | `TierB.HeckeTemperleyLieb` | `QOU.Basic` | `QOU.Core` | `reclassify_target_to_community` |
| 22 | `QOU.BraidKnot.HookSumCompletedSquare` | `TierB.HeckeTemperleyLieb` | `QOU.BraidKnot.HookSumBetaCoordinates` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 23 | `QOU.BraidKnot.HookSumElasticity` | `TierB.HeckeTemperleyLieb` | `QOU.BraidKnot.StaircaseHookMultiset` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 24 | `QOU.BraidKnot.JonesHopfSkein` | `TierB.BraidKnotOctonion` | `QOU.BraidKnot.QBetaCategoricalPrecisionLadder` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 25 | `QOU.BraidKnot.JucysMurphyCentralElementsQOU` | `TierB.BraidKnotOctonion` | `QOU.Basic` | `QOU.Core` | `reclassify_target_to_community` |
| 26 | `QOU.BraidKnot.KazhdanLusztigClassicalLimit` | `TierB.HeckeTemperleyLieb` | `QOU.Basic` | `QOU.Core` | `reclassify_target_to_community` |
| 27 | `QOU.BraidKnot.KeystoneC8SuperExpBound` | `TierB.BraidKnotOctonion` | `QOU.Mass.InvolutionNumbers` | `QOU.MassTheory` | `reclassify_target_to_community` |
| 28 | `QOU.BraidKnot.LadderConventionLocalisation` | `TierB.BraidKnotOctonion` | `QOU.BraidKnot.QBetaCategoricalPrecisionLadder` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 29 | `QOU.BraidKnot.LevelSufficiency` | `TierB.BraidKnotOctonion` | `QOU.Archimedean.HeckeH3` | `QOU.MassTheory` | `factor_pure_base_lemma_or_prune_import` |
| 30 | `QOU.BraidKnot.LevelSufficiency` | `TierB.BraidKnotOctonion` | `QOU.Interactions.ConfinementLP` | `QOU.Confinement` | `reclassify_target_to_community` |
| 31 | `QOU.BraidKnot.LpDualityHypothesisClass` | `TierB.ToricConicOpt` | `QOU.Basic` | `QOU.Core` | `reclassify_target_to_community` |
| 32 | `QOU.BraidKnot.MuPCarrierOrderWindow` | `TierB.BraidKnotOctonion` | `QOU.BraidKnot.MmuR9V9Closure` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 33 | `QOU.BraidKnot.OperatorValuedCombiner` | `TierB.BraidKnotOctonion` | `QOU.BraidKnot.CrystalRMatrixSubLemma` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 34 | `QOU.BraidKnot.PartitionHookProductBridge` | `TierB.HeckeTemperleyLieb` | `QOU.BraidKnot.DeltaLambdaSignRule` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 35 | `QOU.BraidKnot.PartitionNatBridge` | `TierB.BraidKnotOctonion` | `QOU.BraidKnot.DeltaLambdaSignRule` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 36 | `QOU.BraidKnot.QuantumIntBarSymmetric` | `TierB.BraidKnotOctonion` | `QOU.StandardModel.ThetaQcdFramingCp` | `QOU.StandardModel` | `reclassify_target_to_community` |
| 37 | `QOU.BraidKnot.RootOfUnityMTCTruncation` | `TierB.BraidKnotOctonion` | `QOU.Basic` | `QOU.Core` | `reclassify_target_to_community` |
| 38 | `QOU.BraidKnot.SymmetricCrystalPairProduction` | `TierB.BraidKnotOctonion` | `QOU.Basic` | `QOU.Core` | `reclassify_target_to_community` |
| 39 | `QOU.BraidKnot.algebraic_quantum_volume_specialization` | `TierB.BraidKnotOctonion` | `QOU.MathlibExt.MarkovBondRule` | `QOU.Core` | `factor_pure_base_lemma_or_prune_import` |
| 40 | `QOU.BraidsAndKnots.BringFiberActionInstance` | `TierB.BraidKnotOctonion` | `QOU.BraidsAndKnots.S5SO3FiberAction` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 41 | `QOU.BraidsAndKnots.ColorPairIsotypicDecomposition` | `TierB.BraidKnotOctonion` | `QOU.BraidsAndKnots.S5SO3FiberAction` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 42 | `QOU.BraidsAndKnots.DeltaLambdaDTIndex` | `TierB.BraidKnotOctonion` | `QOU.BraidsAndKnots.S5SO3FiberAction` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 43 | `QOU.BraidsAndKnots.DeltaLambdaDTIndexGeneralN` | `TierB.BraidKnotOctonion` | `QOU.BraidsAndKnots.S5SO3FiberAction` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 44 | `QOU.BraidsAndKnots.DeltaLambdaDTModuliUnderdetermined` | `TierB.BraidKnotOctonion` | `QOU.BraidsAndKnots.S5SO3FiberAction` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 45 | `QOU.BraidsAndKnots.DeltaLambdaTopDegreeConcentration` | `TierB.BraidKnotOctonion` | `QOU.BraidsAndKnots.S5SO3FiberAction` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 46 | `QOU.BraidsAndKnots.FibreCategoricalTraceForcesJones` | `TierB.BraidKnotOctonion` | `QOU.Eightfold.RowCapObstruction` | `QOU.EightfoldWay` | `reclassify_target_to_community` |
| 47 | `QOU.BraidsAndKnots.IsospinMurphyOctet` | `TierB.BraidKnotOctonion` | `QOU.BraidsAndKnots.StrangeStrandOctet` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 48 | `QOU.BraidsAndKnots.KeystoneCanonicalAngleMap` | `TierB.BraidKnotOctonion` | `QOU.BraidsAndKnots.S5SO3FiberAction` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 49 | `QOU.BraidsAndKnots.KeystoneFiveFoldStructure` | `TierB.BraidKnotOctonion` | `QOU.BraidsAndKnots.S5SO3FiberAction` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 50 | `QOU.BraidsAndKnots.NStatConjugateGeneral` | `TierB.BraidKnotOctonion` | `QOU.BraidsAndKnots.S5SO3FiberAction` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 51 | `QOU.BraidsAndKnots.ReebChiralitySeparation` | `TierB.BraidKnotOctonion` | `QOU.BraidsAndKnots.S5SO3FiberAction` | `QOU.BraidsAndKnots` | `factor_pure_base_lemma_or_prune_import` |
| 52 | `QOU.BraidsAndKnots.demazure_fiber_markov_trace` | `TierB.HeckeTemperleyLieb` | `QOU.Shared.OperatorSelectionLP` | `QOU.Core` | `factor_pure_base_lemma_or_prune_import` |
| 53 | `QOU.BraidsAndKnots.explicit_alpha_k_h4` | `TierB.BraidKnotOctonion` | `QOU.Shared.MarkovTraceClaim` | `QOU.Core` | `factor_pure_base_lemma_or_prune_import` |
| 54 | `QOU.BraidsAndKnots.wedderburn_bratteli_recursion` | `TierB.HeckeTemperleyLieb` | `QOU.Shared.MarkovTraceClaim` | `QOU.Core` | `factor_pure_base_lemma_or_prune_import` |
| 55 | `QOU.BringHeckeNoOrderThree` | `TierB.BraidKnotOctonion` | `QOU.BringHeckeCommensurability` | `QOU.BringsSurface` | `factor_pure_base_lemma_or_prune_import` |
| 56 | `QOU.BringHeckeNoOrderThree` | `TierB.BraidKnotOctonion` | `QOU.BringTriangleTraces` | `QOU.BringsSurface` | `factor_pure_base_lemma_or_prune_import` |
| 57 | `QOU.BringsSurface.GenusFourFromEquivariantMap` | `TierB.BraidKnotOctonion` | `QOU.RiemannSurface.CombinatorialMapQuotient` | `QOU.BringsSurface` | `reclassify_target_to_community` |
| 58 | `QOU.BringsSurface.GenusFourFromEquivariantMap` | `TierB.BraidKnotOctonion` | `QOU.RiemannSurface.MapGenusNonneg` | `QOU.BringsSurface` | `reclassify_target_to_community` |
| 59 | `QOU.BringsSurface.GenusFourFromGermStabilisers` | `TierB.BraidKnotOctonion` | `QOU.RiemannSurface.GermStabiliserCyclic` | `QOU.BringsSurface` | `reclassify_target_to_community` |
| 60 | `QOU.Eightfold.SecondMarkovTrace` | `TierB.HeckeTemperleyLieb` | `QOU.Eightfold.RowCapObstruction` | `QOU.EightfoldWay` | `reclassify_target_to_community` |
| … | *(+128 more in JSON audit)* | — | — | — | — |

### 3.3 Inter-Package Couplings Among Community `lean_lib` Targets

- Detected **1** inter-package SCC(s) among the community targets: `[['TierA.MathlibExt', 'TierB.BraidKnotOctonion', 'TierB.CompactQuantumMetrics', 'TierB.HeckeTemperleyLieb', 'TierB.QCalculus', 'TierB.ToricConicOpt', 'TierB.TwistedFrobeniusHopf']]`.
- **Resolution:** Keep `TierA.MathlibExt` strictly at Layer 1 (zero imports from `TierB.*`) and orient `TierB` DAG as `{QCalculus, TwistedFrobeniusHopf, ToricConicOpt, BraidKnotOctonion} -> {HeckeTemperleyLieb, CompactQuantumMetrics}` by moving shared braid/partition definitions down into the lower `lean_lib`.

## 4. Directory-Level Tangle & Consolidation (`83` `QOU/*` Dirs -> `12` Canonical `QOU.*` Subgraphs)

### 4.1 Synonym-Directory Merge Clusters

| Synonym Cluster | Current Directories (`#`) | Total Files | Pure-Math Files Inside | Cross-Synonym Edges Eliminated | Remaining External Edges |
|---|---|---:|---:|---:|---:|
| `Braid_Knot_7dirs` | `BraidKnot` (468), `BraidsAndKnots` (113), `Knot` (103), `Braiding` (35), `KnotTheory` (9), `BraidsKnots` (7), `Knots` (1) | **736** | 563 | **22** | 212 |
| `Mass_7dirs` | `Mass` (311), `MassTheory` (239), `MassEndomorphism` (10), `WedderburnMass` (5), `TopologicalMass` (3), `HadronicMass` (2), `AtomicMass` (2) | **572** | 412 | **5** | 120 |
| `Hecke_3dirs` | `Hecke` (102), `IwahoriHecke` (38), `HeckeAlgebra` (14) | **154** | 131 | **3** | 62 |
| `Bring_3dirs` | `BringsSurface` (19), `Brings` (15), `HyperellipticQuintic` (4) | **38** | 36 | **0** | 4 |
| `QOU_Core_4dirs` | `QuantumObservableUniverse` (37), `QuantumObservableUniverses` (18), `QuantumUniverse` (1), `CommutativeQOU` (1) | **57** | 27 | **1** | 16 |
| `Eightfold_2dirs` | `Eightfold` (51), `EightfoldWay` (2) | **53** | 44 | **0** | 8 |
| `Information_2dirs` | `Information` (44), `InformationTheory` (2) | **46** | 31 | **0** | 10 |
| `Archimedean_2dirs` | `Archimedean` (277), `ArchimedeanUniverse` (5) | **282** | 216 | **0** | 59 |
| `Interactions_2dirs` | `Interactions` (38), `ParticleInteractions` (36) | **74** | 33 | **0** | 39 |
| `Fluid_2dirs` | `FluidDynamics` (45), `GaugeFieldFluidDynamics` (1) | **46** | 29 | **0** | 4 |
| `MathlibStaging_4dirs` | `MathlibExt` (302), `Mathlib` (235), `MathlibInfra` (6), `Infra` (4) | **547** | 533 | **16** | 51 |

### 4.2 Directory-Level SCC Tangles & Top Bidirectional Folder Pairs

- **Directory SCC #1 (40 directories mutually coupled):** `<QOU-root-loose>`, `AlgebraicSubstrate`, `AppendixSurreals`, `Archimedean`, `BraidKnot`, `Braiding`, `BraidsAndKnots`, `BringsSurface`, `Conjectures`, `Eightfold`, `Encounter`, `FlavorDressing`, `FluidDynamics`, `GaugeFieldFluidDynamics`, `Hecke`, `HeckeAlgebra`, `Information`, `Interactions`, `IwahoriHecke`, `KZ`, `Knot`, `LiftingDescent`, `Machinery`, `Mass`, `MassEndomorphism`, `MassTheory`, `Mathlib`, `MathlibExt`, `Optimization`, `ParticleInteractions`, `QBeta`, `QuantumBloch`, `QuantumObservableUniverse`, `QuantumObservableUniverses`, `QuarkState`, `Resurgence`, `SchurWeyl`, `Shared`, `StandardModel`, `Torsion`

| Dir A | Dir B | `A -> B` Imports | `B -> A` Imports | Min-Cut Back-Edges |
|---|---|---:|---:|---:|
| `<QOU-root-loose>` | `BraidKnot` | 164 | 14 | **14** |
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
| `QOU.Core` | L4 | **110** | 895 (562) | 0 / 0 | 117 | 54 | `QuantumObservableUniverse`:30, `<QOU-root-loose>`:26, `QuantumObservableUniverses`:17, `MathlibExt`:8, `Shared`:7 |
| `QOU.LiftingDescent` | L5 | **64** | 616 (378) | 0 / 0 | 14 | 45 | `LiftingDescent`:28, `Torsion`:22, `FormalGroups`:10, `<QOU-root-loose>`:3, `Descent`:1 |
| `QOU.BraidsAndKnots` | L6 | **306** | 17,947 (3,392) | 0 / 0 | 113 | 182 | `BraidKnot`:112, `KZ`:44, `BraidsAndKnots`:35, `SchurWeyl`:27, `Machinery`:26 |
| `QOU.BringsSurface` | L7 | **58** | 577 (386) | 0 / 0 | 31 | 11 | `AlgebraicSubstrate`:43, `RiemannSurface`:8, `<QOU-root-loose>`:4, `HyperellipticQuintic`:2, `Geometry`:1 |
| `QOU.Confinement` | L8 | **126** | 2,396 (1,701) | 0 / 0 | 12 | 22 | `QuarkState`:43, `Interactions`:32, `ParticleInteractions`:31, `<QOU-root-loose>`:6, `OptionE`:5 |
| `QOU.EightfoldWay` | L8 | **52** | 734 (500) | 0 / 0 | 8 | 12 | `Eightfold`:43, `FlavorDressing`:6, `EightfoldWay`:2, `BaryonWeight`:1 |
| `QOU.MassTheory` | L9 | **770** | 9,903 (7,029) | 0 / 1 | 124 | 131 | `Mass`:271, `Archimedean`:255, `MassTheory`:205, `<QOU-root-loose>`:13, `MassEndomorphism`:10 |
| `QOU.Nuclear` | L10 | **406** | 5,747 (4,122) | 0 / 0 | 29 | 39 | `QBeta`:396, `ShellCondensation`:4, `Nuclear`:3, `AppendixQValues`:1, `MagicShell`:1 |
| `QOU.StandardModel` | L10 | **78** | 1,029 (659) | 0 / 0 | 21 | 15 | `StandardModel`:34, `AlphaEM`:17, `<QOU-root-loose>`:14, `QFTMath`:5, `Resurgence`:4 |
| `QOU.FluidDynamics` | L10 | **46** | 496 (337) | 0 / 0 | 3 | 2 | `FluidDynamics`:44, `<QOU-root-loose>`:1, `GaugeFieldFluidDynamics`:1 |
| `QOU.InformationTheory` | L10 | **53** | 392 (260) | 0 / 0 | 8 | 9 | `Information`:40, `<QOU-root-loose>`:9, `QGeometricLanglands`:2, `InformationTheory`:1, `QuantumComputationalUniversality`:1 |
| `QOU.Observations` | L11 | **91** | 1,124 (786) | 0 / 1 | 3 | 35 | `AppendixSurreals`:52, `Observations`:18, `Molecular`:15, `<QOU-root-loose>`:3, `Experimental`:2 |

## 5. Comparison of 3 Concrete Refactor Options (Ready for Coordinator `AskUserQuestion`)

| Dimension | **Option 1 (Recommended): Multi-`lean_lib` in `lakefile.toml`** | **Option 2: 6 Separate Lake Packages (`folio/lean-contrib/*`)** | **Option 3: Single-Lib Mirror (`QOU/Contrib/<Pkg>/*`)** |
|---|---|---|---|
| **Lake Target Architecture** | `MathlibExt` + 6 Tier-B `[[lean_lib]]` + `QOU` in `folio/quantum-observable-universe/lean/lakefile.toml` | 6 standalone `lakefile.toml` packages under `folio/lean-contrib/<pkg>/lean/` via `[[require]]` | Single `[[lean_lib]] name = "QOU"` with `QOU/Contrib/<Pkg>/*` folders |
| **`Process_GraphDetanglement` Stage** | **Stage 3 (`Isolate` in-place)** — 1-folder `git mv` away from Stage 4 extraction | **Stage 4 (`Extract` immediately)** — full multi-package split now | **Stage 2 (`Detangle` only)** — keeps `QOU.` namespace prefix |
| **Tier-B Reservoir Modules** | **1359** modules in root namespaces (`HeckeTemperleyLieb.*`, etc.) | **1359** modules in 6 new Lake packages | **1359** modules under `QOU.Contrib.<Pkg>.*` |
| **Tier-A `MathlibExt` Modules** | **321** modules (`MathlibExt.*`) | **321** modules (`MathlibExt.*`) | **321** modules (`QOU.MathlibExt.*`) |
| **Collapsed `QOU.*` Subgraphs** | `83 dirs + 106 loose` → **12 canonical `QOU.<Chapter>` dirs** (**2160** modules) | `83 dirs + 106 loose` → **12 canonical `QOU.<Chapter>` dirs** (**2160** modules) | `83 dirs + 106 loose` → **12 canonical `QOU.<Chapter>` dirs** (**2160** modules) |
| **Blocking Cut-Edges to Prune/Factor** | **188** (`Tier-A/B -> QOU.*`) | **188** (`Tier-A/B -> QOU.*`) | **188** (`Tier-A/B -> QOU.*`) |
| **Zero-`QOU.*` Boundary Enforcement** | `lake build <TierBLib>` + `lean-best-practices-lint.py --package` | Physical Lake package DAG (impossible to import `QOU.*`) + linter | Python linter (`lean-best-practices-lint.py`) only |
| **`import` Lines Rewritten (Codemod)** | ~5,765 (`QOU` + siblings) | ~5,765 (`QOU` + siblings) | ~5,765 (`QOU` + siblings) |
| **`.ts` `lean.ref` Updates** | ~1,313 (keeps `qou:<Decl>` package URI!) | ~1,313 + **6 new URI prefixes** in `schemas/lean-packages.ts` | ~1,313 (keeps `qou:QOU.Contrib...` URI) |
| **`.olean` Cache / Overlay Blast Radius** | **Low** (`0` new `.lake/build` roots; `lean-overlay-env.sh` works unchanged!) | **High** (`+6` `.lake/build/lib/lean` roots in `lean-env.sh`, overlay, & cache seeders) | **Lowest** (`0` new roots, single `QOU/` folder) |
| **Second Rename Needed for Reservoir?** | **No (0 files)** — namespaces are already Reservoir-final | **No (0 files)** | **Yes (1359 files)** must drop `QOU.Contrib.` later |
| **Estimated Effort** | **Medium (3-4 PR tranches after active Lean PRs land; 1 automated codemod + single olean reseed)** | High (5-6 PR tranches; requires updating `schemas/lean-packages.ts`, `lean-env.sh`, `lean-overlay-env.sh`, `lean-olean-cache-seed.sh`, and CI workflows for 6 new Lake build roots) | Low-Medium now (2-3 PR tranches), but incurs technical debt: every Tier-B declaration keeps a `QOU.Contrib.` prefix and requires a second breaking rename before Lean Reservoir publication. |

### Recommended Phased Execution Strategy (`qou-lref` -> `qou-lanx`)

1. **Adopt Option 1 now (`Isolate in-place`)** once active Lean PRs settle and the owner confirms via `AskUserQuestion`:
   - **Step 1 (Cut-edge surgical prep):** Resolve the **188** outbound `Tier-A/B -> QOU.*` cut-edges (`Task_Move`: factor pure base definitions out of `QOU.*` or reclassify pure targets) and re-run `scripts/lean-kg-detangler.py` until `community_to_qou_cut_edges == 0`.
   - **Step 2 (Atomic codemod + `[[lean_lib]]` isolation):** Move the 6 Tier-B subgraphs to top-level namespaces (`HeckeTemperleyLieb/`, `TwistedFrobeniusHopf/`, `ToricConicOpt/`, `CompactQuantumMetrics/`, `QCalculus/`, `BraidKnotOctonion/`) + `MathlibExt/` inside `folio/quantum-observable-universe/lean/`, collapse the remaining `QOU/*` tree into the `12` canonical chapter subgraphs, rewrite `import` and `lean.ref` strings atomically, and verify with `LEAN_NUM_THREADS=1 nice -n 15 bash scripts/lean-direct-cone.sh -j 1` + `scripts/lean-best-practices-lint.py`.
   - **Step 3 (Optional Stage 4 `Extract` to Option 2 per-library):** Whenever an individual Tier-B library (e.g., `TwistedFrobeniusHopf` or `CompactQuantumMetrics`) is ready for public Lean Reservoir indexing, `Task_Extract` lifts its already-isolated folder into a standalone repo with **zero namespace or theorem-name churn**.

