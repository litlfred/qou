---
# qou-8p1g
title: 'qou-8p1x/g: tetraplectic reaches SU(2), not SU(3) — and that SU(2) is already spent'
status: in-progress
type: task
priority: normal
created_at: 2026-08-07T12:40:00Z
updated_at: 2026-09-08T04:00:00Z
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


---

## 2026-08-24 — the open question is CLOSED: the S_3 does not yield SU(3)

"What would change the verdict" above asked whether going to `m >= 2` helps,
and named `Sp(3)/Sp(1)^3` — real dimension `21 - 9 = 12 = 4 * 3`, so `m = 3`,
with `S_3` permuting three quaternionic lines — with the instruction *"it is
NOT obviously yes — do not assume it."*

It is no. `computations/quaternionic_flag_su3_exclusion.py` (exact integers
and highest-weight combinatorics; 23/23 assertions;
`q0Anchor: independent`).

### The part of the proposal that was right

The `m = 1` vacuity IS escaped. `dim Sp(n)/Sp(1)^n = 2n(n-1) = 4·C(n,2)`
exactly, so the full quaternionic flag is tetraplectic with `m = C(n,2)`, and
`m >= 2` from `n >= 3`. At `n = 3`, `m = 3`. The tangent space really does
split into `C(n,2)` quaternionic lines `H_ij`, one per unordered pair, with
`(q_i, q_j)` acting by `x -> q_i x conj(q_j)`; and `N(Sp(1)^n)/Sp(1)^n = S_n`
really does permute them. At `n = 3` all six permutations of `{1,2,3}` induce
distinct permutations of `{12, 13, 23}` — the action on the lines is faithful.
So finding 1 of this bean is answered on its own terms: at `m = 3` the
condition has content, and the three lines with their `S_3` are real.

### Why it still does not reach SU(3)

**Every Lie-algebra homomorphism `su(3) -> su(2)^k` is zero, for every `k`.**
Compose with the projection to factor `i`: its kernel is an ideal of `su(3)`,
which is simple, so the kernel is `0` or everything, and `0` would embed an
8-dimensional algebra in a 3-dimensional one. Every projection vanishes, so
the map does. `SU(3)` is connected, so it lands in the identity component
`Sp(1)^3` of `Sp(1)^3 : S_3` — and there is nothing there for it.

**The naive dimension count does NOT decide this, and it is worth saying so.**
`dim su(2)^3 = 9 > 8 = dim su(3)`, so counting dimensions on the *product*
permits an embedding. Simplicity is what excludes it. This is unlike
`qou-8p1f`, where a dimension count was the whole argument.

**A stronger form, independent of what one names the structure group.** Any
`SU(3)` preserving the decomposition into three quaternionic lines is trivial.
It cannot permute them — that would be a continuous map from a connected group
to the finite `S_3` — so it preserves each line, and each action is then
`SU(3) -> GL(4, R)`, which is trivial because **`SU(3)` has no nontrivial real
representation below dimension 6**: its real-irreducible dimensions run
1, 6, 8, 12, ... (the **3** is of complex type, so its realification is 6; the
adjoint **8** is the smallest of real type). Nothing acts on one quaternionic
line `H = R^4`.

### The equivocation, one level up

This bean already caught the error once: *three Reeb fields is
`dim su(2) = 3`, the **adjoint**, not a 3-dimensional **fundamental** of
`SU(3)`.* The `m >= 2` proposal reproduces it with the permutation
representation standing in for the fundamental. The "three" of the `S_3` is a
three-element **set** carrying a **finite** group; colour needs a
three-dimensional complex **vector space** carrying a **connected** one. A
continuous homomorphism from a connected group to a finite group is constant,
so the `S_n` on the lines admits no connected enhancement at all — it can
never carry gauge bosons, whatever `n` is.

### Enlarging `n` does not help, and here is exactly why

`SU(3) < U(3) < Sp(3)`, so a partial flag
`Sp(n)/(Sp(n_1) x ... x Sp(n_k))` admits `SU(3)` in its isotropy iff some
`n_i >= 3`. But the permutation group only permutes blocks of **equal** size.
So having an `S_3` on three blocks AND an `SU(3)` inside a block needs three
blocks of size `>= 3`, i.e. `n >= 9`: the smallest is `Sp(9)/Sp(3)^3`, real
dimension `171 - 63 = 108 = 4 * 27`. And even there the `SU(3)` is a **chosen
reduction of one `Sp(3)` factor** — it has nothing to do with the `S_3`
permuting the factors, and the tetraplectic condition does not supply it.

The same is true of the cleanest case where a genuine fundamental *does*
appear: `HP^3 = Sp(4)/(Sp(3) x Sp(1))`, real dimension 12, whose tangent
`H^3 = C^3 + C^3·j` restricts to `SU(3) < Sp(3)` as **3 + conj(3)**. That is a
real fundamental — obtained by *reducing* `Sp(3)·Sp(1)` to `SU(3)`, which is
assuming colour, not deriving it. Consistent; not a derivation.

### Verdict

**Scope-(b)** for the claim tested — "the `S_3` on three quaternionic lines
yields `SU(3)`" — licensed by simplicity of `su(3)` together with its real-
representation dimensions.

Route #5 on the `qou-8p1x` scoreboard moves from *"does not reach SU(3) as
instantiated"* to **"does not reach SU(3), and going to `m >= 2` does not
change that"**. The escape the bean left open is closed.

**Not excluded:** quaternionic geometry generally; `SU(3)` obtained by
reducing an `Sp(3)` isotropy factor (consistent, but an assumption of colour);
and every route that does not run through the line decomposition.

### Literature

None needed for the exclusion, and none added. The argument is simplicity of
`su(3)` plus the Weyl dimension formula and reality type — all of it in
`[fulton-harris1991]`, already in `references.ts` and already cited elsewhere
in the corpus. `[foth2002]` and `[fothleitner2003]` remain the sources for the
tetraplectic and Reeb-triad side and are cited on the new
`brings-surface` blocks (bean `qou-wy6d`).

Literature *would* be needed to pursue the constructive half — the
quaternionic-Kähler side, where holonomy `Sp(n)·Sp(1)` and Berger's list are
the relevant machinery, and where one would have to argue that a reduction to
`SU(3)` is forced rather than chosen. The standard references there are Besse
(*Einstein Manifolds*, ch. 14) and Salamon (*Quaternionic Kähler manifolds*,
Invent. Math. 67, 1982), and **neither is in `references.ts`**. Flagging
rather than adding: nothing in the corpus cites them yet, and registering a
reference for an argument nobody is making would be inventory, not provenance.

### Not made into content

Kept as a bean plus a probe, matching `qou-8p1f`. This is an assessment of a
route, and per `qou-cauj` that register does not belong in the paper. If the
owner wants the exclusion in the paper it would be a `remark` in
`brings-surface` interpreting `rem:tetraplectic-su2-gauge-reading` — an
authoring call, deliberately not taken here.

## 2026-09-08 — reopened: `status` disagreed with this bean's OWN body (§13a sweep, `qou-7sin`)

This bean was `completed` while the text above says, in its author's own words,
that the bean itself is still open. Nothing about its mathematics was judged
here and no finding was revisited — only the `status` field was made to agree
with the body.

Found by the `qou-7sin` sweep of the tracker against AGENTS.md **§13a** (owner,
2026-09-06: *"Don't close beans with open conjectures!!!"*), which landed after
most of these were closed. 18 of 2627 completed beans carry this
self-contradiction. It is decidable without judgement — the discriminator is
the bean asserting *its own* openness, not merely mentioning something open.

Re-close it when the work its body names is actually done.
