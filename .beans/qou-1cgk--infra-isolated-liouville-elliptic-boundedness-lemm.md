---
# qou-1cgk
title: 'Infra: isolated Liouville / elliptic-boundedness lemma — doubly-periodic entire ⇒ constant (vr3q residual)'
status: completed
type: task
priority: high
tags:
    - alien-habiro
created_at: 2026-07-18T17:48:54Z
updated_at: 2026-07-18T17:58:43Z
parent: qou-89f9
---

The single classical gap left after ratio_ibinv_periodic landed (both periods proved). Formalize the standalone complex-analysis lemma: f:ℂ→ℂ entire (Differentiable ℂ), periodic wrt ω₁,ω₂ that ℝ-span ℂ ⇒ f constant. Proof: continuous on compact fundamental box K=[0,1]²·(ω₁,ω₂) ⇒ bounded on K; periodicity (integer shifts) extends bound to all ℂ; Mathlib Liouville (Differentiable.exists_const_forall_eq_of_bounded). Standalone, no QOU/Φ_b dep — reusable. Does NOT by itself close uniqueUpToScalar (still needs Φ_b holomorphicity endowment on FaddeevPhi), but supplies the named missing theorem. Anti-laundering: pure math lemma, honest.
