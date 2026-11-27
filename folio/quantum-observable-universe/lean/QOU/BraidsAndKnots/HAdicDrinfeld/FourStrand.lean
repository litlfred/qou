import QOU.BraidsAndKnots.HAdicDrinfeld.CasimirData
import QOU.BraidsAndKnots.RationalAssociator.UniversalDK

/-!
# Four strands and the truncated evaluation map

Epic `qou-dk7p`, step B of `docs/audits/2026-11-27-kz-trio-strangler-plan.md`.

A rational associator lives in `U4 N`, the universal Drinfeld–Kohno algebra truncated at degree
`N` (`RationalAssociator/UniversalDK.lean`). To use it in the h-adic Drinfeld category it has to
be sent to `A^{⊗4}` with `tᵢⱼ ↦ h tᵢⱼ`, modulo `h^N`. This file builds that map without using any
associator:

* `DK4.mulCentral`, `words_mulCentral_eq_zero`, `evalU4`: in any `ℚ`-algebra `B`, a `DK4` family
  multiplied by a central `z` with `z ^ N = 0` is again `DK4` and kills every word of length `N`,
  so `U4 N` maps to `B` with `tᵢⱼ ↦ z sᵢⱼ`;
* `CasimirData.dk4`: the six leg copies of `t` in `((A ⊗ A) ⊗ A) ⊗ A` form a `DK4` family. The
  twelve near relations are the three-strand relations of `CasimirData.dk3`, pushed along the four
  inclusions `A^{⊗3} → A^{⊗4}` that omit one strand; the three far relations hold because the
  legs sit in disjoint tensor factors;
* `CasimirData.evalU4`: for `c ∈ k` with `c ^ N = 0`, the algebra map `U4 N → A^{⊗4}` with
  `tᵢⱼ ↦ c tᵢⱼ`. With `k = ℚ[h]/(h^N)` and `c = h` this is the truncated h-adic evaluation.

Everything is over an arbitrary commutative ring `k`. No analysis is used.
-/

namespace QOU.BraidsAndKnots.HAdicDrinfeld

open scoped TensorProduct
open QOU.HeckeTemperleyLieb.QuasiYangBaxterFromHexagon
open QOU.BraidsAndKnots.RationalAssociator

section Central

variable {B : Type*} [Ring B]

theorem commute_mulCentral {z a b : B} (hz : ∀ y, Commute z y) (h : Commute a b) :
    Commute (z * a) (z * b) := by
  have h1 : z * a * (z * b) = z * z * (a * b) := by
    rw [mul_assoc, ← mul_assoc a, ← (hz a).eq, mul_assoc, mul_assoc]
  have h2 : z * b * (z * a) = z * z * (b * a) := by
    rw [mul_assoc, ← mul_assoc b, ← (hz b).eq, mul_assoc, mul_assoc]
  show z * a * (z * b) = z * b * (z * a)
  rw [h1, h2, h.eq]

/-- A `DK4` family times a central element is a `DK4` family. -/
theorem DK4.mulCentral {z t12 t13 t14 t23 t24 t34 : B} (hz : ∀ y, Commute z y)
    (h : DK4 t12 t13 t14 t23 t24 t34) :
    DK4 (z * t12) (z * t13) (z * t14) (z * t23) (z * t24) (z * t34) := by
  have c := fun {a b c : B} (hh : Commute a (b + c)) =>
    (show Commute (z * a) (z * b + z * c) by rw [← mul_add]; exact commute_mulCentral hz hh)
  exact ⟨commute_mulCentral hz h.f12_34, commute_mulCentral hz h.f13_24,
    commute_mulCentral hz h.f14_23, c h.n12_3, c h.n13_2, c h.n23_1, c h.n12_4, c h.n14_2,
    c h.n24_1, c h.n13_4, c h.n14_3, c h.n34_1, c h.n23_4, c h.n24_3, c h.n34_2⟩

theorem words_mulCentral {z : B} (hz : ∀ y, Commute z y) (s : Fin 6 → B) (w : List (Fin 6)) :
    (w.map (fun i => z * s i)).prod = z ^ w.length * (w.map s).prod := by
  induction w with
  | nil => simp
  | cons i w ih =>
    simp only [List.map_cons, List.prod_cons, ih, List.length_cons, pow_succ]
    rw [mul_assoc, ← mul_assoc (s i), ← ((hz (s i)).pow_left w.length).eq]
    simp only [mul_assoc]
    rw [← mul_assoc z, ← pow_succ', pow_succ, mul_assoc]

/-- Every word of length `N` in `z sᵢⱼ` vanishes when `z ^ N = 0`. -/
theorem words_mulCentral_eq_zero {z : B} (hz : ∀ y, Commute z y) {N : ℕ} (hN : z ^ N = 0)
    (s : Fin 6 → B) (w : List (Fin 6)) (hw : w.length = N) :
    (w.map (fun i => z * s i)).prod = 0 := by
  rw [words_mulCentral hz, hw, hN, zero_mul]

variable [Algebra ℚ B]

/-- **The truncated evaluation map.** For a `DK4` family `s` and a central `z` with `z ^ N = 0`,
the algebra map `U4 N →ₐ[ℚ] B` with `tᵢⱼ ↦ z sᵢⱼ`. -/
noncomputable def evalU4 (N : ℕ) {z : B} (hz : ∀ y, Commute z y) (hN : z ^ N = 0)
    (s : Fin 6 → B) (hs : DK4 (s 0) (s 1) (s 2) (s 3) (s 4) (s 5)) : U4 N →ₐ[ℚ] B :=
  lift N (fun i => z * s i) (DK4.mulCentral hz hs) (words_mulCentral_eq_zero hz hN s)

@[simp] theorem evalU4_t (N : ℕ) {z : B} (hz : ∀ y, Commute z y) (hN : z ^ N = 0)
    (s : Fin 6 → B) (hs : DK4 (s 0) (s 1) (s 2) (s 3) (s 4) (s 5)) (i : Fin 6) :
    evalU4 N hz hN s hs (t N i) = z * s i := by
  simp [evalU4]

end Central

section FourStrand

variable {k A : Type*} [CommRing k] [Ring A] [Algebra k A]

/-- `A^{⊗4}`, associated to the left. -/
abbrev T4 (k A : Type*) [CommRing k] [Ring A] [Algebra k A] :=
  ((A ⊗[k] A) ⊗[k] A) ⊗[k] A

/-- Omit strand 4: `x ↦ x ⊗ 1`. -/
noncomputable def omit4 : (A ⊗[k] A) ⊗[k] A →ₐ[k] T4 k A :=
  Algebra.TensorProduct.includeLeft

/-- Omit strand 3: `(a ⊗ b) ⊗ c ↦ ((a ⊗ b) ⊗ 1) ⊗ c`. -/
noncomputable def omit3 : (A ⊗[k] A) ⊗[k] A →ₐ[k] T4 k A :=
  Algebra.TensorProduct.map Algebra.TensorProduct.includeLeft (AlgHom.id k A)

/-- Omit strand 2: `(a ⊗ b) ⊗ c ↦ ((a ⊗ 1) ⊗ b) ⊗ c`. -/
noncomputable def omit2 : (A ⊗[k] A) ⊗[k] A →ₐ[k] T4 k A :=
  Algebra.TensorProduct.map leg13 (AlgHom.id k A)

/-- Omit strand 1: `(a ⊗ b) ⊗ c ↦ ((1 ⊗ a) ⊗ b) ⊗ c`. -/
noncomputable def omit1 : (A ⊗[k] A) ⊗[k] A →ₐ[k] T4 k A :=
  Algebra.TensorProduct.map leg23 (AlgHom.id k A)

theorem DK3.map {R S : Type*} [Ring R] [Ring S] {F : Type*} [FunLike F R S] [RingHomClass F R S]
    (f : F) {a b c : R} (h : DK3 a b c) : DK3 (f a) (f b) (f c) := by
  obtain ⟨h1, h2, h3⟩ := h
  refine ⟨?_, ?_, ?_⟩
  · rw [← map_add]; exact h1.map f
  · rw [← map_add]; exact h2.map f
  · rw [← map_add]; exact h3.map f

section Legs

open Algebra.TensorProduct

set_option hygiene false in
local macro "leg_tac" : tactic => `(tactic| (
  induction x using TensorProduct.induction_on with
  | zero => simp [leg12]
  | tmul a b => simp [omit1, omit2, omit3, omit4, leg12, leg13, leg23, map_tmul,
      includeLeft_apply, includeRight_apply]
  | add x y hx hy => simp only [CasimirData.leg12_add, map_add, hx, hy]))

theorem omit3_leg12 (x : A ⊗[k] A) : omit3 (leg12 x) = omit4 (leg12 x) := by leg_tac
theorem omit2_leg12 (x : A ⊗[k] A) : omit2 (leg12 x) = omit4 (leg13 x) := by leg_tac
theorem omit2_leg13 (x : A ⊗[k] A) : omit2 (leg13 x) = omit3 (leg13 x) := by leg_tac
theorem omit1_leg12 (x : A ⊗[k] A) : omit1 (leg12 x) = omit4 (leg23 x) := by leg_tac
theorem omit1_leg13 (x : A ⊗[k] A) : omit1 (leg13 x) = omit3 (leg23 x) := by leg_tac
theorem omit1_leg23 (x : A ⊗[k] A) : omit1 (leg23 x) = omit2 (leg23 x) := by leg_tac

set_option hygiene false in
local macro "far_tac" : tactic => `(tactic| (
  induction x using TensorProduct.induction_on with
  | zero => simp only [leg12, TensorProduct.zero_tmul, map_zero]; exact Commute.zero_left (G₀ := T4 k A) _
  | add x x' hx hx' =>
    simp only [CasimirData.leg12_add, map_add]; exact Commute.add_left (R := T4 k A) hx hx'
  | tmul a b =>
    induction y using TensorProduct.induction_on with
    | zero => simp only [leg12, TensorProduct.zero_tmul, map_zero]; exact Commute.zero_right (G₀ := T4 k A) _
    | add y y' hy hy' =>
      simp only [CasimirData.leg12_add, map_add]; exact Commute.add_right (R := T4 k A) hy hy'
    | tmul c d =>
      simp only [omit2, omit3, omit4, leg12, leg13, leg23, map_tmul, includeLeft_apply,
        includeRight_apply, AlgHom.id_apply, AlgHom.coe_coe]
      simp only [Commute, SemiconjBy, tmul_mul_tmul, mul_one, one_mul]))

theorem far12_34 (x y : A ⊗[k] A) : Commute (omit4 (leg12 x)) (omit2 (leg23 y)) := by far_tac
theorem far13_24 (x y : A ⊗[k] A) : Commute (omit4 (leg13 x)) (omit3 (leg23 y)) := by far_tac
theorem far14_23 (x y : A ⊗[k] A) : Commute (omit3 (leg13 x)) (omit4 (leg23 y)) := by far_tac

end Legs

namespace CasimirData

variable (D : CasimirData k A)

/-- The six leg copies of `t` in `A^{⊗4}`, in the order `t₁₂, t₁₃, t₁₄, t₂₃, t₂₄, t₃₄` of
`UniversalDK.t`. -/
noncomputable def t4 : Fin 6 → T4 k A :=
  ![omit4 (leg12 D.t), omit4 (leg13 D.t), omit3 (leg13 D.t), omit4 (leg23 D.t),
    omit3 (leg23 D.t), omit2 (leg23 D.t)]

/-- **The leg copies of `t` on four strands form a Drinfeld–Kohno family.** -/
theorem dk4 : DK4 (D.t4 0) (D.t4 1) (D.t4 2) (D.t4 3) (D.t4 4) (D.t4 5) := by
  have h4 := DK3.map omit4 D.dk3
  have h3 := DK3.map omit3 D.dk3
  have h2 := DK3.map omit2 D.dk3
  have h1 := DK3.map omit1 D.dk3
  rw [omit3_leg12] at h3
  rw [omit2_leg12, omit2_leg13] at h2
  rw [omit1_leg12, omit1_leg13, omit1_leg23] at h1
  simp only [t4, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
  exact ⟨far12_34 _ _, far13_24 _ _, far14_23 _ _, h4.1, h4.2, h4.3, h3.1, h3.2, h3.3,
    h2.1, h2.2, h2.3, h1.1, h1.2, h1.3⟩

/-- **The truncated h-adic evaluation.** For `c ∈ k` with `c ^ N = 0`, the algebra map
`U4 N →ₐ[ℚ] A^{⊗4}` with `tᵢⱼ ↦ c · tᵢⱼ`. -/
noncomputable def evalU4 [Algebra ℚ (T4 k A)] (N : ℕ) (c : k) (hc : c ^ N = 0) :
    U4 N →ₐ[ℚ] T4 k A :=
  HAdicDrinfeld.evalU4 N (z := algebraMap k (T4 k A) c) (fun y => Algebra.commutes c y)
    (by rw [← map_pow, hc, map_zero]) D.t4 D.dk4

theorem evalU4_t [Algebra ℚ (T4 k A)] (N : ℕ) (c : k) (hc : c ^ N = 0) (i : Fin 6) :
    D.evalU4 N c hc (RationalAssociator.t N i) = c • D.t4 i := by
  rw [evalU4, HAdicDrinfeld.evalU4_t]
  exact (Algebra.smul_def (A := T4 k A) c (D.t4 i)).symm

end CasimirData

end FourStrand

end QOU.BraidsAndKnots.HAdicDrinfeld
