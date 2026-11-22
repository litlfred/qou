import Mathlib.CategoryTheory.Linear.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic

namespace QOU.Eightfold.TraceSplitting

open CategoryTheory

variable {k : Type*} [Field k] {C : Type*} [Category C] [Preadditive C] [Linear k C]
variable {U W : C}

/-- The candidate singlet projector `d⁻¹ • (e ≫ c)` on `W`, where `c : U ⟶ W` plays the
coevaluation and `e : W ⟶ U` the evaluation. -/
noncomputable def proj (c : U ⟶ W) (e : W ⟶ U) (d : k) : W ⟶ W := d⁻¹ • (e ≫ c)

/-- The complementary (octet) projector `𝟙 − proj`. -/
noncomputable def coproj (c : U ⟶ W) (e : W ⟶ U) (d : k) : W ⟶ W := 𝟙 W - proj c e d

variable (c : U ⟶ W) (e : W ⟶ U) (d : k)

theorem proj_idem (h : c ≫ e = d • 𝟙 U) (hd : d ≠ 0) :
    proj c e d ≫ proj c e d = proj c e d := by
  unfold proj
  have : (e ≫ c) ≫ (e ≫ c) = d • (e ≫ c) := by
    rw [Category.assoc, ← Category.assoc c, h]; simp
  rw [Linear.smul_comp, Linear.comp_smul, this, smul_smul, smul_smul]
  congr 1; field_simp

theorem coev_comp_proj (h : c ≫ e = d • 𝟙 U) (hd : d ≠ 0) : c ≫ proj c e d = c := by
  unfold proj
  rw [Linear.comp_smul, ← Category.assoc, h]; simp [smul_smul, hd]

theorem proj_comp_ev (h : c ≫ e = d • 𝟙 U) (hd : d ≠ 0) : proj c e d ≫ e = e := by
  unfold proj
  rw [Linear.smul_comp, Category.assoc, h]; simp [smul_smul, hd]

theorem coproj_idem (h : c ≫ e = d • 𝟙 U) (hd : d ≠ 0) :
    coproj c e d ≫ coproj c e d = coproj c e d := by
  unfold coproj
  simp only [Preadditive.sub_comp, Preadditive.comp_sub, Category.id_comp, Category.comp_id,
    proj_idem c e d h hd]
  abel

theorem proj_comp_coproj (h : c ≫ e = d • 𝟙 U) (hd : d ≠ 0) :
    proj c e d ≫ coproj c e d = 0 := by
  unfold coproj
  rw [Preadditive.comp_sub, Category.comp_id, proj_idem c e d h hd, sub_self]

theorem coproj_comp_ev (h : c ≫ e = d • 𝟙 U) (hd : d ≠ 0) : coproj c e d ≫ e = 0 := by
  unfold coproj
  rw [Preadditive.sub_comp, Category.id_comp, proj_comp_ev c e d h hd, sub_self]

theorem coev_comp_coproj (h : c ≫ e = d • 𝟙 U) (hd : d ≠ 0) : c ≫ coproj c e d = 0 := by
  unfold coproj
  rw [Preadditive.comp_sub, Category.comp_id, coev_comp_proj c e d h hd, sub_self]

theorem proj_add_coproj : proj c e d + coproj c e d = 𝟙 W := by
  unfold coproj; abel

/-- The quantum dimension `[3]_q = q² + 1 + q⁻²` of the `U_q(sl₃)` fundamental is nonzero for
every nonzero `q` in an ordered field, so the hypothesis `d ≠ 0` holds there with `d = [3]_q`. -/
theorem qint_three_ne_zero {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (q : F) : q ^ 2 + 1 + q⁻¹ ^ 2 ≠ 0 := by
  positivity

end QOU.Eightfold.TraceSplitting
