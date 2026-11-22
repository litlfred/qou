import QOU.Archimedean.GroundRing

/-!
# QOU.Archimedean.em_coupling_projection — Electromagnetic coupling from braiding

The electromagnetic fine structure constant is determined by three
finite combinatorial ingredients: the antisymmetric eigenvalue of the
R-matrix (q⁻¹), the q-deformed crossing numbers of the two force-carrier
generators T_{2,9} and T_{3,5}, and the substrate parameter q.

  α_EM = q⁻¹ / ([9]_q · [10]_q)

Stated **division-free over ℤ[q, q⁻¹]** as the defining multiplicative
relation (see `IsEmCoupling`): the denominator `[9]_q · [10]_q` is not a
unit of the Laurent ring, so α_EM itself is a fraction-field element —
but its *defining content* is the single relation

  [9]_q · [10]_q · α = q⁻¹,

which lives in `ℤ[q, q⁻¹]` without any division.  This mirrors the
`2 · E_cross = HA` convention in `QOU.Archimedean.GroundRing`, where a
presentation factor that would leave the ground ring is replaced by the
cleared-denominator relation.

LaTeX label: `prop:em-coupling-projection`

## References

- [leitner2026] §5/em-coupling-projection
- [jones1987] https://doi.org/10.2307/1971403

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
The q-integers reuse the division-free `QOU.Archimedean.qInt`; `q⁻¹` is
the genuine ring element `q_inv = T(-1)`, never a field inverse.  The
classical limit `q → 1 ⇒ α_EM → 1/90` is an *archimedean* statement
(it needs an order and `|·|` on the codomain) and therefore belongs to a
`ℝ`-specialisation under `descartes-universe/`, not to this fibre-level
file — see `notation-collisions.md §Base ring convention` (§7c).
-/

namespace QOU.Archimedean

noncomputable section

/-- Crossing number of the strong force carrier `T_{2,9}` (as a ℤ index
    for `qInt`). -/
def strongCrossingNumber : ℤ := 9

/-- Crossing number of the weak force carrier `T_{3,5}` (as a ℤ index
    for `qInt`). -/
def weakCrossingNumber : ℤ := 10

/-- The antisymmetric eigenvalue of the R-matrix for `SU_q(2)`:
    `|tr_τ(σ_anti)|² = q⁻¹`.  This is the genuine ring element
    `q_inv = T(-1) ∈ ℤ[q, q⁻¹]`, **not** a field inverse. -/
def antisymmetricEigenvalue : R_q := q_inv

/-- **Electromagnetic coupling projection** (Proposition).

    The fine-structure constant is the τ-trace of the antisymmetric
    braiding component normalised by the force-carrier crossing
    complexities,

      α_EM = q⁻¹ / ([9]_q · [10]_q),

    stated **division-free over ℤ[q, q⁻¹]** as the cleared-denominator
    relation `α` satisfies:

      [9]_q · [10]_q · α = q⁻¹.

    The formula factorises into three layers:
    1. Charge (discrete, from writhe): `Q_q(K) = [w(K)]_q`.
    2. Coupling strength (R-matrix): `|tr_τ(σ_anti)|² = q⁻¹`.
    3. Normalisation by force-carrier complexity: `[9]_q · [10]_q`. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
-- Ref: [leitner2026] §5/em-coupling-projection
def IsEmCoupling (α : R_q) : Prop :=
  qInt strongCrossingNumber * qInt weakCrossingNumber * α = antisymmetricEigenvalue

/-- The defining relation with the crossing-number indices and the
    antisymmetric eigenvalue unfolded: `[9]_q · [10]_q · α = q⁻¹`.  Holds
    by definitional unfolding (`strongCrossingNumber = 9`,
    `weakCrossingNumber = 10`, `antisymmetricEigenvalue = q_inv`). -/
-- Ref: [leitner2026] §5/em-coupling-projection
theorem isEmCoupling_iff (α : R_q) :
    IsEmCoupling α ↔ qInt 9 * qInt 10 * α = q_inv := Iff.rfl

end

end QOU.Archimedean
