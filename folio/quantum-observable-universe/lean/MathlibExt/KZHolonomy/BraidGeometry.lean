import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.Convex.Star
import Mathlib.Analysis.Calculus.Deriv.Pi
import Mathlib.Analysis.Calculus.Deriv.Prod
import Mathlib.Analysis.Complex.RealDeriv

/-!
# A star-shaped region of configuration space carrying the braid generators

Let `n = m + 1`.  The open set

    D = { z ∈ ℂⁿ : for all a < b, z_b − z_a ∉ −i·[0, ∞) }

consists of configurations of distinct points (`kzRegion_subset_injective`), is open
(`isOpen_kzRegion`) and is star-shaped about `c = (0, i, 2i, …, m i)`
(`starConvex_kzRegion`): along the segment from `c` to `z`, the difference
`(1−s)(b−a) i + s (z_b − z_a)` stays out of the closed ray `−i·[0,∞)`.

For a permutation `σ` let `p_σ = (σ 0, σ 1, …, σ m) ∈ ℝⁿ ⊂ ℂⁿ` (`basePt σ`); all of them
lie in `D`.  For a generator `j` (swapping strands `j` and `j+1`) the path `γ_j`
(`genPath j`) rotates the points at positions `j` and `j+1` half a turn counter-clockwise
about `j + 1/2`:

    γ_j(t)_j = j + ½ − ½ e^{iπt},   γ_j(t)_{j+1} = j + ½ + ½ e^{iπt},

other points fixed.  It runs from `p_1` to `p_{s_j}`, and the permuted path `γ_j ∘ σ`
from `p_σ` to `p_{s_j σ}` lies in `D` as soon as `σ⁻¹(j) < σ⁻¹(j+1)`
(`genPath_comp_mem`): then the two moving points have difference `+e^{iπt}`, which stays
in the closed upper half plane and avoids `−i·[0,∞)`.
-/

set_option autoImplicit false

namespace QOU.Mass.KZHolonomy

open Set Complex

/-- The closed ray `−i·[0,∞)` is avoided: `re w ≠ 0` or `im w > 0`. -/
def GoodDiff (w : ℂ) : Prop := w.re ≠ 0 ∨ 0 < w.im

lemma not_goodDiff_zero : ¬ GoodDiff 0 := by simp [GoodDiff]

/-- The star-shaped region of configuration space. -/
def kzRegion (n : ℕ) : Set (Fin n → ℂ) := {z | ∀ a b : Fin n, a < b → GoodDiff (z b - z a)}

/-- The centre `(0, i, 2i, …)` of the region. -/
noncomputable def kzCenter (n : ℕ) : Fin n → ℂ := fun k => ((k : ℕ) : ℂ) * I

lemma kzRegion_subset_injective (n : ℕ) : kzRegion n ⊆ {z | Function.Injective z} := by
  intro z hz a b hab
  by_contra hne
  rcases lt_or_gt_of_ne hne with h | h
  · exact not_goodDiff_zero (by simpa [hab] using hz a b h)
  · exact not_goodDiff_zero (by simpa [hab] using hz b a h)

lemma isOpen_kzRegion (n : ℕ) : IsOpen (kzRegion n) := by
  have : kzRegion n = ⋂ a : Fin n, ⋂ b : Fin n, {z | a < b → GoodDiff (z b - z a)} := by
    ext z; simp [kzRegion]
  rw [this]
  refine isOpen_iInter_of_finite fun a => isOpen_iInter_of_finite fun b => ?_
  by_cases hab : a < b
  · simp only [hab, true_implies, GoodDiff]
    have hc : Continuous fun z : Fin n → ℂ => z b - z a := by fun_prop
    exact (isOpen_ne_fun (continuous_re.comp hc) continuous_const).union
      (isOpen_lt continuous_const (continuous_im.comp hc))
  · simp [hab]

lemma starConvex_kzRegion (n : ℕ) : StarConvex ℝ (kzCenter n) (kzRegion n) := by
  intro z hz s t hs ht hst a b hab
  have hre : ((s • kzCenter n + t • z) b - (s • kzCenter n + t • z) a).re
      = t * (z b - z a).re := by
    simp [kzCenter, Complex.real_smul]; ring
  have him : ((s • kzCenter n + t • z) b - (s • kzCenter n + t • z) a).im
      = s * (((b : ℕ) : ℝ) - (a : ℕ)) + t * (z b - z a).im := by
    simp [kzCenter, Complex.real_smul]; ring
  have hba : (0 : ℝ) < ((b : ℕ) : ℝ) - (a : ℕ) := by
    have : (a : ℕ) < (b : ℕ) := hab
    have : ((a : ℕ) : ℝ) < (b : ℕ) := by exact_mod_cast this
    linarith
  unfold GoodDiff
  rw [hre, him]
  rcases eq_or_lt_of_le ht with rfl | htpos
  · right; simp only [zero_mul, add_zero]
    have : s = 1 := by linarith
    subst this; linarith
  · rcases hz a b hab with h | h
    · left; exact mul_ne_zero htpos.ne' h
    · right; have := mul_pos htpos h; nlinarith

/-- The real configuration `(σ 0, σ 1, …)`. -/
def basePt {n : ℕ} (σ : Equiv.Perm (Fin n)) : Fin n → ℂ := fun k => (((σ k : Fin n) : ℕ) : ℂ)

lemma basePt_mem {n : ℕ} (σ : Equiv.Perm (Fin n)) : basePt σ ∈ kzRegion n := by
  intro a b hab
  left
  have hne : ((σ b : Fin n) : ℕ) ≠ ((σ a : Fin n) : ℕ) := by
    intro h; exact hab.ne' (σ.injective (Fin.ext h))
  simp only [basePt, sub_re, natCast_re]
  intro h
  exact hne (by exact_mod_cast sub_eq_zero.1 h)

/-- `e^{iπt}`, written with real cosine and sine. -/
noncomputable def eArc (t : ℝ) : ℂ := (Real.cos (Real.pi * t) : ℂ) + (Real.sin (Real.pi * t) : ℂ) * I

/-- The derivative of `eArc`. -/
noncomputable def eArc' (t : ℝ) : ℂ :=
  ((-(Real.sin (Real.pi * t) * Real.pi) : ℝ) : ℂ) + ((Real.cos (Real.pi * t) * Real.pi : ℝ) : ℂ) * I

lemma hasDerivAt_eArc (t : ℝ) : HasDerivAt eArc (eArc' t) t := by
  have hc : HasDerivAt (fun s : ℝ => Real.cos (Real.pi * s)) (-(Real.sin (Real.pi * t) * Real.pi)) t := by
    simpa using ((hasDerivAt_id t).const_mul Real.pi).cos
  have hs : HasDerivAt (fun s : ℝ => Real.sin (Real.pi * s)) (Real.cos (Real.pi * t) * Real.pi) t := by
    simpa using ((hasDerivAt_id t).const_mul Real.pi).sin
  exact hc.ofReal_comp.add (hs.ofReal_comp.mul_const I)

lemma continuous_eArc' : Continuous eArc' := by unfold eArc'; fun_prop

lemma eArc_re (t : ℝ) : (eArc t).re = Real.cos (Real.pi * t) := by
  simp only [eArc, add_re, mul_re, ofReal_re, ofReal_im, I_re, I_im]; ring
lemma eArc_im (t : ℝ) : (eArc t).im = Real.sin (Real.pi * t) := by
  simp only [eArc, add_im, mul_im, ofReal_re, ofReal_im, I_re, I_im]; ring
lemma eArc_zero : eArc 0 = 1 := by simp [eArc]
lemma eArc_one : eArc 1 = -1 := by simp [eArc]

variable {m : ℕ}

/-- The half-turn exchanging the points at positions `j` and `j + 1`. -/
noncomputable def genPath (j : Fin m) (t : ℝ) : Fin (m + 1) → ℂ := fun k =>
  if k = j.castSucc then ((j : ℕ) : ℂ) + 1 / 2 - eArc t / 2
  else if k = j.succ then ((j : ℕ) : ℂ) + 1 / 2 + eArc t / 2
  else ((k : ℕ) : ℂ)

/-- The velocity of `genPath j`. -/
noncomputable def genPath' (j : Fin m) (t : ℝ) : Fin (m + 1) → ℂ := fun k =>
  if k = j.castSucc then -(eArc' t / 2)
  else if k = j.succ then eArc' t / 2
  else 0

lemma hasDerivAt_genPath (j : Fin m) (t : ℝ) : HasDerivAt (genPath j) (genPath' j t) t := by
  refine hasDerivAt_pi.2 fun k => ?_
  simp only [genPath, genPath']
  split_ifs
  · exact ((hasDerivAt_eArc t).div_const 2).const_sub _
  · exact ((hasDerivAt_eArc t).div_const 2).const_add _
  · exact hasDerivAt_const _ _

lemma continuous_genPath' (j : Fin m) : Continuous (genPath' j) := by
  refine continuous_pi fun k => ?_
  simp only [genPath']
  split_ifs
  · exact (continuous_eArc'.div_const 2).neg
  · exact continuous_eArc'.div_const 2
  · exact continuous_const

/-- Derivative of the permuted path `γ_j ∘ σ`. -/
lemma hasDerivAt_genPath_comp (j : Fin m) (σ : Equiv.Perm (Fin (m + 1))) (t : ℝ) :
    HasDerivAt (fun s => genPath j s ∘ σ) (genPath' j t ∘ σ) t :=
  hasDerivAt_pi.2 fun k => hasDerivAt_pi.1 (hasDerivAt_genPath j t) (σ k)

lemma continuous_genPath'_comp (j : Fin m) (σ : Equiv.Perm (Fin (m + 1))) :
    Continuous fun t => genPath' j t ∘ σ :=
  continuous_pi fun k => (continuous_apply (σ k)).comp (continuous_genPath' j)

lemma genPath_zero (j : Fin m) : genPath j 0 = basePt 1 := by
  ext1 k
  simp only [genPath, basePt, eArc_zero, Equiv.Perm.coe_one, id]
  split_ifs with h1 h2
  · subst h1; simp
  · subst h2; simp; ring
  · rfl

lemma genPath_one (j : Fin m) : genPath j 1 = basePt (Equiv.swap j.castSucc j.succ) := by
  ext1 k
  simp only [genPath, basePt, eArc_one]
  have hne : j.castSucc ≠ j.succ := Fin.castSucc_lt_succ j |>.ne
  split_ifs with h1 h2
  · subst h1; simp; ring
  · subst h2; simp [Equiv.swap_apply_right]; ring
  · rw [Equiv.swap_apply_of_ne_of_ne h1 h2]

lemma basePt_comp (σ τ : Equiv.Perm (Fin (m + 1))) : basePt σ ∘ τ = basePt (σ * τ) := rfl

/-- Real parts along `γ_j`: the moving points stay in the strip `j ≤ re ≤ j + 1`. -/
lemma genPath_re_mem (j : Fin m) (t : ℝ) (k : Fin (m + 1))
    (hk : k = j.castSucc ∨ k = j.succ) :
    ((j : ℕ) : ℝ) ≤ (genPath j t k).re ∧ (genPath j t k).re ≤ (j : ℕ) + 1 := by
  have h1 := Real.neg_one_le_cos (Real.pi * t)
  have h2 := Real.cos_le_one (Real.pi * t)
  have hne : j.castSucc ≠ j.succ := (Fin.castSucc_lt_succ j).ne
  rcases hk with rfl | rfl
  · simp only [genPath]; simp [eArc_re]; constructor <;> linarith
  · simp only [genPath, if_neg hne.symm]; simp [eArc_re]; constructor <;> linarith

lemma genPath_re_fixed (j : Fin m) (t : ℝ) (k : Fin (m + 1)) (h1 : k ≠ j.castSucc)
    (h2 : k ≠ j.succ) : (genPath j t k).re = (k : ℕ) := by
  simp [genPath, h1, h2]

/-- All pairs except the reversed moving pair have good differences along `γ_j`. -/
lemma goodDiff_genPath (j : Fin m) {t : ℝ} (ht : t ∈ Icc (0:ℝ) 1) (x y : Fin (m + 1))
    (hxy : x ≠ y) (hrev : ¬ (x = j.succ ∧ y = j.castSucc)) :
    GoodDiff (genPath j t y - genPath j t x) := by
  have hne : j.castSucc ≠ j.succ := (Fin.castSucc_lt_succ j).ne
  have hcs : ((j.castSucc : Fin (m+1)) : ℕ) = j := rfl
  have hsu : ((j.succ : Fin (m+1)) : ℕ) = j + 1 := rfl
  by_cases hxm : x = j.castSucc ∨ x = j.succ <;> by_cases hym : y = j.castSucc ∨ y = j.succ
  · -- both moving: necessarily x = castSucc, y = succ
    have hx : x = j.castSucc := by
      rcases hxm with h | h
      · exact h
      · rcases hym with h' | h'
        · exact absurd ⟨h, h'⟩ hrev
        · exact absurd (h.trans h'.symm) hxy
    have hy : y = j.succ := by
      rcases hym with h' | h'
      · exact absurd (hx.trans h'.symm) hxy
      · exact h'
    subst hx hy
    have hdiff : genPath j t j.succ - genPath j t j.castSucc = eArc t := by
      simp only [genPath, if_neg hne.symm, if_true]; ring
    rw [hdiff]
    unfold GoodDiff
    rw [eArc_re, eArc_im]
    have hsin : 0 ≤ Real.sin (Real.pi * t) :=
      Real.sin_nonneg_of_nonneg_of_le_pi (by nlinarith [Real.pi_pos, ht.1])
        (by nlinarith [Real.pi_pos, ht.2])
    by_cases hc : Real.cos (Real.pi * t) = 0
    · right
      have := Real.sin_sq_add_cos_sq (Real.pi * t)
      rw [hc] at this
      rcases eq_or_lt_of_le hsin with h | h
      · rw [← h] at this; norm_num at this
      · exact h
    · left; exact hc
  · -- x moving, y fixed
    left
    push_neg at hym
    rw [sub_re, genPath_re_fixed j t y hym.1 hym.2]
    obtain ⟨hl, hu⟩ := genPath_re_mem j t x hxm
    have hy1 : (y : ℕ) ≠ j := fun h => hym.1 (Fin.ext (h.trans hcs.symm))
    have hy2 : (y : ℕ) ≠ j + 1 := fun h => hym.2 (Fin.ext (h.trans hsu.symm))
    intro h
    have hyr : ((y : ℕ) : ℝ) = (genPath j t x).re := by linarith
    have a1 : (j : ℕ) ≤ (y : ℕ) := by exact_mod_cast (hyr ▸ hl)
    have a2 : (y : ℕ) ≤ (j : ℕ) + 1 := by exact_mod_cast (hyr ▸ hu)
    omega
  · -- x fixed, y moving
    left
    push_neg at hxm
    rw [sub_re, genPath_re_fixed j t x hxm.1 hxm.2]
    obtain ⟨hl, hu⟩ := genPath_re_mem j t y hym
    have hx1 : (x : ℕ) ≠ j := fun h => hxm.1 (Fin.ext (h.trans hcs.symm))
    have hx2 : (x : ℕ) ≠ j + 1 := fun h => hxm.2 (Fin.ext (h.trans hsu.symm))
    intro h
    have hxr : ((x : ℕ) : ℝ) = (genPath j t y).re := by linarith
    have a1 : (j : ℕ) ≤ (x : ℕ) := by exact_mod_cast (hxr ▸ hl)
    have a2 : (x : ℕ) ≤ (j : ℕ) + 1 := by exact_mod_cast (hxr ▸ hu)
    omega
  · -- both fixed
    left
    push_neg at hxm hym
    rw [sub_re, genPath_re_fixed j t x hxm.1 hxm.2, genPath_re_fixed j t y hym.1 hym.2]
    intro h
    exact hxy (Fin.ext (by exact_mod_cast (sub_eq_zero.1 h).symm))

/-- The permuted half-turn `γ_j ∘ σ` stays in the region when `σ⁻¹(j) < σ⁻¹(j+1)`. -/
lemma genPath_comp_mem (j : Fin m) (σ : Equiv.Perm (Fin (m + 1)))
    (hσ : σ⁻¹ j.castSucc < σ⁻¹ j.succ) {t : ℝ} (ht : t ∈ Icc (0:ℝ) 1) :
    genPath j t ∘ σ ∈ kzRegion (m + 1) := by
  intro a b hab
  refine goodDiff_genPath j ht (σ a) (σ b) (σ.injective.ne hab.ne) ?_
  rintro ⟨h1, h2⟩
  have ha : a = σ⁻¹ j.succ := by rw [← h1]; simp
  have hb : b = σ⁻¹ j.castSucc := by rw [← h2]; simp
  rw [ha, hb] at hab
  exact lt_asymm hab hσ

end QOU.Mass.KZHolonomy
