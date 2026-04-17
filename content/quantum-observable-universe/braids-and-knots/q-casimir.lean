/-!
# QOU.QCasimir — The q-Casimir element of 𝒰_q(𝔰𝔲(2))

The q-Casimir C_q ∈ 𝒰_q(𝔰𝔲(2)) is the distinguished central element
whose eigenvalue on the spin-j irreducible representation V_j is the
symmetric product `[j]_q · [j+1]_q`, where
`[n]_q = (qⁿ - q⁻ⁿ)/(q - q⁻¹)`.  This file gives the formal
construction as an element of the algebra underlying `QuantumSu2`
(defined in `quantum-su2.lean`).

LaTeX label: `def:q-casimir`

## References

- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9

## Coefficient layer

The natural coefficient ring is `R_q = ℤ[q, q⁻¹]` (Laurent
polynomials).  The explicit formula for `C_q` requires inverting
`(q - q⁻¹)`, which is not a unit in `R_q`.  We therefore parameterise
the definition by:

* a ring-hom `ι : R_q →+* qs.Algebra` embedding coefficients into
  the algebra carrier, and
* an element `invQm : qs.Algebra` witnessing that `(q - q⁻¹)`
  becomes invertible after the embedding.

Concretely, callers supply a `QCasimirData` (e.g. after localising at
`q - q⁻¹` or extending scalars to the fraction field).  See Kassel
§VI.4 for the standard choice.
-/

import QOU.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU

noncomputable section

/-- Data needed to construct the q-Casimir element: a ring-hom
    embedding of the ground ring `R_q` into `qs.Algebra`, together with
    an algebra element witnessing that `(q - q⁻¹)` becomes a two-sided
    unit after the embedding.  These inputs abstract the act of
    localising (or extending scalars) at `q - q⁻¹`. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
structure QCasimirData (qs : QuantumSu2) where
  /-- Embedding of the ground ring into the algebra. -/
  ι : R_q →+* qs.Algebra
  /-- An algebra element that inverts `ι (q - q⁻¹)`. -/
  invQm : qs.Algebra
  /-- Left inverse witness. -/
  invQm_left  : invQm * ι (qs.q - qs.q ^ (-(1 : ℤ))) = 1
  /-- Right inverse witness. -/
  invQm_right : ι (qs.q - qs.q ^ (-(1 : ℤ))) * invQm = 1

/-- The (normalised) q-Casimir element inside `qs.Algebra`:
      C_q = F·E + (q·K + q⁻¹·K⁻¹ - (q + q⁻¹)) · (q - q⁻¹)⁻²

    Normalisation is chosen (Kassel §VI.4) so that the eigenvalue on
    the trivial representation V_0 vanishes and the classical limit
    `q → 1` recovers `j(j+1)`.  All scalar coefficients enter via the
    embedding `d.ι`, and `(q - q⁻¹)⁻²` is realised as `d.invQm * d.invQm`. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
def QCasimir (qs : QuantumSu2) (d : QCasimirData qs) : qs.Algebra :=
  let qInv        := qs.q ^ (-(1 : ℤ))
  let kPart       := d.ι qs.q * qs.K + d.ι qInv * qs.K_inv
  let normaliser  := d.ι (qs.q + qInv)
  qs.F * qs.E + (kPart - normaliser) * d.invQm * d.invQm

/-- Centrality of the q-Casimir.  The proof reduces to the commutation
    relations of 𝒰_q(𝔰𝔲(2)) (Kassel §VI.4); agents formalising it
    should discharge the three axioms by calculation with the Hopf
    presentation.  Treating this as a class lets downstream consumers
    assume centrality without committing to a specific derivation. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
class QCasimirCentral (qs : QuantumSu2) (d : QCasimirData qs) : Prop where
  /-- C_q commutes with E. -/
  comm_E : QCasimir qs d * qs.E = qs.E * QCasimir qs d
  /-- C_q commutes with F. -/
  comm_F : QCasimir qs d * qs.F = qs.F * QCasimir qs d
  /-- C_q commutes with K. -/
  comm_K : QCasimir qs d * qs.K = qs.K * QCasimir qs d

/-- Symmetric q-number `[n]_q = (qⁿ - q⁻ⁿ) / (q - q⁻¹)` — the standard
    convention for the q-Casimir on 𝒰_q(𝔰𝔲(2)).  Distinguish from the
    asymmetric `QuantumSu2.qInt` (`(qⁿ - 1)/(q - 1)`). -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
def qNumberSym (q : R_q) (n : R_q) : R_q :=
  (q ^ n - q ^ (-n)) / (q - q ^ (-(1 : R_q)))

/-- Eigenvalue of the q-Casimir on the spin-`j` irreducible.

    On the highest-weight module `V_j` (with convention
    `K v_j = q^{2j} v_j`), the central element `QCasimir qs d` acts
    as the scalar `[j]_q · [j+1]_q` with the symmetric q-number.
    Downstream, `QAngularMomentum` specialises this formula to knot
    representations.  The parameter `j` ranges over `R_q` to
    accommodate half-integer spins. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
def QCasimirEigenvalue (qs : QuantumSu2) (j : R_q) : R_q :=
  qNumberSym qs.q j * qNumberSym qs.q (j + 1)

/-- Sanity check: `[0]_q = 0` in the symmetric convention, so the
    eigenvalue on the trivial representation vanishes. -/
-- Ref: [kassel1995]
theorem qNumberSym_zero (q : R_q) : qNumberSym q 0 = 0 := by
  unfold qNumberSym; simp

end

end QOU
