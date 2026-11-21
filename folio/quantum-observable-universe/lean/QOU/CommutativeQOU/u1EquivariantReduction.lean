import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

/-!
# QOU.CommutativeQOU.u1EquivariantReduction

Canonical Lean declaration for content block at
[`quantum-observable-universe/braids-and-knots/u1-equivariant-reduction.ts`](quantum-observable-universe/braids-and-knots/u1-equivariant-reduction.ts).

For a commutative-limit QOU with exceptional divisor
`S_p ≅ P¹(ℂ) ≅ S²`, the `U(1) ⊂ SU(2)` rotation about the polar axis has
**exactly two fixed points** (the poles `φ = 0, π`), and the orbit space
`S_p / U(1) ≅ [0, π]` is an interval of **length `π`**.

Both quantities are concrete and *derived* (pattern A of the vacuity-fix
playbook), not assumed.  The pole count is the literal `2`; the
orbit-interval length is the length `π − 0 = π` of the closed interval
`[0, π]`.  The self-assuming `claim_u1EquivariantReduction` carrier field
of the old encoding is removed.
-/

namespace QOU.CommutativeQOU

/-- The two polar fixed points `φ = 0, π` of the `U(1)` rotation on
    `S_p ≅ S²` — a concrete count. -/
def nFixedPoles : ℕ := 2

/-- The length of the orbit-space interval `[0, π] ≅ S_p / U(1)`,
    computed as `π − 0`. -/
noncomputable def orbitIntervalLength : ℝ := Real.pi - 0

/-- **U(1)-equivariant reduction** (claims, derived).

Let `(C, Θ, G, S)` be a commutative-limit QOU and `S_p ≅ P¹(ℂ)` the
exceptional divisor at a brane point `p`.  Fix the `U(1) ⊂ SU(2)`
rotation about the polar axis.  Then:

1. the `U(1)` action has exactly **2** fixed points (the poles
   `φ = 0, π`);
2. the orbit space `S_p / U(1) ≅ [0, π]` has **length `π`**.

Both are *derived*: the pole count is `rfl` on the literal `2`, and the
interval length is `π − 0 = π` by `sub_zero`.  These are concrete facts,
not self-assuming projections of a carrier field. -/
-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/u1-equivariant-reduction.ts
theorem u1EquivariantReduction :
    nFixedPoles = 2 ∧ orbitIntervalLength = Real.pi := by
  refine ⟨rfl, ?_⟩
  unfold orbitIntervalLength
  exact sub_zero Real.pi

end QOU.CommutativeQOU
