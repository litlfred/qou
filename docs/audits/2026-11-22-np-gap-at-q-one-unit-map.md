# The n–p gap at q = 1: the E₀ pole and the categorical mass (2026-11-22)

Issue #9002. Follows PR #8955 (audit `2026-11-21-qbeta-energy-map-spectator.md` §30) and the
owner working assumption m_p = m_n at q = 1 (bean `qou-az9l`). Two questions:

1. Which CAL-1 unit map (m_e → MeV) keeps m_p = m_n at q = 1, given that the n–p cell
   2E₀ ln q tends to 2m_e there? Derived, not fitted.
2. (Owner) Can the working assumption be proved from the definition of categorical mass?

Probe: [`computations/qbeta/np_gap_q_one_probe.py`](../../computations/qbeta/np_gap_q_one_probe.py)
(Part A exact over ℚ(q) with sympy; Part B mpmath at 40 digits).
Lean: [`QOU/MassTheory/CategoricalMassAtOne.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/CategoricalMassAtOne.lean)
(`scripts/lean-verify.sh` exit 0, no `sorry`, `#print axioms` gives propext, Classical.choice, Quot.sound only).
Precision gates (`--changed`): no report names the probe. The red ratchets are the same tree-wide ones PR #8955 reported.

## 1. Answer to question 2: yes, the categorical mass at q = 1 counts components

`def:mass-identity` defines the mass of a braid class as the framing-corrected Jones–Markov trace
(1 + q²)ⁿ q^(−n−2w(β)) ∫_A ρ(β). At q = 1:

- h = q − q⁻¹ = 0, so the Hecke generator is the strand swap and ρ(β) is the permutation
  operator of the image π ∈ Sₙ on V^⊗n, V = R² (bridge lemma of `FlipSymmetryAtOneBridge`, PR #8804);
- K = 1 and the framing factor is 2ⁿ for every writhe (`framing_factor_at_one`);
- the trace of a permutation operator on (R²)^⊗n is the number of colourings f : Fin n → Fin 2 with
  f ∘ π = f, which is 2^c with c the number of cycles of π, i.e. the number of components of the
  closure (`card_fixedColouring`, proved);
- so the mass is 2ⁿ · 2^c / 2ⁿ = **2^c** (`mass_at_one`).

**Theorem.** At q = 1 the categorical mass of a braid class is 2^(number of components of its
closure). Two braids whose closures have the same number of components have equal mass at q = 1
(`mass_at_one_eq_of_components`).

The nucleon core β_Bor = (σ₀σ₁⁻¹)³ closes to the Borromean rings (3 components), and so does any
assignment of p and n to β_Bor and its mirror. So **m_p = m_n = 8 at q = 1** in mass units, from the
definition alone. The electron σ₀σ₁σ₀ (Hopf closure, 2 components) has mass 4, so m_p/m_e = 2 at
q = 1, finite.

Exact check (Part A of the probe):

| braid | closure | m(q) | m(1) |
|---|---|---|---|
| (σ₁σ₂⁻¹)³ | Borromean, 3 | −(q²+1)(q¹² − 3q¹⁰ + 2q⁸ − 4q⁶ + 2q⁴ − 3q² + 1)/q⁷ | 8 |
| (σ₁⁻¹σ₂)³ | mirror, 3 | same | 8 |
| σ₁σ₂σ₁ | Hopf, 2 | (q²+1)(q⁴+1)/q⁶ | 4 |
| σ₁³ | trefoil, 1 | (q²+1)(q⁶+q²−1)/q⁹ | 2 |

Markov invariance holds under ± stabilisation, and m(mirror β)(q) = m(β)(q⁻¹).

Two consequences that go beyond the working assumption, both measured above:

- **The bare closure gives no n–p split at any q.** The Borromean rings are amphichiral, so the
  closure mass of β_Bor and of its mirror agree as rational functions. The n–p difference cannot
  come from the closure of the core. It has to come from decorations of the braid (strand labels,
  framing, the lepton strand, the Markov-trace convention), which is where PR #8955's cell lives.
- **The scope condition is the component count.** Any decoration that keeps both nucleons at the
  same number of components keeps m_p = m_n at q = 1. A decoration that changes the count on one
  side only would break it. This is the categorical form of bean `qou-az9l`, and it is narrower
  than "every braid-built term vanishes" only in that it is stated for the closure mass.

Scope (a): the theorem is about `def:mass-identity`. The production identity
m_p/m_e = 2(Vol/ℏ_q²)F_Bor − 12 is a different object; its 1/ℏ_q² diverges at q = 1, so it does not
reduce to 2^c there. That mismatch is recorded, not resolved.

## 2. Answer to question 1: read the cell as a mass, through `def:mass-energy`

The corpus defines energy from mass by 𝔈 = 𝔪·c_q², c_q = 1/(q − 1) (`def:mass-energy`,
`def:information-speed-of-light`). The cell is a Gibbs energy 2k_B T ln q with k_B T = E₀ =
m_e c_q² ℏ_q (route T, audit §8–9): it is an energy 𝔈. The comparison target m_n − m_p, and the unit
m_e it is quoted in, are masses 𝔪 (m_p/m_e in the production identity is a mass ratio).

The current reading divides an energy by a mass: ΔE/m_e = 2 c_q² ℏ_q ln q = 2 ln q/(q(q − 1)). The
pole at q = 1 is the factor c_q² = 1/(q − 1)², the model's own speed of light, which diverges at
q = 1. Proved: this ratio is ≥ 2/q² for q > 1 (`cell_energy_ratio_ge`), so it does not vanish.

Read like with like, the cell as a mass is

  Δ𝔪 = ΔE / c_q² = **2 m_e ℏ_q ln q**   (`cell_mass_eq`),

with 0 ≤ ℏ_q ln q ≤ (q − 1)² for q ≥ 1 (`hbar_log_bounds`). It vanishes at q = 1, to second order.
The same ratio 2ℏ_q ln q comes out if CAL-1 is instead read as the electron's energy
(𝔈_e = m_e c_q² = 0.511 MeV): both consistent readings give Δ/m_e = 2ℏ_q ln q. Only the mixed
reading has the pole.

**So the unit map that keeps m_p = m_n at q = 1 is derived: compare masses with masses, converting
the cell energy by `def:mass-energy`.** Nothing is fitted; the three definitions are on record.

The cost, at the comparison boundary only (proton q₀ = 1.10997858275138, Part B):

| reading | n–p cell | / m_e | vs CODATA m_n − m_p = 1.29333236 MeV |
|---|---|---|---|
| energy / mass (current, has the pole) | 0.8735366214 MeV | 1.709468523 | −32.46 % |
| mass / mass (`def:mass-energy`) | 0.01056567759 MeV | 0.02067651525 | −99.18 % |

The consistent reading makes the cell about 122 times too small to be m_n − m_p. Per the anti-fit
ruling this ranks above the current reading, not below it: the current reading's better number comes
from a factor c_q² ≈ 82.68 that mixes two kinds of quantity.

## 3. What this changes

- Audit `2026-11-21-qbeta-energy-map-spectator.md` §30 bullet 2 ("the MeV map does not settle it"):
  settled. The pole is the c_q² of a mixed energy/mass comparison, not a property of CAL-1 itself.
- Every MeV figure that multiplies a dimensionless *energy* by E₀ and compares it to a *mass*
  difference carries the same c_q² ≈ 82.68. This includes the n–p cell rows of §3 and §8–9 of the
  spectator audit. Binding energies compared to AME B (an energy) are not affected by this argument,
  provided B is compared as an energy. Which other comparisons are mixed has not been audited.
- Bean `qou-az9l` item 4 (unit maps with poles): the E₀ case is the c_q² factor, and it disappears
  under `def:mass-energy`.

## 4. Status

| claim | status |
|---|---|
| fixed-colouring count = 2^components | proved (Lean, `card_fixedColouring`) |
| mass at q = 1 = 2^components, given the q = 1 bridge | proved (Lean `mass_at_one`; bridge from PR #8804) |
| m_p = m_n at q = 1 for the closure mass | proved (corollary) |
| closure mass of β_Bor equals that of its mirror at every q | exact computation (probe Part A) |
| E₀ cell / m_e ≥ 2/q² | proved (Lean) |
| cell / c_q² = 2m_e ℏ_q ln q, bounded by 2m_e(q − 1)² | proved (Lean) |
| the cell is an energy and m_n − m_p a mass | reading of `def:mass-energy` and route T |
| the mass reading gives m_n − m_p | refuted at the comparison boundary, scope (a): this cell, alone, −99.18 % |
