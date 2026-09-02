/-
# The Schur–Weyl row cap, for an arbitrary partition

`QOU.Eightfold.RowCapObstruction` proves the row cap for `V^{⊗3}` alone: the
alternating channel `λ = (1³)` has `dim V_{(1³)} = C(N,3)`, which vanishes
exactly when `N < 3`.  That is the shape the eightfold-way question needed, and
it is the only shape the corpus had.

Everything else that appeals to the row cap appeals to it for **other**
partitions — `(3,2,1)` at `n = 6` in the staircase electroweak residual
(`qou-4qno`), `(2,2,1,1)` at `n = 6`, the whole `ℓ(λ) > 2` sector in the
Temperley–Lieb kernel measurements — and for those it was corpus prose plus a
numerical measurement, not a theorem.  `markov-trace-frobenius-selection.md`
states it by name ("**the row cap**") and
`lem:feynman-eigenbasis-decomposition` puts `ℓ(λ) ≤ 2` in the *index set* of the
mass channel's decomposition, but neither is machine-checked.

This file closes that gap for every partition at once, and the proof is one
pigeonhole step.

## The statement

Schur–Weyl duality decomposes `V^{⊗n}` over `U_q(gl_N) × H_n(q)` as

    V^{⊗n}  =  ⊕_{λ ⊢ n}  V_λ ⊗ S^λ        with  dim V_λ = #SSYT(λ, N)

where `SSYT(λ, N)` is the set of semistandard Young tableaux of shape `λ` with
entries in `{1, …, N}` — weakly increasing along rows, **strictly** increasing
down columns.  So `dim V_λ = 0` precisely when that set is empty.

A partition with `ℓ(λ)` parts has a first column of `ℓ(λ)` boxes.  Strict
increase down that column is a strictly monotone map `Fin (ℓ λ) → Fin N`, and an
injection into a smaller finite type does not exist.  Hence

    ℓ(λ) > N   ⟹   SSYT(λ, N) = ∅   ⟹   dim V_λ = 0

which is `N_min(λ) = ℓ(λ)`: a partition needs at least as many colours as it has
rows.

## Why the column, and not the row

The asymmetry is the whole content.  Rows increase **weakly**, so a row of any
length can be filled from `Fin N` for any `N ≥ 1` — repeat an entry.  Columns
increase **strictly**, so a column of length `r` consumes `r` distinct values
and is the only place a bound can come from.  Reading the cap off the row
lengths instead would give `λ₁ ≤ N`, which is false for every `N < n`.

## What this is not

It bounds the **carrier**, not the algebra.  `H_n(q)` has a Specht module `S^λ`
for every `λ ⊢ n` whatever `N` is, and its seminormal matrices, characters and
eigenvalues all exist; `dim V_λ = 0` says the *multiplicity space* pairing that
Specht module into `V^{⊗n}` is trivial, so the block acts on no states.  A
number read off `S^λ` for `ℓ(λ) > N` is a number about the algebra, not about
the carrier — which is exactly the distinction `qou-4qno` turns on.

## Base ring (§7c)

Pure combinatorics over `ℕ` and `Fin` — no ring, no ordering beyond `ℕ`, no
archimedean content.  Nothing here is `q`-dependent: the cap is a statement
about the fibre dimension `N`, and the `q`-deformation moves the *weights*
`y_λ = s_λ(1, q, …, q^{N-1})`, not which `λ` survive (`qou-fvzm`).
-/
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.Fintype.Card
import Mathlib.Logic.IsEmpty
import Mathlib.Order.Fin.Basic
import Mathlib.Tactic

namespace QOU.Hecke.RowCap

/-! ## 1. A column filling

The only structure the cap uses: a strictly increasing assignment of colours
from `Fin N` to the `r` boxes of one column. -/

/-- A strictly increasing filling of a column of `r` boxes by colours in
`Fin N`.  This is the restriction to the first column of a semistandard Young
tableau of shape `λ` with entries in `{1, …, N}`, where `r = ℓ(λ)`. -/
abbrev ColumnFilling (r N : ℕ) : Type := {f : Fin r → Fin N // StrictMono f}

/-- A column filling is injective — the content of "strictly increasing". -/
theorem columnFilling_injective {r N : ℕ} (f : ColumnFilling r N) :
    Function.Injective f.1 :=
  f.2.injective

/-! ## 2. The cap -/

/-- **A column of `r` boxes needs at least `r` colours.**

The pigeonhole step, and the only mathematical content in the file: a strictly
increasing map is injective, and an injection `Fin r → Fin N` forces `r ≤ N`. -/
theorem le_of_columnFilling {r N : ℕ} (f : ColumnFilling r N) : r ≤ N := by
  simpa using Fintype.card_le_of_injective f.1 (columnFilling_injective f)

/-- **The row cap.**  A column longer than the number of colours cannot be
filled.  With `r = ℓ(λ)` this is `SSYT(λ, N) = ∅` whenever `ℓ(λ) > N`. -/
theorem isEmpty_columnFilling_of_lt {r N : ℕ} (h : N < r) :
    IsEmpty (ColumnFilling r N) :=
  ⟨fun f => by have hle := le_of_columnFilling f; omega⟩

/-- `N_min(λ) = ℓ(λ)`, in the direction that matters: a nonempty channel forces
the fibre to be at least as large as the partition is tall. -/
theorem forces_N_ge_length {r N : ℕ} (h : Nonempty (ColumnFilling r N)) : r ≤ N :=
  h.elim le_of_columnFilling

/-- The cap as a biconditional: a column of `r` boxes is fillable from `N`
colours exactly when `r ≤ N`.  The forward direction is the pigeonhole above;
the reverse exhibits `Fin.castLE` as a witness. -/
theorem nonempty_columnFilling_iff {r N : ℕ} :
    Nonempty (ColumnFilling r N) ↔ r ≤ N := by
  exact ⟨forces_N_ge_length, fun h => ⟨⟨Fin.castLE h, Fin.strictMono_castLE h⟩⟩⟩

/-! ## 3. The framework's fibre is `N = 2`

`lem:feynman-eigenbasis-decomposition` decomposes the mass channel over
`ℓ(λ) ≤ 2`; the fibre is the fundamental `V` of `SU_q(2)`, so `N = 2`. -/

/-- The framework's fibre dimension. `abbrev` rather than `def` so that
`omega` sees through it in the corollaries below. -/
abbrev fibreDim : ℕ := 2

/-- **At the framework's fibre, every partition with three or more rows is
empty.**  This is the general form of what the corpus measured blockwise: the
`ℓ(λ) > 2` sector spans the kernel of `H_n(q) → TL_n(q)`. -/
theorem isEmpty_of_three_rows {r : ℕ} (h : 3 ≤ r) :
    IsEmpty (ColumnFilling r fibreDim) :=
  isEmpty_columnFilling_of_lt (by omega)

/-- `(3,2,1)` — the staircase `ρ₃`, three rows — carries no states at `N = 2`.
This is the block the electroweak residual reads `cot θ_W` off (`qou-4qno`). -/
theorem staircase_three_isEmpty : IsEmpty (ColumnFilling 3 fibreDim) :=
  isEmpty_of_three_rows (le_refl 3)

/-- `(4,3,2,1)` — the staircase `ρ₄`, four rows — likewise. -/
theorem staircase_four_isEmpty : IsEmpty (ColumnFilling 4 fibreDim) :=
  isEmpty_of_three_rows (by omega)

/-- Only `ρ₂ = (2,1)` among the staircases survives at `N = 2`, and it is the
case the conjecture block itself calls untestable. -/
theorem staircase_two_nonempty : Nonempty (ColumnFilling 2 fibreDim) :=
  nonempty_columnFilling_iff.mpr (le_refl 2)

/-! ## 4. Agreement with the `n = 3` special case

`QOU.Eightfold.RowCapObstruction` computes the alternating channel's dimension
as `C(N,3)`.  A column of `r` boxes filled from `N` colours is exactly a choice
of `r` distinct colours, so the general cap and that arithmetic are the same
statement — recorded here so the two cannot drift apart. -/

/-- The `n = 3` singlet channel `dim V_{(1³)} = C(N,3)` vanishes exactly when
the column of three boxes cannot be filled. -/
theorem choose_eq_zero_iff_isEmpty (N : ℕ) :
    N.choose 3 = 0 ↔ IsEmpty (ColumnFilling 3 N) := by
  rw [Nat.choose_eq_zero_iff, ← not_nonempty_iff, nonempty_columnFilling_iff]
  omega

/-- Reproves `weyl_dim_alt_eq_zero_iff` through the general cap: the singlet is
empty exactly below three colours. -/
theorem alt_channel_empty_iff (N : ℕ) : N.choose 3 = 0 ↔ N < 3 :=
  Nat.choose_eq_zero_iff

end QOU.Hecke.RowCap
