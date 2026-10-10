---
# qou-8p1h
title: 'qou-8p1x/h: Bruhat / GL_n(F_q) realisation of H_n(q) as a native route to PSL(2,7)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T12:40:00Z
updated_at: 2026-10-04T15:23:03Z
parent: qou-8lxd
---

Parent: `qou-8p1x`. The strongest idea on the board, gated on `qou-8p1j`.

## The idea

`H_n(q)` is **by origin** the Iwahori–Hecke algebra of `GL_n(F_q)`: the
convolution algebra of `B`-bi-invariant functions, with basis indexed by the
Bruhat cells `G = union over w in W of BwB`. The framework already uses
`H_n(q)` as its core object, so this is not an import — it is that object's
defining realisation.

At `n = 3, q = 2` everything the colour section wants appears at once:

* complete flags: `sum over w in S_3 of 2^len(w) = 1+2+2+4+4+8 = 21`;
* point set of `PG(2,F_2)` = the **Fano plane**;
* `Aut = GL(3,F_2) = PSL(2,7)`, order `7 * 6 * 4 = 168`.

This would make the colour group **native rather than imported**, with the
complex **3** / **3bar** irreps of `PSL(2,7)` supplying the fibre — and it
would retire the octonion algebra from its current role as the section's
undefined sole foundation (`qou-8fl1`).

## Three honest problems

1. **`q = 2` is the whole ballgame.** The framework's `q` is a deformation
   parameter, and `q_0` is a *locally observed value that varies*. Jumping to
   `q = 2` because it yields `168` is textbook numerology absent a structural
   derivation. This is `qou-8p1j` and it is load-bearing: if it fails, this
   route collapses.
2. **`F_2^3` is not a `C`-fibre.** The bridge to a 3-dimensional fibre runs
   through the complex **3** of `PSL(2,7)`, which is rep theory one would have
   had anyway. So "native" is a claim about the *group*, weaker than it first
   sounds.
3. **The Hecke algebra is only the `B`-bi-invariant part.** Recovering
   `GL(3,F_2)` itself needs the building / the full induced representation, not
   `H_3(q)` alone.

## First concrete step

Do not start by computing. Start by asking whether the framework has any
structural reason to single out characteristic 2 (`qou-8p1j`). If it does not,
this route should be recorded as attractive-but-numerological and left alone.


---

## SUBSUMED FOR FLAVOUR (2026-08-07)

`qou-w5fw` / T3f already establishes that the Ocneanu parameter `a = q^{N-1}`
is free on the Hecke tower, so `N = 3` is reachable at the **same `q`** via
`a = q^2` — no characteristic-2 move needed. That is the better-formulated
version of this bean's instinct (get `N = 3` from the Hecke tower itself), and
it is already flagged in `qou-dwsh` §2c as the most promising direction.

**What survives here** is the genuinely different *colour* target: the Fano
plane as `PG(2,F_2)` with `Aut = GL(3,F_2) = PSL(2,7)`. That target really does
want `q = 2`, and so really does depend on `qou-8p1j`. Keep this bean scoped to
colour; do not use it to argue about flavour `N = 3`.
