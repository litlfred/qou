---
# qou-j377
title: 'SW-6 (=R2b): semisimplicity of H_n(q) at generic q (Tits deformation / ρ_λ separate points)'
status: todo
type: task
priority: normal
created_at: 2026-08-02T19:33:07Z
updated_at: 2026-08-19T13:42:33Z
parent: qou-59vq
blocked_by:
    - qou-u86i
    - qou-jfr8
---

H_n(q) is split semisimple for q generic (not a root of unity). Route: the ρ_λ separate points + dim count Σ d_λ²=n! ⇒ the map to ⊕M_{d_λ} is injective on a n!-dim algebra ⇒ iso. Or Tits deformation from K[S_n]. Uses SW-3. Ref: [wenzl1988], [kassel1995].

## Refine (recon): no Tits deformation in Mathlib. K[S_n] semisimple is free (Maschke `instIsSemisimpleRingAddMonoidAlgebra`). Generic-q transfer must be hand-done (discriminant / Gram-determinant nonvanishing of the bilinear form). Substantial.

## ⏩ Concrete Burnside-surjectivity half PROVED (2026-08-10) — sorry-free

[`QOU/SchurWeyl/BurnsideSpan.lean`](https://github.com/litlfred/qou/blob/claude/schur-weyl-sw5-irreducibility-2026-08-10/content/quantum-observable-universe/lean/QOU/SchurWeyl/BurnsideSpan.lean):
`seminormal21_no_linear_relation` (q≠0) — `{1, S0, S1, S0·S1}` admit no nontrivial
linear relation over ℝ ⇒ linearly independent ⇒ (dim M₂=4) span M₂(ℝ) ⇒ the (2,1)
seminormal rep is SURJECTIVE onto M₂(ℝ) (Burnside). Entry-computation proof, no
density theorem. Axiom-clean; lean-direct exit 0; wired into QOU.lean; on PR #4942.

**Still open for full SW-6 (semisimplicity of H_3(q)):** needs `dim H_3(q) = 6`
(the Iwahori–Hecke basis theorem {T_w : w∈S_3}) to turn the surjective block maps
(two 1-dim reps + this M₂ factor, 1+1+4=6) into the iso H_3(q) ≅ ℝ×ℝ×M₂. That
basis/dimension theorem is the real blocker → feeds SW-7 (qou-0h5k); tracking it here.


## Measured 2026-08-19 — blocked, and the blocker is now SW-5 not the reps

State on main: `BurnsideSpan.seminormal21_no_linear_relation` (concrete (2,1),
sorry-free) is the only content. General semisimplicity needs the rho_lambda to be
irreducible and pairwise inequivalent (SW-5, `qou-jfr8`) plus the dimension
anchor sum d_lambda^2 = n! (SW-3, `qou-wtny`). Both are now the live blockers;
the representations themselves are no longer missing (#5279).

Route note kept: no Tits deformation in Mathlib; generic-q transfer from k[S_n]
would have to be hand-done via Gram-determinant nonvanishing. The
separate-points route through SW-5 is the cheaper one now that Ram 4.1 (#5290)
supplies the diagonalisation.
