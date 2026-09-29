import QOU.MathlibExt.QIntegerFactorial
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Notation

/-!
# QOU.Hecke.H2GramArithmetic — the n=2 Gram determinant, arithmetic core

The smallest Iwahori–Hecke algebra `H_2(q)` (one generator `σ`,
`σ² = (q-1)σ + q`) is `2`-dimensional with basis `{1, σ}` — it is
`AdjoinRoot(X² - (q-1)X - q)`, the monogenic algebra on the quadratic
Hecke relation.  Its **regular trace form Gram determinant** equals the
discriminant of that quadratic, and this file proves — sorry-free over a
field — the arithmetic identity behind the Wenzl criterion at `n = 2`:

  `disc = (q-1)² + 4q = (q+1)² = [2]_q²`,   and
  `H_2(q)` semisimple ⟺ `disc ≠ 0` ⟺ `q ≠ -1` ⟺ `[2]_q! ≠ 0`.

So `det(Gram) = [2]_q² ≠ 0 ⟺ [2]_q! ≠ 0` — the `n = 2` instance of the
Schur/Poincaré identity `det(Gram) = [n]_q!` (up to a unit).  The `Gram`
entries here (`tr(1) = 2`, `tr(σ) = q-1`, `tr(σ²) = q²+1`) are *asserted*
as the companion-matrix traces; the companion sibling
`QOU.Hecke.H2CompanionRep` (brick `qou-eedq`) *derives* them from the
**regular representation** `σ ↦ !![0, q; 1, q-1]`, proving that matrix
satisfies the Hecke relation and that its trace-form Gram equals
`h2GramMatrix` below — so `det = [2]_q²` rests on the representation, not
on hand-read traces.
-/

namespace QOU.Hecke

open QOU.MathlibExt

variable {K : Type*} [Field K]

/-- `[2]_q = 1 + q` (sorry-free). -/
theorem qInt_two (q : K) : qInt q 2 = 1 + q := by
  simp [qInt, Finset.sum_range_succ]

/-- `[2]_q! = 1 + q` (sorry-free). -/
theorem qFactorial_two (q : K) : qFactorial q 2 = 1 + q := by
  simp [qFactorial, Finset.prod_range_succ, qInt, Finset.sum_range_succ]

/-- **The `H_2` discriminant = `[2]_q²` (sorry-free).**  The discriminant
    of `X² - (q-1)X - q` is `(q-1)² + 4q = (q+1)²`, which is exactly the
    square of the quantum integer `[2]_q = 1 + q`. -/
theorem h2_disc_eq_qInt_two_sq (q : K) :
    (q - 1) ^ 2 + 4 * q = qInt q 2 ^ 2 := by
  rw [qInt_two]; ring

/-- **`H_2` Gram-determinant criterion (sorry-free).**  The Gram
    determinant `det = (q+1)² = [2]_q²` is nonzero iff `[2]_q! ≠ 0` iff
    `q ≠ -1` — the `n = 2` instance of Wenzl's semisimplicity criterion. -/
theorem h2_gram_det_ne_zero_iff (q : K) :
    qInt q 2 ^ 2 ≠ 0 ↔ qFactorial q 2 ≠ 0 := by
  rw [qInt_two, qFactorial_two, pow_ne_zero_iff (by norm_num : 2 ≠ 0)]

/-- The criterion in bare-parameter form: `H_2(q)` is semisimple iff
    `q ≠ -1` (sorry-free). -/
theorem h2_gram_det_ne_zero_iff_q_ne_neg_one (q : K) :
    qInt q 2 ^ 2 ≠ 0 ↔ q ≠ -1 := by
  rw [qInt_two, pow_ne_zero_iff (by norm_num : 2 ≠ 0), ne_eq, ne_eq,
    not_iff_not]
  constructor
  · exact fun h => eq_neg_of_add_eq_zero_right h
  · exact fun h => by rw [h]; ring

open Matrix in
/-- **The `H_2(q)` regular-trace Gram matrix** in the basis `{1, σ}`.
    Entries are the observable traces `tr(L_{eᵢ eⱼ})`: `tr(1) = 2`,
    `tr(σ) = q-1` (companion-matrix trace of `σ² = (q-1)σ + q`),
    `tr(σ²) = tr((q-1)σ + q·1) = (q-1)² + 2q = q²+1`.  Taking the trace is
    the observation step — the Gram *is* a matrix of observable results. -/
def h2GramMatrix (q : K) : Matrix (Fin 2) (Fin 2) K :=
  !![2, q - 1; q - 1, q ^ 2 + 1]

open Matrix in
/-- **The `H_2` Gram determinant equals `[2]_q²` (sorry-free).**  A direct
    `2×2` determinant: `det = 2(q²+1) - (q-1)² = (q+1)² = [2]_q²`.  This is
    the actual regular-trace Gram determinant — the `n = 2` case of
    `det(Gram) = [n]_q!` (up to a unit) — now at the matrix level. -/
theorem h2GramMatrix_det (q : K) : (h2GramMatrix q).det = qInt q 2 ^ 2 := by
  rw [h2GramMatrix, Matrix.det_fin_two_of, qInt_two]; ring

/-- **`H_2` semisimple ⟺ nonzero Gram determinant ⟺ `[2]_q! ≠ 0`
    (sorry-free).**  Ties the concrete matrix determinant to Wenzl's
    criterion at `n = 2`. -/
theorem h2GramMatrix_det_ne_zero_iff (q : K) :
    (h2GramMatrix q).det ≠ 0 ↔ qFactorial q 2 ≠ 0 := by
  rw [h2GramMatrix_det, h2_gram_det_ne_zero_iff]

end QOU.Hecke
