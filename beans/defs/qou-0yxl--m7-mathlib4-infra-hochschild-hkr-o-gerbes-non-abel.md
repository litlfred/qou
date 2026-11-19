---
# qou-0yxl
title: 'M7 [Mathlib4 Infra]: Hochschild HKR, O^×-Gerbes, Non-Abelian 2-Stokes, Surreal Transfer, q-Borel & Conic SDP Duality'
status: todo
type: feature
priority: high
tags:
    - lean
    - mathlib-gap
    - homological-algebra
    - convex-duality
created_at: 2026-11-19T08:19:50Z
updated_at: 2026-11-19T08:19:50Z
parent: qou-dxbw
---

## Scope & Audit Metrics (`M7_HOCHSCHILD_GERBES_STOKES_QBOREL_SDP`)

- **Source Witness:** `computations/audits/lean-axiom-field-and-mathlib-gap-audit.witness.json`
- **Mathlib4 Target Surface:** Hochschild homology/cohomology HH_* & HKR isomorphism, O^x-gerbe cohomology & spectral sequences, manifold differential k-forms / contact forms & Yekutieli non-abelian Stokes 2-holonomy, Conway surreal / Hahn / hyperreal transfer, q-Gevrey / q-Borel–Laplace / Ramis–Sauloy alien derivations, Carleman–Frechet–Shohat moment determinacy, and conic SDP strong duality under Slater / Goldman–Tucker strict complementarity
- **Cross-Linked Existing Beans:** `qou-a8rj`, `qou-6ers`, `qou-ghc6`, `qou-jvua`, `qou-vspi`, `qou-pan0`, `qou-7b7v`, `qou-x1rm`, `qou-yc05`, `qou-9h4t`, `hypr`, `qou-c8p8`, `qou-rtxm`
- **Uninstantiated / Toy Carriers:** **138** (`63` uninstantiated `class`es, `71` uninstantiated `structure`s, `4` `TOY_ONLY_INSTANCE`) across `97` `.lean` files
- **Total `Prop` Fields:** `271`  |  **Downstream Theorem/Def Consumers:** `328`
- **Standalone `axiom` / `opaque` Declarations in Cluster:** `3` `axiom`, `32` `opaque`

---

## Concrete Mathlib4 / QOU Build Plan

1. **Hochschild Homology $HH_\bullet$, Čech/Gerbe Cohomology & Spectral Sequences:** Instantiate `Cover` & `Refines` (`QOU/MathlibExt/CechColimit.lean`, 56 combined consumers), `LES` (`LongExactSequence.lean`, 12 consumers), `SpectralSequencePage`, and $\mathcal{O}^\times$-gerbe 2-cocycle classes.
2. **Manifold Differential $k$-Forms, Contact Structures & Non-Abelian 2-Stokes:** Extend Mathlib's normed-space `DifferentialForm` to smooth manifolds (`qou-jvua`, `qou-ghc6`) to instantiate `ContactForm`, `CoreLeviFormContext`, and Yekutieli multiplicative-integral 2-holonomy.
3. **Surreal/Hyperreal Transfer, $q$-Borel/Carleman Moment Determinacy & Conic SDP Strong Duality:** Instantiate `SurrealField` (`AppendixSurreals/Basic.lean`, 29 consumers) via Mathlib `Hyperreal` (`hypr`), formalize $q$-Gevrey / Ramis–Sauloy `AlienDerivationSystem` & Stone–Weierstrass compact-support `StieltjesDeterminate`, and build finite-dimensional conic/SDP Slater duality (`HasFiniteLPDuality`, `StrictComplementarityPair`).

---

## Top Priority Uninstantiated / Toy Carriers (Ranked by Consumer Count)

| Status | Kind | Carrier (`class` / `structure`) | Consumers | Prop Flds | Data Flds | Location (`folio/quantum-observable-universe/...`) |
|---|---|---|---:|---:|---:|---|
| `UNINST` | `structure` | `QOU.CentralExtension.CechGerbe.Cover` | 45 | 1 | 2 | `lean/QOU/MathlibExt/CechColimit.lean:96` |
| `UNINST` | `class` | `QOU.AppendixSurreals.SurrealField` | 29 | 8 | 3 | `lean/QOU/AppendixSurreals/Basic.lean:54` |
| `UNINST` | `class` | `QOU.AppendixSurreals.QCollatz` | 15 | 9 | 5 | `lean/QOU/AppendixSurreals/QCollatz.lean:65` |
| `UNINST` | `structure` | `QOU.Mathlib.LongExactSequence.LES` | 12 | 2 | 0 | `lean/QOU/Mathlib/LongExactSequence.lean:70` |
| `UNINST` | `structure` | `QOU.CentralExtension.CechGerbe.Cover.Refines` | 11 | 2 | 1 | `lean/QOU/MathlibExt/CechColimit.lean:106` |
| `UNINST` | `structure` | `MvPolynomial.SubmultSeminorm` | 10 | 5 | 0 | `lean/QOU/Mathlib/RothAuxiliaryPolynomial.lean:460` |
| `UNINST` | `structure` | `QOU.Machinery.CoxeterParabolic.MarkedPair` | 8 | 2 | 2 | `lean/QOU/Machinery/HeckeTauAssignmentGroupoidFunctor.lean:128` |
| `UNINST` | `class` | `QOU.MathlibExt.FrechetShohat.CarlemanDeterminacyStieltjes` | 7 | 1 | 0 | `lean/QOU/MathlibExt/FrechetShohat.lean:232` |
| `UNINST` | `structure` | `QOU.Archimedean.YekutieliObstructionData` | 6 | 2 | 3 | `lean/QOU/Archimedean/yekutieli_leading_coefficient.lean:90` |
| `UNINST` | `structure` | `QOU.AlgebraicSubstrate.LeviFormDefect` | 6 | 1 | 2 | `brings-surface/levi-form-defect.lean:94` |
| `UNINST` | `structure` | `QOU.Mathlib.BarGradedCollapse.BarInvolution` | 6 | 1 | 1 | `lean/QOU/Mathlib/BarGradedCollapse.lean:62` |
| `UNINST` | `structure` | `QOU.Torsion.IdempotentEndomorphism` | 6 | 1 | 1 | `lifting-and-descent/descent-eigenspaces.lean:26` |
| `SHIM_UNIN` | `structure` | `QOU.QuToQou` | 5 | 3 | 6 | `lifting-and-descent/qu-to-qou.lean:74` |
| `UNINST` | `structure` | `QOU.LiftingDescent.BBStratification.SpectralSequence` | 5 | 2 | 1 | `lean/QOU/LiftingDescent/BBStratification.lean:100` |
| `UNINST` | `structure` | `QOU.Torsion.CosimplicialCrossedGroupoid` | 5 | 2 | 5 | `lean/QOU/Torsion/YekutieliTriple.lean:112` |
| `UNINST` | `class` | `QOU.AppendixSurreals.VacuumEpsilon'` | 5 | 1 | 0 | `lean/QOU/AppendixSurreals/Conjectures.lean:410` |
| `UNINST` | `structure` | `QOU.Archimedean.SurrealPrune.SqueezeGrading` | 5 | 1 | 0 | `lean/QOU/Archimedean/SurrealGradingPrune.lean:103` |
| `UNINST` | `structure` | `QOU.CentralExtension.CechGerbe.TwistedCocycle` | 5 | 1 | 0 | `lean/QOU/MathlibExt/CechGerbe.lean:233` |
| `UNINST` | `class` | `QOU.ShellCondensation.HomologicalConjecture` | 5 | 1 | 1 | `mass-endomorphism/homological-shell-condensation.lean:59` |
| `UNINST` | `class` | `QOU.Archimedean.YekutieliStokesNormalisation` | 4 | 2 | 1 | `lean/QOU/Archimedean/yekutieli_leading_coefficient.lean:221` |

---

## Standalone `axiom` / `opaque` Declarations in `M7_HOCHSCHILD_GERBES_STOKES_QBOREL_SDP` (Sample up to 15)

- `opaque QOU.AppendixSurreals.B1HyperbolicRowsTheorem.BlochSuslinRegulator` (`lean/QOU/AppendixSurreals/B1HyperbolicRowsTheorem.lean:64`)
- `opaque QOU.AppendixSurreals.B1HyperbolicRowsTheorem.VanDerVeenVolumeConjecture` (`lean/QOU/AppendixSurreals/B1HyperbolicRowsTheorem.lean:69`)
- `opaque QOU.AppendixSurreals.B1HyperbolicRowsTheorem.B1HoldsAt` (`lean/QOU/AppendixSurreals/B1HyperbolicRowsTheorem.lean:73`)
- `axiom QOU.AppendixSurreals.B1HyperbolicRowsTheorem.b1_holds_at_row` (`lean/QOU/AppendixSurreals/B1HyperbolicRowsTheorem.lean:83`)
- `opaque QOU.AppendixSurreals.QOU_FrobeniusPairing` (`lean/QOU/AppendixSurreals/Conjectures.lean:150`)
- `opaque QOU.AppendixSurreals.QOU_ObservabilityNorm` (`lean/QOU/AppendixSurreals/Conjectures.lean:155`)
- `opaque QOU.AppendixSurreals.QOU_VacuumEnergy` (`lean/QOU/AppendixSurreals/Conjectures.lean:161`)
- `opaque QOU.BraidKnot.StrictlyFeasible` (`lean/QOU/BraidKnot/ConfinementPhaseStratification.lean:92`)
- `opaque QOU.BraidKnot.ExplicitCentralIdempotent.SYT` (`lean/QOU/BraidKnot/ExplicitCentralIdempotent.lean:42`)
- `opaque QOU.BraidKnot.ExplicitCentralIdempotent.centralIdempotent` (`lean/QOU/BraidKnot/ExplicitCentralIdempotent.lean:74`)
- `opaque QOU.BraidKnot.S5bbGeometricIndex.Manifold5` (`lean/QOU/BraidKnot/S5bbGeometricIndex.lean:24`)
- `opaque QOU.BraidKnot.S5bbGeometricIndex.VectorField` (`lean/QOU/BraidKnot/S5bbGeometricIndex.lean:25`)
- `opaque QOU.BraidKnot.S5bbGeometricIndex.WenzlWeights` (`lean/QOU/BraidKnot/S5bbGeometricIndex.lean:26`)
- `opaque QOU.BraidsKnots.AtomicKnot` (`lean/QOU/BraidsKnots/LinearJSJVolume.lean:13`)
- `opaque QOU.BraidsKnots.Vol` (`lean/QOU/BraidsKnots/LinearJSJVolume.lean:21`)
