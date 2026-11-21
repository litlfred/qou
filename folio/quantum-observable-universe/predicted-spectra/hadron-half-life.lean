import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.Calculus.Deriv.Pow


/-!
# QOU.Archimedean.hadron_half_life — Beta-decay half-life from the categorical action

The decay rate Γ_β is determined by the Markov trace ratio between
parent and daughter Gröbner normal forms, the pair Skein mass formula
S_ab(q) = (q μ_a + q⁻¹ μ_b)/(q^½ + q^{-½}), and the q-deformed
Fermi golden rule.

All quantities depend on q alone (no free parameters).

**The proposition's rate formula is carried in full** (added 2026-09-04,
bean `qou-jk6k`): `betaRate` is
`Γ_β = |𝒲(q)|² μ₀ /(2π³) · [2]_q · |ℳ_q|² · f(Q)` over `BetaRateData`
(the four non-`q`-shape factors with the positivity the manuscript asserts
of each), and `hadron_half_life d r = ln 2 / betaRate d r` is the
half-life the block states. `betaRate_eq_qPrefactor_iff` says exactly
what the older `BetaDecayData.halfLife = ln 2 / qPrefactor q` was: the
formula with those four factors collapsed onto the Sargent shape
`(q − q⁻¹)^5`. `hasDerivAt_qPrefactor` + `qSensitivity_eq_logDeriv` prove
the manuscript's sensitivity `∂ln Γ/∂ln q = (q²−1)/(q²+1) + 5(q²+1)/(q²−1)`
is the logarithmic derivative of that shape, and `qSensitivity_near_48`
checks the quoted `≈ 48`. Before this the ref named an alias for
`halfLife` and the rate formula had no Lean at all.

LaTeX label: `prop:hadron-half-life`

## References
- [leitner2026] §6/hadron-half-life

**Ground ring**: `ℝ` (geometric/analytic realisation).
Uses ℝ-specific analysis (trig, norms, real powers).
NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Archimedean

/-- Data for a beta-decay calculation in a Descartes universe.
    All quantities derived from q — no fitted parameters. -/
-- Ref: [leitner2026] §6/hadron-half-life
structure BetaDecayData where
  /-- Substrate parameter q. -/
  q : ℝ
  /-- q > 1 (non-classical universe). -/
  q_gt_one : 1 < q
  /-- Mass number A. -/
  A : ℕ
  /-- A ≥ 1. -/
  A_pos : 0 < A
  /-- Proton displacement δp = p - p_stab(A), integer-valued. -/
  delta_p : ℤ
  /-- The nucleus is unstable: δp ≠ 0. -/
  delta_p_ne_zero : delta_p ≠ 0
  /-- Dressed up-quark Skein mass μ_u > 0. -/
  mu_u : ℝ
  /-- mu_u is positive. -/
  mu_u_pos : 0 < mu_u
  /-- Dressed down-quark Skein mass μ_d > 0. -/
  mu_d : ℝ
  /-- mu_d is positive. -/
  mu_d_pos : 0 < mu_d

/-- Pair Skein mass: S_ab(q) = (q μ_a + q⁻¹ μ_b) / (q^½ + q^{-½}). -/
-- Ref: [leitner2026] §6/hadron-half-life
noncomputable def pairSkeinMass (q mu_a mu_b : ℝ) : ℝ :=
  (q * mu_a + 1/q * mu_b) / (q ^ (1/2 : ℝ) + q ^ (-(1/2 : ℝ)))

/-- The q-integer [2]_q = q + q⁻¹, categorical dimension of the
    SU_q(2) fundamental representation. -/
-- Ref: [leitner2026] §6/hadron-half-life
noncomputable def BetaDecayData.q_integer_2 (d : BetaDecayData) : ℝ :=
  d.q + 1 / d.q

/-- [2]_q > 2 when q > 1. -/
-- Ref: [leitner2026] §6/hadron-half-life
theorem BetaDecayData.q_integer_2_gt_two (d : BetaDecayData) :
    2 < d.q_integer_2 := by
  unfold q_integer_2
  have hq : 0 < d.q := by linarith [d.q_gt_one]
  have hcancel : d.q * (1 / d.q) = 1 := by field_simp
  nlinarith [sq_nonneg (d.q - 1), hq, hcancel, d.q_gt_one]

/-- The q-dependent prefactor of the decay rate:
    F(q) = (q + q⁻¹) · (q - q⁻¹)⁵.

    This vanishes at q = 1 (no beta decay in classical limit)
    and is positive for q > 1. -/
-- Ref: [leitner2026] §6/hadron-half-life
noncomputable def qPrefactor (q : ℝ) : ℝ :=
  (q + 1 / q) * (q - 1 / q) ^ 5

/-- The q-prefactor vanishes at q = 1 (classical limit). -/
-- Ref: [leitner2026] §6/hadron-half-life
theorem qPrefactor_classical : qPrefactor 1 = 0 := by
  unfold qPrefactor
  norm_num

/-- The q-prefactor is positive for q > 1. -/
-- Ref: [leitner2026] §6/hadron-half-life
theorem qPrefactor_pos {q : ℝ} (hq : 1 < q) : 0 < qPrefactor q := by
  unfold qPrefactor
  apply mul_pos
  · have : 0 < q := by linarith
    positivity
  · apply pow_pos
    rw [sub_pos, div_lt_iff₀ (by linarith : (0 : ℝ) < q)]
    nlinarith

/-- The `q`-SHAPE of the half-life: `ln 2 / qPrefactor q`.

    This is NOT the proposition's `t_{1/2} = ln 2 / Γ_β` — it is that formula
    with `|𝒲|² μ₀/(2π³) · |ℳ_q|² · f(Q)` collapsed onto `(q − q⁻¹)^5`
    (`betaRate_eq_qPrefactor_iff`). The full statement is `hadron_half_life`
    below. Kept because `qSensitivity` is its logarithmic derivative. -/
-- Ref: [leitner2026] §6/hadron-half-life
noncomputable def BetaDecayData.halfLife (d : BetaDecayData) : ℝ :=
  Real.log 2 / (qPrefactor d.q)

/-- The half-life is positive. -/
-- Ref: [leitner2026] §6/hadron-half-life
theorem BetaDecayData.halfLife_pos (d : BetaDecayData) : 0 < d.halfLife := by
  unfold halfLife
  exact div_pos (Real.log_pos (by norm_num : (1 : ℝ) < 2)) (qPrefactor_pos d.q_gt_one)

/-- Sensitivity: ∂ ln Γ / ∂ ln q = (q² - 1)/(q² + 1) + 5(q² + 1)/(q² - 1).

    At q = 1.1097 this evaluates to ≈ 48. -/
-- Ref: [leitner2026] §6/hadron-half-life
noncomputable def qSensitivity (q : ℝ) : ℝ :=
  (q ^ 2 - 1) / (q ^ 2 + 1) + 5 * (q ^ 2 + 1) / (q ^ 2 - 1)

/-- The sensitivity is positive for q > 1. -/
-- Ref: [leitner2026] §6/hadron-half-life
theorem qSensitivity_pos {q : ℝ} (hq : 1 < q) : 0 < qSensitivity q := by
  unfold qSensitivity
  have hq2 : 0 < q ^ 2 - 1 := by nlinarith
  have hq2' : 0 < q ^ 2 + 1 := by nlinarith
  positivity

/-- Proton mass from pair Skein weights: m_p = S_uu + 2 S_ud. -/
-- Ref: [leitner2026] §6/hadron-half-life
noncomputable def protonMass (q mu_u mu_d : ℝ) : ℝ :=
  pairSkeinMass q mu_u mu_u + 2 * pairSkeinMass q mu_u mu_d

/-- Neutron mass from pair Skein weights: m_n = 2 S_ud + S_dd. -/
-- Ref: [leitner2026] §6/hadron-half-life
noncomputable def neutronMass (q mu_u mu_d : ℝ) : ℝ :=
  2 * pairSkeinMass q mu_u mu_d + pairSkeinMass q mu_d mu_d

/-- Mass splitting: m_n - m_p = S_dd - S_uu. -/
-- Ref: [leitner2026] §6/hadron-half-life
theorem mass_splitting (q mu_u mu_d : ℝ) :
    neutronMass q mu_u mu_d - protonMass q mu_u mu_d =
    pairSkeinMass q mu_d mu_d - pairSkeinMass q mu_u mu_u := by
  unfold neutronMass protonMass
  ring

/-! ## The rate formula of `prop:hadron-half-life` (bean `qou-jk6k`) -/

/-- The four factors of `Γ_β` beyond the `q`-integer, as data, each with the
    positivity the manuscript asserts of it (items 1, 3, 4, 5 of
    `prf:hadron-half-life`). They are data because none of them has a closed
    form in the corpus yet: `|𝒲(q)|²` is `|tr_M((σ₁σ₂)⁵)|²` in `H₃(q)`
    (`def:beta-decay-skein` carries only its 10-crossing budget), `|ℳ_q|²` is
    `s² · ∏ |V̂ᵢ^par / V̂ᵢ^dau|²` (`prop:trace-ratio-observable`), `f(Q)` is the
    Sargent integral `∝ Q⁵`, and `μ₀` is the unit choice. -/
-- Ref: [leitner2026] §6/hadron-half-life
structure BetaRateData where
  /-- `|𝒲(q)|²`, the `T_{3,5}` weak-vertex form factor squared. -/
  W2 : ℝ
  W2_pos : 0 < W2
  /-- `μ₀`, the dimensional scale (a unit choice). -/
  mu0 : ℝ
  mu0_pos : 0 < mu0
  /-- `|ℳ_q|²`, the parent/daughter Markov-trace ratio. -/
  M2 : ℝ
  M2_pos : 0 < M2
  /-- `f(Q)`, the Sargent phase-space integral. -/
  fQ : ℝ
  fQ_pos : 0 < fQ

/-- `Γ_β = |𝒲(q)|² μ₀ /(2π³) · [2]_q · |ℳ_q|² · f(Q)`. -/
-- Ref: [leitner2026] §6/hadron-half-life
noncomputable def betaRate (d : BetaDecayData) (r : BetaRateData) : ℝ :=
  r.W2 * r.mu0 / (2 * Real.pi ^ 3) * d.q_integer_2 * r.M2 * r.fQ

/-- The rate is positive: every factor is. -/
-- Ref: [leitner2026] §6/hadron-half-life
theorem betaRate_pos (d : BetaDecayData) (r : BetaRateData) : 0 < betaRate d r := by
  unfold betaRate
  have h2 : 0 < d.q_integer_2 := by linarith [d.q_integer_2_gt_two]
  have hpi : 0 < 2 * Real.pi ^ 3 := by positivity
  exact mul_pos (mul_pos (mul_pos (div_pos (mul_pos r.W2_pos r.mu0_pos) hpi) h2) r.M2_pos) r.fQ_pos

/-- **`prop:hadron-half-life`**: `t_{1/2} = ln 2 / Γ_β`. (Until 2026-09-04 this
    name was an alias for `BetaDecayData.halfLife`, the `q`-shape alone.) -/
-- Ref: [leitner2026] §6/hadron-half-life
noncomputable def hadron_half_life (d : BetaDecayData) (r : BetaRateData) : ℝ :=
  Real.log 2 / betaRate d r

/-- The half-life is positive. -/
-- Ref: [leitner2026] §6/hadron-half-life
theorem hadron_half_life_pos (d : BetaDecayData) (r : BetaRateData) :
    0 < hadron_half_life d r :=
  div_pos (Real.log_pos (by norm_num : (1 : ℝ) < 2)) (betaRate_pos d r)

/-- **What the legacy carrier was.** `Γ_β = qPrefactor q` exactly when the four
    non-`q`-integer factors collapse onto the Sargent shape:
    `|𝒲|² μ₀/(2π³) · |ℳ_q|² · f(Q) = (q − q⁻¹)^5`. -/
-- Ref: [leitner2026] §6/hadron-half-life
theorem betaRate_eq_qPrefactor_iff (d : BetaDecayData) (r : BetaRateData) :
    betaRate d r = qPrefactor d.q ↔
      r.W2 * r.mu0 / (2 * Real.pi ^ 3) * r.M2 * r.fQ = (d.q - 1 / d.q) ^ 5 := by
  unfold betaRate qPrefactor BetaDecayData.q_integer_2
  have hq : 0 < d.q := by linarith [d.q_gt_one]
  have h2 : 0 < d.q + 1 / d.q := by positivity
  constructor
  · intro h
    have h' : (r.W2 * r.mu0 / (2 * Real.pi ^ 3) * r.M2 * r.fQ) * (d.q + 1 / d.q)
        = (d.q - 1 / d.q) ^ 5 * (d.q + 1 / d.q) := by linear_combination h
    exact mul_right_cancel₀ h2.ne' h'
  · intro h
    linear_combination (d.q + 1 / d.q) * h

/-- Under that collapse the two half-lives agree. -/
-- Ref: [leitner2026] §6/hadron-half-life
theorem hadron_half_life_eq_halfLife (d : BetaDecayData) (r : BetaRateData)
    (h : r.W2 * r.mu0 / (2 * Real.pi ^ 3) * r.M2 * r.fQ = (d.q - 1 / d.q) ^ 5) :
    hadron_half_life d r = d.halfLife := by
  unfold hadron_half_life BetaDecayData.halfLife
  rw [(betaRate_eq_qPrefactor_iff d r).2 h]

/-- The derivative of the `q`-shape `(q + q⁻¹)(q − q⁻¹)^5`, for `q ≠ 0`. -/
-- Ref: [leitner2026] §6/hadron-half-life
theorem hasDerivAt_qPrefactor {q : ℝ} (hq : q ≠ 0) :
    HasDerivAt qPrefactor
      ((1 - (q ^ 2)⁻¹) * (q - 1 / q) ^ 5
        + (q + 1 / q) * (5 * (q - 1 / q) ^ 4 * (1 + (q ^ 2)⁻¹))) q := by
  have hinv : HasDerivAt (fun y : ℝ => 1 / y) (-(q ^ 2)⁻¹) q := by
    simpa only [one_div] using hasDerivAt_inv hq
  have hu : HasDerivAt (fun y : ℝ => y + 1 / y) (1 + -(q ^ 2)⁻¹) q :=
    HasDerivAt.add (hasDerivAt_id' q) hinv
  have hw : HasDerivAt (fun y : ℝ => y - 1 / y) (1 - -(q ^ 2)⁻¹) q :=
    HasDerivAt.sub (hasDerivAt_id' q) hinv
  have hv : HasDerivAt (fun y : ℝ => (y - 1 / y) ^ 5)
      ((5 : ℕ) * (q - 1 / q) ^ (5 - 1) * (1 - -(q ^ 2)⁻¹)) q := hw.pow 5
  have hprod : HasDerivAt (fun y : ℝ => (y + 1 / y) * (y - 1 / y) ^ 5)
      ((1 + -(q ^ 2)⁻¹) * (q - 1 / q) ^ 5
        + (q + 1 / q) * ((5 : ℕ) * (q - 1 / q) ^ (5 - 1) * (1 - -(q ^ 2)⁻¹))) q :=
    hu.mul hv
  show HasDerivAt (fun y : ℝ => (y + 1 / y) * (y - 1 / y) ^ 5) _ q
  convert hprod using 1
  push_cast
  ring

/-- **The manuscript's sensitivity formula is the logarithmic derivative of the
    `q`-shape**: `∂ln Γ/∂ln q = q · Γ'/Γ` with `Γ = qPrefactor`. -/
-- Ref: [leitner2026] §6/hadron-half-life
theorem qSensitivity_eq_logDeriv {q : ℝ} (hq : 1 < q) :
    qSensitivity q
      = q * ((1 - (q ^ 2)⁻¹) * (q - 1 / q) ^ 5
              + (q + 1 / q) * (5 * (q - 1 / q) ^ 4 * (1 + (q ^ 2)⁻¹))) / qPrefactor q := by
  have hq0 : 0 < q := by linarith
  have hP : qPrefactor q ≠ 0 := (qPrefactor_pos hq).ne'
  have h1 : q ^ 2 - 1 ≠ 0 := by nlinarith
  have h2 : q ^ 2 + 1 ≠ 0 := by positivity
  rw [eq_div_iff hP]
  unfold qSensitivity qPrefactor
  field_simp

/-- The quoted `≈ 48`: at `q = 1.1097` the sensitivity lies in `(48, 49)`. -/
-- Ref: [leitner2026] §6/hadron-half-life
theorem qSensitivity_near_48 : 48 < qSensitivity 1.1097 ∧ qSensitivity 1.1097 < 49 := by
  unfold qSensitivity
  norm_num

end QOU.Archimedean
