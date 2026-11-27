import Mathlib.RingTheory.RootsOfUnity.PrimitiveRoots
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Data.ZMod.Basic
import Mathlib.Algebra.Order.Group.Unbundled.Int
import Mathlib.Tactic

/-!
# The Temperley–Lieb / Hecke quotient at a root of unity has a nondegenerate `S`-matrix

Bean `hkmt` (restated, see below), parents `rtep`, `bwsc`.

## What is proved

Fix a commutative ring `R` without zero divisors (for instance `ℤ[ζ]`), a level `k : ℕ`, put
`ℓ = k + 2`, and let `ζ ∈ Rˣ` be a primitive `2ℓ`-th root of unity. No field, no ordering, no `ℝ`,
no `ℂ`: everything is cyclotomic algebra over `R` (AGENTS.md §7c, base ring). The simple objects of
the semisimplified Temperley–Lieb category at `q = ζ` (equivalently, of the type-`A₁` quotient of the
Hecke category, Wenzl's quotient of `H_n(ζ²)` with at most two rows) are the Jones–Wenzl idempotents
`f_0, …, f_k`. Their Hopf-link (double-braiding Markov-trace) invariant is the quantum integer

    S_{ij} = [(i+1)(j+1)],      [n] = (ζⁿ − ζ⁻ⁿ)/(ζ − ζ⁻¹),

and the vacuum row is the quantum dimension `S_{0j} = [j+1]`. Here `[n]` is defined without
division, by `[0] = 0`, `[n+1] = ζⁿ + ζ⁻¹[n]` (so `[n] = ζ^{n−1} + ζ^{n−3} + ⋯ + ζ^{1−n}`), and
`(ζ − ζ⁻¹)[n] = ζⁿ − ζ⁻ⁿ` is proved (`qDelta_mul_qInt`).

* `tildeS_mul_tildeS` — the unnormalised kernel `S̃(a,b) = ζ^{ab} − ζ^{−ab}` satisfies
  `Σ_{c=1}^{ℓ−1} S̃(a,c)·S̃(c,b) = −2ℓ·δ_{ab}` for `1 ≤ a, b ≤ ℓ − 1`, **for every level `k`**.
* `sMatrix_mul_self` — the modular `S`-matrix `S_{ij} = [(i+1)(j+1)]` satisfies
  `(ζ − ζ⁻¹)²·S² = −2ℓ·1`, that is `S² = D²·1` with `D² = −2ℓ/(ζ − ζ⁻¹)²` in the fraction field.
* `globalDimSq_eq` — `(ζ − ζ⁻¹)²·Σ_{j=0}^{k} [j+1]² = −2ℓ`: the global dimension in closed form.
* `sMatrix_det_ne_zero` — `det S ≠ 0`, so `S` is invertible over the fraction field (and over `R`
  itself once `2ℓ` and `ζ − ζ⁻¹` are units, `isUnit_det_sMatrix`). Invertibility of `S` is exactly
  the nondegeneracy of the braiding: the semisimplified category is **modular** (Turaev,
  Bakalov–Kirillov Thm 3.1.17).

The proofs use only that `ζ` is a primitive `2ℓ`-th root of unity: the full character sum over
`ℤ/2ℓ` is a geometric series, and the reflection `c ↦ 2ℓ − c` (which flips the sign of `S̃`) folds it
onto the `ℓ − 1` simples.

## Honest scope

* The identification of `[(i+1)(j+1)]` with the double-braiding Markov trace of the Jones–Wenzl
  idempotents is the classical Kauffman–Lins / Kirby–Melvin computation. It is **cited** here, not
  re-derived from the corpus Hecke algebra; `qou-pbjv` / `qou-ltwg` (general-`n` `H_n(q)` as a
  braided category with Jones–Wenzl projectors) are the infrastructure that would let it be proved.
* The twist `T` and the relation `(ST)³ = p₊·S²` (a quadratic Gauss sum) are the next step.
* This file is about the root-of-unity quotient. At a generic `q` (for instance real `q > 1`) every
  `[n]` is nonzero, the category has infinitely many simples and is **not** modular
  (`HeckeRealVsRootOfUnityModularity.lean`). The restatement of `hkmt` to the quotient follows the
  2026-11-22 applicability review recorded in the bean.

Refs:
- [turaev1994] Quantum invariants of knots and 3-manifolds, ch. II.
- [bakalovkirillov2001] Lectures on tensor categories and modular functors, §3.1, §3.3.
- [kirbymelvin1991] The 3-manifold invariants of Witten and Reshetikhin–Turaev for sl(2, C).
-/

namespace QOU.HeckeTemperleyLieb.TLRootOfUnity

open Finset

variable {R : Type*} [CommRing R] [IsDomain R]

omit [IsDomain R] in
/-- `ζ^x·ζ^y = ζ^{x+y}` on values of units. -/
theorem val_zpow_mul_val_zpow (ζ : Rˣ) (x y : ℤ) :
    ((ζ ^ x : Rˣ) : R) * ((ζ ^ y : Rˣ) : R) = ((ζ ^ (x + y) : Rˣ) : R) := by
  rw [← Units.val_mul, ← zpow_add]

/-- Unnormalised `S`-kernel `S̃(a,b) = ζ^{ab} − ζ^{−ab}`, so `S̃(a,b) = (ζ − ζ⁻¹)·[ab]`. -/
def tildeS (ζ : Rˣ) (a b : ℕ) : R :=
  ((ζ ^ ((a : ℤ) * b) : Rˣ) : R) - ((ζ ^ (-((a : ℤ) * b)) : Rˣ) : R)

/-- **Character sum.** For a primitive `N`-th root of unity and any integer `m`,
`Σ_{c<N} ζ^{mc}` is `N` if `N ∣ m` and `0` otherwise. -/
theorem sum_zpow_mul {ζ : Rˣ} {N : ℕ} (hζ : IsPrimitiveRoot ζ N) (m : ℤ) :
    ∑ c ∈ range N, ((ζ ^ (m * c) : Rˣ) : R) = if (N : ℤ) ∣ m then (N : R) else 0 := by
  have hterm : ∀ c : ℕ, ((ζ ^ (m * c) : Rˣ) : R) = (((ζ ^ m : Rˣ) : R)) ^ c := by
    intro c; rw [zpow_mul, zpow_natCast, Units.val_pow_eq_pow_val]
  simp_rw [hterm]
  split_ifs with hdvd
  · have h1 : ζ ^ m = 1 := (hζ.zpow_eq_one_iff_dvd m).mpr hdvd
    simp [h1]
  · have h1 : ((ζ ^ m : Rˣ) : R) ≠ 1 := by
      rw [Ne, Units.val_eq_one]
      exact fun h => hdvd ((hζ.zpow_eq_one_iff_dvd m).mp h)
    have hN : (((ζ ^ m : Rˣ) : R)) ^ N = 1 := by
      rw [← Units.val_pow_eq_pow_val, ← zpow_natCast, ← zpow_mul, mul_comm, zpow_mul,
        zpow_natCast, hζ.pow_eq_one, one_zpow, Units.val_one]
    have hgeom := geom_sum_mul (((ζ ^ m : Rˣ) : R)) N
    rw [hN, sub_self] at hgeom
    exact (mul_eq_zero.mp hgeom).resolve_right (sub_ne_zero.mpr h1)

omit [IsDomain R] in
/-- Pointwise expansion of `S̃(a,c)·S̃(c,b)` into four characters. -/
theorem tildeS_mul_expand (ζ : Rˣ) (a b c : ℕ) :
    tildeS ζ a c * tildeS ζ c b =
      ((ζ ^ (((a : ℤ) + b) * c) : Rˣ) : R) + ((ζ ^ (-((a : ℤ) + b) * c) : Rˣ) : R)
        - ((ζ ^ (((a : ℤ) - b) * c) : Rˣ) : R) - ((ζ ^ (((b : ℤ) - a) * c) : Rˣ) : R) := by
  unfold tildeS
  simp only [sub_mul, mul_sub, val_zpow_mul_val_zpow]
  ring_nf

/-- **Full character sum** over `ℤ/N`. -/
theorem sum_tildeS_mul_full {ζ : Rˣ} {N : ℕ} (hζ : IsPrimitiveRoot ζ N) (a b : ℕ) :
    ∑ c ∈ range N, tildeS ζ a c * tildeS ζ c b =
      (if (N : ℤ) ∣ ((a : ℤ) + b) then (N : R) else 0)
        + (if (N : ℤ) ∣ (-((a : ℤ) + b)) then (N : R) else 0)
        - (if (N : ℤ) ∣ ((a : ℤ) - b) then (N : R) else 0)
        - (if (N : ℤ) ∣ ((b : ℤ) - a) then (N : R) else 0) := by
  simp_rw [tildeS_mul_expand, sum_sub_distrib, sum_add_distrib, sum_zpow_mul hζ]

omit [IsDomain R] in
/-- `S̃(a,0) = 0`. -/
@[simp] theorem tildeS_zero_right (ζ : Rˣ) (a : ℕ) : tildeS ζ a 0 = 0 := by simp [tildeS]

omit [IsDomain R] in
/-- `S̃` is symmetric. -/
theorem tildeS_comm (ζ : Rˣ) (a b : ℕ) : tildeS ζ a b = tildeS ζ b a := by
  unfold tildeS; rw [mul_comm]

omit [IsDomain R] in
/-- **Reflection** `c ↦ N − c` flips the sign of `S̃`. -/
theorem tildeS_reflect {ζ : Rˣ} {N : ℕ} (hζ : IsPrimitiveRoot ζ N) (a c : ℕ)
    (hc : c ≤ N) : tildeS ζ a (N - c) = -tildeS ζ a c := by
  have h1 : ζ ^ ((a : ℤ) * N) = 1 :=
    (hζ.zpow_eq_one_iff_dvd _).mpr (dvd_mul_left _ _)
  have h2 : ζ ^ (-((a : ℤ) * N)) = 1 := by rw [zpow_neg, h1, inv_one]
  unfold tildeS
  rw [Nat.cast_sub hc]
  have e1 : (a : ℤ) * ((N : ℤ) - c) = (a : ℤ) * N + (-((a : ℤ) * c)) := by ring
  have e2 : -((a : ℤ) * ((N : ℤ) - c)) = -((a : ℤ) * N) + (a : ℤ) * c := by ring
  rw [e2, e1, zpow_add, zpow_add, h1, h2, one_mul, one_mul]
  ring

/-- `ζ^ℓ = −1` for a primitive `2ℓ`-th root of unity. -/
theorem pow_half_eq_neg_one {ζ : Rˣ} {ℓ : ℕ} (hℓ : 0 < ℓ) (hζ : IsPrimitiveRoot ζ (2 * ℓ)) :
    ζ ^ ℓ = -1 := by
  have hζR : IsPrimitiveRoot (ζ : R) (2 * ℓ) := IsPrimitiveRoot.coe_units_iff.mpr hζ
  have hsq : (ζ : R) ^ ℓ * (ζ : R) ^ ℓ = 1 := by rw [← pow_add, ← two_mul, hζR.pow_eq_one]
  have hne : (ζ : R) ^ ℓ ≠ 1 := hζR.pow_ne_one_of_pos_of_lt (by omega) (by omega)
  apply Units.ext
  rw [Units.val_pow_eq_pow_val, Units.val_neg, Units.val_one]
  rcases mul_self_eq_one_iff.mp hsq with h | h
  · exact absurd h hne
  · exact h

/-- The kernel vanishes on the boundary weight `a = ℓ`: `S̃(ℓ, b) = 0`. -/
theorem tildeS_half_left {ζ : Rˣ} {ℓ : ℕ} (hℓ : 0 < ℓ) (hζ : IsPrimitiveRoot ζ (2 * ℓ)) (b : ℕ) :
    tildeS ζ ℓ b = 0 := by
  have hm : ζ ^ (ℓ : ℤ) = -1 := by rw [zpow_natCast]; exact pow_half_eq_neg_one hℓ hζ
  unfold tildeS
  rw [show -((ℓ : ℤ) * b) = (ℓ : ℤ) * (-(b : ℤ)) by ring, zpow_mul, zpow_mul, hm, zpow_neg,
    ← inv_zpow, inv_neg_one, sub_self]

/-- **Folding.** For a primitive `2(k+2)`-th root, the full character sum is twice the sum over the
`k + 1` simple weights `1, …, k+1`. -/
theorem sum_full_eq_two_mul_half {ζ : Rˣ} (k : ℕ) (hζ : IsPrimitiveRoot ζ (2 * (k + 2)))
    (a b : ℕ) :
    ∑ c ∈ range (2 * (k + 2)), tildeS ζ a c * tildeS ζ c b =
      2 * ∑ j ∈ range (k + 1), tildeS ζ a (j + 1) * tildeS ζ (j + 1) b := by
  set N := 2 * (k + 2) with hNdef
  set f : ℕ → R := fun c => tildeS ζ a c * tildeS ζ c b with hf
  have hrefl : ∀ c, c ≤ N → f (N - c) = f c := by
    intro c hc
    simp only [hf]
    rw [tildeS_reflect hζ a c hc, tildeS_comm ζ (N - c) b, tildeS_reflect hζ b c hc,
      tildeS_comm ζ b c]
    ring
  have hsplit : N = (k + 3) + (k + 1) := by omega
  change ∑ c ∈ range N, f c = 2 * ∑ j ∈ range (k + 1), f (j + 1)
  rw [hsplit, sum_range_add, sum_range_succ', sum_range_succ]
  have hf0 : f 0 = 0 := by simp [hf]
  have hfl : f (k + 1 + 1) = 0 := by
    simp only [hf]
    rw [show k + 1 + 1 = k + 2 by omega, tildeS_half_left (by omega) hζ b, mul_zero]
  rw [hf0, hfl, add_zero, add_zero]
  have hsecond : ∑ c ∈ range (k + 1), f (k + 3 + c) = ∑ j ∈ range (k + 1), f (j + 1) := by
    rw [← sum_range_reflect (fun j => f (j + 1)) (k + 1)]
    apply sum_congr rfl
    intro c hc
    rw [mem_range] at hc
    rw [← hrefl (k + 3 + c) (by omega)]
    congr 1
    omega
  rw [hsecond]; ring

/-- `(2(k+2) : R) ≠ 0` when `R` holds a primitive `2(k+2)`-th root of unity. -/
theorem natCast_two_ell_ne_zero {ζ : Rˣ} (k : ℕ) (hζ : IsPrimitiveRoot ζ (2 * (k + 2))) :
    (2 * ((k : R) + 2)) ≠ 0 := by
  haveI : NeZero (2 * (k + 2)) := ⟨by omega⟩
  have hNK : ((2 * (k + 2) : ℕ) : R) ≠ 0 :=
    ((IsPrimitiveRoot.coe_units_iff.mpr hζ).neZero').out
  push_cast at hNK; exact hNK

/-- **Nondegeneracy kernel, every level.** For `i, m ≤ k` and `ζ` a primitive `2(k+2)`-th root of
unity, `Σ_{j=0}^{k} S̃(i+1, j+1)·S̃(j+1, m+1) = −2(k+2)·δ_{im}`. -/
theorem tildeS_mul_tildeS {ζ : Rˣ} (k : ℕ) (hζ : IsPrimitiveRoot ζ (2 * (k + 2)))
    {i m : ℕ} (hi : i ≤ k) (hm : m ≤ k) :
    ∑ j ∈ range (k + 1), tildeS ζ (i + 1) (j + 1) * tildeS ζ (j + 1) (m + 1) =
      if i = m then -(2 * ((k : R) + 2)) else 0 := by
  have hNK := natCast_two_ell_ne_zero k hζ
  have h2 : (2 : R) ≠ 0 := by
    intro h; apply hNK; rw [h, zero_mul]
  have hfull := sum_tildeS_mul_full hζ (i + 1) (m + 1)
  rw [sum_full_eq_two_mul_half k hζ] at hfull
  have hc1 : ¬ ((2 * (k + 2) : ℕ) : ℤ) ∣ (((i + 1 : ℕ) : ℤ) + ((m + 1 : ℕ) : ℤ)) := by
    intro h
    have := Int.eq_zero_of_abs_lt_dvd h (by rw [abs_lt]; constructor <;> push_cast <;> omega)
    push_cast at this; omega
  have hc2 : ¬ ((2 * (k + 2) : ℕ) : ℤ) ∣ (-(((i + 1 : ℕ) : ℤ) + ((m + 1 : ℕ) : ℤ))) := by
    rw [Int.dvd_neg]; exact hc1
  have hc3 : ((2 * (k + 2) : ℕ) : ℤ) ∣ (((i + 1 : ℕ) : ℤ) - ((m + 1 : ℕ) : ℤ)) ↔ i = m := by
    constructor
    · intro h
      have := Int.eq_zero_of_abs_lt_dvd h (by rw [abs_lt]; constructor <;> push_cast <;> omega)
      push_cast at this; omega
    · rintro rfl; simp
  have hc4 : ((2 * (k + 2) : ℕ) : ℤ) ∣ (((m + 1 : ℕ) : ℤ) - ((i + 1 : ℕ) : ℤ)) ↔ i = m := by
    rw [← dvd_neg, neg_sub]; exact hc3
  rw [if_neg hc1, if_neg hc2] at hfull
  by_cases him : i = m
  · rw [if_pos (hc3.mpr him), if_pos (hc4.mpr him)] at hfull
    rw [if_pos him]
    have : (2 : R) * (∑ j ∈ range (k + 1), tildeS ζ (i + 1) (j + 1) * tildeS ζ (j + 1) (m + 1))
        = 2 * (-(2 * ((k : R) + 2))) := by rw [hfull]; push_cast; ring
    exact mul_left_cancel₀ h2 this
  · rw [if_neg (fun h => him (hc3.mp h)), if_neg (fun h => him (hc4.mp h))] at hfull
    rw [if_neg him]
    have : (2 : R) * (∑ j ∈ range (k + 1), tildeS ζ (i + 1) (j + 1) * tildeS ζ (j + 1) (m + 1))
        = 2 * 0 := by rw [hfull]; ring
    exact mul_left_cancel₀ h2 this

/-! ### Normalised modular data (no division) -/

/-- `ζ − ζ⁻¹`, the denominator of the quantum integers. -/
def qDelta (ζ : Rˣ) : R := (ζ : R) - ((ζ⁻¹ : Rˣ) : R)

omit [IsDomain R] in
/-- `ζ − ζ⁻¹ ≠ 0` for a primitive `2(k+2)`-th root (order `≥ 4 > 2`). -/
theorem qDelta_ne_zero {ζ : Rˣ} (k : ℕ) (hζ : IsPrimitiveRoot ζ (2 * (k + 2))) : qDelta ζ ≠ 0 := by
  intro h
  have h2 : ζ ^ 2 = 1 := by
    have : ζ = ζ⁻¹ := Units.ext (sub_eq_zero.mp h)
    rw [sq]; nth_rewrite 2 [this]; exact mul_inv_cancel ζ
  exact hζ.pow_ne_one_of_pos_of_lt (by norm_num) (by omega) h2

/-- The balanced quantum integer, division-free: `[0] = 0`, `[n+1] = ζⁿ + ζ⁻¹·[n]`, so
`[n] = ζ^{n−1} + ζ^{n−3} + ⋯ + ζ^{1−n}`. -/
def qInt (ζ : Rˣ) : ℕ → R
  | 0 => 0
  | n + 1 => ((ζ ^ (n : ℤ) : Rˣ) : R) + ((ζ⁻¹ : Rˣ) : R) * qInt ζ n

omit [IsDomain R] in
/-- `(ζ − ζ⁻¹)·[n] = ζⁿ − ζ⁻ⁿ`. -/
theorem qDelta_mul_qInt (ζ : Rˣ) (n : ℕ) :
    qDelta ζ * qInt ζ n = ((ζ ^ (n : ℤ) : Rˣ) : R) - ((ζ ^ (-(n : ℤ)) : Rˣ) : R) := by
  induction n with
  | zero => simp [qInt]
  | succ n ih =>
    simp only [qInt]
    have hz : (ζ : R) = ((ζ ^ (1 : ℤ) : Rˣ) : R) := by rw [zpow_one]
    have hzi : ((ζ⁻¹ : Rˣ) : R) = ((ζ ^ (-1 : ℤ) : Rˣ) : R) := by rw [zpow_neg_one]
    rw [mul_add, mul_left_comm, ih]
    unfold qDelta
    rw [hz, hzi]
    simp only [sub_mul, mul_sub, val_zpow_mul_val_zpow]
    push_cast
    ring_nf

omit [IsDomain R] in
theorem tildeS_eq_qDelta_mul_qInt (ζ : Rˣ) (a b : ℕ) :
    tildeS ζ a b = qDelta ζ * qInt ζ (a * b) := by
  rw [qDelta_mul_qInt]; unfold tildeS; push_cast; rfl

/-- The **modular `S`-matrix** of the level-`k` quotient, `S_{ij} = [(i+1)(j+1)]`, on the simples
`f_0, …, f_k` (Hopf-link normalisation, `S_{00} = 1`). -/
def sMatrix (ζ : Rˣ) (k : ℕ) : Matrix (Fin (k + 1)) (Fin (k + 1)) R :=
  fun i j => qInt ζ ((i.val + 1) * (j.val + 1))

/-- **`S² = D²·1`, cleared of denominators:** `(ζ − ζ⁻¹)²·S² = −2(k+2)·1`. Charge conjugation is
trivial for type `A₁`, so this is the full `S² = D²·C` relation. -/
theorem sMatrix_mul_self {ζ : Rˣ} (k : ℕ) (hζ : IsPrimitiveRoot ζ (2 * (k + 2))) :
    qDelta ζ ^ 2 • (sMatrix ζ k * sMatrix ζ k) =
      (-(2 * ((k : R) + 2))) • (1 : Matrix (Fin (k + 1)) (Fin (k + 1)) R) := by
  ext i m
  simp only [Matrix.smul_apply, Matrix.mul_apply, Matrix.one_apply, smul_eq_mul, sMatrix,
    mul_sum]
  have key := tildeS_mul_tildeS k hζ (Nat.lt_succ_iff.mp i.isLt) (Nat.lt_succ_iff.mp m.isLt)
  rw [Fin.sum_univ_eq_sum_range (fun j => qDelta ζ ^ 2 * (qInt ζ ((i.val + 1) * (j + 1)) *
      qInt ζ ((j + 1) * (m.val + 1)))) (k + 1)]
  have hsum : ∑ j ∈ range (k + 1), qDelta ζ ^ 2 * (qInt ζ ((i.val + 1) * (j + 1)) *
      qInt ζ ((j + 1) * (m.val + 1))) =
      ∑ j ∈ range (k + 1), tildeS ζ (i.val + 1) (j + 1) * tildeS ζ (j + 1) (m.val + 1) := by
    apply sum_congr rfl; intro j _
    rw [tildeS_eq_qDelta_mul_qInt, tildeS_eq_qDelta_mul_qInt]; ring
  rw [hsum, key]
  by_cases h : i = m
  · subst h; simp
  · have hv : i.val ≠ m.val := fun hv => h (Fin.ext hv)
    simp [h, hv]

/-- **Global dimension in closed form:** `(ζ − ζ⁻¹)²·Σ_{j=0}^{k} [j+1]² = −2(k+2)`. This is the
`(0,0)` entry of `S² = D²·1`, since `S_{0j} = [j+1]` is the quantum dimension of `f_j`. -/
theorem globalDimSq_eq {ζ : Rˣ} (k : ℕ) (hζ : IsPrimitiveRoot ζ (2 * (k + 2))) :
    qDelta ζ ^ 2 * ∑ j ∈ range (k + 1), qInt ζ (j + 1) ^ 2 = -(2 * ((k : R) + 2)) := by
  have h := congrFun (congrFun (sMatrix_mul_self k hζ) 0) 0
  simp only [Matrix.smul_apply, Matrix.mul_apply, Matrix.one_apply_eq, smul_eq_mul, mul_one,
    sMatrix, Fin.val_zero, zero_add, one_mul] at h
  rw [← h, Fin.sum_univ_eq_sum_range (fun j => qInt ζ (j + 1) * qInt ζ (j + 1))]
  congr 1; apply sum_congr rfl; intro j _; ring

/-- **Modularity (nondegeneracy).** `det S ≠ 0` for every level `k`, over every domain holding a
primitive `2(k+2)`-th root of unity; so `S` is invertible over the fraction field. -/
theorem sMatrix_det_ne_zero {ζ : Rˣ} (k : ℕ) (hζ : IsPrimitiveRoot ζ (2 * (k + 2))) :
    (sMatrix ζ k).det ≠ 0 := by
  intro hdet
  have h := congrArg Matrix.det (sMatrix_mul_self k hζ)
  rw [Matrix.det_smul, Matrix.det_smul, Matrix.det_mul, hdet, Matrix.det_one, mul_zero,
    mul_zero, mul_one, Fintype.card_fin] at h
  exact pow_ne_zero _ (neg_ne_zero.mpr (natCast_two_ell_ne_zero k hζ)) h.symm

/-- Over `R` itself, `S` is invertible as soon as `2(k+2)` and `ζ − ζ⁻¹` are units (for instance
over `ℤ[ζ, 1/2ℓ]`, or any field). -/
theorem isUnit_det_sMatrix {ζ : Rˣ} (k : ℕ) (hζ : IsPrimitiveRoot ζ (2 * (k + 2)))
    (hℓ : IsUnit (2 * ((k : R) + 2))) (hδ : IsUnit (qDelta ζ)) :
    IsUnit (sMatrix ζ k).det := by
  obtain ⟨u, hu⟩ := hℓ
  obtain ⟨d, hd⟩ := hδ
  have h := sMatrix_mul_self k hζ
  rw [← hd, ← hu] at h
  apply Matrix.isUnit_det_of_right_inverse
    (B := (-(((u⁻¹ : Rˣ) : R) * (d : R) ^ 2)) • sMatrix ζ k)
  rw [Matrix.mul_smul, show (-(((u⁻¹ : Rˣ) : R) * (d : R) ^ 2)) =
      (-((u⁻¹ : Rˣ) : R)) * (d : R) ^ 2 by ring, ← smul_smul, h, smul_smul,
    show -((u⁻¹ : Rˣ) : R) * -(u : R) = ((u⁻¹ * u : Rˣ) : R) by push_cast; ring,
    inv_mul_cancel, Units.val_one, one_smul]

/-- `2` is a primitive `4`-th root of unity in `𝔽₅` (`2² = −1`). -/
theorem two_isPrimitiveRoot_four_zmod5 : IsPrimitiveRoot (2 : ZMod 5) 4 := by
  refine IsPrimitiveRoot.mk_of_lt (2 : ZMod 5) (by norm_num) (by decide) ?_
  intro l h0 hl
  interval_cases l <;> decide

instance fact_prime_five : Fact (Nat.Prime 5) := ⟨by norm_num⟩

/-- The unit `2 ∈ 𝔽₅ˣ`. -/
def two5 : (ZMod 5)ˣ := ⟨2, 3, by decide, by decide⟩

/-- **Non-vacuity.** The hypotheses are satisfiable: at level `k = 0` over `𝔽₅` with `ζ = 2`, the
theorem applies, so nothing above is conditional on `False`. -/
example : (sMatrix two5 0).det ≠ 0 :=
  sMatrix_det_ne_zero 0 (IsPrimitiveRoot.coe_units_iff.mp (by
    simpa [two5] using two_isPrimitiveRoot_four_zmod5))

end QOU.HeckeTemperleyLieb.TLRootOfUnity
