/-
# Exact discriminants of the colour-tube sextic and its reductions

Companion to `QOU.Brings.ColourCubicDiscriminant`, which reduces the palindromic
sextic

    16z⁶ + 24z⁵ + 35z⁴ + 50z³ + 35z² + 24z + 16

through `16w³ + 24w² − 13w + 2` to the trinomial `u³ − u + 2/5`. This file proves
the three **discriminant values**, sorry-free and by exact integer/rational
arithmetic only:

| polynomial | discriminant | theorem |
|---|---|---|
| sextic `16z⁶+24z⁵+35z⁴+50z³+35z²+24z+16` | `−5120000000000 = −2¹⁹·5¹⁰` | `colourSextic_discr` |
| reduced cubic `16w³+24w²−13w+2` | `−80000 = −2⁷·5⁴` | `reducedCubic_discr` |
| trinomial `u³ − u + 2/5` | `−8/25 = −2³/5²` | `saddleTrinomial_discr` |

## What "discriminant" means here — read this before citing

This Mathlib pin has **no `Polynomial.disc`**: the
`Mathlib/RingTheory/Polynomial/Resultant/*` modules are absent from the cached
oleans. So the discriminant is defined explicitly, by the classical Sylvester
formula, on **coefficient vectors listed from the leading coefficient down**:

* `sylvesterMatrix p q` is the `(n+m)×(n+m)` Sylvester matrix of a degree-`m`
  polynomial `p` and a degree-`n` polynomial `q`: `n` shifted rows of `p`'s
  coefficients followed by `m` shifted rows of `q`'s;
* `resultant p q := det (sylvesterMatrix p q)`;
* `derivCoeffs a` is the coefficient vector of the formal derivative
  (`(N−k)·a_k`, `k = 0 … N−1`, for a degree-`N` vector `a`);
* `discr a := (−1)^(N(N−1)/2) · a₀⁻¹ · resultant a (derivCoeffs a)`.

This is the textbook definition (Gelfand–Kapranov–Zelevinsky, *Discriminants,
Resultants and Multidimensional Determinants*, Ch. 12). What is **not** proved
here is its equivalence with the root form `a₀^(2N−2) ∏_(i<j) (rᵢ − rⱼ)²`; that
equivalence is classical but not formalised in this file. The coefficient
vectors are tied to the corpus's own polynomial definitions by the `*_eval`
lemmas, so they are checked to be the right polynomials rather than asserted.

## How the determinants are computed (no `native_decide`)

* **Sextic (11×11).** Over `ℤ`, an explicit lower-triangular integer matrix `E`
  (a row-scaled inverse Doolittle factor) satisfies `E · Syl = V` with `V`
  upper-triangular; that matrix identity is checked by the kernel with `decide`.
  Then `det E · det Syl = det V`, both triangular determinants are products of
  diagonal entries, and cancellation gives `det Syl = 2²³·5¹⁰`. The `ℚ`
  statement follows by mapping the Sylvester matrix along `Int.castRingHom ℚ`.
* **Cubics (5×5).** Over `ℚ`, `Syl = L · U` with `L` unit lower-triangular and
  `U` upper-triangular, checked entrywise by `simp`/`norm_num`.

The certificates `E`, `V`, `L`, `U` were generated with `sympy` (which also gives
the same three discriminants via `sympy.discriminant`); the Lean proofs check
them and do not trust that computation.
-/
import Mathlib.LinearAlgebra.Matrix.Block
import Mathlib.Tactic
import QOU.Brings.ColourCubicDiscriminant

namespace QOU.Brings

open Matrix

/-- The Sylvester matrix of `p` (degree `m`; `p 0` leading, …, `p m` constant)
and `q` (degree `n`, same convention). Rows `0 … n−1` are the coefficients of
`p` shifted right by the row index; rows `n … n+m−1` are those of `q`, shifted
by `row − n`. -/
def sylvesterMatrix {R : Type*} [CommRing R] {m n : ℕ} (p : Fin (m + 1) → R)
    (q : Fin (n + 1) → R) : Matrix (Fin (n + m)) (Fin (n + m)) R :=
  Matrix.of fun i j =>
    if i.val < n then
      (if h : i.val ≤ j.val ∧ j.val - i.val ≤ m then p ⟨j.val - i.val, by omega⟩ else 0)
    else
      (if h : i.val - n ≤ j.val ∧ j.val - (i.val - n) ≤ n then
        q ⟨j.val - (i.val - n), by omega⟩ else 0)

/-- The resultant of two leading-first coefficient vectors: the Sylvester
determinant. -/
def resultant {R : Type*} [CommRing R] {m n : ℕ} (p : Fin (m + 1) → R)
    (q : Fin (n + 1) → R) : R :=
  (sylvesterMatrix p q).det

/-- Leading-first coefficient vector of the formal derivative of the degree-`(d+1)`
polynomial with leading-first coefficients `a`: entry `k` is `(d + 1 − k) · a k`. -/
def derivCoeffs {R : Type*} [CommRing R] {d : ℕ} (a : Fin (d + 2) → R) : Fin (d + 1) → R :=
  fun k => ((d + 1 - k.val : ℕ) : R) * a (Fin.castSucc k)

/-- The discriminant of the degree-`N` polynomial (`N = d + 1`) with leading-first
coefficient vector `a`, by the Sylvester formula `(−1)^(N(N−1)/2) · a₀⁻¹ · Res(f, f')`. -/
noncomputable def discr {R : Type*} [Field R] {d : ℕ} (a : Fin (d + 2) → R) : R :=
  (-1) ^ ((d + 1) * d / 2) * (a 0)⁻¹ * resultant a (derivCoeffs a)

/-- The Sylvester matrix commutes with ring homomorphisms applied coefficientwise. -/
theorem sylvesterMatrix_map {R S : Type*} [CommRing R] [CommRing S] (f : R →+* S)
    {m n : ℕ} (p : Fin (m + 1) → R) (q : Fin (n + 1) → R) :
    sylvesterMatrix (fun k => f (p k)) (fun k => f (q k)) = (sylvesterMatrix p q).map f := by
  ext i j
  simp only [sylvesterMatrix, Matrix.of_apply, Matrix.map_apply]
  split_ifs <;> simp

/-- `derivCoeffs` commutes with ring homomorphisms applied coefficientwise. -/
theorem derivCoeffs_map {R S : Type*} [CommRing R] [CommRing S] (f : R →+* S) {d : ℕ}
    (a : Fin (d + 2) → R) :
    derivCoeffs (fun k => f (a k)) = fun k => f (derivCoeffs a k) := by
  funext k
  simp [derivCoeffs]

/-- Cancellation step used to read a determinant off an elimination certificate:
from `e · x = v`, `e = cₑ ≠ 0`, `v = cᵥ` and `cₑ · r = cᵥ`, conclude `x = r`. Stated
with the determinants as opaque variables so that no tactic ever compares two
concrete determinants up to unfolding. -/
theorem eq_of_mul_eq_of_eq {e x v ce cv r : ℤ} (h : e * x = v) (he : e = ce) (hv : v = cv)
    (hce : ce ≠ 0) (hr : ce * r = cv) : x = r := by
  subst he hv
  exact mul_left_cancel₀ hce (h.trans hr.symm)

/-! ### The sextic -/

/-- Leading-first coefficients of the colour sextic, over `ℤ`. -/
def colourSexticCoeffsZ : Fin 7 → ℤ := ![16, 24, 35, 50, 35, 24, 16]

/-- Leading-first coefficients of the colour sextic, over `ℚ`. -/
def colourSexticCoeffs : Fin 7 → ℚ := ![16, 24, 35, 50, 35, 24, 16]

/-- The coefficient vector is the corpus's `colourSextic`. -/
theorem colourSexticCoeffs_eval (z : ℚ) :
    ∑ k : Fin 7, colourSexticCoeffs k * z ^ (6 - k.val) = colourSextic z := by
  simp [colourSexticCoeffs, colourSextic, Fin.sum_univ_succ]
  ring

/-- Elimination certificate, left factor: lower-triangular, integer entries
(a row-scaled inverse of the Doolittle factor of the sextic's Sylvester matrix). -/
def colourSexticElimE : Matrix (Fin (5 + 6)) (Fin (5 + 6)) ℤ :=
  !![1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0; 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0; 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0; 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0; 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0; -768, 192, 272, 372, -633, 128, 0, 0, 0, 0, 0; 243072, -127680, -69360, -94040, 232755, -40512, 11152, 0, 0, 0, 0; -4468896, 859896, -884100, 2888550, -2662250, 744816, 42888, 421861, 0, 0, 0; -5111520, -1366008, -1846772, 969950, -522600, 851920, 440648, 719679, 586973, 0, 0; -250848, -444792, -227556, -101674, 10300, 41808, 84584, 73879, 85623, 52366, 0; 9888, 9288, -2092, -2182, -2342, -1648, -1960, -725, -1310, 215, 1228]

/-- Elimination certificate, result: upper-triangular, integer entries. -/
def colourSexticElimV : Matrix (Fin (5 + 6)) (Fin (5 + 6)) ℤ :=
  !![16, 24, 35, 50, 35, 24, 16, 0, 0, 0, 0; 0, 16, 24, 35, 50, 35, 24, 16, 0, 0, 0; 0, 0, 16, 24, 35, 50, 35, 24, 16, 0, 0; 0, 0, 0, 16, 24, 35, 50, 35, 24, 16, 0; 0, 0, 0, 0, 16, 24, 35, 50, 35, 24, 16; 0, 0, 0, 0, 0, 2788, -1715, -9030, -8875, -9240, -10128; 0, 0, 0, 0, 0, 0, 2109305, 4638830, 4779705, 4081480, 3724080; 0, 0, 0, 0, 0, 0, 0, -29348650, -37999150, -17677200, -42596000; 0, 0, 0, 0, 0, 0, 0, 0, -10473200, 2976800, -8361600; 0, 0, 0, 0, 0, 0, 0, 0, 0, -122800, 164800; 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -8000]

/-- The elimination certificate holds: `E · Syl = V`. Kernel-checked by `decide`
(exact `ℤ` arithmetic). -/
theorem colourSextic_sylvester_elim :
    colourSexticElimE * sylvesterMatrix colourSexticCoeffsZ (derivCoeffs colourSexticCoeffsZ) =
      colourSexticElimV := by
  decide

theorem colourSexticElimE_lowerTriangular :
    colourSexticElimE.BlockTriangular OrderDual.toDual := by
  intro i j hij; fin_cases i <;> fin_cases j <;> first | rfl | (revert hij; decide)

theorem colourSexticElimV_upperTriangular : colourSexticElimV.BlockTriangular id := by
  intro i j hij; fin_cases i <;> fin_cases j <;> first | rfl | (revert hij; decide)

theorem colourSexticElimE_det : colourSexticElimE.det = 22729924915839933910564864 := by
  rw [det_of_lowerTriangular _ colourSexticElimE_lowerTriangular]
  decide

theorem colourSexticElimV_det :
    colourSexticElimV.det = 1862035449105607385953473658880000000000 := by
  rw [det_of_upperTriangular colourSexticElimV_upperTriangular]
  decide

/-- **The sextic's resultant with its derivative**, over `ℤ`:
`Res(f, f') = 2²³·5¹⁰ = 81920000000000`. -/
theorem colourSextic_resultant_int :
    resultant colourSexticCoeffsZ (derivCoeffs colourSexticCoeffsZ) = 81920000000000 := by
  have h : colourSexticElimE.det * resultant colourSexticCoeffsZ (derivCoeffs colourSexticCoeffsZ) =
      colourSexticElimV.det := by
    unfold resultant
    rw [← det_mul]
    exact congrArg Matrix.det colourSextic_sylvester_elim
  exact eq_of_mul_eq_of_eq h colourSexticElimE_det colourSexticElimV_det (by norm_num)
    (by norm_num)

/-- **The discriminant of the colour sextic**
`16z⁶ + 24z⁵ + 35z⁴ + 50z³ + 35z² + 24z + 16` is `−5120000000000 = −2¹⁹·5¹⁰`
(Sylvester-formula discriminant, see the module docstring). -/
theorem colourSextic_discr : discr colourSexticCoeffs = -5120000000000 := by
  have hc : colourSexticCoeffs = fun k => (Int.castRingHom ℚ) (colourSexticCoeffsZ k) := by
    funext k; fin_cases k <;> simp [colourSexticCoeffs, colourSexticCoeffsZ]
  have hres : resultant colourSexticCoeffs (derivCoeffs colourSexticCoeffs) =
      81920000000000 := by
    rw [hc, derivCoeffs_map, resultant, sylvesterMatrix_map, ← RingHom.mapMatrix_apply,
      ← RingHom.map_det]
    have := colourSextic_resultant_int
    unfold resultant at this
    rw [this]; norm_num
  unfold discr
  rw [hres]
  norm_num [colourSexticCoeffs]

/-- The same value as a prime factorisation: `−2¹⁹·5¹⁰`. -/
theorem colourSextic_discr_factored : discr colourSexticCoeffs = -(2 ^ 19 * 5 ^ 10) := by
  rw [colourSextic_discr]; norm_num

/-! ### The reduced cubic -/

/-- Leading-first coefficients of `reducedCubic`. -/
def reducedCubicCoeffs : Fin 4 → ℚ := ![16, 24, -13, 2]

/-- The coefficient vector is the corpus's `reducedCubic`. -/
theorem reducedCubicCoeffs_eval (w : ℚ) :
    ∑ k : Fin 4, reducedCubicCoeffs k * w ^ (3 - k.val) = reducedCubic w := by
  simp [reducedCubicCoeffs, reducedCubic, Fin.sum_univ_succ]
  ring

/-- `Syl = L · U` certificate for the reduced cubic. -/
theorem reducedCubic_sylvester_lu :
    sylvesterMatrix reducedCubicCoeffs (derivCoeffs reducedCubicCoeffs) =
    !![1, 0, 0, 0, 0; 0, 1, 0, 0, 0; 3, (-3/2), 1, 0, 0; 0, 3, (-12/31), 1, 0; 0, 0, (24/31), (21/5), 1] * !![16, 24, -13, 2, 0; 0, 16, 24, -13, 2; 0, 0, 62, (-51/2), 3; 0, 0, 0, (500/31), (-150/31); 0, 0, 0, 0, 5] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [sylvesterMatrix, derivCoeffs, reducedCubicCoeffs, Matrix.mul_apply,
      Fin.sum_univ_succ] <;> norm_num

/-- **The discriminant of the reduced cubic** `16w³ + 24w² − 13w + 2` is
`−80000 = −2⁷·5⁴`. -/
theorem reducedCubic_discr : discr reducedCubicCoeffs = -80000 := by
  unfold discr resultant
  rw [reducedCubic_sylvester_lu, det_mul, det_of_lowerTriangular, det_of_upperTriangular]
  · simp [Fin.prod_univ_succ, reducedCubicCoeffs]; norm_num
  · intro i j h; fin_cases i <;> fin_cases j <;> first | rfl | (revert h; decide)
  · intro i j h; fin_cases i <;> fin_cases j <;> first | rfl | (revert h; decide)

/-! ### The trinomial -/

/-- Leading-first coefficients of `saddleTrinomial`. -/
def saddleTrinomialCoeffs : Fin 4 → ℚ := ![1, 0, -1, 2 / 5]

/-- The coefficient vector is the corpus's `saddleTrinomial`. -/
theorem saddleTrinomialCoeffs_eval (u : ℚ) :
    ∑ k : Fin 4, saddleTrinomialCoeffs k * u ^ (3 - k.val) = saddleTrinomial u := by
  simp [saddleTrinomialCoeffs, saddleTrinomial, Fin.sum_univ_succ]
  ring

/-- `Syl = L · U` certificate for the trinomial. -/
theorem saddleTrinomial_sylvester_lu :
    sylvesterMatrix saddleTrinomialCoeffs (derivCoeffs saddleTrinomialCoeffs) =
    !![1, 0, 0, 0, 0; 0, 1, 0, 0, 0; 3, 0, 1, 0, 0; 0, 3, 0, 1, 0; 0, 0, (3/2), (9/10), 1] * !![1, 0, -1, (2/5), 0; 0, 1, 0, -1, (2/5); 0, 0, 2, (-6/5), 0; 0, 0, 0, 2, (-6/5); 0, 0, 0, 0, (2/25)] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [sylvesterMatrix, derivCoeffs, saddleTrinomialCoeffs, Matrix.mul_apply,
      Fin.sum_univ_succ] <;> norm_num

/-- **The discriminant of the trinomial** `u³ − u + 2/5` is `−8/25 = −2³/5²`. -/
theorem saddleTrinomial_discr : discr saddleTrinomialCoeffs = -8 / 25 := by
  unfold discr resultant
  rw [saddleTrinomial_sylvester_lu, det_mul, det_of_lowerTriangular, det_of_upperTriangular]
  · simp [Fin.prod_univ_succ, saddleTrinomialCoeffs]; norm_num
  · intro i j h; fin_cases i <;> fin_cases j <;> first | rfl | (revert h; decide)
  · intro i j h; fin_cases i <;> fin_cases j <;> first | rfl | (revert h; decide)

end QOU.Brings
