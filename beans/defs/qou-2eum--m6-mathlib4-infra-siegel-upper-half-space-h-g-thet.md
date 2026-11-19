---
# qou-2eum
title: 'M6 [Mathlib4 Infra]: Siegel Upper Half-Space H_g, Theta Characteristics, Bring''s Curve S₅ & X₀(15) Period Isogeny'
status: todo
type: feature
priority: high
tags:
    - lean
    - mathlib-gap
    - siegel-modular
    - brings-curve
created_at: 2026-11-19T08:19:50Z
updated_at: 2026-11-19T08:19:50Z
parent: qou-dxbw
---

## Scope & Audit Metrics (`M6_SIEGEL_THETA_MODULAR_CURVES`)

- **Source Witness:** `computations/audits/lean-axiom-field-and-mathlib-gap-audit.witness.json`
- **Mathlib4 Target Surface:** Siegel upper half-space H_g & Sp(2g,Z) modular action, Riemann theta functions & even/odd theta characteristics, Jacobian & Prym varieties, Bring's genus-4 curve S_5 automorphism representation & period matrix, modular curve X_0(15) & elliptic period isogenies, Kronecker limit formula, and polarized Epstein zeta
- **Cross-Linked Existing Beans:** `qou-k7ad`, `qou-r7qm`, `5lcg`, `qou-c8p8`, `qou-rtxm`
- **Uninstantiated / Toy Carriers:** **12** (`0` uninstantiated `class`es, `11` uninstantiated `structure`s, `1` `TOY_ONLY_INSTANCE`) across `11` `.lean` files
- **Total `Prop` Fields:** `32`  |  **Downstream Theorem/Def Consumers:** `4`
- **Standalone `axiom` / `opaque` Declarations in Cluster:** `0` `axiom`, `0` `opaque`

---

## Concrete Mathlib4 / QOU Build Plan

1. **Siegel Upper Half-Space $\mathfrak{H}_g$ & Riemann Theta Characteristics:** Define $\mathfrak{H}_g = \{\Omega \in M_g(\mathbb{C}) \mid \Omega^T = \Omega,\, \mathrm{Im}\,\Omega > 0\}$, $\mathrm{Sp}(2g, \mathbb{Z})$ action, and Riemann $\theta[\varepsilon,\delta](z, \Omega)$ parity/periodicity.
2. **Bring's Genus-4 Curve $S_5$ Automorphisms & Klein Icosahedral Bridge:** Replace the toy instance on `KleinBringIcosahedralBridge` (`brings-surface/klein-bring-icosahedral-bridge.lean:217`) and instantiate `DescartesSchurWeyl`, `DescartesBraidStructure`, `DescartesBraidRep`, and `Dic3Data` on the explicit homogeneous equations $\sum_{i=1}^5 x_i^k = 0$ ($k=1,2,3$).
3. **Modular Curve $X_0(15)$ & Elliptic Period Decomposition:** Formalize the genus-4 $\mathrm{Jac}(\mathrm{Bring}) \sim E_{15}^4$ isogeny decomposition (`JetSWArchDecomposition`) and Kronecker limit / polarized Epstein zeta identities.

---

## Top Priority Uninstantiated / Toy Carriers (Ranked by Consumer Count)

| Status | Kind | Carrier (`class` / `structure`) | Consumers | Prop Flds | Data Flds | Location (`folio/quantum-observable-universe/...`) |
|---|---|---|---:|---:|---:|---|
| `UNINST` | `structure` | `QOU.Archimedean.DescartesSchurWeyl` | 2 | 2 | 5 | `brings-surface/descartes-knot-eigenbasis.lean:219` |
| `UNINST` | `structure` | `QOU.Dic3Data` | 1 | 4 | 4 | `brings-surface/su2-generators.lean:27` |
| `UNINST` | `structure` | `QOU.Brings.JetSWArchDecomposition` | 1 | 2 | 4 | `brings-surface/jet-sw-tau-decomposition.lean:52` |
| `TOY_ONLY` | `class` | `QOU.KleinBringBridge.KleinBringIcosahedralBridge` | 0 | 6 | 0 | `brings-surface/klein-bring-icosahedral-bridge.lean:217` |
| `UNINST` | `structure` | `QOU.Archimedean.DescartesBraidStructure` | 0 | 4 | 5 | `brings-surface/descartes-braid-structure.lean:31` |
| `UNINST` | `structure` | `QOU.Archimedean.DescartesBraidRep` | 0 | 4 | 4 | `brings-surface/descartes-knot-eigenbasis.lean:254` |
| `UNINST` | `structure` | `QOU.Archimedean.GenerationScheme` | 0 | 3 | 4 | `brings-surface/generation-completeness.lean:68` |
| `UNINST` | `structure` | `QOU.Brings.BriggsKleinChart` | 0 | 2 | 3 | `brings-surface/briggs-klein-chart.lean:41` |
| `UNINST` | `structure` | `QN` | 0 | 2 | 3 | `brings-surface/orbital-fourier-decomposition.lean:71` |
| `UNINST` | `structure` | `QOU.Archimedean.TorusKnotRep` | 0 | 1 | 3 | `brings-surface/cohomological-embedding.lean:44` |
| `UNINST` | `structure` | `QOU.AlgebraicSubstrate.LocalCohomologyGroup` | 0 | 1 | 4 | `brings-surface/local-cohomology-group.lean:34` |
| `UNINST` | `structure` | `QOU.AlgebraicSubstrate.MaximalIdealDefect` | 0 | 1 | 4 | `brings-surface/maximal-ideal-defect.lean:35` |

---

## Standalone `axiom` / `opaque` Declarations in `M6_SIEGEL_THETA_MODULAR_CURVES` (Sample up to 15)

- *(none)*
