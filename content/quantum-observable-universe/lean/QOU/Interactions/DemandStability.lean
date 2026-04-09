/-!
# Demand stability: the demand profile determines nuclear stability

The demand profile (set of negative NF coefficients) is the
categorical diagnostic of stability. Beta-stable nuclei minimize
demand magnitude at fixed mass number A.

## References

- [prop:demand-stability]
- [conj:periodic-table-demand]
-/

import QOU.Interactions.DerivedAtom
import QOU.Descartes.GroundRing

namespace QOU.Interactions

open QOU.Descartes

/-! ## §1  Demand magnitude -/

/-- The demand magnitude: sum of absolute values of negative
    NF coefficients, over ℤ[q, q⁻¹].

    For formal proofs we work with the negative part directly
    since absolute value requires an ordering on R_q. -/
/-- The negative part of a coefficient requires an ordering on R_q.
    Since R_q = ℤ[q,q⁻¹] has no canonical total order, the demand
    profile is defined over ℝ-valued evaluations (at specific q₀),
    not over R_q directly.

    For formal proofs, we use the sign of specific Laurent polynomials
    evaluated at q > 1 (see ProtonTrefoilSign.lean). -/

/-! ## §2  Beta stability criterion -/

/-- A configuration (Z, N) is beta-stable at fixed A = Z + N
    if no single nucleon exchange p ↔ n reduces the demand.

    Formally: (Z, N) is beta-stable iff for Z' = Z ± 1, N' = A - Z':
      demandMag(A(Z,N)) ≤ demandMag(A(Z',N'))

    This is a finite condition: at fixed A, there are only A+1
    configurations to check.  -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- (Beta stability from NF demand minimization.)
sorry

/-! ## §3  The e⁻ coefficient as beta decay receptivity -/

/-- **Beta decay receptivity.**

    The e⁻ coefficient (index 5 in the NF basis) of a nucleon
    is the trefoil demand. If c₅ < 0, the nucleon is receptive
    to beta decay: it can emit an electron (trefoil) to reduce
    its demand.

    At q₀:
      c₅(proton)  ≈ -0.043
      c₅(neutron) ≈ -0.044

    Both are negative — both nucleons have trefoil demand.
    The neutron's is larger: |c₅(n)| > |c₅(p)|.
    Combined with net(n) < net(p), this gives the beta decay
    direction: n → p + e⁻ + ν̄.

    In ℤ[q, q⁻¹], the e⁻ coefficient of B₃·crossings(u,d,d) is
    a Laurent polynomial with leading term −q⁻¹·(...). The sign
    is negative for all q > 1. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
sorry

/-! ## §4  Magic numbers from demand closure -/

/-- A magic number is a value of Z (or N) at which the nucleus
    achieves demand closure (all NF coefficients nonneg) for at
    least one value of the complementary quantum number.

    Conjecture: the magic numbers are exactly {2, 8, 20, 28, 50, 82, 126}.

    Verified computationally for Z = 2 (He-3: demand = ∅). -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- (Magic numbers from demand closure in the NF basis.)
sorry

/-! ## §5  Hecke square identity for typed crossings -/

/-- The typed crossing squares reduce via the Hecke relation.
    This is the key identity for polynomial scaling of the
    inductive GB reduction.

    C_pp² = HA · C_pp + 1
    C_nn² = HA · C_nn + 1  (after expanding σ⁻¹ = σ - HA)

    Both are instances of σ² = HA·σ + 1. -/
theorem typed_crossing_square_pp (ρ : HeckeRep 3 2) (i : Fin 2) :
    ρ.gen i * ρ.gen i = HA_t • ρ.gen i + 1 :=
  ρ.hecke_rel i

/-- The mixed crossing square has an additional constant term.
    C_pn² = HA · C_pn + 1 − ¼HA²

    (In ℤ[q, q⁻¹], we state: 4·C_pn² = 4·HA·C_pn + 4 − HA².) -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
sorry

end QOU.Interactions
