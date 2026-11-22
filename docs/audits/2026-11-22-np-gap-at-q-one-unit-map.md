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

**So the unit map that keeps m_p = m_n at q = 1 is: compare masses with masses, converting
the cell energy by `def:mass-energy`.** Nothing is fitted. **Correction (§5): this is derived only
under one reading of `c_q²`, and that reading conflicts with the CAL-2 pin. It is an owner decision,
not a derivation.**

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
  spectator audit. ~~Binding energies compared to AME B (an energy) are not affected by this argument,
  provided B is compared as an energy.~~ [Edit 2026-11-22: wrong. Experiment uses c = 1, so an
  experimental energy and an experimental mass are the same MeV. If c_q² converts mass to energy, every
  E₀-scaled row is off by c_q², binding included. See §5.]
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

## 5. The pole audit: which MeV comparisons mix energy and mass (owner: "Also investigate the pole")

**Result: there is no row-by-row answer. Either every E₀-scaled comparison is mixed, or none is.**
Experimental tables use c = 1, so a measured energy (Q_β, AME B) and a measured mass (m_n − m_p) are
in the same MeV. The model has c_q = 1/(q − 1) ≈ 9.093 at q₀. So the question is one global fact about
`def:mass-energy`, 𝔈 = 𝔪·c_q²:

- **Reading (i): c_q² converts mass to energy.** CAL-1 fixes 𝔪_e = 0.511 MeV. Then E₀ = 𝔪_e c_q² ℏ_q is
  an energy in model units, and to meet a c = 1 table it must be divided by c_q² = 82.6768196923.
- **Reading (ii): c_q² is a pure number inside the formula.** Model energy and mass share the MeV, as in
  experiment. Nothing is mixed.

Measured at the proton pin q₀ = 1.10997858275138 (40 dps, `tools/qou-substrate` constants):

| scored comparison | value now (reading ii) | ÷ c_q² (reading i) | vs target, reading i |
|---|---|---|---|
| Q_β dashboard row, \|ε_n − ε_p\|·E₀ on V³ | 0.325433928735 MeV | 0.003936217309 MeV | −99.497 % |
| Q_β ruled z_D cell, \|tr\|·E₀ | 0.4447004085 MeV | 0.00537877981 MeV | −99.312 % |
| vertex budget, placement B (PR #8955 §27–29) | 0.420 MeV | 0.005080021239 MeV | −99.351 % |
| vertex budget, placement C | 0.782 MeV | 0.009458515735 MeV | −98.791 % |
| n–p cell 2E₀ ln q | 0.8735366214 MeV | 0.01056567759 MeV | −99.183 % |
| binding at α = E₀ (every isotope) | as on the dashboards | value / 82.68 | ≈ −99 % for all |

Targets: CODATA Q_β = 0.782333559310 MeV, m_n − m_p = 1.29333236 MeV.

The `m_n` and `Δ_pn` dashboard rows are m_p + Q_β + m_e. They add the E₀-scaled Q_β to two masses, so
they are mixed under reading (i) and consistent under reading (ii).

**Why reading (i) cannot be adopted alone: the q₀ pin uses c_q² as a pure number.** CAL-2 is
m_μ/m_e = Vol(4₁)/ℏ_q², and 1/ℏ_q² = q²·c_q². The proton pin m_p/m_e = 2(Vol/ℏ_q²)F_Bor − 12 has the
same factor. Both are mass ratios with c_q² inside. Under reading (i) the muon relation would read as an
energy over a mass; the mass-over-mass version would be m_μ/m_e = Vol·q², which needs q = 10.09267839,
not 1.10998. So reading (i) breaks the calibration that fixes q₀. That is a measured conflict, not a
proof that reading (ii) is right.

**What this changes in §1–§4.** The theorem of §1 (mass at q = 1 is 2^components, so m_p = m_n there)
does not depend on either reading and stands. §2's "the unit map is derived" holds only under reading (i)
and is corrected above. Under reading (ii), the pole of the MeV n–p cell at q = 1 is real: the cell is not
the closure mass, and the working assumption m_p = m_n at q = 1 holds for the closure mass but not for this
cell.

**Owner decision (nothing is changed until it is made).**

1. Reading (ii), c_q² is a pure number (my recommendation, as judgement). Costs nothing: no number moves.
   It keeps CAL-2 and the q₀ pin. It commits to: `def:mass-energy` is a model definition and not the c = 1
   conversion, and the n–p cell's pole at q = 1 is a real property of that cell.
2. Reading (i), c_q² converts. Every E₀ row in the table above falls by 82.68 (all near −99 %), and CAL-2
   and the proton pin must be re-derived, which moves q₀ itself. Large blast radius: every witness that
   reads q₀.
3. A split reading (c_q² converts only for some objects). Needs a rule saying which objects, and that rule
   would be a selection unless it is derived.

Default if nothing is decided: reading (ii) stays in force, as it is today in every producer.

**Corroboration (sibling thread, bean `qou-91w7`, 2026-11-22).** That thread traced the canonical
mass pipeline. Steps 1–8 lie in ℚ(q) and contain no c_q. c_q is defined as q⁻¹/ℏ_q, a ratio of two
coupling weights, so it is dimensionless whenever ℏ_q is; and the CAL-2 pin needs ℏ_q to be a pure
number. This makes the reading (i) conflict sharper. It also records a second issue, separate from the
reading: the corpus attaches MeV to energies in two ways. E₀ = m_e·c_q²·ℏ_q is used for Q_β, the log
binding and the n–p cell. The cheat-sheet's step-9 binding B = m_e·ρ·[…] carries no c_q². The two
differ by c_q²ℏ_q; no ruling yet says which is canonical.
