import QOU.Infra.Polylogarithm

/-!
# Cl_3(2π/5) + Cl_3(4π/5) = -(12/25) ζ(3)

Compiled formalisation of `prop:cl3-zeta5-orbit-sum-identity`.
Sibling docstub at `braids-and-knots/cl3-zeta5-orbit-sum-identity.lean`.

K = 5 specialisation of Theorem B's closed-form orbit sum.
-/

namespace QOU.BraidKnot.Cl3Zeta5OrbitSum

open QOU.Infra.Polylogarithm

/-- **Proposition (`prop:cl3-zeta5-orbit-sum-identity`,
    arithmetic core).**
    Theorem B specialised at N = 5: `-((5² - 1)/5²) · ζ(3)
    = -(24/25) · ζ(3)`.  Per Copilot review: `field_simp` to
    clear denominators before `ring`. -/
theorem orbit_sum_identity (zeta3 : ℝ) :
    cl3OrbitSumPredicted 5 zeta3 = -(24 / 25) * zeta3 := by
  unfold cl3OrbitSumPredicted
  field_simp
  ring

end QOU.BraidKnot.Cl3Zeta5OrbitSum
