---
# qou-g4x1
title: 'GAP: 6 AppendixSurreals conjecture kernels formalise nothing — statement-level, not instance-level'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T19:15:44Z
updated_at: 2026-10-04T15:19:38Z
parent: qou-3kkl
---


## Direct answer to "can we prove / derive these properly?"

**For six of the seven remaining `instProvable` instances: no — there is
nothing to derive, because the formal statement is not a weakened version of
the conjecture, it is an unrelated triviality.** The fix is at the
**statement** level, not the instance level. Removing the instances (as was
right for the three in #4797) would be *wrong* here: it would make these read
as open conjectures when the statement as written is genuinely provable.

Classification of all seven, from reading each class field and its witness:

### A. Already properly derived — leave alone (1)

**`ClassicalLimitIsStandardPart`** is real mathematics, not a fabrication. Its
proof uses `standardPart_spec`, `isFinite_decomposition.unique` and
`classicalLimit_of_tendsto` — genuine surreal analysis about the standard part
of `F(1+ε)`. It happens to be *stated* as an instance, which is a
presentational nit at most. This one is fine.

### B. Kernel is literally "a placeholder type is nonempty" (3)

```lean
class BigBangHeatDeath where
  qou_surreal_inhabited : Nonempty (QOU_Surreal K)   -- i.e. `Nonempty K`

class HahnSubstrate where
  qou_surreal_inhabited : Nonempty (QOU_Surreal K)   -- i.e. `Nonempty K`

class JonesBirthday where
  knot_inhabited : Nonempty Knot                     -- i.e. `Nonempty ℕ`
```

**`BigBangHeatDeath` and `HahnSubstrate` have literally the same field.** As
formal statements the two conjectures are indistinguishable — nothing in the
Lean separates the cosmological-endpoint claim from the Hahn-substrate claim.
`JonesBirthday` asserts that `ℕ` is nonempty.

Each docstring says so plainly ("the … content of the prose is not yet
formalisable in the current placeholder vocabulary"), which is honest, but
the classes still *present* as formalisations of named conjectures and are
counted as such by the conjecture-graph audit.

### C. Trivial because a placeholder is a subsingleton (1)

**`ArchimedeanIsStandardPart`** — essential surjectivity of the standard-part
map onto `QOU_Real`. `QOU_Real := PUnit`, so the witness is
`Subsingleton.elim`. Any map onto a one-point type is surjective.

### D. Trivial because both sides are the same placeholder (1)

**`OnPModularHecke`** — `∃ φ : KazhdanLusztigCells p n → Nimbers p n,
Bijective φ`, witnessed by `id`. The two types are definitionally the same
placeholder, so the bijection carries no information about KL cells or
nimbers.

### E. Trivial because the operators are constant (1)

**`KashaevSurreal`** — the proof works because `ColoredJones` returns the
constant `(0,0)` and `HyperbolicVolume K := 0 * K`. Both sides evaluate to
`0`; the Kashaev limit is never exercised.

## What each would actually need

Not one is a mechanical edit. Ordered by how much new vocabulary is required:

| class | missing vocabulary | rough size |
|---|---|---|
| `JonesBirthday` | the birthday grading on Jones coefficients — **not** merely a real `Knot` type; see the correction below | medium |
| `ArchimedeanIsStandardPart` | a `QOU_Real` that is not `PUnit` — i.e. an actual archimedean QOU with structure | medium; needs the QOU record itself |
| `OnPModularHecke` | genuine `KazhdanLusztigCells` and `Nimbers` types (currently both `Fin (p^n)`-shaped) | medium; KL cells are combinatorially real and formalisable |
| `KashaevSurreal` | a real `ColoredJones` and `HyperbolicVolume` | large; this is the volume-conjecture machinery |
| `BigBangHeatDeath` | evaluation of the parameterised functor `q ↦ QOU_Surreal_q` at `q = 1 + ε^ω` and `q = ω` | large; the functor is informal even in the prose |
| `HahnSubstrate` | Hahn-series substrate corrections | large |

**Correction to my own first pass.** I initially wrote that retargeting
`abbrev Knot := ℕ` to the existing `QOU.KnotTheory.BraidWord` would make
`JonesBirthday`'s kernel non-trivial. **It would not.** The kernel is
`Nonempty Knot`, and `BraidWord` is inhabited too — `QOU.KnotTheory.unknot`
witnesses it. Swapping one inhabited type for another leaves a provable
`Nonempty`.

This is the general shape of the trap in section B: **the defect is the
kernel, not the carrier.** `Nonempty X` is provable for any `X` anyone would
actually pick, so no amount of improving `X` helps. Only restating the
conjecture helps.

Retargeting `Knot` is still worth doing on its own merits — it removes a fake
type that `KashaevSurreal` also leans on, and the `abbrev`'s docstring
anticipates it ("can be retargeted without touching the conjecture
statements") — but it should not be sold as fixing `JonesBirthday`.

## Recommended disposition, and what NOT to do

1. **Do not remove these seven instances.** For what the statements currently
   say, the instances are correct. Removing them would misrepresent trivial
   statements as open conjectures — the mirror of the defect fixed in #4797.
2. **Do not "strengthen" a statement by guessing** what the conjecture means.
   Each needs its `.md` read first. The `VacuumEpsilon` near-miss earlier in
   this session (where the Lean docstring stated the *negation* of the
   conjecture) is the cautionary case.
3. **Retarget `Knot` to `BraidWord`** — cheap and well-signposted, but for
   its own sake (removing a fake type), *not* as a fix for `JonesBirthday`.
4. Treat the rest as formalisation projects sized in the table above, not as
   audit-drain items.

## Cross-cutting note for the vacuity audits

These six are invisible to every detector in the repo, including the two I
added this session: there is no `sorry`, no `True`, no unsound quantifier, and
the *statements* are true. The defect is that the statement is not the
conjecture — a semantic mismatch between `.md` and `.lean` that no syntactic
checker can see. The only reliable detector is reading the pair.

`proof-narrative-lean-equivalence` is the skill that targets exactly this
("lean vs narrative / do they prove the same thing"). This file is a
high-yield target for it, and to my knowledge it has not been run here.
