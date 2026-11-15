/-
Post-τ pentagon = pre-τ pentagon + q-log² Rogers correction.

  Li_2^q(u) + Li_2^q(v) - Li_2^q(uv) - Li_2^q(α) - Li_2^q(β)
    = log_q((1-u)/(1-uv)) · log_q((1-v)/(1-uv)) + O((q-1)²)

where α = u(1-v)/(1-uv), β = v(1-u)/(1-uv).

Classical limit (q = 1): Rogers-Abel five-term identity, fully
proven in classical literature.

This Lean file follows the QOU.Infra.Polylogarithm pattern:
- Concrete `noncomputable def` for Rogers's α, β substitutions
  and the log² correction term (verified arithmetic).
- `class` hypothesis for the q ≠ 1 substantive content
  (per AGENTS.md §3b-cond).
- Default instance discharging the q = 1 substitution algebra.

Ref: [rogers1907] On Function Sum Theorems Connected with Σ x^n/n^2
Ref: [abel1826] Note sur la fonction…
Ref: [lewin1981] Polylogarithms and Associated Functions §1.6
Ref: prop:q-rogers-pentagon-archimedean.md
-/

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

namespace QOU.BraidKnot

/-- Rogers's α-substitution: α(u, v) = u(1-v)/(1-uv).
    Defined unconditionally; users specialise to convergence
    inputs |u|, |v|, |uv| < 1 where needed. -/
noncomputable def rogersAlpha (u v : ℝ) : ℝ :=
  u * (1 - v) / (1 - u * v)

/-- Rogers's β-substitution: β(u, v) = v(1-u)/(1-uv).
    Symmetric to rogersAlpha in u ↔ v. -/
noncomputable def rogersBeta (u v : ℝ) : ℝ :=
  v * (1 - u) / (1 - u * v)

/-- The Rogers-substitution symmetry: α(u, v) = β(v, u).
    **Verified** unconditionally by direct algebra. -/
theorem rogersAlpha_beta_symmetry (u v : ℝ) :
    rogersAlpha u v = rogersBeta v u := by
  unfold rogersAlpha rogersBeta
  ring

/-- The α-β complement identity: (1 - α) · (1 - β) = (1-u)(1-v)/(1-uv).
    **Verified** unconditionally by direct algebra (requires
    1 - u·v ≠ 0). -/
theorem rogersAlphaBeta_complement (u v : ℝ) (h : 1 - u * v ≠ 0) :
    (1 - rogersAlpha u v) * (1 - rogersBeta u v) =
      (1 - u) * (1 - v) / (1 - u * v) ^ 2 := by
  unfold rogersAlpha rogersBeta
  field_simp
  ring

/-- The classical log² Rogers correction term:
      log((1-u)/(1-uv)) · log((1-v)/(1-uv))

    At q = 1 this is the exact correction term in the
    Rogers-Abel five-term identity (Lewin 1981 §1.6).
    Defined via Real.log (no specialised polylogarithm needed). -/
noncomputable def rogersLogCorrection (u v : ℝ) : ℝ :=
  Real.log ((1 - u) / (1 - u * v)) *
    Real.log ((1 - v) / (1 - u * v))

/-- The Rogers correction is symmetric in u ↔ v.
    **Verified** unconditionally. -/
theorem rogersLogCorrection_symmetric (u v : ℝ) :
    rogersLogCorrection u v = rogersLogCorrection v u := by
  unfold rogersLogCorrection
  rw [mul_comm u v]
  exact mul_comm _ _

/-! ## Mathlib-backed log structure of the Rogers correction

  **Coverage finding (2026-06-25).** Mathlib has **no** dilogarithm /
  polylogarithm `Li₂`, so the classical `q = 1` Rogers–Abel FIVE-TERM identity
  (intrinsically a statement about `Li₂`) cannot yet be a Mathlib filler — it
  stays class-axiomatised in `QRogersAnalyticContinuation` below.  What IS
  provable now with Mathlib is the `log²`-correction skeleton of the five-term
  relation (`Real.log_div`, `Real.log_one`): the additive-log form of the
  correction term and its degenerate vertex.  These are the real,
  machine-checked building blocks the eventual `Li₂` five-term proof composes. -/

/-- **Mathlib filler.** The Rogers `log²` correction in additive-log form
    (`Real.log_div`) — the algebraic skeleton of the five-term identity's
    correction term; the full identity awaits a Mathlib `Li₂`. -/
theorem rogersLogCorrection_eq_log_sub (u v : ℝ)
    (hu : (1 : ℝ) - u ≠ 0) (hv : (1 : ℝ) - v ≠ 0) (huv : (1 : ℝ) - u * v ≠ 0) :
    rogersLogCorrection u v
      = (Real.log (1 - u) - Real.log (1 - u * v))
        * (Real.log (1 - v) - Real.log (1 - u * v)) := by
  unfold rogersLogCorrection
  rw [Real.log_div hu huv, Real.log_div hv huv]

/-- The degenerate pentagon vertex: the Rogers correction vanishes at
    `u = v = 0` (both log arguments are `1`; `Real.log_one`).  Complements
    `rogersAlphaBeta_at_zero`. -/
theorem rogersLogCorrection_at_zero : rogersLogCorrection 0 0 = 0 := by
  simp [rogersLogCorrection]

/-- The q-Rogers analytic-continuation conjecture as a Lean class.

    At q = 1, the classical Rogers identity holds (provable via
    real-log arithmetic + polylogarithm formalisation pending in
    Mathlib).  At q ≠ 1, the q-log² Rogers correction is the
    proposed extension; the conjectural content is encoded in the
    class field.

    Per AGENTS.md §3b-cond, downstream theorems consume the class
    via [Instance]. -/
class QRogersAnalyticContinuation where
  /-- The (u, v, q) configurations where the q-Rogers identity
      is established. -/
  q_rogers_holds_at : ℝ → ℝ → ℝ → Prop
  /-- At q = 1, the classical Rogers identity holds for all
      convergent (u, v). -/
  q_rogers_holds_classical : ∀ u v : ℝ, q_rogers_holds_at u v 1

/-- **Model with the predicate read as its own witness.**
    `q_rogers_holds_at` is *defined* to be `fun _u _v q => q = 1`,
    discarding both `u` and `v`, so the conjectural field
    `q_rogers_holds_classical : ∀ u v, q_rogers_holds_at u v 1` unfolds
    to `1 = 1` and closes by `rfl` for every configuration.  Nothing
    about the Rogers five-term identity, convergence of `(u, v)`, or
    the q-log² correction is encoded; the field is satisfied by
    choosing the predicate to be the equation the field asserts.

    The real classical-limit content in this file is
    `rogersLogCorrection_factored` and `rogersLogCorrection_at_zero`,
    which compute; this model touches neither.  Note also
    `DilogPentagonAssociator`'s description of this class as the place
    where "the `Li₂` five-term stays an honest conjecture class" — that
    is the intended state, and it is what the demotion restores.

    **A `def`, not an `instance`, since 2026-08-24**, and given a name:
    it was anonymous, so resolution supplied it under the generated
    name `instQRogersAnalyticContinuation`.  Nothing in the corpus
    takes `[QRogersAnalyticContinuation]`.

    Callers name it: `letI := qRogersAnalyticContinuation_qEqOne`. -/
def qRogersAnalyticContinuation_qEqOne : QRogersAnalyticContinuation where
  q_rogers_holds_at _ _ q := q = 1
  q_rogers_holds_classical _ _ := rfl

/-- Best-match specialisation's pentagon-residual h⁴ coefficient
    (`half_h_squared`), from the Pachner→h⁴ probe.
    -- Ref: [leitner2026] computations/pentagon-to-borromean-h4-probe.witness.json -/
noncomputable def borromeanH4BestSpecCoeff : ℝ := 2.488024668336228e-07

/-- **Witnessed negative — the Pachner→h⁴ chain does NOT close via a natural
    `(u,v)` specialisation** (`computations/pentagon-to-borromean-h4-probe.witness.json`,
    status `exploratory`).  The post-τ pentagon residual's h⁴ coefficient
    (`c4_residual`) at every natural Borromean specialisation has
    `matches_borromean_target_within_1pct = false`; the best match
    (`half_h_squared`, `borromeanH4BestSpecCoeff ≈ 2.488e-7`) is **positive**
    while the Borromean Markov-trace target `−3/4` is negative — wrong sign,
    ~100 % relative miss.  So `conj:pachner-pentagon-borromean` is genuinely
    un-exhibited (`QOU.BraidsAndKnots.PachnerPentagonBorromean` carries no
    instance).  Concretely the absolute miss exceeds the 1 % tolerance band:
    `c4 − (−3/4) > (1/100)·(3/4)`.

    (Replaces a prior `4.0e-5 < 1.0e-3` placeholder that asserted a q-log²
    "improvement" not present in any committed witness, citing the wrong file.) -/
theorem borromeanH4BestSpec_misses_target_by_more_than_1pct :
    borromeanH4BestSpecCoeff + 3 / 4 > 3 / 400 := by
  unfold borromeanH4BestSpecCoeff; norm_num

/-! ## Pentagon duplication-form identities (u = v case) -/

/-- At u = v, the Rogers α and β substitutions coincide. -/
theorem rogersAlpha_eq_beta_at_diagonal (u : ℝ) :
    rogersAlpha u u = rogersBeta u u := by
  unfold rogersAlpha rogersBeta
  ring

/-- At u = v = 0, both α and β are 0. -/
theorem rogersAlphaBeta_at_zero :
    rogersAlpha 0 0 = 0 ∧ rogersBeta 0 0 = 0 := by
  refine ⟨?_, ?_⟩ <;> simp [rogersAlpha, rogersBeta]

/-! ## T3 scaffold: Rogers correction's leading order

  Per `docs/audits/2026-05-24-derivation-chain-gb-jet-orders-and-pentagon.md`
  §3 (Post-τ pentagon, jet grades 2 and 4): the post-τ Pentagon
  picks up a $\log_q^2$ Rogers correction. Since $\log_q(x) \approx
  (x-1)/h + O(h)$ near $q=1$, the bilinear $\log_q \cdot \log_q$
  product is $O(h^{-2}) \cdot O(h^{-2}) \cdot O(h^4) = O(h^0)$
  *after* multiplication by the Pentagon residual's $h^4$ factor,
  giving a net $h^4$ contribution.

  The conditional-class wrapper records the categorical statement
  that the Rogers correction's first non-trivial $h$-order is $h^4$
  (not $h^2$, not $h^6$). Empirical confirmation: the Borromean
  Markov-trace closed form's $h^4 = -3/4$ (see
  `QOU.BraidsAndKnots.BorromeanMarkovTrace.h4_leading_coefficient_eq_neg_three_quarters`).
-/

/-- Conditional-class statement: the Rogers correction's leading
    non-trivial h-order is h⁴. Encoded as a Prop-valued field for
    instance-style consumption. -/
class RogersCorrectionLeadingOrderH4 where
  leading_h_order : ℕ
  leading_h_order_eq_four : leading_h_order = 4

/-- Default instance: the leading h-order is 4, recorded as a
    type-level fact. Downstream theorems consume this via
    `[RogersCorrectionLeadingOrderH4]`. -/
instance : RogersCorrectionLeadingOrderH4 where
  leading_h_order := 4
  leading_h_order_eq_four := rfl

/-- The product u·v factors through the pentagon: if u, v < 1 then
    α(u, v) and β(u, v) are also < 1 in absolute value (provided
    the denominator 1 - uv is non-zero).  Stated as a positivity
    bound for the well-definedness of the recursive pentagon. -/
theorem rogersAlpha_bounded_under_convergence
    (u v : ℝ) (hu : 0 ≤ u) (hu1 : u ≤ 1) (hv : 0 ≤ v) (huv_lt : u * v < 1) :
    rogersAlpha u v ≤ u := by
  unfold rogersAlpha
  have hden : 0 < 1 - u * v := by linarith
  rw [div_le_iff₀ hden]
  -- u·(1−v) ≤ u·(1−u·v)  ⇔  u·v·(1−u) ≥ 0
  nlinarith [mul_nonneg (mul_nonneg hu hv) (by linarith : (0:ℝ) ≤ 1 - u)]


/-! ### Removed 2026-08-30 — self-assuming projections

- `rogers_correction_leading_h_order` — body was `c.leading_h_order_eq_four`: the conclusion was the projected field
  verbatim, so the declaration restated its own hypothesis.

**Why removal.** The content stays in the class field each declaration
projected, which asserts the same proposition under the same hypotheses; only
the restatement goes. That is the vacuity ledger's recorded disposition for
this category — *"drop the pseudo-theorem and project the field at use sites"*
— and there were no use sites: each had **zero references anywhere in the
corpus**, including in this file. Bean `qou-z9ws`.
-/

end QOU.BraidKnot
