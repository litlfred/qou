import Mathlib.Tactic

/-!
# "A linear term minus a concave deficit" is convexity restated, not a narrowing

`QOU.MassTheory.AggregatorConvexityDichotomy` narrowed the many-body binding
magnitude to **convex-through-the-origin** aggregators `Φ` in `B(A) = Φ(m_A·g)`:
the measured `b₃ = +1.4262225 > 0` excludes every concave-through-the-origin `Φ`
for every bond weight and every bond set, and AME's own `Φ` is convex on the
light-nucleus grid.

`QOU.MassTheory.AggregatorFamilyExclusions` then excluded, with nothing fitted,
five **fixed** correction shapes in the two-parameter family `Φ = c·x + a·ψ(x)`
— among them the semi-empirical volume-minus-surface member `c·x − a·x^{2/3}`.

A follow-up was proposed off the back of that: excluding the whole
*linear-minus-concave-deficit class* `Φ(x) = c·x − a·ψ(x)`, `ψ` concave, by
showing its local exponent must **decrease** while the measured one increases.

**This file shows that route is not merely unproved — it cannot succeed**, and
the obstruction is not analytic but definitional.

## The content

On a three-point grid through the origin, write the three secant slopes
`s₀ = f₁/x₁`, `s₁ = (f₂−f₁)/(x₂−x₁)`, `s₂ = (f₃−f₂)/(x₃−x₂)`. Convexity through
the origin is `s₀ ≤ s₁ ≤ s₂`; concavity is the reverse chain.

Subtracting the data from a linear function negates every slope
(`deficit_secant₀`, `deficit_secant₁`, `deficit_secant₂`: the deficit's slopes
are `c − sⱼ`). Hence:

* `deficit_concave_iff_convex` — the deficit `ψ := c·x − Φ` is concave through
  the origin **iff** `Φ` is convex through the origin, for *every* `c`;
* `deficit_increasing_of_gt_secant₂` — and `ψ` is strictly increasing as soon as
  `c` exceeds the largest secant slope.

So `exists_concaveDeficit_of_convex`: **every** convex-through-the-origin
dataset is exactly `c·x − ψ(x)` for a strictly increasing concave-through-the-
origin `ψ`, for every `c` above its top slope — an open ray of witnesses, not a
lucky one. `concaveDeficit_class_not_excludable` states the consequence in the
form the follow-up needs: no three-point test can exclude the class, because
membership *follows from* the convexity the same three points establish.

## Why this does not contradict the determinant exclusions

`AggregatorFamilyExclusions.not_realizable_of_det3_ne_zero` excludes a
**two-parameter family with `ψ` fixed in advance**: three points, two parameters,
one residual. Here `ψ` is a free *shape* — chosen after the data — so the family
has as many parameters as the grid has points and there is no residual left to
fail. The five shape exclusions are about parameter counting; they say nothing
about the concave-deficit *structure*, and this file says the structure is
vacuous as a constraint.

`ame_grid_is_convex` pins the antecedent on the corpus's own numbers, and
`ame_grid_has_concave_deficit` exhibits a concrete witness at `c = 7`, so the
statement is not vacuously true here.

## What this does NOT establish

* It says nothing about whether any **particular** `ψ` is right — only that
  "concave deficit" is not a filter. A fixed shape is still testable by `det3`.
* It does not refute the proposed monotone-exponent claim as a statement about
  `ψ(x) = x^s`, where it is true. It shows that no such claim can generalise to
  the class, since the class contains the data itself.
* Three points are three points: this is a statement about what a three-point
  grid can decide, and the standing recommendation to extend the grid past
  `A = 4` is what would change it.

Base ring: generic `[Field R] [LinearOrder R] [IsStrictOrderedRing R]` (§7c) —
no archimedean construct is used.
-/

namespace QOU.MassTheory.ConcaveDeficitNonExclusion

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- Three data points on a positive, strictly increasing grid, read together
with the origin. `f` is the value; the grid `x` is shared by everything built
from it. -/
structure GridData (R : Type*) [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    where
  x₁ : R
  x₂ : R
  x₃ : R
  f₁ : R
  f₂ : R
  f₃ : R
  hx₁ : 0 < x₁
  hx₁₂ : x₁ < x₂
  hx₂₃ : x₂ < x₃

namespace GridData

variable (d : GridData R)

/-- Secant slope from the origin to the first point. -/
def secant₀ : R := d.f₁ / d.x₁

/-- Secant slope across the first interval. -/
def secant₁ : R := (d.f₂ - d.f₁) / (d.x₂ - d.x₁)

/-- Secant slope across the second interval. -/
def secant₂ : R := (d.f₃ - d.f₂) / (d.x₃ - d.x₂)

/-- Convex through the origin: the three secant slopes increase. -/
def ConvexThroughOrigin : Prop := d.secant₀ ≤ d.secant₁ ∧ d.secant₁ ≤ d.secant₂

/-- Concave through the origin: the three secant slopes decrease. -/
def ConcaveThroughOrigin : Prop := d.secant₁ ≤ d.secant₀ ∧ d.secant₂ ≤ d.secant₁

/-- Strictly increasing through the origin, in the secant sense. -/
def IncreasingThroughOrigin : Prop := 0 < d.secant₂ ∧ 0 < d.secant₁ ∧ 0 < d.secant₀

/-- The deficit of `d` against the linear function `c·x`: same grid, values
`c·xᵢ − fᵢ`. This is the `ψ` of `Φ(x) = c·x − ψ(x)`. -/
def deficit (c : R) : GridData R where
  x₁ := d.x₁
  x₂ := d.x₂
  x₃ := d.x₃
  f₁ := c * d.x₁ - d.f₁
  f₂ := c * d.x₂ - d.f₂
  f₃ := c * d.x₃ - d.f₃
  hx₁ := d.hx₁
  hx₁₂ := d.hx₁₂
  hx₂₃ := d.hx₂₃

end GridData

open GridData

theorem deficit_secant₀ (d : GridData R) (c : R) :
    (d.deficit c).secant₀ = c - d.secant₀ := by
  have hx : d.x₁ ≠ 0 := ne_of_gt d.hx₁
  simp only [GridData.deficit, GridData.secant₀]
  field_simp

theorem deficit_secant₁ (d : GridData R) (c : R) :
    (d.deficit c).secant₁ = c - d.secant₁ := by
  have hx : d.x₂ - d.x₁ ≠ 0 := sub_ne_zero_of_ne (ne_of_gt d.hx₁₂)
  simp only [GridData.deficit, GridData.secant₁]
  field_simp
  all_goals ring

theorem deficit_secant₂ (d : GridData R) (c : R) :
    (d.deficit c).secant₂ = c - d.secant₂ := by
  have hx : d.x₃ - d.x₂ ≠ 0 := sub_ne_zero_of_ne (ne_of_gt d.hx₂₃)
  simp only [GridData.deficit, GridData.secant₂]
  field_simp
  all_goals ring

/-- **Subtracting from a line exchanges convexity for concavity, exactly.**
The deficit is concave through the origin iff the data is convex through the
origin — for every `c`, with no hypothesis on `c` at all. -/
theorem deficit_concave_iff_convex (d : GridData R) (c : R) :
    (d.deficit c).ConcaveThroughOrigin ↔ d.ConvexThroughOrigin := by
  simp only [GridData.ConcaveThroughOrigin, GridData.ConvexThroughOrigin,
    deficit_secant₀, deficit_secant₁, deficit_secant₂, sub_le_sub_iff_left]

/-- The deficit is strictly increasing as soon as `c` clears the largest secant
slope of the data. -/
theorem deficit_increasing_of_gt_secant₂ (d : GridData R) (c : R)
    (hconv : d.ConvexThroughOrigin) (hc : d.secant₂ < c) :
    (d.deficit c).IncreasingThroughOrigin := by
  obtain ⟨h01, h12⟩ := hconv
  refine ⟨?_, ?_, ?_⟩
  · rw [deficit_secant₂]; linarith
  · rw [deficit_secant₁]; linarith
  · rw [deficit_secant₀]; linarith

/-- **The main statement.** Every convex-through-the-origin dataset *is* a
linear term minus a strictly increasing concave-through-the-origin deficit —
and not for one lucky slope but for every `c` above its top secant slope. The
reconstruction identity `fᵢ = c·xᵢ − ψᵢ` is definitional. -/
theorem exists_concaveDeficit_of_convex (d : GridData R)
    (hconv : d.ConvexThroughOrigin) (c : R) (hc : d.secant₂ < c) :
    (d.deficit c).ConcaveThroughOrigin ∧
      (d.deficit c).IncreasingThroughOrigin ∧
      d.f₁ = c * d.x₁ - (d.deficit c).f₁ ∧
      d.f₂ = c * d.x₂ - (d.deficit c).f₂ ∧
      d.f₃ = c * d.x₃ - (d.deficit c).f₃ :=
  ⟨(deficit_concave_iff_convex d c).mpr hconv,
   deficit_increasing_of_gt_secant₂ d c hconv hc,
   by simp [GridData.deficit], by simp [GridData.deficit],
   by simp [GridData.deficit]⟩

/-- **The consequence for the proposed exclusion.** There is no three-point test
that rules out the linear-minus-concave-deficit class, because membership in the
class *follows from* convexity — the very property the same three points are
used to establish. Stated as: the class-membership predicate is implied by the
antecedent, so it cannot be false on a convex dataset. -/
theorem concaveDeficit_class_not_excludable (d : GridData R)
    (hconv : d.ConvexThroughOrigin) :
    ∀ c : R, d.secant₂ < c →
      (d.deficit c).ConcaveThroughOrigin ∧ (d.deficit c).IncreasingThroughOrigin :=
  fun c hc => ⟨(deficit_concave_iff_convex d c).mpr hconv,
    deficit_increasing_of_gt_secant₂ d c hconv hc⟩

/-- The AME2020 light-nucleus grid, bond-count reading: bond counts `1, 3, 6`
against `B(D)`, the isospin-averaged `B(A=3)`, and `B(⁴He)` in MeV. Exact
rationals, no fit, no `q₀`. -/
def ameGrid : GridData ℚ where
  x₁ := 1
  x₂ := 3
  x₃ := 6
  f₁ := 2224566 / 1000000
  f₂ := 80999205 / 10000000
  f₃ := 28295673 / 1000000
  hx₁ := by norm_num
  hx₁₂ := by norm_num
  hx₂₃ := by norm_num

/-- The AME grid is convex through the origin: secant slopes
`2.224566 → 2.93767725 → 6.7319175`. -/
theorem ame_grid_is_convex : ameGrid.ConvexThroughOrigin := by
  constructor <;>
    · simp only [GridData.secant₀, GridData.secant₁, GridData.secant₂, ameGrid]
      norm_num

/-- So the AME grid itself carries a concave deficit — at `c = 7`, just above its
top secant slope `6.7319175`. The antecedent of the main theorem is inhabited on
the corpus's own numbers, so nothing above is vacuous. -/
theorem ame_grid_has_concave_deficit :
    (ameGrid.deficit 7).ConcaveThroughOrigin ∧
      (ameGrid.deficit 7).IncreasingThroughOrigin :=
  concaveDeficit_class_not_excludable ameGrid ame_grid_is_convex 7 (by
    simp only [GridData.secant₂, ameGrid]; norm_num)


/-! ## The same statement on an arbitrary grid

The three-point version above matches the corpus's grid. Nothing in it depends on
there being three points, and that matters for what to do next: the natural
reading of the result is "get a fourth data point and the class becomes
testable", and **that reading is wrong**. The equivalence below is uniform in the
number of grid points, so no amount of extra data can exclude the class.

Index a grid by `Fin (n+1)` with `x 0 = 0`, `f 0 = 0` if the origin is wanted —
the statements do not need that hypothesis, since the origin is just index `0`.
-/

/-- Secant slope of `f` across the `i`-th grid interval. -/
def slope {n : ℕ} (x f : Fin (n + 1) → R) (i : Fin n) : R :=
  (f i.succ - f i.castSucc) / (x i.succ - x i.castSucc)

/-- The deficit of `f` against the line `c·x`, on an arbitrary grid. -/
def deficitFun {n : ℕ} (x f : Fin (n + 1) → R) (c : R) : Fin (n + 1) → R :=
  fun j => c * x j - f j

omit [IsStrictOrderedRing R] in
theorem slope_deficitFun {n : ℕ} (x f : Fin (n + 1) → R) (c : R)
    (hx : ∀ i : Fin n, x i.castSucc < x i.succ) (i : Fin n) :
    slope x (deficitFun x f c) i = c - slope x f i := by
  have h : x i.succ - x i.castSucc ≠ 0 := sub_ne_zero_of_ne (ne_of_gt (hx i))
  simp only [slope, deficitFun]
  field_simp
  ring

/-- **Uniform in the grid size.** The deficit's slopes are antitone — the
discrete concavity of `ψ` — exactly when the data's slopes are monotone, its
discrete convexity. No hypothesis on `c`, and no dependence on `n`. -/
theorem deficitFun_antitone_iff_monotone {n : ℕ} (x f : Fin (n + 1) → R) (c : R)
    (hx : ∀ i : Fin n, x i.castSucc < x i.succ) :
    Antitone (slope x (deficitFun x f c)) ↔ Monotone (slope x f) := by
  constructor
  · intro h a b hab
    have hba := h hab
    rw [slope_deficitFun x f c hx, slope_deficitFun x f c hx] at hba
    linarith
  · intro h a b hab
    have hab' := h hab
    rw [slope_deficitFun x f c hx, slope_deficitFun x f c hx]
    linarith

/-- The deficit is increasing on every interval exactly when `c` clears every
secant slope of the data. -/
theorem deficitFun_slopes_pos_iff {n : ℕ} (x f : Fin (n + 1) → R) (c : R)
    (hx : ∀ i : Fin n, x i.castSucc < x i.succ) :
    (∀ i, 0 < slope x (deficitFun x f c) i) ↔ (∀ i, slope x f i < c) := by
  constructor <;> intro h i <;> have := h i <;>
    rw [slope_deficitFun x f c hx] at * <;> linarith [h i]

/-- **Extra data points do not help.** On a grid of any size, every
discretely-convex dataset whose slopes are bounded by `c` is a linear term minus
a discretely-concave, increasing deficit. So the linear-minus-concave-deficit
class is not excludable by *any* finite grid, and the standing recommendation to
extend past `A = 4` buys the ability to test **fixed shapes** and to locate the
convex→concave turn — not the ability to test this class. -/
theorem concaveDeficit_not_excludable_on_any_grid {n : ℕ}
    (x f : Fin (n + 1) → R) (c : R)
    (hx : ∀ i : Fin n, x i.castSucc < x i.succ)
    (hconv : Monotone (slope x f)) (hc : ∀ i, slope x f i < c) :
    Antitone (slope x (deficitFun x f c)) ∧
      (∀ i, 0 < slope x (deficitFun x f c) i) ∧
      (∀ j, f j = c * x j - deficitFun x f c j) :=
  ⟨(deficitFun_antitone_iff_monotone x f c hx).mpr hconv,
   (deficitFun_slopes_pos_iff x f c hx).mpr hc,
   fun j => by simp [deficitFun]⟩

end QOU.MassTheory.ConcaveDeficitNonExclusion
