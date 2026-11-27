import QOU.BraidsAndKnots.RationalAssociator.AssociatorInduction

/-!
# Drinfeld's Proposition 5.7: the vanishing lemma

Bean `qou-3fdg` (epic `qou-dk7p`), gap (B2) of audit §13.

Drinfeld (1991, Prop. 5.7) proves that (5.17), (5.18), (5.20) imply (5.19) for a Lie element
`ψ`. Put `s(B, C) = [B, ψ(A, B)] + [C, ψ(A, C)]`, `A = −B − C`. The proof has two steps:

1. `s` is symmetric and satisfies the cocycle identity (5.24)
   `s(Y₁, Y₂) − s(Y₁, Y₂ + Y₃) + s(Y₁ + Y₂, Y₃) − s(Y₂, Y₃) = 0`;
2. a symmetric Lie polynomial satisfying (5.24) is zero.

This file proves step 2, in a truncated form and by a purely algebraic argument (Drinfeld cites
a representation-theoretic one). The hypotheses on `s ∈ ℚ⟨B, C⟩` are:

* `LieLike s`: at every commuting pair `x, y` of any `ℚ`-algebra, `s(x, y) = α x + β y` for fixed
  `α, β ∈ ℚ`. Every Lie polynomial has this property (`LieLike` of a bracket is checked in
  `Prop57Cocycle`); it is all the argument uses of "Lie".
* symmetry `s(C, B) = s(B, C)` as a polynomial;
* (5.24) modulo the words of length `≥ N` in `ℚ⟨Y₁, Y₂, Y₃⟩`.

The conclusion is `s ∈ FF N`: every word of length `< N` has coefficient `0` in `s`
(`vanishing_of_cocycle`).

**The argument.** Substitute `Y₁ = B`, `Y₂ = C`, `Y₃ = x·C` with a central variable `x` and take
the coefficient of `x`; do the same with `B` and `C` exchanged. With symmetry, and with the
linearity of the `x`-coefficient in the direction of the derivative, the two identities add up to

  `E(s) = f(B + C) − f(B) − f(C)` modulo `FF N`, where `f(Z) = [x¹] s(Z, x·Z)`,

and `E` multiplies each word by its length. `LieLike` gives `f(Z) = β Z`, so the right side is
`0`. Then `n · sₙ = 0` for every homogeneous part `sₙ` of degree `n < N`, and `s₀ = 0` again by
`LieLike`. Nothing analytic is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open Polynomial

local notation "F2" => FreeAlgebra ℚ (Fin 2)
local notation "F3" => FreeAlgebra ℚ (Fin 3)

/-! ### Word filtrations -/

section Filtrations

/-- The span of the words of length at least `m` in `ℚ⟨Y₁, Y₂, Y₃⟩`. -/
def FF3 (m : ℕ) : Submodule ℚ F3 :=
  Submodule.span ℚ {p | ∃ w : List (Fin 3), m ≤ w.length ∧ p = (w.map (FreeAlgebra.ι ℚ)).prod}

/-- Polynomials over `ℚ⟨B, C⟩` all of whose coefficients lie in `FF m`. -/
def PF (m : ℕ) : Submodule ℚ F2[X] where
  carrier := {p | ∀ k, p.coeff k ∈ FF m}
  add_mem' {p q} hp hq k := by rw [coeff_add]; exact add_mem (hp k) (hq k)
  zero_mem' _ := by simp
  smul_mem' r p hp k := by rw [coeff_smul]; exact Submodule.smul_mem _ r (hp k)

theorem mem_PF {m : ℕ} {p : F2[X]} : p ∈ PF m ↔ ∀ k, p.coeff k ∈ FF m := Iff.rfl

theorem PF_anti {m n : ℕ} (h : m ≤ n) : PF n ≤ PF m := fun _ hp k => FF_anti h (hp k)

theorem mul_mem_PF {a b : ℕ} {p q : F2[X]} (hp : p ∈ PF a) (hq : q ∈ PF b) :
    p * q ∈ PF (a + b) := by
  intro k
  rw [coeff_mul]
  exact Submodule.sum_mem _ fun x _ => mul_mem_FF (hp x.1) (hq x.2)

theorem mem_PF_zero (p : F2[X]) : p ∈ PF 0 := fun _ => mem_FF_zero _

theorem C_mem_PF {m : ℕ} {a : F2} (ha : a ∈ FF m) : C a ∈ PF m := by
  intro k
  rw [coeff_C]
  split_ifs
  · exact ha
  · exact zero_mem _

theorem C_mul_X_mem_PF {m : ℕ} {a : F2} (ha : a ∈ FF m) : C a * X ∈ PF m := by
  intro k
  cases k with
  | zero => simp
  | succ k =>
    rw [coeff_mul_X, coeff_C]
    split_ifs
    · exact ha
    · exact zero_mem _

theorem lift_word_mem_PF (v : Fin 3 → F2[X]) (hv : ∀ i, v i ∈ PF 1) (w : List (Fin 3)) :
    FreeAlgebra.lift ℚ v (w.map (FreeAlgebra.ι ℚ)).prod ∈ PF w.length := by
  induction w with
  | nil => simpa using mem_PF_zero 1
  | cons i w ih =>
    simp only [List.map_cons, List.prod_cons, map_mul, FreeAlgebra.lift_ι_apply,
      List.length_cons]
    have := mul_mem_PF (hv i) ih
    rwa [add_comm] at this

/-- An algebra map `ℚ⟨Y₁, Y₂, Y₃⟩ → ℚ⟨B, C⟩[x]` sending the generators into `PF 1` sends
`FF3 N` into `PF N`. -/
theorem lift_mem_PF {N : ℕ} (v : Fin 3 → F2[X]) (hv : ∀ i, v i ∈ PF 1) {p : F3}
    (hp : p ∈ FF3 N) : FreeAlgebra.lift ℚ v p ∈ PF N := by
  induction hp using Submodule.span_induction with
  | mem x hx =>
    obtain ⟨w, hw, rfl⟩ := hx
    exact PF_anti hw (lift_word_mem_PF v hv w)
  | zero => simp
  | add x y _ _ hx hy => rw [map_add]; exact add_mem hx hy
  | smul r x _ hx => rw [map_smul]; exact Submodule.smul_mem _ r hx

end Filtrations


/-! ### The directional derivative and the homogeneous parts -/

section Derivative

/-- The value of `s` at `(a + x·da, b + x·db)` as a polynomial in a central variable `x`. -/
noncomputable def lineEval (a b da db : F2) (s : F2) : F2[X] :=
  eval (C a + C da * X) (C b + C db * X) s

/-- The derivative of `s` at `(a, b)` in the direction `(da, db)`: the `x`-coefficient. -/
noncomputable def dirD (a b da db : F2) (s : F2) : F2 := (lineEval a b da db s).coeff 1

theorem lineEval_coeff_zero (a b da db s : F2) : (lineEval a b da db s).coeff 0 = eval a b s := by
  induction s using FreeAlgebra.induction with
  | grade0 r =>
    simp only [lineEval, AlgHom.commutes]
    rw [Polynomial.algebraMap_apply, coeff_C_zero]
  | grade1 i => fin_cases i <;> simp [lineEval]
  | mul p q hp hq =>
    simp only [lineEval, map_mul, mul_coeff_zero] at hp hq ⊢
    rw [hp, hq]
  | add p q hp hq =>
    simp only [lineEval, map_add, coeff_add] at hp hq ⊢
    rw [hp, hq]

theorem dirD_mul (a b da db p q : F2) :
    dirD a b da db (p * q) = eval a b p * dirD a b da db q + dirD a b da db p * eval a b q := by
  simp only [dirD]
  have h := coeff_one_mul (lineEval a b da db p) (lineEval a b da db q)
  simp only [lineEval, map_mul] at h ⊢
  rw [h]
  have hp := lineEval_coeff_zero a b da db p
  have hq := lineEval_coeff_zero a b da db q
  simp only [lineEval] at hp hq
  rw [hp, hq]

/-- The derivative is additive in the direction. -/
theorem dirD_add_dir (a b da db ea eb s : F2) :
    dirD a b (da + ea) (db + eb) s = dirD a b da db s + dirD a b ea eb s := by
  induction s using FreeAlgebra.induction with
  | grade0 r =>
    simp only [dirD, lineEval, AlgHom.commutes, Polynomial.algebraMap_apply, coeff_C]
    simp
  | grade1 i => fin_cases i <;> simp [dirD, lineEval, coeff_C]
  | mul p q hp hq =>
    rw [dirD_mul, dirD_mul, dirD_mul, hp, hq]; noncomm_ring
  | add p q hp hq =>
    simp only [dirD, lineEval, map_add, coeff_add] at hp hq ⊢
    rw [hp, hq]; abel

/-- The homogeneous parts of `s`: `(homPoly s).coeff n` is the degree-`n` part. -/
noncomputable def homPoly (s : F2) : F2[X] :=
  eval (C (FreeAlgebra.ι ℚ 0) * X) (C (FreeAlgebra.ι ℚ 1) * X) s

/-- The word with letters `w`. -/
noncomputable def word (w : List (Fin 2)) : F2 := (w.map (FreeAlgebra.ι ℚ)).prod

theorem homPoly_word (w : List (Fin 2)) : homPoly (word w) = C (word w) * X ^ w.length := by
  induction w with
  | nil => simp [homPoly, word]
  | cons i w ih =>
    simp only [homPoly, word, List.map_cons, List.prod_cons, map_mul, List.length_cons] at ih ⊢
    have he : eval (C (FreeAlgebra.ι ℚ 0) * X) (C (FreeAlgebra.ι ℚ 1) * X) (FreeAlgebra.ι ℚ i) =
        C (FreeAlgebra.ι ℚ i) * X := by fin_cases i <;> simp
    rw [ih, he, mul_assoc, ← mul_assoc X, (commute_X _).eq, mul_assoc, ← pow_succ',
      mul_assoc]

/-- Induction over words: a property closed under `0`, `+` and `ℚ`-scaling that holds on every
word holds on all of `ℚ⟨B, C⟩`. -/
theorem word_induction {P : F2 → Prop} (h0 : P 0) (hadd : ∀ p q, P p → P q → P (p + q))
    (hsmul : ∀ (r : ℚ) p, P p → P (r • p)) (hw : ∀ w, P (word w)) (s : F2) : P s := by
  have hs := mem_FF_zero s
  induction hs using Submodule.span_induction with
  | mem x hx => obtain ⟨w, -, rfl⟩ := hx; exact hw w
  | zero => exact h0
  | add x y _ _ hx hy => exact hadd x y hx hy
  | smul r x _ hx => exact hsmul r x hx

theorem coeff_homPoly_word (w : List (Fin 2)) (n : ℕ) :
    (homPoly (word w)).coeff n = if n = w.length then word w else 0 := by
  rw [homPoly_word, coeff_C_mul, coeff_X_pow]
  split_ifs <;> simp

/-- The parts of degree `< N` of an element of `FF N` vanish. -/
theorem coeff_homPoly_of_mem_FF {N n : ℕ} (hn : n < N) {p : F2} (hp : p ∈ FF N) :
    (homPoly p).coeff n = 0 := by
  induction hp using Submodule.span_induction with
  | mem x hx =>
    obtain ⟨w, hw, rfl⟩ := hx
    rw [show (w.map (FreeAlgebra.ι ℚ)).prod = word w from rfl, coeff_homPoly_word, if_neg (by omega)]
  | zero => simp [homPoly]
  | add x y _ _ hx hy => simp only [homPoly, map_add, coeff_add] at hx hy ⊢; rw [hx, hy, add_zero]
  | smul r x _ hx => simp only [homPoly, map_smul, coeff_smul] at hx ⊢; rw [hx, smul_zero]

/-- `s` minus its parts of degree `< N` lies in `FF N`. -/
theorem sub_sum_homPoly_mem_FF (N : ℕ) (s : F2) :
    s - ∑ n ∈ Finset.range N, (homPoly s).coeff n ∈ FF N := by
  induction s using word_induction with
  | h0 => simp [homPoly]
  | hadd p q hp hq =>
    have := add_mem hp hq
    simp only [homPoly, map_add, coeff_add, Finset.sum_add_distrib] at this ⊢
    convert this using 1; abel
  | hsmul r p hp =>
    have := Submodule.smul_mem _ r hp
    simp only [homPoly, map_smul, coeff_smul, ← Finset.smul_sum, smul_sub] at this ⊢
    exact this
  | hw w =>
    simp only [coeff_homPoly_word, Finset.sum_ite_eq', Finset.mem_range]
    split_ifs with h
    · simp
    · rw [sub_zero]; exact word_mem_FF w (by omega)

/-- The degree-`n` part is homogeneous of degree `n`. -/
theorem coeff_homPoly_coeff_homPoly (s : F2) (m n : ℕ) :
    (homPoly ((homPoly s).coeff n)).coeff m = if m = n then (homPoly s).coeff n else 0 := by
  induction s using word_induction with
  | h0 => simp [homPoly]
  | hadd p q hp hq =>
    simp only [homPoly, map_add, coeff_add] at hp hq ⊢
    rw [hp, hq]; split_ifs <;> simp
  | hsmul r p hp =>
    simp only [homPoly, map_smul, coeff_smul] at hp ⊢
    rw [hp]; split_ifs <;> simp
  | hw w =>
    rw [coeff_homPoly_word]
    split_ifs with h1 h2 h2
    · rw [coeff_homPoly_word, if_pos (h2.trans h1)]
    · rw [coeff_homPoly_word, if_neg (fun h => h2 (h.trans h1.symm))]
    · simp [homPoly]
    · simp [homPoly]

/-- The Euler operator: the derivative at `(B, C)` in the direction `(B, C)`. -/
noncomputable def euler (s : F2) : F2 :=
  dirD (FreeAlgebra.ι ℚ 0) (FreeAlgebra.ι ℚ 1) (FreeAlgebra.ι ℚ 0) (FreeAlgebra.ι ℚ 1) s

theorem lineEval_word (w : List (Fin 2)) :
    lineEval (FreeAlgebra.ι ℚ 0) (FreeAlgebra.ι ℚ 1) (FreeAlgebra.ι ℚ 0) (FreeAlgebra.ι ℚ 1)
      (word w) = C (word w) * (X + 1) ^ w.length := by
  induction w with
  | nil => simp [lineEval, word]
  | cons i w ih =>
    simp only [lineEval, word, List.map_cons, List.prod_cons, map_mul, List.length_cons] at ih ⊢
    have he : eval (C (FreeAlgebra.ι ℚ 0) + C (FreeAlgebra.ι ℚ 0) * X)
        (C (FreeAlgebra.ι ℚ 1) + C (FreeAlgebra.ι ℚ 1) * X) (FreeAlgebra.ι ℚ i) =
        C (FreeAlgebra.ι ℚ i) * (X + 1) := by fin_cases i <;> simp [mul_add, add_comm]
    rw [ih, he, mul_assoc, ← mul_assoc (X + 1), ((commute_X _).add_left (Commute.one_left _)).eq,
      mul_assoc, ← pow_succ', mul_assoc]

theorem euler_word (w : List (Fin 2)) : euler (word w) = (w.length : ℚ) • word w := by
  rw [euler, dirD, lineEval_word, coeff_C_mul, coeff_X_add_one_pow, Nat.choose_one_right,
    Algebra.smul_def, map_natCast]
  exact (Nat.cast_commute _ _).eq.symm

theorem euler_add (p q : F2) : euler (p + q) = euler p + euler q := by
  simp [euler, dirD, lineEval]

theorem euler_smul (r : ℚ) (p : F2) : euler (r • p) = r • euler p := by
  simp [euler, dirD, lineEval]

/-- The Euler operator multiplies the degree-`n` part by `n`. -/
theorem coeff_homPoly_euler (s : F2) (n : ℕ) :
    (homPoly (euler s)).coeff n = (n : ℚ) • (homPoly s).coeff n := by
  induction s using word_induction with
  | h0 => simp [euler, dirD, lineEval, homPoly]
  | hadd p q hp hq => simp only [euler_add, homPoly, map_add, coeff_add] at hp hq ⊢; rw [hp, hq, smul_add]
  | hsmul r p hp =>
    simp only [euler_smul, homPoly, map_smul, coeff_smul] at hp ⊢; rw [hp, smul_comm]
  | hw w =>
    rw [euler_word, homPoly, map_smul, coeff_smul]
    change (w.length : ℚ) • (homPoly (word w)).coeff n = _
    rw [coeff_homPoly_word]
    split_ifs with h
    · rw [h]
    · simp

end Derivative

/-! ### The vanishing lemma -/

section Vanishing

/-- **"Lie" as the argument uses it.** At every commuting pair the polynomial is linear, with
coefficients independent of the pair. Every Lie polynomial has this property. -/
def LieLike (s : F2) : Prop :=
  ∃ α β : ℚ, ∀ (R : Type) [Ring R] [Algebra ℚ R] (x y : R), Commute x y →
    eval x y s = α • x + β • y

/-- The generators `Y₁, Y₂, Y₃` of `ℚ⟨Y₁, Y₂, Y₃⟩` (indices `0, 1, 2`). -/
noncomputable abbrev Y3 (i : Fin 3) : F3 := FreeAlgebra.ι ℚ i

/-- The left side of Drinfeld's (5.24) for `s`:
`s(Y₁, Y₂) − s(Y₁, Y₂ + Y₃) + s(Y₁ + Y₂, Y₃) − s(Y₂, Y₃)`. -/
noncomputable def cocycle (s : F2) : F3 :=
  eval (Y3 0) (Y3 1) s - eval (Y3 0) (Y3 1 + Y3 2) s + eval (Y3 0 + Y3 1) (Y3 2) s -
    eval (Y3 1) (Y3 2) s

theorem dirD_zero_dir (a b s : F2) : dirD a b 0 0 s = 0 := by
  have h := dirD_add_dir a b 0 0 0 0 s
  simp only [add_zero] at h
  exact left_eq_add.mp h |>.symm ▸ rfl

theorem eval_swap_of_symm {s : F2} (hsym : eval (FreeAlgebra.ι ℚ 1) (FreeAlgebra.ι ℚ 0) s = s)
    {R : Type*} [Ring R] [Algebra ℚ R] (x y : R) : eval x y s = eval y x s := by
  conv_lhs => rw [← hsym]
  rw [map_eval]; simp

theorem lift_eval (v : Fin 3 → F2[X]) (i j : Fin 3) (s : F2) :
    FreeAlgebra.lift ℚ v (eval (Y3 i) (Y3 j) s) = eval (v i) (v j) s := by
  rw [map_eval]; simp

theorem lift_eval_add (v : Fin 3 → F2[X]) (i j k : Fin 3) (s : F2) :
    FreeAlgebra.lift ℚ v (eval (Y3 i) (Y3 j + Y3 k) s) = eval (v i) (v j + v k) s := by
  rw [map_eval]; simp

theorem lift_eval_add' (v : Fin 3 → F2[X]) (i j k : Fin 3) (s : F2) :
    FreeAlgebra.lift ℚ v (eval (Y3 i + Y3 j) (Y3 k) s) = eval (v i + v j) (v k) s := by
  rw [map_eval]; simp

/-- The `x`-coefficient of (5.24) at `Y₁ = a`, `Y₂ = b`, `Y₃ = x·b`. -/
theorem cocycle_coeff_one (a b s : F2) :
    (FreeAlgebra.lift ℚ ![C a, C b, C b * X] (cocycle s)).coeff 1 =
      -dirD a b 0 b s + dirD (a + b) 0 0 b s - dirD b 0 0 b s := by
  have h0 := dirD_zero_dir a b s
  simp only [cocycle, map_sub, map_add, lift_eval, lift_eval_add, lift_eval_add', coeff_sub,
    coeff_add] at h0 ⊢
  simp only [dirD, lineEval, map_zero, zero_mul, add_zero, zero_add, Matrix.cons_val_zero,
    Matrix.cons_val_one, Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons, C_add] at h0 ⊢
  rw [h0]; abel

theorem cocycle_lift_mem {N : ℕ} {s : F2} (hc : cocycle s ∈ FF3 N) (a b : F2) (ha : a ∈ FF 1)
    (hb : b ∈ FF 1) : -dirD a b 0 b s + dirD (a + b) 0 0 b s - dirD b 0 0 b s ∈ FF N := by
  rw [← cocycle_coeff_one]
  refine lift_mem_PF _ ?_ hc 1
  intro i
  fin_cases i
  · exact C_mem_PF ha
  · exact C_mem_PF hb
  · exact C_mul_X_mem_PF hb

theorem dirD_diag_of_lieLike {s : F2} {α β : ℚ}
    (h : ∀ (R : Type) [Ring R] [Algebra ℚ R] (x y : R), Commute x y → eval x y s = α • x + β • y)
    (z : F2) : dirD z 0 0 z s = β • z := by
  have hc : Commute (C z : F2[X]) (C z * X) := (Commute.refl _).mul_right (commute_X _).symm
  simp only [dirD, lineEval, map_zero, zero_mul, add_zero, zero_add]
  rw [h _ _ _ hc, coeff_add, coeff_smul, coeff_smul, coeff_C, coeff_mul_X, coeff_C_zero]
  simp

/-- **The vanishing lemma** (Drinfeld, Prop. 5.7, second step), truncated at degree `N`. A
symmetric `LieLike` polynomial `s(B, C)` whose (5.24) holds modulo the words of length `≥ N`
lies in `FF N`. -/
theorem vanishing_of_cocycle {N : ℕ} {s : F2} (hL : LieLike s)
    (hsym : eval (FreeAlgebra.ι ℚ 1) (FreeAlgebra.ι ℚ 0) s = s) (hc : cocycle s ∈ FF3 N) :
    s ∈ FF N := by
  obtain ⟨α, β, hL⟩ := hL
  set b : F2 := FreeAlgebra.ι ℚ 0
  set c : F2 := FreeAlgebra.ι ℚ 1
  have hb : b ∈ FF 1 := ι_mem_FF_one 0
  have hc' : c ∈ FF 1 := ι_mem_FF_one 1
  have h1 := cocycle_lift_mem hc b c hb hc'
  have h2 := cocycle_lift_mem hc c b hc' hb
  have hswap : dirD c b 0 b s = dirD b c b 0 s := by
    simp only [dirD, lineEval]
    rw [eval_swap_of_symm hsym]
  have hd := dirD_diag_of_lieLike hL
  have hE : euler s = dirD b c b 0 s + dirD b c 0 c s := by
    rw [euler, ← dirD_add_dir, add_zero, zero_add]
  have hbc : dirD (b + c) 0 0 (b + c) s = dirD (b + c) 0 0 b s + dirD (b + c) 0 0 c s := by
    rw [← dirD_add_dir, add_zero]
  have hEs : euler s ∈ FF N := by
    have hsum := add_mem h1 h2
    rw [hswap, hd, hd, add_comm c b] at hsum
    rw [hd, smul_add] at hbc
    have : euler s = -((-dirD b c 0 c s + dirD (b + c) 0 0 c s - β • c) +
        (-dirD b c b 0 s + dirD (b + c) 0 0 b s - β • b)) := by
      rw [hE]
      apply eq_of_sub_eq_zero
      rw [show dirD b c b 0 s + dirD b c 0 c s - -((-dirD b c 0 c s + dirD (b + c) 0 0 c s - β • c) +
          (-dirD b c b 0 s + dirD (b + c) 0 0 b s - β • b)) =
          (dirD (b + c) 0 0 b s + dirD (b + c) 0 0 c s) - (β • b + β • c) by abel, ← hbc, sub_self]
    rw [this]
    exact neg_mem hsum
  have hz : ∀ n < N, (homPoly s).coeff n = 0 := by
    intro n hn
    rcases Nat.eq_zero_or_pos n with rfl | hpos
    · have h00 := lineEval_coeff_zero 0 0 b c s
      have e : lineEval 0 0 b c s = homPoly s := by simp [lineEval, homPoly, b, c]
      rw [e, hL F2 0 0 (Commute.zero_left 0)] at h00
      simpa using h00
    · have := coeff_homPoly_euler s n
      rw [coeff_homPoly_of_mem_FF hn hEs] at this
      have hn0 : (n : ℚ) ≠ 0 := by exact_mod_cast hpos.ne'
      exact (smul_eq_zero.mp this.symm).resolve_left hn0
  have := sub_sum_homPoly_mem_FF N s
  rwa [Finset.sum_eq_zero (fun n hn => hz n (Finset.mem_range.mp hn)), sub_zero] at this

end Vanishing

end QOU.BraidsAndKnots.RationalAssociator
