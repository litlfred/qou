import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Order.Monotone.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# QOU.Substrate.MuOverDetermination

Lean formalisation of the substrate over-determination finding:
the canonical q₀ (anchored from m_p via PR #1422) and the
"μ-anchored q₀" (the value that would make m_μ_pred = m_μ_CODATA
exactly) are GENERICALLY DIFFERENT. Therefore m_p and m_μ cannot
simultaneously match CODATA at sub-ppb precision via this two-
calibration substrate.

This is the Lean-level structure behind PR #1581's Probe A:
the 211 ppb m_μ residual IS the propagated q₀ shift, NOT a
missing categorical correction.

## What's PROVED (sorry-free)

The muon-mass-ratio formula
   ratio(q) := Vol(4_1) / (1 - 1/q)²
is STRICTLY MONOTONIC on q > 1, hence INJECTIVE.

Therefore for distinct positive constants `m_μ_target_a` and
`m_μ_target_b` (e.g. one from m_p anchor, one from CODATA m_μ),
the unique inverses `q_a := ratio⁻¹(m_μ_target_a / m_e)` and
`q_b := ratio⁻¹(m_μ_target_b / m_e)` are also distinct.

## Why this matters for 1ppb

The L2 dashboard reports m_μ at 210 ppb miss. PR #1581 Probe A
showed numerically that this 211 ppb EQUALS the propagated Δq₀
shift via ∂ ln(m_μ)/∂q = -2/(ℏ_q·q²). This Lean theorem encodes
the STRUCTURE behind that numerical fact: the substrate is
over-determined when one fixes q₀ from a single physical mass.

## Cross-references

- PR #1581 Probe A (`mu_substrate_tension_audit_100dps.py`)
- PR #1422 (q_0 re-pin from m_p)
- `figure-8-muon-mass-cross-check.lean` (the muon Vol-form identity)
-/

namespace QOU
namespace Substrate
namespace MuOverDetermination

/-- The q-deformed Planck constant ℏ_q := 1 - 1/q. -/
def hbarQ (q : ℝ) : ℝ := 1 - 1 / q

/-- ℏ_q² for convenience. -/
def hbarQSq (q : ℝ) : ℝ := (hbarQ q) ^ 2

/-- The muon mass-ratio function:
    `muRatio q = vol_4_1 / ℏ_q²`.

    For `q ∈ (1, ∞)`, ℏ_q ∈ (0, 1), hence ℏ_q² ∈ (0, 1) and
    muRatio is strictly decreasing in ℏ_q (i.e. strictly
    monotonic in q in a specific direction). -/
def muRatio (vol_4_1 : ℝ) (q : ℝ) : ℝ := vol_4_1 / hbarQSq q

/-- `ℏ_q = 1 - 1/q` is strictly positive for `q > 1`. -/
theorem hbarQ_pos (q : ℝ) (hq : 1 < q) : 0 < hbarQ q := by
  unfold hbarQ
  have hq_pos : 0 < q := lt_trans zero_lt_one hq
  have h_inv : 1 / q < 1 := by
    rw [div_lt_one hq_pos]
    exact hq
  linarith

/-- `ℏ_q² > 0` for `q > 1`. -/
theorem hbarQSq_pos (q : ℝ) (hq : 1 < q) : 0 < hbarQSq q := by
  unfold hbarQSq
  exact pow_pos (hbarQ_pos q hq) 2

/-- **Strict monotonicity of `hbarQ` on q > 1.**

    For `1 < q₁ < q₂`, `hbarQ q₁ < hbarQ q₂` (ℏ_q is strictly
    increasing in q since 1 - 1/q is increasing). -/
theorem hbarQ_strictMono (q₁ q₂ : ℝ) (hq₁ : 1 < q₁) (hq : q₁ < q₂) :
    hbarQ q₁ < hbarQ q₂ := by
  unfold hbarQ
  have hq₁_pos : 0 < q₁ := lt_trans zero_lt_one hq₁
  have hq₂_pos : 0 < q₂ := lt_trans hq₁_pos hq
  -- 1/q₂ < 1/q₁ since q₁ < q₂ and both positive
  have h_inv_lt : 1 / q₂ < 1 / q₁ := by
    apply one_div_lt_one_div_of_lt hq₁_pos hq
  linarith

/-- **Strict monotonicity of `muRatio` on q > 1** (for positive vol_4_1).

    Since `hbarQ` is strictly increasing on q > 1 and both
    `hbarQ q₁, hbarQ q₂ > 0`, `hbarQSq` is also strictly
    increasing — therefore `muRatio = vol / hbarQSq` is strictly
    DECREASING in q.

    The key categorical content: muRatio is INJECTIVE on q > 1. -/
theorem muRatio_strictMono_anti (vol_4_1 : ℝ) (hvol : 0 < vol_4_1)
    (q₁ q₂ : ℝ) (hq₁ : 1 < q₁) (hq : q₁ < q₂) :
    muRatio vol_4_1 q₂ < muRatio vol_4_1 q₁ := by
  unfold muRatio
  have hq₁_pos : 0 < q₁ := lt_trans zero_lt_one hq₁
  have hq₂_pos : 0 < q₂ := lt_trans hq₁_pos hq
  have h₁_sq_pos : 0 < hbarQSq q₁ := hbarQSq_pos q₁ hq₁
  have h₂_sq_pos : 0 < hbarQSq q₂ := hbarQSq_pos q₂ (lt_trans hq₁ hq)
  -- hbarQ q₁ < hbarQ q₂, both positive
  have h_hbar_lt : hbarQ q₁ < hbarQ q₂ := hbarQ_strictMono q₁ q₂ hq₁ hq
  have h₁_pos : 0 < hbarQ q₁ := hbarQ_pos q₁ hq₁
  have h₂_pos : 0 < hbarQ q₂ := hbarQ_pos q₂ (lt_trans hq₁ hq)
  -- squaring preserves order on positives
  have h_sq_lt : hbarQSq q₁ < hbarQSq q₂ := by
    unfold hbarQSq
    exact sq_lt_sq' (by linarith) h_hbar_lt
  exact div_lt_div_of_pos_left hvol h₁_sq_pos h_sq_lt

/-- **Injectivity of `muRatio` on q > 1.**

    Two distinct q values strictly greater than 1 give distinct
    muRatio values. This is the precise structural fact behind
    the over-determination finding: if `muRatio` were the unique
    function determining q from the muon ratio, then choosing q
    to match a DIFFERENT physical mass (m_p) would generically
    give a DIFFERENT q than the muon-matching one. -/
theorem muRatio_injective_on_q_gt_one (vol_4_1 : ℝ) (hvol : 0 < vol_4_1)
    (q₁ q₂ : ℝ) (hq₁ : 1 < q₁) (hq₂ : 1 < q₂)
    (h_eq : muRatio vol_4_1 q₁ = muRatio vol_4_1 q₂) :
    q₁ = q₂ := by
  rcases lt_trichotomy q₁ q₂ with hlt | heq | hgt
  · -- q₁ < q₂ contradicts muRatio q₂ < muRatio q₁
    exfalso
    have := muRatio_strictMono_anti vol_4_1 hvol q₁ q₂ hq₁ hlt
    linarith
  · exact heq
  · -- q₁ > q₂ contradicts muRatio q₁ < muRatio q₂
    exfalso
    have := muRatio_strictMono_anti vol_4_1 hvol q₂ q₁ hq₂ hgt
    linarith

/-- **Substrate over-determination corollary**.

    For two distinct target mass ratios `ratio_a ≠ ratio_b`
    (e.g. one from inverting the m_p anchor, one from the
    CODATA m_μ target), the unique q values that make
    `muRatio vol_4_1 q = ratio_*` for each are DIFFERENT.

    Contrapositive: q_a = q_b ⇒ ratio_a = ratio_b. This is the
    *negation* of "one q anchor matches both physical masses." -/
theorem substrate_over_determination
    (vol_4_1 : ℝ) (hvol : 0 < vol_4_1)
    (q_a q_b ratio_a ratio_b : ℝ)
    (hq_a : 1 < q_a) (hq_b : 1 < q_b)
    (h_a : muRatio vol_4_1 q_a = ratio_a)
    (h_b : muRatio vol_4_1 q_b = ratio_b)
    (h_eq : q_a = q_b) :
    ratio_a = ratio_b := by
  rw [← h_a, ← h_b, h_eq]

/-! ## What this Lean module does NOT do

- Does NOT prove the m_μ residual EQUALS the propagated Δq₀ shift
  exactly — that requires real-derivative analysis (Mean Value
  Theorem on Mathlib's `deriv`), which is heavier setup. The
  numerical fact is verified in Probe A (`mu_substrate_tension_audit_100dps.py`)
  at 100 dps with 12-significant-figure match.

- Does NOT prove the framework's choice of q₀ anchor. The class
  `ReadingAValidAtH2` pattern (AGENTS.md §3b-cond) is the right
  way to formalise such structural choices; this module only
  proves the INJECTIVITY structure that makes the choice
  consequential.

- Does NOT provide a Lean-side dashboard wiring (the dashboard
  lives in `per_observable_100x_status.py`).
-/

end MuOverDetermination
end Substrate
end QOU
