# Route 1 for `BraidBoostInertialEquivalence`: clock-Lagrangian inertial mass (bean `qou-2k68`)

**Question (owner, 2026-11-25).** Derive `BraidBoostInertialEquivalence`
(`QOU/Core/CategoricalHamiltonianLegendre.lean`). As stated, the class equates two *free*
functions, so it first needs a definition of inertial mass. Owner option 1 was to define it
as the Reeb-clock kinetic coefficient of the categorical Lagrangian:

    m_clock(β) := 2 a₂ = 2 ℏ_q² τ(reeb ≫ reeb).

**Identification used.**
- `reeb_holonomy_leftTrace_eq_functional_hol` (Stokes hypothesis, `frobeniusForm = counit`)
  turns `τ(reeb²)` into `casimir ≫ leftMul(hol w) ≫ ∫_A`.
- `def:mass-identity` states that this Casimir-weighted functional is the **regular**
  trace `Σ_λ f^λ χ_λ`, not the Markov trace.
- The target is `𝔪(β) = (1+q²)ⁿ q^(−n−2w) tr_M(β)`, with `tr_M` the convention-D Markov trace.

**Pre-registered predictions and outcome.** Exact computation in `H₂(q)` and `H₃(q)`, 9 braids;
point values at the proton-pinned q₀, 80 dps:

| prediction | result |
|---|---|
| P1 `m_clock/𝔪` is not identically 1 | **holds** for all 9 braids |
| P2 the ratio depends on the braid | **holds**: 8 distinct rational functions |
| P3 `m_clock(1) = 0` while `𝔪(1) = 2^components` | **holds** for all 9 |

At q₀ the ratio ranges from about −8.5·10⁻⁴ (`σ₁σ₂⁻¹`) to 1.4·10⁻² (the Borromean word).
It changes sign, because the regular trace of `σ₁σ₂⁻¹` is negative where the Markov trace is
positive. The consistency check `𝔪(1) = 2^c` (unknot 2, Hopf 4, unlinks 4 and 8, Borromean 8)
confirms the representations and the convention-D weights.

**Scope.**
- (a), for this definition: the clock-coefficient inertial mass is not the holonomy mass `𝔪`,
  and no constant rescaling of the clock variable can make it so (P2).
- Structural part (b), with invariant = order of vanishing at q = 1: any definition of the form
  `ℏ_q² × (a trace finite at q = 1)` has a double zero at q = 1, while
  `𝔪(1) = 2^components > 0` (`MarkovTraceClassicalLimit`). So no such definition can satisfy
  the class for any braid. This is the same obstruction that `QOU/QBeta/E0WeightAllWords.lean`
  proves for E₀'s weight.
- Not excluded: a definition that carries a compensating `1/ℏ_q²` (for example through the
  map from the clock rate ω to the horizontal velocity v, which this route leaves open), or
  owner option 2 (an explicit boost action).

Files: `braid_boost_inertial_clock_probe.py`, `braid-boost-inertial-clock.witness.json`.
