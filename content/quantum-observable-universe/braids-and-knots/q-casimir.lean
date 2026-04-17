/-!
# QOU.QCasimir — The q-Casimir element of 𝒰_q(𝔰𝔲(2))

The q-Casimir C_q ∈ 𝒰_q(𝔰𝔲(2)) is the distinguished central element
whose eigenvalue on the spin-j irreducible representation V_j is
[j]_q · [j+1]_q.  This file gives the formal construction as an
element of the algebra underlying `QuantumSu2` (defined in
`quantum-su2.lean`).

LaTeX label: `def:q-casimir`

## References

- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import QOU.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU

noncomputable section

/-- The q-Casimir element inside the algebra carrier of a
    `QuantumSu2` structure.

    Formula:
      C_q = F · E + (q · K + q⁻¹ · K⁻¹) / (q - q⁻¹)²

    The scalar coefficients live in the ground ring `R_q`, so the
    ratio makes sense once we lift them along the canonical map
    `R_q → Algebra` (provided by the ring structure on `Algebra`).
    Here we use the algebra element `(qs.q - qs.q⁻¹)` built from
    `qs.K` and `qs.K_inv` via the identity
    `[E, F] = (K - K⁻¹)/(q - q⁻¹)`.

    In the formulation below, we realise the scalar ratio through
    an auxiliary element `qK_plus_qInvKinv` and divide by
    `(q - q⁻¹)²` at the level of the ground ring, then scalar-multiply
    by the appropriate algebra element. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
def QCasimir (qs : QuantumSu2) : qs.Algebra :=
  qs.F * qs.E +
    (qs.q • qs.K + (qs.q ^ (-(1 : ℤ))) • qs.K_inv) *
      ((qs.q - qs.q ^ (-(1 : ℤ))) ^ 2)⁻¹ • (1 : qs.Algebra)

/-- Centrality of the q-Casimir (conjectural class — the proof
    reduces to the commutation relations of 𝒰_q(𝔰𝔲(2)), see Kassel
    §VI.4).  Any instance commits to the centrality statement as an
    axiom that can be discharged from the Hopf-algebra presentation. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
class QCasimirCentral (qs : QuantumSu2) : Prop where
  /-- C_q commutes with E. -/
  comm_E : QCasimir qs * qs.E = qs.E * QCasimir qs
  /-- C_q commutes with F. -/
  comm_F : QCasimir qs * qs.F = qs.F * QCasimir qs
  /-- C_q commutes with K. -/
  comm_K : QCasimir qs * qs.K = qs.K * QCasimir qs

/-- Symmetric q-number `[n]_q = (qⁿ - q⁻ⁿ) / (q - q⁻¹)` — the standard
    convention for the q-Casimir on 𝒰_q(𝔰𝔲(2)).  Distinguish from the
    asymmetric `QuantumSu2.qInt` (`(qⁿ - 1)/(q - 1)`). -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
noncomputable def qNumberSym (q : R_q) (n : R_q) : R_q :=
  (q ^ n - q ^ (-n)) / (q - q ^ (-(1 : R_q)))

/-- Eigenvalue of the q-Casimir on the spin-j irreducible.

    On the highest-weight module `V_j`, the central element `QCasimir qs`
    acts as the scalar `[j]_q · [j+1]_q` with the **symmetric** q-number
    `[n]_q = (qⁿ - q⁻ⁿ)/(q - q⁻¹)`.  Downstream, `QAngularMomentum`
    specialises this formula to knot representations. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
noncomputable def QCasimirEigenvalue (qs : QuantumSu2) (j : R_q) : R_q :=
  qNumberSym qs.q j * qNumberSym qs.q (j + 1)

/-- Sanity check: `[0]_q = 0` in the symmetric convention. -/
-- Ref: [kassel1995]
theorem qNumberSym_zero (q : R_q) : qNumberSym q 0 = 0 := by
  unfold qNumberSym; simp

end

end QOU
