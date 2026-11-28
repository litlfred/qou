import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

/-!
# What Bring's complex structure does to the orientation of `Gm`

Bean `qou-h0zz` (coordinator request, 2026-11-28). The formal-groups thread (stacked on PR
#9935) shows that the Hodge star `S ↦ Sᶜ` sends weight `k` to `5 − k`, the formal inverse of
`Gm`, and negates every charge; so the chirality sign is an orientation of `Gm`, `q` against
`q⁻¹`. `prop:hypercharge-sign-is-bring-orientation` puts the same sign on the orientation of
Bring's surface, whose reversal is complex conjugation `c`.

The question is whether `c` acts on `Gm` as the inversion `q ↦ q⁻¹`.

## Results

1. `conj_eq_inv_of_normSq_one`: on the unit circle, `conj q = q⁻¹`. There conjugation **is**
   the inversion, so Bring's complex structure and the `Gm` orientation are the same bit.
2. `conj_real` and `real_ne_inv`: at a real point `q > 1`, `conj q = q` while `q ≠ q⁻¹`.
   There conjugation fixes `q` and does not reverse `Gm`.

## Reading

At the real anchor `q₀ > 1`, complex conjugation fixes `q₀`. So Bring's complex structure
cannot select between `q₀` and `q₀⁻¹`. This matches
`prop:braid-chirality-blind-to-hypercharge-sign` from the `Gm` side. On the unit circle, roots
of unity included, conjugation and inversion coincide, so the two orientations are tied there.
Whether the sign is fixed therefore depends on which locus of `Gm` the chirality is read on.
That is a question for the model, not settled here.

Algebra over `ℂ` only. No empirical value enters.
-/

namespace QOU.StandardModel.BringConjGm

open Complex

theorem conj_eq_inv_of_normSq_one (q : ℂ) (h : normSq q = 1) : (starRingEnd ℂ) q = q⁻¹ := by
  rw [inv_def, h]; simp

theorem conj_real (q : ℝ) : (starRingEnd ℂ) (q : ℂ) = q := conj_ofReal q

theorem real_ne_inv (q : ℝ) (hq : 1 < q) : (q : ℂ) ≠ (q : ℂ)⁻¹ := by
  intro h
  have h' : q = q⁻¹ := by exact_mod_cast h
  have hq0 : q ≠ 0 := ne_of_gt (by linarith)
  have h1 : q * q = 1 := by
    calc q * q = q * q⁻¹ := by rw [← h']
      _ = 1 := mul_inv_cancel₀ hq0
  nlinarith

/-- At a real point `q > 1` conjugation fixes `q` but inversion moves it. -/
theorem conj_not_inversion_at_real (q : ℝ) (hq : 1 < q) :
    (starRingEnd ℂ) (q : ℂ) ≠ (q : ℂ)⁻¹ := by
  rw [conj_real]; exact real_ne_inv q hq

end QOU.StandardModel.BringConjGm
