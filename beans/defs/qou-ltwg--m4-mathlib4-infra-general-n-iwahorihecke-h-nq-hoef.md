---
# qou-ltwg
title: 'M4 [Mathlib4 Infra]: General-n Iwahori–Hecke H_n(q), Hoefsmit/Murphy Bases, Ocneanu Markov Trace & Macdonald/Plancherel'
status: todo
type: feature
priority: high
tags:
    - lean
    - mathlib-gap
    - hecke-algebra
    - representation-theory
created_at: 2026-11-19T08:19:50Z
updated_at: 2026-11-20T15:45:46Z
parent: qou-dxbw
---

## Scope & Audit Metrics (`M4_HECKE_MARKOV_SPECHT_MACDONALD`)

- **Source Witness:** `computations/audits/lean-axiom-field-and-mathlib-gap-audit.witness.json`
- **Mathlib4 Target Surface:** General-n Iwahori–Hecke algebras H_n(q), Coxeter/braid presentation, Hoefsmit seminormal & Murphy cellular / Kazhdan–Lusztig bases, Ocneanu–Jones–Wenzl Markov trace & Temperley–Lieb tower, Specht / RSK / skew-SYT branching, Macdonald hook-content / Demazure / Kashiwara crystals / q-Plancherel Feray–Meliot CLT, and Grobner–Shirshov diamond
- **Cross-Linked Existing Beans:** `qou-59vq`, `qou-k4oq`, `qou-0cyu`, `qou-1oif`, `qou-1o8n`, `qou-utb3`, `qou-ep0a`, `qou-c8p8`, `qou-rtxm`
- **Uninstantiated / Toy Carriers:** **204** (`123` uninstantiated `class`es, `74` uninstantiated `structure`s, `7` `TOY_ONLY_INSTANCE`) across `137` `.lean` files
- **Total `Prop` Fields:** `408`  |  **Downstream Theorem/Def Consumers:** `357`
- **Standalone `axiom` / `opaque` Declarations in Cluster:** `13` `axiom`, `18` `opaque`

---

## Concrete Mathlib4 / QOU Build Plan

1. **General-$n$ `IwahoriHecke` Algebra & Ocneanu–Jones–Wenzl Markov Tower:** Construct the $R[q,q^{-1}]$-free module $H_n(q)$ of rank $n!$ via Bourbaki/Matsumoto exchange + Jones basic construction, instantiating `HeckeBraidedPresentationOfRank`, `MarkovTrace`, `MarkovStabilization`, `MarkovTraceN` (replacing toy instances), and `DirectLimitAlgebra`.
2. **Hoefsmit Seminormal, Jucys–Murphy Cellular & Skew-SYT Branching:** Construct concrete non-empty `SkewStandardYoungTableau` (`YoungTableauStandard.lean`, replacing the empty-only toy witness), `StandardTableau`, and general-$n$ Hoefsmit/Murphy matrix representations.
3. **Concrete $q$-Plancherel & Macdonald Hook-Content Instances:** Replace the `Fin 1` toy witnesses (`unitQDimension`, `badPartitionFunction` in `QOU/MathlibExt/QPlancherel.lean`) with genuine partition-indexed `QDimension` and `HasPartitionFunction` instances backed by proved $4\times 4$ Hankel / Cauchy–Binet & Macdonald hook-content sums.

---

## Top Priority Uninstantiated / Toy Carriers (Ranked by Consumer Count)

| Status | Kind | Carrier (`class` / `structure`) | Consumers | Prop Flds | Data Flds | Location (`folio/quantum-observable-universe/...`) |
|---|---|---|---:|---:|---:|---|
| `TOY_ONLY` | `structure` | `QOU.BraidKnot.YoungTableauStandard.SkewStandardYoungTableau` | 27 | 4 | 1 | `lean/QOU/BraidKnot/YoungTableauStandard.lean:112` |
| `TOY_ONLY` | `class` | `QOU.MathlibExt.QPlancherel.QDimension` | 11 | 0 | 1 | `lean/QOU/MathlibExt/QPlancherel.lean:56` |
| `UNINST` | `structure` | `QOU.Torsion.DirectLimitAlgebra` | 9 | 5 | 9 | `lean/QOU/Torsion/BraneTower.lean:41` |
| `UNINST` | `class` | `QOU.BraidKnot.HasRealAxisData` | 9 | 1 | 2 | `lean/QOU/BraidKnot/ConfinementPhaseStratification.lean:47` |
| `UNINST` | `structure` | `QOU.BraidKnot.Keystone.StandardTableau` | 8 | 3 | 0 | `lean/QOU/BraidKnot/StandardTableauSpectral.lean:69` |
| `UNINST` | `structure` | `QOU.BraidKnot.StokesSurfaceBoundary.HoefsmitGen` | 8 | 1 | 3 | `lean/QOU/BraidKnot/nonabelian_stokes_surface_boundary_stokes.lean:260` |
| `UNINST` | `structure` | `QOU.Braiding.HeckeMassElement` | 8 | 1 | 4 | `lean/QOU/Torsion/HeckeMassElement.lean:62` |
| `UNINST` | `structure` | `QOU.BraidKnot.IsMarkovTrace` | 7 | 5 | 0 | `mass-endomorphism/markov-trace-recursive-reducer.lean:161` |
| `SHIM_UNIN` | `structure` | `QOU.Torsion.VacuumState` | 7 | 2 | 1 | `lean/QOU/Torsion/BraneTower.lean:66` |
| `UNINST` | `structure` | `QOU.Mass.GammaGammaH6Interface.InterfaceBranching` | 7 | 1 | 0 | `lean/QOU/Mass/GammaGammaH6Interface.lean:245` |
| `UNINST` | `class` | `QOU.Braiding.MarkovTraceAxioms` | 6 | 2 | 1 | `mass-theory/markov-trace-product.lean:83` |
| `UNINST` | `class` | `QOU.BraidKnot.ShellNeutrality.Saturated` | 6 | 0 | 0 | `lean/QOU/BraidKnot/ShellNeutrality.lean:260` |
| `UNINST` | `structure` | `QOU.Torsion.TopologicalMassDecomposition` | 5 | 6 | 7 | `lean/QOU/Torsion/TopologicalMass.lean:63` |
| `UNINST` | `class` | `QOU.BraidKnot.HasSDPRegularity` | 5 | 4 | 0 | `lean/QOU/BraidKnot/ConfinementPhaseStratification.lean:103` |
| `UNINST` | `class` | `QOU.BraidKnot.GradedTraceResidueSplit` | 5 | 3 | 5 | `lean/QOU/BraidKnot/GradedTraceResidueSplit.lean:55` |
| `UNINST` | `class` | `QOU.BraidKnot.MarkovTraceAxioms` | 5 | 2 | 2 | `lean/QOU/BraidKnot/MarkovAxiomsPrimitive.lean:146` |
| `UNINST` | `class` | `QOU.BraidKnot.PanelImageStructure` | 5 | 2 | 1 | `lean/QOU/BraidKnot/StructuralRank.lean:222` |
| `SHIM_UNIN` | `class` | `QOU.BraidKnot.GBResidueSpectralSum` | 5 | 1 | 7 | `lean/QOU/BraidKnot/GBResidueSpectralSum.lean:67` |
| `UNINST` | `class` | `QOU.BraidKnot.IwahoriHeckeAPI.IwahoriHeckeAlgebra.HeckeQuadratic` | 5 | 1 | 0 | `lean/QOU/BraidKnot/IwahoriHeckeAPI.lean:107` |
| `UNINST` | `structure` | `QOU.Mathlib.KL.KLBasis` | 5 | 1 | 1 | `lean/QOU/Mathlib/KazhdanLusztigBasis.lean:123` |

---

## Standalone `axiom` / `opaque` Declarations in `M4_HECKE_MARKOV_SPECHT_MACDONALD` (Sample up to 15)

- `axiom QOU.VertexAlgebra.MarkovTrace` (`climax-volume-mass/vertex-algebra-relations.lean:108`)
- `axiom QOU.VertexAlgebra.markov_conjugation` (`climax-volume-mass/vertex-algebra-relations.lean:161`)
- `axiom QOU.VertexAlgebra.markov_stabilisation` (`climax-volume-mass/vertex-algebra-relations.lean:172`)
- `axiom QOU.VertexAlgebra.markov_nondegenerate` (`climax-volume-mass/vertex-algebra-relations.lean:185`)
- `opaque QOU.BraidsAndKnots.HeckeAlgebra` (`knots-particles-confinement/confinement-grading-correspondence-conditional.lean:45`)
- `opaque QOU.BraidsAndKnots.KLRModule` (`knots-particles-confinement/confinement-grading-correspondence-conditional.lean:55`)
- `opaque QOU.BraidsAndKnots.KLRTopDegree` (`knots-particles-confinement/confinement-grading-correspondence-conditional.lean:59`)
- `opaque QOU.BraidKnot.GramSeminormalBlock.dimLambda` (`lean/QOU/BraidKnot/GramSeminormalBlock.lean:104`)
- `opaque QOU.BraidKnot.IwahoriHeckeAPI.IwahoriHeckeAlgebra.jucysMurphy` (`lean/QOU/BraidKnot/IwahoriHeckeAPI.lean:294`)
- `opaque QOU.BraidKnot.IwahoriHeckeAPI.IwahoriHeckeAlgebra.centralIdempotent` (`lean/QOU/BraidKnot/IwahoriHeckeAPI.lean:301`)
- `axiom QOU.BraidKnot.IwahoriHeckeAPI.IwahoriHeckeAlgebra.centralIdempotent_central_axiom` (`lean/QOU/BraidKnot/IwahoriHeckeAPI.lean:313`)
- `axiom QOU.BraidKnot.IwahoriHeckeAPI.IwahoriHeckeAlgebra.centralIdempotent_orthogonal_axiom` (`lean/QOU/BraidKnot/IwahoriHeckeAPI.lean:333`)
- `axiom QOU.BraidKnot.IwahoriHeckeAPI.IwahoriHeckeAlgebra.bar_centralIdempotent_transpose_axiom` (`lean/QOU/BraidKnot/IwahoriHeckeAPI.lean:372`)
- `opaque QOU.BraidKnot.PSDFeasibilityProxy.braidWordEval` (`lean/QOU/BraidKnot/PSDFeasibilityProxy.lean:74`)
- `opaque QOU.BraidKnot.S5bbGeometricIndex.EquivariantIndex` (`lean/QOU/BraidKnot/S5bbGeometricIndex.lean:34`)

## 2026-11-20 — W7 slice (PR #8541, session_01VQDpPfKSC33hwjyKMw3EHV)

- **Done:** `QOU/MathlibExt/QPlancherelPartitionInstance.lean` is the first non-toy inhabitant of `QDimension` and `HasPartitionFunction`: the hook-length `d_q` on `Σ n, Nat.Partition n`, and `Z_q(k) = Σ_{p ⊢ k} d_q²`. `Z_pos` is derived from `molienSum_eq_qFactorial`, and total mass one is proved. Sorry-free; the library sweep passed (120 ok).
- **Not done:** `HasQPlancherelCLT` (Féray–Méliot) is still uninstantiated. The general-n Hecke algebra and Ocneanu tower were not attempted.
- **Audit misclassification (likely):** `SkewStandardYoungTableau` is listed `TOY_ONLY` with 27 consumers. Its only explicit term is the containment counterexample `skewSYT_nonempty_of_not_le`, but genuine skew tableaux are counted in `QOU.Mathlib.SkewBranchingSum` / `SkewSYTBranchingBijection`, and `RSKIdentitiesContext` is inhabited (`SkewBranchingTwoOne`). The carrier is a data structure, not an axiom-field. I could not re-check against the scanner because the scanner is not on main (see GAP bean `qou-dx7g`).

## 2026-11-20 (later) — MarkovTraceAxioms restated (PR #8596, owner options 2 + 3)

- All three `MarkovTraceAxioms` classes (`BraidKnot`, `Hecke`, `Braiding`) could be filled in one line and carried no trace. They are removed. The factorisation theorems keep their names and are proved over any genuine `OcneanuTrace.MarkovTrace`, for ascending affine words (`tr_chainWord`). The general-word version is false, and the scope is stated. The `QOU.Braiding` duplicate is deleted. At n = 2 the result is proved on the concrete `H₂(q)`.
- **Still the M4 gap:** no genuine `OcneanuTrace.MarkovTrace` exists on `H_∞(q)` at `q ≠ 1`.

## 2026-11-20T21:28:46Z — correction + status

Earlier this session I described "a genuine Markov trace on H_∞(q) at q≠1" as open. That was
wrong: HeckeColimitMarkovTrace (convention D) and WenzlMarkovTraceInstance (every level r)
already had it. What was open was arbitrary z; closed in PR #8689 (see qou-uer7).
