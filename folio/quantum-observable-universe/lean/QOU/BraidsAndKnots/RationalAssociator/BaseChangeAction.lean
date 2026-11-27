import QOU.BraidsAndKnots.RationalAssociator.BaseChange
import QOU.BraidsAndKnots.RationalAssociator.GRTFlowExact

/-!
# Step 1 of gap B1: a rational `GRT₁` element acts on `K`-associators

Bean `qou-3fdg` (epic `qou-dk7p`), plan `docs/audits/2026-11-27-grt-action-pentagon-derivation.md`
§14 step (1), write-up §16b.

`AssocK K N E Φ` (`BaseChange.lean`) is an associator with coefficients in a field `K ⊇ ℚ`,
evaluated in `K ⊗ U4 N`. For a rational `g` satisfying `GRT1U4 N g`, Drinfeld's right action
`Φ ∘ g = Φ(g A g⁻¹, B) · g` is, written without inverses through (5.12),

  `compK Φ g = Φ(g · A · g(B, A), B) · g`,

the base change of `compPoly` in its first argument. `assocK_compK` proves
`AssocK K N E Φ → GRT1U4 N g → AssocK K N E (compK Φ g)`.

## How

The action theorems of `GRTAction.lean` and `HexagonAction.lean` use `φ` only through the
conjugation identity `φ(u⁻¹ a u, u⁻¹ b u) = u⁻¹ φ(a, b) u`. They are repeated here for an
arbitrary function `f : R → R → R` with that property (`pentagon_actF`,
`hexagon_act_of_transportF`). For `f = evK · · Φ` the property is `evK_conj`.

The transported family of a rational `g` is rational. So the pentagon of `Φ` at the
transported family follows from its pentagon at the universal family by the base change
`id_K ⊗ lift` of the rational transport map, which commutes with `evK` (`map_evK`). The far
relation and the Drinfeld–Kohno property of the transported family are the rational results
`far_of_tcompat` and `transported_dk4`, used unchanged.

Nothing analytic is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator
open TensorProduct

/-! ### The action theorems for an evaluation function -/

section Generic

variable {R : Type*} [Ring R] [Algebra ℚ R]

/-- `f(G a G⁻¹, b) · G`: the right action at a pair, for an evaluation function `f`. -/
noncomputable def actEvalF (f : R → R → R) (a b : R) (G : Rˣ) : R :=
  f ((G : R) * a * ↑G⁻¹) b * G

variable (f : R → R → R)
  (hf : ∀ (u : Rˣ) (a b : R),
    f ((↑u⁻¹ : R) * a * u) ((↑u⁻¹ : R) * b * u) = (↑u⁻¹ : R) * f a b * u)
include hf

omit [Algebra ℚ R] in
/-- `f(G a G⁻¹, b) · G = G · f(a, G⁻¹ b G)`. -/
theorem actEvalF_eq (a b : R) (G : Rˣ) :
    actEvalF f a b G = (G : R) * f a ((↑G⁻¹ : R) * b * G) := by
  have h := hf G⁻¹ a ((↑G⁻¹ : R) * b * G)
  simp only [inv_inv] at h
  have hb : (G : R) * ((↑G⁻¹ : R) * b * G) * ↑G⁻¹ = b := by
    simp only [mul_assoc, Units.mul_inv_cancel_left, Units.mul_inv, mul_one]
  rw [hb] at h
  unfold actEvalF
  rw [h]
  simp only [mul_assoc, Units.inv_mul, mul_one]
/-- **Pentagon preservation under the `GRT` action (conditional on the transported family).**
If `g` satisfies the pentagon at a `DK4` family `t` (its five coface evaluations being the units
`Ga … Ge`), and `φ` satisfies the pentagon at the transported family `s`, then
`φ̃(A, B) = φ(g A g⁻¹, B) · g` satisfies the pentagon at `t`. -/
theorem pentagon_actF (g : FreeAlgebra ℚ (Fin 2)) {t12 t13 t14 t23 t24 t34 : R}
    (hDK : DK4 t12 t13 t14 t23 t24 t34) (Ga Gb Gc Gd Ge : Rˣ)
    (ha : (Ga : R) = eval t12 t23 g) (hb : (Gb : R) = eval (t13 + t23) t34 g)
    (hc : (Gc : R) = eval t12 (t23 + t24) g) (hd : (Gd : R) = eval (t12 + t13) (t24 + t34) g)
    (he : (Ge : R) = eval t23 t34 g)
    (hg : Pentagon g t12 t13 t23 t24 t34)
    (hφ : let s := transported t12 t13 t23 t24 t34 Ga Gb Gc
      PentagonF f s.1 s.2.1 s.2.2.1 s.2.2.2.1 s.2.2.2.2) :
    actEvalF f t12 (t23 + t24) Gc * actEvalF f (t13 + t23) t34 Gb =
      actEvalF f t23 t34 Ge * actEvalF f (t12 + t13) (t24 + t34) Gd * actEvalF f t12 t23 Ga := by
  -- the units' pentagon `Gc Gb = Ge Gd Ga`
  have hP : Gc * Gb = Ge * Gd * Ga := by
    ext; simp only [Units.val_mul]; rw [ha, hb, hc, hd, he]; exact hg
  -- commutation facts, all from `DK4`
  have cb12 : Commute (Gb : R) t12 := hb ▸ commute_eval hDK.n12_3.symm hDK.f12_34.symm g
  have cc34 : Commute (Gc : R) t34 :=
    hc ▸ commute_eval hDK.f12_34 hDK.n34_2.symm g
  have cd23 : Commute (Gd : R) t23 :=
    hd ▸ commute_eval hDK.n23_1.symm hDK.n23_4.symm g
  have ca3 : Commute (Ga : R) (t12 + t13 + t23) := by
    rw [ha]
    refine commute_eval ?_ ?_ g
    · have := hDK.n12_3; rw [show t12 + t13 + t23 = t12 + (t13 + t23) by abel]
      exact (Commute.refl t12).add_right this
    · have := hDK.n23_1; rw [show t12 + t13 + t23 = (t12 + t13) + t23 by abel]
      exact this.add_right (Commute.refl t23)
  have ce3 : Commute (Ge : R) (t23 + t24 + t34) := by
    rw [he]
    refine commute_eval ?_ ?_ g
    · rw [show t23 + t24 + t34 = t23 + (t24 + t34) by abel]
      exact (Commute.refl t23).add_right hDK.n23_4
    · rw [show t23 + t24 + t34 = (t23 + t24) + t34 by abel]
      exact hDK.n34_2.add_right (Commute.refl t34)
  have hP' : Gc * Gb = Ge * (Gd * Ga) := by rw [hP, mul_assoc]
  have F1 : (↑(Gc * Gb)⁻¹ : R) * t34 * ↑(Gc * Gb) = (↑Gb⁻¹ : R) * t34 * Gb :=
    conj_mul_of_commute cc34
  have F2 : (↑(Gd * Ga)⁻¹ : R) * t23 * ↑(Gd * Ga) = (↑Ga⁻¹ : R) * t23 * Ga :=
    conj_mul_of_commute cd23
  have F3 : (↑(Gc * Gb)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gc * Gb) =
      (↑(Gd * Ga)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gd * Ga) := by
    rw [hP']; exact conj_mul_of_commute ce3
  simp only [transported, PentagonF] at hφ
  have k1 : ∀ x y : R, x + (y - x) = y := fun x y => by abel
  have k2 : ∀ x y : R, y - x + x = y := fun x y => by abel
  rw [k1, k2] at hφ
  -- the five factors, rewritten
  have eL1 : (↑Gb⁻¹ : R) * f t12 ((↑Gc⁻¹ : R) * (t23 + t24) * Gc) * Gb =
      f t12 ((↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb)) := by
    have a2 : (↑Gb⁻¹ : R) * ((↑Gc⁻¹ : R) * (t23 + t24) * Gc) * Gb =
        (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) := by
      simp only [mul_inv_rev, Units.val_mul]; noncomm_ring
    rw [← hf, conj_of_commute cb12, a2]
  have eR1 : (↑(Gd * Ga)⁻¹ : R) * f t23 ((↑Ge⁻¹ : R) * t34 * Ge) * ↑(Gd * Ga) =
      f ((↑Ga⁻¹ : R) * t23 * Ga) ((↑Gb⁻¹ : R) * t34 * Gb) := by
    have a2 : (↑(Gd * Ga)⁻¹ : R) * ((↑Ge⁻¹ : R) * t34 * Ge) * ↑(Gd * Ga) =
        (↑Gb⁻¹ : R) * t34 * Gb := by
      rw [← F1, hP']; simp only [mul_inv_rev, Units.val_mul]; noncomm_ring
    rw [← hf, F2, a2]
  have eR2 : (↑Ga⁻¹ : R) * f (t12 + t13) ((↑Gd⁻¹ : R) * (t24 + t34) * Gd) * Ga =
      f (t12 + (t13 + t23 - (↑Ga⁻¹ : R) * t23 * Ga))
        ((↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) - (↑Ga⁻¹ : R) * t23 * Ga +
          (↑Gb⁻¹ : R) * t34 * Gb) := by
    have a1 : (↑Ga⁻¹ : R) * (t12 + t13) * Ga =
        t12 + (t13 + t23 - (↑Ga⁻¹ : R) * t23 * Ga) := by
      have : (↑Ga⁻¹ : R) * (t12 + t13) * Ga =
          (↑Ga⁻¹ : R) * (t12 + t13 + t23) * Ga - (↑Ga⁻¹ : R) * t23 * Ga := by noncomm_ring
      rw [this, conj_of_commute ca3]; abel
    have a2 : (↑Ga⁻¹ : R) * ((↑Gd⁻¹ : R) * (t24 + t34) * Gd) * Ga =
        (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) - (↑Ga⁻¹ : R) * t23 * Ga +
          (↑Gb⁻¹ : R) * t34 * Gb := by
      have b1 : (↑Ga⁻¹ : R) * ((↑Gd⁻¹ : R) * (t24 + t34) * Gd) * Ga =
          (↑(Gd * Ga)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gd * Ga) -
            (↑(Gd * Ga)⁻¹ : R) * t23 * ↑(Gd * Ga) := by
        simp only [mul_inv_rev, Units.val_mul]; noncomm_ring
      have b2 : (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) =
          (↑(Gc * Gb)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gc * Gb) -
            (↑(Gc * Gb)⁻¹ : R) * t34 * ↑(Gc * Gb) := by noncomm_ring
      rw [b1, b2, F3, F2, F1]; abel
    rw [← hf, a1, a2]
  -- assemble
  simp only [actEvalF_eq f hf]
  have lhs : (Gc : R) * f t12 ((↑Gc⁻¹ : R) * (t23 + t24) * Gc) *
      ((Gb : R) * f (t13 + t23) ((↑Gb⁻¹ : R) * t34 * Gb)) =
      ↑(Gc * Gb) * ((↑Gb⁻¹ : R) * f t12 ((↑Gc⁻¹ : R) * (t23 + t24) * Gc) * Gb) *
        f (t13 + t23) ((↑Gb⁻¹ : R) * t34 * Gb) := by
    simp only [Units.val_mul, mul_assoc, Units.mul_inv_cancel_left]
  have rhs : (Ge : R) * f t23 ((↑Ge⁻¹ : R) * t34 * Ge) *
      ((Gd : R) * f (t12 + t13) ((↑Gd⁻¹ : R) * (t24 + t34) * Gd)) *
      ((Ga : R) * f t12 ((↑Ga⁻¹ : R) * t23 * Ga)) =
      ↑(Ge * (Gd * Ga)) *
        ((↑(Gd * Ga)⁻¹ : R) * f t23 ((↑Ge⁻¹ : R) * t34 * Ge) * ↑(Gd * Ga)) *
        ((↑Ga⁻¹ : R) * f (t12 + t13) ((↑Gd⁻¹ : R) * (t24 + t34) * Gd) * Ga) *
        f t12 ((↑Ga⁻¹ : R) * t23 * Ga) := by
    simp only [mul_inv_rev, Units.val_mul, mul_assoc, Units.mul_inv_cancel_left]
  rw [lhs, rhs, eL1, eR1, eR2, ← hP', mul_assoc, hφ]
  simp only [mul_assoc]

/-- **The hexagon under the action, given the hexagon of `f` at the transported family.** -/
theorem hexagon_act_of_transportF (g E : FreeAlgebra ℚ (Fin 2)) {t12 t13 t23 : R}
    (G1 G2 G3 : Rˣ)
    (h1 : (G1 : R) = eval t13 t12 g) (h2 : (G2 : R) = eval t23 t13 g)
    (h3 : (G3 : R) = eval t12 t23 g)
    (h514 : eval t23 t13 g * eval t12 t23 g * eval t13 t12 g = 1)
    (hsum : (G1 : R) * t13 * ↑G1⁻¹ + (↑G3⁻¹ : R) * t23 * G3 = t13 + t23)
    (hφ : HexagonF f E t12 ((G1 : R) * t13 * ↑G1⁻¹) ((↑G3⁻¹ : R) * t23 * G3)) :
    eval (t13 + t23) 0 E =
      actEvalF f t13 t12 G1 * eval t13 0 E * actEvalF f t23 t13 G2 * eval t23 0 E *
        actEvalF f t12 t23 G3 := by
  have hZ : G2 * G3 = G1⁻¹ :=
    eq_inv_of_mul_eq_one_left (Units.ext (by simp [h1, h2, h3, h514]))
  have hG1 : G1 = (G2 * G3)⁻¹ := by rw [hZ, inv_inv]
  unfold HexagonF at hφ
  rw [hsum] at hφ
  rw [hφ]
  clear h1 h2 h3 h514 hsum hφ hZ
  subst hG1
  -- the five factors, one at a time
  have f1 : f ((↑(G2 * G3)⁻¹ : R) * t13 * ↑(G2 * G3)⁻¹⁻¹) t12 =
      actEvalF f t13 t12 (G2 * G3)⁻¹ * ↑(G2 * G3) := by
    simp only [actEvalF, inv_inv, mul_assoc, Units.inv_mul, mul_one]
  have f2 : eval ((↑(G2 * G3)⁻¹ : R) * t13 * ↑(G2 * G3)⁻¹⁻¹) 0 E =
      (↑(G2 * G3)⁻¹ : R) * eval t13 0 E * ↑(G2 * G3) := by
    simpa using eval_conj_zero (G2 * G3) t13 E
  have f3 :
      f ((↑G3⁻¹ : R) * t23 * G3) ((↑(G2 * G3)⁻¹ : R) * t13 * ↑(G2 * G3)⁻¹⁻¹) =
      (↑(G2 * G3)⁻¹ : R) * actEvalF f t23 t13 G2 * G3 := by
    have e : (↑G3⁻¹ : R) * t23 * G3 =
        (↑(G2 * G3)⁻¹ : R) * ((G2 : R) * t23 * ↑G2⁻¹) * ↑(G2 * G3) := by
      simp only [mul_inv_rev, Units.val_mul, mul_assoc, Units.inv_mul_cancel_left]
    rw [e, inv_inv, hf]
    simp only [actEvalF, mul_inv_rev, Units.val_mul, mul_assoc]
  have f4 : eval ((↑G3⁻¹ : R) * t23 * G3) 0 E = (↑G3⁻¹ : R) * eval t23 0 E * G3 :=
    eval_conj_zero G3 t23 E
  have f5 : f t12 ((↑G3⁻¹ : R) * t23 * G3) = (↑G3⁻¹ : R) * actEvalF f t12 t23 G3 := by
    rw [actEvalF_eq f hf]; simp [← mul_assoc]
  rw [f1, f2, f3, f4, f5]
  simp only [mul_assoc, Units.mul_inv_cancel_left]



end Generic

/-! ### Evaluation with coefficients in `K` -/

section EvK

variable {K : Type*} [Field K] [Algebra ℚ K]
variable {S : Type*} [Ring S] [Algebra K S] [Algebra ℚ S] [IsScalarTower ℚ K S]
variable {S' : Type*} [Ring S'] [Algebra K S'] [Algebra ℚ S'] [IsScalarTower ℚ K S']

/-- A `K`-algebra map commutes with rational evaluation. -/
theorem map_eval_K (ψ : S →ₐ[K] S') (a b : S) (p : FreeAlgebra ℚ (Fin 2)) :
    ψ (eval a b p) = eval (ψ a) (ψ b) p :=
  map_eval (ψ.restrictScalars ℚ) a b p

/-- A `K`-algebra map commutes with evaluation of polynomials with coefficients in `K`. -/
theorem map_evK (ψ : S →ₐ[K] S') (a b : S) (Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) :
    ψ (evK a b Φ) = evK (ψ a) (ψ b) Φ := by
  induction Φ using TensorProduct.induction_on with
  | zero => simp
  | tmul k p => rw [evK_tmul, evK_tmul, map_mul, AlgHom.commutes, map_eval_K]
  | add x y hx hy => rw [map_add, map_add, map_add, hx, hy]

/-- Evaluation with coefficients in `K` commutes with conjugation by a unit. -/
theorem evK_conj (u : Sˣ) (a b : S) (Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) :
    evK ((↑u⁻¹ : S) * a * u) ((↑u⁻¹ : S) * b * u) Φ =
      (↑u⁻¹ : S) * evK a b Φ * u := by
  induction Φ using TensorProduct.induction_on with
  | zero => simp
  | tmul k p =>
    rw [evK_tmul, evK_tmul, eval_conj, ← mul_assoc, ← mul_assoc,
      Algebra.commutes k (↑u⁻¹ : S)]
    simp only [mul_assoc]
  | add x y hx hy => rw [map_add, map_add, hx, hy, mul_add, add_mul]

/-- Substitution in the second tensor factor, then evaluation, is evaluation at the
substituted values. -/
theorem evK_map_lift (a b : S) (p q : FreeAlgebra ℚ (Fin 2))
    (Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) :
    evK a b (Algebra.TensorProduct.map (AlgHom.id K K) (FreeAlgebra.lift ℚ ![p, q]) Φ) =
      evK (eval a b p) (eval a b q) Φ := by
  induction Φ using TensorProduct.induction_on with
  | zero => simp
  | tmul k x => simp only [Algebra.TensorProduct.map_tmul, AlgHom.id_apply, evK_tmul, eval_lift]
  | add x y hx hy => rw [map_add, map_add, map_add, hx, hy]

/-- **The right action of a rational `g` on `Φ ∈ K ⊗ ℚ⟨X, Y⟩`**, Drinfeld's (5.16) with
the inverse written through (5.12): `Φ(g · A · g(B, A), B) · g`. -/
noncomputable def compK (Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) (g : FreeAlgebra ℚ (Fin 2)) :
    K ⊗[ℚ] FreeAlgebra ℚ (Fin 2) :=
  Algebra.TensorProduct.map (AlgHom.id K K)
      (FreeAlgebra.lift ℚ ![g * FreeAlgebra.ι ℚ 0 * swapPoly g, FreeAlgebra.ι ℚ 1]) Φ *
    (1 : K) ⊗ₜ g

theorem evK_compK (a b : S) (Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2))
    (g : FreeAlgebra ℚ (Fin 2)) :
    evK a b (compK Φ g) = evK (eval a b g * a * eval b a g) b Φ * eval a b g := by
  rw [compK, map_mul, evK_map_lift, evK_one_tmul, map_mul, map_mul, eval_swapPoly]
  simp [eval]

end EvK

/-! ### `K ⊗ U4 N`: transfer from the universal family -/

section Transfer

variable {K : Type*} [Field K] [Algebra ℚ K] {N : ℕ}

theorem map_lift_ιK (L : U4 N →ₐ[ℚ] U4 N) (u : U4 N) :
    Algebra.TensorProduct.map (AlgHom.id K K) L (ιK K N u) = ιK K N (L u) := by
  simp

/-- **The pentagon of a `K`-associator transfers to every rational nilpotent `DK4` family.** -/
theorem pentK_of_universal {Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)}
    (hΦ : PentagonF (fun a b => evK a b Φ) (ιK K N (t N 0)) (ιK K N (t N 1)) (ιK K N (t N 3))
      (ιK K N (t N 4)) (ιK K N (t N 5)))
    (sf : Fin 6 → U4 N) (hdk : DK4 (sf 0) (sf 1) (sf 2) (sf 3) (sf 4) (sf 5))
    (hmem : ∀ i, sf i ∈ Fil N 1) :
    PentagonF (fun a b => evK a b Φ) (ιK K N (sf 0)) (ιK K N (sf 1)) (ιK K N (sf 3))
      (ιK K N (sf 4)) (ιK K N (sf 5)) := by
  have hw := word_eq_zero_of_Fil_one sf hmem
  have key := congrArg (Algebra.TensorProduct.map (AlgHom.id K K) (lift N sf hdk hw)) hΦ
  simp only [PentagonF, map_mul, map_evK, map_add, map_lift_ιK, lift_t] at key ⊢
  exact key

/-- **The hexagon of a `K`-associator transfers to every rational nilpotent `DK3` family.** -/
theorem hexK_of_universal {Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)} {E : FreeAlgebra ℚ (Fin 2)}
    (hΦ : HexagonF (fun a b => evK a b Φ) E (ιK K N (t N 0)) (ιK K N (t N 1)) (ιK K N (t N 3)))
    {s12 s13 s23 : U4 N} (hs : DK3 s12 s13 s23)
    (h12 : s12 ∈ Fil N 1) (h13 : s13 ∈ Fil N 1) (h23 : s23 ∈ Fil N 1) :
    HexagonF (fun a b => evK a b Φ) E (ιK K N s12) (ιK K N s13) (ιK K N s23) := by
  set sf : Fin 6 → U4 N := ![s12, s13, 0, s23, 0, 0] with hsf
  have hdk : DK4 (sf 0) (sf 1) (sf 2) (sf 3) (sf 4) (sf 5) := hs.toDK4
  have hmem : ∀ i, sf i ∈ Fil N 1 := by
    intro i
    fin_cases i
    · exact h12
    · exact h13
    · exact zero_mem _
    · exact h23
    · exact zero_mem _
    · exact zero_mem _
  have hw := word_eq_zero_of_Fil_one sf hmem
  have key := congrArg (Algebra.TensorProduct.map (AlgHom.id K K) (lift N sf hdk hw)) hΦ
  simp only [HexagonF, map_mul, map_evK, map_eval_K, map_add, map_zero, map_lift_ιK,
    lift_t] at key ⊢
  exact key

end Transfer


/-! ### Step (1): `AssocK` is closed under a rational `GRT₁` element -/

section Step1

variable {K : Type*} [Field K] [Algebra ℚ K] {N : ℕ}

/-- `ε(p)` is the value at `(0, 0)`. -/
theorem eval_zero_zero {R : Type*} [Ring R] [Algebra ℚ R] (p : FreeAlgebra ℚ (Fin 2)) :
    eval (0 : R) 0 p = algebraMap ℚ R (FreeAlgebra.algebraMapInv p) := by
  have : (eval (0 : R) 0) = (Algebra.ofId ℚ R).comp FreeAlgebra.algebraMapInv := by
    apply FreeAlgebra.hom_ext
    funext i
    fin_cases i <;> simp [eval, FreeAlgebra.algebraMapInv]
  rw [this]; rfl

variable (K) in
/-- A unit of `U4 N` as a unit of `K ⊗ U4 N`. -/
noncomputable def uK (G : (U4 N)ˣ) : (K ⊗[ℚ] U4 N)ˣ :=
  Units.map (ιK K N).toRingHom.toMonoidHom G

@[simp] theorem val_uK (G : (U4 N)ˣ) :
    ((uK K G : (K ⊗[ℚ] U4 N)ˣ) : K ⊗[ℚ] U4 N) = ιK K N G :=
  rfl

@[simp] theorem val_uK_inv (G : (U4 N)ˣ) :
    ((↑(uK K G)⁻¹ : K ⊗[ℚ] U4 N)) = ιK K N (↑G⁻¹ : U4 N) :=
  rfl

/-- At a rational pair, `compK Φ g` is the action `actEvalF` with the unit `g(x, y)`. -/
theorem evK_compK_ιK (Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) (g : FreeAlgebra ℚ (Fin 2))
    {x y : U4 N} (G : (U4 N)ˣ) (hG : (G : U4 N) = eval x y g)
    (hi : eval x y g * eval y x g = 1) :
    evK (ιK K N x) (ιK K N y) (compK Φ g) =
      actEvalF (fun a b => evK a b Φ) (ιK K N x) (ιK K N y) (uK K G) := by
  have e : (↑G⁻¹ : U4 N) = eval y x g := by
    rw [← mul_one (↑G⁻¹ : U4 N), ← hi, ← hG, ← mul_assoc, Units.inv_mul, one_mul]
  rw [evK_compK, actEvalF, val_uK, val_uK_inv, e, hG, map_eval, map_eval]

/-- The transported family commutes with `ι : U4 N → K ⊗ U4 N`. -/
theorem transported_ιK (a b c d e : U4 N) (Ga Gb Gc : (U4 N)ˣ) :
    transported (ιK K N a) (ιK K N b) (ιK K N c) (ιK K N d) (ιK K N e) (uK K Ga) (uK K Gb)
        (uK K Gc) =
      (ιK K N (transported a b c d e Ga Gb Gc).1, ιK K N (transported a b c d e Ga Gb Gc).2.1,
        ιK K N (transported a b c d e Ga Gb Gc).2.2.1,
        ιK K N (transported a b c d e Ga Gb Gc).2.2.2.1,
        ιK K N (transported a b c d e Ga Gb Gc).2.2.2.2) := by
  simp only [transported, mul_inv_rev, Units.val_mul, val_uK, val_uK_inv, map_mul, map_add,
    map_sub]

/-- **(5.12) of `compK Φ g`.** -/
theorem inv_compK {Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)}
    (hinv : ∀ a b : U4 N, a ∈ Fil N 1 → b ∈ Fil N 1 →
      evK (ιK K N a) (ιK K N b) Φ * evK (ιK K N b) (ιK K N a) Φ = 1)
    {g : FreeAlgebra ℚ (Fin 2)} (hg : GRT1U4 N g) {a b : U4 N} (ha : a ∈ Fil N 1)
    (hb : b ∈ Fil N 1) :
    evK (ιK K N a) (ιK K N b) (compK Φ g) * evK (ιK K N b) (ιK K N a) (compK Φ g) = 1 := by
  have hGG : eval a b g * eval b a g = 1 := hg.inv512 a b ha hb
  have hGG' : eval b a g * eval a b g = 1 := hg.inv512 b a hb ha
  let u : (U4 N)ˣ := ⟨eval b a g, eval a b g, hGG', hGG⟩
  have hX : eval a b g * a * eval b a g ∈ Fil N 1 := conj_mem_Fil_one u ha
  have e1 : evK (ιK K N a) (ιK K N b) (compK Φ g) =
      evK (ιK K N (eval a b g * a * eval b a g)) (ιK K N b) Φ * ιK K N (eval a b g) := by
    rw [evK_compK]; simp only [map_mul, map_eval]
  have e2 : evK (ιK K N b) (ιK K N a) (compK Φ g) =
      evK (ιK K N (eval b a g * b * eval a b g)) (ιK K N a) Φ * ιK K N (eval b a g) := by
    rw [evK_compK]; simp only [map_mul, map_eval]
  have key : ιK K N (eval a b g) * evK (ιK K N (eval b a g * b * eval a b g)) (ιK K N a) Φ *
      ιK K N (eval b a g) = evK (ιK K N b) (ιK K N (eval a b g * a * eval b a g)) Φ := by
    have h := evK_conj (uK K u) (ιK K N (eval b a g * b * eval a b g)) (ιK K N a) Φ
    simp only [val_uK, val_uK_inv] at h
    change evK (ιK K N (eval a b g) * ιK K N (eval b a g * b * eval a b g) *
        ιK K N (eval b a g)) (ιK K N (eval a b g) * ιK K N a * ιK K N (eval b a g)) Φ =
      ιK K N (eval a b g) * evK (ιK K N (eval b a g * b * eval a b g)) (ιK K N a) Φ *
        ιK K N (eval b a g) at h
    rw [← h, ← map_mul, ← map_mul, ← map_mul, ← map_mul]
    congr 2
    congr 1
    calc eval a b g * (eval b a g * b * eval a b g) * eval b a g
        = (eval a b g * eval b a g) * b * (eval a b g * eval b a g) := by noncomm_ring
      _ = b := by rw [hGG]; simp
  calc evK (ιK K N a) (ιK K N b) (compK Φ g) * evK (ιK K N b) (ιK K N a) (compK Φ g)
      = evK (ιK K N (eval a b g * a * eval b a g)) (ιK K N b) Φ *
          (ιK K N (eval a b g) * evK (ιK K N (eval b a g * b * eval a b g)) (ιK K N a) Φ *
            ιK K N (eval b a g)) := by rw [e1, e2]; simp only [mul_assoc]
    _ = 1 := by rw [key]; exact hinv _ _ hX hb

/-- **The constant term of `compK Φ g`.** -/
theorem const_compK {Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)} (hc : evK (0 : K) 0 Φ = 1)
    {g : FreeAlgebra ℚ (Fin 2)} (hg : GRT1U4 N g) : evK (0 : K) 0 (compK Φ g) = 1 := by
  rw [evK_compK, mul_zero, zero_mul, hc, one_mul, eval_zero_zero, hg.const, map_one]

/-- `g(x, y)` at sums of generators, mapped to `K ⊗ U4 N`. -/
theorem ιK_eval_genSum (g : FreeAlgebra ℚ (Fin 2)) (l m : List (Fin 6)) :
    ιK K N (eval (genSum N l) (genSum N m) g) =
      eval (ιK K N (genSum N l)) (ιK K N (genSum N m)) g := map_eval _ _ _ _

/-- **The pentagon of `compK Φ g`** at the universal family of `K ⊗ U4 N`. -/
theorem pentagon_compK {Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)}
    (hpent : PentagonF (fun a b => evK a b Φ) (ιK K N (t N 0)) (ιK K N (t N 1))
      (ιK K N (t N 3)) (ιK K N (t N 4)) (ιK K N (t N 5)))
    {g : FreeAlgebra ℚ (Fin 2)} (hg : GRT1U4 N g) :
    PentagonF (fun a b => evK a b (compK Φ g)) (ιK K N (t N 0)) (ιK K N (t N 1))
      (ιK K N (t N 3)) (ιK K N (t N 4)) (ιK K N (t N 5)) := by
  have hg1 := hg.const
  have h512 := hg.inv512
  have h514 := hg.tc514
  have m := fun i => t_mem_Fil_one (N := N) i
  have hA : TCompat (t N 1) (t N 3) (gU N hg1 [0] [3]) (gU N hg1 [1] [3]) :=
    (tcompat_iff_poly g _ _ (by simp [genSum]) (by simp [genSum]) (h512 _ _ (m 0) (m 3))
      (h512 _ _ (m 1) (m 3))).2 (h514 _ _ _ (m 0) (m 1) (m 3) (dk4 N).d4)
  have hB : TCompat (t N 4) (t N 3) (gU N hg1 [5] [3]) (gU N hg1 [4] [3]) :=
    (tcompat_iff_poly g _ _ (by simp [genSum]) (by simp [genSum]) (h512 _ _ (m 5) (m 3))
      (h512 _ _ (m 4) (m 3))).2 (h514 _ _ _ (m 5) (m 4) (m 3) (dk4 N).d0.rev)
  have ha : (gU N hg1 [0] [3] : U4 N) = eval (t N 0) (t N 3) g := by simp [genSum]
  have hb : (gU N hg1 [1, 3] [5] : U4 N) = eval (t N 1 + t N 3) (t N 5) g := by simp [genSum]
  have hc : (gU N hg1 [0] [3, 4] : U4 N) = eval (t N 0) (t N 3 + t N 4) g := by simp [genSum]
  have hd : (gU N hg1 [0, 1] [4, 5] : U4 N) = eval (t N 0 + t N 1) (t N 4 + t N 5) g := by
    simp [genSum]
  have he : (gU N hg1 [3] [5] : U4 N) = eval (t N 3) (t N 5) g := by simp [genSum]
  have hfar := far_of_tcompat g (dk4 N) (gU N hg1 [0] [3]) (gU N hg1 [1, 3] [5])
    (gU N hg1 [0] [3, 4]) (gU N hg1 [0, 1] [4, 5]) (gU N hg1 [3] [5]) (gU N hg1 [1] [3])
    (gU N hg1 [3] [4]) (gU N hg1 [1] [3, 5]) (gU N hg1 [0, 3] [4]) (gU N hg1 [5] [3])
    (gU N hg1 [4] [3]) ha hb hc hd he (by simp [genSum]) (by simp [genSum]) (by simp [genSum])
    (by simp [genSum]) (by simp [genSum]) (by simp [genSum]) hg.pent515
    (pentagon_swap23 g hg.pent515) (h512 _ _ (m 5) (m 3)) (h512 _ _ (m 4) (m 3)) hA hB
  have hs := transported_dk4 g (dk4 N) _ _ _ _ _ ha hb hc hd he hg.pent515 hfar
  set s := transported (t N 0) (t N 1) (t N 3) (t N 4) (t N 5) (gU N hg1 [0] [3])
    (gU N hg1 [1, 3] [5]) (gU N hg1 [0] [3, 4]) with hsdef
  set sf : Fin 6 → U4 N := ![s.1, s.2.1, transported14 (t N 2) (t N 4) (t N 5) s, s.2.2.1,
    s.2.2.2.1, s.2.2.2.2] with hsf
  have hdk : DK4 (sf 0) (sf 1) (sf 2) (sf 3) (sf 4) (sf 5) := hs
  have hmem : ∀ i, sf i ∈ Fil N 1 := by
    have T := t_mem_Fil_one (N := N)
    have c := conj_mem_Fil_one (N := N)
    intro i
    fin_cases i <;>
      simp only [hsf, s, transported, transported14, Fin.zero_eta, Fin.mk_one, Fin.reduceFinMk,
        Matrix.cons_val, Matrix.cons_val_zero, Matrix.cons_val_one] <;>
      first
      | exact T 0
      | exact sub_mem (add_mem (T 1) (T 3)) (c _ (T 3))
      | exact c _ (T 3)
      | exact c _ (T 5)
      | exact sub_mem (c _ (add_mem (T 3) (T 4))) (c _ (T 3))
      | exact sub_mem (sub_mem (add_mem (add_mem (T 2) (T 4)) (T 5))
          (sub_mem (c _ (add_mem (T 3) (T 4))) (c _ (T 3)))) (c _ (T 5))
  have hsK := pentK_of_universal hpent sf hdk hmem
  have hgK : Pentagon g (ιK K N (t N 0)) (ιK K N (t N 1)) (ιK K N (t N 3)) (ιK K N (t N 4))
      (ιK K N (t N 5)) := by
    have := congrArg (ιK K N) hg.pent515
    simpa only [Pentagon, map_mul, map_eval, map_add] using this
  have hDKK : DK4 (ιK K N (t N 0)) (ιK K N (t N 1)) (ιK K N (t N 2)) (ιK K N (t N 3))
      (ιK K N (t N 4)) (ιK K N (t N 5)) := (dk4 N).map' (ιK K N).toRingHom
  have key := pentagon_actF (fun a b => evK a b Φ) (fun u a b => evK_conj u a b Φ) g hDKK
    (uK K (gU N hg1 [0] [3])) (uK K (gU N hg1 [1, 3] [5]))
    (uK K (gU N hg1 [0] [3, 4])) (uK K (gU N hg1 [0, 1] [4, 5])) (uK K (gU N hg1 [3] [5]))
    (by simp only [val_uK, ha, map_eval]) (by simp only [val_uK, hb, map_eval, map_add])
    (by simp only [val_uK, hc, map_eval, map_add])
    (by simp only [val_uK, hd, map_eval, map_add])
    (by simp only [val_uK, he, map_eval]) hgK
    (by
      show PentagonF _ (transported _ _ _ _ _ _ _ _).1 _ _ _ _
      rw [transported_ιK]
      exact hsK)
  have r := fun l m' (x y : U4 N) (hx : genSum N l = x) (hy : genSum N m' = y) =>
    evK_compK_ιK (K := K) Φ g (x := x) (y := y) (gU N hg1 l m')
      (by simp [← hx, ← hy]) (hx ▸ hy ▸ h512 _ _ (genSum_mem l) (genSum_mem m'))
  unfold PentagonF
  simp only [← map_add]
  rw [r [0] [3, 4] _ _ (by simp [genSum]) (by simp [genSum]),
    r [1, 3] [5] _ _ (by simp [genSum]) (by simp [genSum]),
    r [3] [5] _ _ (by simp [genSum]) (by simp [genSum]),
    r [0, 1] [4, 5] _ _ (by simp [genSum]) (by simp [genSum]),
    r [0] [3] _ _ (by simp [genSum]) (by simp [genSum])]
  simpa only [map_add] using key

/-- **The hexagon of `compK Φ g`** at the universal family of `K ⊗ U4 N`. -/
theorem hexagon_compK {Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)} {E : FreeAlgebra ℚ (Fin 2)}
    (hhex : HexagonF (fun a b => evK a b Φ) E (ιK K N (t N 0)) (ιK K N (t N 1))
      (ιK K N (t N 3)))
    {g : FreeAlgebra ℚ (Fin 2)} (hg : GRT1U4 N g) :
    HexagonF (fun a b => evK a b (compK Φ g)) E (ιK K N (t N 0)) (ιK K N (t N 1))
      (ιK K N (t N 3)) := by
  have hg1 := hg.const
  have h512 := hg.inv512
  have m := fun i => t_mem_Fil_one (N := N) i
  have hcyc : eval (t N 3) (t N 1) g * eval (t N 0) (t N 3) g * eval (t N 1) (t N 0) g = 1 := by
    apply rotate_of_isUnit (isUnit_eval nilIdeal_Fil (m 1) (m 0) hg1)
    have := hg.hex513
    simp only [Hexagon, map_one, mul_one] at this
    rw [← this]
  have htc : TCompat (t N 1) (t N 0) (gU N hg1 [3] [0]) (gU N hg1 [1] [0]) :=
    (tcompat_iff_poly g _ _ (by simp [genSum]) (by simp [genSum]) (h512 _ _ (m 3) (m 0))
      (h512 _ _ (m 1) (m 0))).2 (hg.tc514 _ _ _ (m 3) (m 1) (m 0) (dk4 N).d4.rev)
  have hDK := (dk4 N).d4
  have h1 : (gU N hg1 [1] [0] : U4 N) = eval (t N 1) (t N 0) g := by simp [genSum]
  have h2 : (gU N hg1 [3] [1] : U4 N) = eval (t N 3) (t N 1) g := by simp [genSum]
  have h3 : (gU N hg1 [0] [3] : U4 N) = eval (t N 0) (t N 3) g := by simp [genSum]
  have hK : (gU N hg1 [3] [0] : U4 N) = eval (t N 3) (t N 0) g := by simp [genSum]
  have hsum := transported3_sum g hDK (gU N hg1 [1] [0]) (gU N hg1 [0] [3]) (gU N hg1 [3] [0])
    h3 hK (h512 _ _ (m 3) (m 0)) htc
  have hd3 := transported3_dk3 g hDK (gU N hg1 [1] [0]) (gU N hg1 [0] [3]) h1 h3 hsum
  have hmem13 : (gU N hg1 [1] [0] : U4 N) * t N 1 * ↑(gU N hg1 [1] [0])⁻¹ ∈ Fil N 1 := by
    simpa using conj_mem_Fil_one (gU N hg1 [1] [0])⁻¹ (m 1)
  have hX := hexK_of_universal hhex hd3 (m 0) hmem13 (conj_mem_Fil_one _ (m 3))
  have key := hexagon_act_of_transportF (fun a b => evK a b Φ) (fun u a b => evK_conj u a b Φ)
    g E (t12 := ιK K N (t N 0)) (t13 := ιK K N (t N 1)) (t23 := ιK K N (t N 3))
    (uK K (gU N hg1 [1] [0])) (uK K (gU N hg1 [3] [1])) (uK K (gU N hg1 [0] [3]))
    (by simp only [val_uK, h1, map_eval]) (by simp only [val_uK, h2, map_eval])
    (by simp only [val_uK, h3, map_eval])
    (by have := congrArg (ιK K N) hcyc; simpa only [map_mul, map_eval, map_one] using this)
    (by have := congrArg (ιK K N) hsum
        simpa only [map_mul, map_add, val_uK, val_uK_inv] using this)
    (by simpa only [map_mul, val_uK, val_uK_inv] using hX)
  have r := fun l m' (x y : U4 N) (hx : genSum N l = x) (hy : genSum N m' = y) =>
    evK_compK_ιK (K := K) Φ g (x := x) (y := y) (gU N hg1 l m')
      (by simp [← hx, ← hy]) (hx ▸ hy ▸ h512 _ _ (genSum_mem l) (genSum_mem m'))
  simp only [HexagonF]
  rw [r [1] [0] _ _ (by simp [genSum]) (by simp [genSum]),
    r [3] [1] _ _ (by simp [genSum]) (by simp [genSum]),
    r [0] [3] _ _ (by simp [genSum]) (by simp [genSum])]
  exact key

/-- **Step (1) of gap B1: `AssocK` is closed under a rational `GRT₁` element.** If `Φ` is an
associator with coefficients in `K` in `K ⊗ U4 N` and `g` satisfies the four `GRT₁` conditions
in `U4 N`, then `Φ ∘ g = Φ(g A g⁻¹, B) · g` is again such an associator. -/
theorem assocK_compK {E : FreeAlgebra ℚ (Fin 2)} {Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)}
    (hΦ : AssocK K N E Φ) {g : FreeAlgebra ℚ (Fin 2)} (hg : GRT1U4 N g) :
    AssocK K N E (compK Φ g) where
  const := const_compK hΦ.const hg
  inv := fun _ _ ha hb => inv_compK hΦ.inv hg ha hb
  hex := hexagon_compK hΦ.hex hg
  pent := pentagon_compK hΦ.pent hg

end Step1

end QOU.BraidsAndKnots.RationalAssociator
