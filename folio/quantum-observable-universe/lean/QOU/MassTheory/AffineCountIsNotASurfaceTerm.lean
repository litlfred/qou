/-
# An affine crossing count cannot supply a surface term

The framework's canonical braid closure for an N=Z nucleus has, measured on
A = 2, 4, 6, 8, 12, 16, exactly `12 * A - 1` crossings — equivalently
`4 * n_strands - 1`, since `n_strands = 3 * A`. The construction places a fixed
number of crossings on each strand, so the count is **affine in A**.

Yekutieli's non-abelian Stokes construction splits its convergence estimate into
a bulk term counted by 2-cells and a correction counted by the singular locus,
so "the surface term is proportional to a singularity count" is the natural
reading. This file records why the braid's crossing count cannot be that count:
a surface term scales as `A ^ (2/3)`, and no constant multiple of an affine
function does.

The clean invariant, in the cube variable `m = A ^ (1/3)` (so `A = m ^ 3` and
`A ^ (2/3) = m ^ 2`):

    ratio m = (12 * m ^ 3 - 1) / m ^ 2 = 12 * m - m⁻²

which is **strictly monotone** on `m > 0`. A strictly monotone function is
injective, so it is constant on no two distinct points — hence there is no
single `c` with `12 * A - 1 = c * A ^ (2/3)` at even two mass numbers, let alone
the six measured.

This licenses a scope-**(b)** exclusion for the specific form "crossing count
times a constant", by a proved invariant rather than by a numerical miss. It
does **not** exclude crossings from playing some other role in a closure; that
weaker statement stays scope-(a).

No `sorry`.
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp

namespace QOU.Mass.AffineCountIsNotASurfaceTerm

open Real

/-- The measured canonical-braid crossing count, as a function of mass number. -/
def crossingCount (A : ℕ) : ℤ := 12 * (A : ℤ) - 1

/-- `n_strands = 3 * A`, so the count is `4 * n_strands - 1`. -/
theorem crossingCount_eq_four_mul_strands (A : ℕ) :
    crossingCount A = 4 * (3 * (A : ℤ)) - 1 := by
  unfold crossingCount; ring

/-- The crossing count in the cube variable: `A = m ^ 3`. -/
noncomputable def countOfCube (m : ℝ) : ℝ := 12 * m ^ 3 - 1

/-- A surface term in the cube variable: `A ^ (2/3) = m ^ 2`. -/
noncomputable def surfaceOfCube (m : ℝ) : ℝ := m ^ 2

/-- The ratio of the count to a surface term, in the cube variable. -/
noncomputable def ratio (m : ℝ) : ℝ := 12 * m - 1 / m ^ 2

/-- On `m > 0` the ratio really is count / surface. -/
theorem ratio_eq (m : ℝ) (hm : 0 < m) :
    ratio m = countOfCube m / surfaceOfCube m := by
  unfold ratio countOfCube surfaceOfCube
  field_simp

/-- **The ratio is strictly monotone on the positives.** Both `12 * m` and
`-m⁻²` increase, so their sum does. -/
theorem ratio_strictMono {m₁ m₂ : ℝ} (h1 : 0 < m₁) (h : m₁ < m₂) :
    ratio m₁ < ratio m₂ := by
  have h2 : 0 < m₂ := h1.trans h
  have hsq : m₁ ^ 2 < m₂ ^ 2 := by nlinarith
  have hinv : 1 / m₂ ^ 2 < 1 / m₁ ^ 2 :=
    one_div_lt_one_div_of_lt (by positivity) hsq
  unfold ratio
  linarith

/-- **The exclusion.** No single constant `c` makes the affine count equal a
surface term at two distinct positive mass numbers. -/
theorem no_constant_surface_coefficient {m₁ m₂ c : ℝ}
    (h1 : 0 < m₁) (h : m₁ < m₂)
    (e1 : countOfCube m₁ = c * surfaceOfCube m₁)
    (e2 : countOfCube m₂ = c * surfaceOfCube m₂) : False := by
  have h2 : 0 < m₂ := h1.trans h
  have s1 : surfaceOfCube m₁ ≠ 0 := by unfold surfaceOfCube; positivity
  have s2 : surfaceOfCube m₂ ≠ 0 := by unfold surfaceOfCube; positivity
  have r1 : ratio m₁ = c := by
    rw [ratio_eq m₁ h1, e1]; field_simp
  have r2 : ratio m₂ = c := by
    rw [ratio_eq m₂ h2, e2]; field_simp
  have := ratio_strictMono h1 h
  rw [r1, r2] at this
  exact lt_irrefl c this

end QOU.Mass.AffineCountIsNotASurfaceTerm
