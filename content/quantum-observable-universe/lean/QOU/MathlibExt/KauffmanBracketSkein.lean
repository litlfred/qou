/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Field.Rat
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# The Kauffman bracket, algebraically

Mathlib has no Kauffman bracket. A case-insensitive search over the vendored
tree (`leanprover/lean4:v4.24.0`, Mathlib commit
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`, 6996 modules) returns **0** files
for each of `Kauffman`, `skein`, `Temperley` and `bracket polynomial`; there is
also no link type, no knot diagram, no Reidemeister move and no writhe. The only
knot-motivated file in Mathlib is `Mathlib/Algebra/Quandle.lean`, in which knots
appear only in prose.

This file supplies the **algebraic skeleton** of the bracket: the three defining
rules, packaged as a structure, together with the consequences that follow from
them by ring arithmetic alone.

## The setting

`R` is any commutative ring and `D` any type, thought of as a type of link
diagrams. A `KauffmanBracketSpec R D` carries

* a variable `A : R` together with a stand-in `Ainv : R` for `A⁻¹` and the
  hypothesis `A * Ainv = 1` — this is what keeps the base ring a bare
  `CommRing`, with no `Field`, no `Inv`, no ordering and no archimedean
  structure anywhere in the file (AGENTS.md §7c);
* a function `bracket : D → R`;
* a distinguished `unknot : D` and an operation `addCircle : D → D`;
* a relation `Smoothing : D → D → D → Prop`, where `Smoothing d d₀ d₁` is read
  "`d` carries a distinguished crossing whose `A`-smoothing is `d₀` and whose
  `B`-smoothing is `d₁`";

subject to the three Kauffman rules

* **K1** (`skein`) `Smoothing d d₀ d₁ → ⟨d⟩ = A⟨d₀⟩ + A⁻¹⟨d₁⟩`;
* **K2** (`loop`) `⟨addCircle d⟩ = δ⟨d⟩` with `δ = -(A² + A⁻²)`;
* **K3** (`normalisation`) `⟨unknot⟩ = 1`.

## What is a THEOREM here

Everything below is proved from K1–K3; there is no `sorry` and no new axiom.

* `loopValue_sq`, `A_sq_mul_loopValue`, `Ainv_sq_mul_loopValue` — the **defining
  quadratic** of the loop value. `A² δ + A⁴ + 1 = 0` (and its mirror), so `δ` is
  the root of an explicit monic-in-`δ` linear relation over `A`, and
  `δ² = A⁴ + 2 + A⁻⁴`. All three genuinely use `A * Ainv = 1`.
* `bracket_iterate_addCircle`, `bracket_unlink` — the **`k`-circle scaling**:
  adding `n` disjoint trivial circles multiplies the bracket by `δⁿ`, so the
  `(n+1)`-component unlink has bracket `δⁿ`. Proved by induction on `n`.
* `bracket_kink_left`, `bracket_kink_right` — the **writhe-normalisation
  factors.** A crossing whose two smoothings are `d` and `d ⊔ (circle)` has
  bracket `-A⁻³⟨d⟩`; with the roles exchanged, `-A³⟨d⟩`. These are the framing
  factors that force the writhe correction in the Jones normalisation, and they
  are the sharpest consequence of K1–K3 in this file.
* `kinkFactor_mul_kinkFactor_inv`, `bracket_kink_pair` — the two factors are
  mutually inverse, so a positive kink followed by a negative kink returns the
  original bracket.
* `bracket_eq_of_smoothing` — the bracket of a crossing is **determined** by the
  brackets of its two smoothings.
* `bracket_add_mirror`, `bracket_sub_mirror` — a crossing and its mirror satisfy
  `⟨d⟩ + ⟨d'⟩ = (A + A⁻¹)(⟨d₀⟩ + ⟨d₁⟩)` and
  `⟨d⟩ - ⟨d'⟩ = (A - A⁻¹)(⟨d₀⟩ - ⟨d₁⟩)`.
* `unreduced_skein`, `unreduced_loop`, `unreduced_unknot`, `unreduced_unlink` —
  the **reduced-versus-unreduced relationship.** `δ · ⟨-⟩` satisfies K1 and K2
  unchanged and sends the unknot to `δ` rather than to `1`; the `(n+1)`-component
  unlink then has unreduced bracket `δⁿ⁺¹`, i.e. one factor of `δ` per component
  rather than per *added* component.
* `smul_skein`, `smul_loop`, `scale_eq_one_of_normalised` — K1 and K2 are
  **homogeneous** (invariant under rescaling the bracket by any `c : R`), and K3
  is exactly what pins the scale: `c · ⟨unknot⟩ = 1` forces `c = 1`. This is the
  precise sense in which the normalisation is a normalisation.

## What is a HYPOTHESIS or a DEFINITION here

* `KauffmanBracketSpec` is a **specification**, not a construction. Nothing here
  builds a bracket from a diagram; the state sum over smoothings is not
  formalised, and no existence theorem over any diagram type is claimed.
* **`D` is an opaque type and `Smoothing` is an abstract relation.** There is no
  planar diagram, no crossing, no smoothing operation and no combinatorics of
  any kind in this file. `Smoothing d d₀ d₁` asserts only that the triple stands
  in some relation; that the relation is realised by resolving a crossing in a
  planar diagram is a *reading imposed from outside*, exactly as in
  `QOU.MathlibExt.SkeinRelation`.
* **No topological invariance is proved, and none is true as stated.** The
  bracket specified here is deliberately *not* a link invariant: `bracket_kink_*`
  shows R1 fails by the factor `-A^{∓3}`, and `exists_kink_bracket_ne` exhibits a
  model in which that failure is visible (`-1/8 ≠ 1` over `ℚ`). Recovering an
  invariant needs the writhe correction, which needs a writhe, which needs a
  diagram — none of which exists here. R2 and R3 invariance are *not* consequences
  of K1–K3 alone over an abstract `Smoothing` relation and are **not** claimed.

## Non-vacuity

A spec with an opaque carrier is worthless unless satisfiable, so:

* `tautological` — a model for **every** `R` and every `A` with `A * Ainv = 1`,
  on the diagram type `D := R` itself, with `bracket = id`. All three rules hold,
  two of them by `rfl`.
* `tautological_smoothing` — its `Smoothing` relation is richly inhabited: every
  pair `(y, z)` is the smoothing pair of some diagram. So K1 is not satisfied
  vacuously by an empty relation, which is the one cheap way this structure could
  have been made trivially consistent.
* `exists_bracket_addCircle_ne` — over `ℚ` at `A = 2` the bracket is **not
  constant**: `⟨unknot ⊔ circle⟩ = -17/4 ≠ 1 = ⟨unknot⟩`. The theorems above are
  therefore not statements about a degenerate model.
* `exists_kink_bracket_ne` — the same model contains a genuine kink, whose
  bracket is `-A⁻³ = -1/8`, confirming `bracket_kink_left` on a witness.

## Relation to the rest of this repository

`QOU.Knots.KauffmanTL3` computes a bracket, but only for the fixed
`5`-dimensional Temperley–Lieb algebra `TL₃` with loop counts hard-coded into the
closure, over a bespoke Laurent-polynomial type, by `decide`. It is a
*computation at `n = 3`*, not a specification, and nothing in it is stated for
general diagrams or a general ring. `QOU.MathlibExt.SkeinFromHecke` treats the
*Hecke* skein relation `L₊ - L₋ = (q - q⁻¹)L₀` at the level of one ring element;
that is the other of the two standard skein calculi and is not the bracket
relation. `QOU.MathlibExt.TemperleyLiebAlgebra` supplies the algebra whose loop
parameter `δ` this file's `loopValue` would specialise to. Imports are
Mathlib-only.

## References

* [kauffman1987] L. H. Kauffman, *State models and the Jones polynomial*,
  Topology 26 (1987), 395–407.
* [kasselTuraev2008] C. Kassel and V. Turaev, *Braid Groups*, GTM 247.
-/

namespace QOU.MathlibExt.KauffmanBracket

variable {R : Type*} [CommRing R]

/-! ## The loop value -/

/-- The **loop value** `δ = -(A² + A⁻²)` of the Kauffman bracket, written with an
explicit stand-in `Ainv` for `A⁻¹` so that the base ring stays a `CommRing`. -/
def loopValue (A Ainv : R) : R := -(A ^ 2 + Ainv ^ 2)

/-- The loop value is symmetric in `A` and `A⁻¹`: the mirror image of a diagram
has the same loop value. -/
theorem loopValue_symm (A Ainv : R) : loopValue A Ainv = loopValue Ainv A := by
  simp only [loopValue]; ring

variable {A Ainv : R}

/-- From `A * A⁻¹ = 1`, the squares are inverse too. -/
theorem sq_mul_sq (h : A * Ainv = 1) : A ^ 2 * Ainv ^ 2 = 1 := by
  linear_combination (A * Ainv + 1) * h

/-- From `A * A⁻¹ = 1`, the cubes are inverse too. -/
theorem cube_mul_cube (h : A * Ainv = 1) : A ^ 3 * Ainv ^ 3 = 1 := by
  linear_combination ((A * Ainv) ^ 2 + A * Ainv + 1) * h

/-- **The defining quadratic of the loop value.** `δ` satisfies
`A²·δ + A⁴ + 1 = 0`; equivalently `δ = -(A⁴ + 1)/A²`. This is a genuine
consequence of `A * Ainv = 1` — it is false for unconstrained `Ainv`. -/
theorem A_sq_mul_loopValue (h : A * Ainv = 1) :
    A ^ 2 * loopValue A Ainv + A ^ 4 + 1 = 0 := by
  simp only [loopValue]
  linear_combination (-(A * Ainv) - 1) * h

/-- The mirror form of `A_sq_mul_loopValue`. -/
theorem Ainv_sq_mul_loopValue (h : A * Ainv = 1) :
    Ainv ^ 2 * loopValue A Ainv + Ainv ^ 4 + 1 = 0 := by
  simp only [loopValue]
  linear_combination (-(A * Ainv) - 1) * h

/-- The square of the loop value, `δ² = A⁴ + 2 + A⁻⁴`. The middle `2` is where
`A * Ainv = 1` is used. -/
theorem loopValue_sq (h : A * Ainv = 1) :
    loopValue A Ainv ^ 2 = A ^ 4 + 2 + Ainv ^ 4 := by
  simp only [loopValue]
  linear_combination (2 * A * Ainv + 2) * h

/-! ## The specification -/

/-- A **Kauffman bracket specification** on a type `D` of diagrams, valued in a
commutative ring `R`.

The three fields `skein`, `loop` and `normalisation` are Kauffman's rules K1, K2
and K3. `D` is opaque and `Smoothing` is an abstract ternary relation: this
structure encodes the *algebra* of the bracket and contains no diagram
combinatorics whatsoever. See the module docstring on what is and is not
claimed. -/
structure KauffmanBracketSpec (R : Type*) [CommRing R] (D : Type*) where
  /-- The bracket variable `A`. -/
  A : R
  /-- A stand-in for `A⁻¹`, kept as a separate scalar so that `R` need only be a
  `CommRing`. -/
  Ainv : R
  /-- `Ainv` really is a two-sided inverse of `A`. -/
  A_mul_Ainv : A * Ainv = 1
  /-- The bracket itself. -/
  bracket : D → R
  /-- The distinguished one-component trivial diagram. -/
  unknot : D
  /-- Adjoin a disjoint trivial circle. -/
  addCircle : D → D
  /-- `Smoothing d d₀ d₁`: `d` carries a distinguished crossing whose
  `A`-smoothing is `d₀` and whose `B`-smoothing is `d₁`. -/
  Smoothing : D → D → D → Prop
  /-- **K1, the bracket skein rule.** -/
  skein : ∀ {d d₀ d₁ : D}, Smoothing d d₀ d₁ →
    bracket d = A * bracket d₀ + Ainv * bracket d₁
  /-- **K2, the loop rule**, with loop value `δ = -(A² + A⁻²)`. -/
  loop : ∀ d : D, bracket (addCircle d) = loopValue A Ainv * bracket d
  /-- **K3, the normalisation.** -/
  normalisation : bracket unknot = 1

namespace KauffmanBracketSpec

variable {D : Type*} (S : KauffmanBracketSpec R D)

/-- The loop value of a specification. -/
def δ : R := loopValue S.A S.Ainv

/-- K2 restated in terms of `S.δ`. This is a notational restatement, true by
unfolding `δ`; the mathematical content is the structure field `loop`. -/
@[simp]
theorem bracket_addCircle (d : D) : S.bracket (S.addCircle d) = S.δ * S.bracket d :=
  S.loop d

/-- The defining quadratic of the loop value, for a specification. -/
theorem A_sq_mul_δ : S.A ^ 2 * S.δ + S.A ^ 4 + 1 = 0 :=
  A_sq_mul_loopValue S.A_mul_Ainv

/-- `δ² = A⁴ + 2 + A⁻⁴`, for a specification. -/
theorem δ_sq : S.δ ^ 2 = S.A ^ 4 + 2 + S.Ainv ^ 4 :=
  loopValue_sq S.A_mul_Ainv

/-! ## The `k`-circle scaling -/

/-- **Adding `n` disjoint trivial circles multiplies the bracket by `δⁿ`.** -/
theorem bracket_iterate_addCircle (n : ℕ) (d : D) :
    S.bracket (S.addCircle^[n] d) = S.δ ^ n * S.bracket d := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [Function.iterate_succ_apply', S.bracket_addCircle, ih]
      ring

/-- Circle counts add: `m` circles on top of `n` circles is `m + n` circles. -/
theorem bracket_iterate_add (m n : ℕ) (d : D) :
    S.bracket (S.addCircle^[m] (S.addCircle^[n] d)) = S.δ ^ (m + n) * S.bracket d := by
  rw [S.bracket_iterate_addCircle, S.bracket_iterate_addCircle]
  ring

/-- **The unlink.** The diagram obtained from the unknot by adjoining `n` trivial
circles — that is, the `(n+1)`-component unlink — has bracket `δⁿ`. -/
theorem bracket_unlink (n : ℕ) :
    S.bracket (S.addCircle^[n] S.unknot) = S.δ ^ n := by
  rw [S.bracket_iterate_addCircle, S.normalisation, mul_one]

/-! ## Crossings -/

variable {S}

/-- The bracket of a crossing is **determined** by the brackets of its two
smoothings: two diagrams with the same smoothing pair have the same bracket. -/
theorem bracket_eq_of_smoothing {d d' d₀ d₁ : D}
    (h : S.Smoothing d d₀ d₁) (h' : S.Smoothing d' d₀ d₁) :
    S.bracket d = S.bracket d' := by
  rw [S.skein h, S.skein h']

/-- A crossing and its **mirror** (the same smoothing pair, in the opposite
order) satisfy `⟨d⟩ + ⟨d'⟩ = (A + A⁻¹)(⟨d₀⟩ + ⟨d₁⟩)`. -/
theorem bracket_add_mirror {d d' d₀ d₁ : D}
    (h : S.Smoothing d d₀ d₁) (h' : S.Smoothing d' d₁ d₀) :
    S.bracket d + S.bracket d' = (S.A + S.Ainv) * (S.bracket d₀ + S.bracket d₁) := by
  rw [S.skein h, S.skein h']; ring

/-- The difference form of `bracket_add_mirror`:
`⟨d⟩ - ⟨d'⟩ = (A - A⁻¹)(⟨d₀⟩ - ⟨d₁⟩)`. -/
theorem bracket_sub_mirror {d d' d₀ d₁ : D}
    (h : S.Smoothing d d₀ d₁) (h' : S.Smoothing d' d₁ d₀) :
    S.bracket d - S.bracket d' = (S.A - S.Ainv) * (S.bracket d₀ - S.bracket d₁) := by
  rw [S.skein h, S.skein h']; ring

/-! ## The writhe-normalisation factors

A curl (a Reidemeister-I kink) is a crossing one of whose smoothings is the
original diagram and the other of which is that diagram with a trivial circle
adjoined. K1 and K2 then force the bracket to change by `-A^{∓3}`. -/

/-- **Positive kink.** If `k` is a crossing whose `A`-smoothing is `d` and whose
`B`-smoothing is `d` with a trivial circle adjoined, then
`⟨k⟩ = -A⁻³ ⟨d⟩`. -/
theorem bracket_kink_left {k d : D} (h : S.Smoothing k d (S.addCircle d)) :
    S.bracket k = -(S.Ainv ^ 3) * S.bracket d := by
  rw [S.skein h, S.bracket_addCircle, δ, loopValue]
  linear_combination (-(S.A * S.bracket d)) * S.A_mul_Ainv

/-- **Negative kink.** With the two smoothings exchanged, `⟨k⟩ = -A³ ⟨d⟩`. -/
theorem bracket_kink_right {k d : D} (h : S.Smoothing k (S.addCircle d) d) :
    S.bracket k = -(S.A ^ 3) * S.bracket d := by
  rw [S.skein h, S.bracket_addCircle, δ, loopValue]
  linear_combination (-(S.Ainv * S.bracket d)) * S.A_mul_Ainv

variable (S)

/-- The two kink factors are mutually inverse. This is why the writhe correction
`(-A³)^{-w}` is well defined: cancelling a positive against a negative curl
returns the original bracket. -/
theorem kinkFactor_mul_kinkFactor_inv :
    (-(S.A ^ 3)) * (-(S.Ainv ^ 3)) = 1 := by
  have := cube_mul_cube S.A_mul_Ainv
  linear_combination this

variable {S}

/-- A positive kink followed by a negative kink restores the bracket. -/
theorem bracket_kink_pair {d k₁ k₂ : D}
    (h₁ : S.Smoothing k₁ d (S.addCircle d))
    (h₂ : S.Smoothing k₂ (S.addCircle k₁) k₁) :
    S.bracket k₂ = S.bracket d := by
  rw [bracket_kink_right h₂, bracket_kink_left h₁, ← mul_assoc,
    kinkFactor_mul_kinkFactor_inv S, one_mul]

/-! ## Homogeneity, and what the normalisation normalises -/

variable (S)

/-- K1 is **homogeneous**: rescaling the bracket by any `c : R` preserves the
skein rule. -/
theorem smul_skein (c : R) {d d₀ d₁ : D} (h : S.Smoothing d d₀ d₁) :
    c * S.bracket d = S.A * (c * S.bracket d₀) + S.Ainv * (c * S.bracket d₁) := by
  rw [S.skein h]; ring

/-- K2 is **homogeneous** as well. -/
theorem smul_loop (c : R) (d : D) :
    c * S.bracket (S.addCircle d) = S.δ * (c * S.bracket d) := by
  rw [S.bracket_addCircle]; ring

/-- K3 is exactly what pins the scale: the only rescaling of a normalised
bracket that is again normalised is the identity. Together with `smul_skein` and
`smul_loop` this says the normalisation is a genuine normalisation — K1 and K2
alone determine the bracket only up to one overall scalar. -/
theorem scale_eq_one_of_normalised {c : R} (hc : c * S.bracket S.unknot = 1) :
    c = 1 := by
  rwa [S.normalisation, mul_one] at hc

/-! ## Reduced versus unreduced

The *unreduced* bracket is the convention in which the unknot evaluates to `δ`
rather than to `1` — that is, one factor of `δ` per component rather than per
component *beyond the first*. -/

/-- The **unreduced bracket** `δ · ⟨-⟩`. -/
def unreduced (d : D) : R := S.δ * S.bracket d

/-- The unreduced bracket obeys the same skein rule K1. -/
theorem unreduced_skein {d d₀ d₁ : D} (h : S.Smoothing d d₀ d₁) :
    S.unreduced d = S.A * S.unreduced d₀ + S.Ainv * S.unreduced d₁ := by
  simp only [unreduced]; rw [S.skein h]; ring

/-- The unreduced bracket obeys the same loop rule K2. -/
theorem unreduced_loop (d : D) :
    S.unreduced (S.addCircle d) = S.δ * S.unreduced d := by
  simp only [unreduced]; rw [S.bracket_addCircle]

/-- **The reduced/unreduced relationship at the unknot**: the normalisation K3 is
where the two conventions differ, and they differ by exactly one factor of `δ`. -/
theorem unreduced_unknot : S.unreduced S.unknot = S.δ := by
  simp only [unreduced]; rw [S.normalisation, mul_one]

/-- The `(n+1)`-component unlink has unreduced bracket `δⁿ⁺¹` — one factor of
`δ` per component — against `δⁿ` for the reduced bracket of `bracket_unlink`. -/
theorem unreduced_unlink (n : ℕ) :
    S.unreduced (S.addCircle^[n] S.unknot) = S.δ ^ (n + 1) := by
  simp only [unreduced]
  rw [S.bracket_unlink]
  ring

end KauffmanBracketSpec

/-! ## Non-vacuity

The rules K1–K3 constrain each other — K1 relates three values, K2 forces a
specific multiplier and K3 fixes an absolute value — so their joint
satisfiability is not automatic and must be exhibited. -/

/-- The **tautological model**: take the diagram type to be `R` itself, with the
bracket the identity. Every one of K1, K2, K3 holds, the last two by `rfl`.

This model exists for every commutative ring `R` and every pair `A`, `Ainv` with
`A * Ainv = 1`, so the specification is consistent in complete generality. -/
def tautological (A Ainv : R) (h : A * Ainv = 1) : KauffmanBracketSpec R R where
  A := A
  Ainv := Ainv
  A_mul_Ainv := h
  bracket := id
  unknot := 1
  addCircle := fun x => loopValue A Ainv * x
  Smoothing := fun x y z => x = A * y + Ainv * z
  skein := fun hd => hd
  loop := fun _ => rfl
  normalisation := rfl

/-- **The smoothing relation of the tautological model is inhabited**, for every
pair `(y, z)`. This matters: a specification whose `Smoothing` relation were
empty would satisfy K1 vacuously, and every theorem above that takes a
`Smoothing` hypothesis would be contentless. It is not. -/
theorem tautological_smoothing (A Ainv : R) (h : A * Ainv = 1) (y z : R) :
    (tautological A Ainv h).Smoothing (A * y + Ainv * z) y z := rfl

/-- **The model is non-degenerate**: over `ℚ` at `A = 2` the bracket is not
constant, since `⟨unknot ⊔ circle⟩ = δ = -17/4 ≠ 1 = ⟨unknot⟩`. So the theorems
above are not statements about a collapsed model in which every diagram has the
same bracket. -/
theorem exists_bracket_addCircle_ne :
    ∃ S : KauffmanBracketSpec ℚ ℚ,
      S.bracket (S.addCircle S.unknot) ≠ S.bracket S.unknot := by
  refine ⟨tautological (2 : ℚ) (1 / 2) (by norm_num), ?_⟩
  show loopValue (2 : ℚ) (1 / 2) * 1 ≠ (1 : ℚ)
  norm_num [loopValue]

/-- **A genuine kink exists, and R1 genuinely fails.** In the tautological model
over `ℚ` at `A = 2` there is a diagram `k` standing in the kink relation to the
unknot; `bracket_kink_left` predicts `⟨k⟩ = -A⁻³ = -1/8`, which is what it is,
and `-1/8 ≠ 1 = ⟨unknot⟩`.

This is the non-vacuity witness for `bracket_kink_left`, and it is also the
concrete reason the bracket specified here is *not* a link invariant: the writhe
correction is exactly what repairs this failure, and it is not formalised in this
file. -/
theorem exists_kink_bracket_ne :
    ∃ (S : KauffmanBracketSpec ℚ ℚ) (k : ℚ),
      S.Smoothing k S.unknot (S.addCircle S.unknot) ∧
      S.bracket k = -(S.Ainv ^ 3) ∧
      S.bracket k ≠ S.bracket S.unknot := by
  refine ⟨tautological (2 : ℚ) (1 / 2) (by norm_num), -(1 / 8), ?_, ?_, ?_⟩
  · show (-(1 / 8) : ℚ) = 2 * 1 + (1 / 2) * (loopValue (2 : ℚ) (1 / 2) * 1)
    norm_num [loopValue]
  · show (-(1 / 8) : ℚ) = -((1 / 2 : ℚ) ^ 3)
    norm_num
  · show (-(1 / 8) : ℚ) ≠ (1 : ℚ)
    norm_num

end QOU.MathlibExt.KauffmanBracket
