/-
# Finite cyclic quantum dilogarithm + N-periodic shift (Φ_b workplan result L2)

Building on **L1** (`QOU.QBeta.CyclotomicDilogCollapse.cyclotomic_collapse`,
`∏_{k<N}(1 - x·ζ^k) = 1 - x^N` at a primitive `N`-th root of unity), this file
defines the **finite cyclic quantum dilogarithm** and proves its shift structure
(PR #3768, bean `qou-nyvu`).

## The objects

* `cyclicDenom ζ x N = ∏_{k=0}^{N-1} (1 - x·ζ^k)` — the finite q-Pochhammer
  denominator `(x;ζ)_N`. By L1 it collapses to `1 - x^N` (`cyclicDenom_eq`).
* `cyclicDilog ζ x N = (cyclicDenom ζ x N)⁻¹` — the finite cyclic quantum dilog
  `Φ`, the reciprocal of the denominator.

## The shift structure

The Faddeev quantum dilogarithm satisfies a **single-step shift**
`Φ(q²x) = (1 + qx)·Φ(x)`, arising because shifting the argument of the infinite
product `(x;q)_∞ = ∏_{k≥0}(1 - x q^k)` removes/adds exactly one boundary factor.
Its finite analog is a *genuine telescoping identity* — the **finite shift factor
law** (`cyclicDenom_shift_factor`), which holds for every truncation length `m`
and needs no root-of-unity hypothesis:

    (1 - x) · cyclicDenom ζ (ζ·x) m  =  (1 - x·ζ^m) · cyclicDenom ζ x m .

Shifting the argument by `ζ` rotates the factor family `k ↦ k+1`; the product
loses the bottom boundary factor `(1 - x)` and gains the top boundary factor
`(1 - x·ζ^m)`. This is the exact finite mirror of the infinite `(qx;q)` shift.

**At the root of unity** (`m = N`, `ζ^N = 1`) the top factor `1 - x·ζ^N` equals
the bottom factor `1 - x`, so they cancel and the shift becomes an **exact
N-periodicity**: `cyclicDenom ζ (ζ·x) N = cyclicDenom ζ x N`
(`cyclicDenom_shift`), equivalently `Φ(ζ·x) = Φ(x)` (`cyclicDilog_shift`). This
is why the `(1 + qx)`-type multiplier of the *infinite* Faddeev shift is absorbed
on the cyclic branch: the cyclic wrap-around cancels the boundary factor the
infinite product would accumulate.

All results are stated over a generic field `K` (never specialised to `ℂ`), per
the §7c base-ring convention.
-/
import QOU.QBeta.CyclotomicDilogCollapse

namespace QOU.QBeta.CyclicQuantumDilog

open Finset
open QOU.QBeta.CyclotomicDilogCollapse

variable {K : Type*} [Field K]

/-- **Finite q-Pochhammer denominator** `(x;ζ)_N = ∏_{k=0}^{N-1}(1 - x·ζ^k)`.
This is the finite root-of-unity truncation of the analytic q-Pochhammer
denominator; by `cyclicDenom_eq` it collapses to the polynomial `1 - x^N`. -/
def cyclicDenom (ζ x : K) (N : ℕ) : K :=
  ∏ k ∈ Finset.range N, (1 - x * ζ ^ k)

/-- **Finite cyclic quantum dilogarithm** `Φ(x) = (x;ζ)_N⁻¹`, the reciprocal of
the finite q-Pochhammer denominator. -/
noncomputable def cyclicDilog (ζ x : K) (N : ℕ) : K :=
  (cyclicDenom ζ x N)⁻¹

@[simp] theorem cyclicDenom_zero (ζ x : K) : cyclicDenom ζ x 0 = 1 := by
  simp [cyclicDenom]

/-- Peel the top factor: `(x;ζ)_{N+1} = (x;ζ)_N · (1 - x·ζ^N)`. -/
theorem cyclicDenom_succ (ζ x : K) (N : ℕ) :
    cyclicDenom ζ x (N + 1) = cyclicDenom ζ x N * (1 - x * ζ ^ N) := by
  simp [cyclicDenom, Finset.prod_range_succ]

/-- **Cyclotomic collapse of the denominator** (corollary of L1
`cyclotomic_collapse`): at a primitive `N`-th root of unity `ζ` with `N > 0`,
the finite q-Pochhammer denominator is the polynomial `1 - x^N`. -/
theorem cyclicDenom_eq {ζ : K} {N : ℕ} (hN : 0 < N)
    (hζ : IsPrimitiveRoot ζ N) (x : K) :
    cyclicDenom ζ x N = 1 - x ^ N := by
  simpa [cyclicDenom] using cyclotomic_collapse hN hζ x

/-- **Finite shift factor law** (the honest finite analog of the Faddeev shift
`Φ(q²x) = (1 + qx)Φ(x)`). For *every* truncation length `m` — no root-of-unity
hypothesis — scaling the argument by `ζ` trades the bottom boundary factor
`(1 - x)` for the top boundary factor `(1 - x·ζ^m)`:

    (1 - x) · cyclicDenom ζ (ζ·x) m  =  (1 - x·ζ^m) · cyclicDenom ζ x m .

Both sides equal the length-`(m+1)` product `∏_{k=0}^{m}(1 - x·ζ^k)`: the left
side reconstructs it by prepending the `k = 0` factor to the shifted family, the
right side by appending the `k = m` factor to the unshifted family. -/
theorem cyclicDenom_shift_factor (ζ x : K) (m : ℕ) :
    (1 - x) * cyclicDenom ζ (ζ * x) m = (1 - x * ζ ^ m) * cyclicDenom ζ x m := by
  -- The unshifted factor family `h k = 1 - x·ζ^k`.
  set h : ℕ → K := fun k => 1 - x * ζ ^ k with hh
  -- Rewrite the ζ-scaled denominator as the shifted family `∏ h (k+1)`.
  have hshift : cyclicDenom ζ (ζ * x) m = ∏ k ∈ Finset.range m, h (k + 1) := by
    simp only [cyclicDenom, hh]
    apply Finset.prod_congr rfl
    intro k _
    ring
  -- Left side: prepend the k = 0 boundary factor `h 0 = 1 - x`.
  have hleft : (1 - x) * cyclicDenom ζ (ζ * x) m
      = ∏ k ∈ Finset.range (m + 1), h k := by
    rw [hshift, Finset.prod_range_succ']
    have : (1 : K) - x = h 0 := by simp [hh]
    rw [this]; ring
  -- Right side: append the k = m boundary factor `h m = 1 - x·ζ^m`.
  have hright : (1 - x * ζ ^ m) * cyclicDenom ζ x m
      = ∏ k ∈ Finset.range (m + 1), h k := by
    simp only [cyclicDenom, hh]
    rw [Finset.prod_range_succ]
    ring
  rw [hleft, hright]

/-- **Exact N-periodicity of the denominator** at the root of unity: scaling the
argument by `ζ` (a full rotation of the cyclic factor family) leaves the finite
denominator invariant. Equivalently, the reindex

    ∏_{k<N}(1 - x·ζ^{k+1}) = ∏_{k<N}(1 - x·ζ^k)

holds because `ζ^N = 1`. Proved via the collapse `cyclicDenom = 1 - x^N`:
`(ζ·x)^N = ζ^N·x^N = x^N`. -/
theorem cyclicDenom_shift {ζ : K} {N : ℕ} (hN : 0 < N)
    (hζ : IsPrimitiveRoot ζ N) (x : K) :
    cyclicDenom ζ (ζ * x) N = cyclicDenom ζ x N := by
  rw [cyclicDenom_eq hN hζ, cyclicDenom_eq hN hζ]
  rw [mul_pow, hζ.pow_eq_one, one_mul]

/-- The N-periodicity as an explicit `Finset.prod` reindex statement:
`∏_{k<N}(1 - x·ζ^{k+1}) = ∏_{k<N}(1 - x·ζ^k)`. -/
theorem cyclicDenom_prod_shift {ζ : K} {N : ℕ} (hN : 0 < N)
    (hζ : IsPrimitiveRoot ζ N) (x : K) :
    ∏ k ∈ Finset.range N, (1 - x * ζ ^ (k + 1))
      = ∏ k ∈ Finset.range N, (1 - x * ζ ^ k) := by
  have h := cyclicDenom_shift hN hζ x
  simp only [cyclicDenom] at h
  rw [← h]
  apply Finset.prod_congr rfl
  intro k _
  ring

/-- **Shift invariance of the finite cyclic quantum dilog** `Φ(ζ·x) = Φ(x)` at
the root of unity — the finite mirror of the Faddeev shift, with the `(1 + qx)`
multiplier absorbed by the cyclic wrap-around. -/
theorem cyclicDilog_shift {ζ : K} {N : ℕ} (hN : 0 < N)
    (hζ : IsPrimitiveRoot ζ N) (x : K) :
    cyclicDilog ζ (ζ * x) N = cyclicDilog ζ x N := by
  unfold cyclicDilog
  rw [cyclicDenom_shift hN hζ]

/-- Full periodicity under scaling by any power `ζ^j`: `Φ(ζ^j·x) = Φ(x)`. This
is the "closes as a finite N-step recursion" statement — iterating the single
`ζ`-shift `cyclicDilog_shift` `j` times leaves `Φ` unchanged, so the shift
recursion is `N`-periodic (indeed period `1` in the `ζ`-scaling). -/
theorem cyclicDilog_periodic {ζ : K} {N : ℕ} (hN : 0 < N)
    (hζ : IsPrimitiveRoot ζ N) (x : K) (j : ℕ) :
    cyclicDilog ζ (ζ ^ j * x) N = cyclicDilog ζ x N := by
  induction j with
  | zero => simp
  | succ n ih =>
    have : ζ ^ (n + 1) * x = ζ * (ζ ^ n * x) := by ring
    rw [this, cyclicDilog_shift hN hζ, ih]

end QOU.QBeta.CyclicQuantumDilog
