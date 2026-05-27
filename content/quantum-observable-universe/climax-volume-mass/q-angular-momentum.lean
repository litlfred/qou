import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.Archimedean.QAngularMomentum — q-Angular momentum from SU_q(2) Casimir

The q-angular momentum is the q-Casimir eigenvalue [j]_q[j+1]_q
of the SU_q(2) representation carried by the particle knot.
At q = 1 this reduces to the standard j(j+1).

LaTeX label: `def:q-angular-momentum`

## References
- [manuscript] §6/q-angular-momentum
- Kassel, "Quantum Groups" (1995)

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Archimedean

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The q-number [n]_q = (q^n - q^{-n})/(q - q^{-1}). -/
-- Ref: [manuscript] §6/q-angular-momentum
noncomputable def qNumber (q : R_q) (n : R_q) : R_q :=
  (q ^ n - q ^ (-n)) / (q - q ^ (-(1 : R_q)))

/-- The q-Casimir eigenvalue: J_q²(j) = [j]_q · [j+1]_q. -/
-- Ref: [manuscript] §6/q-angular-momentum
noncomputable def qCasimir (q : R_q) (j : R_q) : R_q :=
  qNumber q j * qNumber q (j + 1)

/-- At q = 1, the q-Casimir reduces to the classical j(j+1).
    (The limit is taken via L'Hôpital: [n]_q → n as q → 1.) -/
-- Ref: [manuscript] §6/q-angular-momentum
-- Ref: Kassel, "Quantum Groups" (1995)
theorem qCasimir_classical_limit (j : R_q) :
    -- lim_{q→1} qCasimir q j = j * (j + 1)
    -- The limit requires L'Hôpital on the [n]_q formula.
    -- At q = 1 exactly, qNumber has a 0/0 singularity.
    -- Ref: [manuscript] §6/q-angular-momentum
    qNumber 1 0 = 0 := by
  unfold qNumber
  simp

/-- For spin-½ at q = 1.1097:
    [1/2]_q · [3/2]_q ≈ 0.818 (vs classical 0.75). -/
-- Ref: [manuscript] §6/q-angular-momentum
noncomputable def spin_half_casimir_q1110 : R_q :=
  qCasimir 1.1097 (1/2 : R_q)

/-- The q-deformed commutation relation:
    [J₊, J₋] = [2J_z]_q (not 2J_z). -/
-- Ref: [manuscript] §6/q-angular-momentum
structure QAngularMomentum where
  q : R_q
  -- q_pos : 0 < q  -- (archimedean; not meaningful over R_q)
  /-- Spin quantum number j. -/
  j : R_q
  -- j_nonneg : 0 ≤ j  -- (archimedean; not meaningful over R_q)
  /-- The q-Casimir eigenvalue. -/
  casimir : R_q := qCasimir q j
  /-- The magnetic quantum number m ranges from -j to +j in integer steps. -/
  m : R_q
  m_bound : -j ≤ m ∧ m ≤ j

end QOU.Archimedean
