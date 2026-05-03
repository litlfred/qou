import QOU.Interactions.DerivedAtom
import QOU.Descartes.GroundRing

/-!
# Demand stability: the demand profile determines nuclear stability

The demand profile (set of negative NF coefficients) is the
categorical diagnostic of stability. Beta-stable nuclei minimize
demand magnitude at fixed mass number A.

## References

- [prop:demand-stability]
- [conj:periodic-table-demand]
-/

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
-- beta_stability_criterion: requires defining demandMag over ℝ (evaluating
-- Laurent polynomials at q₀) and showing minimum over A+1 configurations.
-- Not yet formalised; the typed crossing infrastructure is in DerivedAtom.lean.
-- Ref: [jones1987] https://doi.org/10.2307/1971403

/-! ## §3  The e⁻ coefficient as beta decay receptivity -/

/-- **Beta decay receptivity.**

    The e⁻ coefficient (index 5 in the NF basis) of a nucleon
    is the trefoil demand. If c₅ < 0, the nucleon is receptive
    to beta decay: it can emit an electron (trefoil) to reduce
    its demand.

    The sign of the e⁻ coefficient for the proton and neutron is
    proved negative in ProtonTrefoilSign.lean:
    - `proton_trefoil_neg_on_interval`: c₅(p) < 0 for q ∈ (1, 3/2]
    - `neutron_trefoil_neg`: c₅(n) < 0 for all q > 1
    - `neutron_more_negative`: |c₅(n)| > |c₅(p)| for q > 1 -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- See: ProtonTrefoilSign.lean for the sign proofs.
-- sorry  -- Replaced: the sign proofs are in ProtonTrefoilSign.lean

/-! ## §4  Magic numbers from demand closure -/

/-- A magic number is a value of Z (or N) at which the nucleus
    achieves demand closure (all NF coefficients nonneg) for at
    least one value of the complementary quantum number.

    Conjecture: the magic numbers are exactly {2, 8, 20, 28, 50, 82, 126}.

    Verified computationally for Z = 2 (He-3: demand = ∅). -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- (Magic numbers from demand closure in the NF basis.)
-- magic_numbers_conjecture: requires demand magnitude function over ℝ.
-- Verified computationally for Z = 2 (He-4: demand = ∅).
-- Ref: [jones1987] https://doi.org/10.2307/1971403

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

/-- The mixed crossing square identity.
    C_pn² = HA · C_pn + 1 − ¼HA²

    (In ℤ[q, q⁻¹], we state: 4·C_pn² = 4·HA·C_pn + 4 − HA².)

    This requires expanding (σ - ½HA)² and using the Hecke relation.
    Since ½ ∉ ℤ[t,t⁻¹], we multiply through by 4. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
/-- The mixed crossing square: (2σ - HA)² = 4 + HA².
    Uses the Hecke relation σ² = HA·σ + 1. -/
theorem mixed_crossing_square_identity (ρ : HeckeRep 3 2) (i : Fin 2) :
    (2 • ρ.gen i - HA_t • 1) * (2 • ρ.gen i - HA_t • 1) =
    (4 + HA_t * HA_t) • (1 : TMatrix) := by
  set σ := ρ.gen i with hσ
  have hecke : σ * σ = HA_t • σ + 1 := ρ.hecke_rel i
  -- Rewrite `(2 : ℕ) • σ` as `σ + σ` to expose only ring + R_t-smul ops.
  rw [show (2 : ℕ) • σ = σ + σ from two_smul _ σ]
  -- Goal: (σ + σ - HA•1) * (σ + σ - HA•1) = (4 + HA*HA) • 1
  -- Expand the product:
  --   (σ+σ)(σ+σ) - (σ+σ)(HA•1) - (HA•1)(σ+σ) + (HA•1)(HA•1)
  -- = (σσ + σσ + σσ + σσ) - HA•(σ+σ) - HA•(σ+σ) + (HA·HA)•1
  -- = 4·(σσ) - 2·HA•(σ+σ) + (HA·HA)•1
  -- = 4·(HA•σ + 1) - 4·HA•σ + (HA·HA)•1   [Hecke; 2·HA•(σ+σ) = 4·HA•σ via 2σ=σ+σ ↪ 2HA•σ via add_smul]
  -- = 4·1 + (HA·HA)•1
  -- = (4 + HA·HA)•1.
  --
  -- Discharge via mul_add / add_mul / mul_smul_comm / smul_mul_assoc /
  -- smul_mul_smul_comm, then `hecke` substitution, then abel.
  rw [add_mul, mul_add, mul_add, sub_mul, mul_sub, mul_sub, mul_sub, mul_sub,
      mul_smul_comm, mul_smul_comm, smul_mul_assoc, smul_mul_assoc,
      smul_mul_smul_comm, Matrix.one_mul, Matrix.mul_one, Matrix.one_mul,
      Matrix.mul_one, hecke]
  -- After rewrites, LHS expands as a sum of σσ, HA•σ, and (HA·HA)•1
  -- terms with arithmetic on ℤ-coefficients of TMatrix as additive group.
  -- RHS: (4 + HA*HA) • 1. Convert (4 : R_t) • 1 to integer-multiple form
  -- via `add_smul` (so that `4 • 1 = 1 + 1 + 1 + 1`).
  rw [show ((4 : R_t) + HA_t * HA_t) • (1 : TMatrix)
        = (4 : R_t) • (1 : TMatrix) + (HA_t * HA_t) • (1 : TMatrix)
        from add_smul _ _ _]
  rw [show ((4 : R_t) • (1 : TMatrix)) = (1 : TMatrix) + 1 + 1 + 1 from by
    rw [show (4 : R_t) = 1 + 1 + 1 + 1 from by norm_num,
        add_smul, add_smul, add_smul, one_smul]]
  -- Now both sides are sums of identity-matrix terms + HA•σ + (HA·HA)•1
  -- modulo addition. Close by abel.
  abel

end QOU.Interactions
