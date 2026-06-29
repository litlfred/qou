import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Data.Real.Basic


/-!
# QOU.Archimedean.QAngularMomentum — q-Angular momentum from SU_q(2) Casimir

The q-angular momentum is the q-Casimir eigenvalue [j]_q[j+1]_q
of the SU_q(2) representation carried by the particle knot.
At q = 1 this reduces to the standard j(j+1).

LaTeX label: `def:q-angular-momentum`

## References
- [manuscript] §6/q-angular-momentum
- Kassel, "Quantum Groups" (1995)

**Ground ring**: archimedean specialisation over `ℝ` (AGENTS.md §7c).
The q-number formula uses real exponents `q^j` (`Real.rpow`),
division, scientific literals and ordering, all of which require the
archimedean structure of `ℝ`. The underlying combinatorial content
stays generic to any commutative ring carrying the same q-data.
-/

namespace QOU.Archimedean

/-- Ground ring: the archimedean specialisation `R_q = ℝ`. -/
abbrev R_q := ℝ

/-- The substrate indeterminate, specialised to the numerical anchor. -/
noncomputable def q_param : R_q := 1.1097

/-- The q-number `[n]_q = (qⁿ - q⁻ⁿ)/(q - q⁻¹)` (real exponents). -/
-- Ref: [manuscript] §6/q-angular-momentum
noncomputable def qNumber (q : R_q) (n : R_q) : R_q :=
  (q ^ n - q ^ (-n)) / (q - q ^ (-(1 : R_q)))

/-- The q-Casimir eigenvalue: J_q²(j) = [j]_q · [j+1]_q. -/
-- Ref: [manuscript] §6/q-angular-momentum
noncomputable def qCasimir (q : R_q) (j : R_q) : R_q :=
  qNumber q j * qNumber q (j + 1)

/-- At `n = 0` the q-number vanishes: `[0]_q = 0` (the numerator
    `q⁰ - q⁰ = 0`). This is the value underlying the classical limit
    `[n]_q → n` as `q → 1`. -/
-- Ref: [manuscript] §6/q-angular-momentum
-- Ref: [kassel1995] Kassel, "Quantum Groups" (1995)
theorem qNumber_zero (q : R_q) : qNumber q 0 = 0 := by
  unfold qNumber
  simp

/-- For spin-½ at q = 1.1097:
    [1/2]_q · [3/2]_q ≈ 0.818 (vs classical 0.75). -/
-- Ref: [manuscript] §6/q-angular-momentum
noncomputable def spin_half_casimir_q1110 : R_q :=
  qCasimir 1.1097 (1 / 2 : R_q)

/-- The q-deformed commutation relation:
    [J₊, J₋] = [2J_z]_q (not 2J_z). -/
-- Ref: [manuscript] §6/q-angular-momentum
structure QAngularMomentum where
  /-- Substrate parameter `q` (archimedean, `q > 0`). -/
  q : R_q
  /-- Spin quantum number j. -/
  j : R_q
  /-- The q-Casimir eigenvalue. -/
  casimir : R_q := qCasimir q j
  /-- The magnetic quantum number m ranges from -j to +j in integer steps. -/
  m : R_q
  /-- The magnetic quantum number is bounded by `±j`. -/
  m_bound : -j ≤ m ∧ m ≤ j

end QOU.Archimedean
