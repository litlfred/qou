import Mathlib.LinearAlgebra.Alternating.Uncurry.Fin
import Mathlib.Algebra.Lie.Basic
import Mathlib.RingTheory.Derivation.Lie

set_option autoImplicit false

/-!
# QOU.Core.LieDerivative — Lie derivatives of forms and Cartan's magic formula

Cartan's homotopy formula `L_x = d ∘ ι_x + ι_x ∘ d`, **proved**, in the generic
algebraic setting of Chevalley–Eilenberg cochains.

## Setting

* `R` is any commutative ring (no field, no `ℝ`, no topology);
* `L` is a Lie ring that is an `R`-module (the "vector fields");
* `M` is an `R`-module on which `L` acts as a Lie ring module, `⁅x, m⁆`
  (the "functions", or any coefficient module);
* an `n`-form is an `R`-multilinear alternating map `ω : L [⋀^Fin n]→ₗ[R] M`.

The three operators are given by their explicit formulas, each defined
independently of the other two:

* **Koszul / Chevalley–Eilenberg differential** (`ceD`),
  `dω(v₀,…,vₙ) = Σᵢ (-1)ⁱ ⁅vᵢ, ω(…v̂ᵢ…)⁆ + Σ_{i<j} (-1)^{i+j} ω(⁅vᵢ,vⱼ⁆, …v̂ᵢ…v̂ⱼ…)`;
* **interior product** `ι_x ω = ω.curryLeft x`, i.e. `(ι_x ω)(v) = ω(x, v)`;
* **Lie derivative** (`lieDeriv`), the derivation extension of the action,
  `(L_x ω)(v₁,…,vₙ) = ⁅x, ω(v)⁆ - Σᵢ ω(v₁,…,⁅x,vᵢ⁆,…,vₙ)`.

`cartan_formula` proves `d(ι_x ω) + ι_x(dω) = L_x ω` pointwise, for every
degree `n + 1`. The proof is a finite signed-sum cancellation using only
alternation of `ω`; it uses no choice, no limits and no `2⁻¹`.

## Relation to forms on a manifold

For a smooth manifold `X`, take `M = C^∞(X)` and `L = 𝔛(X)` acting by
`⁅ξ, f⁆ = ξ f`. Differential `n`-forms are the `C^∞(X)`-multilinear alternating
maps on `𝔛(X)`, and on them `ceD` is the exterior derivative (Koszul's
formula), `curryLeft` the interior product and `lieDeriv` the Lie derivative
(the derivation formula for `L_ξ` on tensors). The algebraic shadow of that
instance is recorded here: for a commutative `R`-algebra `A`, the Lie ring
`Derivation R A A` acts on `A` (`derivationLieRingModule`), so
`cartan_formula_derivation` is Cartan's formula for algebraic forms on
`Spec A`. **Not formalised here:** the identification of Mathlib's analytic
objects (`extDeriv` on normed spaces, `VectorField.mlieBracket` on manifolds)
with this model; Mathlib has no interior product or Lie derivative of forms to
compare against.

This discharges the explicit `cartan` hypothesis of
`QOU.AlgebraicSubstrate.d_iota_eq_zero_of_closed_of_invariant`
(`QOU/BringsSurface/CartanContraction.lean`) in the Chevalley–Eilenberg model:
see `ceD_curryLeft_eq_zero_of_closed_of_invariant`.

## References

* H. Cartan, S. Eilenberg, *Homological Algebra* (1956), Ch. XIII (Lie algebra
  cohomology; the operators `θ_x`, `i_x`, `d` and `θ_x = d i_x + i_x d`).
* J.-L. Koszul, *Homologie et cohomologie des algèbres de Lie*, Bull. SMF 78 (1950).
-/

namespace QOU.LieDerivative

open Fin

variable {R : Type*} [CommRing R] {L : Type*} [LieRing L] [Module R L]
  {M : Type*} [AddCommGroup M] [Module R M]

/-- Removing entry `i + 1` of `x :: v` is `x :: (v with entry i removed)`. -/
lemma removeNth_succ_cons {α : Type*} {n : ℕ} (x : α) (v : Fin (n + 1) → α) (i : Fin (n + 1)) :
    (i.succ).removeNth (Fin.cons x v : Fin (n + 2) → α) = Fin.cons x (i.removeNth v) := by
  funext j
  refine Fin.cases ?_ (fun j => ?_) j
  · simp [Fin.removeNth]
  · simp [Fin.removeNth, Fin.succ_succAbove_succ]

/-- Antisymmetry of an alternating map in its first two slots. -/
lemma map_cons_cons_swap {n : ℕ} (ω : L [⋀^Fin (n + 2)]→ₗ[R] M) (a b : L) (r : Fin n → L) :
    ω (Fin.cons a (Fin.cons b r)) = - ω (Fin.cons b (Fin.cons a r)) := by
  have h := ω.map_swap (Fin.cons b (Fin.cons a r)) (i := 0) (j := 1) (by simp)
  rw [← h]
  congr 1
  funext k
  refine Fin.cases ?_ (fun k => Fin.cases ?_ (fun k => ?_) k) k <;> rfl

/-- Replacing slot `i` by `a` equals `(-1)^i` times putting `a` in front. -/
lemma map_update_eq {n : ℕ} (ω : L [⋀^Fin (n + 1)]→ₗ[R] M) (v : Fin (n + 1) → L) (i : Fin (n + 1))
    (a : L) :
    ω (Function.update v i a) = (-1 : ℤ) ^ (i : ℕ) • ω (Fin.cons a (i.removeNth v)) := by
  rw [← Fin.insertNth_removeNth, AlternatingMap.map_insertNth]
  rfl

variable [LieRingModule L M]

/-- The action part of the Koszul differential, `Σᵢ (-1)ⁱ ⁅vᵢ, ω(…v̂ᵢ…)⁆`. -/
def firstSum {n : ℕ} (ω : L [⋀^Fin n]→ₗ[R] M) (v : Fin (n + 1) → L) : M :=
  ∑ i : Fin (n + 1), (-1 : ℤ) ^ (i : ℕ) • ⁅v i, ω (i.removeNth v)⁆

/-- The bracket part of the Koszul differential,
`Σ_{i<j} (-1)^{i+j} ω(⁅vᵢ,vⱼ⁆, …v̂ᵢ…v̂ⱼ…)`. A pair `i < j` of `Fin (m + 2)` is
encoded as `i` together with the index `j'` of `vⱼ` in `i.removeNth v`, so
`j = j' + 1` and `i ≤ j'`; the sign `(-1)^{i+j}` is `(-1)^{i+j'+1}`. -/
def bracketSum {m : ℕ} (ω : L [⋀^Fin (m + 1)]→ₗ[R] M) (v : Fin (m + 2) → L) : M :=
  ∑ i : Fin (m + 2), ∑ j : Fin (m + 1),
    if i ≤ j.castSucc then
      (-1 : ℤ) ^ ((i : ℕ) + (j : ℕ) + 1) •
        ω (Fin.cons ⁅v i, v j.succ⁆ (j.removeNth (i.removeNth v)))
    else 0

/-- The Chevalley–Eilenberg (Koszul) differential of an `n`-form, as a function of
`n + 1` arguments. In degree `0` there is no bracket part. -/
def ceD : {n : ℕ} → (L [⋀^Fin n]→ₗ[R] M) → (Fin (n + 1) → L) → M
  | 0, ω, v => firstSum ω v
  | _ + 1, ω, v => firstSum ω v + bracketSum ω v

/-- The Lie derivative `L_x ω`, the derivation extension of the action of `x`:
`(L_x ω)(v) = ⁅x, ω v⁆ - Σᵢ ω(v₁,…,⁅x,vᵢ⁆,…,vₙ)`. -/
def lieDeriv {n : ℕ} (x : L) (ω : L [⋀^Fin n]→ₗ[R] M) (v : Fin n → L) : M :=
  ⁅x, ω v⁆ - ∑ i, ω (Function.update v i ⁅x, v i⁆)


lemma firstSum_cons {n : ℕ} (ω : L [⋀^Fin (n + 1)]→ₗ[R] M) (x : L) (y : Fin (n + 1) → L) :
    firstSum ω (Fin.cons x y) =
      ⁅x, ω y⁆ - ∑ i : Fin (n + 1), (-1 : ℤ) ^ (i : ℕ) • ⁅y i, ω (Fin.cons x (i.removeNth y))⁆ := by
  rw [firstSum, Fin.sum_univ_succ]
  simp [removeNth_succ_cons, pow_succ, sub_eq_add_neg, Fin.removeNth_zero]

lemma firstSum_curryLeft {n : ℕ} (ω : L [⋀^Fin (n + 1)]→ₗ[R] M) (x : L) (y : Fin (n + 1) → L) :
    firstSum (ω.curryLeft x) y =
      ∑ i : Fin (n + 1), (-1 : ℤ) ^ (i : ℕ) • ⁅y i, ω (Fin.cons x (i.removeNth y))⁆ := by
  simp [firstSum, AlternatingMap.curryLeft_apply_apply, Matrix.vecCons]

omit [LieRingModule L M] in
lemma bracketSum_curryLeft {m : ℕ} (ω : L [⋀^Fin (m + 2)]→ₗ[R] M) (x : L) (y : Fin (m + 2) → L) :
    bracketSum (ω.curryLeft x) y =
      ∑ i : Fin (m + 2), ∑ j : Fin (m + 1),
        if i ≤ j.castSucc then
          (-1 : ℤ) ^ ((i : ℕ) + (j : ℕ) + 1) •
            ω (Fin.cons x (Fin.cons ⁅y i, y j.succ⁆ (j.removeNth (i.removeNth y))))
        else 0 := by
  simp [bracketSum, AlternatingMap.curryLeft_apply_apply, Matrix.vecCons]

omit [LieRingModule L M] in
lemma bracketSum_cons {m : ℕ} (ω : L [⋀^Fin (m + 2)]→ₗ[R] M) (x : L) (y : Fin (m + 2) → L) :
    bracketSum ω (Fin.cons x y) =
      ∑ j : Fin (m + 2), (-1 : ℤ) ^ ((j : ℕ) + 1) • ω (Fin.cons ⁅x, y j⁆ (j.removeNth y)) +
      ∑ i : Fin (m + 2), ∑ j : Fin (m + 1),
        if i ≤ j.castSucc then
          (-1 : ℤ) ^ ((i : ℕ) + (j : ℕ) + 1) •
            ω (Fin.cons ⁅y i, y j.succ⁆ (Fin.cons x (j.removeNth (i.removeNth y))))
        else 0 := by
  rw [bracketSum, Fin.sum_univ_succ]
  congr 1
  · refine Finset.sum_congr rfl fun j _ => ?_
    simp [Fin.removeNth_zero]
  · refine Finset.sum_congr rfl fun i _ => ?_
    rw [Fin.sum_univ_succ]
    simp only [Fin.castSucc_zero, Fin.castSucc_succ, Fin.succ_le_succ_iff, removeNth_succ_cons,
      Fin.cons_succ, Fin.val_succ, Fin.removeNth_zero]
    rw [if_neg (by simp [Fin.le_zero_iff, Fin.succ_ne_zero]), zero_add]
    refine Finset.sum_congr rfl fun j _ => ?_
    split_ifs
    · rw [show (i : ℕ) + 1 + ((j : ℕ) + 1) + 1 = (i : ℕ) + j + 1 + 2 by ring, pow_add]
      simp
    · rfl

/-- **Cartan's magic formula** `L_x = d ∘ ι_x + ι_x ∘ d`, for forms of every degree
`n + 1`: `d(ι_x ω)(y) + (dω)(x, y) = (L_x ω)(y)`. -/
theorem cartan_formula {n : ℕ} (x : L) (ω : L [⋀^Fin (n + 1)]→ₗ[R] M) (y : Fin (n + 1) → L) :
    ceD (ω.curryLeft x) y + ceD ω (Fin.cons x y) = lieDeriv x ω y := by
  have hupd : ∑ i : Fin (n + 1), ω (Function.update y i ⁅x, y i⁆) =
      ∑ j : Fin (n + 1), (-1 : ℤ) ^ (j : ℕ) • ω (Fin.cons ⁅x, y j⁆ (j.removeNth y)) :=
    Finset.sum_congr rfl fun j _ => map_update_eq ω y j _
  cases n with
  | zero =>
    simp only [ceD]
    rw [firstSum_curryLeft, firstSum_cons, lieDeriv, hupd]
    simp [bracketSum, Fin.removeNth_zero]
    abel
  | succ m =>
    simp only [ceD]
    rw [firstSum_curryLeft, firstSum_cons, bracketSum_curryLeft, bracketSum_cons, lieDeriv, hupd]
    have hP : ∑ j : Fin (m + 2), (-1 : ℤ) ^ ((j : ℕ) + 1) • ω (Fin.cons ⁅x, y j⁆ (j.removeNth y)) =
        -∑ j : Fin (m + 2), (-1 : ℤ) ^ (j : ℕ) • ω (Fin.cons ⁅x, y j⁆ (j.removeNth y)) := by
      rw [← Finset.sum_neg_distrib]
      refine Finset.sum_congr rfl fun j _ => ?_
      rw [pow_succ, mul_neg_one, neg_smul]
    have hB : (∑ i : Fin (m + 2), ∑ j : Fin (m + 1),
        if i ≤ j.castSucc then
          (-1 : ℤ) ^ ((i : ℕ) + (j : ℕ) + 1) •
            ω (Fin.cons ⁅y i, y j.succ⁆ (Fin.cons x (j.removeNth (i.removeNth y))))
        else 0) = -∑ i : Fin (m + 2), ∑ j : Fin (m + 1),
        if i ≤ j.castSucc then
          (-1 : ℤ) ^ ((i : ℕ) + (j : ℕ) + 1) •
            ω (Fin.cons x (Fin.cons ⁅y i, y j.succ⁆ (j.removeNth (i.removeNth y))))
        else 0 := by
      rw [← Finset.sum_neg_distrib]
      refine Finset.sum_congr rfl fun i _ => ?_
      rw [← Finset.sum_neg_distrib]
      refine Finset.sum_congr rfl fun j _ => ?_
      split_ifs
      · rw [map_cons_cons_swap ω, smul_neg]
      · simp
    rw [hP, hB]
    abel

/-- Degree-`0` Cartan: on a `0`-form (an element `m : M`, as a constant map), `L_x m = ⁅x, m⁆`
and the formula reads `ι_x (dm) = L_x m`. -/
theorem cartan_formula_zero (x : L) (ω : L [⋀^Fin 0]→ₗ[R] M) :
    ceD ω ![x] = lieDeriv x ω ![] := by
  simp only [ceD, firstSum, lieDeriv, Finset.univ_eq_empty, Finset.sum_empty, sub_zero]
  rw [Fin.sum_univ_one, Fin.val_zero, pow_zero, one_smul, Matrix.cons_val_zero,
    Subsingleton.elim ((0 : Fin 1).removeNth ![x]) ![]]

/-- On a closed form, the Lie derivative is exact with primitive the contraction:
`dω = 0 ⇒ L_x ω = d(ι_x ω)`. -/
theorem lieDeriv_eq_ceD_curryLeft_of_closed {n : ℕ} (x : L) (ω : L [⋀^Fin (n + 1)]→ₗ[R] M)
    (hclosed : ∀ v, ceD ω v = 0) (y : Fin (n + 1) → L) :
    lieDeriv x ω y = ceD (ω.curryLeft x) y := by
  rw [← cartan_formula, hclosed, add_zero]

/-- **Cartan contraction, unconditional in the Chevalley–Eilenberg model.** A closed,
`x`-invariant form contracts to a closed form: `dω = 0`, `L_x ω = 0 ⇒ d(ι_x ω) = 0`.
This is `QOU.AlgebraicSubstrate.d_iota_eq_zero_of_closed_of_invariant` with its `cartan`
hypothesis proved rather than assumed. -/
theorem ceD_curryLeft_eq_zero_of_closed_of_invariant {n : ℕ} (x : L)
    (ω : L [⋀^Fin (n + 1)]→ₗ[R] M) (hclosed : ∀ v, ceD ω v = 0)
    (hinv : ∀ v, lieDeriv x ω v = 0) (y : Fin (n + 1) → L) :
    ceD (ω.curryLeft x) y = 0 := by
  rw [← lieDeriv_eq_ceD_curryLeft_of_closed x ω hclosed, hinv]

end QOU.LieDerivative

/-! ### Algebraic vector fields: derivations of a commutative algebra -/

namespace QOU.LieDerivative

variable {R : Type*} [CommRing R] {A : Type*} [CommRing A] [Algebra R A]

/-- Derivations act on the algebra by evaluation, `⁅D, a⁆ = D a`. This is the algebraic
form of "vector fields act on functions". Kept as a `def` (not a global instance) so it
cannot clash with other actions on `A`. -/
@[reducible] def derivationLieRingModule : LieRingModule (Derivation R A A) A where
  bracket D a := D a
  add_lie D E a := by simp
  lie_add D a b := by simp
  leibniz_lie D E a := by
    change D (E a) = ⁅D, E⁆ a + E (D a)
    rw [Derivation.commutator_apply]; abel

attribute [local instance] derivationLieRingModule

/-- Cartan's formula for algebraic differential forms: alternating `R`-multilinear maps
on the derivations `Der_R(A)` with values in `A`. -/
theorem cartan_formula_derivation {n : ℕ} (X : Derivation R A A)
    (ω : Derivation R A A [⋀^Fin (n + 1)]→ₗ[R] A) (Y : Fin (n + 1) → Derivation R A A) :
    ceD (ω.curryLeft X) Y + ceD ω (Fin.cons X Y) = lieDeriv X ω Y :=
  cartan_formula X ω Y

end QOU.LieDerivative
