import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Combinatorics.Young.SemistandardTableau
import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.Tactic
import QOU.HeckeAlgebra.Common

/-!
# QOU.HeckeAlgebra.Hoefsmit — seminormal representation skeleton

Abstract framework for the Hoefsmit seminormal matrix
representation of the Iwahori-Hecke algebra `H_n(q)`.  This is
the categorical Lean-side analogue of the Python implementation
in `folio-assistant/computations/hecke/hecke_characters.py` (function
`build_seminormal_matrices`).

## What this module provides

- `partition` — a typed wrapper for partitions of `n` (using
  `Nat.partitions` from Mathlib's combinatorics).
- `seminormalDim λ` — the dimension `dim V_λ` of the irrep
  `V_λ` indexed by partition `λ`, equal to the number of standard
  Young tableaux of shape `λ`.
- `HoefsmitMatrix λ q i` — the Hoefsmit seminormal matrix for
  the **T-form generator** `T_i` in the irrep `V_λ` at parameter
  `q`.  Currently axiomatised; concrete construction is the
  open Lean port.

## Convention: T-form throughout

Per Copilot review consistency note: this file uses **T-form**
generators `T_i` consistently — both in the type signature
`HoefsmitMatrix λ q i` (representing `T_i ∈ End(V_λ)`) and in
the Hecke relation axiom (`T_i² = (q − 1) T_i + q · 1`).

The σ-form alternative (`σ_i = q^{−1/2} T_i`) is mathematically
equivalent but introduces `q^{1/2}` denominators that lose F_p
compatibility (per user direction "we want as many stmts to
hold in F_p" — see `QOU.HeckeAlgebra.Formal`).

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

namespace QOU.HeckeAlgebra.Hoefsmit

open QOU.HeckeAlgebra

/-- The seminormal dimension of the irrep `V_λ` — equal to
    `f^λ`, the number of standard Young tableaux of shape `λ`.
    Axiomatised pending the Mathlib `StandardYoungTableau`
    enumeration. -/
opaque seminormalDim : ∀ {n : ℕ}, Nat.Partition n → ℕ

/-- The seminormal dimension is positive for non-empty
    partitions (the trivial Young tableau `T = λ` is always
    standard, giving `f^λ ≥ 1`). -/
-- Ref: [fulton1997] https://doi.org/10.1017/CBO9780511626241 §4 (f^λ ≥ 1 for nonempty λ; standard Young tableaux)
axiom seminormalDim_pos : ∀ {n : ℕ} (lam : Nat.Partition n) (hn : 0 < n),
    0 < seminormalDim lam

/-- **Hoefsmit seminormal matrix** for generator `σ_i` of
    `H_n(q)` acting on the irrep `V_λ` at parameter `q`.

    Axiomatised at the type level pending the Mathlib port of
    Hoefsmit (1974); the concrete construction is in
    `folio-assistant/computations/hecke/hecke_characters.py`
    (function `build_seminormal_matrices`). -/
opaque HoefsmitMatrix : ∀ {n : ℕ} (lam : Nat.Partition n) (_q : ℝ) (_i : Fin (n - 1)),
    Matrix (Fin (seminormalDim lam)) (Fin (seminormalDim lam)) ℝ

/-- **Hecke relation in T-form** (the F_p-friendly form, per
    user direction "we want as many stmts to hold in F_p"):

        `T_i² = (q − 1) · T_i + q · 1`

    INTEGER coefficients in q ⟹ holds uniformly across all F_p
    when `q : ZMod p`.  The σ-form alternative
    `σ_i² = (q^{1/2} − q^{−1/2}) σ_i + 1` requires `q^{1/2}` and
    therefore lives over `ℚ(q^{1/2})` — losing F_p compatibility
    at primes where `q^{1/2}` doesn't exist.

    Conversion: `T_i = q^{1/2} σ_i` (in σ-form), so the two
    formulations are related by a `q^{1/2}` rescaling that we
    avoid by working in T-form throughout.

    NOTE: previous draft (post-Gemini-review) used σ-form.
    Reverted to T-form because:
    1. F_p compatibility (per user direction).
    2. The Mathlib-port aligns naturally with `ℤ[q, q⁻¹]`.
    3. The σ-form's `q^{1/2}` necessitates `ℚ(q^{1/2})` which
       has poor F_p reduction properties.

    For the q-integer convention, the T-form analogue is
    `[k]_q := (q^k − 1) / (q − 1)` (a polynomial in q, integer
    coefficients).  See `QOU.HeckeAlgebra.JonesMarkovWenzl`. -/
-- Ref: [hoefsmit1974] Hoefsmit, PhD thesis, UBC (1974) — seminormal Hecke relation T_i² = (q−1)T_i + q
axiom HoefsmitMatrix_hecke_relation : ∀ {n : ℕ} (lam : Nat.Partition n) (q : ℝ)
    (i : Fin (n - 1)),
    (HoefsmitMatrix lam q i) * (HoefsmitMatrix lam q i) =
      (q - 1) • (HoefsmitMatrix lam q i) + q • 1

/-- **Braid relation** (axiomatised): `T_i T_{i+1} T_i = T_{i+1}
    T_i T_{i+1}` whenever both `i` and `i+1` index valid
    generators (`i+1 < n - 1`).

    This is the T-form braid relation matching the T-form Hecke
    relation `T_i^2 = (q − 1) T_i + q` above.  The braid relation
    has the same shape as the σ-form (it does not depend on the
    quadratic relation), but we phrase it in T's to keep this
    file uniformly in the T-form / `ℤ[q, q⁻¹]`-friendly setup. -/
-- Ref: [hoefsmit1974] Hoefsmit, PhD thesis, UBC (1974) — seminormal braid relation T_i T_{i+1} T_i = T_{i+1} T_i T_{i+1}
axiom HoefsmitMatrix_braid_relation : ∀ {n : ℕ} (lam : Nat.Partition n) (q : ℝ)
    (i j : Fin (n - 1)) (_h_adj : j.val = i.val + 1),
    (HoefsmitMatrix lam q i) * (HoefsmitMatrix lam q j) * (HoefsmitMatrix lam q i) =
      (HoefsmitMatrix lam q j) * (HoefsmitMatrix lam q i) * (HoefsmitMatrix lam q j)

end QOU.HeckeAlgebra.Hoefsmit
