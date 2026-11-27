import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith

/-!
# QOU.Nuclear.OhtsukiKappaSign — the Ohtsuki/Q_β sign obstruction over any ordered field

Bean `qou-gfsr` (item 5 of epic `qou-dk7p`). The algebraic half of
`OhtsukiKappaVsCkSign`. The first four Ohtsuki rungs of `4₁` are ring symbols in
`s` (standing for `√3`) and `p` (standing for `π`):

    κ₁ = 11 s p / 108,  κ₂ = 2 p² / 27,  κ₃ = 1081 s p³ / 21870,  κ₄ = 98 p⁴ / 729.

In any ordered field with `0 < s` and `0 < p` all four are positive, and the
sign obstruction (no real rescaling of the ladder variable carries a positive
even rung onto a negative Q_β coefficient) is order algebra. The `ℝ`
instantiation `s = √3`, `p = π` is
`QOU.Transcendental.Nuclear.OhtsukiKappaVsCkSign`.

No empirical value enters this file.
-/

namespace QOU.QBeta.OhtsukiKappaSign

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

def kappa1Sym (s p : K) : K := 11 * s * p / 108
def kappa2Sym (p : K) : K := 2 * p ^ 2 / 27
def kappa3Sym (s p : K) : K := 1081 * s * p ^ 3 / 21870
def kappa4Sym (p : K) : K := 98 * p ^ 4 / 729

variable {s p : K}

theorem kappa1Sym_pos (hs : 0 < s) (hp : 0 < p) : 0 < kappa1Sym s p := by
  unfold kappa1Sym; positivity
theorem kappa2Sym_pos (hp : 0 < p) : 0 < kappa2Sym p := by
  unfold kappa2Sym; positivity
theorem kappa3Sym_pos (hs : 0 < s) (hp : 0 < p) : 0 < kappa3Sym s p := by
  unfold kappa3Sym; positivity
theorem kappa4Sym_pos (hp : 0 < p) : 0 < kappa4Sym p := by
  unfold kappa4Sym; positivity

/-- **Even-rung positivity kills any rescaling.** `κ·λ² ≥ 0` for `κ > 0`, so it
never equals a negative coefficient `c`. -/
theorem even_rung_positive_ne_neg {κ c : K} (hκ : 0 < κ) (hc : c < 0) (lam : K) :
    κ * lam ^ 2 ≠ c := by
  have hnn : 0 ≤ κ * lam ^ 2 := by positivity
  intro h
  rw [h] at hnn
  linarith

/-- **No rescaling aligns the tower with the ladder.** -/
theorem no_real_rescaling_aligns
    {κ₁' κ₂' c₂ c₃ : K} (hκ₂ : 0 < κ₂') (hc₃ : c₃ < 0) :
    ¬ ∃ lam : K, κ₁' * lam = c₂ ∧ κ₂' * lam ^ 2 = c₃ := by
  rintro ⟨lam, _h1, h2⟩
  exact even_rung_positive_ne_neg hκ₂ hc₃ lam h2

/-- **Any negative coefficient differs from every positive rung.** -/
theorem neg_ck_ne_kappaSym {c : K} (hc : c < 0) (hs : 0 < s) (hp : 0 < p) :
    c ≠ kappa1Sym s p ∧ c ≠ kappa2Sym p ∧ c ≠ kappa3Sym s p ∧ c ≠ kappa4Sym p :=
  ⟨by linarith [kappa1Sym_pos hs hp], by linarith [kappa2Sym_pos hp (K := K)],
   by linarith [kappa3Sym_pos hs hp], by linarith [kappa4Sym_pos hp (K := K)]⟩

end QOU.QBeta.OhtsukiKappaSign
