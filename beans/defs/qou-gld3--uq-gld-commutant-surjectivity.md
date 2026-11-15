---
# qou-gld3
title: 'GAP (G3): Jimbo image = full U_q(gl_d) commutant on (K^d)^{⊗n} — not provable from the tree'
status: todo
type: task
priority: normal
tags:
    - quark-state
    - schur-weyl
created_at: 2026-11-15T12:00:00Z
updated_at: 2026-11-15T12:00:00Z
parent: qou-qs4c
---

G3 of the qou-qs4c dispatch (2026-11-15), investigated and recorded as OPEN.

Statement wanted: rho(H_n(q)) = End_{U_q(gl_d)}((K^d)^{⊗n}), equivalently
V^{⊗n} = ⊕_{l(λ) ≤ d} L(λ) ⊗ S_λ with L(λ) the U_q(gl_d) irreducible.

What exists:
- `QOU.SchurWeyl.JimboGL` (this dispatch): kernel of the gl_d Jimbo action = blocks with
  more than d rows; image dimension Σ_{l(λ)≤d} (f^λ)²; ordered field.
- `QOU.Mass.QuantumSl2Fundamental`, `QOU.IwahoriHecke.TensorSchurWeyl`: for d = 2 ONLY, the
  inclusion image(H) ⊆ commutant of the U_q(sl₂) coproduct. U_q(sl₂) as an algebra is not
  constructed (representation data only).
- Nothing for U_q(gl_d), d ≥ 3: no generators, no coproduct, no intertwining.

Missing, in order:
1. U_q(gl_d) representation data on K^d and its iterated coproduct on V^{⊗n}
   (generalise `Rep` of QuantumSl2Fundamental); intertwining [Ř_i, Δ^(n)(X)] = 0.
2. The reverse inclusion: a dimension count dim End_{U_q}(V^{⊗n}) ≤ Σ_{l(λ)≤d}(f^λ)², which
   needs complete reducibility of V^{⊗n} and the U_q-multiplicities — highest-weight theory not
   in Mathlib — or a double-centraliser argument, which needs the same input.

Is it needed? NOT for the trace, weights, kernel or dimension:
`JimboGL.qtr_jimbo_blockIdempotent` reads Wenzl's weights off H-semisimplicity alone.
It IS needed to identify the multiplicity spaces with U_q(gl_d) irreducibles
(e.g. "the (1^d) block is the q-determinant line Λ^d V").

Also open, separate: the kernel identification over a non-ordered field (e.g. ℂ, generic q);
the transpose/positivity route does not reach it.
