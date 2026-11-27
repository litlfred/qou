import QOU.BraidsAndKnots.HAdicDrinfeld.FourStrand
import QOU.BraidsAndKnots.RationalAssociator.QuasiYBE

/-!
# The hexagon for `R = E(h t)` from a rational associator

Epic `qou-dk7p`, step B of `docs/audits/2026-11-27-kz-trio-strangler-plan.md`.

`RationalAssociator/QuasiYBE.lean` (stage 5) proves the hexagon and the quasi-Yang–Baxter
equation for a rational associator `Φ` in the universal truncated algebra `U4 N`, and transports
them along any realisation `ρ : U4 N → (A ⊗ A) ⊗ A` that sends `E(t₁₃ + t₂₃)`, `E(t₁₃)`,
`E(t₂₃)` to `(Δ ⊗ id)(R)`, `R₁₃`, `R₂₃`. Its docstring records that such a realisation by a
Casimir tensor was not available. This file provides one.

Let `D : CasimirData k A` (cocommutative `Δ`, symmetric invariant `t` with the two splitting
identities), with `k` a `ℚ`-algebra, and let `c ∈ k` with `c ^ N = 0`. For `k = ℚ[h]/(h^N)` take
`c = h`. Then:

* `realize3`: the algebra map `U4 N →ₐ[ℚ] (A ⊗ A) ⊗ A` with `t₁₂, t₁₃, t₂₃ ↦ c t₁₂, c t₁₃, c t₂₃`
  and `t₁₄, t₂₄, t₃₄ ↦ 0`. Its `DK4` hypothesis is `CasimirData.dk3` extended by `DK3.toDK4`;
* `rMatrix`: `R = E(c t) ∈ A ⊗ A`. For `E = exp(X/2)` truncated at degree `N` this is
  `exp(h t / 2)` modulo `h^N`;
* `rMatrix_quasiCocomm`: `Δᵒᵖ(a) R = R Δ(a)`;
* `hexagon`: for every rational associator `Φ` in `U4 N` with exponential `E`,
  `(Δ ⊗ id)(R) = Φ₃₁₂ · R₁₃ · Φ₁₃₂⁻¹ · R₂₃ · Φ₁₂₃`, with the three associator factors the
  `realize3`-images of `φ(t₁₃,t₁₂)`, `φ(t₂₃,t₁₃)`, `φ(t₁₂,t₂₃)`;
* `quasiYBE`: the quasi-Yang–Baxter equation in `(A ⊗ A) ⊗ A`, from `quasiYBE_of_hexagon`.

No analysis and no numerical value is used. The associator is a hypothesis (`AssocU4 N E Φ`),
which stage 5 supplies.
-/

namespace QOU.BraidsAndKnots.HAdicDrinfeld

open scoped TensorProduct
open QOU.HeckeTemperleyLieb.QuasiYangBaxterFromHexagon
open QOU.BraidsAndKnots.RationalAssociator

set_option linter.unusedSectionVars false

variable {k A : Type*} [CommRing k] [Algebra ℚ k] [Ring A] [Algebra k A] [Algebra ℚ A]
  [IsScalarTower ℚ k A]

/-- `A^{⊗3}`, associated to the left. -/
abbrev T3 (k A : Type*) [CommRing k] [Ring A] [Algebra k A] := (A ⊗[k] A) ⊗[k] A

namespace CasimirData

variable (D : CasimirData k A)

/-- The three-strand family `(t₁₂, t₁₃, 0, t₂₃, 0, 0)`, in the order of `UniversalDK.t`. -/
noncomputable def t3 : Fin 6 → T3 k A := ![leg12 D.t, leg13 D.t, 0, leg23 D.t, 0, 0]

theorem dk4_t3 : DK4 (D.t3 0) (D.t3 1) (D.t3 2) (D.t3 3) (D.t3 4) (D.t3 5) :=
  D.dk3.toDK4

/-- **The realisation of `U4 N` on three strands**, `tᵢⱼ ↦ c tᵢⱼ` for `i, j ≤ 3` and
`tᵢ₄ ↦ 0`. -/
noncomputable def realize3 (N : ℕ) (c : k) (hc : c ^ N = 0) : U4 N →ₐ[ℚ] T3 k A :=
  HAdicDrinfeld.evalU4 N (z := algebraMap k (T3 k A) c) (fun y => Algebra.commutes c y)
    (by rw [← map_pow, hc, map_zero]) D.t3 D.dk4_t3

theorem realize3_t (N : ℕ) (c : k) (hc : c ^ N = 0) (i : Fin 6) :
    D.realize3 N c hc (RationalAssociator.t N i) = c • D.t3 i := by
  rw [realize3, HAdicDrinfeld.evalU4_t]
  exact (Algebra.smul_def (A := T3 k A) c (D.t3 i)).symm

/-- `R = E(c t)`. -/
noncomputable def rMatrix (E : FreeAlgebra ℚ (Fin 2)) (c : k) : A ⊗[k] A :=
  eval (c • D.t) 0 E

/-- **Quasi-cocommutativity of `R`.** -/
theorem rMatrix_quasiCocomm (E : FreeAlgebra ℚ (Fin 2)) (c : k) (a : A) :
    Algebra.TensorProduct.comm k A A (D.Δ a) * D.rMatrix E c =
      D.rMatrix E c * D.Δ a := by
  rw [D.cocomm a]
  exact (commute_eval ((D.invariant a).smul_left c) (Commute.zero_left _) E).eq.symm

theorem leg12_smul (c : k) (x : A ⊗[k] A) : leg12 (c • x) = c • leg12 x := by
  simp [leg12, TensorProduct.smul_tmul']

theorem leg12_eval (E : FreeAlgebra ℚ (Fin 2)) (x : A ⊗[k] A) :
    leg12 (eval x 0 E) = eval (leg12 x) 0 E := by
  have h := map_eval ((Algebra.TensorProduct.includeLeft :
    A ⊗[k] A →ₐ[k] T3 k A).restrictScalars ℚ) x 0 E
  simpa [leg12, Algebra.TensorProduct.includeLeft_apply] using h

theorem leg13_eval (E : FreeAlgebra ℚ (Fin 2)) (x : A ⊗[k] A) :
    leg13 (eval x 0 E) = eval (leg13 x) 0 E := by
  simpa using map_eval ((leg13 : A ⊗[k] A →ₐ[k] T3 k A).restrictScalars ℚ) x 0 E

theorem leg23_eval (E : FreeAlgebra ℚ (Fin 2)) (x : A ⊗[k] A) :
    leg23 (eval x 0 E) = eval (leg23 x) 0 E := by
  simpa using map_eval ((leg23 : A ⊗[k] A →ₐ[k] T3 k A).restrictScalars ℚ) x 0 E

theorem mapLeft_eval (E : FreeAlgebra ℚ (Fin 2)) (x : A ⊗[k] A) :
    Algebra.TensorProduct.map D.Δ (AlgHom.id k A) (eval x 0 E) =
      eval (Algebra.TensorProduct.map D.Δ (AlgHom.id k A) x) 0 E := by
  simpa using map_eval ((Algebra.TensorProduct.map D.Δ (AlgHom.id k A)).restrictScalars ℚ) x 0 E

variable {N : ℕ} (E : FreeAlgebra ℚ (Fin 2)) (c : k) (hc : c ^ N = 0)

theorem realize3_R12 : D.realize3 N c hc (eval (RationalAssociator.t N 0) 0 E) = leg12 (D.rMatrix E c) := by
  rw [map_eval, map_zero, realize3_t, rMatrix, leg12_eval, leg12_smul]; rfl

theorem realize3_R13 : D.realize3 N c hc (eval (RationalAssociator.t N 1) 0 E) = leg13 (D.rMatrix E c) := by
  rw [map_eval, map_zero, realize3_t, rMatrix, leg13_eval, map_smul]; rfl

theorem realize3_R23 : D.realize3 N c hc (eval (RationalAssociator.t N 3) 0 E) = leg23 (D.rMatrix E c) := by
  rw [map_eval, map_zero, realize3_t, rMatrix, leg23_eval, map_smul]; rfl

theorem realize3_coproduct :
    D.realize3 N c hc (eval (RationalAssociator.t N 1 + RationalAssociator.t N 3) 0 E) =
      Algebra.TensorProduct.map D.Δ (AlgHom.id k A) (D.rMatrix E c) := by
  rw [map_eval, map_zero, map_add, realize3_t, realize3_t, rMatrix, mapLeft_eval, map_smul,
    D.split_left, smul_add]; rfl

/-- **The hexagon for `R = E(c t)`.** For a rational associator `Φ` in `U4 N` with
exponential `E`,

  `(Δ ⊗ id)(R) = ρ φ(t₁₃,t₁₂) · R₁₃ · ρ φ(t₂₃,t₁₃) · R₂₃ · ρ φ(t₁₂,t₂₃)`,

with `ρ = realize3`. -/
theorem hexagon {Φ : FreeAlgebra ℚ (Fin 2)} (hΦ : AssocU4 N E Φ) :
    Algebra.TensorProduct.map D.Δ (AlgHom.id k A) (D.rMatrix E c) =
      D.realize3 N c hc (eval (RationalAssociator.t N 1) (RationalAssociator.t N 0) Φ) * leg13 (D.rMatrix E c) *
        D.realize3 N c hc (eval (RationalAssociator.t N 3) (RationalAssociator.t N 1) Φ) * leg23 (D.rMatrix E c) *
        D.realize3 N c hc (eval (RationalAssociator.t N 0) (RationalAssociator.t N 3) Φ) := by
  have key := congrArg (D.realize3 N c hc) hΦ.hex
  simp only [map_mul] at key
  rw [D.realize3_coproduct E c hc, D.realize3_R13 E c hc, D.realize3_R23 E c hc] at key
  exact key

/-- **The quasi-Yang–Baxter equation for `R = E(c t)` and a rational associator.** -/
theorem quasiYBE {Φ : FreeAlgebra ℚ (Fin 2)} (hΦ : AssocU4 N E Φ) :
    leg12 (D.rMatrix E c) *
        (D.realize3 N c hc (eval (RationalAssociator.t N 1) (RationalAssociator.t N 0) Φ) * leg13 (D.rMatrix E c) *
          D.realize3 N c hc (eval (RationalAssociator.t N 3) (RationalAssociator.t N 1) Φ) * leg23 (D.rMatrix E c) *
          D.realize3 N c hc (eval (RationalAssociator.t N 0) (RationalAssociator.t N 3) Φ)) =
      tau12 (D.realize3 N c hc (eval (RationalAssociator.t N 1) (RationalAssociator.t N 0) Φ)) * leg23 (D.rMatrix E c) *
        tau12 (D.realize3 N c hc (eval (RationalAssociator.t N 3) (RationalAssociator.t N 1) Φ)) * leg13 (D.rMatrix E c) *
        tau12 (D.realize3 N c hc (eval (RationalAssociator.t N 0) (RationalAssociator.t N 3) Φ)) * leg12 (D.rMatrix E c) :=
  quasiYBE_of_hexagon D.Δ (D.rMatrix E c) (D.rMatrix_quasiCocomm E c) _ _ _
    (D.hexagon E c hc hΦ)

end CasimirData

end QOU.BraidsAndKnots.HAdicDrinfeld
