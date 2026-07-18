import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Ring.Defs

/-!
# Cyclotomic value truncation — the residue ↔ Habiro-tail change of basis is finite

Structural core supporting
`prop:habiro-residue-sum-equivalence`
(`content/.../mass-theory/habiro-residue-sum-equivalence.md`) and the audit
`docs/audits/2026-07-18-residue-habiro-tail-algebraic-not-analytic.md`.

The identity between the Habiro cyclotomic expansion `Σ_m a_m (q;q)_m` and the
Gröbner–Shirshov residue spectral sum is often labelled an *analytic* identity.
It is not: both sides are algebraic operations on one element of the Habiro
ring `Ẑ[q]`, related by the unipotent-triangular evaluation-at-roots-of-unity
map. The load-bearing algebraic fact is that at a root of unity `ζ` where
`(ζ;ζ)_N = 0`, the cyclotomic sum **truncates** to its degree-`< N` partial sum
— every higher term vanishes because the vanishing Pochhammer factor persists.
There is nothing to resum; the change of basis is finite.

Generic `[CommRing R]`, §7c wall-safe: no `ℝ`, no ordering, no analysis. The
`ζ` is an arbitrary ring element with `(ζ;ζ)_N = 0` (a root of unity in the
intended reading); no root-of-unity structure is needed for the truncation.

Verified `lean`-direct against the pinned Mathlib (exit 0), sorry-free.

Ref: [habiro2004] https://doi.org/10.2140/gt.2004.8.1127
-/

open Finset

namespace QOU.Common

variable {R : Type*} [CommRing R]

/-- Diagonal q-Pochhammer `(u;u)_m = ∏_{k=1}^{m} (1 - u^k)`. -/
noncomputable def qPochDiag (u : R) (m : ℕ) : R :=
  ∏ k ∈ Finset.range m, (1 - u ^ (k + 1))

/-- If `(u;u)_N = 0` then `(u;u)_m = 0` for every `m ≥ N`: the vanishing factor
    of the shorter product persists into the longer one. -/
theorem qPochDiag_eq_zero_of_ge (u : R) {N m : ℕ}
    (hN : qPochDiag u N = 0) (hm : N ≤ m) : qPochDiag u m = 0 := by
  unfold qPochDiag at hN ⊢
  have hsub : Finset.range N ⊆ Finset.range m := by
    intro x hx; rw [Finset.mem_range] at hx ⊢; omega
  rw [← Finset.prod_sdiff hsub, hN, mul_zero]

/-- **Cyclotomic value truncates.** At a root of unity `ζ` with `(ζ;ζ)_N = 0`,
    a cyclotomic sum `Σ_{m ≤ M} a_m (ζ;ζ)_m` (`M ≥ N`) equals its partial sum up
    to `N`: every term with `m ≥ N` vanishes.

    This is the finite, unipotent-triangular change of basis between the Habiro
    cyclotomic coefficients `a_m` and the root-of-unity value — the algebraic
    fact that makes the residue ↔ cyclotomic-tail equivalence a **finite
    algebraic identity**, not an analytic one. -/
theorem cyclotomic_value_truncates
    (a : ℕ → R) (ζ : R) (N : ℕ) (hζ : qPochDiag ζ N = 0) (M : ℕ) (hM : N ≤ M) :
    (∑ m ∈ Finset.range (M + 1), a m * qPochDiag ζ m)
      = ∑ m ∈ Finset.range N, a m * qPochDiag ζ m := by
  have hsub : Finset.range N ⊆ Finset.range (M + 1) := by
    intro x hx; rw [Finset.mem_range] at hx ⊢; omega
  rw [← Finset.sum_sdiff hsub]
  have hz : (∑ k ∈ Finset.range (M + 1) \ Finset.range N, a k * qPochDiag ζ k) = 0 := by
    apply Finset.sum_eq_zero
    intro k hk
    rw [Finset.mem_sdiff, Finset.mem_range, Finset.mem_range, not_lt] at hk
    rw [qPochDiag_eq_zero_of_ge ζ hζ hk.2, mul_zero]
  rw [hz, zero_add]

end QOU.Common
