/-
# QOU.QBeta.LadderCoeffNormalisation — `c₂` and `c̃₂` are different quantities,
# and the offset between them is exactly `1/8`.

Bean `qou-f09n` recorded a symbol collision: three distinct quantities in the
Q_β channel are all written `c₂`. Two of them come from the *same* model read
two ways, and the owner ruled (2026-08-16) that they get short distinct names,
following the register's existing `w_λ` / `w̃_λ` convention:

| name | value | what it is |
|---|---|---|
| `c₂` | `−1` | coefficient of the explicit ladder factor `(1 + c₂ x²)` |
| `c̃₂` | `−9/8` | `x²` coefficient of the normalised series |

This file proves the relation that makes those *two names for one model*
legitimate rather than a contradiction:

    c̃₂ = c₂ − 1/8      (`normalisedQuadCoeff_eq`)

so at `c₂ = −1` the normalised coefficient is `−9/8` (`normalisedQuadCoeff_at_neg_one`).
Neither number is wrong; they are related by an exact offset contributed by
the cosine factor, not by anything about `c₂`.

**Why the offset is `1/8` and not `1/2`.** The model's cosine factor is
`cos(A − x/2)`, and the half-argument is what supplies it: the second
derivative at `0` is `−cos A / 4`, so the quadratic Taylor coefficient is
`−cos A / 8`, i.e. `−1/8` after normalising by `cos A`. The value is
independent of `A` — the `A`-dependence cancels in the normalisation, which is
why the offset is a clean rational and not a function of the anchor.

**Scope.** This is a statement about reading one model two ways. It gives no
`c₂` value, no derivation of `A` (the ladder's phase `α`, un-derived in both
Markov conventions), and no accuracy claim. It exists so that the naming
decision rests on a theorem rather than on a symbolic run.

Base ring `ℝ`, per §7c: `Real.cos` is genuinely archimedean, so this belongs
on the real side of the substrate/archimedean wall.

-- Ref: [manuscript] bean `qou-f09n` (owner naming ruling, 2026-08-16);
-- `computations/qbeta/qbeta_ck_cache.py` (the `c₂ = −1` factor);
-- `computations/qbeta/qbeta_alpha_eff_ladder_reconciliation_probe.py`
-- (which measured the `−9/8` and reported it as a discrepancy).
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.QBeta

open Real

/-- The ladder's cosine factor as a function of the ladder variable, with the
phase `A` held fixed. In the producer this is `cos(α − u/2)` with `A = α`. -/
noncomputable def cosFactor (A x : ℝ) : ℝ := Real.cos (A - x / 2)

/-- The committed one-rung model: the cosine factor times the explicit
quadratic factor `(1 + c x²)`. In the producer, `c = c₂ = −1`. -/
noncomputable def ladderModel (A c x : ℝ) : ℝ :=
  cosFactor A x * (1 + c * x ^ 2)

/-- `d/dx cos(A − x/2) = sin(A − x/2)/2`. -/
theorem hasDerivAt_cosFactor (A x : ℝ) :
    HasDerivAt (cosFactor A) (Real.sin (A - x / 2) / 2) x := by
  have hin : HasDerivAt (fun t : ℝ => A - t / 2) (-(1 / 2)) x := by
    simpa using ((hasDerivAt_id x).div_const 2).const_sub A
  have := (Real.hasDerivAt_cos (A - x / 2)).comp x hin
  convert this using 1
  ring

/-- `d/dx sin(A − x/2)/2 = −cos(A − x/2)/4`. The two halvings compose to the
quarter, which is where the eventual `1/8` comes from. -/
theorem hasDerivAt_cosFactor' (A x : ℝ) :
    HasDerivAt (fun t : ℝ => Real.sin (A - t / 2) / 2)
      (-(Real.cos (A - x / 2)) / 4) x := by
  have hin : HasDerivAt (fun t : ℝ => A - t / 2) (-(1 / 2)) x := by
    simpa using ((hasDerivAt_id x).div_const 2).const_sub A
  have h := ((Real.hasDerivAt_sin (A - x / 2)).comp x hin).div_const 2
  convert h using 1
  ring

/-- Product rule for the model. -/
theorem hasDerivAt_ladderModel (A c x : ℝ) :
    HasDerivAt (ladderModel A c)
      (Real.sin (A - x / 2) / 2 * (1 + c * x ^ 2)
        + Real.cos (A - x / 2) * (c * (2 * x))) x := by
  have h2 : HasDerivAt (fun t : ℝ => 1 + c * t ^ 2) (c * (2 * x)) x := by
    simpa using ((hasDerivAt_pow 2 x).const_mul c).const_add 1
  exact (hasDerivAt_cosFactor A x).mul h2

/-- Second derivative of the model. -/
theorem hasDerivAt_ladderModel' (A c x : ℝ) :
    HasDerivAt (fun t : ℝ => Real.sin (A - t / 2) / 2 * (1 + c * t ^ 2)
        + Real.cos (A - t / 2) * (c * (2 * t)))
      ((-(Real.cos (A - x / 2)) / 4) * (1 + c * x ^ 2)
        + Real.sin (A - x / 2) / 2 * (c * (2 * x))
        + ((Real.sin (A - x / 2) / 2) * (c * (2 * x))
           + Real.cos (A - x / 2) * (c * 2))) x := by
  have h2 : HasDerivAt (fun t : ℝ => 1 + c * t ^ 2) (c * (2 * x)) x := by
    simpa using ((hasDerivAt_pow 2 x).const_mul c).const_add 1
  have h3 : HasDerivAt (fun t : ℝ => c * (2 * t)) (c * 2) x := by
    simpa using ((hasDerivAt_id x).const_mul 2).const_mul c
  exact ((hasDerivAt_cosFactor' A x).mul h2).add ((hasDerivAt_cosFactor A x).mul h3)

/-- `deriv` of the model, as a function — needed to iterate. -/
theorem deriv_ladderModel (A c : ℝ) :
    deriv (ladderModel A c)
      = fun x => Real.sin (A - x / 2) / 2 * (1 + c * x ^ 2)
          + Real.cos (A - x / 2) * (c * (2 * x)) :=
  funext fun x => (hasDerivAt_ladderModel A c x).deriv

/-- **The model's second derivative at `0` is `cos A · (2c − 1/4)`.**

The `−1/4` is the cosine factor's own contribution and the `2c` is the
explicit factor's; they are separate terms, which is exactly why reading the
same model at two normalisations gives two different "quadratic
coefficients". -/
theorem deriv_deriv_ladderModel_zero (A c : ℝ) :
    deriv (deriv (ladderModel A c)) 0 = Real.cos A * (2 * c - 1 / 4) := by
  rw [deriv_ladderModel]
  rw [(hasDerivAt_ladderModel' A c 0).deriv]
  norm_num
  ring

/-- The normalised quadratic (Taylor) coefficient of the model: the second
derivative at `0`, divided by `2!` and by the model's own value at `0`. This
is the `c̃₂` of the naming ruling. -/
noncomputable def normalisedQuadCoeff (A c : ℝ) : ℝ :=
  deriv (deriv (ladderModel A c)) 0 / (2 * ladderModel A c 0)

/-- **`c̃₂ = c₂ − 1/8`** — the exact offset between the two readings.

Independent of `A`: the phase cancels in the normalisation, so the offset is a
clean rational rather than an anchor-dependent quantity. This is what makes
`c₂` and `c̃₂` two names for one model rather than a contradiction. -/
theorem normalisedQuadCoeff_eq (A c : ℝ) (hA : Real.cos A ≠ 0) :
    normalisedQuadCoeff A c = c - 1 / 8 := by
  unfold normalisedQuadCoeff
  rw [deriv_deriv_ladderModel_zero]
  unfold ladderModel cosFactor
  norm_num
  field_simp
  ring

/-- **At the committed `c₂ = −1`, the normalised coefficient is `−9/8`.**

The two numbers the collision was reported as a discrepancy between. They are
the same model, read at two normalisations. -/
theorem normalisedQuadCoeff_at_neg_one (A : ℝ) (hA : Real.cos A ≠ 0) :
    normalisedQuadCoeff A (-1) = -(9 / 8) := by
  rw [normalisedQuadCoeff_eq A (-1) hA]
  norm_num

end QOU.QBeta
