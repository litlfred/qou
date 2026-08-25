import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.SetTheory.Cardinal.Finite
import QOU.Mathlib.StandardYoungTableau
import QOU.Mathlib.RSKBurnsideTarget

/-!
# QOU.SchurWeyl.YoungTableaux — partitions and standard Young tableaux (bean SW-2)

The combinatorial index set of the quantum Schur–Weyl program: for `n : ℕ`,

* the **partitions** `λ ⊢ n` as a `Fintype` (so one can `∑`/`⊕` over them), and
* the **standard Young tableaux** (SYT) of shape `λ`, together with the **Specht dimension**
  `dLambda λ := #SYT(λ)` presented as a `Fintype.card`.

## What is reused vs. built here

`Mathlib.Combinatorics.Young` supplies `YoungDiagram` and `SemistandardYoungTableau`, and
`Mathlib.Combinatorics.Enumerative.Partition` supplies `Nat.Partition` **with** a `Fintype`
instance — but Mathlib (at the pinned toolchain `v4.24.0`) has **no** standard-tableau type,
**no** `#SYT(λ)` count, and **no** `Combinatorics.RSK`.

The in-repo `QOU.Mathlib` layer already fills the first two gaps:
[`QOU.Mathlib.StandardYoungTableau`](../Mathlib/StandardYoungTableau.lean) is a genuine SYT
(a `SemistandardYoungTableau` whose entry map bijects the cells onto `{1,…,|μ|}`; strict rows are
*derived*, `StandardYoungTableau.row_strict`) carrying a `Finite` instance, and
[`QOU.Mathlib.RSKBurnsideTarget`](../Mathlib/RSKBurnsideTarget.lean) provides `partitionShape`
and `dimSYT p = numStandardYoungTableaux (partitionShape p)` (a `Nat.card`).

This SW-2 file does **not** duplicate that machinery.  It provides the Schur–Weyl-facing API and
its one genuinely new piece: upgrading the existing `Finite (StandardYoungTableau μ)` to a
`Fintype`, so `dLambda` can be presented as `Fintype.card` as the program requires, and proving
that this `Fintype.card` agrees with the pre-existing `Nat.card` count (hence with `dimSYT`).

Pure combinatorics on `ℕ`; nothing archimedean; no fit.
-/

namespace QOU.SchurWeyl

open scoped BigOperators
open QOU.Mathlib (StandardYoungTableau numStandardYoungTableaux partitionShape dimSYT)

/-! ## Partitions `λ ⊢ n` as a finite index set -/

/-- A **partition** `λ ⊢ n` — an abbreviation for Mathlib's `Nat.Partition n` (a multiset of
positive parts summing to `n`).  Reused verbatim; not reinvented. -/
abbrev Partition (n : ℕ) : Type := Nat.Partition n

/-- Partitions of `n` form a `Fintype` (Mathlib's instance; `Classical.choice`-backed, so
`noncomputable` — it does not reduce in the kernel).  Restated here so the Schur–Weyl program can
`∑`/`⊕` over `Partition n` without reaching into `Nat.Partition`. -/
noncomputable instance instFintypePartition (n : ℕ) : Fintype (Partition n) :=
  (inferInstance : Fintype (Nat.Partition n))

/-- The number of partitions of `n` (`p(n)`), as `Fintype.card`. -/
noncomputable def numPartitions (n : ℕ) : ℕ := Fintype.card (Partition n)

/-! ## Standard Young tableaux of shape `λ` -/

/-- The Young diagram (shape) of a partition `λ ⊢ n` — its parts sorted weakly decreasing as row
lengths.  Delegates to `QOU.Mathlib.partitionShape`. -/
abbrev shape {n : ℕ} (lam : Partition n) : YoungDiagram := partitionShape lam

/-- A **standard Young tableau of shape `λ`** — the in-repo `QOU.Mathlib.StandardYoungTableau` of
the diagram `shape λ`.  Rows and columns are strictly increasing and the entries are a bijection
onto `{1,…,n}`; see `QOU.Mathlib.StandardYoungTableau.row_strict`. -/
abbrev SYT {n : ℕ} (lam : Partition n) : Type := StandardYoungTableau (shape lam)

/-- SYT of any Young diagram form a `Fintype`.  The underlying type is `Finite`
(`QOU.Mathlib.StandardYoungTableau.instFinite`, via an injection into a finite function space);
`Fintype.ofFinite` upgrades that to a `Fintype` (`noncomputable`).  This is the one genuinely new
construction of this file — it is what lets `#SYT` be a `Fintype.card`. -/
noncomputable instance instFintypeStandardYoungTableau (μ : YoungDiagram) :
    Fintype (StandardYoungTableau μ) :=
  Fintype.ofFinite _

/-! ## The Specht dimension `dLambda λ = #SYT(λ)` -/

/-- **`#SYT` of a Young diagram**, as a `Fintype.card`. -/
noncomputable def numSYT (μ : YoungDiagram) : ℕ := Fintype.card (StandardYoungTableau μ)

/-- **`dLambda λ = #SYT(λ)`** — the dimension of the Specht module `S^λ`, presented as a
`Fintype.card` over the standard Young tableaux of shape `λ`. -/
noncomputable def dLambda {n : ℕ} (lam : Partition n) : ℕ := Fintype.card (SYT lam)

/-! ## The `Fintype.card` face agrees with the pre-existing `Nat.card` count -/

/-- `numSYT` (this file's `Fintype.card`) equals the pre-existing `numStandardYoungTableaux`
(`QOU.Mathlib`'s `Nat.card`).  `Nat.card` and `Fintype.card` coincide on a `Fintype`. -/
theorem numSYT_eq_numStandardYoungTableaux (μ : YoungDiagram) :
    numSYT μ = numStandardYoungTableaux μ := by
  unfold numSYT numStandardYoungTableaux
  exact (Nat.card_eq_fintype_card).symm

/-- `dLambda λ` (this file's `Fintype.card`) equals `QOU.Mathlib.dimSYT λ` (its `Nat.card`), so the
Schur–Weyl-facing dimension is definitionally the same combinatorial number that the RSK/Burnside
target `∑_{λ ⊢ n} dimSYT(λ)² = n!` ranges over. -/
theorem dLambda_eq_dimSYT {n : ℕ} (lam : Partition n) :
    dLambda lam = dimSYT lam :=
  numSYT_eq_numStandardYoungTableaux (partitionShape lam)

/-- The RSK / Burnside target restated with this file's `dLambda`: `∑_{λ ⊢ n} dLambda(λ)² = n!` is
equivalent to `QOU.Mathlib.RSKBurnsideHolds n`.  (This is a *restatement*, not a proof — the
identity itself needs the RSK correspondence, absent from the pinned Mathlib; it is the target of
bean SW-3.) -/
theorem sum_dLambda_sq_eq_iff (n : ℕ) :
    (∑ lam : Partition n, (dLambda lam) ^ 2 = n.factorial) ↔ QOU.Mathlib.RSKBurnsideHolds n := by
  unfold QOU.Mathlib.RSKBurnsideHolds
  constructor <;> intro h
  · calc ∑ p : Nat.Partition n, (dimSYT p) ^ 2
        = ∑ lam : Partition n, (dLambda lam) ^ 2 := by
          refine Finset.sum_congr rfl (fun lam _ => ?_)
          rw [dLambda_eq_dimSYT]
      _ = n.factorial := h
  · calc ∑ lam : Partition n, (dLambda lam) ^ 2
        = ∑ p : Nat.Partition n, (dimSYT p) ^ 2 := by
          refine Finset.sum_congr rfl (fun lam _ => ?_)
          rw [dLambda_eq_dimSYT]
      _ = n.factorial := h

end QOU.SchurWeyl
