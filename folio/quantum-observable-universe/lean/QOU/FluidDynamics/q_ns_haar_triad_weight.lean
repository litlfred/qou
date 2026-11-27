import QOU.FluidDynamics.q_ns_haar_budget_full

/-!
# QOU.FluidDynamics.q_ns_haar_triad_weight — triad transfer block by block in the PBW basis

Bean `qou-q3dc` (progress on `qou-pa7n`, Part A of `conj:regularity-breakdown`, which stays
open). Owner route: use the PBW basis downstream (2026-11-27).

`q_ns_triad_noncomm.lean` recorded a precise gap: the transports of `O_q(SU(2))` are
**twisted** derivations, `X(fg) = X f · T g + f · X g`, and its energy argument needed the
untwisted rule. This file computes, for the three twisted fields `X₊, X₋, X₀`, the pairwise
coupling between torus weight blocks

  `D_X(x, y) = h(x · X y)`,

the transfer from block `y` into block `x` along `X`, on the whole algebra and with no
untwisting.

## Results

A **weight vector** of weight `(a, m) ∈ ℤ²` is an element with `θ_{u,v} y = u^a v^m y` for every
torus automorphism (`IsWeight`). Every PBW monomial `(a, b, c)` is one, of weight `(a, b − c)`
(`isWeight_pbwMono`), and weights add under products (`IsWeight.mul`). The fields shift weight
by `(1, −1)`, `(−1, 1)` and `(0, 0)` (`IsWeight.fieldPlus`, `.fieldMinus`, `.fieldZero`).

* **Selection rule.** For `q` not a root of unity the Haar state vanishes off weight `(0, 0)`
  (`haarState_eq_zero_of_isWeight`). Hence `D_{X₊}(x, y) = 0` unless `w_x + w_y + (1, −1) = 0`,
  and likewise for `X₋, X₀` (`coupling_plus_eq_zero` …). The same holds for three-mode triads
  `h(e_n · e_p · X e_r)` (`triad_plus_eq_zero` …).
* **Twisted skew symmetry.** For weight vectors `x : (a, m)`, `y : (b, n)`,
  `D_{X₊}(x, y) = −q^{n−b−2a−2} D_{X₊}(y, x)`, and similarly for `X₋` (exponent `n−b−2a+2`) and
  `X₀` (exponent `n−b−2a`) (`coupling_plus_twisted_skew` …). The proof is integration by parts
  (`haarState_ibp_*`) plus the modular property `h(xy) = h(y σx)`.
* **On the selection support the twist is uniform.** Wherever the coupling can be nonzero, all
  three fields give the same factor:
  `D_X(x, y) = −q^{−(a+m)} D_X(y, x)` (`coupling_*_skew_on_support`).
  So the block transfer is exactly skew (Kraichnan detailed conservation) iff `a + m = 0` for the
  receiving block; on a PBW monomial `(a, b, c)` that is `a + b − c = 0`. Off that diagonal the
  transfer is skew only up to the factor `q^{−(a+m)}`, which equals `1` at `q = 1`.

## What is not established

* That `X₊, X₋, X₀` (or `L = X₊ ∘ X₋`) are the q-NS transport `∇_q` and viscous term; the corpus
  has no `∇_q` on `O_q(SU(2))`.
* That any particular coupling is nonzero; only the vanishing pattern and the twist are proved.
* Any rate, cascade bound, or Part A of `conj:regularity-breakdown`.
* No numerical coupling is computed and no empirical value enters any proof. `q` is generic,
  subject only to not being a root of unity.

## References

- [woronowicz1987] S. L. Woronowicz, *Twisted SU(2) group. An example of a non-commutative
  differential calculus*, Publ. RIMS 23 (1987) 117–181 (Haar state, modular property).
- [leitner2026] fluid-dynamics/q-navier-stokes.md (`def:q-navier-stokes`).
-/

namespace QOU.FluidDynamics.HaarTriadWeight

open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2
open QOU.FluidDynamics.HaarFieldInvarianceFull QOU.FluidDynamics.HaarBudgetFull

variable {K : Type*} [Field K] (q : Kˣ)

/-- `y` has torus weight `(a, m)`: `θ_{u,v} y = u^a v^m y`. -/
def IsWeight (y : OqSU2 K q) (a m : ℤ) : Prop :=
  ∀ u v : Kˣ, torusScaleAlgHom q u v y = ((u ^ a * v ^ m : Kˣ) : K) • y

variable {q}

theorem isWeight_pbwMono (i : MonoIdx) :
    IsWeight q (pbwMono q i) i.1 ((i.2.1 : ℤ) - i.2.2) :=
  fun u v => torus_pbwMono q u v i

theorem IsWeight.mul {x y : OqSU2 K q} {a m b n : ℤ} (hx : IsWeight q x a m)
    (hy : IsWeight q y b n) : IsWeight q (x * y) (a + b) (m + n) := by
  intro u v
  rw [map_mul, hx, hy, smul_mul_smul_comm, ← Units.val_mul, zpow_add, zpow_add,
    mul_mul_mul_comm]

theorem IsWeight.fieldPlus {y : OqSU2 K q} {a m : ℤ} (hy : IsWeight q y a m) :
    IsWeight q (fieldPlus q y) (a + 1) (m - 1) := by
  intro u v
  rw [torus_fieldPlus, hy, map_smul, smul_smul, ← Units.val_mul, ← Units.val_mul, zpow_add_one,
    zpow_sub_one]
  congr 1
  ac_rfl

theorem IsWeight.fieldMinus {y : OqSU2 K q} {a m : ℤ} (hy : IsWeight q y a m) :
    IsWeight q (fieldMinus q y) (a - 1) (m + 1) := by
  intro u v
  rw [torus_fieldMinus, hy, map_smul, smul_smul, ← Units.val_mul, ← Units.val_mul, zpow_add_one,
    zpow_sub_one]
  congr 1
  ac_rfl

theorem IsWeight.fieldZero {y : OqSU2 K q} {a m : ℤ} (hy : IsWeight q y a m) :
    IsWeight q (fieldZero q y) a m := by
  intro u v
  rw [torus_fieldZero, hy, map_smul]

variable (hq : ∀ n : ℕ, 0 < n → (q : K) ^ n ≠ 1)
include hq

theorem zpow_ne_one (a : ℤ) (ha : a ≠ 0) : ((q ^ a : Kˣ) : K) ≠ 1 := by
  obtain ⟨n, rfl | rfl⟩ := Int.eq_nat_or_neg a
  · have hn : 0 < n := by omega
    rw [zpow_natCast, Units.val_pow_eq_pow_val]
    exact hq n hn
  · have hn : 0 < n := by omega
    rw [zpow_neg, zpow_natCast, Units.val_inv_eq_inv_val, Units.val_pow_eq_pow_val]
    intro h
    exact hq n hn (inv_eq_one.1 h)

/-- **The Haar state vanishes off weight `(0, 0)`.** -/
theorem haarState_eq_zero_of_isWeight {y : OqSU2 K q} {a m : ℤ} (hy : IsWeight q y a m)
    (hne : a ≠ 0 ∨ m ≠ 0) : haarState q y = 0 := by
  rcases hne with ha | hm
  · refine haarState_eq_zero_of_torus q q 1 _ ?_ y (hy q 1)
    rw [one_zpow, mul_one]
    exact zpow_ne_one hq a ha
  · refine haarState_eq_zero_of_torus q 1 q _ ?_ y (hy 1 q)
    rw [one_zpow, one_mul]
    exact zpow_ne_one hq m hm

/-! ## Selection rules -/

theorem coupling_plus_eq_zero {x y : OqSU2 K q} {a m b n : ℤ} (hx : IsWeight q x a m)
    (hy : IsWeight q y b n) (hne : a + b + 1 ≠ 0 ∨ m + n - 1 ≠ 0) :
    haarState q (x * fieldPlus q y) = 0 :=
  haarState_eq_zero_of_isWeight hq (hx.mul hy.fieldPlus) (by omega)

theorem coupling_minus_eq_zero {x y : OqSU2 K q} {a m b n : ℤ} (hx : IsWeight q x a m)
    (hy : IsWeight q y b n) (hne : a + b - 1 ≠ 0 ∨ m + n + 1 ≠ 0) :
    haarState q (x * fieldMinus q y) = 0 :=
  haarState_eq_zero_of_isWeight hq (hx.mul hy.fieldMinus) (by omega)

theorem coupling_zero_eq_zero {x y : OqSU2 K q} {a m b n : ℤ} (hx : IsWeight q x a m)
    (hy : IsWeight q y b n) (hne : a + b ≠ 0 ∨ m + n ≠ 0) :
    haarState q (x * fieldZero q y) = 0 :=
  haarState_eq_zero_of_isWeight hq (hx.mul hy.fieldZero) (by omega)

/-- Three-mode triads `h(e · e' · X₊ e'')` obey the weight selection rule. -/
theorem triad_plus_eq_zero {x y z : OqSU2 K q} {a m b n c k : ℤ} (hx : IsWeight q x a m)
    (hy : IsWeight q y b n) (hz : IsWeight q z c k)
    (hne : a + b + c + 1 ≠ 0 ∨ m + n + k - 1 ≠ 0) :
    haarState q (x * y * fieldPlus q z) = 0 :=
  haarState_eq_zero_of_isWeight hq ((hx.mul hy).mul hz.fieldPlus) (by omega)

theorem triad_minus_eq_zero {x y z : OqSU2 K q} {a m b n c k : ℤ} (hx : IsWeight q x a m)
    (hy : IsWeight q y b n) (hz : IsWeight q z c k)
    (hne : a + b + c - 1 ≠ 0 ∨ m + n + k + 1 ≠ 0) :
    haarState q (x * y * fieldMinus q z) = 0 :=
  haarState_eq_zero_of_isWeight hq ((hx.mul hy).mul hz.fieldMinus) (by omega)

theorem triad_zero_eq_zero {x y z : OqSU2 K q} {a m b n c k : ℤ} (hx : IsWeight q x a m)
    (hy : IsWeight q y b n) (hz : IsWeight q z c k)
    (hne : a + b + c ≠ 0 ∨ m + n + k ≠ 0) :
    haarState q (x * y * fieldZero q z) = 0 :=
  haarState_eq_zero_of_isWeight hq ((hx.mul hy).mul hz.fieldZero) (by omega)

/-! ## Twisted skew symmetry -/

omit hq in
theorem T_unit_eq (b n s t : ℤ) :
    ((q⁻¹ ^ b * q⁻¹⁻¹ ^ n : Kˣ) : K) * ((((q⁻¹ ^ 2) ^ s * (1 : Kˣ) ^ t : Kˣ)) : K) =
      ((q ^ (n - b - 2 * s) : Kˣ) : K) := by
  rw [← Units.val_mul]
  congr 1
  have h2 : (q⁻¹ ^ 2 : Kˣ) = q ^ (-2 : ℤ) := by
    rw [zpow_neg, inv_pow]; rfl
  rw [h2, inv_inv, one_zpow, mul_one, ← zpow_mul, inv_zpow', ← zpow_add, ← zpow_add]
  congr 1
  ring

/-- **Twisted skew symmetry for `X₊`.** For weight vectors `x : (a, m)` and `y : (b, n)`. -/
theorem coupling_plus_twisted_skew {x y : OqSU2 K q} {a m b n : ℤ} (hx : IsWeight q x a m)
    (hy : IsWeight q y b n) :
    haarState q (x * fieldPlus q y) =
      -((q ^ (n - b - 2 * (a + 1)) : Kˣ) : K) * haarState q (y * fieldPlus q x) := by
  have h1 := haarState_ibp_plus q hq x y
  rw [hy, mul_smul_comm, map_smul, smul_eq_mul] at h1
  have h2 := haarState_modular q (qSqNum_ne_zero_of_not_root q hq) (fieldPlus q x) y
  have h3 : modularAut q (fieldPlus q x) =
      (((q⁻¹ ^ 2) ^ (a + 1) * (1 : Kˣ) ^ (m - 1) : Kˣ) : K) • fieldPlus q x :=
    hx.fieldPlus (q⁻¹ ^ 2) 1
  rw [h3, mul_smul_comm, map_smul, smul_eq_mul] at h2
  rw [← T_unit_eq b n (a + 1) (m - 1)]
  linear_combination h1 - ((q⁻¹ ^ b * q⁻¹⁻¹ ^ n : Kˣ) : K) * h2

/-- On the support of the selection rule the `X₊` twist is `q^(−(a+m))`. -/
theorem coupling_plus_skew_on_support {x y : OqSU2 K q} {a m b n : ℤ} (hx : IsWeight q x a m)
    (hy : IsWeight q y b n) (hb : a + b + 1 = 0) (hn : m + n - 1 = 0) :
    haarState q (x * fieldPlus q y) =
      -((q ^ (-(a + m)) : Kˣ) : K) * haarState q (y * fieldPlus q x) := by
  have he : n - b - 2 * (a + 1) = -(a + m) := by omega
  rw [coupling_plus_twisted_skew hq hx hy, he]

/-- **Twisted skew symmetry for `X₋`.** For weight vectors `x : (a, m)` and `y : (b, n)`. -/
theorem coupling_minus_twisted_skew {x y : OqSU2 K q} {a m b n : ℤ} (hx : IsWeight q x a m)
    (hy : IsWeight q y b n) :
    haarState q (x * fieldMinus q y) =
      -((q ^ (n - b - 2 * (a - 1)) : Kˣ) : K) * haarState q (y * fieldMinus q x) := by
  have h1 := haarState_ibp_minus q hq x y
  rw [hy, mul_smul_comm, map_smul, smul_eq_mul] at h1
  have h2 := haarState_modular q (qSqNum_ne_zero_of_not_root q hq) (fieldMinus q x) y
  have h3 : modularAut q (fieldMinus q x) =
      (((q⁻¹ ^ 2) ^ (a - 1) * (1 : Kˣ) ^ (m + 1) : Kˣ) : K) • fieldMinus q x :=
    hx.fieldMinus (q⁻¹ ^ 2) 1
  rw [h3, mul_smul_comm, map_smul, smul_eq_mul] at h2
  rw [← T_unit_eq b n (a - 1) (m + 1)]
  linear_combination h1 - ((q⁻¹ ^ b * q⁻¹⁻¹ ^ n : Kˣ) : K) * h2

/-- On the support of the selection rule the `X₋` twist is `q^(−(a+m))`. -/
theorem coupling_minus_skew_on_support {x y : OqSU2 K q} {a m b n : ℤ} (hx : IsWeight q x a m)
    (hy : IsWeight q y b n) (hb : a + b - 1 = 0) (hn : m + n + 1 = 0) :
    haarState q (x * fieldMinus q y) =
      -((q ^ (-(a + m)) : Kˣ) : K) * haarState q (y * fieldMinus q x) := by
  have he : n - b - 2 * (a - 1) = -(a + m) := by omega
  rw [coupling_minus_twisted_skew hq hx hy, he]

/-- **Twisted skew symmetry for `X₀`.** For weight vectors `x : (a, m)` and `y : (b, n)`. -/
theorem coupling_zero_twisted_skew {x y : OqSU2 K q} {a m b n : ℤ} (hx : IsWeight q x a m)
    (hy : IsWeight q y b n) :
    haarState q (x * fieldZero q y) =
      -((q ^ (n - b - 2 * (a)) : Kˣ) : K) * haarState q (y * fieldZero q x) := by
  have h1 := haarState_ibp_zero q hq x y
  rw [hy, mul_smul_comm, map_smul, smul_eq_mul] at h1
  have h2 := haarState_modular q (qSqNum_ne_zero_of_not_root q hq) (fieldZero q x) y
  have h3 : modularAut q (fieldZero q x) =
      (((q⁻¹ ^ 2) ^ (a) * (1 : Kˣ) ^ (m) : Kˣ) : K) • fieldZero q x :=
    hx.fieldZero (q⁻¹ ^ 2) 1
  rw [h3, mul_smul_comm, map_smul, smul_eq_mul] at h2
  rw [← T_unit_eq b n (a) (m)]
  linear_combination h1 - ((q⁻¹ ^ b * q⁻¹⁻¹ ^ n : Kˣ) : K) * h2

/-- On the support of the selection rule the `X₀` twist is `q^(−(a+m))`. -/
theorem coupling_zero_skew_on_support {x y : OqSU2 K q} {a m b n : ℤ} (hx : IsWeight q x a m)
    (hy : IsWeight q y b n) (hb : a + b = 0) (hn : m + n = 0) :
    haarState q (x * fieldZero q y) =
      -((q ^ (-(a + m)) : Kˣ) : K) * haarState q (y * fieldZero q x) := by
  have he : n - b - 2 * (a) = -(a + m) := by omega
  rw [coupling_zero_twisted_skew hq hx hy, he]

end QOU.FluidDynamics.HaarTriadWeight
