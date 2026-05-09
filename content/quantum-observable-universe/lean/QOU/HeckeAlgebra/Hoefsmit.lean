/-!
# QOU.HeckeAlgebra.Hoefsmit — seminormal representation skeleton

Abstract framework for the Hoefsmit seminormal matrix
representation of the Iwahori-Hecke algebra `H_n(q)`.  This is
the categorical Lean-side analogue of the Python implementation
in `folio-assistant/computations/hecke_characters.py` (function
`build_seminormal_matrices`).

## What this module provides

- `partition` — a typed wrapper for partitions of `n` (using
  `Nat.partitions` from Mathlib's combinatorics).
- `seminormalDim λ` — the dimension `dim V_λ` of the irrep
  `V_λ` indexed by partition `λ`, equal to the number of standard
  Young tableaux of shape `λ`.
- `HoefsmitMatrix λ q i` — the Hoefsmit seminormal matrix for
  generator `σ_i` in the irrep `V_λ` at parameter `q`.  Currently
  axiomatised; concrete construction is the open Lean port.

## Categorical content

Hoefsmit (1974) constructed an explicit "seminormal" matrix
representation of `H_n(q)` whose generators `σ_i` act block-
diagonally with respect to the Young tableau basis of `V_λ`.
The diagonal entries on tableau `T` are determined by the
content `c_T(i)` of cell `i` in `T`:
    `(σ_i)_{T,T} = (q · q^{c_T(i+1) - c_T(i)} - 1) / (q^{c_T(i+1) - c_T(i)} + 1)`
Off-diagonal entries between `T` and `s_i T` (the standard
tableau obtained by swapping `i, i+1`) involve the same content
differences.

## Open Lean port

The full Hoefsmit machinery would require:
- Mathlib's `Nat.Partition`, `YoungDiagram`, `StandardYoungTableau`
  (these exist as of Mathlib 2024)
- A `Hoefsmit` namespace constructing the seminormal matrices
  per generator, satisfying the Hecke relations
  `σ_i² = (q - q^{-1}) σ_i + 1` and braid `σ_i σ_{i+1} σ_i =
  σ_{i+1} σ_i σ_{i+1}`.

This module captures the type-level interface; the construction
+ relation proofs are deferred to a follow-up.

## References

- [hoefsmit1974] Hoefsmit, *Representations of Hecke algebras of
  finite groups with BN-pairs of classical type* (1974).
- [kassel2008] Kassel-Turaev, *Braid Groups*, Springer GTM 247
  §13.6.
-/

import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Combinatorics.Young.SemistandardTableau
import Mathlib.Data.Nat.Partition
import Mathlib.Tactic
import QOU.HeckeAlgebra.Common

namespace QOU.HeckeAlgebra.Hoefsmit

open QOU.HeckeAlgebra

/-- The seminormal dimension of the irrep `V_λ` — equal to
    `f^λ`, the number of standard Young tableaux of shape `λ`.
    Axiomatised pending the Mathlib `StandardYoungTableau`
    enumeration. -/
axiom seminormalDim : ∀ {n : ℕ}, Nat.Partition n → ℕ

/-- The seminormal dimension is positive for non-empty
    partitions (the trivial Young tableau `T = λ` is always
    standard, giving `f^λ ≥ 1`). -/
axiom seminormalDim_pos : ∀ {n : ℕ} (λ : Nat.Partition n) (hn : 0 < n),
    0 < seminormalDim λ

/-- **Hoefsmit seminormal matrix** for generator `σ_i` of
    `H_n(q)` acting on the irrep `V_λ` at parameter `q`.

    Axiomatised at the type level pending the Mathlib port of
    Hoefsmit (1974); the concrete construction is in
    `folio-assistant/computations/hecke_characters.py`
    (function `build_seminormal_matrices`). -/
axiom HoefsmitMatrix : ∀ {n : ℕ} (λ : Nat.Partition n) (_q : ℝ) (_i : Fin (n - 1)),
    Matrix (Fin (seminormalDim λ)) (Fin (seminormalDim λ)) ℝ

/-- **Hecke relation** (axiomatised property of Hoefsmit
    matrices): `σ_i² = (q - q^{-1}) σ_i + 1`. -/
axiom HoefsmitMatrix_hecke_relation : ∀ {n : ℕ} (λ : Nat.Partition n) (q : ℝ)
    (hq : q ≠ 0) (i : Fin (n - 1)),
    (HoefsmitMatrix λ q i) * (HoefsmitMatrix λ q i) =
      (q - q⁻¹) • (HoefsmitMatrix λ q i) + 1

/-- **Braid relation** (axiomatised): `σ_i σ_{i+1} σ_i = σ_{i+1}
    σ_i σ_{i+1}` whenever both `i` and `i+1` index valid
    generators (`i+1 < n - 1`). -/
axiom HoefsmitMatrix_braid_relation : ∀ {n : ℕ} (λ : Nat.Partition n) (q : ℝ)
    (i j : Fin (n - 1)) (_h_adj : j.val = i.val + 1),
    (HoefsmitMatrix λ q i) * (HoefsmitMatrix λ q j) * (HoefsmitMatrix λ q i) =
      (HoefsmitMatrix λ q j) * (HoefsmitMatrix λ q i) * (HoefsmitMatrix λ q j)

end QOU.HeckeAlgebra.Hoefsmit
