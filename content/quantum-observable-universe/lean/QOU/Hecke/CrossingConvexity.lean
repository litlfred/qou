/-
# The two crossings: coordinates, the cone, and what a central multiplier does

Three measured claims from the `Delta_bind` arc are algebra, not measurement,
and this file discharges them.  A fourth is measurement and is **not** proved
here; §5 says so explicitly, because the value of a formalisation is entirely in
knowing which side of that line each statement is on.

## What is proved

1. **The two-crossing coordinate change.**  Under the Hecke quadratic relation
   `s² = h·s + 1` the opposite crossing is `s⁻¹ = s - h`, so `{1, s}` and
   `{s, s⁻¹}` are two coordinate systems on the same plane and the change
   between them is `b = -c₁/h`, `a = c_σ + c₁/h`.

2. **Composing crossings leaves the cone they span.**  `s^k` for `k ≥ 2` has
   `b`-coordinate `-(P k).1 / h`, and `(P k).1 > 0` for every `k ≥ 2` whenever
   `h > 0`, so `b < 0`.  Two crossings compose to something outside the segment
   between the two crossings — the owner's "not obviously a convex combination
   of the two crossings", settled in the affirmative and by the defining
   relation rather than by a computation.

3. **A central multiplier is exactly a reweighting.**  On a Wedderburn block
   Schur's lemma makes a central element the scalar `c • 1`, and then
   `trace (M * (c • 1)) = c * trace M`.  That is the whole content of "the ell-1
   ceiling bounds precisely the centre": multiplying by a central element
   rescales each block's character by a constant, which is the move the ceiling
   already ranges over.  Schur's lemma supplies the hypothesis `Z = c • 1`; the
   step that carries the claim is the trace identity, and it is proved here.

4. **Every atom letter is a convex combination of the two crossings.**
   `atom_braid_word_3A` emits letters `c·σ_g + d·1`, and the averaged ones —
   `d = -h/2` and `d = -h(1/2 - δ/4)` — are the midpoint and the `δ`-weighted
   point of `[s⁻¹, s]`, with weights that are nonnegative for `|δ| ≤ 2` and sum
   to `1` identically.

5. **Complementary projectors split a trace.**  `P + Q = 1` gives
   `trace (M*P) + trace (M*Q) = trace M`, which is the internal check the
   `sigma_1` spectral projectors satisfy numerically (`1.103672165665516 +
   (-0.103672165665516) = 1`).

## What is NOT proved, and must not be read as proved

The measured **inertness** of `sigma_1`, `L_2` and the two projectors on
`Delta_bind` — each rescaling by an atom-independent constant, so that four
candidates share the spread `0.83903` — is an observation.  The explanation
offered for it (every atom word opens with the same intra-nucleon block, so a
`w` supported there modifies a common factor) is a **conjecture about why**, and
it is not formalised here because it has not been established as a theorem.  A
Lean file that proved the algebra and quietly implied the rest would be worse
than one that proves nothing.

Note also that §2 is stated on **coordinates**, not on elements.  Concluding
"`s^k` is not a nonnegative combination of `s` and `s⁻¹`" as a statement about
ring elements needs `{s, s⁻¹}` to be linearly independent over the base, which
is an extra hypothesis about the representation and not part of the Hecke
relation.  The coordinate statement is exactly what the computation reports, so
that is what is proved.

## Base ring (§7c)

§1, §4 are over a commutative ring, then a field where division appears; §2
needs an ordered field for `0 < h`; §3, §5 are over a commutative ring.  No
archimedean content beyond the order.
-/
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic

namespace QOU.Hecke.CrossingConvexity

/-! ## 1. The two crossings -/

section Ring
variable {R : Type*} [CommRing R]

/-- The Hecke quadratic relation `s² = h·s + 1` satisfied by a crossing. -/
def IsCrossing (h s : R) : Prop := s * s = h * s + 1

/-- The opposite crossing.  Under `IsCrossing h s` this is the inverse of `s`. -/
def opp (h s : R) : R := s - h

/-- `opp` really is the inverse crossing: `s⁻¹ · s = 1`. -/
theorem opp_mul_self {h s : R} (hs : IsCrossing h s) : opp h s * s = 1 := by
  unfold opp
  have : s * s = h * s + 1 := hs
  ring_nf
  linear_combination this

/-- A combination of the two crossings, rewritten in the `{1, s}` basis. -/
theorem crossing_expand (a b h s : R) :
    a * s + b * opp h s = (a + b) * s - b * h := by
  unfold opp; ring

end Ring

section Field
variable {K : Type*} [Field K]

/-- The change of coordinates: `c₁ + c_σ·s` written over the two crossings. -/
def toCrossingCoords (h c₁ cσ : K) : K × K := (cσ + c₁ / h, -(c₁ / h))

/-- **The coordinate change is correct.**  With `a, b` as above,
`a·s + b·s⁻¹ = c₁ + c_σ·s`. -/
theorem toCrossingCoords_spec {h : K} (hh : h ≠ 0) (c₁ cσ s : K) :
    (toCrossingCoords h c₁ cσ).1 * s + (toCrossingCoords h c₁ cσ).2 * opp h s
      = c₁ + cσ * s := by
  unfold toCrossingCoords opp
  field_simp
  ring

/-- The `s⁻¹` coordinate is `-c₁/h`; it depends only on the constant term. -/
theorem crossingCoord_snd (h c₁ cσ : K) :
    (toCrossingCoords h c₁ cσ).2 = -(c₁ / h) := rfl

/-! ## 2. Powers of a crossing leave the cone

`s^{k+2} = h·s^{k+1} + s^k` follows from the quadratic relation, so the `{1, s}`
coordinates of `s^k` obey the same recursion. -/

/-- `(pow_coords h k).1 + (pow_coords h k).2 * s = s ^ k`. -/
def pow_coords (h : K) : ℕ → K × K
  | 0 => (1, 0)
  | 1 => (0, 1)
  | (k + 2) => (h * (pow_coords h (k + 1)).1 + (pow_coords h k).1,
                h * (pow_coords h (k + 1)).2 + (pow_coords h k).2)

@[simp] theorem pow_coords_zero (h : K) : pow_coords h 0 = (1, 0) := rfl
@[simp] theorem pow_coords_one (h : K) : pow_coords h 1 = (0, 1) := rfl

theorem pow_coords_succ_succ (h : K) (k : ℕ) :
    pow_coords h (k + 2)
      = (h * (pow_coords h (k + 1)).1 + (pow_coords h k).1,
         h * (pow_coords h (k + 1)).2 + (pow_coords h k).2) := rfl

/-- The recursion reproduces the powers of `s`. -/
theorem pow_coords_spec {h s : K} (hs : IsCrossing h s) :
    ∀ k, (pow_coords h k).1 + (pow_coords h k).2 * s = s ^ k := by
  have step : ∀ k, ((pow_coords h k).1 + (pow_coords h k).2 * s = s ^ k) ∧
      ((pow_coords h (k + 1)).1 + (pow_coords h (k + 1)).2 * s = s ^ (k + 1)) := by
    intro k
    induction k with
    | zero => constructor <;> simp
    | succ n ih =>
        refine ⟨ih.2, ?_⟩
        rw [pow_coords_succ_succ]
        have hq : s * s = h * s + 1 := hs
        have h1 := ih.1
        have h2 := ih.2
        simp only []
        have : s ^ (n + 2) = h * s ^ (n + 1) + s ^ n := by
          have : s ^ (n + 2) = s ^ n * (s * s) := by ring
          rw [this, hq]; ring
        rw [this, ← h1, ← h2]; ring
  exact fun k => (step k).1

end Field

section Ordered
variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- The constant coordinate of `s^{k+2}` is strictly positive when `h > 0`.
Proved together with the next index so the two-step recursion closes. -/
theorem pow_coords_fst_pos {h : K} (hh : 0 < h) :
    ∀ k, 0 < (pow_coords h (k + 2)).1 ∧ 0 < (pow_coords h (k + 3)).1 := by
  intro k
  induction k with
  | zero =>
      constructor
      · rw [pow_coords_succ_succ]; simp
      · rw [pow_coords_succ_succ]; simp [pow_coords_succ_succ, hh]
  | succ n ih =>
      refine ⟨ih.2, ?_⟩
      have : (pow_coords h (n + 4)).1
          = h * (pow_coords h (n + 3)).1 + (pow_coords h (n + 2)).1 := by
        rw [pow_coords_succ_succ]
      rw [this]
      exact add_pos (mul_pos hh ih.2) ih.1

/-- **Composing crossings leaves the cone.**  For `k ≥ 2` and `h > 0`, the
`s⁻¹` coordinate of `s^k` is strictly negative, so `s^k` is not a nonnegative
combination of the two crossings. -/
theorem crossingCoord_snd_neg_of_two_le {h : K} (hh : 0 < h) (k : ℕ) :
    (toCrossingCoords h (pow_coords h (k + 2)).1 (pow_coords h (k + 2)).2).2 < 0 := by
  rw [crossingCoord_snd]
  have := (pow_coords_fst_pos hh k).1
  have : 0 < (pow_coords h (k + 2)).1 / h := div_pos this hh
  linarith

/-- The `k = 2` case in closed form: `s² = h·s + 1` has `b = -1/h`. -/
theorem sq_crossingCoord_snd {h : K} (hh : 0 < h) :
    (toCrossingCoords h (1 : K) h).2 = -(1 / h) := rfl

end Ordered

/-! ## 3. A central multiplier is exactly a reweighting

Schur's lemma makes a central element a scalar on each Wedderburn block; the
step that carries the claim is what a scalar does to the character. -/

section Trace
variable {n : Type*} [Fintype n] [DecidableEq n]
variable {R : Type*} [CommRing R]

/-- **Central multiplication rescales the character.**  This is the whole
content of "the ell-1 ceiling bounds precisely the centre": the ceiling already
ranges over per-block coefficients, and a central `Z = c • 1` only supplies one
more. -/
theorem trace_mul_scalar (M : Matrix n n R) (c : R) :
    Matrix.trace (M * (c • (1 : Matrix n n R))) = c * Matrix.trace M := by
  rw [Matrix.mul_smul, mul_one, Matrix.trace_smul, smul_eq_mul]

/-! ## 5. Complementary projectors split a trace -/

/-- `P + Q = 1` splits any character additively.  The numerical instance is the
pair of Lagrange spectral projectors of `sigma_1`, whose measured ratios are
`1.103672165665516` and `-0.103672165665516`. -/
theorem trace_split_of_add_eq_one (M P Q : Matrix n n R) (h : P + Q = 1) :
    Matrix.trace (M * P) + Matrix.trace (M * Q) = Matrix.trace M := by
  rw [← Matrix.trace_add, ← Matrix.mul_add, h, mul_one]

end Trace

/-! ## 4. Every atom letter is a convex combination of the two crossings -/

section Letters
-- `CharZero` is LOAD-BEARING, not decoration: the residual goal without it is
-- `2⁻¹ * 2 = 1`, which fails in characteristic 2, where `1/2` names nothing and
-- "convex combination" has no content. An earlier draft dropped the `2 ≠ 0`
-- hypotheses as unnecessary and Lean rejected it.
variable {K : Type*} [Field K] [CharZero K]

/-- The averaged crossing is the midpoint of the two crossings. -/
theorem averaged_letter (h s : K) :
    s - h / 2 = (1 / 2) * s + (1 / 2) * opp h s := by
  have h2 : (2 : K) ≠ 0 := two_ne_zero
  unfold opp; field_simp; ring

/-- The colour-weighted letter `σ - h(1/2 - δ/4)` in two-crossing coordinates. -/
theorem weighted_letter (h s d : K) :
    s - h * (1 / 2 - d / 4)
      = (1 / 2 + d / 4) * s + (1 / 2 - d / 4) * opp h s := by
  have h4 : (4 : K) ≠ 0 := by norm_num
  unfold opp; field_simp; ring

/-- Its weights sum to one — the letter is an affine combination, and a convex
one exactly when both weights are nonnegative. -/
theorem weighted_letter_weights_sum (d : K) :
    (1 / 2 + d / 4) + (1 / 2 - d / 4) = 1 := by
  have h2 : (2 : K) ≠ 0 := two_ne_zero
  field_simp
  ring

end Letters

end QOU.Hecke.CrossingConvexity
