import QOU.Mass.KZHolonomy.BraidGauge
import QOU.MathlibExt.PathLebesgue
import Mathlib.Data.Fin.Tuple.Sort
import Mathlib.Data.Prod.Lex

/-!
# Star-shaped regions of `Conf_{m+1}(ℂ)` around the half-turns

For a permutation `τ` and a position `j`, `region τ j` is the set of configurations `z` such that

* the real parts `re z(τ 0), …, re z(τ m)` are strictly increasing, except possibly between the
  two positions `j, j+1`; and
* the difference `z(τ j) − z(τ (j+1))` avoids the closed ray `i·[0, ∞)`.

It is open, lies in `Conf_{m+1}(ℂ)`, and is star-shaped about the midpoint of the half-turn
`γ_j ∘ τ⁻¹`, so it is simply connected.  It contains the whole half-turn `γ_j ∘ τ⁻¹`, which runs
from `p_{τ⁻¹}` to `p_{s_j τ⁻¹}`.

Every configuration `z` has a unique *lexicographic order* `σ_z`: the permutation for which
`k ↦ (re z(σ k), im z(σ k))` is strictly increasing in the lexicographic order
(`lexSorted`).  A configuration in `region τ j` is lexicographically sorted by `τ` or by `τ s_j`
(`lexSorted_of_mem_region`), and a configuration whose real parts are strictly sorted by `σ` lies in
`region σ j` and `region (σ s_j) j` for every `j` (`mem_region_of_reSorted`).
-/

set_option autoImplicit false

namespace QOU.Mass.KZHolonomy

open Set Complex

variable {m : ℕ}

/-- The closed ray `i·[0, ∞)`. -/
def slit : Set ℂ := {w | w.re = 0 ∧ 0 ≤ w.im}

lemma isClosed_slit : IsClosed slit :=
  (isClosed_eq continuous_re continuous_const).inter (isClosed_le continuous_const continuous_im)

lemma zero_mem_slit : (0 : ℂ) ∈ slit := by simp [slit]

/-- The region around the half-turn at positions `j, j+1` of the order `τ`. -/
def region (τ : Equiv.Perm (Fin (m + 1))) (j : Fin m) : Set (Fin (m + 1) → ℂ) :=
  {z | (∀ k l : Fin (m + 1), k < l → ¬ (k = j.castSucc ∧ l = j.succ) →
      (z (τ k)).re < (z (τ l)).re) ∧
    z (τ j.castSucc) - z (τ j.succ) ∉ slit}

lemma isOpen_region (τ : Equiv.Perm (Fin (m + 1))) (j : Fin m) : IsOpen (region τ j) := by
  refine IsOpen.inter ?_ ((isClosed_slit.preimage (by fun_prop)).isOpen_compl)
  have : {z : Fin (m + 1) → ℂ | ∀ k l : Fin (m + 1), k < l → ¬ (k = j.castSucc ∧ l = j.succ) →
      (z (τ k)).re < (z (τ l)).re} =
      ⋂ k : Fin (m + 1), ⋂ l : Fin (m + 1), {z | k < l → ¬ (k = j.castSucc ∧ l = j.succ) →
        (z (τ k)).re < (z (τ l)).re} := by ext; simp
  rw [show (fun z : Fin (m + 1) → ℂ => ∀ k l : Fin (m + 1), k < l →
      ¬ (k = j.castSucc ∧ l = j.succ) → (z (τ k)).re < (z (τ l)).re) =
      {z : Fin (m + 1) → ℂ | ∀ k l : Fin (m + 1), k < l → ¬ (k = j.castSucc ∧ l = j.succ) →
      (z (τ k)).re < (z (τ l)).re} from rfl, this]
  refine isOpen_iInter_of_finite fun k => isOpen_iInter_of_finite fun l => ?_
  by_cases h : k < l ∧ ¬ (k = j.castSucc ∧ l = j.succ)
  · have e : {z : Fin (m + 1) → ℂ | k < l → ¬ (k = j.castSucc ∧ l = j.succ) →
        (z (τ k)).re < (z (τ l)).re} = {z | (z (τ k)).re < (z (τ l)).re} := by
      ext z; simp only [mem_setOf_eq]; exact ⟨fun hz => hz h.1 h.2, fun hz _ _ => hz⟩
    rw [e]; exact isOpen_lt (by fun_prop) (by fun_prop)
  · have e : {z : Fin (m + 1) → ℂ | k < l → ¬ (k = j.castSucc ∧ l = j.succ) →
        (z (τ k)).re < (z (τ l)).re} = univ := by
      ext z; simp only [mem_setOf_eq, mem_univ, iff_true]
      intro h1 h2; exact absurd ⟨h1, h2⟩ h
    rw [e]; exact isOpen_univ

lemma region_subset_conf (τ : Equiv.Perm (Fin (m + 1))) (j : Fin m) :
    region τ j ⊆ confSet (m + 1) := by
  rintro z ⟨hlt, hsl⟩ a b hab
  by_contra hne
  have key : ∀ k l : Fin (m + 1), k < l → z (τ k) = z (τ l) → False := by
    intro k l hkl he
    by_cases hs : k = j.castSucc ∧ l = j.succ
    · obtain ⟨rfl, rfl⟩ := hs
      exact hsl (by rw [he, sub_self]; exact zero_mem_slit)
    · exact (hlt k l hkl hs).ne (by rw [he])
  have ha : a = τ (τ⁻¹ a) := by simp
  have hb : b = τ (τ⁻¹ b) := by simp
  rcases lt_trichotomy (τ⁻¹ a) (τ⁻¹ b) with h | h | h
  · exact key _ _ h (by rw [← ha, ← hb]; exact hab)
  · exact hne (by rw [ha, hb, h])
  · exact key _ _ h (by rw [← ha, ← hb]; exact hab.symm)

/-! ### The half-turn lies in its region -/

lemma genPath_re_lt (j : Fin m) (t : ℝ) {k l : Fin (m + 1)} (hkl : k < l)
    (hns : ¬ (k = j.castSucc ∧ l = j.succ)) : (genPath j t k).re < (genPath j t l).re := by
  have hcs : ((j.castSucc : Fin (m + 1)) : ℕ) = j := rfl
  have hsu : ((j.succ : Fin (m + 1)) : ℕ) = j + 1 := rfl
  have hkl' : (k : ℕ) < l := hkl
  by_cases hkm : k = j.castSucc ∨ k = j.succ <;> by_cases hlm : l = j.castSucc ∨ l = j.succ
  · exfalso
    rcases hkm with rfl | rfl <;> rcases hlm with rfl | rfl
    · exact lt_irrefl _ hkl
    · exact hns ⟨rfl, rfl⟩
    · rw [hcs, hsu] at hkl'; omega
    · exact lt_irrefl _ hkl
  · push_neg at hlm
    rw [genPath_re_fixed j t l hlm.1 hlm.2]
    obtain ⟨-, hu⟩ := genPath_re_mem j t k hkm
    have hl1 : (l : ℕ) ≠ j := fun h => hlm.1 (Fin.ext (h.trans hcs.symm))
    have hl2 : (l : ℕ) ≠ j + 1 := fun h => hlm.2 (Fin.ext (h.trans hsu.symm))
    have hk : (k : ℕ) = j ∨ (k : ℕ) = j + 1 := by
      rcases hkm with rfl | rfl
      · left; rfl
      · right; rfl
    have : (j : ℕ) + 2 ≤ (l : ℕ) := by omega
    have : ((j : ℕ) : ℝ) + 2 ≤ ((l : ℕ) : ℝ) := by exact_mod_cast this
    linarith
  · push_neg at hkm
    rw [genPath_re_fixed j t k hkm.1 hkm.2]
    obtain ⟨hl, -⟩ := genPath_re_mem j t l hlm
    have hk1 : (k : ℕ) ≠ j := fun h => hkm.1 (Fin.ext (h.trans hcs.symm))
    have hk2 : (k : ℕ) ≠ j + 1 := fun h => hkm.2 (Fin.ext (h.trans hsu.symm))
    have hl' : (l : ℕ) = j ∨ (l : ℕ) = j + 1 := by
      rcases hlm with rfl | rfl
      · left; rfl
      · right; rfl
    have : (k : ℕ) + 1 ≤ (j : ℕ) := by omega
    have : ((k : ℕ) : ℝ) + 1 ≤ ((j : ℕ) : ℝ) := by exact_mod_cast this
    linarith
  · push_neg at hkm hlm
    rw [genPath_re_fixed j t k hkm.1 hkm.2, genPath_re_fixed j t l hlm.1 hlm.2]
    exact_mod_cast hkl'

lemma genPath_diff (j : Fin m) (t : ℝ) :
    genPath j t j.castSucc - genPath j t j.succ = -eArc t := by
  have hne : j.castSucc ≠ j.succ := (Fin.castSucc_lt_succ j).ne
  simp only [genPath, if_neg hne.symm, if_true]; ring

lemma neg_eArc_not_mem_slit {t : ℝ} (ht : t ∈ Icc (0 : ℝ) 1) : -eArc t ∉ slit := by
  rintro ⟨h1, h2⟩
  rw [neg_re, eArc_re] at h1
  rw [neg_im, eArc_im] at h2
  have hsin : 0 ≤ Real.sin (Real.pi * t) :=
    Real.sin_nonneg_of_nonneg_of_le_pi (by nlinarith [Real.pi_pos, ht.1])
      (by nlinarith [Real.pi_pos, ht.2])
  have h3 := Real.sin_sq_add_cos_sq (Real.pi * t)
  have hs0 : Real.sin (Real.pi * t) = 0 := by linarith
  have hc0 : Real.cos (Real.pi * t) = 0 := by linarith
  rw [hs0, hc0] at h3; norm_num at h3

/-- The half-turn `γ_j ∘ τ⁻¹` stays in `region τ j`. -/
theorem genPath_comp_mem_region (τ : Equiv.Perm (Fin (m + 1))) (j : Fin m) {t : ℝ}
    (ht : t ∈ Icc (0 : ℝ) 1) : genPath j t ∘ ⇑τ⁻¹ ∈ region τ j := by
  refine ⟨fun k l hkl hns => ?_, ?_⟩
  · simp only [Function.comp_apply, Equiv.Perm.inv_apply_self]
    exact genPath_re_lt j t hkl hns
  · simp only [Function.comp_apply, Equiv.Perm.inv_apply_self]
    rw [genPath_diff]; exact neg_eArc_not_mem_slit ht

/-- The centre of `region τ j`: the midpoint of the half-turn. -/
noncomputable def regionCentre (τ : Equiv.Perm (Fin (m + 1))) (j : Fin m) :
    Fin (m + 1) → ℂ := genPath j (1 / 2) ∘ ⇑τ⁻¹

lemma eArc_half : eArc (1 / 2) = I := by
  rw [eArc, show Real.pi * (1 / 2) = Real.pi / 2 by ring, Real.cos_pi_div_two,
    Real.sin_pi_div_two]
  simp

lemma regionCentre_mem (τ : Equiv.Perm (Fin (m + 1))) (j : Fin m) :
    regionCentre τ j ∈ region τ j :=
  genPath_comp_mem_region τ j ⟨by norm_num, by norm_num⟩

lemma regionCentre_diff (τ : Equiv.Perm (Fin (m + 1))) (j : Fin m) :
    regionCentre τ j (τ j.castSucc) - regionCentre τ j (τ j.succ) = -I := by
  simp only [regionCentre, Function.comp_apply, Equiv.Perm.inv_apply_self]
  rw [genPath_diff, eArc_half]

theorem starConvex_region (τ : Equiv.Perm (Fin (m + 1))) (j : Fin m) :
    StarConvex ℝ (regionCentre τ j) (region τ j) := by
  intro z hz a b ha hb hab
  obtain ⟨hc1, -⟩ := regionCentre_mem τ j
  obtain ⟨hz1, hz2⟩ := hz
  refine ⟨fun k l hkl hns => ?_, ?_⟩
  · have h1 := hc1 k l hkl hns
    have h2 := hz1 k l hkl hns
    simp only [Pi.add_apply, Pi.smul_apply, add_re, smul_re, smul_eq_mul]
    rcases eq_or_lt_of_le ha with ha0 | ha0
    · subst ha0; have hb1 : b = 1 := by linarith
      subst hb1; simpa using h2
    · nlinarith
  · have hdc := regionCentre_diff τ j
    simp only [Pi.add_apply, Pi.smul_apply]
    rintro ⟨h1, h2⟩
    have hre : ((a • regionCentre τ j (τ j.castSucc) + b • z (τ j.castSucc)) -
        (a • regionCentre τ j (τ j.succ) + b • z (τ j.succ))).re =
        a * (regionCentre τ j (τ j.castSucc) - regionCentre τ j (τ j.succ)).re +
          b * (z (τ j.castSucc) - z (τ j.succ)).re := by
      simp only [sub_re, add_re, smul_re, smul_eq_mul]; ring
    have him : ((a • regionCentre τ j (τ j.castSucc) + b • z (τ j.castSucc)) -
        (a • regionCentre τ j (τ j.succ) + b • z (τ j.succ))).im =
        a * (regionCentre τ j (τ j.castSucc) - regionCentre τ j (τ j.succ)).im +
          b * (z (τ j.castSucc) - z (τ j.succ)).im := by
      simp only [sub_im, add_im, smul_im, smul_eq_mul]; ring
    rw [hre, hdc] at h1
    rw [him, hdc] at h2
    simp only [neg_re, I_re, neg_zero, mul_zero, zero_add, neg_im, I_im] at h1 h2
    rcases eq_or_lt_of_le hb with hb0 | hb0
    · subst hb0; have : a = 1 := by linarith
      subst this; linarith
    · have hr : (z (τ j.castSucc) - z (τ j.succ)).re = 0 := by
        rcases mul_eq_zero.1 h1 with h | h
        · exact absurd h hb0.ne'
        · exact h
      have hi : (z (τ j.castSucc) - z (τ j.succ)).im < 0 := by
        by_contra hc; push_neg at hc; exact hz2 ⟨hr, hc⟩
      nlinarith

instance (τ : Equiv.Perm (Fin (m + 1))) (j : Fin m) : SimplyConnectedSpace (region τ j) :=
  haveI := (starConvex_region τ j).contractibleSpace ⟨_, regionCentre_mem τ j⟩
  inferInstance

/-! ### Lexicographic and real-part orders -/

/-- The lexicographic key `(re, im)` of a point. -/
def lexKey (z : Fin (m + 1) → ℂ) (k : Fin (m + 1)) : ℝ ×ₗ ℝ := toLex ((z k).re, (z k).im)

lemma lexKey_lt_iff (z : Fin (m + 1) → ℂ) (k l : Fin (m + 1)) :
    lexKey z k < lexKey z l ↔
      (z k).re < (z l).re ∨ ((z k).re = (z l).re ∧ (z k).im < (z l).im) :=
  Prod.Lex.toLex_lt_toLex

/-- `σ` sorts `z` lexicographically. -/
def LexSorted (z : Fin (m + 1) → ℂ) (σ : Equiv.Perm (Fin (m + 1))) : Prop :=
  StrictMono (lexKey z ∘ σ)

lemma lexKey_injective {z : Fin (m + 1) → ℂ} (hz : z ∈ confSet (m + 1)) :
    Function.Injective (lexKey z) := by
  intro k l h
  apply hz
  have h' := congrArg ofLex h
  simp only [lexKey, ofLex_toLex, Prod.mk.injEq] at h'
  exact Complex.ext h'.1 h'.2

lemma exists_lexSorted {z : Fin (m + 1) → ℂ} (hz : z ∈ confSet (m + 1)) :
    ∃ σ, LexSorted z σ :=
  ⟨Tuple.sort (lexKey z),
    (Tuple.monotone_sort _).strictMono_of_injective
      ((lexKey_injective hz).comp (Tuple.sort _).injective)⟩

lemma lexSorted_unique {z : Fin (m + 1) → ℂ} {σ σ' : Equiv.Perm (Fin (m + 1))} (h : LexSorted z σ) (h' : LexSorted z σ') : σ = σ' := by
  set π := σ⁻¹ * σ' with hπ
  have hmono : StrictMono π := by
    intro a b hab
    have := h' hab
    have e : ∀ x, σ' x = σ (π x) := fun x => by simp [hπ]
    simp only [Function.comp_apply, e] at this
    exact h.lt_iff_lt.1 this
  have hid : (π : Fin (m + 1) → Fin (m + 1)) = id :=
    (hmono.range_inj strictMono_id).1 (by simp [π.surjective.range_eq])
  have : π = 1 := Equiv.ext fun x => congrFun hid x
  rw [hπ, inv_mul_eq_one] at this
  exact this

/-- `σ` sorts the real parts of `z` strictly. -/
def ReSorted (z : Fin (m + 1) → ℂ) (σ : Equiv.Perm (Fin (m + 1))) : Prop :=
  StrictMono fun k => (z (σ k)).re

lemma ReSorted.lexSorted {z : Fin (m + 1) → ℂ} {σ : Equiv.Perm (Fin (m + 1))}
    (h : ReSorted z σ) : LexSorted z σ := fun _ _ hab =>
  (lexKey_lt_iff _ _ _).2 (Or.inl (h hab))

/-- The adjacent transposition preserves every strict inequality except its own. -/
lemma swap_lt_swap (j : Fin m) {k l : Fin (m + 1)} (hkl : k < l)
    (hns : ¬ (k = j.castSucc ∧ l = j.succ)) :
    Equiv.swap j.castSucc j.succ k < Equiv.swap j.castSucc j.succ l := by
  have hcs : ((j.castSucc : Fin (m + 1)) : ℕ) = j := rfl
  have hsu : ((j.succ : Fin (m + 1)) : ℕ) = j + 1 := rfl
  rw [Equiv.swap_apply_def, Equiv.swap_apply_def]
  have hkl' : (k : ℕ) < l := hkl
  have hns' : ¬ ((k : ℕ) = j ∧ (l : ℕ) = j + 1) := fun ⟨h1, h2⟩ =>
    hns ⟨Fin.ext (h1.trans hcs.symm), Fin.ext (h2.trans hsu.symm)⟩
  split_ifs with h1 h2 h3 h4 h5 h6 h7 h8 <;>
    simp only [Fin.lt_iff_val_lt_val, Fin.ext_iff, hcs, hsu] at * <;> omega

lemma mem_region_of_reSorted {z : Fin (m + 1) → ℂ} {σ : Equiv.Perm (Fin (m + 1))}
    (h : ReSorted z σ) (j : Fin m) :
    z ∈ region σ j ∧ z ∈ region (σ * Equiv.swap j.castSucc j.succ) j := by
  have hne : j.castSucc ≠ j.succ := (Fin.castSucc_lt_succ j).ne
  have hlt : (z (σ j.castSucc)).re < (z (σ j.succ)).re := h (Fin.castSucc_lt_succ j)
  refine ⟨⟨fun k l hkl _ => h hkl, fun hs => ?_⟩, ⟨fun k l hkl hns => ?_, fun hs => ?_⟩⟩
  · have := hs.1; rw [sub_re] at this; linarith
  · simp only [Equiv.Perm.coe_mul, Function.comp_apply]
    exact h (swap_lt_swap j hkl hns)
  · have := hs.1
    simp only [Equiv.Perm.coe_mul, Function.comp_apply, Equiv.swap_apply_left,
      Equiv.swap_apply_right, sub_re] at this
    linarith

lemma reSorted_basePt (σ : Equiv.Perm (Fin (m + 1))) : ReSorted (basePt σ⁻¹) σ := by
  intro a b hab
  simp only [basePt, Equiv.Perm.inv_apply_self, natCast_re]
  exact_mod_cast hab

/-- A configuration in `region τ j` is sorted lexicographically by `τ` or by `τ s_j`. -/
theorem lexSorted_of_mem_region {τ : Equiv.Perm (Fin (m + 1))} {j : Fin m}
    {z : Fin (m + 1) → ℂ} (hz : z ∈ region τ j) :
    ((z (τ j.castSucc)).re ≤ (z (τ j.succ)).re ∧ LexSorted z τ) ∨
      ((z (τ j.succ)).re < (z (τ j.castSucc)).re ∧
        LexSorted z (τ * Equiv.swap j.castSucc j.succ)) := by
  obtain ⟨hlt, hsl⟩ := hz
  rcases le_or_gt (z (τ j.castSucc)).re (z (τ j.succ)).re with hle | hgt
  · refine Or.inl ⟨hle, fun k l hkl => ?_⟩
    simp only [Function.comp_apply]
    rw [lexKey_lt_iff]
    by_cases hs : k = j.castSucc ∧ l = j.succ
    · obtain ⟨rfl, rfl⟩ := hs
      rcases lt_or_eq_of_le hle with h | h
      · exact Or.inl h
      · refine Or.inr ⟨h, ?_⟩
        by_contra hc; push_neg at hc
        exact hsl ⟨by rw [sub_re, h, sub_self], by rw [sub_im]; linarith⟩
    · exact Or.inl (hlt k l hkl hs)
  · refine Or.inr ⟨hgt, fun k l hkl => ?_⟩
    simp only [Function.comp_apply, Equiv.Perm.coe_mul]
    rw [lexKey_lt_iff]
    by_cases hs : k = j.castSucc ∧ l = j.succ
    · obtain ⟨rfl, rfl⟩ := hs
      simp only [Equiv.swap_apply_left, Equiv.swap_apply_right]
      exact Or.inl hgt
    · exact Or.inl (hlt _ _ (swap_lt_swap j hkl hs) (by
        rintro ⟨h1, h2⟩
        have e1 : k = j.succ := by
          have := congrArg (Equiv.swap j.castSucc j.succ) h1
          simpa using this
        have e2 : l = j.castSucc := by
          have := congrArg (Equiv.swap j.castSucc j.succ) h2
          simpa using this
        rw [e1, e2] at hkl
        exact absurd hkl (not_lt.2 (Fin.castSucc_lt_succ j).le)))

end QOU.Mass.KZHolonomy
