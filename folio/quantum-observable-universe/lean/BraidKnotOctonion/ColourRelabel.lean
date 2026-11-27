import BraidKnotOctonion.JimboGl3Singlet
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Algebra.Module.Pi

/-!
# Relabelling colours does not preserve Jimbo's singlet at `q² ≠ 1`

The colour tube over a point `z` of Bring's surface has three sheets `r, g, b`
(`color-tube-fibers`), and under the working assumption of issue #9106 these are the three
colour states of a strand. Jimbo's braiding `Ř` on `K³` uses an *ordering* of the basis: the
`(q − q⁻¹)` term sits on the pairs `b < a`. Monodromy of the colour tube permutes the sheets.

This file shows that the ordering is real structure at generic `q`: swapping the first two
colours sends `ε_q` to a tensor that is a multiple of `ε_q` only if `q² = 1`
(`swap01_eps_proportional_iff`). So the identification of sheets with an ordered basis of
`K³` is a choice made on a patch of the tube, not something monodromy preserves. The
relabelled tensor is still the singlet of the relabelled braiding (by conjugation), so trace
values do not depend on the choice.
-/

namespace QOU.Braiding.ColourRelabel

open QOU.Braiding.JimboGl3Singlet

variable {K : Type*} [Field K]

/-- Swap colours `0` and `1`. -/
def sw : Fin 3 → Fin 3 := fun x => if x = 0 then 1 else if x = 1 then 0 else x

/-- Relabel a three-fold colour tensor by the swap. -/
def swapT (w : T3 K) : T3 K := fun a b c => w (sw a) (sw b) (sw c)

/-- The relabelled singlet is a multiple of `ε_q` only when `q² = 1`. -/
theorem swap01_eps_proportional (q : K) (hq : q ≠ 0) (c : K)
    (H : swapT (eps q) = fun a b d => c * eps q a b d) : q ^ 2 = 1 := by
  have h1 : eps q 1 0 2 = c * eps q 0 1 2 := congrFun (congrFun (congrFun H 0) 1) 2
  have h2 : eps q 0 1 2 = c * eps q 1 0 2 := congrFun (congrFun (congrFun H 1) 0) 2
  have e012 : eps q 0 1 2 = 1 := by simp [eps]
  have e102 : eps q 1 0 2 = -q⁻¹ := by simp [eps]
  rw [e012, e102] at h1 h2
  have hc : c = -q⁻¹ := by rw [h1]; ring
  rw [hc] at h2
  have : q ^ 2 * (q⁻¹ * q⁻¹) = 1 := by field_simp
  linear_combination (q ^ 2) * h2 + this

/-- Conversely at `q² = 1` it is the multiple `−q⁻¹` (the classical sign). -/
theorem swap01_eps_of_sq_eq_one (q : K) (h : q ^ 2 = 1) :
    swapT (eps q) = fun a b d => -q⁻¹ * eps q a b d := by
  have hi2 : q⁻¹ ^ 2 = 1 := by rw [inv_pow, h, inv_one]
  have hi3 : q⁻¹ ^ 3 = q⁻¹ := by rw [pow_succ, hi2, one_mul]
  funext a b d
  fin_cases a <;> fin_cases b <;> fin_cases d <;>
    simp [swapT, sw, eps, hi2, hi3] <;> linear_combination (-1 : K) * hi2

/-- Both directions together. -/
theorem swap01_eps_proportional_iff (q : K) (hq : q ≠ 0) :
    (∃ c : K, swapT (eps q) = fun a b d => c * eps q a b d) ↔ q ^ 2 = 1 :=
  ⟨fun ⟨c, H⟩ => swap01_eps_proportional q hq c H,
   fun h => ⟨-q⁻¹, swap01_eps_of_sq_eq_one q h⟩⟩

/-- **Any linear map compatible with the braiding keeps the singlet line.** If
`Φ : V^{⊗3} → V^{⊗3}` is `K`-linear and commutes with both Jimbo braidings, then `Φ ε_q` is a
multiple of `ε_q` (for `q ≠ 0`, `q² + 1 ≠ 0`). No ordering of the colours is used: this is the
form in which a monodromy that respects the braided structure must act on the singlet. -/
theorem braid_commuting_fixes_singlet (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (Φ : T3 K →ₗ[K] T3 K)
    (h12 : ∀ w, R12 q (Φ w) = Φ (R12 q w)) (h23 : ∀ w, R23 q (Φ w) = Φ (R23 q w)) :
    Φ (eps q) = fun a b c => Φ (eps q) 0 1 2 * eps q a b c := by
  have hs12 : R12 q (eps q) = (-q⁻¹) • eps q := by
    rw [R12_eps q hq]; funext a b c; simp
  have hs23 : R23 q (eps q) = (-q⁻¹) • eps q := by
    rw [R23_eps q hq]; funext a b c; simp
  apply singlet_unique q hq h2
  · rw [h12, hs12, map_smul]; funext a b c; simp
  · rw [h23, hs23, map_smul]; funext a b c; simp

/-- The colour swap as a `K`-linear map of `V^{⊗3}`. -/
def swapL : T3 K →ₗ[K] T3 K where
  toFun := swapT
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

/-- **The bare swap is not compatible with the braiding at generic `q`.** If the colour swap
commuted with both Jimbo braidings then `q² = 1`. -/
theorem swap_braid_commuting_imp (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h12 : ∀ w, R12 q (swapT w) = swapT (R12 q w))
    (h23 : ∀ w, R23 q (swapT w) = swapT (R23 q w)) : q ^ 2 = 1 :=
  swap01_eps_proportional q hq _
    (braid_commuting_fixes_singlet q hq h2 swapL h12 h23)

end QOU.Braiding.ColourRelabel
