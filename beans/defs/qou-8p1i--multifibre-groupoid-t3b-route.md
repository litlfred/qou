---
# qou-8p1i
title: 'qou-8p1x/i: multi-fibre groupoid (T3b) — the only untouched native route'
status: scrapped
type: task
created_at: 2026-08-07T12:40:00Z
updated_at: 2026-08-07T14:20:00Z
---

Parent: `qou-8p1x`. Direction 1 of the two construction directions already
named in `schur-weyl-eightfold.md`; direction 2 (octonionic `G_2`) is the one
whose substrate bridge died with `qou-8p1b`.

## The proposal, as it currently stands

"Inequivalent fibre objects whose interaction space is three-dimensional (T3b)."
Here the `3` is a **count of objects**, not the dimension of a single fibre.

## The roast

It is a **name, not a construction**. Nobody has exhibited the inequivalent
fibre objects, and nobody has shown their interaction space is three-dimensional.
As stated it relocates "why is `dim V = 3`" to "why are there exactly three
inequivalent fibres" — the same question wearing a hat.

## Why it is nonetheless the route to try

It is the only candidate that is **both substrate-native and completely
untouched** by the Klein exclusion, the marked-pair obstruction, and the
4-form dimension count. Every other native route is either excluded
(`qou-8p1f`), mis-targeted (`qou-8p1g`), or gated on an unjustified
specialisation (`qou-8p1h` via `qou-8p1j`).

## First step

Find where T3b is actually defined, and determine whether "inequivalent fibre
objects" is a definition with content or a placeholder. If it is a placeholder,
say so plainly — that would mean the framework currently has **no** live
substrate-native route to colour, which is an honest and important thing for
the corpus to record rather than leave implicit.


---

## LIVE SURFACE COLLAPSED (2026-08-07) — see the synthesis audit

`docs/audits/2026-08-07-eightfold-live-surface-collapse.md`.

Three independent threads now terminate on the **same** requirement:
* the Sym^2-gate result — no **odd-dimensional** summand of any
  `V^{tensor n}` passes (Frobenius–Schur parity: odd-dim SU(2) irreps are
  orthogonal, so their singlet lands in `Sym^2`), so "inequivalent fibre
  objects" must mean genuinely non-isomorphic fibres. *Corrected 2026-08-07:
  self-duality alone does NOT decide the gate — even-dimensional summands are
  symplectic and do pass it, they are just the wrong dimension;*
* the Ocneanu result — an N = 3 channel must be the categorical trace on a
  genuinely 3-dimensional object, since the parameter is the fibre's quantum
  dimension;
* T3g's own question — does the braided category admit inequivalent fibre
  *functors* (a non-neutral Tannakian gerbe)?

**`qou-8p1i` (T3b) and `qou-y7vg` (T3g) are the same question.** Merge their
scope.

**And T3g's stand-down is VOID.** It deferred to the S₄/Fano route ("the Fano/S₄
route subsumes the structural content of this bean") — and that route was
excluded today, scope-(b). T3g is now the *surviving* direction, not the
subsumed one, and should be re-prioritised.


---

## THE CORPUS ALREADY ASSERTS AN ANSWER — as an unproved remark (2026-08-07)

`rem:fivefold-affine-charts-generations`
(`brings-surface/fivefold-affine-charts-generations.md`) states, verbatim:

> "Each fibre functor `tau : C -> Vect` serves as an **affine chart**. The
> `S_5` symmetry acts directly on **the space of these affine charts**. The
> five sheets of Bring's surface correspond to **five classes of affine
> charts**. ... There are **five topologically distinct embeddings of a fibre
> functor**. Three sheets carry the matter families (`T_{2,3}, T_{2,5},
> T_{2,7}`), while the remaining two carry the force mediators (`T_{2,9},
> T_{3,5}`). ... Transition functions between distinct sheets invoke **5-fold
> monodromy**."

So T3g's existence question — *does QOU's braided category admit inequivalent
fibre functors?* — is **already answered affirmatively in the corpus**, with a
specific count (five) and a specific `S_5` action. "Transition functions
between distinct sheets" is literally cocycle/gerbe language.

### But check the status before building on it

The block is a **`remark`**, `interprets: def:quantum-universe`, **no `.lean`
sibling, no proof, no witness**. Per AGENTS.md §3a a remark carries "physical
interpretation, motivation, or examples — **not new mathematical claims**". So
this is **asserted, not established**. It cannot be cited as settling T3g.

### Two things this changes

1. **The count is FIVE, and its 3 is the wrong 3.** Three of the five sheets
   carry *matter families* — i.e. **generations**, not colour or flavour. Even
   granting the remark in full, it delivers a 5-fold structure with a 3+2 split,
   not an `SU(3)`.
2. **T3g may have analysed the wrong extension degree.** T3g §5 rules out the
   *degree-3* extension route on the grounds that `Out(SU(3)) = Z/2`, not `Z/3`
   — it assumed three fibres because `SU(3)` wants a 3. But the corpus's actual
   multi-fibre structure is **five-fold with `S_5`**. **Nobody has analysed the
   degree-5 / `S_5` case.** T3g's obstruction does not obviously transfer:
   `S_5` has plenty of subgroups and quotients, and the relevant question is
   which band an `S_5`-glued gerbe can carry, not a `Z/3` one.

### Adversarial note, recorded so it is not skipped

The remark's supporting language — 5-fold monodromy, "globally aperiodic
structure similar to a quasicrystal", Penrose-tiling analogy — is evocative and
entirely unformalised, and the assignment of specific torus knots
`T_{2,3}/T_{2,5}/T_{2,7}` to the three generations has the shape of a pattern
match rather than a derivation. Establishing the remark is a real research task,
not a citation.

### Concrete next step

Before any gerbe construction: **promote or refute the existence claim.** Is
"five topologically distinct embeddings of a fibre functor" a theorem, or a
picture? That is prior to asking what band the gerbe has, and it is the honest
first move on the merged `qou-8p1i`/`qou-y7vg` scope.


---

## SCRAPPED as a DUPLICATE (2026-08-07) — my bean-hygiene failure

This bean duplicates **`qou-dwsh`** ("T3b: distinct-fibre groupoid -- does a
non-self-dual 3-object exist?", `parent: qou-8lxd`, priority high), which
existed since 2026-08-03 and which I did not grep for before creating this one.
`qou-dwsh` even states the same conclusion my Sym^2 probe later re-derived:
*"the representation must NOT be a tensor power of one V"*.

The state was incoherent — the same question sitting **completed** on
`qou-dwsh` and **todo** here.

**Live carrier is `qou-y7vg` (T3g).** Everything of value from this bean has
been folded there: the merged T3b/T3g scope, the `rem:fivefold-affine-charts-generations`
finding, and the corrected Frobenius-Schur parity statement.

What this bean *did* add over `qou-dwsh`, and which survives on `qou-y7vg`: the
**reason** the tensor-power route fails (FS parity, not self-duality) and its
Lean formalization in `QOU/Eightfold/Sym2GateParity.lean`.
