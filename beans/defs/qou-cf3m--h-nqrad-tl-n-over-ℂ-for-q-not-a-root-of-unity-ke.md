---
# qou-cf3m
title: H_n(q)/rad ≅ TL_n over ℂ for q not a root of unity; kernel of the Hecke action on (ℂ²)^{⊗n} (also OS kernel r>n at n=2)
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T20:03:36Z
updated_at: 2026-10-12T20:48:16Z
parent: qou-xhci
---

2026-10-12 (session 01A1cKZc, PR #7768): PROVED sorry-free, `QOU/SchurWeyl/JimboKernelGeneric.lean`, over any CharZero field K, q ≠ 0, NotRootOfUnity q (so ℂ included):
- `ker_jimbo_eq_traceRadicalIdeal_generic`: ker(Jimbo on (K²)^{⊗(m+1)}) = traceRadicalIdeal(wtrace). The ordered-field hypothesis of JimboActionKernel is removed.
- `tlTraceQuotEquiv` / `traceQuotTLEquiv`: TL_{m+1}(q+q⁻¹) ≃ₐ H_{m+1}(q)/rad, π(σ_i) ↦ q − e_i (`traceQuotTLEquiv_σ`).
- `jimbo_eq_comp`: jimbo = tlRep ∘ heckeToTLGeneric.
- `tlRep_injective`: TL acts faithfully on V^{⊗(m+1)}.
- `finrank_tl_eq_catalan_generic`, `finrank_range_jimbo_eq_catalan_generic`: dimension catalan(m+1). ℂ instances `*_complex`.
Route, with no positivity: (1) ker ⊆ rad is formal via jimboTrace = wtrace. (2) TL relations hold in H/rad because they hold after Jimbo, giving a surjection TL → H/rad. (3) dim TL ≤ catalan and dim H/rad = catalan (TraceQuotGeneric), so the surjection is bijective. (4) jimbo = tlRep∘ψ⁻¹∘π on generators, so rad ⊆ ker.
Axioms: propext, Classical.choice, Quot.sound only. Verified with lean-direct against a shadow rebuild of the stale cone (≈180 modules).
Remaining: CharZero is inherited from heckeProduct (the dimension of H/rad). Not covered: positive characteristic, roots of unity, and the OS-kernel item (r>n at n=2).
