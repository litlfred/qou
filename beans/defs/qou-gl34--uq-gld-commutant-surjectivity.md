---
# qou-gl34
title: 'G3.4: V^{⊗n} = ⊕ W_λ ⊗ S_λ and ρ(H) = End_{U_q(gl_d)}(V^{⊗n}) — the hard direction'
status: todo
type: task
priority: normal
tags:
    - quark-state
    - schur-weyl
created_at: 2026-11-15T10:10:00Z
updated_at: 2026-11-15T10:10:00Z
parent: qou-gld3
---

Needs: (i) complete reducibility of V^{⊗n} under U' = ⟨K, E, F⟩ at generic q; (ii) dim HW_λ = f^λ; then dim End_{U'} ≤ Σ_{ℓ(λ)≤d} (f^λ)² = dim ρ(H) (JimboGL.finrank_range_jimbo) gives equality. Mathlib has no quantum-group highest-weight theory and no complete reducibility for it. Feasibility flag: research-scale formalisation (weeks), not PR-sized. Possible shortcuts to weigh: q-Schur algebra (Dipper–James), or a dimension bound from the weight-space decomposition plus HW_λ ≅ S_λ.

Owner ruling 2026-11-15 ("G3: add infra"): build the highest-weight theory that Mathlib lacks, in PR-sized pieces.

2026-11-15 (q-Schur sibling, PR #7864): scoping done. Mathlib has no bicommutant or Jacobson density, and the Dipper–James/Du/Green generation proof would take weeks, so that route is not recommended. Cheaper route: lowerOp = raiseOpᵀ ⇒ B is transpose-closed ⇒ complete reducibility over an ordered field; V = B·N; dim B' ≤ Σ(dim N_μ)². G3.4 then reduces to (★): N_μ = 0 for non-dominant μ, dim N_λ ≤ f^λ (7a). P1–P3 are about 3 PRs, pending the coordinator's go. Still open.

2026-11-15 (PR #7864, merged on owner decision "Merge now, scoped wording"): `QuantumGLCommutant.range_jimbo_eq_commutant` proves, over a linearly ordered field with q not a root of unity and with no hypothesis left ((★) = `hstar_occWeights`, #7873), that the Jimbo image of H_{m+1}(q) equals the commutant of `uqGens` = {E_i = raiseOp, lowerOp, Cartan elements, weight projectors}. Verified by the old Stream 14 session: library sweep 217/217, `lean -DautoImplicit=false -s 65536` exit 0, axioms propext/Classical.choice/Quot.sound only, no sorry. STILL OPEN before it may be called the U_q(gl_d) commutant (do not close this bean on #7864): (1) weight projectors are polynomials in the Cartan elements at generic q; (2) lowerOp vs the standard Δ(F) of U_q(gl_d) (expected: a Cartan factor times F, unchecked); (3) optional, Stream 16: drop the ordered-field hypothesis (only isCompl_dotPerp uses it). Citation for the U_q(gl_n) → q-Schur surjectivity side: Du 1995 (uploads/weylweb.pdf, not yet ingested).
