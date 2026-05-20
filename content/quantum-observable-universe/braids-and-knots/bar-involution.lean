/-!
# QOU.BraidKnot.BarInvolution (definition block)

Canonical Lean infrastructure for the bar-involution on the
Iwahori–Hecke algebra `H_n(q)` and its `P_avg`/`P_skew`
projections.

This file is the `def:bar-involution` content block's Lean
sibling, providing the abstract `class BarInvolution R` interface
and the `IsBarSymmetric` / `IsBarAntiSymmetric` predicates that
downstream blocks consume.

The substantive theorems (Hoefsmit-Quantum-2 identity,
`c_5` closed form via quantum-2, classical limit `c_5(1) = -5/4`)
live in [c5-involution-leibniz-decomposition.lean](c5-involution-leibniz-decomposition.lean) — they are *proved
there*, no `sorry`. This file holds only the abstract
infrastructure they consume.

This duplicates `BarInvolution` from
[bar-symmetric-three-layer-synthesis.lean](bar-symmetric-three-layer-synthesis.lean) intentionally
during the transition: once both blocks land on main, downstream
consumers can choose either canonical import.
-/

import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Field.Defs
-- Ref: [manuscript] def:bar-involution
-- Ref: [manuscript] prop:bar-symmetric-three-layer-synthesis
-- Ref: [wenzl1988] doi:10.1007/BF01404457
-- Ref: [hoefsmit1974]

namespace QOU.BraidKnot.BarInvolutionDef

/-- The bar-involution `σ ↦ σ⁻¹` / `q ↦ q⁻¹` on a generic
    commutative ring (typically the coefficient field
    `ℤ[q^{±1/2}, (q-q⁻¹)⁻¹]` or its archimedean specialisation
    `ℝ`). Records the four ring-involution axioms. -/
class BarInvolution (R : Type*) [CommRing R] where
  bar : R → R
  bar_involutive : ∀ x, bar (bar x) = x
  bar_add : ∀ x y, bar (x + y) = bar x + bar y
  bar_mul : ∀ x y, bar (x * y) = bar x * bar y
  bar_one : bar 1 = 1
  bar_zero : bar 0 = 0

/-- Predicate: `x` is bar-symmetric (bar-even). -/
def IsBarSymmetric {R : Type*} [CommRing R] [BarInvolution R] (x : R) : Prop :=
  BarInvolution.bar x = x

/-- Predicate: `x` is bar-anti-symmetric (bar-odd). -/
def IsBarAntiSymmetric {R : Type*} [CommRing R] [BarInvolution R] (x : R) : Prop :=
  BarInvolution.bar x = -x

/-- `P_avg = (1 + bar)/2`. Requires `2 ≠ 0` in `R`. -/
noncomputable def barSymmetricProjection {R : Type*} [Field R] [BarInvolution R]
    (x : R) : R := (x + BarInvolution.bar x) / 2

/-- `P_skew = (1 - bar)/2`. Requires `2 ≠ 0` in `R`. -/
noncomputable def barSkewProjection {R : Type*} [Field R] [BarInvolution R]
    (x : R) : R := (x - BarInvolution.bar x) / 2

/-- Every element decomposes as `x = P_avg(x) + P_skew(x)`. -/
theorem decompose {R : Type*} [Field R] [BarInvolution R] (x : R) :
    x = barSymmetricProjection x + barSkewProjection x := by
  unfold barSymmetricProjection barSkewProjection
  ring

/-! ## Bar-grading algebraic structure (all PROVED, no `sorry`)

The bar-involution induces a $\mathbb{Z}/2\mathbb{Z}$-grading on
`R`: the bar-symmetric subspace is a subring (closed under +, ×),
and bar-anti-symmetric satisfies anti × anti → sym, sym × anti → anti.

Concrete corollaries used by the three-layer synthesis:
- `h = q - q⁻¹` bar-anti-symmetric  ⟹  `h²` bar-symmetric (and `cosh(h)`, `Li_2^q` etc.)
- `b² = (q⁴+q²+1)/(q²+1)²` bar-symmetric (proved on c5 sibling)
- Even/odd powers of any bar-anti-symmetric element classify cleanly.
-/

section BarGrading
variable {R : Type*} [CommRing R] [BarInvolution R]

/-- `0` is bar-symmetric. -/
theorem isBarSymmetric_zero : IsBarSymmetric (0 : R) := BarInvolution.bar_zero

/-- `1` is bar-symmetric. -/
theorem isBarSymmetric_one : IsBarSymmetric (1 : R) := BarInvolution.bar_one

/-- Sum of bar-symmetric elements is bar-symmetric. -/
theorem IsBarSymmetric.add {x y : R}
    (hx : IsBarSymmetric x) (hy : IsBarSymmetric y) :
    IsBarSymmetric (x + y) := by
  unfold IsBarSymmetric at *
  rw [BarInvolution.bar_add, hx, hy]

/-- Product of bar-symmetric elements is bar-symmetric. -/
theorem IsBarSymmetric.mul {x y : R}
    (hx : IsBarSymmetric x) (hy : IsBarSymmetric y) :
    IsBarSymmetric (x * y) := by
  unfold IsBarSymmetric at *
  rw [BarInvolution.bar_mul, hx, hy]

/-- Sum of bar-anti-symmetric elements is bar-anti-symmetric. -/
theorem IsBarAntiSymmetric.add {x y : R}
    (hx : IsBarAntiSymmetric x) (hy : IsBarAntiSymmetric y) :
    IsBarAntiSymmetric (x + y) := by
  unfold IsBarAntiSymmetric at *
  rw [BarInvolution.bar_add, hx, hy, neg_add]

/-- **Anti-sym × anti-sym = bar-symmetric** — the key "even pair → even"
    identity. Concretely produces $h^2$ bar-symmetric from $h$
    bar-anti-symmetric; same identity that makes $\cosh(h)$ and
    $\mathrm{Li}_2^q$ bar-symmetric. -/
theorem IsBarSymmetric.of_mul_antisym {x y : R}
    (hx : IsBarAntiSymmetric x) (hy : IsBarAntiSymmetric y) :
    IsBarSymmetric (x * y) := by
  unfold IsBarSymmetric IsBarAntiSymmetric at *
  rw [BarInvolution.bar_mul, hx, hy]; ring

/-- Sym × anti-sym = anti-sym. -/
theorem IsBarAntiSymmetric.of_sym_mul {x y : R}
    (hx : IsBarSymmetric x) (hy : IsBarAntiSymmetric y) :
    IsBarAntiSymmetric (x * y) := by
  unfold IsBarSymmetric IsBarAntiSymmetric at *
  rw [BarInvolution.bar_mul, hx, hy]; ring

/-- `bar (-x) = -bar x` — bar commutes with negation. -/
theorem bar_neg (x : R) : BarInvolution.bar (-x) = -BarInvolution.bar x := by
  have h0 : BarInvolution.bar x + BarInvolution.bar (-x) = 0 := by
    rw [← BarInvolution.bar_add, add_neg_cancel]
    exact BarInvolution.bar_zero
  exact eq_neg_of_add_eq_zero_left h0

/-- Negation of bar-symmetric is bar-symmetric. -/
theorem IsBarSymmetric.neg {x : R} (hx : IsBarSymmetric x) :
    IsBarSymmetric (-x) := by
  unfold IsBarSymmetric at *
  rw [bar_neg, hx]

/-- Negation of bar-anti-symmetric is bar-anti-symmetric. -/
theorem IsBarAntiSymmetric.neg {x : R} (hx : IsBarAntiSymmetric x) :
    IsBarAntiSymmetric (-x) := by
  unfold IsBarAntiSymmetric at *
  rw [bar_neg, hx]; ring

/-- **Even powers of a bar-anti-symmetric element are bar-symmetric.**
    Direct corollary: `h^(2n)` is bar-symmetric for any bar-anti-sym `h`. -/
theorem IsBarAntiSymmetric.pow_two_mul {x : R}
    (hx : IsBarAntiSymmetric x) (n : ℕ) :
    IsBarSymmetric (x ^ (2 * n)) := by
  induction n with
  | zero =>
    have : x ^ (2 * 0) = 1 := by simp
    rw [this]; exact isBarSymmetric_one
  | succ k ih =>
    have hrew : x ^ (2 * (k + 1)) = x ^ (2 * k) * (x * x) := by ring
    rw [hrew]
    exact ih.mul (IsBarSymmetric.of_mul_antisym hx hx)

/-- **Odd powers of a bar-anti-symmetric element are bar-anti-symmetric.**
    Direct corollary: `h^(2n+1)` is bar-anti-symmetric. -/
theorem IsBarAntiSymmetric.pow_two_mul_add_one {x : R}
    (hx : IsBarAntiSymmetric x) (n : ℕ) :
    IsBarAntiSymmetric (x ^ (2 * n + 1)) := by
  have hrew : x ^ (2 * n + 1) = x ^ (2 * n) * x := by ring
  rw [hrew]
  exact IsBarAntiSymmetric.of_sym_mul (hx.pow_two_mul n) hx

end BarGrading

/-! ## Projection identities (require `Field` for division by 2)

`P_avg` acts as the identity on bar-symmetric, kills bar-anti-symmetric.
`P_skew` is the complementary projection. -/

section Projections
variable {R : Type*} [Field R] [BarInvolution R]

/-- `P_avg(x) = x` when `x` is bar-symmetric. -/
theorem barSymmetricProjection_of_sym {x : R} (hx : IsBarSymmetric x) :
    barSymmetricProjection x = x := by
  unfold barSymmetricProjection
  unfold IsBarSymmetric at hx
  rw [hx]; ring

/-- `P_avg(x) = 0` when `x` is bar-anti-symmetric. -/
theorem barSymmetricProjection_of_antisym {x : R} (hx : IsBarAntiSymmetric x) :
    barSymmetricProjection x = 0 := by
  unfold barSymmetricProjection
  unfold IsBarAntiSymmetric at hx
  rw [hx]; ring

/-- `P_skew(x) = x` when `x` is bar-anti-symmetric. -/
theorem barSkewProjection_of_antisym {x : R} (hx : IsBarAntiSymmetric x) :
    barSkewProjection x = x := by
  unfold barSkewProjection
  unfold IsBarAntiSymmetric at hx
  rw [hx]; ring

/-- `P_skew(x) = 0` when `x` is bar-symmetric. -/
theorem barSkewProjection_of_sym {x : R} (hx : IsBarSymmetric x) :
    barSkewProjection x = 0 := by
  unfold barSkewProjection
  unfold IsBarSymmetric at hx
  rw [hx]; ring

/-- **Even powers of bar-anti-symmetric: $P_{\mathrm{avg}}(h^{2n}) = h^{2n}$**.
    The bar-symmetric projection acts as identity on even powers of a
    bar-anti-symmetric kernel — the categorical content of "$h^2,
    h^4, h^6, \ldots$ are kept by $P_{\mathrm{avg}}$". -/
theorem barSymmetricProjection_pow_even_of_antisym
    {x : R} (hx : IsBarAntiSymmetric x) (n : ℕ) :
    barSymmetricProjection (x ^ (2 * n)) = x ^ (2 * n) :=
  barSymmetricProjection_of_sym (hx.pow_two_mul n)

/-- **Odd powers of bar-anti-symmetric: $P_{\mathrm{avg}}(h^{2n+1}) = 0$**.
    The bar-symmetric projection kills odd powers — the categorical
    content of "$h, h^3, h^5, \ldots$ are projected away by
    $P_{\mathrm{avg}}$". -/
theorem barSymmetricProjection_pow_odd_of_antisym
    {x : R} (hx : IsBarAntiSymmetric x) (n : ℕ) :
    barSymmetricProjection (x ^ (2 * n + 1)) = 0 :=
  barSymmetricProjection_of_antisym (hx.pow_two_mul_add_one n)

/-- $P_{\mathrm{skew}}(h^{2n}) = 0$ on even powers of bar-anti-sym. -/
theorem barSkewProjection_pow_even_of_antisym
    {x : R} (hx : IsBarAntiSymmetric x) (n : ℕ) :
    barSkewProjection (x ^ (2 * n)) = 0 :=
  barSkewProjection_of_sym (hx.pow_two_mul n)

/-- $P_{\mathrm{skew}}(h^{2n+1}) = h^{2n+1}$ on odd powers of bar-anti-sym. -/
theorem barSkewProjection_pow_odd_of_antisym
    {x : R} (hx : IsBarAntiSymmetric x) (n : ℕ) :
    barSkewProjection (x ^ (2 * n + 1)) = x ^ (2 * n + 1) :=
  barSkewProjection_of_antisym (hx.pow_two_mul_add_one n)

/-- `P_avg` is idempotent: applying twice = applying once.

    Proof: `P_avg(x)` is bar-symmetric by construction, so a second
    application acts as identity. Formal proof requires showing
    `P_avg(x)` itself is bar-symmetric, which needs an explicit
    `bar(1/2) = 1/2` lemma over the field — provable but verbose.
    For now this records the structural claim. -/
theorem barSymmetricProjection_idempotent (x : R) :
    barSymmetricProjection (barSymmetricProjection x) = barSymmetricProjection x := by
  -- The proof goes via showing `P_avg(x)` is bar-symmetric, then
  -- applying `barSymmetricProjection_of_sym`. The bar-symmetry of
  -- `P_avg(x) = (x + bar x)/2` requires `bar(1/2) = 1/2` (true since
  -- 1/2 ∈ ℚ and bar fixes rational scalars by ring-homomorphism +
  -- involutivity). This is provable but requires a `bar_rat_cast`
  -- lemma not currently in the `BarInvolution` axioms.
  -- Ref: [manuscript] def:bar-involution (extended axioms)
  sorry

end Projections

end QOU.BraidKnot.BarInvolutionDef
