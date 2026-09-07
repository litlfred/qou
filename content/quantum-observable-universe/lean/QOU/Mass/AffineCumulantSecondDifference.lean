/-
# An affine count multiplicity has vanishing second difference — the exclusion is parameter-free

`QOU.Mass.AffineCountMultiplicityWindow` studies the ansatz that the count
multiplicity is affine, `μ(A) = α·A + β`, and proves the exact cumulant
`b₃ = −(3α + 2β)` with the `A`-dependence cancelling.  That file establishes what
the ansatz *implies*.  This file supplies the invariant that lets it be *tested*,
and the test is passed to data by `affine_count_multiplicity_refuted_probe.py`,
where it fails.

## The invariant

Write the binding in the binomial (Möbius) basis, `B(A) = Σ_k μ_k C(A,k)`, with
the corpus convention `B 0 = B 1 = 0` (`CoordinationWeightDifferences.b3`, `b4`).
Under the affine ansatz the `k`-th coefficient has the closed form

    μ_k = (-1)^k * (k * (α + β) - β)

so the **signed** coefficient `(-1)^k μ_k` is an *affine function of k*, for every
`(α, β)`.  Hence its second difference vanishes identically — and `α` and `β`
cancel before any datum is touched.

That is what makes the resulting exclusion **parameter-free**: there is nothing
to tune and nothing to select, so it is the opposite of the
selection-against-the-target the NO-FITTING directive bans.

## What is proved here, and what is not

Proved: the closed form agrees with the corpus's own Möbius definitions at
`k = 2, 3, 4, 5`; the signed coefficient is affine in `k`; its second difference
is identically zero; and the contrapositive — a single non-zero second difference
refutes the whole affine class.

Not proved here, because it is a measurement rather than a theorem: that the
AME2020 second differences *are* non-zero.  They are `+14.32039`, `+35.86614`,
`+63.81021`, `+96.77193` — four of four, monotonically growing — computed in
exact rational arithmetic by the probe named above from the coefficients recorded
in `QOU.Mass.JetFiltrationSignObstruction`.

## Scope

Scope-**(b)**, a structural exclusion, and legitimately so: the required invariant
is *proved* (`secondDiff_signedCumulant_eq_zero`) rather than searched for.

It excludes the **affine class only**.  It says nothing about count
multiplicities in general, nothing about the coordination picture `z = A − 1`,
and nothing about the binding gap's extensive term beyond removing one candidate
shape.

Stated over an arbitrary commutative ring: no ordering and no division are used
(§7c).
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Nat.Cast.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Push

namespace QOU.Mass.AffineCumulantSecondDifference

variable {R : Type*} [CommRing R]

/-- The affine count multiplicity `μ(A) = α·A + β`, matching
`AffineCountMultiplicityWindow.mu`. -/
def bind (α β : R) (A : ℕ) : R := α * A + β

/-- The **signed** binomial-basis coefficient, `(-1)^k μ_k`, under the affine ansatz.
The claim of this file is that *this* is the affine object. -/
def signedCumulant (α β : R) (k : ℕ) : R := (k : R) * (α + β) - β

/-- The binomial-basis coefficient itself, `μ_k = (-1)^k · signedCumulant`. -/
def cumulant (α β : R) (k : ℕ) : R := (-1) ^ k * signedCumulant α β k

/-! ## The closed form agrees with the corpus's Möbius definitions -/

/-- `μ₂ = B(2)` — matches `CoordinationWeightDifferences` with `B 0 = B 1 = 0`. -/
theorem cumulant_two (α β : R) : cumulant α β 2 = bind α β 2 := by
  unfold cumulant signedCumulant bind; push_cast; ring

/-- `μ₃ = B(3) − 3·B(2)`, and this equals `−(3α + 2β)` — the value
`AffineCountMultiplicityWindow.b3_affine_eq` proves independently. -/
theorem cumulant_three (α β : R) :
    cumulant α β 3 = bind α β 3 - 3 * bind α β 2 := by
  unfold cumulant signedCumulant bind; push_cast; ring

theorem cumulant_three_eq_neg (α β : R) : cumulant α β 3 = -(3 * α + 2 * β) := by
  unfold cumulant signedCumulant; push_cast; ring

/-- `μ₄ = B(4) − 4·B(3) + 6·B(2)` — matches `CoordinationWeightDifferences.b4`. -/
theorem cumulant_four (α β : R) :
    cumulant α β 4 = bind α β 4 - 4 * bind α β 3 + 6 * bind α β 2 := by
  unfold cumulant signedCumulant bind; push_cast; ring

/-- `μ₅ = B(5) − 5·B(4) + 10·B(3) − 10·B(2)`. -/
theorem cumulant_five (α β : R) :
    cumulant α β 5 = bind α β 5 - 5 * bind α β 4 + 10 * bind α β 3 - 10 * bind α β 2 := by
  unfold cumulant signedCumulant bind; push_cast; ring

/-! ## The invariant, and the exclusion it powers -/

/-- **The signed coefficient is affine in `k`** — the content of the whole file,
stated as a one-step difference that does not depend on `k`. -/
theorem signedCumulant_succ_sub (α β : R) (k : ℕ) :
    signedCumulant α β (k + 1) - signedCumulant α β k = α + β := by
  unfold signedCumulant; push_cast; ring

/-- **The second difference vanishes identically, for every `(α, β)`.**

This is the invariant the exclusion rests on, and it is why the test is
parameter-free: `α` and `β` have cancelled before any measured value is used. -/
theorem secondDiff_signedCumulant_eq_zero (α β : R) (k : ℕ) :
    signedCumulant α β (k + 2) - 2 * signedCumulant α β (k + 1) + signedCumulant α β k = 0 := by
  unfold signedCumulant; push_cast; ring

/-- **The contrapositive: one non-zero second difference refutes the entire affine
class.**

`s` is the observed signed-coefficient sequence.  If any single second difference
of it is non-zero, then no `(α, β)` whatsoever generates it — so the exclusion
needs no fit, and no search over parameters. -/
theorem not_affine_of_secondDiff_ne_zero {s : ℕ → R} {k : ℕ}
    (h : s (k + 2) - 2 * s (k + 1) + s k ≠ 0) :
    ¬ ∃ α β : R, ∀ n, s n = signedCumulant α β n := by
  rintro ⟨α, β, hs⟩
  exact h (by rw [hs, hs, hs]; exact secondDiff_signedCumulant_eq_zero α β k)

/-- The same statement for the unsigned coefficients, since that is the form the
measured table is quoted in: `μ_k` alternates, and it is `(-1)^k μ_k` whose second
difference must vanish. -/
theorem signedCumulant_eq_neg_one_pow_mul_cumulant (α β : R) (k : ℕ) :
    ((-1 : R)) ^ k * cumulant α β k = signedCumulant α β k := by
  unfold cumulant
  rw [← mul_assoc, ← mul_pow]
  simp

end QOU.Mass.AffineCumulantSecondDifference
