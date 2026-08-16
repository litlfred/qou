---
# qou-omuz
title: QuantumUniverse is over [Field k] but the paper says commutative ring R — and R_q is not a field
status: todo
type: task
priority: normal
created_at: 2026-08-16T03:16:10Z
updated_at: 2026-08-16T03:16:58Z
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
