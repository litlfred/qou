import Mathlib.LinearAlgebra.Matrix.SpecialLinearGroup
import Mathlib.LinearAlgebra.UnitaryGroup
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Analysis.SpecialFunctions.Complex.Arg
import Mathlib.GroupTheory.QuotientGroup.Basic
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic

set_option autoImplicit false

/-!
# `S(U(3) × U(2)) ≃* (SU(3) × SU(2) × U(1)) ⧸ ℤ₆` and the Parameterized `𝔰𝔲(3) ⊕ 𝔰𝔲(2)` Commutant Trace Ratio (`qou-txc1`)

Pure-mathematics formalization (`0 sorry`, `0 axiom`) of the re-scoped `qou-txc1` targets
(`owner-rulings.md` row 43, `2026-11-21` math-only rescope + `2026-11-22` parameterization review):

1. **Section 1 — Exact Group Isomorphism `(SU(3) × SU(2) × U(1)) ⧸ ker φ ≃* S(U(3) × U(2))` with `ker φ ≃* ℤ/6ℤ`:**
   - Defines `SU3xU2Subgroup ≤ unitaryGroup (Fin 3) ℂ × unitaryGroup (Fin 2) ℂ` (`det A * det B = 1`).
   - Constructs the Baez–Huerta covering homomorphism
     `smCoverHom : (SU(3) × SU(2) × U(1)) →* S(U(3) × U(2))` sending
     `(g₃, g₂, u) ↦ ((u² • I₃) g₃, (u⁻³ • I₂) g₂)`.
   - Characterizes `ker smCoverHom` (`mem_ker_smCoverHom_iff`) as the subgroup of triples
     `((u⁻² • I₃), (u³ • I₂), u)` with `u⁶ = 1`, proves the group isomorphisms
     `kerSmCoverEquivRoots6 : ↥smCoverHom.ker ≃* ↥rootsOfUnity6Circle` and
     `kerSmCoverEquivZMod6 : ↥smCoverHom.ker ≃* Multiplicative (ZMod 6)` (exact order `6`),
     proves surjectivity `smCoverHom_surjective`, and applies the First Isomorphism Theorem to
     obtain `smQuotientZ6EquivSU3xU2`.

2. **Section 2 — Commutant of `𝔰𝔩₃(K) ⊕ 𝔰𝔩₂(K)` in `𝔰𝔩₅(K)` and Parameterized Trace Ratio on `5̄ ⊕ 10`:**
   - Over any `[Field K] [CharZero K]` (`AGENTS.md` §7c), proves that the traceless commutant of
     `sl3_oplus_sl2 K` inside `Matrix (Fin 5) (Fin 5) K` is strictly 1-dimensional, spanned by
     `Y0 K = diag(-2, -2, -2, 3, 3)` (`mem_traceless_commutant_sl3_sl2_iff`).
   - Leaving the commutant normalization `α : K` as an **explicit free parameter** per the
     `2026-11-22` quark-charge derivation ruling (`Q5 α = T3 K + α • Y0 K`), evaluates the
     exact quadratic traces on `5`, `5̄`, and `10 = Λ²(5)`, proving the Dynkin proportionality
     `tr10_Q_sq α = 3 * tr5_Q_sq α` and the parameterized trace ratio on `5̄ ⊕ 10`:
     `tr5bar10_T3_sq K / tr5bar10_Q_sq α = 1 / (1 + 60 * α ^ 2)`,
     which equals `3 / 8` if and only if `α ^ 2 = 1 / 36` (`α = ±1/6`).

3. **Section 3 — part (c):** the former carrier `BringKummerSU5EmbeddingHypothesis` was satisfied
   by `α = 1/6` and is retired (2026-11-27).  Part (c) is now the flavour `W` construction,
   bean `qou-j3w6`.

-- Ref: [baez-huerta2010] Baez & Huerta, Bull. Amer. Math. Soc. 47 (2010) 483–552, Theorem 1.
-/

namespace QOU.StandardModel.Su3Su2U1Z6GroupAndCommutant

open Matrix

/-! ## Section 1: Exact Group Isomorphism `(SU(3) × SU(2) × U(1)) ⧸ ℤ₆ ≃* S(U(3) × U(2))` -/

section BaezHuertaGroupIso

abbrev U3C : Type := ↥(Matrix.unitaryGroup (Fin 3) ℂ)
abbrev U2C : Type := ↥(Matrix.unitaryGroup (Fin 2) ℂ)
abbrev SU3C : Type := ↥(Matrix.specialUnitaryGroup (Fin 3) ℂ)
abbrev SU2C : Type := ↥(Matrix.specialUnitaryGroup (Fin 2) ℂ)

/-- Inclusion homomorphism `SU(n) →* U(n)` over `ℂ`. -/
def suToU (n : Type*) [Fintype n] [DecidableEq n] :
    ↥(Matrix.specialUnitaryGroup n ℂ) →* ↥(Matrix.unitaryGroup n ℂ) where
  toFun g := ⟨g.1, (Matrix.mem_specialUnitaryGroup_iff.mp g.2).1⟩
  map_one' := rfl
  map_mul' _ _ := rfl

@[simp] theorem coe_suToU {n : Type*} [Fintype n] [DecidableEq n]
    (g : ↥(Matrix.specialUnitaryGroup n ℂ)) :
    ((suToU n g : ↥(Matrix.unitaryGroup n ℂ)) : Matrix n n ℂ) = g.1 := rfl

/-- Central scalar inclusion `U(1) = Circle →* U(n)` sending `u ↦ u • I_n`. -/
def scalarUnitaryHom (n : Type*) [Fintype n] [DecidableEq n] :
    Circle →* ↥(Matrix.unitaryGroup n ℂ) where
  toFun u := ⟨(u : ℂ) • (1 : Matrix n n ℂ), by
    rw [Matrix.mem_unitaryGroup_iff]
    have hu : (u : ℂ) * star (u : ℂ) = 1 := by
      rw [Complex.star_def, Complex.mul_conj, Complex.normSq_eq_norm_sq, Circle.norm_coe]
      norm_num
    rw [Matrix.star_eq_conjTranspose, Matrix.conjTranspose_smul, Matrix.conjTranspose_one,
      Matrix.smul_mul, Matrix.mul_smul, mul_one, smul_smul, hu, one_smul]⟩
  map_one' := by
    apply Subtype.ext
    change ((1 : Circle) : ℂ) • (1 : Matrix n n ℂ) = 1
    simp
  map_mul' u v := by
    apply Subtype.ext
    change (((u * v : Circle) : ℂ) • (1 : Matrix n n ℂ)) =
      ((u : ℂ) • (1 : Matrix n n ℂ)) * ((v : ℂ) • (1 : Matrix n n ℂ))
    rw [Matrix.smul_mul, Matrix.mul_smul, one_mul, smul_smul]
    rfl

@[simp] theorem coe_scalarUnitaryHom {n : Type*} [Fintype n] [DecidableEq n] (u : Circle) :
    ((scalarUnitaryHom n u : ↥(Matrix.unitaryGroup n ℂ)) : Matrix n n ℂ) =
      (u : ℂ) • (1 : Matrix n n ℂ) := rfl

/-- `scalarUnitaryHom n u` lies in the center of `U(n)`. -/
theorem scalarUnitaryHom_mul_comm {n : Type*} [Fintype n] [DecidableEq n]
    (u : Circle) (A : ↥(Matrix.unitaryGroup n ℂ)) :
    scalarUnitaryHom n u * A = A * scalarUnitaryHom n u := by
  apply Subtype.ext
  change ((u : ℂ) • (1 : Matrix n n ℂ)) * A.1 = A.1 * ((u : ℂ) • (1 : Matrix n n ℂ))
  rw [Matrix.smul_mul, Matrix.mul_smul, one_mul, mul_one]

/-- Every unitary matrix `A ∈ U(n)` has `det A ∈ Circle` (`‖det A‖ = 1`). -/
theorem det_mem_unitSphere_of_mem_unitaryGroup {n : Type*} [Fintype n] [DecidableEq n]
    (A : ↥(Matrix.unitaryGroup n ℂ)) :
    (A.1 : Matrix n n ℂ).det ∈ Submonoid.unitSphere ℂ := by
  change (A.1 : Matrix n n ℂ).det ∈ Metric.sphere (0 : ℂ) 1
  rw [mem_sphere_zero_iff_norm]
  have h1 : A.1 * star A.1 = 1 := Matrix.mem_unitaryGroup_iff.mp A.2
  have hstar : (star A.1 : Matrix n n ℂ).det = star (A.1.det) := by
    rw [Matrix.star_eq_conjTranspose, Matrix.det_conjTranspose, Complex.star_def]
  have hdet : A.1.det * star A.1.det = 1 := by
    calc A.1.det * star A.1.det = A.1.det * (star A.1).det := by rw [hstar]
      _ = (A.1 * star A.1).det := (Matrix.det_mul _ _).symm
      _ = 1 := by rw [h1, Matrix.det_one]
  have hnorm := congrArg norm hdet
  rw [norm_mul, norm_star, norm_one] at hnorm
  have hnn : 0 ≤ ‖A.1.det‖ := norm_nonneg A.1.det
  nlinarith

/-- Determinant as a group homomorphism `U(n) →* Circle`. -/
noncomputable def unitaryDetHom (n : Type*) [Fintype n] [DecidableEq n] :
    ↥(Matrix.unitaryGroup n ℂ) →* Circle where
  toFun A := ⟨A.1.det, det_mem_unitSphere_of_mem_unitaryGroup A⟩
  map_one' := by apply Subtype.ext; exact Matrix.det_one
  map_mul' A B := by apply Subtype.ext; exact Matrix.det_mul A.1 B.1

@[simp] theorem coe_unitaryDetHom {n : Type*} [Fintype n] [DecidableEq n]
    (A : ↥(Matrix.unitaryGroup n ℂ)) :
    ((unitaryDetHom n A : Circle) : ℂ) = A.1.det := rfl

/-- The unimodular block-diagonal subgroup `S(U(3) × U(2)) ≤ U(3) × U(2)` cut out by
`det A * det B = 1` (the kernel of `(A, B) ↦ unitaryDetHom A * unitaryDetHom B`). -/
noncomputable def prodDetHom : (U3C × U2C) →* Circle where
  toFun p := unitaryDetHom (Fin 3) p.1 * unitaryDetHom (Fin 2) p.2
  map_one' := by simp
  map_mul' p q := by
    simp only [Prod.fst_mul, Prod.snd_mul, map_mul]
    exact mul_mul_mul_comm _ _ _ _

/-- `S(U(3) × U(2))` as a `Subgroup` of `U(3) × U(2)`. -/
noncomputable def SU3xU2Subgroup : Subgroup (U3C × U2C) := prodDetHom.ker

theorem mem_SU3xU2Subgroup_iff (p : U3C × U2C) :
    p ∈ SU3xU2Subgroup ↔ p.1.1.det * p.2.1.det = 1 := by
  rw [SU3xU2Subgroup, MonoidHom.mem_ker, ← Subtype.coe_inj]
  rfl

/-- Helper: determinant of `scalarUnitaryHom (Fin 3) v * A` is `v³ * det A`. -/
theorem unitaryDet_scalar3_mul (v : Circle) (A : U3C) :
    unitaryDetHom (Fin 3) (scalarUnitaryHom (Fin 3) v * A) = v ^ 3 * unitaryDetHom (Fin 3) A := by
  apply Subtype.ext
  change (((v : ℂ) • (1 : Matrix (Fin 3) (Fin 3) ℂ)) * A.1).det = (v : ℂ) ^ 3 * A.1.det
  rw [Matrix.det_mul, Matrix.det_smul, Fintype.card_fin, Matrix.det_one, mul_one]

/-- Helper: determinant of `scalarUnitaryHom (Fin 2) v * B` is `v² * det B`. -/
theorem unitaryDet_scalar2_mul (v : Circle) (B : U2C) :
    unitaryDetHom (Fin 2) (scalarUnitaryHom (Fin 2) v * B) = v ^ 2 * unitaryDetHom (Fin 2) B := by
  apply Subtype.ext
  change (((v : ℂ) • (1 : Matrix (Fin 2) (Fin 2) ℂ)) * B.1).det = (v : ℂ) ^ 2 * B.1.det
  rw [Matrix.det_mul, Matrix.det_smul, Fintype.card_fin, Matrix.det_one, mul_one]

theorem unitaryDet_suToU {n : Type*} [Fintype n] [DecidableEq n]
    (g : ↥(Matrix.specialUnitaryGroup n ℂ)) :
    unitaryDetHom n (suToU n g) = 1 := by
  apply Subtype.ext
  exact (Matrix.mem_specialUnitaryGroup_iff.mp g.2).2

/-- **The Baez–Huerta covering homomorphism**
`smCoverHom : SU(3) × SU(2) × U(1) →* S(U(3) × U(2))` sending
`(g₃, g₂, u) ↦ ((u² • I₃) g₃, (u⁻³ • I₂) g₂)`. -/
noncomputable def smCoverHom : (SU3C × SU2C × Circle) →* ↥SU3xU2Subgroup where
  toFun x := ⟨(scalarUnitaryHom (Fin 3) (x.2.2 ^ 2) * suToU (Fin 3) x.1,
               scalarUnitaryHom (Fin 2) ((x.2.2 ^ 3)⁻¹) * suToU (Fin 2) x.2.1), by
    rw [SU3xU2Subgroup, MonoidHom.mem_ker]
    change unitaryDetHom (Fin 3) (scalarUnitaryHom (Fin 3) (x.2.2 ^ 2) * suToU (Fin 3) x.1) *
        unitaryDetHom (Fin 2) (scalarUnitaryHom (Fin 2) ((x.2.2 ^ 3)⁻¹) * suToU (Fin 2) x.2.1) = 1
    rw [unitaryDet_scalar3_mul, unitaryDet_scalar2_mul, unitaryDet_suToU, unitaryDet_suToU,
      mul_one, mul_one, ← pow_mul, inv_pow, ← pow_mul]
    exact mul_inv_cancel (x.2.2 ^ 6)⟩
  map_one' := by
    apply Subtype.ext
    ext <;> simp
  map_mul' x y := by
    apply Subtype.ext
    apply Prod.ext
    · change scalarUnitaryHom (Fin 3) ((x.2.2 * y.2.2) ^ 2) * suToU (Fin 3) (x.1 * y.1) =
        (scalarUnitaryHom (Fin 3) (x.2.2 ^ 2) * suToU (Fin 3) x.1) *
          (scalarUnitaryHom (Fin 3) (y.2.2 ^ 2) * suToU (Fin 3) y.1)
      rw [mul_pow, map_mul, map_mul, mul_assoc,
        ← mul_assoc (scalarUnitaryHom (Fin 3) (y.2.2 ^ 2)) (suToU (Fin 3) x.1) (suToU (Fin 3) y.1),
        scalarUnitaryHom_mul_comm (y.2.2 ^ 2) (suToU (Fin 3) x.1)]
      simp only [mul_assoc]
    · change scalarUnitaryHom (Fin 2) (((x.2.2 * y.2.2) ^ 3)⁻¹) * suToU (Fin 2) (x.2.1 * y.2.1) =
        (scalarUnitaryHom (Fin 2) ((x.2.2 ^ 3)⁻¹) * suToU (Fin 2) x.2.1) *
          (scalarUnitaryHom (Fin 2) ((y.2.2 ^ 3)⁻¹) * suToU (Fin 2) y.2.1)
      have hinv : ((x.2.2 * y.2.2) ^ 3)⁻¹ = (x.2.2 ^ 3)⁻¹ * (y.2.2 ^ 3)⁻¹ := by
        rw [mul_pow, mul_inv]
      rw [hinv, map_mul, map_mul, mul_assoc,
        ← mul_assoc (scalarUnitaryHom (Fin 2) ((y.2.2 ^ 3)⁻¹)) (suToU (Fin 2) x.2.1)
          (suToU (Fin 2) y.2.1),
        scalarUnitaryHom_mul_comm ((y.2.2 ^ 3)⁻¹) (suToU (Fin 2) x.2.1)]
      simp only [mul_assoc]

/-- The subgroup `μ₆ ⊆ U(1)` of 6th roots of unity on the unit circle. -/
abbrev rootsOfUnity6Circle : Subgroup Circle := (powMonoidHom 6 : Circle →* Circle).ker

theorem mem_rootsOfUnity6Circle_iff (u : Circle) :
    u ∈ rootsOfUnity6Circle ↔ u ^ 6 = 1 :=
  MonoidHom.mem_ker

/-- **Exact Kernel Characterization of `smCoverHom`:**
`(g₃, g₂, u) ∈ ker smCoverHom` if and only if `u⁶ = 1`, `g₃ = u⁻² • I₃`, and `g₂ = u³ • I₂`. -/
theorem mem_ker_smCoverHom_iff (x : SU3C × SU2C × Circle) :
    x ∈ smCoverHom.ker ↔
      x.2.2 ^ 6 = 1 ∧
      suToU (Fin 3) x.1 = scalarUnitaryHom (Fin 3) ((x.2.2 ^ 2)⁻¹) ∧
      suToU (Fin 2) x.2.1 = scalarUnitaryHom (Fin 2) (x.2.2 ^ 3) := by
  rw [MonoidHom.mem_ker]
  constructor
  · intro hx
    have hp := congrArg Subtype.val hx
    have h1 : scalarUnitaryHom (Fin 3) (x.2.2 ^ 2) * suToU (Fin 3) x.1 = 1 :=
      congrArg Prod.fst hp
    have h2 : scalarUnitaryHom (Fin 2) ((x.2.2 ^ 3)⁻¹) * suToU (Fin 2) x.2.1 = 1 :=
      congrArg Prod.snd hp
    have hg3 : suToU (Fin 3) x.1 = scalarUnitaryHom (Fin 3) ((x.2.2 ^ 2)⁻¹) := by
      calc suToU (Fin 3) x.1
          = (scalarUnitaryHom (Fin 3) (x.2.2 ^ 2))⁻¹ *
              (scalarUnitaryHom (Fin 3) (x.2.2 ^ 2) * suToU (Fin 3) x.1) := by group
        _ = (scalarUnitaryHom (Fin 3) (x.2.2 ^ 2))⁻¹ := by rw [h1, mul_one]
        _ = scalarUnitaryHom (Fin 3) ((x.2.2 ^ 2)⁻¹) := (map_inv _ _).symm
    have hg2 : suToU (Fin 2) x.2.1 = scalarUnitaryHom (Fin 2) (x.2.2 ^ 3) := by
      calc suToU (Fin 2) x.2.1
          = (scalarUnitaryHom (Fin 2) ((x.2.2 ^ 3)⁻¹))⁻¹ *
              (scalarUnitaryHom (Fin 2) ((x.2.2 ^ 3)⁻¹) * suToU (Fin 2) x.2.1) := by group
        _ = (scalarUnitaryHom (Fin 2) ((x.2.2 ^ 3)⁻¹))⁻¹ := by rw [h2, mul_one]
        _ = scalarUnitaryHom (Fin 2) (x.2.2 ^ 3) := by rw [← map_inv, inv_inv]
    have hdet2 : unitaryDetHom (Fin 2) (suToU (Fin 2) x.2.1) = (x.2.2 ^ 3) ^ 2 := by
      have hsc := unitaryDet_scalar2_mul (x.2.2 ^ 3) 1
      rw [mul_one, map_one, mul_one, ← hg2] at hsc
      exact hsc
    rw [unitaryDet_suToU, ← pow_mul] at hdet2
    exact ⟨hdet2.symm, hg3, hg2⟩
  · rintro ⟨hu6, hg3, hg2⟩
    apply Subtype.ext
    apply Prod.ext
    · change scalarUnitaryHom (Fin 3) (x.2.2 ^ 2) * suToU (Fin 3) x.1 = 1
      rw [hg3, ← map_mul, mul_inv_cancel, map_one]
    · change scalarUnitaryHom (Fin 2) ((x.2.2 ^ 3)⁻¹) * suToU (Fin 2) x.2.1 = 1
      rw [hg2, ← map_mul, inv_mul_cancel, map_one]

/-- Helper embedding `ζ ∈ μ₆(Circle)` into `SU(3)` via `ζ⁻² • I₃`. -/
noncomputable def roots6ToSU3 (ζ : ↥rootsOfUnity6Circle) : SU3C :=
  ⟨(scalarUnitaryHom (Fin 3) ((ζ.1 ^ 2)⁻¹)).1, by
    rw [Matrix.mem_specialUnitaryGroup_iff]
    refine ⟨(scalarUnitaryHom (Fin 3) ((ζ.1 ^ 2)⁻¹)).2, ?_⟩
    have hζ6 : ζ.1 ^ 6 = 1 := (mem_rootsOfUnity6Circle_iff ζ.1).mp ζ.2
    have hdet : unitaryDetHom (Fin 3) (scalarUnitaryHom (Fin 3) ((ζ.1 ^ 2)⁻¹)) = 1 := by
      have h := unitaryDet_scalar3_mul ((ζ.1 ^ 2)⁻¹) 1
      rw [mul_one, map_one, mul_one, inv_pow, ← pow_mul, hζ6, inv_one] at h
      exact h
    exact congrArg Subtype.val hdet⟩

/-- Helper embedding `ζ ∈ μ₆(Circle)` into `SU(2)` via `ζ³ • I₂`. -/
noncomputable def roots6ToSU2 (ζ : ↥rootsOfUnity6Circle) : SU2C :=
  ⟨(scalarUnitaryHom (Fin 2) (ζ.1 ^ 3)).1, by
    rw [Matrix.mem_specialUnitaryGroup_iff]
    refine ⟨(scalarUnitaryHom (Fin 2) (ζ.1 ^ 3)).2, ?_⟩
    have hζ6 : ζ.1 ^ 6 = 1 := (mem_rootsOfUnity6Circle_iff ζ.1).mp ζ.2
    have hdet : unitaryDetHom (Fin 2) (scalarUnitaryHom (Fin 2) (ζ.1 ^ 3)) = 1 := by
      have h := unitaryDet_scalar2_mul (ζ.1 ^ 3) 1
      rw [mul_one, map_one, mul_one, ← pow_mul, hζ6] at h
      exact h
    exact congrArg Subtype.val hdet⟩

/-- **Kernel Isomorphism `ker smCoverHom ≃* μ₆(Circle)`:**
The kernel of `SU(3) × SU(2) × U(1) →* S(U(3) × U(2))` is canonically isomorphic as a group
to the 6th roots of unity in `U(1)`. -/
noncomputable def kerSmCoverEquivRoots6 : ↥smCoverHom.ker ≃* ↥rootsOfUnity6Circle where
  toFun x := ⟨x.1.2.2, (mem_rootsOfUnity6Circle_iff x.1.2.2).mpr
    ((mem_ker_smCoverHom_iff x.1).mp x.2).1⟩
  invFun ζ := ⟨(roots6ToSU3 ζ, roots6ToSU2 ζ, ζ.1), by
    rw [mem_ker_smCoverHom_iff]
    exact ⟨(mem_rootsOfUnity6Circle_iff ζ.1).mp ζ.2, rfl, rfl⟩⟩
  left_inv x := by
    rcases x with ⟨⟨g3, g2, u⟩, hx⟩
    rcases (mem_ker_smCoverHom_iff (g3, g2, u)).mp hx with ⟨_, hg3, hg2⟩
    have hg3_val : (scalarUnitaryHom (Fin 3) ((u ^ 2)⁻¹)).1 = g3.1 :=
      congrArg (Subtype.val : U3C → _) hg3.symm
    have hg2_val : (scalarUnitaryHom (Fin 2) (u ^ 3)).1 = g2.1 :=
      congrArg (Subtype.val : U2C → _) hg2.symm
    apply Subtype.ext
    refine Prod.ext ?_ (Prod.ext ?_ rfl)
    · exact Subtype.ext hg3_val
    · exact Subtype.ext hg2_val
  right_inv _ := rfl
  map_mul' _ _ := rfl

/-- `Circle.exp s ^ m = Circle.exp (m * s)`. -/
theorem circle_exp_pow_nat (s : ℝ) (m : ℕ) :
    Circle.exp s ^ m = Circle.exp ((m : ℝ) * s) := by
  induction m with
  | zero => simp
  | succ m ih => rw [pow_succ, ih, ← Circle.exp_add]; push_cast; ring_nf

/-- Polar surjectivity `ℝ → Circle`: every `w ∈ U(1)` equals `Circle.exp (Complex.arg w)`. -/
theorem circle_exp_surjective (w : Circle) : ∃ θ : ℝ, Circle.exp θ = w := by
  refine ⟨Complex.arg (w : ℂ), ?_⟩
  apply Subtype.ext
  rw [Circle.coe_exp]
  have h := Complex.norm_mul_exp_arg_mul_I (w : ℂ)
  rw [Circle.norm_coe, Complex.ofReal_one, one_mul] at h
  exact h

/-- Existence of a 6th root on `U(1) = Circle`. -/
theorem exists_sixth_root_circle (w : Circle) : ∃ u : Circle, u ^ 6 = w := by
  obtain ⟨θ, hθ⟩ := circle_exp_surjective w
  refine ⟨Circle.exp (θ / 6), ?_⟩
  rw [circle_exp_pow_nat, ← hθ]
  congr 1
  ring

/-- **Surjectivity of `smCoverHom`:** Every `(A, B) ∈ S(U(3) × U(2))` lifts to
`SU(3) × SU(2) × U(1)`. -/
theorem smCoverHom_surjective : Function.Surjective smCoverHom := by
  intro p
  obtain ⟨u, hu⟩ := exists_sixth_root_circle (unitaryDetHom (Fin 3) p.1.1)
  have hpdet : unitaryDetHom (Fin 3) p.1.1 * unitaryDetHom (Fin 2) p.1.2 = 1 := p.2
  let g3U : U3C := scalarUnitaryHom (Fin 3) ((u ^ 2)⁻¹) * p.1.1
  let g2U : U2C := scalarUnitaryHom (Fin 2) (u ^ 3) * p.1.2
  have hg3_det : g3U.1.det = 1 := by
    have h := unitaryDet_scalar3_mul ((u ^ 2)⁻¹) p.1.1
    rw [inv_pow, ← pow_mul, hu, inv_mul_cancel] at h
    exact congrArg Subtype.val h
  have hg2_det : g2U.1.det = 1 := by
    have h := unitaryDet_scalar2_mul (u ^ 3) p.1.2
    rw [← pow_mul, hu, hpdet] at h
    exact congrArg Subtype.val h
  let g3 : SU3C := ⟨g3U.1, Matrix.mem_specialUnitaryGroup_iff.mpr ⟨g3U.2, hg3_det⟩⟩
  let g2 : SU2C := ⟨g2U.1, Matrix.mem_specialUnitaryGroup_iff.mpr ⟨g2U.2, hg2_det⟩⟩
  refine ⟨(g3, g2, u), ?_⟩
  apply Subtype.ext
  apply Prod.ext
  · change scalarUnitaryHom (Fin 3) (u ^ 2) * g3U = p.1.1
    dsimp [g3U]
    rw [← mul_assoc, ← map_mul, mul_inv_cancel, map_one, one_mul]
  · change scalarUnitaryHom (Fin 2) ((u ^ 3)⁻¹) * g2U = p.1.2
    dsimp [g2U]
    rw [← mul_assoc, ← map_mul, inv_mul_cancel, map_one, one_mul]

/-- **Main Group Isomorphism (`qou-txc1` Part (a)):**
`(SU(3) × SU(2) × U(1)) ⧸ ker smCoverHom ≃* S(U(3) × U(2))`, where `ker smCoverHom ≃* μ₆`. -/
noncomputable def smQuotientZ6EquivSU3xU2 :
    (SU3C × SU2C × Circle) ⧸ smCoverHom.ker ≃* ↥SU3xU2Subgroup :=
  QuotientGroup.quotientKerEquivOfSurjective smCoverHom smCoverHom_surjective

/-- Explicit isomorphism `μ₆(Circle) ≃* Multiplicative (ZMod 6)` via `k ↦ exp(2πik/6)`. -/
noncomputable def zmod6ToRoots6 : Multiplicative (ZMod 6) →* ↥rootsOfUnity6Circle where
  toFun k := ⟨Circle.exp (((Multiplicative.toAdd k).val : ℝ) * (2 * Real.pi / 6)), by
    rw [mem_rootsOfUnity6Circle_iff, circle_exp_pow_nat]
    have h6 : ((6 : ℕ) : ℝ) * (((Multiplicative.toAdd k).val : ℝ) * (2 * Real.pi / 6)) =
        (((Multiplicative.toAdd k).val : ℤ) : ℝ) * (2 * Real.pi) := by
      push_cast; ring
    rw [h6]
    exact Circle.exp_int_mul_two_pi _⟩
  map_one' := by
    apply Subtype.ext
    change Circle.exp (((0 : ZMod 6).val : ℝ) * (2 * Real.pi / 6)) = 1
    simp
  map_mul' a b := by
    apply Subtype.ext
    let ka : ZMod 6 := Multiplicative.toAdd a
    let kb : ZMod 6 := Multiplicative.toAdd b
    let qn : ℕ := (ka.val + kb.val) / 6
    change Circle.exp (((ka + kb).val : ℝ) * (2 * Real.pi / 6)) =
      Circle.exp ((ka.val : ℝ) * (2 * Real.pi / 6)) *
        Circle.exp ((kb.val : ℝ) * (2 * Real.pi / 6))
    rw [← Circle.exp_add]
    have hmod : ((ka + kb).val : ℤ) = (ka.val : ℤ) + (kb.val : ℤ) - 6 * (qn : ℤ) := by
      have hval : (ka + kb).val = (ka.val + kb.val) % 6 := ZMod.val_add ka kb
      dsimp [qn]
      omega
    have hm : ((ka + kb).val : ℝ) = (ka.val : ℝ) + (kb.val : ℝ) - 6 * (qn : ℝ) := by
      exact_mod_cast hmod
    have hexp : (((ka + kb).val : ℝ) * (2 * Real.pi / 6)) =
        ((ka.val : ℝ) * (2 * Real.pi / 6) + (kb.val : ℝ) * (2 * Real.pi / 6)) +
          ((-(qn : ℤ) : ℤ) : ℝ) * (2 * Real.pi) := by
      rw [hm]
      push_cast
      ring
    rw [hexp, Circle.exp_add, Circle.exp_int_mul_two_pi, mul_one]

theorem zmod6ToRoots6_bijective : Function.Bijective zmod6ToRoots6 := by
  constructor
  · intro a b hab
    have h1 : zmod6ToRoots6 (a * b⁻¹) = 1 := by rw [map_mul, map_inv, hab, mul_inv_cancel]
    let k : ZMod 6 := Multiplicative.toAdd (a * b⁻¹)
    have hexp : Circle.exp ((k.val : ℝ) * (2 * Real.pi / 6)) = 1 :=
      congrArg Subtype.val h1
    obtain ⟨m, hm⟩ := Circle.exp_eq_one.mp hexp
    have hpi : (2 * Real.pi) ≠ 0 := by positivity
    have hkr : (k.val : ℝ) = (6 : ℝ) * (m : ℝ) := by
      have : (k.val : ℝ) * (2 * Real.pi) = (6 * (m : ℝ)) * (2 * Real.pi) := by linarith
      exact mul_right_cancel₀ hpi this
    have hkz : (k.val : ℤ) = 6 * m := by exact_mod_cast hkr
    have hklt : k.val < 6 := ZMod.val_lt k
    have hk0 : k.val = 0 := by omega
    have hk_eq : k = 0 := by
      rw [← ZMod.natCast_zmod_val k, hk0, Nat.cast_zero]
    have hab1 : a * b⁻¹ = 1 := Multiplicative.toAdd.injective hk_eq
    exact mul_inv_eq_one.mp hab1
  · intro ζ
    obtain ⟨θ, hθ⟩ := circle_exp_surjective ζ.1
    have h6 : Circle.exp (((6 : ℕ) : ℝ) * θ) = 1 := by
      rw [← circle_exp_pow_nat, hθ]
      exact ζ.2
    obtain ⟨n, hn⟩ := Circle.exp_eq_one.mp h6
    have hn6 : (6 : ℝ) * θ = (n : ℝ) * (2 * Real.pi) := by simpa using hn
    let k : ZMod 6 := (n : ZMod 6)
    refine ⟨Multiplicative.ofAdd k, ?_⟩
    apply Subtype.ext
    change Circle.exp ((k.val : ℝ) * (2 * Real.pi / 6)) = ζ.1
    rw [← hθ]
    have hmod : (n : ℤ) = (k.val : ℤ) + 6 * (n / 6) := by
      have hv : (k.val : ℤ) = n % 6 := by
        simpa [k] using (ZMod.val_intCast n)
      omega
    have hnr : (n : ℝ) = (k.val : ℝ) + 6 * ((n / 6 : ℤ) : ℝ) := by exact_mod_cast hmod
    have hθ_eq : θ = (k.val : ℝ) * (2 * Real.pi / 6) + ((n / 6 : ℤ) : ℝ) * (2 * Real.pi) := by
      calc θ = ((6 : ℝ) * θ) / 6 := by ring
        _ = ((n : ℝ) * (2 * Real.pi)) / 6 := by rw [hn6]
        _ = (k.val : ℝ) * (2 * Real.pi / 6) + ((n / 6 : ℤ) : ℝ) * (2 * Real.pi) := by
            rw [hnr]; ring
    rw [hθ_eq, Circle.exp_add, Circle.exp_int_mul_two_pi, mul_one]

/-- Group isomorphism `ker smCoverHom ≃* Multiplicative (ZMod 6)` (`ℤ/6ℤ`). -/
noncomputable def kerSmCoverEquivZMod6 : ↥smCoverHom.ker ≃* Multiplicative (ZMod 6) :=
  kerSmCoverEquivRoots6.trans (MulEquiv.ofBijective zmod6ToRoots6 zmod6ToRoots6_bijective).symm

/-- Exact cardinality of `ker smCoverHom` is `6`. -/
theorem natCard_ker_smCoverHom : Nat.card ↥smCoverHom.ker = 6 := by
  rw [Nat.card_congr kerSmCoverEquivZMod6.toEquiv, Nat.card_congr Multiplicative.toAdd]
  exact Nat.card_zmod 6

end BaezHuertaGroupIso

/-! ## Section 2: Commutant of `𝔰𝔩₃(K) ⊕ 𝔰𝔩₂(K)` in `𝔰𝔩₅(K)` & Parameterized `5̄ ⊕ 10` Trace Ratio -/

section ParameterizedCommutantTraceRatio

variable {K : Type*} [Field K]

/-- The 11-dimensional block-diagonal traceless Lie subalgebra `𝔰𝔩₃(K) ⊕ 𝔰𝔩₂(K)` inside
`Matrix (Fin 5) (Fin 5) K` (colour indices `{0, 1, 2}`, weak indices `{3, 4}`). -/
def sl3_oplus_sl2 (K : Type*) [Ring K] : Set (Matrix (Fin 5) (Fin 5) K) :=
  {X | (∀ i j : Fin 5, (i.1 < 3 ↔ ¬ j.1 < 3) → X i j = 0) ∧
       X 0 0 + X 1 1 + X 2 2 = 0 ∧
       X 3 3 + X 4 4 = 0}

/-- Integer-scaled traceless commutant generator `Y₀ = diag(-2, -2, -2, 3, 3) ∈ 𝔰𝔩₅(K)`. -/
def Y0 (K : Type*) [Ring K] : Matrix (Fin 5) (Fin 5) K :=
  Matrix.diagonal ![-2, -2, -2, 3, 3]

/-- Weak third-isospin generator `T₃ = diag(0, 0, 0, 1/2, -1/2) ∈ 𝔰𝔩₃(K) ⊕ 𝔰𝔩₂(K)`. -/
def T3 (K : Type*) [Field K] : Matrix (Fin 5) (Fin 5) K :=
  Matrix.diagonal ![0, 0, 0, (1 : K) / 2, -((1 : K) / 2)]

/-- `Y0 K` is traceless (`Tr(Y₀) = 0`). -/
theorem trace_Y0 : (Y0 K).trace = 0 := by
  simp [Y0, Matrix.trace, Matrix.diag, Fin.sum_univ_five]
  ring

/-- `T3 K` lies in `sl3_oplus_sl2 K` and is traceless. -/
theorem T3_mem_sl3_oplus_sl2 : T3 K ∈ sl3_oplus_sl2 K := by
  refine ⟨?_, ?_, ?_⟩
  · intro i j hij
    have hne : i ≠ j := by intro h; subst h; exact iff_not_self hij
    simp [T3, Matrix.diagonal_apply_ne _ hne]
  · simp [T3]
  · simp [T3]

/-- Elementary `5 × 5` matrix `E_{ab}` with `1` at `(a, b)` and `0` elsewhere. -/
def elemMat (K : Type*) [Ring K] (a b : Fin 5) : Matrix (Fin 5) (Fin 5) K :=
  fun i j => if i = a ∧ j = b then 1 else 0

theorem elemMat_diag_eq_zero (a b c : Fin 5) (hab : a ≠ b) :
    elemMat K a b c c = 0 := by
  simp only [elemMat, ite_eq_right_iff, one_ne_zero, imp_false, not_and]
  intro h1 h2
  exact hab (h1.symm.trans h2)

theorem mul_elemMat_col (Y : Matrix (Fin 5) (Fin 5) K) (a b i : Fin 5) :
    (Y * elemMat K a b) i b = Y i a := by
  fin_cases a <;> simp [Matrix.mul_apply, elemMat]

theorem elemMat_mul_col (Y : Matrix (Fin 5) (Fin 5) K) (a b i : Fin 5) :
    (elemMat K a b * Y) i b = if i = a then Y b b else 0 := by
  by_cases hia : i = a
  · subst hia
    fin_cases b <;> simp [Matrix.mul_apply, elemMat]
  · simp [Matrix.mul_apply, elemMat, hia]

/-- Helper: elementary off-diagonal matrix `E_{ab}` with `a ≠ b` in the same `{0,1,2}` or `{3,4}`
block belongs to `sl3_oplus_sl2 K`. -/
theorem elemMat_mem_sl3_oplus_sl2 (a b : Fin 5) (hab : a ≠ b)
    (hblk : a.1 < 3 ↔ b.1 < 3) :
    elemMat K a b ∈ sl3_oplus_sl2 K := by
  refine ⟨?_, ?_, ?_⟩
  · intro i j hij
    simp only [elemMat, ite_eq_right_iff, one_ne_zero, imp_false, not_and]
    intro hia hjb
    subst hia; subst hjb
    tauto
  · simp [elemMat_diag_eq_zero a b _ hab]
  · simp [elemMat_diag_eq_zero a b _ hab]

/-- **Exact 1D Commutant Theorem (`qou-txc1` Part (b), `2026-11-22` Rescope):**
A traceless `5 × 5` matrix `Y` commutes with every `X ∈ sl3_oplus_sl2 K` if and only if
`Y = α • Y0 K` for some free normalization scalar `α : K`. -/
theorem mem_traceless_commutant_sl3_sl2_iff [CharZero K] (Y : Matrix (Fin 5) (Fin 5) K) :
    ((∀ X ∈ sl3_oplus_sl2 K, Y * X = X * Y) ∧ Y.trace = 0) ↔
      ∃ α : K, Y = α • Y0 K := by
  constructor
  · rintro ⟨hcomm, htr⟩
    -- Helper extracting entries from `Y * elemMat K a b = elemMat K a b * Y`
    have hE : ∀ (a b : Fin 5), a ≠ b → (a.1 < 3 ↔ b.1 < 3) →
        (∀ i : Fin 5, i ≠ a → Y i a = 0) ∧ Y a a = Y b b := by
      intro a b hab hblk
      have hmem := elemMat_mem_sl3_oplus_sl2 (K := K) a b hab hblk
      have hc := hcomm _ hmem
      refine ⟨?_, ?_⟩
      · intro i hia
        have hij := congrFun (congrFun hc i) b
        rw [mul_elemMat_col, elemMat_mul_col, if_neg hia] at hij
        exact hij
      · have hij := congrFun (congrFun hc a) b
        rw [mul_elemMat_col, elemMat_mul_col, if_pos rfl] at hij
        exact hij
    have h01 := hE 0 1 (by decide) (by decide)
    have h12 := hE 1 2 (by decide) (by decide)
    have h20 := hE 2 0 (by decide) (by decide)
    have h34 := hE 3 4 (by decide) (by decide)
    have h43 := hE 4 3 (by decide) (by decide)
    have htr5 : Y 0 0 + Y 1 1 + Y 2 2 + Y 3 3 + Y 4 4 = 0 := by
      simpa [Matrix.trace, Matrix.diag, Fin.sum_univ_five, add_assoc] using htr
    have hd1 : Y 1 1 = Y 0 0 := h01.2.symm
    have hd2 : Y 2 2 = Y 0 0 := (h12.2.symm).trans hd1
    have hd4 : Y 4 4 = Y 3 3 := h34.2.symm
    refine ⟨-(Y 0 0) / 2, ?_⟩
    have hsum : 2 * Y 3 3 = -(3 * Y 0 0) := by
      rw [hd1, hd2, hd4] at htr5
      calc 2 * Y 3 3 = (Y 0 0 + Y 0 0 + Y 0 0 + Y 3 3 + Y 3 3) - 3 * Y 0 0 := by ring
        _ = 0 - 3 * Y 0 0 := by rw [htr5]
        _ = -(3 * Y 0 0) := by ring
    have h2 : (2 : K) ≠ 0 := two_ne_zero
    have hY33 : Y 3 3 = (-(Y 0 0) / 2) * 3 := by
      calc Y 3 3 = (2 * Y 3 3) / 2 := by field_simp [h2]
        _ = (-(3 * Y 0 0)) / 2 := by rw [hsum]
        _ = (-(Y 0 0) / 2) * 3 := by ring
    ext i j
    fin_cases i <;> fin_cases j
    · simp [Y0]
    · exact (h12.1 0 (by decide)).trans (by simp [Y0])
    · exact (h20.1 0 (by decide)).trans (by simp [Y0])
    · exact (h34.1 0 (by decide)).trans (by simp [Y0])
    · exact (h43.1 0 (by decide)).trans (by simp [Y0])
    · exact (h01.1 1 (by decide)).trans (by simp [Y0])
    · simp [Y0, hd1]
    · exact (h20.1 1 (by decide)).trans (by simp [Y0])
    · exact (h34.1 1 (by decide)).trans (by simp [Y0])
    · exact (h43.1 1 (by decide)).trans (by simp [Y0])
    · exact (h01.1 2 (by decide)).trans (by simp [Y0])
    · exact (h12.1 2 (by decide)).trans (by simp [Y0])
    · simp [Y0, hd2]
    · exact (h34.1 2 (by decide)).trans (by simp [Y0])
    · exact (h43.1 2 (by decide)).trans (by simp [Y0])
    · exact (h01.1 3 (by decide)).trans (by simp [Y0])
    · exact (h12.1 3 (by decide)).trans (by simp [Y0])
    · exact (h20.1 3 (by decide)).trans (by simp [Y0])
    · simp [Y0, hY33]
    · exact (h43.1 3 (by decide)).trans (by simp [Y0])
    · exact (h01.1 4 (by decide)).trans (by simp [Y0])
    · exact (h12.1 4 (by decide)).trans (by simp [Y0])
    · exact (h20.1 4 (by decide)).trans (by simp [Y0])
    · exact (h34.1 4 (by decide)).trans (by simp [Y0])
    · simp [Y0, hd4, hY33]
  · rintro ⟨α, rfl⟩
    refine ⟨?_, ?_⟩
    · intro X hX
      rcases hX with ⟨hblk, _, _⟩
      ext i j
      fin_cases i <;> fin_cases j <;>
        simp [Y0, Matrix.mul_apply, Fin.sum_univ_five,
          hblk 0 3 (by decide), hblk 0 4 (by decide),
          hblk 1 3 (by decide), hblk 1 4 (by decide),
          hblk 2 3 (by decide), hblk 2 4 (by decide),
          hblk 3 0 (by decide), hblk 3 1 (by decide), hblk 3 2 (by decide),
          hblk 4 0 (by decide), hblk 4 1 (by decide), hblk 4 2 (by decide)] <;>
        ring
    · rw [Matrix.trace_smul, trace_Y0, smul_zero]

/-- Parameterized charge generator `Q(α) = T₃ + α • Y₀` on the fundamental `5` (`K⁵`), keeping the
hypercharge / commutant scale `α : K` completely free. -/
def Q5 (α : K) : Matrix (Fin 5) (Fin 5) K := T3 K + α • Y0 K

/-- Weight `q_i(α) = (Q5 α)_{ii}` on the `5` representation. -/
def qWeight5 (α : K) (i : Fin 5) : K := Q5 α i i

/-- Third-isospin weight `(T₃)_{ii}` on the `5` representation. -/
def t3Weight5 (K : Type*) [Field K] (i : Fin 5) : K := T3 K i i

/-- Quadratic trace `Tr_5(T₃²) = 1 / 2` on the fundamental `5`. -/
theorem tr5_T3_sq [CharZero K] : (T3 K * T3 K).trace = (1 : K) / 2 := by
  have h2 : (2 : K) ≠ 0 := two_ne_zero
  simp [T3, Matrix.trace, Matrix.diag, Matrix.mul_apply, Fin.sum_univ_five]
  field_simp [h2]
  ring

/-- Quadratic trace `Tr_5(Y₀²) = 30` on the fundamental `5`. -/
theorem tr5_Y0_sq : (Y0 K * Y0 K).trace = 30 := by
  simp [Y0, Matrix.trace, Matrix.diag, Matrix.mul_apply, Fin.sum_univ_five]
  norm_num

/-- Orthogonality `Tr_5(T₃ · Y₀) = 0` on the fundamental `5`. -/
theorem tr5_T3_Y0 : (T3 K * Y0 K).trace = 0 := by
  simp [T3, Y0, Matrix.trace, Matrix.diag, Fin.sum_univ_five]

/-- Parameterized quadratic trace `Tr_5(Q(α)²) = 1 / 2 + 30 α²` on `5` (and identically on `5̄`). -/
theorem tr5_Q_sq [CharZero K] (α : K) : (Q5 α * Q5 α).trace = (1 : K) / 2 + 30 * α ^ 2 := by
  have h2 : (2 : K) ≠ 0 := two_ne_zero
  simp [Q5, T3, Y0, Matrix.trace, Matrix.diag, Matrix.mul_apply, Fin.sum_univ_five]
  field_simp [h2]
  ring

/-- Quadratic trace `Tr_{10}(X²)` of a diagonal weight `w : Fin 5 → K` on the exterior square
`10 = Λ²(K⁵)` (sum of `(w i + w j)²` over the 10 basis wedges `e_i ∧ e_j`, `i < j`). -/
def tr10DiagSq (w : Fin 5 → K) : K :=
  ∑ p ∈ Finset.univ.filter (fun p : Fin 5 × Fin 5 => p.1 < p.2), (w p.1 + w p.2) ^ 2

/-- Quadratic trace `Tr_{5̄}(X²)` of a diagonal weight `w : Fin 5 → K` on the dual `5̄`
(sum of `(-w i)²` over `i : Fin 5`). -/
def tr5barDiagSq (w : Fin 5 → K) : K :=
  ∑ i : Fin 5, (-w i) ^ 2

/-- Total quadratic trace on the 15-dimensional chiral representation `5̄ ⊕ 10`. -/
def tr5bar10DiagSq (w : Fin 5 → K) : K :=
  tr5barDiagSq w + tr10DiagSq w

/-- Explicit expansion of `tr10DiagSq w` over the `10` strict pairs `i < j` in `Fin 5`, yielding
the universal exterior-square quadratic identity
`∑_{i < j} (w_i + w_j)² = 3 * (∑_i w_i²) + (∑_i w_i)²` (for `n = 5`, Dynkin factor `n - 2 = 3`). -/
theorem tr10DiagSq_eq_three_sum_sq_add_sq_sum (w : Fin 5 → K) :
    tr10DiagSq w = 3 * (∑ i : Fin 5, (w i) ^ 2) + (∑ i : Fin 5, w i) ^ 2 := by
  unfold tr10DiagSq
  rw [Finset.sum_filter, Fintype.sum_prod_type]
  simp [Fin.sum_univ_five]
  ring

/-- Dual `5̄` quadratic trace equals `∑_i w_i²`. -/
theorem tr5barDiagSq_eq_sum_sq (w : Fin 5 → K) :
    tr5barDiagSq w = ∑ i : Fin 5, (w i) ^ 2 := by
  unfold tr5barDiagSq
  simp

/-- For any traceless diagonal generator (`∑_i w_i = 0`), the `10 = Λ²(5)` quadratic trace is
identically `3` times the fundamental `5` quadratic trace (`I(10) = 3 I(5)`), and the `5̄ ⊕ 10`
quadratic trace is identically `4` times the fundamental `5` quadratic trace. -/
theorem tr10_and_tr5bar10_of_traceless (w : Fin 5 → K) (htr : (∑ i : Fin 5, w i) = 0) :
    tr10DiagSq w = 3 * (∑ i : Fin 5, (w i) ^ 2) ∧
    tr5bar10DiagSq w = 4 * (∑ i : Fin 5, (w i) ^ 2) := by
  refine ⟨?_, ?_⟩
  · rw [tr10DiagSq_eq_three_sum_sq_add_sq_sum, htr]
    ring
  · unfold tr5bar10DiagSq
    rw [tr5barDiagSq_eq_sum_sq, tr10DiagSq_eq_three_sum_sq_add_sq_sum, htr]
    ring

/-- On `10 = Λ²(5)`, `Tr_{10}(T₃²) = 3 / 2`. -/
theorem tr10_T3_sq [CharZero K] : tr10DiagSq (t3Weight5 K) = (3 : K) / 2 := by
  have h2 : (2 : K) ≠ 0 := two_ne_zero
  have htr : (∑ i : Fin 5, t3Weight5 K i) = 0 := by
    simp [t3Weight5, T3, Fin.sum_univ_five]
  rw [(tr10_and_tr5bar10_of_traceless (t3Weight5 K) htr).1]
  simp [t3Weight5, T3, Fin.sum_univ_five]
  field_simp [h2]
  ring

/-- On `5̄ ⊕ 10`, `Tr_{5̄ ⊕ 10}(T₃²) = 2`. -/
theorem tr5bar10_T3_sq [CharZero K] : tr5bar10DiagSq (t3Weight5 K) = 2 := by
  have h2 : (2 : K) ≠ 0 := two_ne_zero
  have htr : (∑ i : Fin 5, t3Weight5 K i) = 0 := by
    simp [t3Weight5, T3, Fin.sum_univ_five]
  rw [(tr10_and_tr5bar10_of_traceless (t3Weight5 K) htr).2]
  simp [t3Weight5, T3, Fin.sum_univ_five]
  field_simp [h2]
  ring

/-- `qWeight5 α` is traceless (`∑_i q_i(α) = 0`) for every `α : K`. -/
theorem sum_qWeight5 (α : K) : (∑ i : Fin 5, qWeight5 α i) = 0 := by
  change (Q5 α).trace = 0
  rw [Q5, Matrix.trace_add, Matrix.trace_smul, trace_Y0, smul_zero, add_zero]
  simp [T3, Matrix.trace, Matrix.diag, Fin.sum_univ_five]

/-- On `10 = Λ²(5)`, `Tr_{10}(Q(α)²) = 3 / 2 + 90 α²`. -/
theorem tr10_Q_sq [CharZero K] (α : K) :
    tr10DiagSq (qWeight5 α) = (3 : K) / 2 + 90 * α ^ 2 := by
  have h2 : (2 : K) ≠ 0 := two_ne_zero
  rw [(tr10_and_tr5bar10_of_traceless (qWeight5 α) (sum_qWeight5 α)).1]
  simp [qWeight5, Q5, T3, Y0, Fin.sum_univ_five]
  field_simp [h2]
  ring

/-- On `5̄ ⊕ 10`, `Tr_{5̄ ⊕ 10}(Q(α)²) = 2 * (1 + 60 α²)`. -/
theorem tr5bar10_Q_sq [CharZero K] (α : K) :
    tr5bar10DiagSq (qWeight5 α) = 2 * (1 + 60 * α ^ 2) := by
  have h2 : (2 : K) ≠ 0 := two_ne_zero
  rw [(tr10_and_tr5bar10_of_traceless (qWeight5 α) (sum_qWeight5 α)).2]
  simp [qWeight5, Q5, T3, Y0, Fin.sum_univ_five]
  field_simp [h2]
  ring

/-- **Parameterized `5̄ ⊕ 10` Trace Ratio (`qou-txc1` Part (b), `2026-11-22` Rescope):**
With the `𝔰𝔩₃ ⊕ 𝔰𝔩₂` commutant scale `α : K` left completely free (`Q(α) = T₃ + α • Y₀`),
`Tr_{5̄ ⊕ 10}(T₃²) / Tr_{5̄ ⊕ 10}(Q(α)²) = 1 / (1 + 60 α²)`. -/
theorem traceRatio_5bar_oplus_10_param [CharZero K] (α : K) (hden : 1 + 60 * α ^ 2 ≠ 0) :
    tr5bar10DiagSq (t3Weight5 K) / tr5bar10DiagSq (qWeight5 α) =
      1 / (1 + 60 * α ^ 2) := by
  have h2 : (2 : K) ≠ 0 := two_ne_zero
  rw [tr5bar10_T3_sq, tr5bar10_Q_sq]
  field_simp [hden, h2]

/-- **Normalization Equivalence (`3 / 8 ↔ α² = 1 / 36`):**
The parameterized `5̄ ⊕ 10` trace ratio equals `3 / 8` if and only if `α² = 1 / 36`
(`α = 1 / 6` or `α = -1 / 6`, i.e., unit charge `±1` on the colour-singlet `e^c` wedge `(3, 4)`). -/
theorem traceRatio_5bar_oplus_10_eq_three_eighths_iff [CharZero K] (α : K)
    (hden : 1 + 60 * α ^ 2 ≠ 0) :
    tr5bar10DiagSq (t3Weight5 K) / tr5bar10DiagSq (qWeight5 α) = (3 : K) / 8 ↔
      α ^ 2 = (1 : K) / 36 := by
  rw [traceRatio_5bar_oplus_10_param α hden]
  have h8 : (8 : K) ≠ 0 := by norm_num
  have h180 : (180 : K) ≠ 0 := by norm_num
  rw [div_eq_div_iff hden h8]
  constructor
  · intro h
    have h1 : 180 * α ^ 2 = 5 := by
      calc 180 * α ^ 2 = 3 * (1 + 60 * α ^ 2) - 3 := by ring
        _ = 1 * 8 - 3 := by rw [← h]
        _ = 5 := by norm_num
    calc α ^ 2 = (180 * α ^ 2) / 180 := by field_simp [h180]
      _ = 5 / 180 := by rw [h1]
      _ = (1 : K) / 36 := by norm_num
  · intro h
    rw [h]
    norm_num

end ParameterizedCommutantTraceRatio

/-! ## Section 3: part (c) is the flavour `W` construction (carrier retired 2026-11-27)

The former carrier `BringKummerSU5EmbeddingHypothesis` was satisfiable by `α = 1/6` (any field of
characteristic zero), so it recorded no open content.  Retired on Carl's card of 2026-11-27
("Retire carrier, link to flavour W").  What part (c) actually asks is that the substrate supply
the 3-dimensional, non-self-dual `W` with `Λ³W ≅ 1` beside `V` (bean `qou-j3w6`); once `W` exists,
`α² = 1/36` follows from the neutral-lepton condition
(`AnomalyFreeHypercharge.neutral_lepton_iff_three_eighths`). -/

end QOU.StandardModel.Su3Su2U1Z6GroupAndCommutant

