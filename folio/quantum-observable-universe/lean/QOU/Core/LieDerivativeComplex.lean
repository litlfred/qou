import QOU.Core.LieDerivative

set_option autoImplicit false

/-!
# QOU.Core.LieDerivativeComplex — `d` as an operator on forms

Continues `QOU/Core/LieDerivative.lean` (Chevalley–Eilenberg model: a Lie algebra `L`
over a commutative ring `R` acting on an `R`-module `M`; `n`-forms are alternating
`R`-multilinear maps `L^n → M`). There `ceD ω` was a function of `n + 1` arguments.
Here it is shown to be an alternating `(n + 1)`-form, `ceDAlt ω`.

* The action part of `d` is Mathlib's `alternatizeUncurryFin` of `x ↦ ⁅x, ω(·)⁆`, so it is
  alternating for free.
* The bracket part `B ω` satisfies the recursion `B ω (x :: y) = -θ_x ω (y) - B (ι_x ω) (y)`
  (`bracketPart_cons`), where `θ_x ω (v) = Σᵢ ω(…, ⁅x, vᵢ⁆, …)`. Multilinearity and
  alternation are proved by induction on the degree through this recursion
  (`bracketPart_isAltMulti`); the only non-recursive input is `B ω (x :: x :: z) = 0`, which
  is `⁅x, x⁆ = 0` plus `ι_x ι_x = 0`.

Then the rest of the Cartan calculus, each identity proved by induction on degree from
Cartan's formula and contraction (`ext_curryLeft`), with no index juggling:

* `curryLeft_ceDAlt` — `ι_y d = L_y - d ι_y` on forms (Cartan's formula);
* `curryLeft_lieDerivAlt` — `ι_y L_x = L_x ι_y - ι_{⁅x,y⁆}`;
* `lieDerivAlt_comm` — `[L_x, L_y] = L_{⁅x,y⁆}` (Jacobi + module Leibniz in the base case);
* `lieDerivAlt_ceDAlt` — `[L_x, d] = 0`;
* `ceDAlt_ceDAlt` — **`d ∘ d = 0`**: alternating forms with `ceDAlt` are a cochain complex.

No division by `2` is used, so `R` is arbitrary (characteristic `2` included).
-/

namespace QOU.LieDerivative

open Fin

variable {R : Type*} [CommRing R] {L : Type*} [LieRing L] [LieAlgebra R L]
  {M : Type*} [AddCommGroup M] [Module R M]

/-- The coadjoint part of the Lie derivative: `θ_x ω (v) = Σᵢ ω(v₁,…,⁅x,vᵢ⁆,…,vₙ)`. -/
def theta {n : ℕ} (x : L) (ω : L [⋀^Fin n]→ₗ[R] M) (v : Fin n → L) : M :=
  ∑ i : Fin n, ω (Function.update v i ⁅x, v i⁆)

/-- The bracket part of `d`, extended by `0` in degree `0`. -/
def bracketPart : {n : ℕ} → (L [⋀^Fin n]→ₗ[R] M) → (Fin (n + 1) → L) → M
  | 0, _, _ => 0
  | _ + 1, ω, v => bracketSum ω v

lemma theta_cons {n : ℕ} (x a : L) (ω : L [⋀^Fin (n + 1)]→ₗ[R] M) (z : Fin n → L) :
    theta x ω (Fin.cons a z) = ω (Fin.cons ⁅x, a⁆ z) + theta x (ω.curryLeft a) z := by
  simp only [theta, Fin.sum_univ_succ, Fin.cons_zero, Fin.cons_succ, Fin.update_cons_zero,
    ← Fin.cons_update, AlternatingMap.curryLeft_apply_apply]
  rfl

/-- **Recursion for the bracket part.** `B ω (x :: y) = -θ_x ω (y) - B (ι_x ω) (y)`. -/
lemma bracketPart_cons {n : ℕ} (ω : L [⋀^Fin (n + 1)]→ₗ[R] M) (x : L) (y : Fin (n + 1) → L) :
    bracketPart ω (Fin.cons x y) = -theta x ω y - bracketPart (ω.curryLeft x) y := by
  cases n with
  | zero =>
    simp [bracketPart, bracketSum, theta, Fin.removeNth_zero]
    congr 1
    funext i
    fin_cases i
    rfl
  | succ m =>
    simp only [bracketPart]
    rw [bracketSum_cons, bracketSum_curryLeft, theta]
    have hP : ∑ j : Fin (m + 2), (-1 : ℤ) ^ ((j : ℕ) + 1) • ω (Fin.cons ⁅x, y j⁆ (j.removeNth y)) =
        -∑ j : Fin (m + 2), ω (Function.update y j ⁅x, y j⁆) := by
      rw [← Finset.sum_neg_distrib]
      refine Finset.sum_congr rfl fun j _ => ?_
      rw [map_update_eq, pow_succ, mul_neg_one, neg_smul]
    rw [hP, sub_eq_add_neg]
    congr 1
    rw [← Finset.sum_neg_distrib]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [← Finset.sum_neg_distrib]
    refine Finset.sum_congr rfl fun j _ => ?_
    split_ifs
    · rw [map_cons_cons_swap ω, smul_neg]
    · simp


/-- Swapping two equal slots turns "replace slot `a`" into "replace slot `b`". -/
lemma update_comp_swap {α : Type*} {n : ℕ} (v : Fin n → α) {a b : Fin n} (hab : a ≠ b)
    (hv : v a = v b) (c : α) :
    Function.update v a c ∘ Equiv.swap a b = Function.update v b c := by
  funext k
  rw [Function.comp_apply]
  rcases eq_or_ne k a with rfl | hka
  · rw [Equiv.swap_apply_left, Function.update_of_ne hab.symm, Function.update_of_ne hab, hv]
  rcases eq_or_ne k b with rfl | hkb
  · rw [Equiv.swap_apply_right, Function.update_self, Function.update_self]
  · rw [Equiv.swap_apply_of_ne_of_ne hka hkb, Function.update_of_ne hka,
      Function.update_of_ne hkb]

/-- `θ_x ω` vanishes on a tuple with two equal entries. -/
lemma theta_eq_zero_of_eq {n : ℕ} (x : L) (ω : L [⋀^Fin n]→ₗ[R] M) {v : Fin n → L}
    {a b : Fin n} (hv : v a = v b) (hab : a ≠ b) : theta x ω v = 0 := by
  classical
  unfold theta
  rw [← Finset.add_sum_erase _ _ (Finset.mem_univ a),
    ← Finset.add_sum_erase _ _ (Finset.mem_erase.2 ⟨hab.symm, Finset.mem_univ b⟩)]
  have hrest : ∑ i ∈ (Finset.univ.erase a).erase b, ω (Function.update v i ⁅x, v i⁆) = 0 := by
    refine Finset.sum_eq_zero fun i hi => ?_
    obtain ⟨hib, hia⟩ : i ≠ b ∧ i ≠ a := by simpa using hi
    exact ω.map_eq_zero_of_eq _ (i := a) (j := b)
      (by simp [Function.update_of_ne hia.symm, Function.update_of_ne hib.symm, hv]) hab
  rw [hrest, add_zero]
  have hswap := ω.map_swap (Function.update v a ⁅x, v a⁆) hab
  rw [update_comp_swap v hab hv, hv] at hswap
  rw [hv, hswap, add_neg_cancel]


lemma theta_update_add {n : ℕ} (x : L) (ω : L [⋀^Fin n]→ₗ[R] M) (v : Fin n → L) (k : Fin n)
    (a b : L) : theta x ω (Function.update v k (a + b)) =
      theta x ω (Function.update v k a) + theta x ω (Function.update v k b) := by
  unfold theta
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun i _ => ?_
  rcases eq_or_ne i k with rfl | hik
  · simp only [Function.update_self, Function.update_idem, lie_add]
    exact ω.map_update_add v i _ _
  · have e : ∀ p, Function.update (Function.update v k p) i ⁅x, Function.update v k p i⁆ =
        Function.update (Function.update v i ⁅x, v i⁆) k p := fun p => by
      rw [Function.update_of_ne hik]; exact Function.update_comm hik.symm _ _ _
    rw [e, e, e]
    exact ω.map_update_add _ k a b

lemma theta_add_left {n : ℕ} (a b : L) (ω : L [⋀^Fin n]→ₗ[R] M) (v : Fin n → L) :
    theta (a + b) ω v = theta a ω v + theta b ω v := by
  unfold theta
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [add_lie]
  exact ω.map_update_add v i _ _

lemma bracketPart_add {n : ℕ} (ω₁ ω₂ : L [⋀^Fin n]→ₗ[R] M) (v : Fin (n + 1) → L) :
    bracketPart (ω₁ + ω₂) v = bracketPart ω₁ v + bracketPart ω₂ v := by
  cases n with
  | zero => simp [bracketPart]
  | succ m =>
    simp only [bracketPart, bracketSum, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
    split_ifs <;> simp [smul_add]

lemma bracketPart_smul {n : ℕ} (c : R) (ω : L [⋀^Fin n]→ₗ[R] M) (v : Fin (n + 1) → L) :
    bracketPart (c • ω) v = c • bracketPart ω v := by
  cases n with
  | zero => simp [bracketPart]
  | succ m =>
    simp only [bracketPart, bracketSum, Finset.smul_sum]
    refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
    split_ifs <;> simp [smul_comm c]

lemma bracketPart_zero {n : ℕ} (v : Fin (n + 1) → L) :
    bracketPart (0 : L [⋀^Fin n]→ₗ[R] M) v = 0 := by
  cases n <;> simp [bracketPart, bracketSum]


lemma theta_update_smul {n : ℕ} (x : L) (ω : L [⋀^Fin n]→ₗ[R] M) (v : Fin n → L) (k : Fin n)
    (c : R) (a : L) : theta x ω (Function.update v k (c • a)) =
      c • theta x ω (Function.update v k a) := by
  unfold theta
  rw [Finset.smul_sum]
  refine Finset.sum_congr rfl fun i _ => ?_
  rcases eq_or_ne i k with rfl | hik
  · simp only [Function.update_self, Function.update_idem, lie_smul]
    exact ω.map_update_smul v i _ _
  · have e : ∀ p, Function.update (Function.update v k p) i ⁅x, Function.update v k p i⁆ =
        Function.update (Function.update v i ⁅x, v i⁆) k p := fun p => by
      rw [Function.update_of_ne hik]; exact Function.update_comm hik.symm _ _ _
    rw [e, e]
    exact ω.map_update_smul _ k c a

lemma theta_smul_left {n : ℕ} (c : R) (a : L) (ω : L [⋀^Fin n]→ₗ[R] M) (v : Fin n → L) :
    theta (c • a) ω v = c • theta a ω v := by
  unfold theta
  rw [Finset.smul_sum]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [smul_lie]
  exact ω.map_update_smul v i _ _


lemma bracketPart_cons_cons_self {n : ℕ} (ω : L [⋀^Fin (n + 1)]→ₗ[R] M) (x : L)
    (z : Fin n → L) : bracketPart ω (Fin.cons x (Fin.cons x z)) = 0 := by
  rw [bracketPart_cons, theta_cons, lie_self, ω.map_coord_zero 0 (by simp)]
  cases n with
  | zero => simp [bracketPart, theta]
  | succ m =>
    rw [bracketPart_cons, AlternatingMap.curryLeft_same, bracketPart_zero]
    abel

/-- A function of `k` arguments that is `R`-multilinear and vanishes on tuples with two equal
entries. -/
def IsAltMulti {k : ℕ} (f : (Fin k → L) → M) : Prop :=
  (∀ v i a b, f (Function.update v i (a + b)) =
      f (Function.update v i a) + f (Function.update v i b)) ∧
  (∀ v i (c : R) a, f (Function.update v i (c • a)) = c • f (Function.update v i a)) ∧
  (∀ v i j, v i = v j → i ≠ j → f v = 0)

/-- Package an `IsAltMulti` function as an alternating map. -/
def IsAltMulti.toAlt {k : ℕ} {f : (Fin k → L) → M} (h : IsAltMulti (R := R) f) :
    L [⋀^Fin k]→ₗ[R] M where
  toFun := f
  map_update_add' := by
    intro _ v i a b
    convert h.1 v i a b
  map_update_smul' := by
    intro _ v i c a
    convert h.2.1 v i c a
  map_eq_zero_of_eq' := fun v i j hv hij => h.2.2 v i j hv hij

@[simp] lemma IsAltMulti.toAlt_apply {k : ℕ} {f : (Fin k → L) → M} (h : IsAltMulti (R := R) f)
    (v : Fin k → L) : h.toAlt v = f v := rfl

lemma theta_isAltMulti {n : ℕ} (x : L) (ω : L [⋀^Fin n]→ₗ[R] M) :
    IsAltMulti (R := R) (theta x ω) :=
  ⟨theta_update_add x ω, theta_update_smul x ω,
    fun _ _ _ hv hij => theta_eq_zero_of_eq x ω hv hij⟩

lemma bracketPart_eq_head_tail {n : ℕ} (ω : L [⋀^Fin (n + 1)]→ₗ[R] M) (v : Fin (n + 2) → L) :
    bracketPart ω v = -theta (v 0) ω (Fin.tail v) - bracketPart (ω.curryLeft (v 0)) (Fin.tail v) := by
  conv_lhs => rw [← Fin.cons_self_tail v]
  exact bracketPart_cons ω (v 0) (Fin.tail v)

/-- **The bracket part of `d` is alternating and multilinear**, in every degree. Induction on
the degree through the recursion `B ω (x :: y) = -θ_x ω (y) - B (ι_x ω) (y)`. -/
theorem bracketPart_isAltMulti : ∀ {n : ℕ} (ω : L [⋀^Fin n]→ₗ[R] M),
    IsAltMulti (R := R) (bracketPart ω)
  | 0, ω => ⟨fun _ _ _ _ => by simp [bracketPart], fun _ _ _ _ => by simp [bracketPart],
      fun _ _ _ _ _ => rfl⟩
  | n + 1, ω => by
    have IH : ∀ η : L [⋀^Fin n]→ₗ[R] M, IsAltMulti (R := R) (bracketPart η) :=
      fun η => bracketPart_isAltMulti η
    -- the function of the tail, for a fixed head
    have hG : ∀ x : L, IsAltMulti (R := R)
        (fun y => -theta x ω y - bracketPart (ω.curryLeft x) y) := by
      intro x
      obtain ⟨t1, t2, t3⟩ := theta_isAltMulti (R := R) x ω
      obtain ⟨b1, b2, b3⟩ := IH (ω.curryLeft x)
      refine ⟨fun v i a b => ?_, fun v i c a => ?_, fun v i j hv hij => ?_⟩
      · simp only [t1, b1]; abel
      · simp only [t2, b2, smul_sub, smul_neg]
      · simp [t3 v i j hv hij, b3 v i j hv hij]
    refine ⟨fun v i a b => ?_, fun v i c a => ?_, fun v i j hv hij => ?_⟩
    · simp only [bracketPart_eq_head_tail]
      refine Fin.cases ?_ (fun k => ?_) i
      · simp only [Function.update_self, Fin.tail_update_zero, theta_add_left, map_add,
          bracketPart_add]
        abel
      · simp only [Function.update_of_ne (Fin.succ_ne_zero k).symm, Fin.tail_update_succ]
        exact (hG (v 0)).1 _ _ _ _
    · simp only [bracketPart_eq_head_tail]
      refine Fin.cases ?_ (fun k => ?_) i
      · simp only [Function.update_self, Fin.tail_update_zero, theta_smul_left, map_smul,
          bracketPart_smul, smul_sub, smul_neg]
      · simp only [Function.update_of_ne (Fin.succ_ne_zero k).symm, Fin.tail_update_succ]
        exact (hG (v 0)).2.1 _ _ _ _
    · -- vanishing on equal entries
      have key : ∀ (j' : Fin (n + 1)) (v : Fin (n + 2) → L), v 0 = v j'.succ →
          bracketPart ω v = 0 := by
        intro j' v hv
        rw [bracketPart_eq_head_tail]
        set t := Fin.tail v
        have ht : t = j'.insertNth (v 0) (j'.removeNth t) := by
          rw [Fin.insertNth_removeNth, hv]
          exact (Function.update_eq_self _ _).symm
        change (hG (v 0)).toAlt t = 0
        rw [ht, AlternatingMap.map_insertNth, IsAltMulti.toAlt_apply]
        have := bracketPart_cons ω (v 0) (Fin.cons (v 0) (j'.removeNth t))
        rw [bracketPart_cons_cons_self] at this
        simp only [Matrix.vecCons]
        rw [← this, smul_zero]
      rcases Fin.eq_zero_or_eq_succ i with rfl | ⟨i', rfl⟩ <;>
        rcases Fin.eq_zero_or_eq_succ j with rfl | ⟨j', rfl⟩
      · exact absurd rfl hij
      · exact key j' v hv
      · exact key i' v hv.symm
      · rw [bracketPart_eq_head_tail]
        have hne : i' ≠ j' := fun h => hij (by rw [h])
        rw [(theta_isAltMulti (R := R) (v 0) ω).2.2 (Fin.tail v) i' j' hv hne,
          (IH _).2.2 (Fin.tail v) i' j' hv hne]
        simp


section Action

variable [LieRingModule L M] [LieModule R L M]

/-- `x ↦ ⁅x, ω(·)⁆`, the action part of `d` before alternation. -/
def actionMap {n : ℕ} (ω : L [⋀^Fin n]→ₗ[R] M) : L →ₗ[R] L [⋀^Fin n]→ₗ[R] M where
  toFun x := (LieModule.toEnd R L M x).compAlternatingMap ω
  map_add' a b := by ext v; simp
  map_smul' c a := by ext v; simp

/-- **`d` maps forms to forms.** The Chevalley–Eilenberg differential of an alternating
`n`-form, packaged as an alternating `(n + 1)`-form. -/
def ceDAlt {n : ℕ} (ω : L [⋀^Fin n]→ₗ[R] M) : L [⋀^Fin (n + 1)]→ₗ[R] M :=
  AlternatingMap.alternatizeUncurryFin (actionMap ω) + (bracketPart_isAltMulti ω).toAlt

@[simp] theorem ceDAlt_apply {n : ℕ} (ω : L [⋀^Fin n]→ₗ[R] M) (v : Fin (n + 1) → L) :
    ceDAlt ω v = ceD ω v := by
  cases n with
  | zero => simp [ceDAlt, ceD, firstSum, bracketPart, AlternatingMap.alternatizeUncurryFin_apply,
      actionMap]
  | succ m => simp [ceDAlt, ceD, firstSum, bracketPart, AlternatingMap.alternatizeUncurryFin_apply,
      actionMap]

end Action


section Calculus

variable [LieRingModule L M] [LieModule R L M]

/-- The Lie derivative `L_x ω` as an alternating form. -/
def lieDerivAlt {n : ℕ} (x : L) (ω : L [⋀^Fin n]→ₗ[R] M) : L [⋀^Fin n]→ₗ[R] M :=
  actionMap ω x - (theta_isAltMulti (R := R) x ω).toAlt

@[simp] theorem lieDerivAlt_apply {n : ℕ} (x : L) (ω : L [⋀^Fin n]→ₗ[R] M) (v : Fin n → L) :
    lieDerivAlt x ω v = lieDeriv x ω v := by
  simp [lieDerivAlt, actionMap, lieDeriv, theta]

omit [LieRingModule L M] [LieModule R L M] in
/-- Forms of positive degree are determined by their contractions. -/
lemma ext_curryLeft {n : ℕ} {f g : L [⋀^Fin (n + 1)]→ₗ[R] M}
    (h : ∀ y, f.curryLeft y = g.curryLeft y) : f = g := by
  ext v
  rw [← Fin.cons_self_tail v]
  have := congrArg (fun φ => φ (Fin.tail v)) (h (v 0))
  simpa [AlternatingMap.curryLeft_apply_apply, Matrix.vecCons] using this

/-- **Cartan's formula for forms**: `ι_y (dω) = L_y ω - d(ι_y ω)`. -/
theorem curryLeft_ceDAlt {n : ℕ} (ω : L [⋀^Fin (n + 1)]→ₗ[R] M) (y : L) :
    (ceDAlt ω).curryLeft y = lieDerivAlt y ω - ceDAlt (ω.curryLeft y) := by
  ext z
  simp only [AlternatingMap.curryLeft_apply_apply, AlternatingMap.sub_apply, ceDAlt_apply,
    lieDerivAlt_apply, Matrix.vecCons]
  rw [← cartan_formula y ω z]
  abel

/-- Degree `0`: `ι_y (dω) = L_y ω`. -/
theorem curryLeft_ceDAlt_zero (ω : L [⋀^Fin 0]→ₗ[R] M) (y : L) :
    (ceDAlt ω).curryLeft y = lieDerivAlt y ω := by
  ext z
  simp only [AlternatingMap.curryLeft_apply_apply, ceDAlt_apply, lieDerivAlt_apply]
  rw [Subsingleton.elim z ![]]
  exact cartan_formula_zero y ω

/-- **The second Cartan identity** `ι_y L_x = L_x ι_y - ι_{⁅x,y⁆}`. -/
theorem curryLeft_lieDerivAlt {n : ℕ} (x : L) (ω : L [⋀^Fin (n + 1)]→ₗ[R] M) (y : L) :
    (lieDerivAlt x ω).curryLeft y = lieDerivAlt x (ω.curryLeft y) - ω.curryLeft ⁅x, y⁆ := by
  ext z
  simp only [AlternatingMap.curryLeft_apply_apply, AlternatingMap.sub_apply, lieDerivAlt_apply,
    lieDeriv, Matrix.vecCons]
  rw [show (∑ i, ω (Function.update (Fin.cons y z : Fin (n + 1) → L) i
      ⁅x, (Fin.cons y z : Fin (n + 1) → L) i⁆)) = theta x ω (Fin.cons y z) from rfl, theta_cons]
  simp [theta, AlternatingMap.curryLeft_apply_apply, Matrix.vecCons]
  abel


omit [LieRingModule L M] [LieModule R L M] in
lemma curryLeft_sub {n : ℕ} (f g : L [⋀^Fin (n + 1)]→ₗ[R] M) (y : L) :
    (f - g).curryLeft y = f.curryLeft y - g.curryLeft y := by
  ext z; simp [AlternatingMap.curryLeft_apply_apply]

lemma lieDerivAlt_sub {n : ℕ} (x : L) (ω₁ ω₂ : L [⋀^Fin n]→ₗ[R] M) :
    lieDerivAlt x (ω₁ - ω₂) = lieDerivAlt x ω₁ - lieDerivAlt x ω₂ := by
  ext v
  simp only [lieDerivAlt_apply, AlternatingMap.sub_apply, lieDeriv, lie_sub,
    Finset.sum_sub_distrib]
  abel

omit [LieModule R L M] in
lemma ceD_eq {n : ℕ} (ω : L [⋀^Fin n]→ₗ[R] M) (v : Fin (n + 1) → L) :
    ceD ω v = firstSum ω v + bracketPart ω v := by
  cases n <;> simp [ceD, bracketPart]

lemma ceDAlt_sub {n : ℕ} (ω₁ ω₂ : L [⋀^Fin n]→ₗ[R] M) :
    ceDAlt (ω₁ - ω₂) = ceDAlt ω₁ - ceDAlt ω₂ := by
  ext v
  simp only [ceDAlt_apply, AlternatingMap.sub_apply, ceD_eq]
  have hB : bracketPart (ω₁ - ω₂) v = bracketPart ω₁ v - bracketPart ω₂ v := by
    rw [sub_eq_add_neg, bracketPart_add, show -ω₂ = (-1 : R) • ω₂ by simp, bracketPart_smul]
    simp [sub_eq_add_neg]
  have hF : firstSum (ω₁ - ω₂) v = firstSum ω₁ v - firstSum ω₂ v := by
    simp only [firstSum, AlternatingMap.sub_apply, lie_sub, smul_sub, Finset.sum_sub_distrib]
  rw [hB, hF]
  abel

/-- **`[L_x, L_y] = L_{⁅x,y⁆}`** on forms of every degree. -/
theorem lieDerivAlt_comm : ∀ {n : ℕ} (x y : L) (ω : L [⋀^Fin n]→ₗ[R] M),
    lieDerivAlt x (lieDerivAlt y ω) - lieDerivAlt y (lieDerivAlt x ω) = lieDerivAlt ⁅x, y⁆ ω
  | 0, x, y, ω => by
    ext v
    simp [lieDeriv, lie_lie]
  | n + 1, x, y, ω => by
    refine ext_curryLeft fun v0 => ?_
    have IH := lieDerivAlt_comm x y (ω.curryLeft v0)
    simp only [curryLeft_sub, curryLeft_lieDerivAlt, lieDerivAlt_sub]
    rw [lie_lie, map_sub, ← IH]
    abel

/-- **`[L_x, d] = 0`**: the Lie derivative commutes with the differential. -/
theorem lieDerivAlt_ceDAlt : ∀ {n : ℕ} (x : L) (ω : L [⋀^Fin n]→ₗ[R] M),
    lieDerivAlt x (ceDAlt ω) = ceDAlt (lieDerivAlt x ω)
  | 0, x, ω => by
    refine ext_curryLeft fun y => ?_
    rw [curryLeft_lieDerivAlt, curryLeft_ceDAlt_zero, curryLeft_ceDAlt_zero,
      curryLeft_ceDAlt_zero, ← lieDerivAlt_comm]
    abel
  | n + 1, x, ω => by
    refine ext_curryLeft fun y => ?_
    have IH := lieDerivAlt_ceDAlt x (ω.curryLeft y)
    rw [curryLeft_lieDerivAlt, curryLeft_ceDAlt, curryLeft_ceDAlt, curryLeft_ceDAlt,
      curryLeft_lieDerivAlt, lieDerivAlt_sub, ceDAlt_sub, IH, ← lieDerivAlt_comm]
    abel

/-- **`d ∘ d = 0`.** The Chevalley–Eilenberg forms form a cochain complex. -/
theorem ceDAlt_ceDAlt : ∀ {n : ℕ} (ω : L [⋀^Fin n]→ₗ[R] M), ceDAlt (ceDAlt ω) = 0
  | 0, ω => by
    refine ext_curryLeft fun x => ?_
    rw [curryLeft_ceDAlt, curryLeft_ceDAlt_zero, lieDerivAlt_ceDAlt, sub_self]
    ext; simp
  | n + 1, ω => by
    refine ext_curryLeft fun x => ?_
    rw [curryLeft_ceDAlt, curryLeft_ceDAlt, ceDAlt_sub, ceDAlt_ceDAlt (ω.curryLeft x),
      lieDerivAlt_ceDAlt, sub_zero, sub_self]
    ext; simp

end Calculus

end QOU.LieDerivative
