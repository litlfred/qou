---
# qou-tmeq
title: 'GAP: equality in lem:topological-mass-eigenspace-decomp (norm additivity of the multiplicative integral over the descent split)'
status: todo
type: task
priority: normal
created_at: 2026-11-20T16:45:00Z
updated_at: 2026-11-20T16:40:00Z
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

## 2026-11-20 W11, option 2 (attack co-directionality): a fork on WHAT the descent map is
Step 0 now runs: `scripts/corpus-search.ts`, PR #8603. Queries "conditional expectation", "descent homomorphism", "transient trace", "Frobenius positivity", plus "descent" with `--search-text`. None returned a positivity result for the descended or transient pieces; this adds to the six-path grep (see qou-wuxx).

The corpus fixes two different descent maps, and the transient trace behaves oppositely under them:
1. **Trace-preserving conditional expectation**, the Hecke/Markov reading. `hecke-markov-interpretation-table-data.md:7` calls the vertex volume a "one-step conditional expectation", and the Markov property tr(xσ_n) = z·tr(x) makes tr_{n+1} = tr_n ∘ E hold on the WHOLE algebra by construction. Then `transient_trace_eq_zero_of_global_compat` (PR #8593) gives tr_trans ≡ 0. The equality of conj:topological-mass holds TRIVIALLY, but then no Φ_q(z_i) transient term can come from a trace. That contradicts `lem:topological-mass-dilogarithm` / `cor:quantum-dilogarithm` as written.
2. **Surjective algebra homomorphism**, the categorical reading: `lem:descent`, `def:descent-involution`. Trace-compatibility holds only on the image, so the transient trace can be nonzero. But no concrete realisation of τ̂ in H_n is given, so the reading-3 positivity route (`trM_nonneg_of_reading3`) has no element to act on. It cannot be attempted until τ̂ is made concrete.

Next honest step: decide or derive which map 𝔡_{n+1} is in the Hecke realisation. If it is (1), the conjecture is trivially true and the dilogarithm identification must move off the trace. If it is (2), construct τ̂ in H_n and test reading 3 on τ̂α and α − τ̂α. Stays open.
