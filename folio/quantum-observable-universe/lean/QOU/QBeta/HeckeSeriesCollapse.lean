import Mathlib.Algebra.Algebra.Basic
import Mathlib.Tactic.Module
import Mathlib.Tactic.LinearCombination
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.FieldSimp

/-!
# Every order in φ of a single-crossing photon reduces to first order

Part B of `computations/probes/np_splitting/np_charge_vertex_search_preregistration.md`.

A crossing `σ` satisfies the Hecke relation `σ² = h·σ + 1`, `h = q − q⁻¹`. So every power of `σ`,
and therefore every polynomial in `σ` (every truncation of the photon series in `φ`), is
`a + b·σ` with scalars `a, b`. The pair shift is linear in the inserted element and is `1` on the
identity, so the pair shift of `a + b·σ` is `a + b·ΔE_σ`. If `b ≠ 0`, that has a Coulomb form
exactly when `ΔE_σ` has one (`coulomb_of_affine`). With `TwoBlockExchangeNotCoulomb.not_coulomb_s2`
this gives: no finite order of the single-crossing photon between two `V³` blocks is a
charge–charge term, except an order whose `σ` coefficient vanishes, which carries no exchange.
-/

namespace QOU.QBeta.HeckeSeriesCollapse

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- Hecke collapse: if `s² = h•s + 1` then `sⁿ = a•1 + b•s` for scalars `a, b`. -/
theorem pow_eq_affine (s : A) (h : R) (hs : s * s = h • s + 1) (n : ℕ) :
    ∃ a b : R, s ^ n = a • (1 : A) + b • s := by
  induction n with
  | zero => exact ⟨1, 0, by simp⟩
  | succ n ih =>
    obtain ⟨a, b, hab⟩ := ih
    refine ⟨b, a + b * h, ?_⟩
    rw [pow_succ, hab, add_mul, smul_mul_assoc, smul_mul_assoc, one_mul, hs]
    module

/-- Polynomials in `s` (every finite truncation of a series in `s`) are affine in `s`. -/
theorem sum_pow_eq_affine (s : A) (h : R) (hs : s * s = h • s + 1) (c : ℕ → R) (N : ℕ) :
    ∃ a b : R, (∑ n ∈ Finset.range N, c n • s ^ n) = a • (1 : A) + b • s := by
  induction N with
  | zero => exact ⟨0, 0, by simp⟩
  | succ N ih =>
    obtain ⟨a, b, hab⟩ := ih
    obtain ⟨a', b', h'⟩ := pow_eq_affine s h hs N
    refine ⟨a + c N * a', b + c N * b', ?_⟩
    rw [Finset.sum_range_succ, hab, h']
    module

/-- A Coulomb form on the four nucleon pairs, for a pair shift `f za zb` (`za, zb` = number of
`u` bits on each block; `Q = z − 1`). Same shape as `TwoBlockExchange.CoulombForm`. -/
def CoulombShape (f : ℕ → ℕ → ℚ) : Prop :=
  ∃ c κ : ℚ, ∀ za ∈ [1, 2], ∀ zb ∈ [1, 2], f za zb = c + κ * ((za : ℚ) - 1) * ((zb : ℚ) - 1)

/-- If `a + b·g` has a Coulomb shape and `b ≠ 0`, so does `g`. -/
theorem coulomb_of_affine (g : ℕ → ℕ → ℚ) (a b : ℚ) (hb : b ≠ 0)
    (h : CoulombShape fun za zb => a + b * g za zb) : CoulombShape g := by
  obtain ⟨c, κ, hc⟩ := h
  refine ⟨(c - a) / b, κ / b, fun za hza zb hzb => ?_⟩
  have := hc za hza zb hzb
  field_simp
  linear_combination this

end QOU.QBeta.HeckeSeriesCollapse
