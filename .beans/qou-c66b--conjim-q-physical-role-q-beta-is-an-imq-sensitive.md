---
# qou-c66b
title: 'conj:im-q-physical-role: Q_beta IS an Im(q)-sensitive observable already in the framework — the conjecture''s stated obstacle is wrong'
status: todo
type: task
priority: normal
created_at: 2026-09-04T10:42:33Z
updated_at: 2026-09-04T10:43:11Z
---

Parent: `conj:im-q-physical-role`. Reached from `qou-pdix` route 5 (the elliptic
generator) on the author's instruction to chip away at where the imaginarity
comes from.

## The conjecture's stated obstacle

`content/quantum-observable-universe/mass-theory/conj-im-q-physical-role.md`,
§"Obstacles to a current proof":

> *The framework's mass formula explicitly **projects away** Im(q) content via
> `|·|`, so **no mass observable** can detect Im(q) directly. The candidate roles
> are all in **non-mass observables**.*

and candidate (iii)'s test is listed as needing *"a categorical formula for decay
widths Γ"* — i.e. the framework is said not to have an Im-sensitive observable yet.

## Measured: Q_beta already is one

`Q_β/m_e = |q² − 2q − 1| · (q+1) / (2q³)` (AGENTS.md cheat sheet). **The modulus
sits on ONE factor.** `(q+1)/(2q³)` is not under it, so the modulus projection
that makes the mass formula Im-blind does not apply to two of the three factors:

    Im q        Q_b(q)                          Q_b(conj q)                |diff|
    0           1.5335566273 + 0j               1.5335566273 + 0j          0
    1e-6        1.5335566273 - 3.418016e-6j     ... + 3.418016e-6j         6.836e-6
    1e-3        1.53355190423 - 3.418010e-3j    ... + 3.418010e-3j         6.836e-3
    0.01        1.53308438987 - 3.417423e-2j    ... + 3.417423e-2j         6.835e-2
    0.139956    1.44367544417 - 0.462524635j    ... + 0.462524635j         0.925

Control, the mass shape `|f(q)|` — fully modulus-projected, invariant, diff
**exactly 0** at both Im q = 1e-3 and 0.139956.

So `Q_β(q̄) = conj(Q_β(q))`, and the sensitivity is **linear**:
`∂Im(Q_β)/∂Im(q) ≈ 3.418`.

## What follows, at the OBSERVABLE level

`Q_β` is experimentally a real Q-value in MeV. Requiring `Im Q_β = 0` therefore
forces `Im q = 0` — the same conclusion `character_im_zero_iff` reaches from the
Kohno–Drinfeld character, but reached from a **decay** observable and from the
`Q_β` formula rather than from the holonomy.

Two consequences, and the second is the useful one:

1. The conjecture's obstacle statement needs correcting. It is not the case that
   the framework lacks an Im-sensitive observable; candidate (iii)'s test is
   *partially runnable now*, on `Q_β`, without a categorical Γ.
2. The answer it gives is a **constraint, not a discovery**: `Im q = 0` at the
   observable level. That corroborates the framework's default from a third
   independent direction and pushes all three candidate roles firmly to the
   **fibre** level — which is where `qou-cds1` already says a D-frame story must
   live ("must first close a FIBRE-level construction").

## 🛑 The caveat, and it is load-bearing

**The complex extension of `Q_β` used here is MINE, not the corpus's.** That
formula was derived for real `q`, where the `|·|` is a sign fix — `q² − 2q − 1`
is negative at `q₀` and `Q_β` must be positive. Extending to complex `q` by
keeping the modulus on that one factor and nothing else is *a* reading, and the
Im-sensitivity is entirely an artefact of which factors the projection covers.

So the honest statement is conditional: **any complex extension of `Q_β` that
preserves the formula's shape is Im(q)-sensitive, because only one of its three
factors is modulus-projected.** Whether that extension is the canonical one is
itself unfixed, and fixing it is prerequisite to running candidate (iii)'s test
properly. What is NOT conditional is the correction to the obstacle statement:
the mass formula's Im-blindness comes from `|tr_M|` covering the whole
expression, and `Q_β`'s does not have that property under any reading.

Scope (a). Derives no `α`, adjudicates no convention, proposes no wiring.
