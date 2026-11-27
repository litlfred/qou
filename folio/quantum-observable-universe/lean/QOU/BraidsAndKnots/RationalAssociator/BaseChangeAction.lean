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
conjugation identity `φ(u⁻¹ a u, u⁻¹ b u) = u⁻¹ φ(a, b) u`. They are repeated here for an arbitrary
function `f : R → R → R` with that property (`pentagon_actF`, `hexagon_act_of_transportF`). For
`f = evK · · Φ` the property is `evK_conj`.

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
      f (t12 + (t13 + t23 - (↑Ga⁻¹ : R) * t23 * Ga)) ((↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) - (↑Ga⁻¹ : R) * t23 * Ga +
          (↑Gb⁻¹ : R) * t34 * Gb) := by
    have a1 : (↑Ga⁻¹ : R) * (t12 + t13) * Ga = t12 + (t13 + t23 - (↑Ga⁻¹ : R) * t23 * Ga) := by
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
  have f3 : f ((↑G3⁻¹ : R) * t23 * G3) ((↑(G2 * G3)⁻¹ : R) * t13 * ↑(G2 * G3)⁻¹⁻¹) =
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
    evK ((↑u⁻¹ : S) * a * u) ((↑u⁻¹ : S) * b * u) Φ = (↑u⁻¹ : S) * evK a b Φ * u := by
  induction Φ using TensorProduct.induction_on with
  | zero => simp
  | tmul k p =>
    rw [evK_tmul, evK_tmul, eval_conj, ← mul_assoc, ← mul_assoc,
      Algebra.commutes k (↑u⁻¹ : S)]
    simp only [mul_assoc]
  | add x y hx hy => rw [map_add, map_add, hx, hy, mul_add, add_mul]

/-- Substitution in the second tensor factor, then evaluation, is evaluation at the
substituted values. -/
theorem evK_map_lift (a b : S) (p q : FreeAlgebra ℚ (Fin 2)) (Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) :
    evK a b (Algebra.TensorProduct.map (AlgHom.id K K) (FreeAlgebra.lift ℚ ![p, q]) Φ) =
      evK (eval a b p) (eval a b q) Φ := by
  induction Φ using TensorProduct.induction_on with
  | zero => simp
  | tmul k x => simp only [Algebra.TensorProduct.map_tmul, AlgHom.id_apply, evK_tmul, eval_lift]
  | add x y hx hy => rw [map_add, map_add, map_add, hx, hy]

/-- **The right action of a rational `g` on `Φ ∈ K ⊗ ℚ⟨X, Y⟩`**, Drinfeld's (5.16) with the
inverse written through (5.12): `Φ(g · A · g(B, A), B) · g`. -/
noncomputable def compK (Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) (g : FreeAlgebra ℚ (Fin 2)) :
    K ⊗[ℚ] FreeAlgebra ℚ (Fin 2) :=
  Algebra.TensorProduct.map (AlgHom.id K K)
      (FreeAlgebra.lift ℚ ![g * FreeAlgebra.ι ℚ 0 * swapPoly g, FreeAlgebra.ι ℚ 1]) Φ *
    (1 : K) ⊗ₜ g

theorem evK_compK (a b : S) (Φ : K ⊗[ℚ] FreeAlgebra ℚ (Fin 2)) (g : FreeAlgebra ℚ (Fin 2)) :
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


end QOU.BraidsAndKnots.RationalAssociator
