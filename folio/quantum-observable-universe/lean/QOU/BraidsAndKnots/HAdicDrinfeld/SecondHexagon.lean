import QOU.BraidsAndKnots.HAdicDrinfeld.Hexagon

/-!
# The second hexagon for `R = E(h t)`

Epic `qou-dk7p`, step C of `docs/audits/2026-11-27-kz-trio-strangler-plan.md`.

`Hexagon.lean` gives `(Δ ⊗ id)(R)`. A quasitriangular structure also needs `(id ⊗ Δ)(R)`. The
hexagon in `U4 N` is stated at the universal family `(t₁₂, t₁₃, t₂₃)`; realising it at the
reversed family `(t₂₃, t₁₃, t₁₂)` (again a Drinfeld–Kohno family, since the three relations
are symmetric under `1 ↔ 3`) gives the second hexagon

  `(id ⊗ Δ)(R) = φ(c t₁₃, c t₂₃) · R₁₃ · φ(c t₁₂, c t₁₃) · R₁₂ · φ(c t₂₃, c t₁₂)`.

* `DK3.reverse`: `(t₂₃, t₁₃, t₁₂)` is a `DK3` family;
* `realizeRev`: `U4 N → A^{⊗3}` with `t₁₂ ↦ c t₂₃`, `t₁₃ ↦ c t₁₃`, `t₂₃ ↦ c t₁₂`;
* `hexagon2`: the displayed identity.

The hypothesis is the hexagon in `U4 N` for the exponential `E`. No analysis is used.
-/

namespace QOU.BraidsAndKnots.HAdicDrinfeld

open scoped TensorProduct
open QOU.HeckeTemperleyLieb.QuasiYangBaxterFromHexagon
open QOU.BraidsAndKnots.RationalAssociator

set_option linter.unusedSectionVars false

theorem DK3.reverse {R : Type*} [Ring R] {a b c : R} (h : DK3 a b c) : DK3 c b a :=
  ⟨by rw [add_comm]; exact h.n23_1, by rw [add_comm]; exact h.n13_2,
    by rw [add_comm]; exact h.n12_3⟩

variable {k A : Type*} [CommRing k] [Algebra ℚ k] [Ring A] [Algebra k A] [Algebra ℚ A]
  [IsScalarTower ℚ k A]

namespace CasimirData

variable (D : CasimirData k A)

/-- The reversed three-strand family `(t₂₃, t₁₃, 0, t₁₂, 0, 0)`. -/
noncomputable def t3rev : Fin 6 → T3 k A := ![leg23 D.t, leg13 D.t, 0, leg12 D.t, 0, 0]

theorem dk4_t3rev : DK4 (D.t3rev 0) (D.t3rev 1) (D.t3rev 2) (D.t3rev 3) (D.t3rev 4) (D.t3rev 5) :=
  (DK3.reverse D.dk3).toDK4

/-- The realisation of `U4 N` at the reversed family. -/
noncomputable def realizeRev (N : ℕ) (c : k) (hc : c ^ N = 0) : U4 N →ₐ[ℚ] T3 k A :=
  HAdicDrinfeld.evalU4 N (z := algebraMap k (T3 k A) c) (fun y => Algebra.commutes c y)
    (by rw [← map_pow, hc, map_zero]) D.t3rev D.dk4_t3rev

theorem realizeRev_t (N : ℕ) (c : k) (hc : c ^ N = 0) (i : Fin 6) :
    D.realizeRev N c hc (RationalAssociator.t N i) = c • D.t3rev i := by
  rw [realizeRev, HAdicDrinfeld.evalU4_t]
  exact (Algebra.smul_def (A := T3 k A) c (D.t3rev i)).symm

theorem mapRight_eval (E : FreeAlgebra ℚ (Fin 2)) (x : A ⊗[k] A) :
    (Algebra.TensorProduct.assoc k k A A A).symm
        (Algebra.TensorProduct.map (AlgHom.id k A) D.Δ (eval x 0 E)) =
      eval ((Algebra.TensorProduct.assoc k k A A A).symm
        (Algebra.TensorProduct.map (AlgHom.id k A) D.Δ x)) 0 E := by
  simpa using map_eval (((Algebra.TensorProduct.assoc k k A A A).symm.toAlgHom.comp
    (Algebra.TensorProduct.map (AlgHom.id k A) D.Δ)).restrictScalars ℚ) x 0 E

variable {N : ℕ} (E : FreeAlgebra ℚ (Fin 2)) (c : k)

/-- **The second hexagon for `R = E(c t)`.** If `Φ` satisfies the hexagon in `U4 N` with
exponential `E`, then

  `(id ⊗ Δ)(R) = φ(c t₁₃, c t₂₃) · R₁₃ · φ(c t₁₂, c t₁₃) · R₁₂ · φ(c t₂₃, c t₁₂)`. -/
theorem hexagon2 (hc : c ^ N = 0) {Φ : FreeAlgebra ℚ (Fin 2)}
    (hhex : Hexagon Φ E (RationalAssociator.t N 0) (RationalAssociator.t N 1)
      (RationalAssociator.t N 3)) :
    (Algebra.TensorProduct.assoc k k A A A).symm
        (Algebra.TensorProduct.map (AlgHom.id k A) D.Δ (D.rMatrix E c)) =
      eval (c • leg13 D.t) (c • leg23 D.t) Φ * leg13 (D.rMatrix E c) *
        eval (c • leg12 D.t) (c • leg13 D.t) Φ * leg12 (D.rMatrix E c) *
        eval (c • leg23 D.t) (c • leg12 D.t) Φ := by
  have key := congrArg (D.realizeRev N c hc) hhex
  have hm : ∀ a b p, D.realizeRev N c hc (eval a b p) =
      eval (D.realizeRev N c hc a) (D.realizeRev N c hc b) p := fun a b p =>
    map_eval (A := U4 N) (B := T3 k A) (D.realizeRev N c hc) a b p
  simp only [map_mul, hm, map_add, map_zero, realizeRev_t] at key
  simp only [t3rev, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val] at key
  rw [rMatrix, mapRight_eval, leg13_eval, leg12_eval]
  simp only [map_smul, leg12_smul, D.split_right, smul_add]
  rw [add_comm]
  exact key

end CasimirData

end QOU.BraidsAndKnots.HAdicDrinfeld
