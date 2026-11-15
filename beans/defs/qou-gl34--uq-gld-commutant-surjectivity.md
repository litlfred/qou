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
