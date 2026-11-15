import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Commutativity of the Gaudin / KZ connection components

For `n` distinct points `z : Fin n → k` and tangent vectors `u, v`, the KZ form evaluated on
`u` is `Σ_{a,b} w_ab(u) Ω_ab` with `w_ab(u) = (u_a − u_b)/(z_a − z_b)` and residue
`Ω_ab = ρ(a b) − c`, for any representation `ρ` of `S_n` in a `k`-algebra. We prove the
`n`-point statement `[ω(u), ω(v)] = 0` (`gaudinOp_commute`, `kzOp_commute`): the
commutator reduces to sums over triples, which cancel in cyclic threes by the Arnold
relation, and `3 ≠ 0` in characteristic zero.
-/

namespace QOU.Mass.KZHolonomy

open Equiv Finset

variable {k : Type*} [Field k] {R : Type*} [Ring R] [Algebra k R] {n : ℕ}

/-- `w z u a b = (u a - u b)/(z a - z b)`: the form `d log(z_a - z_b)` on the tangent vector `u`. -/
def dlogPair (z u : Fin n → k) (a b : Fin n) : k := (u a - u b) / (z a - z b)

/-- `gaudinOp ρ z u = Σ_{a,b} w_ab(u) • ρ(swap a b)` (terms with a = b vanish since w_aa = 0). -/
noncomputable def gaudinOp (ρ : Equiv.Perm (Fin n) →* R) (z u : Fin n → k) : R :=
  ∑ a, ∑ b, dlogPair z u a b • ρ (Equiv.swap a b)

/-- The KZ operator with residues `Ω_ab = ρ(swap a b) - c`. -/
noncomputable def kzOp (ρ : Equiv.Perm (Fin n) →* R) (c : k) (z u : Fin n → k) : R :=
  ∑ a, ∑ b, dlogPair z u a b • (ρ (Equiv.swap a b) - algebraMap k R c)

lemma dlogPair_self (z u : Fin n → k) (a : Fin n) : dlogPair z u a a = 0 := by
  simp [dlogPair]

lemma dlogPair_comm (z u : Fin n → k) (a b : Fin n) : dlogPair z u a b = dlogPair z u b a := by
  unfold dlogPair
  rw [← neg_sub (u b), ← neg_sub (z b), neg_div_neg_eq]

/-- Three-cycle identity: for distinct `a, b, d`, `(a b)(b d) = (b d)(d a)`. -/
lemma swap_mul_swap_cyc {a b d : Fin n} (hab : a ≠ b) (hbd : b ≠ d) (had : a ≠ d) :
    swap a b * swap b d = swap b d * swap d a := by
  ext x
  simp only [Perm.mul_apply, swap_apply_def]
  split_ifs <;> simp_all

lemma swap_mul_swap_disj {a b c d : Fin n} (hac : a ≠ c) (had : a ≠ d) (hbc : b ≠ c)
    (hbd : b ≠ d) : swap a b * swap c d = swap c d * swap a b := by
  ext x
  simp only [Perm.mul_apply, swap_apply_def]
  split_ifs <;> simp_all

/-- The Arnold relation for the triple `(a, b, d)`. -/
lemma arnold_triple {z : Fin n → k} (hz : Function.Injective z) (u v : Fin n → k)
    {a b d : Fin n} (hab : a ≠ b) (hbd : b ≠ d) (had : a ≠ d) :
    (dlogPair z u a b * dlogPair z v b d - dlogPair z u d b * dlogPair z v b a) +
      (dlogPair z u b d * dlogPair z v d a - dlogPair z u a d * dlogPair z v d b) +
      (dlogPair z u d a * dlogPair z v a b - dlogPair z u b a * dlogPair z v a d) = 0 := by
  have h1 : z a - z b ≠ 0 := sub_ne_zero.2 (hz.ne hab)
  have h2 : z b - z d ≠ 0 := sub_ne_zero.2 (hz.ne hbd)
  have h3 : z a - z d ≠ 0 := sub_ne_zero.2 (hz.ne had)
  have h1' : z b - z a ≠ 0 := sub_ne_zero.2 (hz.ne hab.symm)
  have h2' : z d - z b ≠ 0 := sub_ne_zero.2 (hz.ne hbd.symm)
  have h3' : z d - z a ≠ 0 := sub_ne_zero.2 (hz.ne had.symm)
  unfold dlogPair
  field_simp
  ring

/-- A single term of the commutator `[gaudinOp u, gaudinOp v]`. -/
noncomputable def commTerm (ρ : Equiv.Perm (Fin n) →* R) (z u v : Fin n → k) (a b c d : Fin n) :
    R :=
  (dlogPair z u a b * dlogPair z v c d) •
    (ρ (swap a b) * ρ (swap c d) - ρ (swap c d) * ρ (swap a b))

lemma commTerm_swap₁ (ρ : Equiv.Perm (Fin n) →* R) (z u v : Fin n → k) (a b c d : Fin n) :
    commTerm ρ z u v a b c d = commTerm ρ z u v b a c d := by
  simp only [commTerm, dlogPair_comm z u a b, swap_comm a b]

lemma commTerm_swap₂ (ρ : Equiv.Perm (Fin n) →* R) (z u v : Fin n → k) (a b c d : Fin n) :
    commTerm ρ z u v a b c d = commTerm ρ z u v a b d c := by
  simp only [commTerm, dlogPair_comm z v c d, swap_comm c d]

/-- Each commutator term equals the sum of its four "one shared index" indicator copies. -/
lemma commTerm_split (ρ : Equiv.Perm (Fin n) →* R) (z u v : Fin n → k) (a b c d : Fin n) :
    commTerm ρ z u v a b c d =
      (if c = b then commTerm ρ z u v a b c d else 0) +
        (if c = a then commTerm ρ z u v a b c d else 0) +
        (if d = a then commTerm ρ z u v a b c d else 0) +
        (if d = b then commTerm ρ z u v a b c d else 0) := by
  by_cases hab : a = b
  · subst hab; simp [commTerm, dlogPair_self]
  by_cases hcd : c = d
  · subst hcd; simp [commTerm, dlogPair_self]
  have hT : ∀ (h : c = b ∧ d = a ∨ c = a ∧ d = b ∨ (c ≠ a ∧ c ≠ b ∧ d ≠ a ∧ d ≠ b)),
      commTerm ρ z u v a b c d = 0 := by
    intro h
    rcases h with ⟨rfl, rfl⟩ | ⟨rfl, rfl⟩ | ⟨h1, h2, h3, h4⟩
    · simp [commTerm, swap_comm c d]
    · simp [commTerm]
    · simp only [commTerm]
      rw [← map_mul, ← map_mul, swap_mul_swap_disj (Ne.symm h1) (Ne.symm h3) (Ne.symm h2)
        (Ne.symm h4), sub_self, smul_zero]
  by_cases h : c = b ∧ d = a ∨ c = a ∧ d = b ∨ (c ≠ a ∧ c ≠ b ∧ d ≠ a ∧ d ≠ b)
  · rw [hT h]; simp
  · split_ifs <;> subst_vars <;> simp_all

lemma sum_four (F : Fin n → Fin n → R) (a b : Fin n)
    (h : ∀ c d, F c d = (if c = b then F c d else 0) + (if c = a then F c d else 0) +
      (if d = a then F c d else 0) + (if d = b then F c d else 0)) :
    ∑ c, ∑ d, F c d = ∑ d, F b d + ∑ d, F a d + ∑ c, F c a + ∑ c, F c b := by
  rw [Finset.sum_congr rfl fun c _ => Finset.sum_congr rfl fun d _ => h c d]
  simp only [Finset.sum_add_distrib]
  congr 1
  congr 1
  congr 1
  · rw [Finset.sum_comm]; simp
  · rw [Finset.sum_comm]; simp
  · simp
  · simp

/-- Reindexing a triple sum by reversal `(a, b, d) ↦ (d, b, a)`. -/
lemma sum_rev {M : Type*} [AddCommMonoid M] (f : Fin n → Fin n → Fin n → M) :
    ∑ a, ∑ b, ∑ d, f a b d = ∑ a, ∑ b, ∑ d, f d b a := by
  let e : Fin n × Fin n × Fin n ≃ Fin n × Fin n × Fin n :=
    ⟨fun x => (x.2.2, x.2.1, x.1), fun x => (x.2.2, x.2.1, x.1), fun _ => rfl, fun _ => rfl⟩
  have := Fintype.sum_equiv e (fun x => f x.1 x.2.1 x.2.2) (fun x => f x.2.2 x.2.1 x.1)
    (fun _ => rfl)
  simpa [Fintype.sum_prod_type] using this

/-- Reindexing a triple sum by the cyclic rotation `(a, b, d) ↦ (b, d, a)`. -/
lemma sum_cyc {M : Type*} [AddCommMonoid M] (f : Fin n → Fin n → Fin n → M) :
    ∑ a, ∑ b, ∑ d, f a b d = ∑ a, ∑ b, ∑ d, f b d a := by
  let e : Fin n × Fin n × Fin n ≃ Fin n × Fin n × Fin n :=
    ⟨fun x => (x.2.2, x.1, x.2.1), fun x => (x.2.1, x.2.2, x.1), fun _ => rfl, fun _ => rfl⟩
  have := Fintype.sum_equiv e (fun x => f x.1 x.2.1 x.2.2) (fun x => f x.2.1 x.2.2 x.1)
    (fun _ => rfl)
  simpa [Fintype.sum_prod_type] using this

/-- The Arnold-relation coefficient attached to the ordered triple `(a, b, d)`. -/
def coef (z u v : Fin n → k) (a b d : Fin n) : k :=
  dlogPair z u a b * dlogPair z v b d - dlogPair z u d b * dlogPair z v b a

/-- Cyclic cancellation: the three rotations of a triple contribute zero in total. -/
lemma cyc_cancel (ρ : Equiv.Perm (Fin n) →* R) {z : Fin n → k} (hz : Function.Injective z)
    (u v : Fin n → k) (a b d : Fin n) :
    coef z u v a b d • (ρ (swap a b) * ρ (swap b d)) +
      coef z u v b d a • (ρ (swap b d) * ρ (swap d a)) +
      coef z u v d a b • (ρ (swap d a) * ρ (swap a b)) = 0 := by
  by_cases hab : a = b
  · subst hab; simp [coef, dlogPair_self]
  by_cases hbd : b = d
  · subst hbd; simp [coef, dlogPair_self]
  by_cases had : a = d
  · subst had; simp [coef, dlogPair_self]
  have g1 : ρ (swap b d) * ρ (swap d a) = ρ (swap a b) * ρ (swap b d) := by
    rw [← map_mul, ← map_mul, swap_mul_swap_cyc hab hbd had]
  have g2 : ρ (swap d a) * ρ (swap a b) = ρ (swap a b) * ρ (swap b d) := by
    rw [← map_mul, ← map_mul, ← swap_mul_swap_cyc hbd (Ne.symm had) (Ne.symm hab),
      ← swap_mul_swap_cyc hab hbd had]
  rw [g1, g2, ← add_smul, ← add_smul]
  have := arnold_triple hz u v hab hbd had
  simp only [coef]
  rw [this, zero_smul]

variable [CharZero k]

lemma triple_sum_zero (ρ : Equiv.Perm (Fin n) →* R) {z : Fin n → k} (hz : Function.Injective z)
    (u v : Fin n → k) :
    ∑ a, ∑ b, ∑ d, coef z u v a b d • (ρ (swap a b) * ρ (swap b d)) = 0 := by
  set X := ∑ a, ∑ b, ∑ d, coef z u v a b d • (ρ (swap a b) * ρ (swap b d)) with hX
  have h3 : X + X + X = 0 := by
    have e1 := sum_cyc (fun a b d => coef z u v a b d • (ρ (swap a b) * ρ (swap b d)))
    have e2 := sum_cyc (fun a b d => coef z u v b d a • (ρ (swap b d) * ρ (swap d a)))
    simp only at e1 e2
    have E1 : ∑ a, ∑ b, ∑ d, coef z u v b d a • (ρ (swap b d) * ρ (swap d a)) = X := e1.symm
    have E2 : ∑ a, ∑ b, ∑ d, coef z u v d a b • (ρ (swap d a) * ρ (swap a b)) = X :=
      e2.symm.trans e1.symm
    calc X + X + X
        = ∑ a, ∑ b, ∑ d, coef z u v a b d • (ρ (swap a b) * ρ (swap b d)) +
            ∑ a, ∑ b, ∑ d, coef z u v b d a • (ρ (swap b d) * ρ (swap d a)) +
            ∑ a, ∑ b, ∑ d, coef z u v d a b • (ρ (swap d a) * ρ (swap a b)) := by
          rw [E1, E2]
      _ = ∑ a, ∑ b, ∑ d, (coef z u v a b d • (ρ (swap a b) * ρ (swap b d)) +
            coef z u v b d a • (ρ (swap b d) * ρ (swap d a)) +
            coef z u v d a b • (ρ (swap d a) * ρ (swap a b))) := by
          simp only [Finset.sum_add_distrib]
      _ = 0 := by simp [cyc_cancel ρ hz]
  have h3' : (3 : k) • X = 0 := by
    rw [show (3 : k) = 1 + 1 + 1 by norm_num, add_smul, add_smul, one_smul, h3]
  have h3ne : (3 : k) ≠ 0 := by norm_num
  calc X = ((3 : k)⁻¹ * 3) • X := by rw [inv_mul_cancel₀ h3ne, one_smul]
    _ = 0 := by rw [mul_smul, h3', smul_zero]


omit [CharZero k] in
lemma sum_commTerm_diag (ρ : Equiv.Perm (Fin n) →* R) (z u v : Fin n → k) :
    ∑ a, ∑ b, ∑ d, commTerm ρ z u v a b b d =
      ∑ a, ∑ b, ∑ d, coef z u v a b d • (ρ (swap a b) * ρ (swap b d)) := by
  simp only [commTerm, smul_sub, Finset.sum_sub_distrib]
  rw [sum_rev (fun a b d => (dlogPair z u a b * dlogPair z v b d) •
    (ρ (swap b d) * ρ (swap a b)))]
  simp only [coef, sub_smul, Finset.sum_sub_distrib]
  congr 1
  refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ =>
    Finset.sum_congr rfl fun d _ => ?_
  rw [swap_comm b a, swap_comm d b]

lemma sum4_swap {M : Type*} [AddCommMonoid M] (F : Fin n → Fin n → Fin n → Fin n → M) :
    ∑ c, ∑ d, ∑ a, ∑ b, F a b c d = ∑ a, ∑ b, ∑ c, ∑ d, F a b c d := by
  have := Fintype.sum_equiv (Equiv.prodComm (Fin n × Fin n) (Fin n × Fin n))
    (fun x => F x.2.1 x.2.2 x.1.1 x.1.2) (fun x => F x.1.1 x.1.2 x.2.1 x.2.2) (fun _ => rfl)
  simpa [Fintype.sum_prod_type] using this

omit [CharZero k] in
lemma gaudinOp_sub (ρ : Equiv.Perm (Fin n) →* R) (z u v : Fin n → k) :
    gaudinOp ρ z u * gaudinOp ρ z v - gaudinOp ρ z v * gaudinOp ρ z u =
      ∑ a, ∑ b, ∑ c, ∑ d, commTerm ρ z u v a b c d := by
  have h1 : gaudinOp ρ z u * gaudinOp ρ z v = ∑ a, ∑ b, ∑ c, ∑ d,
      (dlogPair z u a b * dlogPair z v c d) • (ρ (swap a b) * ρ (swap c d)) := by
    simp only [gaudinOp, Finset.sum_mul, Finset.mul_sum, smul_mul_smul_comm]
    exact sum4_swap (fun a b c d =>
      (dlogPair z u a b * dlogPair z v c d) • (ρ (swap a b) * ρ (swap c d)))
  have h2 : gaudinOp ρ z v * gaudinOp ρ z u = ∑ a, ∑ b, ∑ c, ∑ d,
      (dlogPair z u a b * dlogPair z v c d) • (ρ (swap c d) * ρ (swap a b)) := by
    simp only [gaudinOp, Finset.sum_mul, Finset.mul_sum, smul_mul_smul_comm]
    simp only [mul_comm (dlogPair z v _ _)]
  rw [h1, h2]
  simp only [commTerm, smul_sub, Finset.sum_sub_distrib]


/-- **Commutativity of the Gaudin operators**: `[Σ w_ab(u) s_ab, Σ w_cd(v) s_cd] = 0`
for pairwise distinct points `z`. -/
theorem gaudinOp_commute (ρ : Equiv.Perm (Fin n) →* R) {z : Fin n → k}
    (hz : Function.Injective z) (u v : Fin n → k) :
    gaudinOp ρ z u * gaudinOp ρ z v = gaudinOp ρ z v * gaudinOp ρ z u := by
  rw [← sub_eq_zero, gaudinOp_sub]
  rw [Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ =>
    sum_four _ a b (fun c d => commTerm_split ρ z u v a b c d)]
  simp only [Finset.sum_add_distrib]
  have hS : ∑ a, ∑ b, ∑ d, commTerm ρ z u v a b b d = 0 :=
    (sum_commTerm_diag ρ z u v).trans (triple_sum_zero ρ hz u v)
  have h2 : ∑ a, ∑ b, ∑ d, commTerm ρ z u v a b a d = 0 := by
    rw [Finset.sum_comm, ← hS]
    exact Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ =>
      Finset.sum_congr rfl fun d _ => commTerm_swap₁ ρ z u v b a b d
  have h3 : ∑ a, ∑ b, ∑ c, commTerm ρ z u v a b c a = 0 := by
    rw [← h2]
    exact Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ =>
      Finset.sum_congr rfl fun c _ => commTerm_swap₂ ρ z u v a b c a
  have h4 : ∑ a, ∑ b, ∑ c, commTerm ρ z u v a b c b = 0 := by
    rw [← hS]
    exact Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ =>
      Finset.sum_congr rfl fun c _ => commTerm_swap₂ ρ z u v a b c b
  rw [hS, h2, h3, h4]
  simp

omit [CharZero k] in
lemma kzOp_eq (ρ : Equiv.Perm (Fin n) →* R) (c : k) (z u : Fin n → k) :
    kzOp ρ c z u = gaudinOp ρ z u - algebraMap k R (∑ a, ∑ b, dlogPair z u a b * c) := by
  simp only [kzOp, gaudinOp, map_sum, map_mul, Algebra.smul_def, mul_sub,
    Finset.sum_sub_distrib]

/-- **Commutativity of the KZ connection components** with residues `Ω_ab = ρ(a b) − c`. -/
theorem kzOp_commute (ρ : Equiv.Perm (Fin n) →* R) (c : k) {z : Fin n → k}
    (hz : Function.Injective z) (u v : Fin n → k) :
    kzOp ρ c z u * kzOp ρ c z v = kzOp ρ c z v * kzOp ρ c z u := by
  have hAB : Commute (gaudinOp ρ z u) (gaudinOp ρ z v) := gaudinOp_commute ρ hz u v
  rw [kzOp_eq, kzOp_eq]
  exact (Commute.sub_left (hAB.sub_right (Algebra.commute_algebraMap_right _ _))
    (Algebra.commute_algebraMap_left _ _)).eq

end QOU.Mass.KZHolonomy
