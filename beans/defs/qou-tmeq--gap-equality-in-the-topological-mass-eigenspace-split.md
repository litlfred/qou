---
# qou-tmeq
title: 'GAP: equality in lem:topological-mass-eigenspace-decomp (norm additivity of the multiplicative integral over the descent split)'
status: todo
type: task
priority: normal
created_at: 2026-11-20T16:45:00Z
updated_at: 2026-11-20T16:45:00Z
parent: qou-27ys
---

Opened by tm on owner approval of D3 (2026-11-20, relayed by the coordinator on #8526). Do NOT close while the equality is open.

`lem:topological-mass-eigenspace-decomp` stated `m(ϱ) = ‖MI∫ τ̂(α)‖ + ‖MI∫ (α − τ̂(α))‖`, justified by Killing-form orthogonality. Branch `claude/topological-mass-ray-followup-2026-11-20` restates it as `≤`, granted the factorisation `MI∫α = MI∫τ̂(α) · MI∫(α − τ̂(α))`. The Lean is `QOU.LiftingDescent.tm_eigenspace_decomp_norm_le` (content sibling, sorry-free). This bean holds the equality.

Known facts:
- Orthogonality cannot give it. Two non-zero orthogonal vectors satisfy the triangle inequality strictly: `QOU.Torsion.norm_add_lt_of_inner_eq_zero` (PR #8581).
- In a strictly convex normed space, equality holds iff the two pieces lie on a common ray: `QOU.Torsion.mass_decomposition_eq_iff` / `norm_sum_eq_sum_norm_iff` (PR #8581). For values in `Multiplicative ℝ` this means their logarithms share a sign: `transient_norm_equality_mult_iff`.
- The library conditional `QOU.LiftingDescent.tm_eigenspace_decomp` (in `lean/QOU/LiftingDescent/tm_eigenspace_decomp.lean`) carries a class field `mi_additive`, which makes MI additive on Killing-orthogonal pairs. No actual inner-product norm satisfies it on non-zero orthogonal pairs, so that class has no honest instance with `MI = norm`.
- The factorisation `MI∫(x+y) = MI∫x · MI∫y` itself is also unproved for non-commuting pieces. It is a hypothesis of the ≤ form.

Next honest step: decide whether the two multiplicative integrals share a ray (a phase) for the actual integrand, or show that they generically do not (scope (a), numerical) or provably cannot (scope (b), needs an invariant).
