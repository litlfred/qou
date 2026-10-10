import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Algebra.Order.Ring.Defs

/-!
# Bond order is not particle count: the Ursell slot alignment

**Why the triple bond difference belongs in the 3-body slot, not the 4-body one.**

The Δ_λ binding programme carries two ladders that look alike and are indexed
differently, and conflating them mis-slots every comparison:

* the **moment ladder** `μ₂, μ₃, μ₄, …` of the residual simplex, indexed by
  **particle count** — `μ_k` is the coefficient of `C(A,k)` in
  `M(A) = ∑_k μ_k · C(A,k)`;
* the **mixed-difference ladder** `Δ¹g, Δ²g, Δ³g, …` of a subset trace, indexed
  by **bond count** — `Δᵐg` is the `m`-th mixed difference over `m` chosen
  interface bonds.

For three particles the bonds `a = 0↔1`, `b = 1↔2`, `c = 0↔2` form a triangle:
three *bonds*, but only three *vertices*. So `Δ³g` — a bond-order-3 object — is
still a **3-body** quantity. It is not a 4-body term, and pairing it against `μ₄`
is an index error. A genuine `μ₄` needs a fourth particle (hence `A = 4`, `H₁₂`,
and `C(4,2) = 6` bonds).

`triangle_moment_decomp` gives the correct assembly: the 3-body moment is the
**sum of all three pair differences plus the triple**, not either piece alone.
`moment_eq_triple_iff` says exactly when the shortcut of reading `Δ³g` as the
moment is legitimate — precisely when the pair differences cancel — and
`moment_pos_of_pairs_dominate` is the measured configuration, in which they do
not: three positive pair differences outweigh a negative triple, so the assembled
moment keeps the pair differences' sign.

The consequence for the programme is a **robustness result, not a new door**: the
sign obstruction found for the pair difference survives the slot correction. It
does not survive it *because* the correction is small — the correction is large
(it roughly doubles the magnitude) — but because the triple enters with the same
sign as the assembled moment demands.

`mu_inversion_three` / `mu_inversion_four` verify, over a generic commutative
ring, that the recursive form used by the residual-simplex compute
(`mu3 = M₃ − 3μ₂`, `mu4 = M₄ − 6μ₂ − 4μ₃`) is the binomial inversion of
`M(A) = ∑ μ_k C(A,k)` at `A = 2,3,4`, and `mu4_closed_form` that it agrees with
the closed alternating form `M₄ − 4M₃ + 6M₂`.

Base ring: **generic** `[CommRing R]` (§7c) for the identities; the sign lemma
adds only an ordering. No `ℝ`, no analysis — these are `ring`-level facts about
inclusion–exclusion.

Companion probe: `computations/deltalambda/ursell_slot_alignment_probe.py`.

**Scope.** These are theorems about the inclusion–exclusion bookkeeping. They do
**not** assert that the block trace `g` is the right operator, nor that its
assembled 3-body moment matches the derived `μ₃`; the probe reports that
comparison separately, and it misses.
-/

namespace QOU.MassTheory.UrsellSlotAlignment

section Decomposition

variable {R : Type*} [CommRing R]

/-- The second mixed difference over two bonds: `Δ²g(x,y) = g_{xy} − g_x − g_y + g_∅`. -/
def pairDiff (e x y xy : R) : R := xy - x - y + e

/-- The triple (Ursell) mixed difference over three bonds. -/
def tripleDiff (e a b c ab ac bc abc : R) : R :=
  abc - ab - ac - bc + a + b + c - e

/-- The 3-body moment of a triangle: total interaction minus the sum of the
single-bond (2-body) pieces, `μ₃ = M₃ − 3μ₂` with `M₃ = g_{abc} − g_∅` and
`μ₂ = g_x − g_∅`. -/
def bodyMoment3 (e a b c abc : R) : R := abc - a - b - c + 2 * e

/-- **The slot-alignment identity.** The 3-body moment of the triangle is the sum
of the three pair differences **plus** the triple difference — neither piece
alone. This is the statement that fixes which measured quantity is the `μ₃`
comparand. -/
theorem triangle_moment_decomp (e a b c ab ac bc abc : R) :
    bodyMoment3 e a b c abc
      = (pairDiff e a b ab + pairDiff e a c ac + pairDiff e b c bc)
        + tripleDiff e a b c ab ac bc abc := by
  simp only [bodyMoment3, pairDiff, tripleDiff]
  ring

/-- **When reading `Δ³g` as the moment is legitimate.** The triple difference
equals the 3-body moment exactly when the three pair differences cancel. Since
they are measured strictly positive (and hence do not cancel), the shortcut is
invalid for this operator. -/
theorem moment_eq_triple_iff (e a b c ab ac bc abc : R) :
    bodyMoment3 e a b c abc = tripleDiff e a b c ab ac bc abc
      ↔ pairDiff e a b ab + pairDiff e a c ac + pairDiff e b c bc = 0 := by
  simp only [bodyMoment3, pairDiff, tripleDiff]
  constructor <;> intro h <;> linear_combination h

/-- Likewise, the single pair difference is the moment only when the other two
pairs and the triple cancel against it — so `Δ²g(a,b)` alone is not the
comparand either. -/
theorem moment_eq_pair_iff (e a b c ab ac bc abc : R) :
    bodyMoment3 e a b c abc = pairDiff e a b ab
      ↔ pairDiff e a c ac + pairDiff e b c bc
          + tripleDiff e a b c ab ac bc abc = 0 := by
  simp only [bodyMoment3, pairDiff, tripleDiff]
  constructor <;> intro h <;> linear_combination h

end Decomposition

section Sign

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **The measured configuration: the sign obstruction survives the slot
correction.** If the triple difference exceeds minus the total of the three pair
differences, the assembled 3-body moment is strictly positive. With the three
pair differences measured positive (total `≈ 1.23`) and the triple measured
`≈ -0.33`, the hypothesis holds comfortably, so the assembled moment carries the
pair differences' sign — correcting the slot from `Δ²g` to `∑Δ²g + Δ³g` cannot
flip the sign verdict.

The decomposition is load-bearing here: the conclusion is about `bodyMoment3`,
which is only connected to the hypothesis through `triangle_moment_decomp`. -/
theorem moment_pos_of_triple_dominated {e a b c ab ac bc abc : R}
    (h : -(pairDiff e a b ab + pairDiff e a c ac + pairDiff e b c bc)
           < tripleDiff e a b c ab ac bc abc) :
    0 < bodyMoment3 e a b c abc := by
  rw [triangle_moment_decomp]
  linarith

/-- The contrapositive, as the programme uses it: to get a **non-positive**
assembled moment, the triple must be at least as large in magnitude as the whole
pair total. A triple that is merely negative does not suffice — which is exactly
why the measured `Δ³g < 0` does not open the sign door. -/
theorem triple_must_dominate_of_moment_nonpos {e a b c ab ac bc abc : R}
    (h : bodyMoment3 e a b c abc ≤ 0) :
    tripleDiff e a b c ab ac bc abc
      ≤ -(pairDiff e a b ab + pairDiff e a c ac + pairDiff e b c bc) := by
  rw [triangle_moment_decomp] at h
  linarith

end Sign

section MomentInversion

variable {R : Type*} [CommRing R]

/-- The residual-simplex ansatz `M(A) = ∑_k μ_k · C(A,k)`, with the binomial
coefficients taken from `Nat.choose` rather than hand-substituted, so that the
combinatorics is part of the statement. -/
def Mval (μ₂ μ₃ μ₄ : R) (A : ℕ) : R :=
  μ₂ * (A.choose 2 : ℕ) + μ₃ * (A.choose 3 : ℕ) + μ₄ * (A.choose 4 : ℕ)

/-- `M(2) = μ₂`: only the edge column is populated at `A = 2`. -/
theorem Mval_two (μ₂ μ₃ μ₄ : R) : Mval μ₂ μ₃ μ₄ 2 = μ₂ := by
  simp [Mval, Nat.choose]

/-- `M(3) = 3μ₂ + μ₃`: `C(3,2) = 3`, `C(3,3) = 1`, `C(3,4) = 0`. -/
theorem Mval_three (μ₂ μ₃ μ₄ : R) : Mval μ₂ μ₃ μ₄ 3 = 3 * μ₂ + μ₃ := by
  simp [Mval, Nat.choose]; ring

/-- `M(4) = 6μ₂ + 4μ₃ + μ₄`: `C(4,2) = 6`, `C(4,3) = 4`, `C(4,4) = 1`. -/
theorem Mval_four (μ₂ μ₃ μ₄ : R) : Mval μ₂ μ₃ μ₄ 4 = 6 * μ₂ + 4 * μ₃ + μ₄ := by
  simp [Mval, Nat.choose]; ring

/-- **Binomial inversion at `A = 3`.** From the ansatz, the 3-body moment is
`μ₃ = M₃ − 3μ₂` — the recursion used by the residual-simplex compute. -/
theorem mu_inversion_three (μ₂ μ₃ μ₄ : R) :
    μ₃ = Mval μ₂ μ₃ μ₄ 3 - 3 * Mval μ₂ μ₃ μ₄ 2 := by
  rw [Mval_three, Mval_two]; ring

/-- **Binomial inversion at `A = 4`.** The 4-body moment is
`μ₄ = M₄ − 6μ₂ − 4μ₃`, matching the compute's recursive form. -/
theorem mu_inversion_four (μ₂ μ₃ μ₄ : R) :
    μ₄ = Mval μ₂ μ₃ μ₄ 4 - 6 * Mval μ₂ μ₃ μ₄ 2
          - 4 * (Mval μ₂ μ₃ μ₄ 3 - 3 * Mval μ₂ μ₃ μ₄ 2) := by
  rw [Mval_four, Mval_three, Mval_two]; ring

/-- The recursive form agrees with the closed alternating (finite-difference)
form `μ₄ = M₄ − 4M₃ + 6M₂`. Recorded because the compute uses the recursion and
the exposition quotes the closed form. -/
theorem mu4_closed_form (M₂ M₃ M₄ : R) :
    M₄ - 6 * M₂ - 4 * (M₃ - 3 * M₂) = M₄ - 4 * M₃ + 6 * M₂ := by ring

/-- **No 3-particle measurement determines `μ₄`.** Two simplex ansätze differing
*only* in their 4-body moment agree on `M(A)` for every `A ≤ 3`, because the
`C(A,4)` column vanishes there. Hence nothing measured on a 3-particle cluster —
at any bond order, `Δ²g`, `Δ³g`, or higher — constrains `μ₄`; a genuine `μ₄`
comparand requires `A = 4`. -/
theorem mu4_unconstrained_below_four (μ₂ μ₃ μ₄ μ₄' : R) {A : ℕ} (hA : A < 4) :
    Mval μ₂ μ₃ μ₄ A = Mval μ₂ μ₃ μ₄' A := by
  have h : A.choose 4 = 0 := Nat.choose_eq_zero_of_lt hA
  simp [Mval, h]

end MomentInversion

end QOU.MassTheory.UrsellSlotAlignment
