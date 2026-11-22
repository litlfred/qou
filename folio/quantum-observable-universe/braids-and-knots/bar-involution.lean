import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Field.Defs
import Mathlib.Tactic

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

-- Ref: [leitner2026] def:bar-involution
-- Ref: [leitner2026] prop:bar-symmetric-three-layer-synthesis
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

/-! ### The `P_avg` / `P_skew` projections

§7c base ring: these need only that **`2` is invertible**, which is an
`Invertible (2 : R)` instance over a `CommRing` — not a field. The division by
`2` is carried as the unit `⅟(2 : R)`, so the projections exist over e.g.
`ℤ[1/2][q, q⁻¹]`, which is where the bar-graded Hecke coefficients live. A
field instance is recovered for free: `[Field R] [CharZero R]` supplies
`Invertible (2 : R)` via Mathlib's `invertibleTwo`, so the earlier signature is
the special case. -/

/-- `P_avg = (1 + bar)/2`, written with the unit `⅟2`. -/
def barSymmetricProjection {R : Type*} [CommRing R] [Invertible (2 : R)]
    [BarInvolution R] (x : R) : R := ⅟(2 : R) * (x + BarInvolution.bar x)

/-- `P_skew = (1 - bar)/2`, written with the unit `⅟2`. -/
def barSkewProjection {R : Type*} [CommRing R] [Invertible (2 : R)]
    [BarInvolution R] (x : R) : R := ⅟(2 : R) * (x - BarInvolution.bar x)

/-- Every element decomposes as `x = P_avg(x) + P_skew(x)`. -/
theorem decompose {R : Type*} [CommRing R] [Invertible (2 : R)] [BarInvolution R]
    (x : R) : x = barSymmetricProjection x + barSkewProjection x := by
  unfold barSymmetricProjection barSkewProjection
  linear_combination (-x) * invOf_mul_self (2 : R)

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
  linear_combination h0

/-- Negation of bar-symmetric is bar-symmetric. -/
theorem IsBarSymmetric.neg {x : R} (hx : IsBarSymmetric x) :
    IsBarSymmetric (-x) := by
  unfold IsBarSymmetric at *
  rw [bar_neg, hx]

/-- Negation of bar-anti-symmetric is bar-anti-symmetric. -/
theorem IsBarAntiSymmetric.neg {x : R} (hx : IsBarAntiSymmetric x) :
    IsBarAntiSymmetric (-x) := by
  unfold IsBarAntiSymmetric at *
  rw [bar_neg, hx]

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
    have hrew : x ^ (2 * (k + 1)) = x ^ (2 * k) * (x * x) := by
      rw [Nat.mul_succ, pow_add]
      ring
    rw [hrew]
    exact ih.mul (IsBarSymmetric.of_mul_antisym hx hx)

/-- **Odd powers of a bar-anti-symmetric element are bar-anti-symmetric.**
    Direct corollary: `h^(2n+1)` is bar-anti-symmetric. -/
theorem IsBarAntiSymmetric.pow_two_mul_add_one {x : R}
    (hx : IsBarAntiSymmetric x) (n : ℕ) :
    IsBarAntiSymmetric (x ^ (2 * n + 1)) := by
  rw [pow_succ]
  exact IsBarAntiSymmetric.of_sym_mul (hx.pow_two_mul n) hx

end BarGrading

/-! ## Bar on integers, inverses (provable, no axiom needed)

`bar` fixes every rational scalar — proved from the four ring-
involution axioms alone. Used by the `Field`-section projection
identities below. -/

section BarOnScalars
variable {R : Type*} [CommRing R] [BarInvolution R]

/-- `bar 2 = 2`. -/
theorem bar_two : BarInvolution.bar (2 : R) = 2 := by
  have h : (2 : R) = 1 + 1 := by ring
  rw [h, BarInvolution.bar_add, BarInvolution.bar_one]

/-- `bar` fixes every natural-number scalar. -/
theorem bar_natCast (n : ℕ) : BarInvolution.bar ((n : R)) = (n : R) := by
  induction n with
  | zero =>
    simpa using BarInvolution.bar_zero
  | succ k ih =>
    have hstep : ((k + 1 : ℕ) : R) = (k : R) + 1 := by push_cast; ring
    rw [hstep, BarInvolution.bar_add, BarInvolution.bar_one, ih]

/-- Every natural-number scalar is bar-symmetric. -/
theorem isBarSymmetric_natCast (n : ℕ) : IsBarSymmetric ((n : R)) :=
  bar_natCast n

end BarOnScalars

/-! ## Projection identities (need only `Invertible (2 : R)`, not a field)

`P_avg` acts as the identity on bar-symmetric, kills bar-anti-symmetric.
`P_skew` is the complementary projection.

§7c: the whole section runs over a `CommRing` with `2` invertible; the sole
inverse used is the unit `⅟(2 : R)`. The one statement here that genuinely
needs a field — `bar_inv`, which inverts an element that may *vanish* — is
isolated in its own `section FieldInverse` below. -/

section Projections
variable {R : Type*} [CommRing R] [Invertible (2 : R)] [BarInvolution R]

/-- `bar(⅟2) = ⅟2`. Foundation for `barSymmetricProjection` idempotency.
    Over a `CommRing`: `bar(⅟2)·2 = bar(⅟2·2) = bar 1 = 1`, and the inverse
    of `2` is unique — no division, and no field. -/
theorem bar_invOf_two : BarInvolution.bar (⅟(2 : R)) = ⅟(2 : R) := by
  have hb2 : BarInvolution.bar (2 : R) = 2 := bar_two
  have h : BarInvolution.bar (⅟(2 : R)) * 2 = 1 := by
    have hmul : BarInvolution.bar (⅟(2 : R) * (2 : R))
        = BarInvolution.bar (⅟(2 : R)) * BarInvolution.bar (2 : R) :=
      BarInvolution.bar_mul _ _
    rw [invOf_mul_self, BarInvolution.bar_one, hb2] at hmul
    exact hmul.symm
  calc BarInvolution.bar (⅟(2 : R))
      = BarInvolution.bar (⅟(2 : R)) * (2 * ⅟(2 : R)) := by
        rw [mul_invOf_self, mul_one]
    _ = BarInvolution.bar (⅟(2 : R)) * 2 * ⅟(2 : R) := by ring
    _ = ⅟(2 : R) := by rw [h, one_mul]

omit [Invertible (2 : R)] in
/-- Every integer scalar is bar-symmetric (pure `CommRing` content). -/
theorem isBarSymmetric_intCast (n : ℤ) : IsBarSymmetric ((n : R)) := by
  unfold IsBarSymmetric
  induction n using Int.rec with
  | ofNat k => simpa using bar_natCast (R := R) k
  | negSucc k =>
    have hstep : (Int.negSucc k : R) = -((k + 1 : ℕ) : R) := by push_cast; ring
    rw [hstep, bar_neg, bar_natCast]

/-- `P_avg(x) = x` when `x` is bar-symmetric. -/
theorem barSymmetricProjection_of_sym {x : R} (hx : IsBarSymmetric x) :
    barSymmetricProjection x = x := by
  unfold barSymmetricProjection
  unfold IsBarSymmetric at hx
  rw [hx]
  linear_combination x * invOf_mul_self (2 : R)

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
  rw [hx]
  linear_combination x * invOf_mul_self (2 : R)

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

/-- **`P_avg(x)` is bar-symmetric** for every `x : R`. Uses
    `bar_half` (proved above). -/
theorem barSymmetricProjection_isBarSymmetric (x : R) :
    IsBarSymmetric (barSymmetricProjection x) := by
  unfold IsBarSymmetric barSymmetricProjection
  rw [BarInvolution.bar_mul, bar_invOf_two, BarInvolution.bar_add,
      BarInvolution.bar_involutive]
  ring

/-- **`P_avg` is idempotent**: applying twice = applying once.
    Follows directly from `barSymmetricProjection_isBarSymmetric`
    and `barSymmetricProjection_of_sym`. -/
theorem barSymmetricProjection_idempotent (x : R) :
    barSymmetricProjection (barSymmetricProjection x) = barSymmetricProjection x :=
  barSymmetricProjection_of_sym (barSymmetricProjection_isBarSymmetric x)

/-- **`P_skew(x)` is bar-anti-symmetric** for every `x : R`. -/
theorem barSkewProjection_isBarAntiSymmetric (x : R) :
    IsBarAntiSymmetric (barSkewProjection x) := by
  unfold IsBarAntiSymmetric barSkewProjection
  rw [BarInvolution.bar_mul, bar_invOf_two,
      show x - BarInvolution.bar x =
        x + (-1) * BarInvolution.bar x by ring,
      BarInvolution.bar_add, BarInvolution.bar_mul,
      BarInvolution.bar_involutive]
  -- bar(-1) = -1, from `bar_neg 1` + `bar_one`.
  have hbar_neg_one : BarInvolution.bar (-1 : R) = -1 := by
    rw [show (-1 : R) = -(1 : R) by ring, bar_neg, BarInvolution.bar_one]
  rw [hbar_neg_one]
  ring

/-- **`P_skew` is idempotent**. -/
theorem barSkewProjection_idempotent (x : R) :
    barSkewProjection (barSkewProjection x) = barSkewProjection x :=
  barSkewProjection_of_antisym (barSkewProjection_isBarAntiSymmetric x)

end Projections

/-! ## The one genuinely field-requiring statement

`bar (x⁻¹) = (bar x)⁻¹` quantifies over **every** `x : R`, including `x = 0`,
so it needs a total inverse on `R` — a `GroupWithZero`/`Field`, not a unit.
This is the §7c "inverse of something that can vanish" case: it is *not*
restatable over `CommRing` with `x : Rˣ` without dropping the `x = 0` branch
that the proof explicitly discharges. It therefore keeps its own field section,
and nothing above depends on it. -/

section FieldInverse
variable {R : Type*} [Field R] [BarInvolution R]

/-- `bar (x⁻¹) = (bar x)⁻¹` over a field. From `bar(x · x⁻¹) = bar 1 = 1`
    and the multiplicativity of bar. -/
theorem bar_inv (x : R) :
    BarInvolution.bar x⁻¹ = (BarInvolution.bar x)⁻¹ := by
  by_cases hx : x = 0
  · rw [hx, inv_zero, BarInvolution.bar_zero, inv_zero]
  · have h_bar_ne : BarInvolution.bar x ≠ 0 := by
      intro h
      apply hx
      have hbb : BarInvolution.bar (BarInvolution.bar x) =
          BarInvolution.bar 0 := by rw [h]
      rw [BarInvolution.bar_involutive, BarInvolution.bar_zero] at hbb
      exact hbb
    have h1 : BarInvolution.bar x * BarInvolution.bar x⁻¹ = 1 := by
      rw [← BarInvolution.bar_mul, mul_inv_cancel₀ hx, BarInvolution.bar_one]
    exact eq_inv_of_mul_eq_one_left (by rw [mul_comm]; exact h1)

/-- `bar(1/2) = 1/2` — the field-division form of `bar_invOf_two`. -/
theorem bar_half : BarInvolution.bar ((1 : R) / 2) = 1 / 2 := by
  rw [one_div, bar_inv, bar_two]

end FieldInverse

end QOU.BraidKnot.BarInvolutionDef
