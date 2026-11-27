import QOU.BraidsAndKnots.RationalAssociator.DrinfeldKohno
import HeckeTemperleyLieb.QuasiYangBaxterFromHexagon
import Mathlib.Algebra.Polynomial.AlgebraMap

/-!
# Casimir data for the h-adic Drinfeld category

Epic `qou-dk7p`, step B of `docs/audits/2026-11-27-kz-trio-strangler-plan.md`.

The analytic Drinfeld category (`QOU/Transcendental/BraidsAndKnots/Drinfeld/*`) puts the KZ
associator into a normed `ℂ`-algebra. The algebraic version puts a **rational** associator
`Φ ∈ ℚ⟨⟨A, B⟩⟩` into `A^{⊗3}⟦h⟧` by `Φ(h t₁₂, h t₂₃)`, where `A` carries a cocommutative
coproduct and a symmetric invariant tensor `t` (for `A = U(𝔤)`, the split Casimir). This file
sets up that input and proves the two facts about it that do not depend on `Φ`:

* `CasimirData.dk3`: the three leg copies `(t₁₂, t₁₃, t₂₃)` form a Drinfeld–Kohno family
  (`RationalAssociator.DK3`). So every statement proved for `DK3` families, in particular the
  hexagon of `RationalAssociator/HexagonUniversal.lean`, applies to them;
* `CasimirData.dk3_smul`: so do the rescaled copies `(c t₁₂, c t₁₃, c t₂₃)` for any scalar
  `c`, which is how `h` enters;
* `CasimirData.quasiCocomm_aeval`: every polynomial `R = p(t)` is quasi-cocommutative,
  `Δᵒᵖ(a) R = R Δ(a)`. Truncated at `h^N`, `exp(h t / 2)` is such a polynomial, with
  coefficients in `k = ℚ[h]/(h^N)`. This is the hypothesis `hR` of
  `QuasiYangBaxterFromHexagon.quasiYBE_of_hexagon`.

Everything is over an arbitrary commutative ring `k` and an arbitrary `k`-algebra `A`. No
analysis, no limit and no numerical value is used. The associator itself is **not** an input
here. It enters once the rational associator is built in every degree (stage 5 of the
Bar-Natan plan).
-/

namespace QOU.BraidsAndKnots.HAdicDrinfeld

open scoped TensorProduct
open QOU.HeckeTemperleyLieb.QuasiYangBaxterFromHexagon
open QOU.BraidsAndKnots.RationalAssociator

variable {k A : Type*} [CommRing k] [Ring A] [Algebra k A]

/-- The data `(Δ, t)` from which the h-adic Drinfeld category is built.

* `Δ` is cocommutative;
* `t` commutes with every `Δ(a)` (invariance);
* `t` is symmetric;
* `(Δ ⊗ id)(t) = t₁₃ + t₂₃` and `(id ⊗ Δ)(t) = t₁₂ + t₁₃` (the two splitting identities; they
  hold for `t = Σ xᵢ ⊗ xⁱ` with every `xᵢ` primitive). -/
structure CasimirData (k A : Type*) [CommRing k] [Ring A] [Algebra k A] where
  /-- The coproduct. -/
  Δ : A →ₐ[k] A ⊗[k] A
  /-- The invariant tensor. -/
  t : A ⊗[k] A
  cocomm : ∀ a, Algebra.TensorProduct.comm k A A (Δ a) = Δ a
  invariant : ∀ a, Commute t (Δ a)
  symm : Algebra.TensorProduct.comm k A A t = t
  split_left : Algebra.TensorProduct.map Δ (AlgHom.id k A) t = leg13 t + leg23 t
  split_right :
    (Algebra.TensorProduct.assoc k k A A A).symm (Algebra.TensorProduct.map (AlgHom.id k A) Δ t) =
      leg12 t + leg13 t

namespace CasimirData

variable (D : CasimirData k A)

theorem leg12_mul (x y : A ⊗[k] A) : leg12 (x * y) = leg12 x * leg12 y := by
  simp [leg12, Algebra.TensorProduct.tmul_mul_tmul]

theorem leg12_add (x y : A ⊗[k] A) : leg12 (x + y) = leg12 x + leg12 y := by
  simp [leg12, TensorProduct.add_tmul]

/-- `x₂₃` is `(1 ⊗ x)` re-associated. -/
theorem leg23_eq_assoc (x : A ⊗[k] A) :
    leg23 x = (Algebra.TensorProduct.assoc k k A A A).symm ((1 : A) ⊗ₜ[k] x) := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul a b => simp [leg23, Algebra.TensorProduct.map_tmul,
      Algebra.TensorProduct.includeRight_apply]
  | add x y hx hy => rw [map_add, hx, hy, TensorProduct.tmul_add, map_add]

theorem tau12_leg12 (x : A ⊗[k] A) :
    tau12 (leg12 x) = leg12 (Algebra.TensorProduct.comm k A A x) := by
  simp [tau12, leg12, Algebra.TensorProduct.map_tmul]

/-- `t₁₂` commutes with `(Δ ⊗ id)(X)` for every `X`. -/
theorem commute_leg12_mapLeft (X : A ⊗[k] A) :
    Commute (leg12 D.t) (Algebra.TensorProduct.map D.Δ (AlgHom.id k A) X) := by
  induction X using TensorProduct.induction_on with
  | zero => simp
  | tmul a b =>
    simp only [leg12, Algebra.TensorProduct.map_tmul, AlgHom.id_apply]
    exact (Commute.tmul (D.invariant a) (Commute.one_left b))
  | add x y hx hy => rw [map_add]; exact hx.add_right hy

/-- `t₂₃` commutes with `(id ⊗ Δ)(X)`, re-associated, for every `X`. -/
theorem commute_leg23_mapRight (X : A ⊗[k] A) :
    Commute (leg23 D.t) ((Algebra.TensorProduct.assoc k k A A A).symm
      (Algebra.TensorProduct.map (AlgHom.id k A) D.Δ X)) := by
  rw [leg23_eq_assoc]
  apply Commute.map
  induction X using TensorProduct.induction_on with
  | zero => simp
  | tmul a b =>
    simp only [Algebra.TensorProduct.map_tmul, AlgHom.id_apply]
    exact Commute.tmul (Commute.one_left a) (D.invariant b)
  | add x y hx hy => rw [map_add]; exact hx.add_right hy

/-- **The leg copies of `t` form a Drinfeld–Kohno family.** -/
theorem dk3 : DK3 (leg12 D.t) (leg13 D.t) (leg23 D.t) := by
  have h12 : Commute (leg12 D.t) (leg13 D.t + leg23 D.t) := by
    rw [← D.split_left]; exact D.commute_leg12_mapLeft D.t
  have h23 : Commute (leg23 D.t) (leg12 D.t + leg13 D.t) := by
    rw [← D.split_right]; exact D.commute_leg23_mapRight D.t
  have h13 : Commute (leg13 D.t) (leg12 D.t + leg23 D.t) := by
    have := h23.map tau12
    rwa [map_add, tau12_leg23, tau12_leg12, D.symm, tau12_leg13] at this
  exact ⟨h12, h13, h23⟩

/-- **Rescaling.** `(c t₁₂, c t₁₃, c t₂₃)` is again a Drinfeld–Kohno family, for every scalar
`c ∈ k`. With `k = ℚ[h]/(h^N)` and `c = h` this is the family at which a rational associator is
evaluated. -/
theorem dk3_smul (c : k) :
    DK3 (c • leg12 D.t) (c • leg13 D.t) (c • leg23 D.t) := by
  obtain ⟨h12, h13, h23⟩ := D.dk3
  refine ⟨?_, ?_, ?_⟩
  · rw [← smul_add]; exact (h12.smul_left c).smul_right c
  · rw [← smul_add]; exact (h13.smul_left c).smul_right c
  · rw [← smul_add]; exact (h23.smul_left c).smul_right c

/-- **Quasi-cocommutativity of every polynomial in `t`.** For `R = p(t)`,
`Δᵒᵖ(a) · R = R · Δ(a)`. This is the hypothesis `hR` of `quasiYBE_of_hexagon`. -/
theorem quasiCocomm_aeval (p : Polynomial k) (a : A) :
    Algebra.TensorProduct.comm k A A (D.Δ a) * Polynomial.aeval D.t p =
      Polynomial.aeval D.t p * D.Δ a := by
  rw [D.cocomm a]
  have hc : Commute (D.Δ a) (Polynomial.aeval D.t p) := by
    induction p using Polynomial.induction_on' with
    | add p q hp hq => rw [map_add]; exact hp.add_right hq
    | monomial n c =>
      rw [Polynomial.aeval_monomial]
      exact (show Commute (D.Δ a) (algebraMap k (A ⊗[k] A) c) from
        (Algebra.commutes c (D.Δ a)).symm).mul_right ((D.invariant a).symm.pow_right n)
  exact hc.eq

end CasimirData

end QOU.BraidsAndKnots.HAdicDrinfeld
