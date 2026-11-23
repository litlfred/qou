import QOU.Mass.HeckeMonodromy
import QOU.SchurWeyl.MarkovTraceDescent
import QOU.SchurWeyl.MarkovTraceInstance
import QOU.SchurWeyl.HeckeColimitFamilyTrace
import Mathlib.RingTheory.Localization.Away.Basic
import Mathlib.RingTheory.Localization.FractionRing

/-!
# `HeckeMonodromy` on the convention-D Hecke tower over `ℤ[q, q⁻¹, (q²+1)⁻¹]`

The only instance of `QOU.Mass.HeckeMonodromy` before this file was the rank-one
`HeckeMonodromy.LaurentModel`. This file gives one on the real tower: the whole Iwahori–Hecke
colimit `H_∞(q)` over the ring `R = ℤ[q, q⁻¹, (q²+1)⁻¹]`, carrying the convention-D Ocneanu
Markov trace `z_D = q³/(q²+1)`, with shadow `ε : H_∞(q) → ℤ[1/2]` lying over `q ↦ 1`.

* `R` is the smallest localisation of `ℤ[q, q⁻¹]` in which `z_D` exists. It is a domain, and
  `q ↦ 1` extends to `R → ℤ[1/2]` because `q² + 1 ↦ 2`.
* `traceR`: the seminormal (Ocneanu) trace is built over the fraction field `K` of `R`
  (`SeminormalRep.ocneanuMarkovTrace`, which needs `q` generic; here `q` is transcendental), and
  `MarkovTraceFamily.descend` shows its values lie in `R`. Nothing is assumed about the values.
* `tower`: that family on the Hecke colimit, by `ocneanuMarkovTraceAt`.
* `ε`: each level `H_n(q) → ℤ[1/2]` sends every generator to `1` (the trivial representation at
  `q = 1`), glued by the universal property of the colimit.
* `heckeMonodromy`: the four class fields are the colimit relations `gLim_quadratic`,
  `gLim_braid`, `gLim_far`, and `ε(q) = 1`. The shadow ring `ℤ[1/2]` is nonzero
  (`shadow_nontrivial`), so `subsingleton_of_isUnit_h` does not bite: `q − q⁻¹` is not a unit of `R`.

**What this does NOT do.** It does not say that the substrate connection's monodromy *is* this
tower; the class is still the Step-2 conjecture, and this is a model of it that uses the actual
Hecke tower and the actual convention-D trace rather than a rank-one stand-in. No numerical value
of `q` enters.

Base ring §7c: everything is over commutative rings built from `ℤ`; nothing archimedean.
-/

namespace QOU.Mass.LaurentHecke

open LaurentPolynomial QOU.SchurWeyl

/-- The Laurent ring `ℤ[q, q⁻¹]`. -/
abbrev L : Type := LaurentPolynomial ℤ

/-- The element `q² + 1` of `ℤ[q, q⁻¹]`. -/
noncomputable abbrev d : L := T 2 + 1

/-- Evaluation of `ℤ[q, q⁻¹]` at `q = 1`. -/
noncomputable def evalOne : L →+* ℤ := eval₂ (RingHom.id ℤ) 1

theorem evalOne_T (n : ℤ) : evalOne (T n) = 1 := by simp [evalOne, eval₂_T]

theorem evalOne_d : evalOne d = 2 := by
  simp only [d, map_add, map_one, evalOne_T]; norm_num

theorem d_ne_zero : d ≠ 0 := by
  intro h
  have := evalOne_d
  rw [h, map_zero] at this
  norm_num at this

/-- The base ring `R = ℤ[q, q⁻¹, (q² + 1)⁻¹]`. -/
abbrev R : Type := Localization.Away d

instance : IsDomain R :=
  IsLocalization.isDomain_localization (powers_le_nonZeroDivisors_of_noZeroDivisors d_ne_zero)

theorem algebraMap_injective : Function.Injective (algebraMap L R) :=
  IsLocalization.injective R (powers_le_nonZeroDivisors_of_noZeroDivisors d_ne_zero)

/-- The shadow ring `ℤ[1/2]`. -/
abbrev B : Type := Localization.Away (2 : ℤ)

instance : IsDomain B :=
  IsLocalization.isDomain_localization
    (powers_le_nonZeroDivisors_of_noZeroDivisors (by norm_num : (2 : ℤ) ≠ 0))

/-- The shadow `q ↦ 1` on the base: `ℤ[q, q⁻¹, (q²+1)⁻¹] → ℤ[1/2]`. Well defined because
`q² + 1 ↦ 2`, a unit of `ℤ[1/2]`. -/
noncomputable def εR : R →+* B :=
  IsLocalization.Away.lift d (g := (algebraMap ℤ B).comp evalOne) (by
    rw [RingHom.comp_apply, evalOne_d]
    exact IsLocalization.Away.algebraMap_isUnit 2)

theorem εR_algebraMap (a : L) : εR (algebraMap L R a) = algebraMap ℤ B (evalOne a) :=
  IsLocalization.Away.lift_eq d _ a

/-- The deformation parameter `q`, a unit of `R`. -/
noncomputable def qU : Rˣ :=
  ⟨algebraMap L R (T 1), algebraMap L R (T (-1)),
    by rw [← map_mul, ← T_add]; simp, by rw [← map_mul, ← T_add]; simp⟩

theorem qU_val : ((qU : Rˣ) : R) = algebraMap L R (T 1) := rfl
theorem qU_inv : ((qU⁻¹ : Rˣ) : R) = algebraMap L R (T (-1)) := rfl

theorem εR_q : εR (qU : R) = 1 := by rw [qU_val, εR_algebraMap, evalOne_T, map_one]
theorem εR_qinv : εR ((qU⁻¹ : Rˣ) : R) = 1 := by rw [qU_inv, εR_algebraMap, evalOne_T, map_one]

theorem q_mul_qinv : (qU : R) * ((qU⁻¹ : Rˣ) : R) = 1 := Units.mul_inv qU

/-- The convention-D Markov parameter `z_D = q³ / (q² + 1)`, an element of `R`. -/
noncomputable def zD : R := algebraMap L R (T 3) * IsLocalization.Away.invSelf d

theorem qpow (m : ℕ) : (qU : R) ^ m = algebraMap L R (T m) := by
  rw [qU_val, ← map_pow, T_pow]; simp

theorem q_sq_add_one : (qU : R) ^ 2 + 1 = algebraMap L R d := by
  rw [qpow]; simp [d]

theorem q_pow_eq_one {m : ℕ} (h : (qU : R) ^ m = 1) : m = 0 := by
  rw [qpow, ← map_one (algebraMap L R)] at h
  have h' : (T (m : ℤ) : L) = T 0 := by rw [T_zero]; exact algebraMap_injective h
  have := (Finsupp.single_left_inj (one_ne_zero (α := ℤ))).mp h'
  exact_mod_cast this

/-! ## The convention-D trace over `R`, by descent from the fraction field -/

open HeckeCoset

/-- The fraction field of `R`, where the seminormal (Ocneanu) trace is built. -/
abbrev K : Type := FractionRing R

theorem φ_injective : Function.Injective (algebraMap R K) := IsFractionRing.injective R K

/-- `q` in the fraction field. -/
noncomputable abbrev qK : K := algebraMap R K (qU : R)

theorem qK_ne_zero : qK ≠ 0 := by
  intro h
  have : (qU : R) = 0 := φ_injective (h.trans (map_zero _).symm)
  exact qU.ne_zero this

theorem qK_notRootOfUnity : GenericParameter.NotRootOfUnity qK := by
  intro m hm h
  have h' : (qU : R) ^ m = 1 := φ_injective (by rw [map_pow, h, map_one])
  exact (Nat.pos_iff_ne_zero.mp hm) (q_pow_eq_one h')

theorem d_isUnit : IsUnit (algebraMap L R d) := IsLocalization.Away.algebraMap_isUnit d

theorem qK_sq_add_one : qK ^ 2 + 1 = algebraMap R K (algebraMap L R d) := by
  rw [← q_sq_add_one, map_add, map_pow, map_one]

theorem qK_sq_add_one_ne_zero : qK ^ 2 + 1 ≠ 0 := by
  rw [qK_sq_add_one]
  intro h
  exact d_isUnit.ne_zero (φ_injective (by rw [h, map_zero]))

theorem qK_gen : ∀ i : ℕ, 0 < i → (qK ^ 2 : K) ^ i ≠ 1 := by
  intro i hi
  rw [← pow_mul]
  exact qK_notRootOfUnity (2 * i) (by omega)

theorem φ_qinv : algebraMap R K ((qU⁻¹ : Rˣ) : R) = qK⁻¹ := by
  refine eq_inv_of_mul_eq_one_right ?_
  rw [← map_mul, q_mul_qinv, map_one]

theorem φ_zD : algebraMap R K zD = qK ^ 3 / (qK ^ 2 + 1) := by
  have hinv : algebraMap R K (IsLocalization.Away.invSelf d) = (qK ^ 2 + 1)⁻¹ := by
    refine eq_inv_of_mul_eq_one_right ?_
    rw [qK_sq_add_one, ← map_mul, IsLocalization.Away.mul_invSelf, map_one]
  have h3 : algebraMap L R (T 3) = (qU : R) ^ 3 := by rw [qpow]; rfl
  rw [zD, map_mul, hinv, div_eq_mul_inv, h3, map_pow]

/-- Rename the parameters of a Markov trace family along equalities. -/
def MarkovTraceFamily.recast {F : Type*} [CommRing F] {q qi z qi' z' : F} (h1 : qi = qi')
    (h2 : z = z') (U : MarkovTraceFamily F q qi z) : MarkovTraceFamily F q qi' z' := by
  subst h1; subst h2; exact U

/-- The Ocneanu (convention-D) Markov trace family over the fraction field, with its
parameters written as images of `q, q⁻¹, z_D ∈ R`. -/
noncomputable def traceK :
    MarkovTraceFamily K qK (algebraMap R K ((qU⁻¹ : Rˣ) : R)) (algebraMap R K zD) :=
  MarkovTraceFamily.recast φ_qinv.symm φ_zD.symm
    (SeminormalRep.ocneanuMarkovTrace qK qK_ne_zero qK_notRootOfUnity qK_sq_add_one_ne_zero qK_gen)

/-- **The convention-D Markov trace takes values in `R`.** The Ocneanu trace on the Hecke tower
over `ℤ[q, q⁻¹, (q²+1)⁻¹]`, descended from the fraction field. -/
noncomputable def traceR : MarkovTraceFamily R (qU : R) ((qU⁻¹ : Rˣ) : R) zD :=
  traceK.descend φ_injective

/-! ## The Markov-trace tower over `R` and its shadow -/

open HeckeColimit HeckeColimitFamilyTrace HeckeDirectedSystem QOU.MathlibExt.OcneanuTrace

/-- The Hecke colimit over `R`. -/
abbrev A : Type := HeckeLim R (qU : R) ((qU⁻¹ : Rˣ) : R)

/-- **The tower.** The convention-D Markov trace on the whole Hecke tower over `R`. -/
noncomputable def tower : MarkovTrace R A := ocneanuMarkovTraceAt traceR q_mul_qinv

theorem tower_z : tower.z = zD := rfl

/-- `B` as an `R`-algebra through the shadow `εR`. -/
noncomputable instance algRB : Algebra R B := εR.toAlgebra

theorem algebraMap_RB (r : R) : algebraMap R B r = εR r := rfl

/-- The shadow at level `n`: every generator goes to `1` (the trivial representation at `q = 1`). -/
noncomputable def εLevel (n : ℕ) : Hecke R (qU : R) ((qU⁻¹ : Rˣ) : R) n →ₐ[R] B :=
  Hecke.lift R (qU : R) ((qU⁻¹ : Rˣ) : R) n (fun _ => 1)
    (fun _ => by rw [Algebra.smul_def, Algebra.smul_def, algebraMap_RB, algebraMap_RB,
        map_sub, map_mul, εR_q, εR_qinv]; ring)
    (fun _ _ => rfl) (fun _ _ _ => rfl)

theorem εLevel_compat (i j : ℕ) (hij : i ≤ j) (x : Hecke R (qU : R) ((qU⁻¹ : Rˣ) : R) i) :
    εLevel j (heckeInclLE R (qU : R) ((qU⁻¹ : Rˣ) : R) i j hij x) = εLevel i x := by
  have h : (εLevel j).comp (heckeInclLE R (qU : R) ((qU⁻¹ : Rˣ) : R) i j hij) = εLevel i := by
    apply Hecke.hom_ext
    intro m
    rw [AlgHom.comp_apply]
    obtain ⟨m, hm⟩ := m
    rw [heckeInclLE_σ R (qU : R) ((qU⁻¹ : Rˣ) : R) i j hij m hm]
    simp only [εLevel, Hecke.lift_σ]
  exact congrArg (fun f => f x) h

/-- **The shadow** `ε : A → ℤ[1/2]`, the specialisation `q ↦ 1` of the whole tower. -/
noncomputable def ε : A →+* B :=
  DirectLimit.Ring.lift _ _ B (fun n => (εLevel n : _ →+* B)) εLevel_compat

theorem ε_algebraMap (r : R) : ε (algebraMap R A r) = εR r := by
  rw [← (ofLimₐ R (qU : R) ((qU⁻¹ : Rˣ) : R) 0).commutes r, ofLimₐ_apply]
  show εLevel 0 (algebraMap R _ r) = εR r
  rw [AlgHom.commutes]; rfl

/-- **Step 2 holds on the convention-D Hecke tower over `ℤ[q, q⁻¹, (q²+1)⁻¹]`.** The Ocneanu
Markov trace tower carries a `HeckeMonodromy` instance whose shadow is `q ↦ 1` into `ℤ[1/2]`. -/
instance heckeMonodromy : HeckeMonodromy tower qU ε where
  quad i := by
    have h := gLim_quadratic R (qU : R) ((qU⁻¹ : Rˣ) : R) i
    rw [q_mul_qinv, one_smul] at h
    exact h
  braid i := (gLim_braid R (qU : R) ((qU⁻¹ : Rˣ) : R) i).symm
  far_comm i j hij := (gLim_far R (qU : R) ((qU⁻¹ : Rˣ) : R) j i (by omega)).symm
  shadow_at_one := by rw [ε_algebraMap, εR_q]

/-- The shadow ring is not zero. -/
theorem shadow_nontrivial : Nontrivial B := inferInstance

/-- The shadow of every generator is `1`. -/
theorem ε_g (i : ℕ) : ε (tower.g i) = 1 := by
  show εLevel (i + 1) _ = 1
  simp only [εLevel, Hecke.lift_σ]

end QOU.Mass.LaurentHecke
