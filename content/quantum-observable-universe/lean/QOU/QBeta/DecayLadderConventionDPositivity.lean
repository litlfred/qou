/-
  # Convention D is incompatible with the Q_β ladder's three-row weight instance

  S1 (PR #5187), owner instruction "derive D ladder", following the
  2026-08-15 ruling that convention D (`z_D = q³/(q²+1)`) is canonical and
  C (`z_C = √q/(1+q)`) is excised for the registered channels.

  ## What this file settles, and why it is the answer to "derive the D ladder"

  The Q_β precision ladder is

      Q_β(q) = Q_A(q) · cos(α(q) − u/2) · ∏_{k≥2} (1 + c_k u^k),
      α = (z − 1)·h/2,   u = b·ℏ_q²,

  and `α` is the **only** place a Markov-trace convention enters it — `Q_A`,
  `h`, `ℏ_q`, `b`, `u` and the N=2 factor `1 − b²ℏ_q⁴` are all z-free.  That
  `α` is built from the explicit three-row weight instance

      y = (y_(3), y_(2,1), y_(1³)) = (z, 1/2 − z, z)

  of `CanonicalMarkovWeightsH3`; indeed `α = −h/4 − (h/2)·y_(2,1)`, so `α` is
  an affine functional of the standard-block weight **alone**.

  So the question "what ladder does convention D support?" reduces to: what
  is `y_(2,1)` at `z_D`?  This file answers it.

  **`z_D(q) > 1/2` for every `q > 1`** (`zD_gt_half`), hence

      y_(2,1) = 1/2 − z_D(q) < 0   for every substrate value q > 1

  (`threeRowMiddleWeight_neg_at_zD`).  A Markov trace with a **strictly
  negative** Wedderburn weight is not a positive trace, so the ladder's `α`
  formula has no positive-trace reading at `z_D` — not merely at the pin
  `q₀ ≈ 1.10998`, but on the whole substrate regime.  Convention C is the
  opposite case: `z_C(q) < 1/2` for every `q > 1` (`zC_lt_half`), so
  `y_(2,1) > 0` there (`threeRowMiddleWeight_pos_at_zC`).

  ## Relation to the existing exclusion

  `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` shows the mirror obstruction:
  at `z_C` the sign-block weight `y_(1³)` is nonzero, so convention C is
  incompatible with the two-row cap that forces D in the mass channel.  Read
  together:

  * the three-row weight instance — the one the ladder's `α` is derived
    from — **admits C and excludes D** (this file);
  * the two-row forcing **admits D and excludes C** (the existing theorem).

  Therefore the D-frame ladder is **not** obtained by substituting `z_D` into
  `α = (z−1)h/2`.  That substitution evaluates the three-row instance outside
  its positivity domain.  Deriving a genuine D ladder requires first deriving
  the D-frame **two-row** weight vector and recomputing `α` from it; that is
  open (see the S1 audit doc).

  ## Scope

  Scope-(b) **structural exclusion** in the sense of AGENTS.md
  §"Before declaring refuted": the excluded object is named (the three-row
  instance `(z, 1/2−z, z)` at `z_D`) and the invariant forbidding it is a
  proved sign condition, not a numerical miss.  It excludes **that weight
  instance at that parameter**; it does not exclude convention D for the
  decay channel, which stays `disputed` per registry §9g.

  Sorry-free.

  Ref: [jones1987] https://doi.org/10.2307/1971403
       [wenzl1988] https://doi.org/10.1007/BF02101492
       docs/coordination/ck-dk-canonical-registry.md §9g
       docs/audits/2026-08-16-s1-derive-d-ladder.md
       computations/qbeta/qbeta_d_frame_ladder_structure_probe.py
-/

import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith

namespace QOU.QBeta

/-- The convention-D Markov parameter, `z_D(q) = q³/(q²+1)`. -/
noncomputable def zD (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

/-- The convention-C Markov parameter, `z_C(q) = √q/(1+q)`. -/
noncomputable def zC (q : ℝ) : ℝ := Real.sqrt q / (1 + q)

/-- The standard-block (`λ = (2,1)`) weight of the explicit three-row
    instance `y = (z, 1/2 − z, z)` of `CanonicalMarkovWeightsH3`.

    The Q_β ladder's phase is the affine functional
    `α = −h/4 − (h/2)·threeRowMiddleWeight z`, so this is the single
    quantity through which a Markov-trace convention reaches the ladder. -/
noncomputable def threeRowMiddleWeight (z : ℝ) : ℝ := 1 / 2 - z

/-- **`z_D(q) > 1/2` on the whole substrate regime `q > 1`.**

    The cubic `2q³ − q² − 1` factors as `(q − 1)(2q² + q + 1)`, whose second
    factor is positive for all real `q`; so the inequality is strict and
    holds for every `q > 1`, degenerating to equality only at the classical
    point `q = 1`. -/
theorem zD_gt_half (q : ℝ) (hq : 1 < q) : 1 / 2 < zD q := by
  have hden : (0 : ℝ) < q ^ 2 + 1 := by positivity
  rw [zD, lt_div_iff₀ hden]
  nlinarith [sq_nonneg q, sq_nonneg (q - 1), sq_nonneg (q + 1)]

/-- **The three-row middle weight is strictly negative at `z_D`, for every
    `q > 1`.**

    Immediate from `zD_gt_half`.  Its content: the explicit three-row weight
    instance the ladder's phase is built from fails positivity at the
    convention-D Markov parameter throughout the substrate regime, so the
    phase `α = (z_D − 1)h/2` is not the phase of any positive Markov trace
    in that instance. -/
theorem threeRowMiddleWeight_neg_at_zD (q : ℝ) (hq : 1 < q) :
    threeRowMiddleWeight (zD q) < 0 := by
  have := zD_gt_half q hq
  simp only [threeRowMiddleWeight]
  linarith

/-- **`z_C(q) < 1/2` on the whole substrate regime `q > 1`.**

    With `s = √q > 1`, the claim `2s < 1 + s²` is `0 < (s − 1)²`. -/
theorem zC_lt_half (q : ℝ) (hq : 1 < q) : zC q < 1 / 2 := by
  have hq0 : (0 : ℝ) < q := lt_trans zero_lt_one hq
  have hs : Real.sqrt q ^ 2 = q := Real.sq_sqrt hq0.le
  have hs1 : 1 < Real.sqrt q := by
    have : Real.sqrt 1 < Real.sqrt q := by
      exact Real.sqrt_lt_sqrt zero_le_one hq
    simpa using this
  have hden : (0 : ℝ) < 1 + q := by linarith
  rw [zC, div_lt_iff₀ hden]
  nlinarith [sq_nonneg (Real.sqrt q - 1)]

/-- **The three-row middle weight is strictly positive at `z_C`, for every
    `q > 1`** — the mirror of `threeRowMiddleWeight_neg_at_zD`. -/
theorem threeRowMiddleWeight_pos_at_zC (q : ℝ) (hq : 1 < q) :
    0 < threeRowMiddleWeight (zC q) := by
  have := zC_lt_half q hq
  simp only [threeRowMiddleWeight]
  linarith

/-- **The two conventions sit on opposite sides of the positivity boundary.**

    Capstone: for every substrate value `q > 1` the three-row middle weight
    is positive at `z_C` and negative at `z_D`.  There is no `q > 1` at which
    both readings are positive, so the ladder's three-row phase formula
    cannot be transported from C to D by substituting the parameter. -/
theorem threeRow_positivity_separates_zC_zD (q : ℝ) (hq : 1 < q) :
    0 < threeRowMiddleWeight (zC q) ∧ threeRowMiddleWeight (zD q) < 0 :=
  ⟨threeRowMiddleWeight_pos_at_zC q hq, threeRowMiddleWeight_neg_at_zD q hq⟩

end QOU.QBeta
