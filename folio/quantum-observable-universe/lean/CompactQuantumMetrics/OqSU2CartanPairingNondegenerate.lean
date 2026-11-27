import CompactQuantumMetrics.OqSU2BudgetLittleQJacobi
import Mathlib.Algebra.Polynomial.Roots

/-!
# The Haar pairing on the Cartan block is nondegenerate

Thread "Audit the q-Bessel special-function dictionary" (2026-11-27); bean `qou-q3dc`
(q-NS Part A). `OqSU2BudgetLittleQJacobi` shows that on the Cartan block `K[ζ]`, `ζ = βγ`,
the Haar state `h` makes `L = X₊X₋` symmetric, so eigenpolynomials with different eigenvalues
are orthogonal. This file proves the missing half: the pairing `(P, Q) ↦ h(P(ζ) Q(ζ))` is
**nondegenerate**. So orthogonality is an honest orthogonality, and `ζ` satisfies no
polynomial relation in `O_q(SU(2))`.

## Results (over a field `K`, `q : Kˣ`, with `p = q²` not a root of unity)

* `qHilbert_nondegenerate`: the `q`-Hilbert moment form is nondegenerate. If
  `p ≠ 0`, `p^{m+1} ≠ 1` for all `m`, and `Σ_{j ≤ n} c_j / (1 − p^{i+j+1}) = 0` for every
  `i ≤ n`, then every `c_j = 0`. The proof is a Lagrange argument and needs no determinant.
  The numerator polynomial `N(x) = Σ_j c_j Π_{k ≠ j} (1 − p^{k+1} x)` has degree `≤ n` and
  vanishes at the `n + 1` distinct points `p^0, …, p^n`, so `N = 0`. Evaluating `N` at
  `p^{-(j+1)}` isolates `c_j` times a nonzero product.
* `haarState_ev_mul_zetaB_pow`: `h(P(ζ) ζ^i) = Σ_j P_j h(ζ^{i+j})`.
* `haarMoment_eq`: `h(ζ^m) = (−q)^m (1 − p) / (1 − p^{m+1})`.
* `cartan_pairing_nondegenerate`: if `h(P(ζ) ζ^i) = 0` for all `i`, then `P = 0`.
* `ev_injective`: `P ↦ P(ζ)` is injective. `ζ` is transcendental over `K` inside
  `O_q(SU(2))`.
* `qSqNum_ne_zero_of_not_root`: the hypothesis `[n+1]_{q²} ≠ 0` used upstream follows.

## What this gives

With `haarState_eigen_orthogonal`, the eigenpolynomials of `L` (the little `q`-Jacobi
polynomials `p_n(ζ; 1, 1; q²)`) are orthogonal for a **nondegenerate** form. The norms
`h(p_n²)` are therefore nonzero as soon as the `p_n` span `K[ζ]`. That spanning is in
`OqSU2LittleQJacobiBasis`.

## Not established

* Positivity `h(p_n²) > 0` (an ordered-field statement; #9646 covers `h(a* a) ≥ 0`).
* The case `q² = 1` (classical limit). There the moments are `(−1)^m/(m+1)`, the Hilbert matrix,
  and the same argument works with `1/(x + k + 1)` in place of `1/(1 − p^{k+1} x)`. It is
  not done here.

Everything is algebraic. No empirical value enters any proof. Sorry-free.
-/

namespace QOU.AlgebraicSubstrate.OqSU2

open Polynomial Finset

section QHilbert

variable {K : Type*} [Field K]

/-- The Lagrange numerator `N(x) = Σ_{j ≤ n} c_j Π_{k ≤ n, k ≠ j} (1 − p^{k+1} x)`. -/
noncomputable def lagNum (p : K) (n : ℕ) (c : ℕ → K) : K[X] :=
  ∑ j ∈ range (n + 1), C (c j) * ∏ k ∈ (range (n + 1)).erase j, (1 - C (p ^ (k + 1)) * X)

theorem natDegree_lagNum_le (p : K) (n : ℕ) (c : ℕ → K) : (lagNum p n c).natDegree ≤ n := by
  unfold lagNum
  apply natDegree_sum_le_of_forall_le
  intro j hj
  refine (natDegree_C_mul_le _ _).trans ?_
  refine (natDegree_prod_le _ _).trans ?_
  have h1 : ∀ k ∈ (range (n + 1)).erase j, (1 - C (p ^ (k + 1)) * X : K[X]).natDegree ≤ 1 := by
    intro k _
    refine (natDegree_sub_le _ _).trans ?_
    simp only [natDegree_one, zero_le, max_eq_right]
    exact (natDegree_C_mul_le _ _).trans natDegree_X_le
  refine (sum_le_sum h1).trans ?_
  simp [card_erase_of_mem hj]

theorem eval_lagNum (p : K) (n : ℕ) (c : ℕ → K) (x : K) :
    (lagNum p n c).eval x =
      ∑ j ∈ range (n + 1), c j * ∏ k ∈ (range (n + 1)).erase j, (1 - p ^ (k + 1) * x) := by
  simp [lagNum, eval_finset_sum, eval_prod]

/-- Powers of `p` are injective when `p ≠ 0` and no positive power is `1`. -/
theorem pow_injective_of_not_root {p : K} (hp0 : p ≠ 0) (hp : ∀ m : ℕ, p ^ (m + 1) ≠ 1) :
    Function.Injective (fun a : ℕ => p ^ a) := by
  intro a b hab
  simp only at hab
  by_contra hne
  rcases Nat.lt_or_gt_of_ne hne with h | h
  · obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_lt h
    have : p ^ (d + 1) = 1 := by
      have h' : p ^ a * p ^ (d + 1) = p ^ a * 1 := by rw [← pow_add, mul_one, ← add_assoc]; exact hab.symm
      exact mul_left_cancel₀ (pow_ne_zero _ hp0) h'
    exact hp d this
  · obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_lt h
    have : p ^ (d + 1) = 1 := by
      have h' : p ^ b * p ^ (d + 1) = p ^ b * 1 := by rw [← pow_add, mul_one, ← add_assoc]; exact hab
      exact mul_left_cancel₀ (pow_ne_zero _ hp0) h'
    exact hp d this

/-- **The `q`-Hilbert form is nondegenerate.** -/
theorem qHilbert_nondegenerate {p : K} (hp0 : p ≠ 0) (hp : ∀ m : ℕ, p ^ (m + 1) ≠ 1)
    (n : ℕ) (c : ℕ → K)
    (h : ∀ i ≤ n, ∑ j ∈ range (n + 1), c j / (1 - p ^ (i + j + 1)) = 0) :
    ∀ j ≤ n, c j = 0 := by
  classical
  have hne : ∀ m : ℕ, (1 : K) - p ^ (m + 1) ≠ 0 := fun m h0 => hp m (sub_eq_zero.mp h0).symm
  have hinj := pow_injective_of_not_root hp0 hp
  -- Step 1: the numerator vanishes.
  have hN : lagNum p n c = 0 := by
    refine eq_zero_of_natDegree_lt_card_of_eval_eq_zero (lagNum p n c)
      (f := fun i : Fin (n + 1) => p ^ (i : ℕ)) ?_ ?_ ?_
    · intro a b hab
      exact Fin.ext (hinj hab)
    · intro i
      have hi : (i : ℕ) ≤ n := Nat.lt_succ_iff.mp i.isLt
      rw [eval_lagNum]
      have hfac : ∀ k : ℕ, (1 : K) - p ^ (k + 1) * p ^ (i : ℕ) = 1 - p ^ ((i : ℕ) + k + 1) := by
        intro k; rw [← pow_add]; congr 2; omega
      simp_rw [hfac]
      have hterm : ∀ j ∈ range (n + 1),
          c j * ∏ k ∈ (range (n + 1)).erase j, (1 - p ^ ((i : ℕ) + k + 1)) =
            (∏ k ∈ range (n + 1), (1 - p ^ ((i : ℕ) + k + 1))) *
              (c j / (1 - p ^ ((i : ℕ) + j + 1))) := by
        intro j hj
        rw [← mul_prod_erase (range (n + 1)) (fun k => (1 : K) - p ^ ((i : ℕ) + k + 1)) hj]
        have : (1 : K) - p ^ ((i : ℕ) + j + 1) ≠ 0 := hne _
        field_simp
      rw [sum_congr rfl hterm, ← mul_sum, h i hi, mul_zero]
    · simp only [Fintype.card_fin]
      exact Nat.lt_succ_of_le (natDegree_lagNum_le p n c)
  -- Step 2: evaluate at `p^{-(j+1)}`.
  intro j hj
  have hjm : j ∈ range (n + 1) := mem_range.mpr (Nat.lt_succ_of_le hj)
  have hev := congrArg (eval (p ^ (j + 1))⁻¹) hN
  rw [eval_lagNum, eval_zero] at hev
  have hpj : p ^ (j + 1) ≠ 0 := pow_ne_zero _ hp0
  rw [sum_eq_single j] at hev
  · have hprod : ∏ k ∈ (range (n + 1)).erase j, (1 - p ^ (k + 1) * (p ^ (j + 1))⁻¹) ≠ 0 := by
      rw [prod_ne_zero_iff]
      intro k hk
      have hkj : k ≠ j := ne_of_mem_erase hk
      intro h0
      have : p ^ (k + 1) = p ^ (j + 1) := by
        have := sub_eq_zero.mp h0
        field_simp at this
        exact this.symm
      exact hkj (by have := hinj this; omega)
    exact (mul_eq_zero.mp hev).resolve_right hprod
  · intro b _ hbj
    have hjb : j ∈ (range (n + 1)).erase b := mem_erase.mpr ⟨fun h => hbj h.symm, hjm⟩
    rw [prod_eq_zero hjb (by rw [mul_inv_cancel₀ hpj, sub_self]), mul_zero]
  · intro h; exact absurd hjm h

end QHilbert

section Haar

variable {K : Type*} [Field K] (q : Kˣ)

theorem jk_mul_sub_one {S : Type*} [CommRing S] (x : S) (n : ℕ) :
    jk x n * (x - 1) = x ^ n - 1 := by
  induction n with
  | zero => simp [jk]
  | succ n ih => rw [jk_succ, add_mul, ih]; ring

/-- `[n+1]_{q²} ≠ 0` follows from `q²` not being a root of unity. -/
theorem qSqNum_ne_zero_of_not_root (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1) (n : ℕ) :
    qSqNum q n ≠ 0 := by
  intro h0
  have := jk_mul_sub_one ((q : K) * q) (n + 1)
  rw [← qSqNum_eq_jk, h0, zero_mul] at this
  exact hp n (sub_eq_zero.mp this.symm)

/-- `h(ζ^m) = (−q)^m (1 − p)/(1 − p^{m+1})`, `p = q²`. -/
theorem haarMoment_eq (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1) (m : ℕ) :
    haarMoment q m = (-(q : K)) ^ m * (1 - (q : K) * q) / (1 - ((q : K) * q) ^ (m + 1)) := by
  have hm := jk_mul_sub_one ((q : K) * q) (m + 1)
  rw [← qSqNum_eq_jk] at hm
  have h1 : qSqNum q m ≠ 0 := qSqNum_ne_zero_of_not_root q hp m
  have h2 : (1 : K) - ((q : K) * q) ^ (m + 1) ≠ 0 := fun h0 => hp m (sub_eq_zero.mp h0).symm
  rw [haarMoment, div_eq_div_iff h1 h2]
  linear_combination (-(q : K)) ^ m * hm

/-- `h(P(ζ) ζ^i) = Σ_j P_j h(ζ^{j+i})`. -/
theorem haarState_ev_mul_zetaB_pow (P : K[X]) (i : ℕ) :
    haarState q (ev q P * zetaB q ^ i) =
      ∑ j ∈ range (P.natDegree + 1), P.coeff j * haarMoment q (j + i) := by
  rw [ev, aeval_eq_sum_range, sum_mul, map_sum]
  refine sum_congr rfl fun j _ => ?_
  rw [smul_mul_assoc, ← pow_add, map_smul, haarState_zetaB_pow, smul_eq_mul]

/-- **The Haar pairing on the Cartan block is nondegenerate.** -/
theorem cartan_pairing_nondegenerate (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1)
    (P : K[X]) (h : ∀ i : ℕ, haarState q (ev q P * zetaB q ^ i) = 0) : P = 0 := by
  set n := P.natDegree
  set p : K := (q : K) * q
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  have hp0 : p ≠ 0 := mul_ne_zero hq0 hq0
  have hp1 : (1 : K) - p ≠ 0 := fun h0 => hp 0 (by rw [zero_add, pow_one]; exact (sub_eq_zero.mp h0).symm)
  have key := qHilbert_nondegenerate hp0 hp n (fun j => P.coeff j * (-(q : K)) ^ j) ?_
  · ext j
    rw [coeff_zero]
    by_cases hj : j ≤ n
    · have := key j hj
      rcases mul_eq_zero.mp this with h0 | h0
      · exact h0
      · exact absurd h0 (pow_ne_zero _ (neg_ne_zero.mpr hq0))
    · exact coeff_eq_zero_of_natDegree_lt (by omega)
  · intro i _
    have hi := h i
    rw [haarState_ev_mul_zetaB_pow] at hi
    have hrw : ∀ j ∈ range (n + 1), P.coeff j * haarMoment q (j + i) =
        ((-(q : K)) ^ i * (1 - p)) * (P.coeff j * (-(q : K)) ^ j / (1 - p ^ (i + j + 1))) := by
      intro j _
      rw [haarMoment_eq q hp, show j + i + 1 = i + j + 1 by omega, pow_add]
      ring
    rw [sum_congr rfl hrw, ← mul_sum] at hi
    exact (mul_eq_zero.mp hi).resolve_left
      (mul_ne_zero (pow_ne_zero _ (neg_ne_zero.mpr hq0)) hp1)

/-- `P ↦ P(ζ)` is injective: `ζ = βγ` satisfies no polynomial relation. -/
theorem ev_injective (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1) :
    Function.Injective (ev q) := by
  rw [injective_iff_map_eq_zero]
  intro P hP
  exact cartan_pairing_nondegenerate q hp P (fun i => by rw [hP, zero_mul, map_zero])

/-- The pairing in symmetric form: `h(P(ζ) Q(ζ)) = 0` for every `Q` forces `P = 0`. -/
theorem cartan_pairing_nondegenerate' (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1)
    (P : K[X]) (h : ∀ Q : K[X], haarState q (ev q P * ev q Q) = 0) : P = 0 :=
  cartan_pairing_nondegenerate q hp P fun i => by
    simpa [ev, map_pow] using h (X ^ i)

end Haar

end QOU.AlgebraicSubstrate.OqSU2
