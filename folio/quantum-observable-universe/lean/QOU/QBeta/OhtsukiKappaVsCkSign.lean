import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds
import Mathlib.Tactic

/-!
# The Ohtsuki κ-tower cannot be the Q_β `c_k` ladder — the sign invariant

The "prize" question of the S-channel saddle-point tranche: is the Q_β truncation
ladder `c_k` the figure-eight (4₁) Chern–Simons perturbative (Ohtsuki) series
`κ_n`? The probe
`computations/qbeta/qbeta_ohtsuki_kappa_vs_ck_direct_comparison.py` answers **no**,
with four independent obstructions. This file formalizes the crispest of them —
the **sign / even-rung positivity invariant** — sorry-free.

**The invariant.** The DERIVED Ohtsuki coefficients of 4₁ are all **positive**
closed forms (from the Kashaev sum `log J_N`, PSLQ-exact, corpus #3606/#3628):

  κ₁ = 11√3π/108,  κ₂ = 2π²/27,  κ₃ = 1081√3π³/21870,  κ₄ = 98π⁴/729  (all > 0).

The Q_β ladder coefficients are **negative**: `c₂ = −1` (Lean-proved Taylor-exact)
and the q₀-extract `c₃ ≈ −2.07 < 0`. A positive number is never a negative number,
so `c_k ≠ κ_n` for every pair — no rescaling of the ladder variable `u` can align
them either, because the obstruction is the even-power sign, not a magnitude.

**Why this is not superficial.** The natural "defence" of an identification is a
reparametrization `u ↦ λ·u` of the ladder variable. `even_rung_positive_ne_neg`
shows a single **even** rung already blocks it: `κ₂·λ² ≥ 0` (κ₂ > 0, λ² ≥ 0) can
**never** equal `c₃ < 0`, for ANY real λ. So no real rescaling maps the
all-positive κ-tower onto the negative `c_k` pair (`no_real_rescaling_aligns`).
This is the Lean root of obstruction (B1)/(B2) of the probe's honest negative.

This is a genuine scope-(a)/(b) exclusion **of the raw identification**, NOT a
claim that the deeper 4₁-resurgence ↔ Q_β-action bridge is closed: that bridge
remains the standing open keystone (corpus `2026-07-12-ohtsuki-higher-rungs-exact.md`,
`2026-07-18-phib-a1-mis-identified-not-ohtsuki-kappa1.md`). The κ_n are topological
invariants of the figure-eight; the c_k are the Q_β observable ladder. **No `c_k`
is wired; no channel instance is fabricated; `u(q₀)` stays OPEN.**

Base ring is `ℝ` (archimedean §7c: `Real.sqrt`, `Real.pi`, ordering).

-- Ref: [leitner2026] docs/audits/2026-08-01-schannel-saddle-point-ohtsuki-vs-ck.md
-- Ref: [andersen-hansen2006] https://doi.org/10.1142/S0218216506004555 (κ-tower)
-- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-/

namespace QOU.QBeta.OhtsukiKappaVsCkSign

open Real

/-! ## The DERIVED Ohtsuki closed forms are positive -/

/-- Ohtsuki `κ₁ = 11√3π/108` (odd rung, ℚ(√3)·π). Derived from the 4₁ Kashaev
    sum; here as a closed real number. -/
noncomputable def kappa1 : ℝ := 11 * Real.sqrt 3 * Real.pi / 108

/-- Ohtsuki `κ₂ = 2π²/27` (even rung, ℚ·π²). -/
noncomputable def kappa2 : ℝ := 2 * Real.pi ^ 2 / 27

/-- Ohtsuki `κ₃ = 1081√3π³/21870` (odd rung). -/
noncomputable def kappa3 : ℝ := 1081 * Real.sqrt 3 * Real.pi ^ 3 / 21870

/-- Ohtsuki `κ₄ = 98π⁴/729` (even rung). -/
noncomputable def kappa4 : ℝ := 98 * Real.pi ^ 4 / 729

theorem kappa1_pos : 0 < kappa1 := by
  unfold kappa1; positivity

theorem kappa2_pos : 0 < kappa2 := by
  unfold kappa2; positivity

theorem kappa3_pos : 0 < kappa3 := by
  unfold kappa3; positivity

theorem kappa4_pos : 0 < kappa4 := by
  unfold kappa4; positivity

/-! ## The sign obstruction -/

/-- **Even-rung positivity kills any real rescaling (the core invariant).** A
    positive even Ohtsuki rung `κ` scaled by ANY real `λ` gives `κ·λ² ≥ 0`, so it
    can never equal a negative Q_β coefficient `c < 0`. This is *why* no
    reparametrization `u ↦ λ·u` of the ladder variable can turn the all-positive
    κ-tower into the negative `c_k` — the even-power sign is reparametrization-
    invariant. -/
theorem even_rung_positive_ne_neg {κ c : ℝ} (hκ : 0 < κ) (hc : c < 0) (lam : ℝ) :
    κ * lam ^ 2 ≠ c := by
  have hnn : 0 ≤ κ * lam ^ 2 := by positivity
  intro h
  rw [h] at hnn
  linarith

/-- **No real rescaling aligns the tower with the ladder.** There is no real `λ`
    simultaneously matching an odd rung to `c₂ < 0` and the next even rung to
    `c₃ < 0`: the even constraint `κ₂·λ² = c₃` alone is impossible for `κ₂ > 0`,
    `c₃ < 0`. (The first component is stated for faithfulness to the index-shifted
    pairing κ₁↔c₂, κ₂↔c₃; the contradiction comes from the second.) -/
theorem no_real_rescaling_aligns
    {κ₁' κ₂' c₂ c₃ : ℝ} (hκ₂ : 0 < κ₂') (hc₃ : c₃ < 0) :
    ¬ ∃ lam : ℝ, κ₁' * lam = c₂ ∧ κ₂' * lam ^ 2 = c₃ := by
  rintro ⟨lam, _h1, h2⟩
  exact even_rung_positive_ne_neg hκ₂ hc₃ lam h2

/-- **Concrete: `c₂ = −1 ≠ κ₁` (sign).** The Lean-proved Q_β Taylor coefficient
    `c₂ = −1` is negative; the derived Ohtsuki `κ₁ = 11√3π/108` is positive; they
    are unequal. -/
theorem c2_ne_kappa1 : (-1 : ℝ) ≠ kappa1 := by
  have := kappa1_pos
  linarith

/-- **Concrete: any negative `c_k` differs from every κ_n.** For a negative Q_β
    coefficient `c < 0` and any of the four derived (positive) Ohtsuki rungs, the
    two are unequal — the universal sign obstruction of the honest negative. -/
theorem neg_ck_ne_kappa {c : ℝ} (hc : c < 0) :
    c ≠ kappa1 ∧ c ≠ kappa2 ∧ c ≠ kappa3 ∧ c ≠ kappa4 :=
  ⟨by linarith [kappa1_pos], by linarith [kappa2_pos],
   by linarith [kappa3_pos], by linarith [kappa4_pos]⟩

end QOU.QBeta.OhtsukiKappaVsCkSign
