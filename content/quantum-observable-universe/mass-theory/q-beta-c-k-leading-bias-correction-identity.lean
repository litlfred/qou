/-
  # Leading-bias correction identity for joint-fit c_k extraction

  Sibling .lean for `prop:q-beta-c-k-leading-bias-correction-identity`.

  Given algebraic ladder coefficients `c_alg : ℕ → R` and a leading-order
  bias model

      ĉ_j := c_alg j + c_alg (j+1) * u,

  the bias-corrected value `ĉ_k - ĉ_{k+1} * u` equals `c_alg k - c_alg (k+2) * u²`,
  i.e. recovers `c_alg k` modulo a residual at order `u²`.

  Sorry-free, one-line `ring` proof in `CommRing R`. The proposition is the
  algebraic core of the empirical finding in
  `qbeta_ck_truncation_bias_correction_probe.py` (PR #1824 probe 6.a), which
  showed the bias correction recovers c_2 = -1 (canonical) and c_3 = -2
  (= J_Hopf(q=1)) to ppm precision.

  Three results:
    * `bias_correction_recovers_alg` — the headline identity.
    * `bias_correction_residual_is_quadratic` — the residual after correction
      is exactly `-c_alg (k+2) * u²`, structurally bounded by the (k+2)-th
      coefficient and `u²`.
    * `bias_correction_recovers_alg_exact_when_truncated` — if the ladder
      terminates at depth ≤ k+1 (`c_alg (k+2) = 0`), the correction is exact.

  Ref: [pr1786] https://github.com/litlfred/qou/pull/1786
       [pr1824] https://github.com/litlfred/qou/pull/1824
       computations/qbeta/qbeta_ck_truncation_bias_correction_probe.py
-/

import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

namespace QOU.QBeta.CkLeadingBiasCorrection

universe u

/-- The leading-order extraction-bias model for the joint-fit c_k
    extraction.  Given algebraic ladder coefficients `c_alg` and a
    small parameter `u`, the extracted ĉ_j is modeled as

        ĉ_j = c_alg j + c_alg (j+1) * u.

    This is the structural assumption motivating the bias-correction
    identity below. -/
def biasedExtraction {R : Type u} [CommRing R]
    (c_alg : ℕ → R) (u : R) (j : ℕ) : R :=
  c_alg j + c_alg (j + 1) * u

/-- **Bias correction recovers c_alg modulo u².**

    Given the leading-order bias model, the bias-corrected value
    `ĉ_k - ĉ_{k+1} * u` equals `c_alg k - c_alg (k+2) * u²`.  The
    residual is structurally at order `u²` and bounded by the
    (k+2)-th algebraic coefficient.

    Pure ring identity, holds over any commutative ring. -/
theorem bias_correction_recovers_alg {R : Type u} [CommRing R]
    (c_alg : ℕ → R) (u : R) (k : ℕ) :
    biasedExtraction c_alg u k - biasedExtraction c_alg u (k + 1) * u
      = c_alg k - c_alg (k + 2) * u ^ 2 := by
  simp only [biasedExtraction]
  ring

/-- **The residual after bias correction is exactly `-c_alg (k+2) · u²`.**

    Restating the previous result by isolating the residual on the RHS.
    Shows that the leading bias correction is exact up to a single
    quadratic-in-u term. -/
theorem bias_correction_residual_is_quadratic {R : Type u} [CommRing R]
    (c_alg : ℕ → R) (u : R) (k : ℕ) :
    biasedExtraction c_alg u k - biasedExtraction c_alg u (k + 1) * u
      - c_alg k = -(c_alg (k + 2)) * u ^ 2 := by
  simp only [biasedExtraction]
  ring

/-- **Bias correction is EXACT when the ladder terminates.**

    If the algebraic ladder is zero from index `k+2` onward (a
    truncated generating function), the bias correction exactly
    recovers `c_alg k`. -/
theorem bias_correction_recovers_alg_exact_when_truncated
    {R : Type u} [CommRing R]
    (c_alg : ℕ → R) (u : R) (k : ℕ) (h : c_alg (k + 2) = 0) :
    biasedExtraction c_alg u k - biasedExtraction c_alg u (k + 1) * u
      = c_alg k := by
  rw [bias_correction_recovers_alg, h]
  ring

end QOU.QBeta.CkLeadingBiasCorrection
