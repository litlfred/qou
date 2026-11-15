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
