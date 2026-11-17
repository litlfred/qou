---
# qou-xyxc
title: 'KZ Step 2: ribbon lemma (q−q⁻¹)·dim_q V = a−a⁻¹ from the curl identities, instantiated to dim_q V = [2]_q'
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T18:13:09Z
updated_at: 2026-11-17T11:53:03Z
parent: qou-59vq
---

Plan from coordination doc. Lean ribbon layer exists: QOU/MathlibExt/Ribbon.lean, PivotalCategory.lean, SphericalCategory.lean.


## 2026-10-12 — DONE on branch claude/kz-ribbon-qdim-2026-10-12 (no prior 2026-10-11 ribbon branch existed)
File QOU/MathlibExt/RibbonHeckeDimension.lean, sorry-free, axioms [propext, Classical.choice, Quot.sound]:
- ribbon_hecke_dimension: k-linear ribbon C, β_{V,V} − β_{V,V}⁻¹ = (q−q⁻¹)•𝟙, θ_V = a•𝟙, a≠0, qDimTwistedWith V Vᘁ = d•𝟙 ⟹ ((q−q⁻¹)d)•𝟙_V = (a−a⁻¹)•𝟙_V.
- ribbon_hecke_qDim_eq_qint_two: a = q², q−q⁻¹≠0, 𝟙_V≠0 ⟹ d = q + q⁻¹.
- curls from the axioms: ptrWith_braiding (twistless ptr of β is 𝟙, any braided rigid C), ptrTwistWith_braiding (= θ, balanced), ptrTwistWith_braiding_inv (= θ⁻¹; uses ribbon axiom once via twist_closure_eq).
Convention: ribbon trace = closure (θ ▷ Vᘁ) ≫ β ≫ ε, matching qDimTwistedWith.
Open: no nondegenerate (q²≠1) instance exists in the tree (only symmetric θ=1, where q=q⁻¹); instantiation at D_ℏ is qou-zoyv.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `qou-xhci` → `qou-59vq`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## Progress 2026-11-17 (Round 65 — PR #8331)

- Formalized in `folio/quantum-observable-universe/lean/QOU/Foundations/CumulativeSwapCentralityTabloidTransitionCellProductFactorialCurlTrace.lean` (Lean 4.24.0, `0` `sorry`, `0` `axiom`, `0` warnings, `0` directory-mode static vacuity & borrowed-name advisories).
- 80-dps `mpmath` numerical witness stamped in `computations/probes/cumulative-swap-centrality-tabloid-transition-cell-product-factorial-curl-trace.witness.json` (`scriptHash = 9e4c62bb8c28`, `scriptCommitSha = 4331c3d6858037c7a16d08f2202e77af0fee8a52`, `HEAD = 69f8f329d2048eae2ceddcc8d14985dd544d587f`).
- PR: https://github.com/litlfred/qou/pull/8331 (`ready: 69f8f329d2048eae2ceddcc8d14985dd544d587f`).
