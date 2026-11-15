import QOU.KZ.Drinfeld.RibbonDH
import QOU.Mass.BraidedStrands

/-!
# The Drinfeld category `D_ℏ` gives a Hecke action on `V^{⊗n}` for every `n`

Bridge A, step A4 (`QOU.Mass.BraidedStrands`), applied to the braided `ℂ`-linear category
`D_ℏ` of bean `qou-zoyv` (`QOU.KZ.Drinfeld.Braided`, `QOU.KZ.Drinfeld.Linear`). Here
`V = ℂ²`, `s = e^{iπℏ/2}`, `q = e^{iπℏ}`, and the generator is the rescaled braiding
`g = s · β_{V,V}`.

* `g_quad` — `g² = (q − q⁻¹) g + 1` on `V ⊗ V`, from `hecke_DH`
  (`s β − s⁻¹ β⁻¹ = (q − q⁻¹)·𝟙`).
* `g_isYB` — `g` satisfies the three-strand relation: the braiding does, by the hexagons
  (`isYB_braiding`), and rescaling preserves it (`isYB_smul`).
* `hecke_strand`, `braid_strand`, `far_strand` — for every `n`, the generators
  `σ_i = strand g n i` on `V^{⊗n}` satisfy the Hecke quadratic, the braid relation and far
  commutation. **No holonomy is computed for `n ≥ 3`**: the braid relation is categorical.
* `heckeMonodromy_of_DH` — the step-2 class `QOU.Mass.HeckeMonodromy` holds for any Markov-trace
  tower whose generators are the images of these `σ_i` (`BraidedMonodromy`, the Drinfeld–Kohno
  hypothesis), with the shadow field passed separately.

The analytic content of `D_ℏ` (Drinfeld's KZ associator) is already proved in its own files; this
file adds only algebra and category theory. Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv; beans/defs/qou-9634
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open CategoryTheory MonoidalCategory QOU.Mass.BraidedStrands

variable (c : ℂ) [hc : Fact (Transcendental ℚ c)]

/-- The rescaled braiding `g = s · β_{V,V}`, `s = e^{iπℏ/2}`. -/
def gDH : Vd c ⊗ Vd c ⟶ Vd c ⊗ Vd c := sV c • (β_ (Vd c) (Vd c)).hom

/-- **The Hecke quadratic on two strands** in `D_ℏ`: `g² = (q − q⁻¹) g + 1`. -/
theorem g_quad : gDH c ≫ gDH c = (qV c - (qV c)⁻¹) • gDH c + 𝟙 (Vd c ⊗ Vd c) := by
  have h := congrArg (· ≫ gDH c) (hecke_DH c)
  simp only [gDH, Preadditive.sub_comp, Linear.smul_comp, Linear.comp_smul, smul_smul,
    Iso.inv_hom_id, Category.id_comp] at h
  rw [smul_sub, smul_smul, smul_smul, mul_inv_cancel₀ (sV_ne_zero c), one_smul,
    sub_eq_iff_eq_add] at h
  simp only [gDH, Linear.smul_comp, Linear.comp_smul, smul_smul]
  rw [h, mul_comm (sV c)]

/-- `g` satisfies the three-strand (Yang–Baxter) relation. -/
theorem g_isYB : IsYB (gDH c) :=
  isYB_smul (isYB_braiding (Vd c)) (sV c)

/-- **Hecke quadratic on every strand of `V^{⊗n}`.** -/
theorem hecke_strand (n i : ℕ) (h : i + 1 < n) :
    strand (Vd c) (gDH c) n i ≫ strand (Vd c) (gDH c) n i =
      (qV c - (qV c)⁻¹) • strand (Vd c) (gDH c) n i + 𝟙 (tpow (Vd c) n) :=
  strand_quad (g_quad c) n i h

/-- **Braid relation on every `V^{⊗n}`.** -/
theorem braid_strand (n i : ℕ) (h : i + 2 < n) :
    strand (Vd c) (gDH c) n i ≫ strand (Vd c) (gDH c) n (i + 1) ≫ strand (Vd c) (gDH c) n i =
      strand (Vd c) (gDH c) n (i + 1) ≫ strand (Vd c) (gDH c) n i ≫
        strand (Vd c) (gDH c) n (i + 1) :=
  strand_braid (gDH c) (g_isYB c) n i h

/-- **Far commutation on every `V^{⊗n}`.** -/
theorem far_strand (n i j : ℕ) (hij : i + 2 ≤ j) (hj : j + 1 < n) :
    strand (Vd c) (gDH c) n i ≫ strand (Vd c) (gDH c) n j =
      strand (Vd c) (gDH c) n j ≫ strand (Vd c) (gDH c) n i :=
  strand_far (gDH c) n i j hij hj

open QOU.MathlibExt.OcneanuTrace in
/-- **Step 2 from Drinfeld–Kohno alone.** For a Markov-trace tower over `ℂ` whose generators are
the images of the `D_ℏ` braid generators (`BraidedMonodromy`), the step-2 class holds at
`q = e^{iπℏ}`. The only hypothesis besides that is the shadow field (see
`QOU.Mass.HeckeMonodromy.subsingleton_of_ne`). -/
theorem heckeMonodromy_of_DH {A : Type*} [Ring A] [Algebra ℂ A] (T : MarkovTrace ℂ A)
    {B : Type*} [Ring B] (ε : A →+* B) [BraidedMonodromy T (Vd c) (gDH c)]
    (shadow_involution : ∀ i, ε (T.g i) * ε (T.g i) = 1) :
    QOU.Mass.HeckeMonodromy T (qV c) ε :=
  heckeMonodromy_of_braided T (qV c) ε (Vd c) (gDH c) (g_isYB c) (g_quad c) shadow_involution

end QOU.KZ.Drinfeld
