import QOU.KZ.Drinfeld.RibbonDH
import QOU.Mass.BraidedStrands

/-!
# The Drinfeld category `D_ℏ` gives a Hecke action on `V^{⊗n}` for every `n`

Bridge A, step A4 (`QOU.Mass.BraidedStrands`), applied to the braided `ℂ`-linear category
`D_ℏ` of bean `qou-zoyv`, over any Drinfeld associator `Ψ` (`QOU.KZ.Drinfeld.Braided`,
`QOU.KZ.Drinfeld.Linear`). Here
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
  tower over a ring `R` whose generators are the images of these `σ_i` (`BraidedMonodromy`, the
  Drinfeld–Kohno hypothesis), with the `q ↦ 1` shadow passed separately.
* `heckeMonodromy_shadow_trivial` — at one fixed `ℏ` that shadow is necessarily the zero ring: the
  classical shadow is a statement about the family over `ℏ`, which this file does not construct.

The analytic content of `D_ℏ` (Drinfeld's KZ associator) is already proved in its own files; this
file adds only algebra and category theory. Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv; beans/defs/qou-9634
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open QOU.KZ.DrinfeldAssociator CategoryTheory MonoidalCategory QOU.Mass.BraidedStrands

variable (Ψ : Associator.{0}) (c : ℂ) [hc : Fact (Transcendental ℚ c)]

/-- The rescaled braiding `g = s · β_{V,V}`, `s = e^{iπℏ/2}`. -/
def gDH : Vd Ψ c ⊗ Vd Ψ c ⟶ Vd Ψ c ⊗ Vd Ψ c := sV c • (β_ (Vd Ψ c) (Vd Ψ c)).hom

/-- **The Hecke quadratic on two strands** in `D_ℏ`: `g² = (q − q⁻¹) g + 1`. -/
theorem g_quad : gDH Ψ c ≫ gDH Ψ c = (qV c - (qV c)⁻¹) • gDH Ψ c + 𝟙 (Vd Ψ c ⊗ Vd Ψ c) := by
  have h := congrArg (· ≫ gDH Ψ c) (hecke_DH Ψ c)
  simp only [gDH, Preadditive.sub_comp, Linear.smul_comp, Linear.comp_smul, smul_smul,
    Iso.inv_hom_id, Category.id_comp] at h
  rw [smul_sub, smul_smul, smul_smul, mul_inv_cancel₀ (sV_ne_zero c), one_smul,
    sub_eq_iff_eq_add] at h
  simp only [gDH, Linear.smul_comp, Linear.comp_smul, smul_smul]
  rw [h, mul_comm (sV c)]

/-- `g` satisfies the three-strand (Yang–Baxter) relation. -/
theorem g_isYB : IsYB (gDH Ψ c) :=
  isYB_smul (isYB_braiding (Vd Ψ c)) (sV c)

/-- **Hecke quadratic on every strand of `V^{⊗n}`.** -/
theorem hecke_strand (n i : ℕ) (h : i + 1 < n) :
    strand (Vd Ψ c) (gDH Ψ c) n i ≫ strand (Vd Ψ c) (gDH Ψ c) n i =
      (qV c - (qV c)⁻¹) • strand (Vd Ψ c) (gDH Ψ c) n i + 𝟙 (tpow (Vd Ψ c) n) :=
  strand_quad (g_quad Ψ c) n i h

/-- **Braid relation on every `V^{⊗n}`.** -/
theorem braid_strand (n i : ℕ) (h : i + 2 < n) :
    strand (Vd Ψ c) (gDH Ψ c) n i ≫ strand (Vd Ψ c) (gDH Ψ c) n (i + 1) ≫ strand (Vd Ψ c) (gDH Ψ c) n i =
      strand (Vd Ψ c) (gDH Ψ c) n (i + 1) ≫ strand (Vd Ψ c) (gDH Ψ c) n i ≫
        strand (Vd Ψ c) (gDH Ψ c) n (i + 1) :=
  strand_braid (gDH Ψ c) (g_isYB Ψ c) n i h

/-- **Far commutation on every `V^{⊗n}`.** -/
theorem far_strand (n i j : ℕ) (hij : i + 2 ≤ j) (hj : j + 1 < n) :
    strand (Vd Ψ c) (gDH Ψ c) n i ≫ strand (Vd Ψ c) (gDH Ψ c) n j =
      strand (Vd Ψ c) (gDH Ψ c) n j ≫ strand (Vd Ψ c) (gDH Ψ c) n i :=
  strand_far (gDH Ψ c) n i j hij hj

open QOU.MathlibExt.OcneanuTrace in
/-- **Step 2 from Drinfeld–Kohno alone.** For a Markov-trace tower over a commutative ring `R`,
with `q : Rˣ` mapped to `q = e^{iπℏ}` by `φ : R → ℂ`, whose generators are the images of the
`D_ℏ` braid generators (`BraidedMonodromy`), the step-2 class holds for any shadow `ε` lying over
`q ↦ 1`. By `heckeMonodromy_shadow_trivial` that shadow is necessarily zero when the monodromy
factors through `D_ℏ` at one fixed `ℏ`: the shadow needs the family in `ℏ`. -/
theorem heckeMonodromy_of_DH {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
    (T : MarkovTrace R A) (q : Rˣ) (φ : R →+* ℂ) (hφ : φ q = qV c) {B : Type*} [Ring B]
    (ε : A →+* B) [BraidedMonodromy T φ (Vd Ψ c) (gDH Ψ c)]
    (shadow_at_one : ε (algebraMap R A q) = 1) :
    QOU.Mass.HeckeMonodromy T q ε := by
  have hinv : φ ↑q⁻¹ = (qV c)⁻¹ := by rw [map_units_inv, hφ]
  refine heckeMonodromy_of_braided T q φ ε (Vd Ψ c) (gDH Ψ c) (g_isYB Ψ c) ?_ shadow_at_one
  rw [hφ, hinv]
  exact g_quad Ψ c

open QOU.MathlibExt.OcneanuTrace in
/-- **At fixed `ℏ` the shadow is zero.** Since `q = e^{iπℏ} ≠ 1` for transcendental `ℏ`
(`qV_sub_inv_ne_zero`), a tower whose monodromy factors through `D_ℏ` has only the zero ring as a
`q ↦ 1` shadow (`subsingleton_of_fixed_coupling`). The classical shadow is a statement about the
family over the coupling, not about one `D_ℏ`. -/
theorem heckeMonodromy_shadow_trivial {R : Type*} [CommRing R] {A : Type*} [Ring A]
    [Algebra R A] (T : MarkovTrace R A) (q : Rˣ) (φ : R →+* ℂ) (hφ : φ q = qV c) {B : Type*}
    [Ring B] (ε : A →+* B) [BraidedMonodromy T φ (Vd Ψ c) (gDH Ψ c)]
    [QOU.Mass.HeckeMonodromy T q ε] : Subsingleton B := by
  refine subsingleton_of_fixed_coupling T q φ ε (Vd Ψ c) (gDH Ψ c) ?_
  rw [hφ]
  intro h1
  apply qV_sub_inv_ne_zero c hc.out
  rw [h1, inv_one, sub_self]

end QOU.KZ.Drinfeld
