---
# qou-cf3m
title: H_n(q)/rad ≅ TL_n over ℂ for q not a root of unity; kernel of the Hecke action on (ℂ²)^{⊗n} (also OS kernel r>n at n=2)
status: todo
type: task
priority: normal
created_at: 2026-10-12T20:03:36Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-59vq
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

## Parented 2026-11-15 (owner-approved bean triage)

Parent `qou-xhci` → `qou-59vq`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## Re-scoped 2026-11-15 (owner tap, E1 bean triage)

H_n(q)/rad ≅ TL_n over ℂ at q not a root of unity is proved (#7768, merged 2026-10-13). **Still open:** positive characteristic, roots of unity, and the OS kernel for r>n at n=2. This bean now tracks only those.

- Round 73 (`lane-e667`): Formalized `qou-0fmb`, `qou-4lft`, `qou-avt2`, `qou-cf3m`, `qou-g6vb` in `QOU.Foundations.TowerCompatibilityRootOfUnitySeminormalNormalizationRadicalKernelBilinearSymmetry` with 80-dps `mpmath` 2-commit witness stamp (`98224baac4097812a7a075b15a3d78cd7d6d0f26` -> `57db1e21b3add3a8efd73f5cd0f4cff40a2a1827`, `scriptHash=28e0042d776cdc079c85f0254ab21558d7f5b492e88420dbd3fa8ba157431743`) in PR `litlfred/qou#8394` (`status: in-progress`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8394, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
