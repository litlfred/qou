/-
  # The Q_β ladder's affine phase coefficient `1/2 − z` at `z_C` and `z_D`

  S1 (PR #5187), owner instruction "derive D ladder", following the
  2026-08-15 ruling that convention D (`z_D = q³/(q²+1)`) is canonical and
  C (`z_C = √q/(1+q)`) is excised for the registered channels.

  ## ⚠️ RETRACTED: `1/2 − z` is NOT the Wedderburn weight `y_(2,1)`

  **This file originally claimed** that `1/2 − z` is the standard-block
  Wedderburn weight `y_(2,1)` of an explicit three-row instance
  `y = (z, 1/2 − z, z)` of `CanonicalMarkovWeightsH3`, and concluded from
  `1/2 − z_D < 0` that convention D has a **strictly negative Wedderburn
  weight**, hence no positive-trace reading.

  **That identification is false, and the conclusion inverts.**  S2
  (PR #5185, `claude/s2-gram-radical-quotient-2026-08-16`) solved the
  corpus's own three defining conditions for the `H₃(q)` Markov weights —
  the ones `TemperleyLiebTower.conventionD_kills_antisymmetriser` takes as
  hypotheses — symbolically over ℚ(q) at `z = z_D`:

  | λ | rows | `y_λ` under D | sign for `q > 1` |
  |---|---|---|---|
  | `(3)`  | 1 | `(q⁴+1)/(q²+1)²` | **positive** |
  | `(2,1)`| 2 | `q²/(q²+1)²`     | **positive** |
  | `(1³)` | 3 | `0`              | identically zero |

  The vector `(z, 1/2 − z, z)` satisfies **only** the normalisation
  condition `h1`; it **fails** `h2` and `h3`, the remaining defining
  conditions.  So it is not a weight vector of `H₃(q)` at all, and
  `1/2 − z_D` is simply not `y_(2,1)`.  At `q ≈ 1.11` the two differ in
  sign as well as magnitude: `1/2 − z_D ≈ −0.1127`, while the actual
  `y_(2,1) ≈ +0.2473`.

  **The corrected picture, from S2 and cited not re-derived:** under
  convention D the surviving weights are both **strictly positive** and the
  single dead weight `y_(1³)` is **exactly zero**, not negative — a
  **positive semidefinite** form of signature `(5, 0, 1)`.  Far from arguing
  against D, that is what a Temperley–Lieb trace should look like.
  Convention D does **not** fail positivity.

  This was a **symbol-collision / claim-shape failure** in the sense of
  AGENTS.md §"Grep the claim SHAPE, not only the topic": a formula was given
  the *name* of an object whose defining conditions it does not satisfy.
  Grepping the topic (`y_(2,1)`, Markov weights) found plenty; checking
  whether *this* expression satisfies the *defining conditions* of that
  object was the step that was skipped.

  ## What this file actually proves — unchanged and correct

  The Q_β precision ladder is

      Q_β(q) = Q_A(q) · cos(α(q) − u/2) · ∏_{k≥2} (1 + c_k u^k),
      α = (z − 1)·h/2,   u = b·ℏ_q²,

  and `α` is the **only** place a Markov-trace convention enters it — `Q_A`,
  `h`, `ℏ_q`, `b`, `u` and the N=2 factor `1 − b²ℏ_q⁴` are all z-free.  The
  phase is affine in the coefficient `1/2 − z`:

      α = −h/4 − (h/2)·(1/2 − z)                     (pure algebra)

  and this file locates that coefficient's sign for each convention:

  * **`z_D(q) > 1/2` for every `q > 1`** (`zD_gt_half`), hence
    `1/2 − z_D(q) < 0` (`ladderPhaseCoeff_neg_at_zD`);
  * **`z_C(q) < 1/2` for every `q > 1`** (`zC_lt_half`), hence
    `1/2 − z_C(q) > 0` (`ladderPhaseCoeff_pos_at_zC`).

  Both statements are true and were never in question.  What they establish
  is that the two conventions place the **ladder ansatz's phase** on
  opposite sides of the point `z = 1/2`, so the C ladder's phase formula
  does not transport to D by substituting the parameter.

  **The sign of `1/2 − z` carries no trace-positivity content whatsoever.**
  It is a threshold crossing of an affine coefficient in one ansatz, not a
  Wedderburn weight, and nothing about the positivity of any Markov trace
  may be inferred from it.

  ## Scope

  Scope-**(a)** scope-limited negative in the sense of AGENTS.md
  §"Before declaring refuted".  What is excluded is the *transport* of one
  ansatz's phase formula from C to D.  This is **not** a structural
  exclusion of convention D, and the earlier scope-(b) claim to that effect
  is withdrawn: the invariant it cited (a negative Wedderburn weight) does
  not exist.  Convention D's status in the decay channel stays `disputed`
  per registry §9g, on other grounds.

  Sorry-free.

  Ref: [jones1987] https://doi.org/10.2307/1971403
       [wenzl1988] https://doi.org/10.1007/BF02101492
       docs/coordination/ck-dk-canonical-registry.md §9g
       docs/audits/2026-08-16-s1-derive-d-ladder.md §4
       docs/audits/2026-08-16-s2-gram-radical-independent-revalidation.md §3bis
       computations/qbeta/qbeta_d_frame_ladder_structure_probe.py
-/

import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith

-- Declarations here are nested one namespace deeper than the module's
-- parent so this module and QOU.QBeta.LadderPhaseMirrorCovariance
-- can be imported together: both declared the same fully-qualified
-- name(s), and Lean rejects the second import with "environment already
-- contains" (bean `qou-kfcl`). Nothing imports this module, so the
-- nesting costs no consumer.
namespace QOU.QBeta.DecayLadderConventionDPositivity

/-- The convention-D Markov parameter, `z_D(q) = q³/(q²+1)`. -/
noncomputable def zD (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

/-- The convention-C Markov parameter, `z_C(q) = √q/(1+q)`. -/
noncomputable def zC (q : ℝ) : ℝ := Real.sqrt q / (1 + q)

/-- The Q_β ladder's **affine phase coefficient**, `1/2 − z`.

    The ladder's phase satisfies `α = (z−1)h/2 = −h/4 − (h/2)·(1/2 − z)`,
    pure algebra, so this is the single quantity through which the Markov
    parameter `z` reaches the ladder.

    **This is not a Wedderburn weight.**  It was previously named
    `threeRowMiddleWeight` and identified with the standard-block weight
    `y_(2,1)` of `H₃(q)`; that identification is retracted — see the module
    docstring.  The vector `(z, 1/2 − z, z)` satisfies only the
    normalisation condition of `CanonicalMarkovWeightsH3` and fails the
    other two, and the actual `y_(2,1)` under convention D is
    `q²/(q²+1)² > 0`.  No positivity claim about any Markov trace follows
    from the sign of this coefficient. -/
noncomputable def ladderPhaseCoeff (z : ℝ) : ℝ := 1 / 2 - z

/-- **`z_D(q) > 1/2` on the whole substrate regime `q > 1`.**

    The cubic `2q³ − q² − 1` factors as `(q − 1)(2q² + q + 1)`, whose second
    factor is positive for all real `q`; so the inequality is strict and
    holds for every `q > 1`, degenerating to equality only at the classical
    point `q = 1`. -/
theorem zD_gt_half (q : ℝ) (hq : 1 < q) : 1 / 2 < zD q := by
  have hden : (0 : ℝ) < q ^ 2 + 1 := by positivity
  rw [zD, lt_div_iff₀ hden]
  nlinarith [sq_nonneg q, sq_nonneg (q - 1), sq_nonneg (q + 1)]

/-- **The ladder's affine phase coefficient is strictly negative at `z_D`,
    for every `q > 1`.**

    Immediate from `zD_gt_half`.  Its content is exactly that `z_D` lies
    above `1/2` throughout the substrate regime, so the ladder ansatz's
    phase `α = (z_D − 1)h/2` sits on the far side of `−h/4` from where
    convention C puts it.

    **No trace-positivity content.**  `1/2 − z` is not a Wedderburn weight
    (module docstring); the actual convention-D weight `y_(2,1) = q²/(q²+1)²`
    is strictly *positive*.  Do not read this as "convention D has a negative
    weight" — that reading is retracted. -/
theorem ladderPhaseCoeff_neg_at_zD (q : ℝ) (hq : 1 < q) :
    ladderPhaseCoeff (zD q) < 0 := by
  have := zD_gt_half q hq
  simp only [ladderPhaseCoeff]
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

/-- **The ladder's affine phase coefficient is strictly positive at `z_C`,
    for every `q > 1`** — the mirror of `ladderPhaseCoeff_neg_at_zD`, and
    likewise carrying no trace-positivity content. -/
theorem ladderPhaseCoeff_pos_at_zC (q : ℝ) (hq : 1 < q) :
    0 < ladderPhaseCoeff (zC q) := by
  have := zC_lt_half q hq
  simp only [ladderPhaseCoeff]
  linarith

/-- **The two conventions sit on opposite sides of `z = 1/2`.**

    Capstone: for every substrate value `q > 1` the ladder's affine phase
    coefficient is positive at `z_C` and negative at `z_D`.  There is no
    `q > 1` at which the two agree in sign, so the C ladder's phase formula
    cannot be transported to D by substituting the parameter.

    **This is a statement about one ansatz's phase, not about either
    trace.**  The earlier reading — that it separates the conventions by
    *positivity of a Wedderburn weight* — is retracted (module docstring):
    under convention D the `H₃(q)` weights are positive semidefinite,
    signature `(5, 0, 1)`, per S2 (PR #5185). -/
theorem ladderPhaseCoeff_sign_separates_zC_zD (q : ℝ) (hq : 1 < q) :
    0 < ladderPhaseCoeff (zC q) ∧ ladderPhaseCoeff (zD q) < 0 :=
  ⟨ladderPhaseCoeff_pos_at_zC q hq, ladderPhaseCoeff_neg_at_zD q hq⟩

/-- The actual convention-D `H₃(q)` middle Wedderburn weight on the 2-d irrep
    `V_{(2,1)}`, solved from the three `H₃(q)` Markov defining conditions in
    `QOU.QBeta.MarkovWeightsConventionD` (PR #5185):
    `y_{(2,1)}(z_D) = q² / (q² + 1)²`. -/
noncomputable def wedderburnMiddleWeightD (q : ℝ) : ℝ :=
  q ^ 2 / (q ^ 2 + 1) ^ 2

/-- **The actual convention-D `H₃(q)` middle Wedderburn weight `y_{(2,1)}(z_D)`
    is strictly positive for every `q > 1`.** -/
theorem wedderburnMiddleWeightD_pos (q : ℝ) (hq : 1 < q) :
    0 < wedderburnMiddleWeightD q := by
  have hq0 : (0 : ℝ) < q := lt_trans zero_lt_one hq
  rw [wedderburnMiddleWeightD]
  positivity

/-- **Discrepancy theorem (`qou-q2oa`).** For every `q > 1`, the ladder's
    affine phase coefficient `κ(z_D) = 1/2 − z_D < 0` is strictly negative
    while the actual convention-D `H₃(q)` middle Wedderburn weight
    `y_{(2,1)}(z_D) = q²/(q²+1)² > 0` is strictly positive; hence
    `1/2 − z_D ≠ y_{(2,1)}(z_D)` throughout the substrate regime `q > 1`. -/
theorem ladderPhaseCoeff_ne_wedderburnMiddleWeight (q : ℝ) (hq : 1 < q) :
    ladderPhaseCoeff (zD q) ≠ wedderburnMiddleWeightD q := by
  have hneg := ladderPhaseCoeff_neg_at_zD q hq
  have hpos := wedderburnMiddleWeightD_pos q hq
  linarith

/-! ### `z_D` in Temperley–Lieb form

The Markov parameter of convention D is `q²` divided by the quantum integer
`[2]_q = q + q⁻¹` — the loop parameter `δ` of the Temperley–Lieb algebra.
The identity is purely algebraic: `q + q⁻¹ = (q² + 1)/q`, so
`q²/(q + q⁻¹) = q³/(q² + 1) = z_D`.

This is recorded because it is the shape of `z_D`, not evidence for a
mechanism.  Whether the D-frame trace actually *factors through* `TL_n` is a
hypothesis under test (S2's front, PR #5185, corank data at `n = 3, 4, 5`
only); this lemma is one algebraic input to that question and settles none
of it.  See the audit doc §6.

Stated over a generic field per AGENTS.md §7c — no ordering, no `Real.sqrt`,
nothing archimedean is involved.  The `ℝ` corollary is the specialisation.
(The convention-C mirror `z_C = 1/[2]_{√q}` is *not* stated generically: it
needs `Real.sqrt`, so it lives on the archimedean side of the wall.) -/
theorem zD_eq_qsq_div_bracketTwo {R : Type*} [Field R] (q : R)
    (hq : q ≠ 0) (hden : q ^ 2 + 1 ≠ 0) :
    q ^ 3 / (q ^ 2 + 1) = q ^ 2 / (q + q⁻¹) := by
  field_simp

/-- **`z_D(q) = q²/[2]_q`** — the archimedean specialisation of
`zD_eq_qsq_div_bracketTwo`, matching the definition `zD`. -/
theorem zD_eq_qsq_div_bracketTwo_real (q : ℝ) (hq : 0 < q) :
    zD q = q ^ 2 / (q + q⁻¹) := by
  have hden : q ^ 2 + 1 ≠ 0 := by positivity
  exact zD_eq_qsq_div_bracketTwo q (ne_of_gt hq) hden

end QOU.QBeta.DecayLadderConventionDPositivity
