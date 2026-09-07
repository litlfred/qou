---
# qou-0ie7
title: 'REV_n sharpness: the dropped Σβ = n + ℓ(ℓ−1)/2 constraint after the (ℓ,W) route closed (takeover of #7093, qou-hok7)'
status: todo
type: task
priority: normal
created_at: 2026-09-07T18:06:40Z
updated_at: 2026-09-07T18:37:58Z
parent: qou-6g7j
---

PR #7093 (branch claude/rev-pair-term-even-gap-minimizer-2026-09-07, 3 commits, awaiting merge permission) closed the (ℓ,W) route: Jensen is optimal per distance class, and the inter-class coupling factor SHRINKS with ℓ (1.208 at ℓ=8 → 1.072 at ℓ=60; 1.128 at the maximizer's ℓ=22, 8.2 % of B against a ~3× gap). The only remaining relaxation of size is the dropped constraint Σβ = n + ℓ(ℓ−1)/2, which ties the β's to n directly rather than through two summary integers. Task: formulate the bound WITH that constraint (fresh formulation, not another bound on the same object), measure against the exact REV_n (n ≤ 44 available from rev_free_energy_over_shapes_probe), and say whether the 3/4 exponent is sharp. REV_n is the free energy over partition shapes: energy = excess hook length, entropy = shape multiplicity. Exact / mpmath, no float64.



**ROAST 2026-09-07 (qou-pbwj) — verdict: CONTINUE, conditional on a budget measurement first.** Strongest objection: 'the dropped Σβ = n + ℓ(ℓ−1)/2 constraint is the only remaining relaxation of size' is asserted, not measured. The over-statement at the n = 40 argmax is 3.09× (#7081); PR #7093 prices the Jensen inter-class coupling at only 1.21× and shrinking with ℓ; ~2.5× is unattributed, and (III) is a restriction on the feasible set, not a term in the bound — it cannot reduce the per-configuration slack of the one-body term Σ_i F(β_i) ≤ ℓC, where F(k) saturates at C = 6.1714 only as k → ∞ and the maximiser's β's are O(√n) with W/ℓ ≈ 1.7. Before formulating: at n ∈ {16,24,32,40} and the maximiser's own (ℓ,W), split the 3× into (one-body slack) × (Jensen) × (what (III) removes). Formulate only if (III) owns the majority. Fit exposure: none in the forbidden sense (a bound is valid or not), but the live hazard is reading n ≤ 44 numerics as sharpness — rev_sharpness_discriminator_control_probe shows a provably √n object is flat at 1.20–1.23 on the n^{3/4} column over exactly the reachable range; no 'tracks √n / n^{3/4}' claim below n ~ 150. Arity: the proved bounds are ∀n with constants; sharpness is ∃c ∀N ∃n > N — undecidable from any finite table; and REV_n is a one-parameter family in q evaluated at one archimedean point (say so). L2 relevance: none — qou-hok7 itself records the resummation route to B_D as negative since 2026-08-21; REV's asymptotics is a statement about the object. Full frame: docs/audits/2026-09-07-takeover-fronts-roast.md §Front 4.
