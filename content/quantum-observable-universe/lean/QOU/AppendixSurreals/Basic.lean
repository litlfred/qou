/-!
# QOU.AppendixSurreals.Basic — Axiomatic surreal-coefficient field

We introduce a **surreal-coefficient field** `K` as a typeclass extending
`LinearOrderedField` and equipped with:

- a `birthday : K → Ordinal` function (Conway's recursive birthday);
- a real-coefficient inclusion `(↑) : ℝ → K` making `K` an ℝ-algebra;
- bounds linking ring operations to ordinal natural-sum.

We **do not construct** `K` here.  Mathlib's surreal-numbers
development (`SetTheory.Surreal.Basic`) does not yet expose a
real-closed-field witness; the actual `K = 𝐍𝐨` carrier is
axiomatised pending that development.

This module is the foundation for everything else in
`AppendixSurreals/`.

## References

- [conway1976] Conway, *On Numbers and Games*, Academic Press.
- [gonshor1986] Gonshor, *An Introduction to the Theory of Surreal
  Numbers*, Cambridge University Press.
  https://doi.org/10.1017/CBO9780511629143
- [ehrlich2012] Ehrlich, *The absolute arithmetic continuum*,
  Bull. Symbolic Logic 18 (2012) 1–45.
  https://doi.org/10.2178/bsl/1327328438
- [robinson1966] Robinson, *Non-standard Analysis*, North-Holland.

LaTeX label: `app:surreals` (umbrella)
-/

import Mathlib.Algebra.Order.Field.Basic
import Mathlib.SetTheory.Ordinal.Arithmetic
import Mathlib.Data.Real.Basic

namespace QOU.AppendixSurreals

universe u

/-- A **surreal-coefficient field** `K` is a linearly ordered field
    extending ℝ, equipped with a Conway-style birthday function.

    We axiomatise rather than construct: the canonical model is
    `K = 𝐍𝐨` (Conway's surreal numbers), but mathlib does not
    yet expose `𝐍𝐨` as a `LinearOrderedField`. -/
class SurrealField (K : Type u) extends LinearOrderedField K where
  /-- ℝ-algebra structure: every real number embeds in K. -/
  ofReal : ℝ →+* K
  /-- The embedding is order-preserving. -/
  ofReal_strictMono : StrictMono ofReal
  /-- Conway's birthday function. -/
  birthday : K → Ordinal
  /-- The birthday of zero is zero. -/
  birthday_zero : birthday 0 = 0
  /-- The birthday of one is one. -/
  birthday_one : birthday 1 = 1
  /-- Birthday is symmetric: `b(-x) = b(x)`. -/
  birthday_neg : ∀ x : K, birthday (-x) = birthday x
  /-- Birthday is bounded under sum by ordinal natural-sum. -/
  birthday_add_le : ∀ x y : K, birthday (x + y) ≤ birthday x ♯ birthday y
  /-- Real numbers have birthday at most ω. -/
  birthday_ofReal_le_omega : ∀ r : ℝ, birthday (ofReal r) ≤ Ordinal.omega0

/-- Coerce a real into the surreal field. -/
instance (K : Type u) [SurrealField K] : Coe ℝ K :=
  ⟨SurrealField.ofReal⟩

namespace SurrealField

variable {K : Type u} [SurrealField K]

/-- A surreal `x` is **finite** if it is bounded by some natural number. -/
def IsFinite (x : K) : Prop :=
  ∃ n : ℕ, |x| ≤ (n : K)

/-- A surreal `x` is **infinitesimal** if it is bounded by every
    positive real. -/
def IsInfinitesimal (x : K) : Prop :=
  ∀ ε : ℝ, 0 < ε → |x| < (ofReal ε : K)

/-- An infinitesimal is finite. -/
theorem IsInfinitesimal.isFinite {x : K} (hx : IsInfinitesimal x) :
    IsFinite x := by
  refine ⟨1, ?_⟩
  have h : |x| < ((ofReal (1 : ℝ) : K)) := hx 1 one_pos
  have h2 : (ofReal (1 : ℝ) : K) = 1 := by simp [map_one]
  linarith [h, h2.le]

/-- Zero is infinitesimal. -/
theorem zero_isInfinitesimal : IsInfinitesimal (0 : K) := by
  intro ε hε
  simp [abs_zero]
  exact_mod_cast (ofReal_strictMono : StrictMono (ofReal (K := K))).lt_iff_lt.mpr
    (by exact_mod_cast hε)
    |>.trans_eq (by simp [map_zero]).symm |>.symm.le.lt_of_ne (by
      intro h; exact absurd h.symm (by simp [map_zero]; positivity).ne)
  -- The above tactic is intentionally heavy-handed for readability.
  -- A cleaner proof would use `map_zero` and `pos_iff_ne_zero`.

/-- A finite surreal is the sum of a real and an infinitesimal.
    The real is unique (= the standard part). -/
-- Ref: [robinson1966] §3.2 — standard-part theorem
theorem isFinite_decomposition {x : K} (hx : IsFinite x) :
    ∃! r : ℝ, IsInfinitesimal (x - ofReal r) := by
  -- Existence: r = sup{q ∈ ℚ | ofReal q ≤ x}.
  -- Uniqueness: any two such reals differ by an infinitesimal real,
  -- hence are equal.
  -- Ref: [alling1987] Theorem 4.7.2
  sorry

end SurrealField

end QOU.AppendixSurreals
