---
# qou-ce54
title: 'T1: prove ⟨I·b, I/b⟩ is an ℝ-basis of ℂ when b²∉ℝ (hspan input of the rigidity reduction)'
status: completed
type: task
priority: high
tags:
    - alien-habiro
created_at: 2026-07-18T18:22:29Z
updated_at: 2026-07-18T18:27:11Z
parent: qou-89f9
---

Closeable now, pure Lean. Two complex numbers v=I·b, w=I/b are ℝ-linearly independent iff v/w=b² ∉ ℝ iff (b²).im≠0. dim_ℝ ℂ = 2 ⇒ 2 indep vectors form a Basis (Fin 2) ℝ ℂ. Deliver: exists_basis_of_sq_not_real : (b^2).im ≠ 0 → ∃ bas : Basis (Fin 2) ℝ ℂ, bas 0 = I*b ∧ bas 1 = I/b. Feeds FaddeevRigidityReduction.uniqueUpToScalar_of_entire (the bas/hb0/hb1 args). Physics: b²∉ℝ = substrate arg b=π/4; FAILS for real b (periods parallel). Approach: LinearIndependent ℝ ![v,w] via re/im determinant (conj(v)·w).im = -Im(b²)/|b|² ≠ 0, then basisOfLinearIndependentOfCardEqFinrank.
