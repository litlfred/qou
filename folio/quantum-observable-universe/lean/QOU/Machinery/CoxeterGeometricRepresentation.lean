/-
# The geometric representation, tier 1 — simply-laced simple-injectivity

The last wall behind the transversal program: the collapsed Tits residue
(#4302) is `σᵢ ≠ σⱼ` per pair, and this file discharges it for every
SIMPLY-LACED Coxeter system (all off-diagonal bond orders in `{2, 3}` —
in particular every type-A tower rung) by constructing the standard
geometric representation:

* **`bilinCoeff`** — the standard-form coefficients
  `B(αᵢ, αⱼ) = −cos(π / mᵢⱼ)` (the `m = ∞` convention `−1` arrives free
  from `π / 0 = 0`); at simply-laced orders these are the EXACT
  rationals `0` (m = 2) and `−1/2` (m = 3), so no Chebyshev
  trigonometry appears anywhere below.
* **`formLin` / `reflEnd`** — the pairing functionals and the
  reflection endomorphisms `v ↦ v − 2⟨αᵢ, v⟩ αᵢ` on `B →₀ ℝ`, with
  `reflEnd_mul_self : reflection² = 1` (no hypotheses at all).
* **`reflEnd_isLiftable_of_simplyLaced`** — the Coxeter relations in
  `Module.End ℝ (B →₀ ℝ)`: commutation at `m = 2` (form value 0), and
  the order-3 relation at `m = 3` by stepwise expansion of the cube
  (the scalar pair `(⟨αᵢ,·⟩, ⟨αⱼ,·⟩)` transforms by an explicit
  rational recursion; the `single`-coefficients cancel by `module`).
* **`geomRep`** — the representation `W →* Module.End ℝ (B →₀ ℝ)` via
  `CoxeterSystem.lift`.
* **`simple_ne_of_simplyLaced`** — THE PAYOFF: `σᵢ ≠ σⱼ` for `i ≠ j`,
  by evaluating the images at the basis vector `αᵢ` and reading the
  `i`-coefficient (`−1` versus `+1`).
* **`braid_unconditional` / `far_commute_unconditional`** — braid and
  far commutation on the length-rule module of ANY simply-laced
  Coxeter system with NO hypothesis: the residue is gone. Supersedes
  the per-system A₃ `decide` instantiation.

HONESTY (STRICT): sorry-free; the simply-laced hypothesis is explicit
(`SimplyLaced M`). General bond orders need the `cos(π/m)` rotation
power identity (Chebyshev) and remain open, stated so. Base ring: `ℝ`
by necessity — the geometric representation is the archimedean
construct; the module payoffs stay generic `[CommRing R]` (§7c).

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.CoxeterTitsResidueCollapse
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.LinearAlgebra.Finsupp.LSum
import Mathlib.Tactic.Module

namespace QOU.Machinery.CoxeterParabolic

open CoxeterSystem List
open QOU.Machinery.HeckeGeneral
open scoped Classical

variable {B : Type*}

/-! ## The standard form and the reflection endomorphisms -/

/-- Every off-diagonal bond order is 2 or 3. -/
def SimplyLaced (M : CoxeterMatrix B) : Prop :=
  ∀ i j : B, i ≠ j → M i j = 2 ∨ M i j = 3

/-- The standard-form coefficients `B(αᵢ, αⱼ) = −cos(π / mᵢⱼ)`; the
diagonal is 1, and `m = 0` (infinite order) yields `−cos 0 = −1` from
the `π / 0 = 0` convention. -/
noncomputable def bilinCoeff (M : CoxeterMatrix B) (i j : B) : ℝ :=
  if i = j then 1 else -Real.cos (Real.pi / M i j)

lemma bilinCoeff_diag (M : CoxeterMatrix B) (i : B) :
    bilinCoeff M i i = 1 := if_pos rfl

lemma bilinCoeff_symm (M : CoxeterMatrix B) (i j : B) :
    bilinCoeff M i j = bilinCoeff M j i := by
  unfold bilinCoeff
  by_cases h : i = j
  · subst h; rfl
  · rw [if_neg h, if_neg (Ne.symm h), M.symmetric]

lemma bilinCoeff_of_eq_two {M : CoxeterMatrix B} {i j : B}
    (hne : i ≠ j) (hm : M i j = 2) : bilinCoeff M i j = 0 := by
  unfold bilinCoeff
  rw [if_neg hne, hm]
  norm_num [Real.cos_pi_div_two]

lemma bilinCoeff_of_eq_three {M : CoxeterMatrix B} {i j : B}
    (hne : i ≠ j) (hm : M i j = 3) : bilinCoeff M i j = -(1 / 2) := by
  unfold bilinCoeff
  rw [if_neg hne, hm]
  norm_num [Real.cos_pi_div_three]

/-- The pairing functional `⟨αᵢ, ·⟩` as a linear map. -/
noncomputable def formLin (M : CoxeterMatrix B) (i : B) :
    (B →₀ ℝ) →ₗ[ℝ] ℝ :=
  Finsupp.lsum ℝ (fun j => bilinCoeff M i j • (LinearMap.id : ℝ →ₗ[ℝ] ℝ))

lemma formLin_single (M : CoxeterMatrix B) (i j : B) (c : ℝ) :
    formLin M i (Finsupp.single j c) = bilinCoeff M i j * c := by
  simp [formLin, mul_comm]

/-- The reflection endomorphism `v ↦ v − 2⟨αᵢ, v⟩ αᵢ`. -/
noncomputable def reflEnd (M : CoxeterMatrix B) (i : B) :
    Module.End ℝ (B →₀ ℝ) :=
  LinearMap.id - (2 : ℝ) • ((Finsupp.lsingle i).comp (formLin M i))

lemma reflEnd_apply (M : CoxeterMatrix B) (i : B) (v : B →₀ ℝ) :
    reflEnd M i v = v - Finsupp.single i (2 * formLin M i v) := by
  unfold reflEnd
  rw [LinearMap.sub_apply, LinearMap.smul_apply, LinearMap.comp_apply,
    LinearMap.id_apply, Finsupp.lsingle_apply, Finsupp.smul_single,
    smul_eq_mul]

/-- `⟨αᵢ, reflection of v⟩ = −⟨αᵢ, v⟩`. -/
lemma formLin_reflEnd_self (M : CoxeterMatrix B) (i : B) (v : B →₀ ℝ) :
    formLin M i (reflEnd M i v) = -(formLin M i v) := by
  rw [reflEnd_apply, map_sub, formLin_single, bilinCoeff_diag]
  ring

/-- The reflections are involutions. -/
lemma reflEnd_mul_self (M : CoxeterMatrix B) (i : B) :
    reflEnd M i * reflEnd M i = 1 := by
  apply LinearMap.ext
  intro v
  show reflEnd M i (reflEnd M i v) = v
  rw [reflEnd_apply M i (reflEnd M i v), formLin_reflEnd_self,
    reflEnd_apply, mul_neg, Finsupp.single_neg]
  abel

/-! ## The Coxeter relations at simply-laced orders -/

variable {M : CoxeterMatrix B}

/-- Commutation of the reflections at `m = 2` (orthogonal roots). -/
lemma reflEnd_comm_of_eq_two {i j : B} (hne : i ≠ j) (hm : M i j = 2) :
    reflEnd M i * reflEnd M j = reflEnd M j * reflEnd M i := by
  have hc : bilinCoeff M i j = 0 := bilinCoeff_of_eq_two hne hm
  have hc' : bilinCoeff M j i = 0 := by rw [← bilinCoeff_symm]; exact hc
  apply LinearMap.ext
  intro v
  show reflEnd M i (reflEnd M j v) = reflEnd M j (reflEnd M i v)
  rw [reflEnd_apply M j v, reflEnd_apply M i (v - _), map_sub,
    formLin_single, hc, zero_mul, sub_zero,
    reflEnd_apply M i v, reflEnd_apply M j (v - _), map_sub,
    formLin_single, hc', zero_mul, sub_zero]
  abel

/-- The order-3 relation at `m = 3`, by stepwise expansion of the cube
with the exact form value `−1/2`. -/
lemma reflEnd_braid_of_eq_three {i j : B} (hne : i ≠ j) (hm : M i j = 3) :
    (reflEnd M i * reflEnd M j) ^ 3 = 1 := by
  have hc : bilinCoeff M i j = -(1 / 2) := bilinCoeff_of_eq_three hne hm
  have hc' : bilinCoeff M j i = -(1 / 2) := by
    rw [← bilinCoeff_symm]; exact hc
  set g := reflEnd M i * reflEnd M j with hgdef
  -- the composite action and the scalar recursion
  have hg : ∀ w : B →₀ ℝ, g w
      = w - Finsupp.single j (2 * formLin M j w)
          - Finsupp.single i (2 * (formLin M i w + formLin M j w)) := by
    intro w
    show reflEnd M i (reflEnd M j w) = _
    rw [reflEnd_apply M j w, reflEnd_apply M i (w - _), map_sub,
      formLin_single, hc]
    congr 2
    ring
  have hgi : ∀ w : B →₀ ℝ, formLin M i (g w)
      = -(formLin M i w + formLin M j w) := by
    intro w
    rw [hg, map_sub, map_sub, formLin_single, formLin_single, hc,
      bilinCoeff_diag]
    ring
  have hgj : ∀ w : B →₀ ℝ, formLin M j (g w) = formLin M i w := by
    intro w
    rw [hg, map_sub, map_sub, formLin_single, formLin_single, hc',
      bilinCoeff_diag]
    ring
  apply LinearMap.ext
  intro v
  have h3 : (g ^ 3) v = g (g (g v)) := by
    rw [pow_succ, pow_succ, pow_one]
    rfl
  show (g ^ 3) v = v
  rw [h3]
  set a := formLin M i v with ha
  set b := formLin M j v with hb
  have e1 : g v
      = v - Finsupp.single j (2 * b) - Finsupp.single i (2 * (a + b)) :=
    hg v
  have ei1 : formLin M i (g v) = -(a + b) := hgi v
  have ej1 : formLin M j (g v) = a := hgj v
  have e2 : g (g v)
      = g v - Finsupp.single j (2 * a)
          - Finsupp.single i (2 * (-(a + b) + a)) := by
    rw [hg (g v), ej1, ei1]
  have ei2 : formLin M i (g (g v)) = -(-(a + b) + a) := by
    rw [hgi (g v), ei1, ej1]
  have ej2 : formLin M j (g (g v)) = -(a + b) := by
    rw [hgj (g v), ei1]
  have e3 : g (g (g v))
      = g (g v) - Finsupp.single j (2 * -(a + b))
          - Finsupp.single i (2 * (-(-(a + b) + a) + -(a + b))) := by
    rw [hg (g (g v)), ej2, ei2]
  rw [e3, e2, e1]
  have sj : ∀ c : ℝ, (Finsupp.single j c : B →₀ ℝ)
      = c • Finsupp.single j (1 : ℝ) := fun c => by
    rw [Finsupp.smul_single, smul_eq_mul, mul_one]
  have si : ∀ c : ℝ, (Finsupp.single i c : B →₀ ℝ)
      = c • Finsupp.single i (1 : ℝ) := fun c => by
    rw [Finsupp.smul_single, smul_eq_mul, mul_one]
  rw [sj (2 * b), sj (2 * a), sj (2 * -(a + b)), si (2 * (a + b)),
    si (2 * (-(a + b) + a)), si (2 * (-(-(a + b) + a) + -(a + b)))]
  module

/-- **The Coxeter relations hold in the geometric representation** for
every simply-laced matrix. -/
theorem reflEnd_isLiftable_of_simplyLaced (hSL : SimplyLaced M) :
    M.IsLiftable (reflEnd M) := by
  intro i j
  by_cases hij : i = j
  · subst hij
    rw [M.diagonal, pow_one, reflEnd_mul_self]
  · rcases hSL i j hij with hm | hm
    · rw [hm]
      have hcomm : Commute (reflEnd M i) (reflEnd M j) :=
        reflEnd_comm_of_eq_two hij hm
      rw [hcomm.mul_pow, pow_two, pow_two, reflEnd_mul_self,
        reflEnd_mul_self, one_mul]
    · rw [hm]
      exact reflEnd_braid_of_eq_three hij hm

/-! ## The representation and the payoff -/

variable {W : Type*} [Group W] (cs : CoxeterSystem M W)

/-- The geometric representation of a simply-laced Coxeter system. -/
noncomputable def geomRep (hSL : SimplyLaced M) :
    W →* Module.End ℝ (B →₀ ℝ) :=
  cs.lift ⟨reflEnd M, reflEnd_isLiftable_of_simplyLaced hSL⟩

@[simp] lemma geomRep_simple (hSL : SimplyLaced M) (i : B) :
    geomRep cs hSL (cs.simple i) = reflEnd M i :=
  cs.lift_apply_simple (reflEnd_isLiftable_of_simplyLaced hSL) i

/-- **THE TITS RESIDUE, DISCHARGED (simply-laced)**: distinct generators
have distinct simple reflections — read off the `i`-coefficient of the
images of the basis vector `αᵢ`. -/
theorem simple_ne_of_simplyLaced (hSL : SimplyLaced M) {i j : B}
    (hij : i ≠ j) : cs.simple i ≠ cs.simple j := by
  intro h
  have happ := congrArg (geomRep cs hSL) h
  rw [geomRep_simple, geomRep_simple] at happ
  have hv := congrArg
    (fun F : Module.End ℝ (B →₀ ℝ) => (F (Finsupp.single i 1)) i) happ
  simp only [reflEnd_apply, formLin_single, bilinCoeff_diag,
    Finsupp.sub_apply, Finsupp.single_eq_same] at hv
  rw [Finsupp.single_eq_of_ne hij] at hv
  norm_num at hv

/-- **Braid at every simply-laced system, UNCONDITIONAL.** -/
theorem braid_unconditional {R : Type*} [CommRing R]
    (hSL : SimplyLaced M) {i j : B} (hm : M i j = 3) (h : R) (v : W → R) :
    letI hne := simple_ne_of_simplyLaced cs hSL
      (fun he => by subst he; exact absurd (M.diagonal i ▸ hm) (by norm_num))
    mulStep (dihedralTransversal' cs i j hm hne).Di h
        (mulStep (dihedralTransversal' cs i j hm hne).Dj h
          (mulStep (dihedralTransversal' cs i j hm hne).Di h v))
      = mulStep (dihedralTransversal' cs i j hm hne).Dj h
          (mulStep (dihedralTransversal' cs i j hm hne).Di h
            (mulStep (dihedralTransversal' cs i j hm hne).Dj h v)) :=
  DihedralCosetStructure.braid_of_dihedral _ h v

/-- **Far commutation at every simply-laced system, UNCONDITIONAL.** -/
theorem far_commute_unconditional {R : Type*} [CommRing R]
    (hSL : SimplyLaced M) {i j : B} (hm : M i j = 2) (h : R) (v : W → R) :
    letI hne := simple_ne_of_simplyLaced cs hSL
      (fun he => by subst he; exact absurd (M.diagonal i ▸ hm) (by norm_num))
    mulStep (commutingTransversal' cs i j hm hne).Di h
        (mulStep (commutingTransversal' cs i j hm hne).Dj h v)
      = mulStep (commutingTransversal' cs i j hm hne).Dj h
          (mulStep (commutingTransversal' cs i j hm hne).Di h v) :=
  CommutingCosetStructure.far_commute_of_commuting _ h v

end QOU.Machinery.CoxeterParabolic
