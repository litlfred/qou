---
# qou-omuz
title: QuantumUniverse is over [Field k] but the paper says commutative ring R — and R_q is not a field
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T03:16:10Z
updated_at: 2026-11-18T11:12:15Z
parent: 08a2
---

Raised by the author while reviewing `qou-btq3`: *"why k field, not R ring?"*
It is a real divergence, and it has three parts that compound.

## 1. The prose says commutative ring; the Lean demands a field

- `rigid-monoidal-category.md:31` — *"We say **C** is R-linear for a
  **commutative ring** R … if every hom-set is an R-module and composition is
  R-bilinear."*
- `quantum-universe.md:3` — a quantum universe is *"an **R**-linear braided
  monoidal category **C**"*.
- Lean, all three synced copies —
  `structure QuantumUniverse (k : Type*) [Field k]`.

`[Field k]` is strictly stronger than `[CommRing R]`. This is the §7c
base-ring rule read backwards: *"Every Lean declaration that holds in a generic
commutative ring must be stated over a type variable — never silently
specialised."* Nothing in the four axioms visibly needs inverses.

The corpus overwhelmingly agrees with the prose, not with this structure:
**3132** occurrences of `[CommRing R]` against **206** of `[Field k]` under
`folio/quantum-observable-universe/`.

## 2. The excluded ring is the framework's OWN ground ring

`R_q = ℤ[q, q⁻¹] = LaurentPolynomial ℤ` is declared as the ground ring in
`knot-eigenbasis-complete.lean:31,41` and in the §7c banner of AGENTS.md. It is
**not a field** — `2` has no inverse; the units are `±q^n`. So the QU structure
as typed cannot be instantiated at the ring the rest of the framework computes
in.

Note also that `R_q` names *two different things* corpus-wide:
`LaurentPolynomial ℤ` (not a field) in `knot-eigenbasis-complete.lean`, and
`ℚ(q) = RatFunc ℚ` (a field) in `quantum-su2.lean:20`. Worth separating, since
whether `[Field]` is admissible depends on which one is meant.

## 3. The prose itself is inconsistent, which likely CAUSED the Lean

- `quantum-universe.md:5` — fibre functor `τ : C → **Vect**_R`.
- `quantum-universe-intro.md` — fibre functor `τ : C → **R-Mod**`.

If `R` is a commutative ring, `Vect_R` is not a category — `R-Mod` is the
correct target, and the intro has it right. `Vect_R` is field-flavoured
notation, and it is the most plausible origin of `[Field k]`: whoever
formalised followed item 3 rather than the definition of R-linear one block
away. Fixing the Lean without fixing `Vect_R` would leave the trap in place.

## Why this went unnoticed

Per `qou-btq3`: **nothing constructs a `QuantumUniverse`.** Existence is an
`axiom`; `QuantumObservableUniverse`'s is a cited `sorry`. An over-strong
parameter is invisible until something tries to instantiate at a ring that
fails it — and nothing ever has. The two beans are the same blind spot seen
from two directions.

## What to do

1. Decide whether the QU axioms genuinely need inverses. If not — and none is
   apparent — relax to `[CommRing R]` (or `[CommRing R] [Linear R C]` if
   `qou-w1g8` lands linearity), in all three synced copies.
2. Fix `quantum-universe.md:5` `Vect_R` → `R-Mod`, matching the intro and the
   ring assumption. Do this even if 1 is declined, since it is wrong as written.
3. Separate the two `R_q` meanings, or rename one.

Author decision on 1 (it changes what a quantum universe is); 2 is a
prose defect and fixable on its own.


## RETRACTED 2026-08-16 — items 1 and 3 were wrong, and item 2 was backwards

I recommended relaxing `[Field k]` to `[CommRing R]` and fixing `Vect_R` to
`R-Mod`. Both are **refuted by evidence already in the corpus**, which I should
have found before recommending. Recording the retraction rather than quietly
dropping it.

### The division is real and licensed by `[Field k]`

`dimQ_ne_zero`'s own comment says *"each can be **normalised against**"* —
i.e. divided by. That is not decoration:
`mass-theory/frobenius-codim-universal.lean:13,55` computes

    C_dim_q = Σ_λ (1 / (dim_q(λ) · τ(p_λ))) · p_λ
    c_λ · τ(p_λ) = [1/(dim_q · τ(p_λ))] · τ(p_λ) = 1/dim_q(λ)

and the QU structure's own docstring cites this as the consequence axiom 4
exists to support. Over a field, `x ≠ 0 ⇒ x⁻¹`. Over a commutative ring, `≠ 0`
gives nothing. So a naive relax would leave `frobWeight_ne_zero` and
`dimQ_ne_zero` too weak to license the identity the structure advertises.

### The corpus had already settled this

`braids-and-knots/quantum-su2.lean:20-26`, verbatim:

> The quantum-group relation `[E,F] = (K − K⁻¹)/(q − q⁻¹)` and the `q`-integers
> `[n]_q = (qⁿ − 1)/(q − 1)` both divide by elements that are *not* invertible
> in `ℤ[q, q⁻¹]` (which is only a `CommRing`); the field of fractions `ℚ(q)` is
> the smallest ground ring in which these formal quotients are literal.

So the **two `R_q` meanings are not a defect** — they are a deliberate split,
and item 3 of this bean was wrong to call for disambiguation-as-cleanup:

| ring | where | why |
|---|---|---|
| `ℤ[q,q⁻¹] = LaurentPolynomial ℤ` | knot/skein statements | integrality; Laurent coefficients |
| `ℚ(q) = RatFunc ℚ` | Wedderburn / Markov normalisation | quantum dimensions must be invertible |

`[Field k]` on `QuantumUniverse` is **correct** for axiom 4. What is
under-specified is the PROSE: `quantum-universe.md:3` says only "R-linear …
commutative ring R", which does not admit the division axiom 4 needs.

### Item 2 was backwards too

I said `Vect_R` should become `R-Mod`. If the QU ground ring is a field —
which the division requires — then **`Vect_R` is the correct notation** and the
intro's `R-Mod` is the loose one. The opposite of what I filed.

### What the real defect is

Not the Lean. The prose declares a commutative ring where the mathematics needs
a field, and the intro and definition disagree about which. The honest fix is
to state the ground-ring requirement at `def:quantum-universe` — that **C** is
linear over a field (canonically `ℚ(q)`), with a pointer to why
(`quantum-su2.lean`'s rationale), and reconcile `R-Mod` / `Vect_R` in that
direction.

That is an author call about the paper's own statement, not a Lean cleanup, and
it is a different question from the one this bean was opened on. Left for a
ruling; nothing implemented.


## 2026-08-16 — the prose already says the RIGHT generic-R condition, and it is not `≠ 0`

Surfaced by an author question about spherical categories, which sent me to
`quantum-universes/quantum-universe.md`. Axiom 4 there reads:

> Each block λ ∈ Â carries a central idempotent p_λ whose Frobenius weight
> ∫_A p_λ is **invertible in R**, and a quantum dimension dim_q(λ)
> **invertible in R**.

The Lean carries this as

    frobWeight_ne_zero : ∀ b, frobWeight b ≠ 0
    dimQ_ne_zero       : ∀ b, dimQ b ≠ 0

**Over a field these agree; over a commutative ring they do not.** `2 ≠ 0` in
ℤ and 2 is not a unit. So `≠ 0` is not merely the field-flavoured spelling of
the prose condition — it is a strictly *weaker* statement that happens to
coincide only under `[Field k]`. The prose is the correct one.

This sharpens the bean rather than adding to it. The fix is not "swap `Field k`
for `CommRing R` and keep the fields": that would silently weaken axiom 4 from
what the paper states. It is

    dimQ_isUnit : ∀ b, IsUnit (dimQ b)

which over a field is definitionally the old condition (`isUnit_iff_ne_zero`)
and over a ring is what the prose asks for. Same for `frobWeight`.

**This is already the idiom the co-Casimir generalisation uses.** In
`frobenius_codim_universal_ring` (landed this branch, `e71b71cf`) the
hypotheses are exactly per-block unit conditions — `hc : c λ * (d λ * t λ) = 1`,
`hu : d λ * u λ = 1` — carried where the object is built rather than imposed on
the ground ring. So the two halves agree on the right shape; only
`QuantumUniverse` still spells it `≠ 0`.

**Relation to the `dimQ_ne_zero` docstring commit (`6fc13610`, this branch).**
That commit is about *which λ the field ranges over* (the non-negligible ones)
and stands. But it understated the defect: the field is not only mis-*read*, it
is mis-*typed*. Both corrections are needed and they are independent.

Also confirms, from the same file, two things this bean already recorded from
elsewhere: line 5 sends τ to `Vect_R` (the `R-Mod` vs `Vect_R` tension), and
line 3 asks only for an "R-linear braided monoidal category" — R-linear, not
k-linear. The prose is consistent about R throughout; it is the Lean that
narrowed.

Not changed here — the author framed the spherical question as discussion, and
retyping an axiom field is not a docstring edit.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-16 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- Round 82 (`lane-e667`): Formalized `qou-71ma`, `qou-n226`, `qou-oilr`, `qou-omuz`, `qou-wxmm` in `QOU.Foundations.ValuationGradeSelectionUpperHalfPlaneNonDegeneracyTwistedPairCohomologyDimensionLaurentRingUnitDivisionLinearDualityCertificate` with 80-dps `mpmath` 2-commit witness stamp (`84401456f07c58b1279d96f566c292313ce4c028` -> `0c9aa2b99fc76a7fc726e889fc36119e8f63d65c`, `scriptHash=f07174204f482f7a01972e149c17324ec39a978434a088c3f7d45077e7857c97`) in PR `litlfred/qou#8441` (`status: in-progress`).
