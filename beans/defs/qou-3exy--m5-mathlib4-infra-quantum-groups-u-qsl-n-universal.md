---
# qou-3exy
title: 'M5 [Mathlib4 Infra]: Quantum Groups U_q(sl_N), Universal R-Matrix, Ribbon/Modular Categories & GPMT Modified Traces'
status: todo
type: feature
priority: high
tags:
    - lean
    - mathlib-gap
    - quantum-groups
    - modular-categories
created_at: 2026-11-19T08:19:50Z
updated_at: 2026-11-19T08:19:50Z
parent: qou-dxbw
---

## Scope & Audit Metrics (`M5_QUANTUM_GROUPS_RIBBON_GPMT`)

- **Source Witness:** `computations/audits/lean-axiom-field-and-mathlib-gap-audit.witness.json`
- **Mathlib4 Target Surface:** Drinfeld–Jimbo quantum groups U_q(sl_N) & quantum Casimir, universal R-matrix & Yang–Baxter, Jimbo quantum Schur–Weyl duality, pivotal / spherical / ribbon / modular tensor categories, Reshetikhin–Turaev tangle functor, and Geer–Patureau-Mirand–Turaev (GPMT) modified traces & modified quantum dimensions
- **Cross-Linked Existing Beans:** `qou-o9ge`, `rtqd`, `rtrb`, `bwrt`, `hkmt`, `qou-ga7i`, `qou-xsmr`, `qou-c8p8`, `qou-rtxm`
- **Uninstantiated / Toy Carriers:** **28** (`14` uninstantiated `class`es, `13` uninstantiated `structure`s, `1` `TOY_ONLY_INSTANCE`) across `23` `.lean` files
- **Total `Prop` Fields:** `65`  |  **Downstream Theorem/Def Consumers:** `100`
- **Standalone `axiom` / `opaque` Declarations in Cluster:** `2` `axiom`, `1` `opaque`

---

## Concrete Mathlib4 / QOU Build Plan

1. **Concrete $U_q(\mathfrak{sl}_2) / U_q(\mathfrak{sl}_N)$ & Quantum Casimir Realization:** Construct concrete weight-module instances of `QuantumSu2` (`CasimirShared.lean`, 24 consumers) and `QuantumSu2Relations` (`braids-and-knots/q-casimir.lean`, 12 consumers), eliminating `QCasimir_comm_E_axiom` / `QCasimir_comm_F_axiom`.
2. **Universal $R$-Matrix, Vassiliev Chord Diagrams & Jimbo Schur–Weyl Duality:** Instantiate `RMatrix`, `BraidRelation`, and concrete finite-type `ChordDiagram` (4T relation) on $V^{\otimes n}$ commuting with $H_n(q)$.
3. **Pivotal / Spherical / Ribbon Categories & GPMT Modified Quantum Dimensions:** Build `PivotalCategory` $\to$ `SphericalCategory` $\to$ `RibbonCategory` over Mathlib's `MonoidalCategory` + `BraidedCategory`, replace the toy instance of `RootOfUnityMTCTruncation`, and connect ambiprojective ideal traces to `gpmt_dmod`.

---

## Top Priority Uninstantiated / Toy Carriers (Ranked by Consumer Count)

| Status | Kind | Carrier (`class` / `structure`) | Consumers | Prop Flds | Data Flds | Location (`folio/quantum-observable-universe/...`) |
|---|---|---|---:|---:|---:|---|
| `UNINST` | `structure` | `QOU.QuantumSu2` | 24 | 3 | 6 | `lean/QOU/BraidKnot/CasimirShared.lean:56` |
| `UNINST` | `structure` | `QOU.KnotTheory.Vassiliev.ChordDiagram` | 21 | 1 | 2 | `lean/QOU/KnotTheory/Vassiliev/ChordDiagram.lean:46` |
| `UNINST` | `class` | `QOU.QuantumSu2Relations` | 12 | 3 | 0 | `braids-and-knots/q-casimir.lean:98` |
| `SHIM_UNIN` | `structure` | `QOU.Torsion.CategoricalTransferMatrix` | 9 | 3 | 3 | `lean/QOU/Torsion/MassGap.lean:142` |
| `UNINST` | `class` | `QOU.BraidKnot.BraidRelation` | 5 | 2 | 0 | `lean/QOU/BraidKnot/YangBaxterBlowupTruncation.lean:22` |
| `UNINST` | `structure` | `QOU.PathIntegrals.RMatrix` | 4 | 3 | 3 | `lean/QOU/PathIntegrals.lean:260` |
| `TOY_ONLY` | `class` | `QOU.BraidKnot.RootOfUnityMTCTruncation` | 3 | 4 | 1 | `lean/QOU/BraidKnot/RootOfUnityMTCTruncation.lean:45` |
| `UNINST` | `structure` | `QOU.QuantumSu2` | 3 | 3 | 6 | `braids-and-knots/quantum-su2.lean:45` |
| `UNINST` | `structure` | `QOU.Archimedean.TransferMatrixOperator` | 3 | 2 | 3 | `lean/QOU/Archimedean/TransferMatrixOperator.lean:25` |
| `UNINST` | `class` | `QOU.Interactions.TransferMatrixEigenphase` | 3 | 2 | 0 | `nuclear-interactions/q-beta-cos-resummation.lean:318` |
| `UNINST` | `structure` | `QOU.PAdicQuantumGroups.FiniteFieldQOU` | 2 | 3 | 3 | `lean/QOU/PAdicQuantumGroups.lean:88` |
| `UNINST` | `class` | `QOU.BraidKnot.YangBaxterRule` | 2 | 1 | 1 | `mass-theory/ck-extraction-from-algebraic-rules.lean:71` |
| `UNINST` | `class` | `QOU.Archimedean.SkeinPolynomialTransferMatrixContext` | 1 | 3 | 7 | `lean/QOU/Archimedean/skein_polynomial_transfer_matrix.lean:25` |
| `UNINST` | `class` | `QOU.Information.ToffoliTransferMatrixContext` | 1 | 3 | 6 | `lean/QOU/Information/toffoli_transfer_matrix.lean:41` |
| `UNINST` | `structure` | `QOU.KnotTheory.Vassiliev.VassilievSetup` | 1 | 3 | 1 | `lean/QOU/KnotTheory/Vassiliev/FiniteTypeInvariant.lean:62` |
| `UNINST` | `class` | `QOU.KnotTheory.Vassiliev.BrunnianVassilievBridge` | 1 | 2 | 0 | `lean/QOU/KnotTheory/Vassiliev/MilnorVassilievBridge.lean:85` |
| `UNINST` | `class` | `QOU.MassTheory.MilnorVassilievGrading.BarSymmetricDegreeDoubling` | 1 | 2 | 0 | `lean/QOU/MassTheory/MilnorVassilievGrading.lean:88` |
| `UNINST` | `class` | `QOU.Atomicity.RankOneToSingleObject.TannakianRankOneSingleGenerator` | 1 | 1 | 0 | `lean/QOU/ParticleInteractions/AtomicityRankOneToSingleObject.lean:211` |
| `UNINST` | `class` | `QOU.Atomicity.SelfDualToSymplectic` | 1 | 1 | 0 | `lean/QOU/ParticleInteractions/AtomicitySelfDualToSymplectic.lean:102` |
| `UNINST` | `structure` | `QOU.Torsion.TwoPointFunction` | 1 | 1 | 3 | `lean/QOU/Torsion/MassGap.lean:171` |

---

## Standalone `axiom` / `opaque` Declarations in `M5_QUANTUM_GROUPS_RIBBON_GPMT` (Sample up to 15)

- `axiom QOU.QCasimir_comm_E_axiom` (`braids-and-knots/q-casimir.lean:547`)
- `axiom QOU.QCasimir_comm_F_axiom` (`braids-and-knots/q-casimir.lean:565`)
- `opaque QOU.KnotTheory.JonesPolynomial.jonesAt` (`lean/QOU/KnotTheory/JonesPolynomial.lean:85`)
