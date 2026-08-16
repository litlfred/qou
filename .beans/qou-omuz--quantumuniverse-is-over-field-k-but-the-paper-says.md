---
# qou-omuz
title: QuantumUniverse is over [Field k] but the paper says commutative ring R — and R_q is not a field
status: in-progress
type: task
priority: normal
created_at: 2026-08-16T03:16:10Z
updated_at: 2026-08-16T10:33:29Z
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
`content/quantum-observable-universe/`.

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
