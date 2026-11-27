import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Combinatorics.Young.SemistandardTableau
import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.Tactic
import HeckeTemperleyLieb.Common
import HeckeTemperleyLieb.NumSYTPos

/-!
# QOU.HeckeAlgebra.Hoefsmit — seminormal representation skeleton

Abstract framework for the Hoefsmit seminormal matrix
representation of the Iwahori-Hecke algebra `H_n(q)`.  This is
the categorical Lean-side analogue of the Python implementation
in `computations/hecke/hecke_characters.py` (function
`build_seminormal_matrices`).

## What this module provides

- `partition` — a typed wrapper for partitions of `n` (using
  `Nat.partitions` from Mathlib's combinatorics).
- `seminormalDim λ` — the dimension `dim V_λ` of the irrep
  `V_λ` indexed by partition `λ`, equal to the number of standard
  Young tableaux of shape `λ`.
- The seminormal matrices themselves are no longer here: see
  `QOU.SchurWeyl.SeminormalRep.genMat` (deleted placeholder note at
  the end of this file).

## Categorical content

Hoefsmit (1974) constructed an explicit "seminormal" matrix
representation of `H_n(q)` whose generators `T_i` act block-
diagonally with respect to the Young tableau basis of `V_λ`.
In T-form, the diagonal entries on tableau `T_w` are determined
by the content `c_T(i)` of cell `i` in `T_w`:
    `(T_i)_{T_w,T_w} = q^{c_T(i+1) - c_T(i)} − 1` divided by a
content-difference q-integer.
Off-diagonal entries between `T_w` and `s_i T_w` (the standard
tableau obtained by swapping `i, i+1`) involve the same content
differences.

## Lean port: done elsewhere

The seminormal construction and both relation proofs now live in
`QOU.SchurWeyl.SeminormalRep` (σ-form, generic field, `q` not a root of
unity). This module keeps only `seminormalDim` and its positivity.

## References

- [hoefsmit1974] Hoefsmit, *Representations of Hecke algebras of
  finite groups with BN-pairs of classical type* (1974).
- [kassel2008] Kassel-Turaev, *Braid Groups*, Springer GTM 247
  §13.6.
-/

namespace QOU.HeckeAlgebra.Hoefsmit

open QOU.HeckeAlgebra

/-- The seminormal dimension of the irrep `V_λ` — equal to `f^λ`, the number of
    standard Young tableaux of shape `λ`.

    **No longer opaque (2026-09-03).** This was `opaque`, with the docstring
    *"axiomatised pending the Mathlib `StandardYoungTableau` enumeration"*. That
    enumeration exists: `QOU.Mathlib.numStandardYoungTableaux` counts the
    in-repo standard-tableau type Mathlib lacks, and `QOU.Mathlib.dimSYT` is
    exactly `f^λ` for a partition's shape. The stated blocker had been cleared;
    nobody came back to the definition. -/
noncomputable def seminormalDim {n : ℕ} (lam : Nat.Partition n) : ℕ :=
  QOU.Mathlib.dimSYT lam

/-- The seminormal dimension is positive.

    **Was a cited `axiom`; now proved (2026-09-03).** `f^λ = Nat.card` of a type
    that is `Finite` (injective encoding) and `Nonempty` (the row-superstandard
    tableau, sorry-free in `QOU/BraidKnot/SytRowSuperstandard.lean`), so
    `Nat.card_pos` applies.

    The `0 < n` hypothesis is **retained for compatibility but unused**: the
    empty diagram carries exactly one standard tableau — the empty one — so the
    count is `1`, and positivity is unconditional. `seminormalDim_pos'` below is
    the hypothesis-free form. -/
-- Ref: [fulton1997] https://doi.org/10.1017/CBO9780511626241 §4 (f^λ ≥ 1 for nonempty λ; standard Young tableaux)
theorem seminormalDim_pos {n : ℕ} (lam : Nat.Partition n) (_hn : 0 < n) :
    0 < seminormalDim lam :=
  QOU.Mathlib.dimSYT_pos lam

/-- Positivity of `f^λ` without the unused nonemptiness hypothesis. -/
theorem seminormalDim_pos' {n : ℕ} (lam : Nat.Partition n) : 0 < seminormalDim lam :=
  QOU.Mathlib.dimSYT_pos lam

/-! ## Seminormal matrices: deleted placeholder (2026-11-23)

This file used to declare `opaque HoefsmitMatrix` with two axioms, the T-form
Hecke relation and the braid relation. Both axioms were vacuous (the opaque
could be the sign representation), and nothing consumed them. They were deleted
on owner approval, 2026-11-23. The concrete seminormal representation, with
both relations PROVED, is `QOU.SchurWeyl.SeminormalRep.genMat`:
`genMat_quadratic` (σ-form quadratic relation) and `genMat_braid_generic`
(braid relation). The T-form and σ-form Hecke algebras are identified in
`QOU.Hecke.ModelsBridge.iwahoriEquivSigma`. -/

end QOU.HeckeAlgebra.Hoefsmit
