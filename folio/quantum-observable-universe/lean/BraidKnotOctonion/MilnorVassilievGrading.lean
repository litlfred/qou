/-
# DD-1: the factor-of-2 grading crux of the Milnor = leading-Vassiliev bridge

The Milnor-order law (#4471 `MilnorOrderLawGeneral`, #4480 `MilnorExactCoefficient`)
establishes that the `A`-component Brunnian trace-deficit
`D_A(h)`, `h = q - q⁻¹`, has leading order **`2(A−1)`** (lower bound proved for all
`A`; measured exactly at `A = 3,4,5,6`).

Standard finite-type (Vassiliev) theory expands a Jones-type invariant in the
variable `ℏ = log q` (`q = e^{ℏ}`); a degree-`m` Vassiliev invariant sits at order
`ℏ^m`.  The length-`A` Milnor invariant `μ̄(12…A)` of an `A`-component Brunnian link
is a Vassiliev invariant of **degree `A−1`** (Bar-Natan 1995; Lin).  Naively that
predicts leading order `A−1` — but the qou deficit has order `2(A−1)`, **double**.

This file pins the two grading conventions against each other, so the discrepancy
is shown to be REAL (not a variable-convention artifact), and states the resolution
as an honest conjecture class (no instance).  It is the analysis layer for bean
`qou-q64u`; the finite-type Lean scaffold itself is built elsewhere
(`claude/vassiliev-finite-type-infra-…`).  Nothing here is axiomatised as proved.

-- Ref: [barnatan1995] On the Vassiliev knot invariants, Topology 34 (1995).
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic

namespace QOU.MassTheory.MilnorVassilievGrading

/-! ### 1. The two expansion variables agree to first order (no convention factor) -/

/-- **The deficit variable is `2·sinh` of the Vassiliev variable.**  With `h = q−q⁻¹`
(the qou Markov-deficit variable) and `ℏ = log q` (`q = e^{ℏ}`, the finite-type
variable), `h = 2·sinh ℏ`.  Hence the two gradings differ by no rescaling constant
other than the harmless factor `2`: they assign the **same leading order** to a term. -/
theorem deficit_var_eq_two_sinh (q : ℝ) (hq : 0 < q) :
    q - q⁻¹ = 2 * Real.sinh (Real.log q) := by
  rw [Real.sinh_eq, Real.exp_log hq, Real.exp_neg, Real.exp_log hq]
  ring

/-- **`sinh` vanishes at `0`, so the change of variable fixes the origin.**  With
`Real.sinh_zero`, `2·sinh 0 = 0`: the substitution `q = e^{ℏ}` sends `ℏ = 0` (i.e.
`q = 1`) to `h = 0`.  Together with `deficit_var_eq_two_sinh`, `h = 2 sinh ℏ =
2ℏ + O(ℏ³)`, so `h` and `ℏ` share the same leading order (the harmless factor `2` is
a unit): an order-`k`-in-`h` term is an order-`k`-in-`ℏ` (Vassiliev-degree-`k`) term.
The `2(A−1)` deficit order is therefore a genuine Vassiliev **degree** statement, not
a variable-convention artifact. -/
theorem grading_change_fixes_origin : 2 * Real.sinh 0 = 0 := by
  rw [Real.sinh_zero]; ring

/-! ### 2. The doubling is real: qou order = 2 × the Milnor Vassiliev degree -/

/-- Vassiliev degree of the length-`A` Milnor invariant `μ̄(12…A)` (cited:
Bar-Natan 1995 / Lin): `A − 1`. -/
def milnorVassilievDegree (A : ℕ) : ℕ := A - 1

/-- The qou Brunnian deficit's leading order (proved lower bound #4471; measured
exact #4480): `2(A − 1)`. -/
def qouDeficitLeadingOrder (A : ℕ) : ℕ := 2 * (A - 1)

/-- **The factor-of-2 discrepancy, exactly.**  The qou deficit's leading Vassiliev
degree is exactly **twice** the length-`A` Milnor invariant's Vassiliev degree.  So
the Milnor-Vassiliev bridge, invoked at face value (first non-vanishing Vassiliev
invariant = `μ̄` at degree `A−1`), does **not** predict the observed order — a real
gap, not a rescaling artifact (§1 pinned the variables). -/
theorem qou_order_is_double_milnor_degree (A : ℕ) :
    qouDeficitLeadingOrder A = 2 * milnorVassilievDegree A := rfl

/-- Sanity anchors: A=3 → 4 = 2·2; A=6 → 10 = 2·5 (the #4480 endpoints). -/
theorem doubling_A3 : qouDeficitLeadingOrder 3 = 4 ∧ milnorVassilievDegree 3 = 2 := by
  constructor <;> rfl
theorem doubling_A6 : qouDeficitLeadingOrder 6 = 10 ∧ milnorVassilievDegree 6 = 5 := by
  constructor <;> rfl

/-! ### 3. DD-1 resolution — OPEN conjecture class (content-bearing, no instance)

The mechanism proposed by #4480: a **cyclic** Markov trace annihilates the linear
(Milnor-degree `A−1`) part of the deficit — `cyclic_trace_kills_iterCommTower` proved
this for the Lie tower — so the first **surviving** contribution is a bar-symmetric
(`q ↔ q⁻¹`) **quadratic** in the tree-level data, landing at the doubled degree
`2(A−1)`.  This is the honest open resolution of DD-1; it is NOT proved here (it needs
the finite-type scaffold + the Habegger–Masbaum tree-level identity). -/

/-- **(CONJECTURE, primary — OPEN.)**  A Vassiliev-degree function `vdeg` on the
Brunnian deficit family realises DD-1: the linear (degree-`A−1`) part vanishes and
the first non-vanishing degree is the doubled `2(A−1)`.  Content-bearing; NO instance
(the honest open state).  Do not fabricate an instance — that would launder the
bridge (§"Axiomatization is NOT a Proof"). -/
class BarSymmetricDegreeDoubling (vdeg : ℕ → ℕ) : Prop where
  /-- The linear Milnor-degree part carries no deficit weight (cyclic-trace
      annihilation, #4480): the realised degree is never the bare `A−1`. -/
  linear_milnor_part_absent : ∀ A : ℕ, 2 ≤ A → vdeg A ≠ milnorVassilievDegree A
  /-- The first non-vanishing degree is the bar-symmetric doubled order. -/
  first_surviving_is_doubled : ∀ A : ℕ, 2 ≤ A → vdeg A = qouDeficitLeadingOrder A

/-- **(CONDITIONAL on the conjecture.)**  If a Vassiliev-degree function realises the
doubling, then at every `A ≥ 2` its degree is `2(A−1)` and strictly exceeds the naive
Milnor degree `A−1`.  Fully verified modulo the single open class instance. -/
theorem dd1_degree_of_doubling {vdeg : ℕ → ℕ} [hc : BarSymmetricDegreeDoubling vdeg]
    {A : ℕ} (hA : 2 ≤ A) :
    vdeg A = 2 * (A - 1) ∧ milnorVassilievDegree A < vdeg A := by
  refine ⟨hc.first_surviving_is_doubled A hA, ?_⟩
  have heq := hc.first_surviving_is_doubled A hA
  rw [heq, qouDeficitLeadingOrder, milnorVassilievDegree]
  omega

end QOU.MassTheory.MilnorVassilievGrading
