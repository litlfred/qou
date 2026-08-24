---
# qou-8p1g
title: 'qou-8p1x/g: tetraplectic reaches SU(2), not SU(3) — and that SU(2) is already spent'
status: todo
type: task
created_at: 2026-08-07T12:40:00Z
updated_at: 2026-08-07T12:40:00Z
---

Parent: `qou-8p1x`. Assessment of the tetraplectic / quaternionic layer
(`bring_tetraplectic.md`, `foth2002`, `fothleitner2003`, `BringCone.lean`,
`QuaternionicElectroweak.lean`) as a route to colour.

**This layer is real, in-corpus, the owner's own paper, and Lean-formalised
sorry-free.** None of that is in question. The question is only whether it
produces a 3-dimensional fibre. Three findings, increasing in severity.

## 1. At `m = 1` the tetraplectic condition is vacuous

`bring_tetraplectic.md` §1 says it itself: a tetraplectic structure on a
`4m`-manifold is a closed 4-form with `Omega^m` non-degenerate, but the Bring
cone `C(B)` is a **real 4-manifold**, so `m = 1`, every 4-form is closed
automatically, and *"the tetraplectic requirement reduces to a nowhere-vanishing
volume form"*.

So the current instantiation uses the **name** and none of the **content**.
Foth's machinery — tri-momentum maps, the `Omega^m` non-degeneracy — only bites
at `m >= 2`, i.e. real dimension `>= 8`. Nothing that distinguishes tetraplectic
geometry from "pick a measure" is in play on the Bring cone.

## 2. Its output is `SU(2)`

§4: the 3-dimensional radial boundary carries a **3-Sasakian** structure — an
`SU(2)` triad of contact forms and Reeb fields, with
`[M_i, M_j] = 2 M_k` proved sorry-free in `BringCone.lean`
(`reeb_twist_ij`/`jk`/`ki`). That bracket is `su(2)`.

**The "3" here is the wrong 3.** Three Reeb fields is `dim su(2) = 3`, the
*adjoint* of `SU(2)`. Colour needs a 3-dimensional *fundamental* of `SU(3)`.
Conflating those is the classic error and must not be made.

## 3. That `SU(2)` is already double-booked

`QuaternionicElectroweak.lean` already allocates exactly this structure to the
**electroweak** sector: the quaternion's 4 real d.o.f. = 2 complex = an `SU(2)`
doublet, with `su2L`/`su2R` unit-quaternion actions, `su2L_su2R_commute`, and
`u1Y` inside `SU(2)`. Reusing the same Reeb triad for colour would double-book
it.

## Verdict

As instantiated, tetraplectic supplies the `SU(2)` the framework **already
has** — it is the `dim V = 2` side of the gap, not the fix for it — and that
`SU(2)` is spent. This is not a refutation of tetraplectic geometry; it is a
statement that this layer is not where colour comes from.

## What would change the verdict

Go to `m >= 2` (real dim `>= 8`), where the tetraplectic condition has content.
Foth's quaternionic flag manifolds live there. Concretely: does any quaternionic
flag manifold in the framework's reach carry a *three*-fold structure that is
not merely the `SU(2)` triad? `Sp(3)/Sp(1)^3` has real dimension
`21 - 9 = 12 = 4 * 3`, so `m = 3`, with `S_3` permuting three quaternionic
lines. Whether that `S_3` on three lines yields `SU(3)` rather than
`Sp(1)^3 : S_3` is the question, and it is **not** obviously yes — do not
assume it.

Note also `qou-8p1f`: the 4-form route out of this layer to `Spin(7)/G_2/SU(3)`
is separately excluded by a dimension count.

## 2026-08-24 — the three findings are now IN the paper, and the bean stays open

`bring_tetraplectic.md` was incorporated into `brings-surface/`
(bean `qou-wy6d`). All three findings above ride on the new blocks as
`authorNotes` rather than living only here:

* finding 1 (`m = 1` is vacuous) -> `def:bring-cone-tetraplectic-structure`,
  which states in its own prose that `d(Omega) = 0` is automatic and the
  requirement reduces to a nowhere-vanishing volume form;
* findings 2 and 3 (adjoint-not-fundamental; already spent on electroweak) ->
  `rem:tetraplectic-su2-gauge-reading`, whose body says the triad is
  `dim su(2) = 3` and not a three-dimensional fundamental, so this layer is not
  a source of colour.

NOT closing. The verdict is recorded; the open question is unchanged and
untouched — go to `m >= 2` (real dimension `>= 8`), where the tetraplectic
condition has content, and settle whether any quaternionic flag manifold in
reach carries a three-fold structure that is not the `SU(2)` triad.
`Sp(3)/Sp(1)^3` is the concrete candidate named above.
