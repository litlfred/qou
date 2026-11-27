import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.SetTheory.Ordinal.Arithmetic
import Mathlib.SetTheory.Ordinal.Family
import Mathlib.SetTheory.Ordinal.NaturalOps
import Mathlib.Tactic.Abel
import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import Mathlib.Order.ConditionallyCompleteLattice.Basic

/-!
# QOU.AppendixSurreals.Basic — Axiomatic surreal-coefficient field

Three typeclasses, each extending the last (owner ruling 2026-11-27, "Split into
base + Conway class"):

- `SurrealBase K` — a linearly ordered field with an order-preserving
  `ofReal : ℝ →+* K` and an element `ω` above every natural.  No birthday;
  `ℝ*` is an instance.
- `BirthdayField K` — adds `birthday : K → Ordinal` with six upper-bound axioms
  linking ring operations to ordinal natural-sum.
- `SurrealField K` — adds `birthday_natCast` and Conway simplicity: the full
  Conway structure, whose intended model is `𝐍𝐨`.

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

namespace QOU.AppendixSurreals

universe u


/-- **`SurrealBase K`: the birthday-free base.**  A linearly ordered field extending `ℝ`
    (via an order-preserving `ofReal`) with an element `ω` above every natural number.

    This is exactly the structure the infinitesimal / standard-part / limit-transfer
    layer uses, and nothing more.  It carries **no** birthday, so `ℝ*` is a genuine
    instance (`HyperrealTransfer.surrealBaseHyperreal`) and theorems stated over it
    apply to `ℝ*` honestly.  Owner ruling 2026-11-27 ("Split into base + Conway class",
    beans `qou-6qbv` / `qou-3kkl`). -/
class SurrealBase (K : Type u) extends Field K, LinearOrder K, IsStrictOrderedRing K where
  /-- ℝ-algebra structure: every real number embeds in K. -/
  ofReal : ℝ →+* K
  /-- The embedding is order-preserving. -/
  ofReal_strictMono : StrictMono ofReal
  /-- The first infinite element `ω` of `K`.

      In `𝐍𝐨` this is Conway's `ω = {0, 1, 2, … | }` (Ehrlich 2012, Thm 12.5); in `ℝ*`
      it is the class of the sequence `n ↦ n`. -/
  omegaSurreal : K
  /-- `omegaSurreal` is strictly greater than every natural number. -/
  omegaSurreal_gt_natCast : ∀ n : ℕ, (n : K) < omegaSurreal

/-- **`BirthdayField K`: the base plus a birthday bounded from above.**

    The six birthday axioms below give **upper bounds only**, so they do not pin
    Conway's birthday: `flatBirthday x := if x = 0 then 0 else 1` on `ℝ*` satisfies all
    six (`HyperrealTransfer.surrealFieldHyperreal`), and so does a dyadic birthday that
    gets the naturals right (`DyadicBirthday.surrealFieldHyperrealDyadic`).  This class
    exists to state those independence results; a theorem about Conway's birthday takes
    `[SurrealField K]`. -/
class BirthdayField (K : Type u) extends SurrealBase K where
  /-- A birthday function, constrained here only from above. -/
  birthday : K → Ordinal
  /-- The birthday of zero is zero. -/
  birthday_zero : birthday 0 = 0
  /-- The birthday of one is one. -/
  birthday_one : birthday 1 = 1
  /-- Birthday is symmetric: `b(-x) = b(x)`. -/
  birthday_neg : ∀ x : K, birthday (-x) = birthday x
  /-- Birthday is bounded under sum by ordinal natural-sum. -/
  birthday_add_le : ∀ x y : K,
    birthday (x + y) ≤ Ordinal.nadd (birthday x) (birthday y)
  /-- Birthday of a dyadic midpoint is bounded by the natural-sum
      of its parents' birthdays plus one.

      This is exactly Conway's `{L | R}` recipe: the midpoint
      `(x + y) / 2` is born one day after the deepest of `x, y`.
      The bound is genuinely independent of `birthday_add_le`: the
      additive bound gives only upper bounds on `birthday (x + y)`
      (hence lower bounds on summands), whereas this asks for an
      upper bound on a *strictly earlier* surreal.

      **Narrow kernel rationale.**  Every caller in the surreals
      appendix that reasons about halving does so in the form
      `(parent₁ + parent₂) / 2` (Gonshor sign-sequence step,
      dyadic refinement).  A standalone `birthday (x / 2)` axiom
      would assert more than callers need; this combined form is
      exactly the Conway midpoint recipe and nothing more. -/
  birthday_avg_le : ∀ x y : K,
    birthday ((x + y) / 2) ≤ Ordinal.nadd (birthday x) (birthday y) + 1
  /-- Real numbers have birthday at most ω. -/
  birthday_ofReal_le_omega : ∀ r : ℝ, birthday (ofReal r) ≤ Ordinal.omega0

/-- A **surreal-coefficient field** `K`: the full Conway structure.

    `BirthdayField` plus the two axioms the six upper bounds cannot supply, each proved
    independent of them in `AppendixSurreals/BirthdayFaithful.lean`:

    * `birthday_natCast` — the natural number `n` is born on day `n`
      (the flat `ℝ*` birthday fails it);
    * `simplicity` — Conway's simplicity (tree) axiom: if every number older than `x`
      lies on the same side of `z` as of `x`, then `z ≠ x` is born after `x`
      (the dyadic `ℝ*` birthday satisfies the first axiom and fails this one).

    We axiomatise rather than construct: the intended model is `K = 𝐍𝐨`, which mathlib
    does not yet expose as a `LinearOrderedField`.  Neither `ℝ*` birthday above is a
    model; whether some other birthday on `ℝ*` is one is not addressed here.  Results
    that need only the ordered field, `ofReal` and `ω` are stated over `SurrealBase` and
    apply to `ℝ*`; lower bounds on the birthday are in `ConwayBirthday.lean`.

    -- Ref: [conway1976] Ch. 2, Theorem 11 (simplicity)
    -- Ref: [ehrlich2012] §3 (s-hierarchical ordered structures) -/
class SurrealField (K : Type u) extends BirthdayField K where
  /-- Conway: the natural number `n` is born on day `n`. -/
  birthday_natCast : ∀ n : ℕ, birthday ((n : ℕ) : K) = (n : Ordinal)
  /-- **Conway simplicity.**  For `x ≠ z`: if every `y` born before `x` lies on the same
      side of `z` as of `x`, then `z` is born after `x`. -/
  simplicity : ∀ x z : K, x ≠ z →
    (∀ y : K, birthday y < birthday x → (y < x ↔ y < z)) →
    birthday x < birthday z

/-- Coerce a real into a `SurrealBase` field. -/
instance (K : Type u) [SurrealBase K] : Coe ℝ K :=
  ⟨SurrealBase.ofReal⟩

/-- Every `SurrealBase K` is canonically an `Algebra ℝ K` via the
    `ofReal` ring homomorphism.  This unlocks Mathlib's
    `Polynomial.aeval`, `MvPolynomial.aeval`, and the full
    `Algebra`-flavored API for free. -/
noncomputable instance SurrealField.toAlgebra (K : Type u) [SurrealBase K] :
    Algebra ℝ K :=
  RingHom.toAlgebra SurrealBase.ofReal

/-! The field names of the three classes are re-exported under `SurrealField.*`, so
`SurrealField.ofReal`, `SurrealField.birthday_add_le`, … and `open SurrealField` keep
working for every consumer. -/
namespace SurrealField
export SurrealBase (ofReal ofReal_strictMono omegaSurreal omegaSurreal_gt_natCast)
export BirthdayField (birthday birthday_zero birthday_one birthday_neg birthday_add_le
  birthday_avg_le birthday_ofReal_le_omega)
end SurrealField

namespace SurrealField

variable {K : Type u} [SurrealBase K]

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
  rw [h2] at h
  exact_mod_cast h.le

/-- Zero is infinitesimal. -/
theorem zero_isInfinitesimal : IsInfinitesimal (0 : K) := by
  intro ε hε
  rw [abs_zero]
  have h := SurrealField.ofReal_strictMono (K := K) hε
  rwa [map_zero] at h

/-- The image of `ofReal` commutes with `abs`. -/
theorem ofReal_abs (r : ℝ) :
    |(SurrealField.ofReal r : K)| = SurrealField.ofReal |r| := by
  rcases le_or_gt 0 r with hr | hr
  · rw [abs_of_nonneg hr, abs_of_nonneg]
    have h := (SurrealField.ofReal_strictMono (K := K)).monotone hr
    rwa [map_zero] at h
  · rw [abs_of_neg hr, abs_of_neg, map_neg]
    have h := SurrealField.ofReal_strictMono (K := K) hr
    rwa [map_zero] at h

/-- A real is infinitesimal in `K` iff it is zero. -/
theorem ofReal_isInfinitesimal_iff_eq_zero (r : ℝ) :
    IsInfinitesimal (SurrealField.ofReal r : K) ↔ r = 0 := by
  refine ⟨fun hinf => ?_, ?_⟩
  · -- Forward: contraposition, choose ε = |r|/2 to get contradiction
    by_contra hne
    have hpos : (0 : ℝ) < |r| := abs_pos.mpr hne
    have hhalf : (0 : ℝ) < |r| / 2 := half_pos hpos
    have h := hinf (|r| / 2) hhalf
    -- h : |ofReal r| < ofReal (|r|/2)
    rw [ofReal_abs] at h
    -- h : ofReal |r| < ofReal (|r|/2)
    have hlt : |r| / 2 < |r| := by linarith
    have hmono : SurrealField.ofReal (|r|/2) < (SurrealField.ofReal |r| : K) :=
      SurrealField.ofReal_strictMono hlt
    linarith
  · rintro rfl
    rw [map_zero]
    exact zero_isInfinitesimal

/-- Negation of an infinitesimal is infinitesimal. -/
theorem IsInfinitesimal.neg {x : K} (hx : IsInfinitesimal x) :
    IsInfinitesimal (-x) := by
  intro ε hε
  rw [abs_neg]
  exact hx ε hε

/-- Sum of two infinitesimals is infinitesimal. -/
theorem IsInfinitesimal.add {x y : K}
    (hx : IsInfinitesimal x) (hy : IsInfinitesimal y) :
    IsInfinitesimal (x + y) := by
  intro ε hε
  -- |x + y| ≤ |x| + |y| < ofReal(ε/2) + ofReal(ε/2) = ofReal ε
  have hhalf : (0 : ℝ) < ε / 2 := half_pos hε
  have hx' := hx (ε/2) hhalf
  have hy' := hy (ε/2) hhalf
  have hsum : |x + y| ≤ |x| + |y| := abs_add_le x y
  have hlt : |x| + |y| < SurrealField.ofReal (ε/2) + SurrealField.ofReal (ε/2) := by
    exact add_lt_add hx' hy'
  have heq : SurrealField.ofReal (ε/2) + SurrealField.ofReal (ε/2)
              = (SurrealField.ofReal ε : K) := by
    rw [← map_add]; congr 1; ring
  rw [heq] at hlt
  exact lt_of_le_of_lt hsum hlt

/-- Sum of two finite surreals is finite. -/
theorem IsFinite.add {x y : K} (hx : IsFinite x) (hy : IsFinite y) :
    IsFinite (x + y) := by
  obtain ⟨n, hn⟩ := hx
  obtain ⟨m, hm⟩ := hy
  refine ⟨n + m, ?_⟩
  calc |x + y| ≤ |x| + |y|          := abs_add_le x y
    _ ≤ (n : K) + m                   := add_le_add hn hm
    _ = ((n + m : ℕ) : K)             := by push_cast; ring

/-- Product of two finite surreals is finite. -/
theorem IsFinite.mul {x y : K} (hx : IsFinite x) (hy : IsFinite y) :
    IsFinite (x * y) := by
  obtain ⟨n, hn⟩ := hx
  obtain ⟨m, hm⟩ := hy
  refine ⟨n * m, ?_⟩
  have habs_nonneg_x : (0 : K) ≤ |x| := abs_nonneg x
  have habs_nonneg_y : (0 : K) ≤ |y| := abs_nonneg y
  have hn_nonneg : (0 : K) ≤ (n : K) := Nat.cast_nonneg n
  have hm_nonneg : (0 : K) ≤ (m : K) := Nat.cast_nonneg m
  calc |x * y| = |x| * |y|            := abs_mul x y
    _ ≤ (n : K) * (m : K)             :=
        mul_le_mul hn hm habs_nonneg_y hn_nonneg
    _ = ((n * m : ℕ) : K)             := by push_cast; ring

/-- Finite × infinitesimal is infinitesimal. -/
theorem IsInfinitesimal.mul_finite {x y : K}
    (hx : IsInfinitesimal x) (hy : IsFinite y) :
    IsInfinitesimal (x * y) := by
  obtain ⟨n, hn⟩ := hy
  intro ε hε
  -- Need: |x * y| < ofReal ε.
  -- Case split on n: if n = 0 then |y| ≤ 0 so y = 0, so x * y = 0.
  rcases Nat.eq_zero_or_pos n with hn0 | hn0
  · -- n = 0: |y| ≤ 0, so |y| = 0 (since abs_nonneg), so y = 0.
    have hy_abs : |y| ≤ 0 := by rw [hn0] at hn; simpa using hn
    have hy_zero : y = 0 := by
      have := abs_nonneg y
      have habs_eq : |y| = 0 := le_antisymm hy_abs this
      exact abs_eq_zero.mp habs_eq
    rw [hy_zero, mul_zero, abs_zero]
    have hpos : (0 : K) < SurrealField.ofReal ε := by
      have := SurrealField.ofReal_strictMono (K := K) hε
      rwa [map_zero] at this
    exact hpos
  · -- n ≥ 1: use |x| < ofReal (ε / n) and |y| ≤ n.
    have hn_pos_real : (0 : ℝ) < n := by exact_mod_cast hn0
    have hdiv_pos : (0 : ℝ) < ε / n := div_pos hε hn_pos_real
    have hxlt : |x| < SurrealField.ofReal (ε / n) := hx (ε / n) hdiv_pos
    -- |x * y| = |x| * |y| < ofReal(ε/n) * ofReal n = ofReal ε
    have habs_mul : |x * y| = |x| * |y| := abs_mul x y
    have hy_nonneg : (0 : K) ≤ |y| := abs_nonneg y
    have hx_nonneg : (0 : K) ≤ |x| := abs_nonneg x
    have hofReal_nonneg : (0 : K) ≤ SurrealField.ofReal (ε / n) := by
      have := (SurrealField.ofReal_strictMono (K := K)).monotone hdiv_pos.le
      rwa [map_zero] at this
    -- |y| ≤ (n : K) = ofReal n
    have hyn : |y| ≤ SurrealField.ofReal (n : ℝ) := by
      have := hn
      -- hn : |y| ≤ (n : K); need same as ofReal (n : ℝ)
      have heq : (n : K) = SurrealField.ofReal (n : ℝ) := by
        rw [← map_natCast SurrealField.ofReal n]
      rwa [heq] at this
    have hlt : |x| * |y| ≤ SurrealField.ofReal (ε / n) * SurrealField.ofReal (n : ℝ) := by
      apply mul_le_mul hxlt.le hyn hy_nonneg hofReal_nonneg
    have heq_mul : SurrealField.ofReal (ε / n) * SurrealField.ofReal (n : ℝ)
                    = (SurrealField.ofReal ε : K) := by
      rw [← map_mul]; congr 1; field_simp
    rw [heq_mul] at hlt
    -- Strict: |x * y| < ofReal ε.  We have |x * y| = |x| * |y| ≤ ofReal ε.
    -- Need to sharpen: since |x| < ofReal (ε / n) strictly and |y| ≤ ofReal n,
    -- use strict monotonicity in the left factor.
    -- If |y| = 0 then |x|*|y| = 0 < ofReal ε.  Otherwise |y| > 0 and strict.
    rcases eq_or_lt_of_le hy_nonneg with hy0 | hy_pos
    · rw [habs_mul, ← hy0, mul_zero]
      have hpos : (0 : K) < SurrealField.ofReal ε := by
        have := SurrealField.ofReal_strictMono (K := K) hε
        rwa [map_zero] at this
      exact hpos
    · rw [habs_mul]
      calc |x| * |y|
          < SurrealField.ofReal (ε / n) * |y| := by
            exact (mul_lt_mul_iff_of_pos_right hy_pos).mpr hxlt
        _ ≤ SurrealField.ofReal (ε / n) * SurrealField.ofReal (n : ℝ) := by
            exact mul_le_mul_of_nonneg_left hyn hofReal_nonneg
        _ = SurrealField.ofReal ε := heq_mul

/-- Uniqueness of the real part of a finite surreal: if two reals
    both differ from `x` by an infinitesimal, they are equal. -/
theorem standardPart_unique {x : K} {r s : ℝ}
    (hr : IsInfinitesimal (x - SurrealField.ofReal r))
    (hs : IsInfinitesimal (x - SurrealField.ofReal s)) : r = s := by
  -- (ofReal r - ofReal s) = (x - ofReal s) - (x - ofReal r) is inf.
  have hdiff : IsInfinitesimal
      ((SurrealField.ofReal r : K) - SurrealField.ofReal s) := by
    have hrewrite :
        (SurrealField.ofReal r : K) - SurrealField.ofReal s
          = (x - SurrealField.ofReal s) - (x - SurrealField.ofReal r) := by
      ring
    rw [hrewrite]
    have hadd := hs.add hr.neg
    -- hadd : IsInfinitesimal (x - ofReal s + -(x - ofReal r))
    -- goal : IsInfinitesimal (x - ofReal s - (x - ofReal r))
    rw [sub_eq_add_neg]
    exact hadd
  have heq : (SurrealField.ofReal r : K) - SurrealField.ofReal s
              = SurrealField.ofReal (r - s) := by rw [map_sub]
  rw [heq] at hdiff
  have := (ofReal_isInfinitesimal_iff_eq_zero (K := K) (r - s)).mp hdiff
  linarith

/-- A finite surreal has an associated real (its standard part).

    **Construction**: `r = sup { q ∈ ℝ | ofReal q ≤ x }`.  Existence
    uses Dedekind completeness of ℝ. -/
-- Ref: [robinson1966] §3.2, [alling1987] Theorem 4.7.2
theorem isFinite_has_standardPart {x : K} (hx : IsFinite x) :
    ∃ r : ℝ, IsInfinitesimal (x - SurrealField.ofReal r) := by
  obtain ⟨n, hn⟩ := hx
  -- |x| ≤ (n : K), so -(n : K) ≤ x ≤ (n : K).
  have hx_le : x ≤ (n : K) := le_trans (le_abs_self x) hn
  have hneg_le_x : -(n : K) ≤ x := by
    have habs : -|x| ≤ x := neg_abs_le x
    have hnn : -(n : K) ≤ -|x| := neg_le_neg hn
    linarith
  -- S := { q : ℝ | ofReal q ≤ x }
  set S : Set ℝ := { q : ℝ | (SurrealField.ofReal q : K) ≤ x } with hS_def
  have hne : S.Nonempty := by
    refine ⟨-(n : ℝ), ?_⟩
    change (SurrealField.ofReal (-(n : ℝ)) : K) ≤ x
    rw [map_neg]
    have : SurrealField.ofReal ((n : ℝ)) = ((n : K)) := by
      rw [map_natCast]
    rw [this]
    exact hneg_le_x
  have hbdd : BddAbove S := by
    refine ⟨(n : ℝ), ?_⟩
    intro q hq
    by_contra hgt
    push_neg at hgt
    have h1 : (SurrealField.ofReal (n : ℝ) : K) < SurrealField.ofReal q :=
      SurrealField.ofReal_strictMono hgt
    rw [map_natCast] at h1
    have : (SurrealField.ofReal q : K) > x := lt_of_le_of_lt hx_le h1
    exact absurd hq (not_le.mpr this)
  set r := sSup S with hr_def
  refine ⟨r, ?_⟩
  intro ε hε
  -- Upper bound: r + ε > r = sup S, so ofReal (r + ε) ∉ S.
  have hr_plus : x < SurrealField.ofReal (r + ε) := by
    by_contra hle
    push_neg at hle
    have h_in_S : r + ε ∈ S := hle
    have h_le : r + ε ≤ r := le_csSup hbdd h_in_S
    linarith
  -- Lower bound: ∃ s ∈ S with r - ε < s.
  have hrε_lt_r : r - ε < r := by linarith
  obtain ⟨s, hs_in, hs_gt⟩ := exists_lt_of_lt_csSup hne hrε_lt_r
  have hof_s_le : (SurrealField.ofReal s : K) ≤ x := hs_in
  have hr_minus : (SurrealField.ofReal (r - ε) : K) < x := by
    have hlt : (SurrealField.ofReal (r - ε) : K) < SurrealField.ofReal s :=
      SurrealField.ofReal_strictMono hs_gt
    linarith
  -- Combine: |x - ofReal r| < ofReal ε.
  have hmap_add : (SurrealField.ofReal (r + ε) : K)
                    = SurrealField.ofReal r + SurrealField.ofReal ε := by
    rw [map_add]
  have hmap_sub : (SurrealField.ofReal (r - ε) : K)
                    = SurrealField.ofReal r - SurrealField.ofReal ε := by
    rw [map_sub]
  rw [hmap_add] at hr_plus
  rw [hmap_sub] at hr_minus
  rw [abs_lt]
  refine ⟨?_, ?_⟩
  · linarith
  · linarith

/-- A finite surreal is the sum of a real and an infinitesimal.
    The real is unique (= the standard part). -/
-- Ref: [robinson1966] §3.2, [alling1987] Theorem 4.7.2
theorem isFinite_decomposition {x : K} (hx : IsFinite x) :
    ∃! r : ℝ, IsInfinitesimal (x - ofReal r) := by
  obtain ⟨r, hr⟩ := isFinite_has_standardPart hx
  exact ⟨r, hr, fun s hs => standardPart_unique hs hr⟩

/-! ### Closure of `IsFinite` under the field operations

The finite surreals form a sub-(unital sub-)ring of `K`.  The
following closure lemmas (`zero`, `one`, `neg`, `sub`, plus the
already-proved `add`, `mul`) provide the predicate-level closure
needed to bundle `{x | IsFinite x}` as a `Subring K`. -/

/-- `0` is finite. -/
theorem zero_isFinite : IsFinite (0 : K) := by
  refine ⟨0, ?_⟩
  simp

/-- `1` is finite. -/
theorem one_isFinite : IsFinite (1 : K) := by
  refine ⟨1, ?_⟩
  simp

/-- Negation preserves finiteness (using the same bound). -/
theorem IsFinite.neg {x : K} (hx : IsFinite x) : IsFinite (-x) := by
  obtain ⟨n, hn⟩ := hx
  refine ⟨n, ?_⟩
  rwa [abs_neg]

/-- Subtraction of finite surreals is finite. -/
theorem IsFinite.sub {x y : K} (hx : IsFinite x) (hy : IsFinite y) :
    IsFinite (x - y) := by
  rw [sub_eq_add_neg]
  exact hx.add hy.neg

/-- Subtraction of infinitesimals is infinitesimal. -/
theorem IsInfinitesimal.sub {x y : K}
    (hx : IsInfinitesimal x) (hy : IsInfinitesimal y) :
    IsInfinitesimal (x - y) := by
  rw [sub_eq_add_neg]
  exact hx.add hy.neg

end SurrealField

end QOU.AppendixSurreals
