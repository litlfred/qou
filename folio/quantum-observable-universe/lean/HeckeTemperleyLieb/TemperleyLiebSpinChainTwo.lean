/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import HeckeTemperleyLieb.TemperleyLiebAlgebra
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring

/-!
# The spin-chain representation of `TL_{n+1}(2)`, over any commutative ring

Bean `qou-tcl5`, step 1 of the basis theorem. `TemperleyLiebNormalFormSpanning` proves that
the Jones normal forms span `TL_{n+1}(δ)` and leaves their linear independence open: it
"needs a representation that separates them". This file supplies that representation at
`δ = 2`, for every `n` and over every commutative ring `R`.

The space is `R`-valued functions on spin configurations `τ : Fin (n+1) → Fin 2`. The
generator `e_i` acts on sites `i, i+1` by the unnormalised singlet projector
`|s⟩⟨s|`, `s = |01⟩ − |10⟩`:

    (e_i v)(τ) = s(τ_i, τ_{i+1}) · ( v(τ[i,i+1 ↦ 0,1]) − v(τ[i,i+1 ↦ 1,0]) ),

with `s(0,1) = 1`, `s(1,0) = −1` and `s(a,a) = 0`. This is the `q = 1` point of the quantum
spin chain. We check the three defining relations (`e_i² = 2 e_i`, `e_i e_j e_i = e_i` for
adjacent `i, j`, and far commutation), which gives an `R`-algebra map
`spinRep : TLFin R 2 n →ₐ[R] Module.End R ((Fin (n+1) → Fin 2) → R)`.

## Why `δ = 2` is enough for the basis theorem

Measured exactly (integer arithmetic, `N ≤ 7` strands; bean `qou-tcl5`): the images of the
Catalan(N) normal forms under this map are linearly independent, and their lexicographically
least nonzero matrix entries are pairwise distinct with value `±1`. That echelon pattern is
the general-`n` statement still to be proved here. Independence at the single value `δ = 2`
then lifts to the generic parameter by the `(δ − 2)`-adic specialisation argument.

No empirical input; everything holds over an arbitrary commutative ring.

-- Ref: [jones1983] https://doi.org/10.1007/BF01389127
-/

namespace QOU.MathlibExt.TemperleyLiebSpinChainTwo

open QOU.MathlibExt.TemperleyLieb

variable {R : Type*} [CommRing R] {n : ℕ}

/-- Spin configurations on `n + 1` sites. -/
abbrev Spin (n : ℕ) := Fin (n + 1) → Fin 2

/-- The singlet coefficient: `s(0,1) = 1`, `s(1,0) = -1`, `s(a,a) = 0`. -/
def sgn (R : Type*) [CommRing R] (a b : Fin 2) : R :=
  if a = 0 ∧ b = 1 then 1 else if a = 1 ∧ b = 0 then -1 else 0

/-- Overwrite sites `i, i+1` of `τ` by `a, b`. -/
def put (τ : Spin n) (i : Fin n) (a b : Fin 2) : Spin n :=
  Function.update (Function.update τ i.castSucc a) i.succ b

theorem castSucc_ne_succ (i : Fin n) : i.castSucc ≠ i.succ :=
  (Fin.castSucc_lt_succ i).ne

@[simp] theorem put_castSucc (τ : Spin n) (i : Fin n) (a b : Fin 2) :
    put τ i a b i.castSucc = a := by
  simp [put, castSucc_ne_succ]

@[simp] theorem put_succ (τ : Spin n) (i : Fin n) (a b : Fin 2) :
    put τ i a b i.succ = b := by
  simp [put]

@[simp] theorem put_put (τ : Spin n) (i : Fin n) (a b c d : Fin 2) :
    put (put τ i a b) i c d = put τ i c d := by
  funext t
  simp only [put, Function.update_apply]
  split_ifs <;> simp_all [Fin.ext_iff]

/-- The generator `e_i`. -/
def E (R : Type*) [CommRing R] (i : Fin n) : Module.End R (Spin n → R) where
  toFun v τ := sgn R (τ i.castSucc) (τ i.succ) * (v (put τ i 0 1) - v (put τ i 1 0))
  map_add' v w := by funext τ; simp only [Pi.add_apply]; ring
  map_smul' c v := by funext τ; simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]; ring

theorem E_apply (i : Fin n) (v : Spin n → R) (τ : Spin n) :
    E R i v τ = sgn R (τ i.castSucc) (τ i.succ) * (v (put τ i 0 1) - v (put τ i 1 0)) := rfl

/-- `e_i² = 2 e_i`. -/
theorem E_sq (i : Fin n) :
    E R i * E R i = algebraMap R (Module.End R (Spin n → R)) 2 * E R i := by
  apply LinearMap.ext; intro v; funext τ
  simp only [Module.End.mul_apply, E_apply, put_castSucc, put_succ, put_put,
    Module.algebraMap_end_apply, Pi.smul_apply, smul_eq_mul]
  simp only [sgn]
  norm_num
  ring_nf

/-! ## Three consecutive sites -/

/-- Overwrite three sites `a, b, c` of `τ`. -/
def put3 (τ : Spin n) (a b c : Fin (n + 1)) (x y z : Fin 2) : Spin n :=
  Function.update (Function.update (Function.update τ a x) b y) c z

theorem put3_a {a b c : Fin (n + 1)} (hab : a ≠ b) (hac : a ≠ c) (τ : Spin n) (x y z : Fin 2) :
    put3 τ a b c x y z a = x := by
  simp [put3, hab, hac]

theorem put3_b {a b c : Fin (n + 1)} (hbc : b ≠ c) (τ : Spin n) (x y z : Fin 2) :
    put3 τ a b c x y z b = y := by
  simp [put3, hbc]

theorem put3_c {a b c : Fin (n + 1)} (τ : Spin n) (x y z : Fin 2) :
    put3 τ a b c x y z c = z := by
  simp [put3]

theorem put3_self {a b c : Fin (n + 1)} (τ : Spin n) : put3 τ a b c (τ a) (τ b) (τ c) = τ := by
  funext t
  simp only [put3, Function.update_apply]
  split_ifs <;> simp_all

section Adjacent

variable {i j : Fin n} (hij : i.val + 1 = j.val)
include hij

theorem put_i_put3 (τ : Spin n) (x y z p q : Fin 2) :
    put (put3 τ i.castSucc i.succ j.succ x y z) i p q =
      put3 τ i.castSucc i.succ j.succ p q z := by
  funext t
  simp only [put, put3, Function.update_apply]
  split_ifs <;> simp_all [Fin.ext_iff] <;> omega

theorem put_j_put3 (τ : Spin n) (x y z p q : Fin 2) :
    put (put3 τ i.castSucc i.succ j.succ x y z) j p q =
      put3 τ i.castSucc i.succ j.succ x p q := by
  funext t
  simp only [put, put3, Function.update_apply]
  split_ifs <;> simp_all [Fin.ext_iff]

theorem put_i_eq (τ : Spin n) (p q : Fin 2) :
    put τ i p q = put3 τ i.castSucc i.succ j.succ p q (τ j.succ) := by
  conv_lhs => rw [← put3_self (a := i.castSucc) (b := i.succ) (c := j.succ) τ]
  rw [put_i_put3 hij]

theorem put_j_eq (τ : Spin n) (p q : Fin 2) :
    put τ j p q = put3 τ i.castSucc i.succ j.succ (τ i.castSucc) p q := by
  conv_lhs => rw [← put3_self (a := i.castSucc) (b := i.succ) (c := j.succ) τ]
  rw [put_j_put3 hij]

theorem succ_eq : i.succ = j.castSucc := by ext; simp; omega

theorem neq_ab : i.castSucc ≠ i.succ := (Fin.castSucc_lt_succ i).ne
theorem neq_ac : i.castSucc ≠ j.succ := by intro h; rw [Fin.ext_iff] at h; simp at h; omega
theorem neq_bc : i.succ ≠ j.succ := by intro h; rw [Fin.ext_iff] at h; simp at h; omega

theorem E_adj_up : E R i * E R j * E R i = E R i := by
  apply LinearMap.ext; intro v; funext τ
  simp only [Module.End.mul_apply, E_apply]
  rw [put_i_eq hij τ 0 1, put_i_eq hij τ 1 0]
  simp only [put_i_put3 hij, put_j_put3 hij, put3_a (neq_ab hij) (neq_ac hij),
    put3_b (neq_bc hij), put3_c, ← succ_eq hij]
  generalize τ j.succ = z
  fin_cases z <;> simp only [sgn] <;> norm_num

theorem E_adj_down : E R j * E R i * E R j = E R j := by
  apply LinearMap.ext; intro v; funext τ
  simp only [Module.End.mul_apply, E_apply]
  rw [put_j_eq hij τ 0 1, put_j_eq hij τ 1 0]
  simp only [put_i_put3 hij, put_j_put3 hij, put3_a (neq_ab hij) (neq_ac hij),
    put3_b (neq_bc hij), put3_c, ← succ_eq hij]
  generalize τ i.castSucc = z
  fin_cases z <;> simp only [sgn] <;> norm_num

end Adjacent

/-! ## Far commutation -/

section Far

variable {i j : Fin n} (hfar : i.val + 2 ≤ j.val ∨ j.val + 2 ≤ i.val)
include hfar

theorem put_jc (τ : Spin n) (a b : Fin 2) : put τ i a b j.castSucc = τ j.castSucc := by
  simp only [put, Function.update_apply]
  split_ifs <;> simp_all [Fin.ext_iff] <;> omega

theorem put_js (τ : Spin n) (a b : Fin 2) : put τ i a b j.succ = τ j.succ := by
  simp only [put, Function.update_apply]
  split_ifs <;> simp_all [Fin.ext_iff] <;> omega

theorem put_comm (τ : Spin n) (a b c d : Fin 2) :
    put (put τ i a b) j c d = put (put τ j c d) i a b := by
  funext t
  simp only [put, Function.update_apply]
  split_ifs <;> simp_all [Fin.ext_iff] <;> omega

theorem E_comm : E R i * E R j = E R j * E R i := by
  have hfar' : j.val + 2 ≤ i.val ∨ i.val + 2 ≤ j.val := hfar.symm
  apply LinearMap.ext; intro v; funext τ
  simp only [Module.End.mul_apply, E_apply, put_jc hfar, put_js hfar, put_jc hfar',
    put_js hfar', put_comm hfar]
  ring

end Far

/-! ## The representation -/

theorem adj_cases {i j : Fin n} (h : adjFin i j) : i.val + 1 = j.val ∨ j.val + 1 = i.val := h

/-- **The spin-chain representation of `TL_{n+1}(2)`**, over any commutative ring. -/
noncomputable def spinRep (R : Type*) [CommRing R] (n : ℕ) :
    TLFin R 2 n →ₐ[R] Module.End R (Spin n → R) :=
  lift R 2 adjFin (fun i => E R i) (fun i => E_sq i)
    (fun i j h => by
      rcases adj_cases h with h | h
      · exact E_adj_up h
      · exact E_adj_down h)
    (fun i j h => by
      by_cases hij : i = j
      · subst hij; rfl
      · apply E_comm
        have h1 : i.val ≠ j.val := fun h' => hij (Fin.ext h')
        have h2 : ¬ (i.val + 1 = j.val ∨ j.val + 1 = i.val) := h
        omega)

@[simp] theorem spinRep_e (i : Fin n) : spinRep R n (e R 2 adjFin i) = E R i :=
  lift_e R 2 adjFin _ _ _ _ i

end QOU.MathlibExt.TemperleyLiebSpinChainTwo
