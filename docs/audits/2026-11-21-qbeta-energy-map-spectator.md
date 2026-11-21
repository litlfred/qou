# The ε → MeV map of the n–p cell: spectator invariance forces a logarithm

Date 2026-11-21. Thread "Derive the n–p cell's E0 and ε→MeV map" (sibling of the eigenphase
thread, PR #8836, and the error-budget thread, PR #8868). Pre-registration:
`computations/probes/qbeta_energy_map/PREREGISTRATION.md` (committed before the probe existed).
Lean: `QOU/QBeta/SpectatorEnergyMap.lean`. Probe: `qbeta_energy_map_probe.py`, 10/10, witness
`qbeta-energy-map.witness.json`. CODATA appears only in §5, never in a proof.

## 1. Result

- **Premise S (spectator invariance):** an energy difference does not change when both states are
  multiplied by one common positive factor. The corpus already treats three things as common
  factors: the shared lepton factor (owner ruling 2026-11-21, "not one-sided yet"), an idle
  strand (the premise PR #8836 used to derive the lepton normalisation), and the choice of global
  normalisation `[2]³` (error-budget link L7).
- **S plus continuity forces E(ε) = c·log ε + d** (`eq_log_of_spectatorInvariant`). The linear map
  the cell uses now fails S (`linear_not_spectatorInvariant`): under it the shared lepton factor
  shrinks the cell by f(1) < 1 (error budget §10), and the L7 normalisation choice moves the q = 1
  coefficient between 0 and 1.
- **Under the log map the cell is −2c·log q for every word, trace and normalisation**
  (`log_cell`). The reason is exact: ε_n/ε_p = q⁻² for every word, because the two weight-space
  traces are equal (`NucleonWeightSpaceTraces.trace_word_eq`). V³, τ and [2]³ all drop out.
  The neutron is the heavier side iff c < 0 (`log_cell_pos_iff`), i.e. a decreasing map, the
  free-energy form E = −|c|·log Z.
- **The scale |c| is not fixed by S.** It is still the open item. With |c| = E₀ the cell lies in
  (2m_e/q², 2m_e/q) for every q > 1 (`log_cell_bounds`). With |c| = E₀^full it stays below 2m_e for
  every q > 1 (`log_cell_tower_lt_two`).

## 2. What this means for the F scans

If S holds, F (the multiplier on the linear cell) is not an energy ratio. Some structural
additions tested on PR #8836 multiply ε_n and ε_p by exactly the same factor: the colour factor
as a separate tensor factor, and unlinked lepton strands (ε_p·f_L). Under the log map those
cancel exactly. For linked words (γγ gluons, linked leptons, gl₆) the log cell is
log(ε_p′/ε_n′) of the new traces, which this probe did **not** compute. The eigenphase thread
reports that its 758-word framing scan shows max |F| falling as the gluon's own framing grows;
that is consistent with, not a test of, S.

**Addendum (eigenphase thread, reanalysis, not pre-registered).** On the committed gluon-strand
witness of PR #8836 (79 γγ words on 4–5 strands, linked gluons), every word has
ε_p′/ε_n′ = ε_p/ε_n of V³ to 1.3e-12, the limit of the 12-digit reference values. So each
gluon word multiplies both nucleons by one common factor, the linear F reported there is exactly
that factor, and the log cell is unchanged for every word. In 16 words both ε′ are negative (same
ratio), where the log is undefined as written; the sign convention for negative traces is open.

## 3. What the log map costs, stated plainly

Under the log map the cell is **only the K-weight step**: moving one unit of T³ changes the
weight by q², and the energy is 2|c|·log q. The dynamical content of the γγ selection (V³, τ) is
gone. So the log map turns the n–p cell into an isospin-charge energy. That is consistent with
the corpus fact that the two weight spaces carry equal plain traces for every word (the
"commutant" obstruction, `commutant_trace_eq`). But it means the β-decay word does not enter the
energy at all. Whether that is acceptable is a modelling question for the owner, not a result.

## 4. The base E₀ (coordinator's question: order zero vs tower)

- E₀ = m_e/(q(q−1)) is "the energy of one Hecke reduction step" (`energy-scale-planck`). The
  tower form divides by 1 − ℏ_q², and E₀^full/E₀ = q²/(2q − 1) exactly (`tower_ratio`): 1.009915
  at the proton q₀. Under either map that is a 1 % effect. It cannot supply ×2.4.
- **Under the linear map** E₀'s 1/h cancels the split's h (error budget `e0_mul_h`), so E₀ enters
  only through its q = 1 coefficient 2.
- **Under the log map** E₀ enters as |c|. The block does not say whether "one step" means energy
  per unit of log-weight (rows L0, LT) or per factor q (rows S0, ST). Both readings were
  pre-registered. Under L0/LT the q = 1 limit of the cell is 2m_e, against 3/4·m_e for the linear
  cell.

## 5. Numbers at the proton q₀ (model), then comparison (outside any proof)

ε_p = 0.408718179341, ε_n = 0.331737644740 (match the coordinator's values to 1e-12),
log q₀ = 0.104341, E₀ = 4.18598 MeV, E₀^full = 4.22748 MeV.

| row | map, scale | cell (MeV) | cell / m_e | vs Q_β | vs m_n − m_p |
|---|---|---|---|---|---|
| linear, E₀ | E₀·\|ε_n − ε_p\| | 0.322239 | 0.630606 | −58.81 % | −75.09 % |
| linear, E₀^full (scored) | E₀^full·\|ε_n − ε_p\| | 0.325434 | 0.636858 | −58.40 % | −74.84 % |
| L0 | log, \|c\| = E₀ | 0.873537 | 1.709469 | +11.66 % | −32.46 % |
| LT | log, \|c\| = E₀^full | 0.882197 | 1.726417 | +12.77 % | −31.79 % |
| S0 | log, \|c\| = E₀/log q | 8.37196 | 16.3835 | +970 % | +547 % |
| ST | log, \|c\| = E₀^full/log q | 8.45497 | 16.5460 | +981 % | +554 % |

CODATA/AME: Q_β = 0.78233 MeV, m_n − m_p = 1.29333 MeV. **No row is selected.**

Two comparison-boundary facts (the arithmetic is in Lean; the measured numbers are not):
- m_n − m_p = 2.531 m_e. Rows L0 and LT are below 2m_e at **every** q > 1. So the log map with
  |c| = E₀ or E₀^full cannot be read as m_n − m_p at any pin.
- Q_β = 1.531 m_e. At the proton q₀ the L0 lower bound is 2/q₀² = 1.623, so L0 overshoots there.
  This is a statement at one pin, not for all q.

## 6. Status of each step

| step | status |
|---|---|
| S ⇒ log (with continuity) | **proved** (Lean), given S |
| S itself | **premise**, motivated by three corpus common factors; not derived |
| ε_n/ε_p = q⁻² for every word | **proved** on main (`trace_word_eq`) |
| log cell = −2c·log q, sign ⇔ c < 0 | **proved** (Lean) |
| tower ratio, bounds on 2E₀·log q | **proved** (Lean) |
| |c| = E₀ or E₀^full | **posited** (the E₀ block); per-log vs per-step reading open |
| reading Q_β vs m_n − m_p | open; the D2 ruling was for the linear cell |

Lean: `SpectatorEnergyMap.lean` compiles with lean-direct (Lean 4.24.0, Mathlib imports only), exit 0,
no `sorry`. All 19 theorems depend only on `propext`, `Classical.choice`, `Quot.sound`.

## 7. Open, framed for the owner

1. **Accept S as a premise?** If yes, the linear cell is retired as an energy, the F scans are
   closed as expected nulls, and the open question becomes the scale |c|. If no, the linear map
   stays and the ×2.4 hunt continues on PR #8836 / #8868.
2. **The scale.** S leaves |c| free. The corpus has only E₀. A derivation would have to say what
   energy one unit of log-weight costs, from CAL-1 and CAL-2. None is on record.

## 8. Deriving the scale |c| (owner: "Try to derive"; pre-registration addendum 1)

**What S already forces.** A scale that rescaled with ε would break S, so |c| cannot carry the
trace normalisation. It is m_e·φ(q), built from CAL-1 and CAL-2 only. This excludes the one
scale that would make the log map agree with the linear map at small differences
(|c| = E₀·ε̄, which gives back the linear cell).

**The corpus reads the trace as a partition function, so |c| is a temperature:**
E(X) = −k_B T·log ε(X), the free energy. Two definitions on record give T, and they disagree.

| route | temperature | |c| | cell | status |
|---|---|---|---|---|
| **T** | `def:quantum-temperature`: k_B T_q = ℏ_q in natural units; energy unit m_e·c_q² (`def:information-speed-of-light`, CAL-1) | m_e·c_q²·ℏ_q = **E₀ exactly** (`kT_eq_e0`) | 2E₀·log q = **0.873537 MeV** (`routeT_cell`) | derived from three definitions on record |
| **D** | `prop:beta-eq-ln-q-dictionary`: β = ln q | 1/ln q in the dictionary's units | **exactly 2 units** (`routeD_cell`) | the dictionary fixes no MeV unit |

So route T **derives** |c| = E₀ (order zero), and with it the base E₀ itself acquires a reading:
E₀ = m_e·c_q²·ℏ_q is the thermal energy k_B T_q, not only "energy per Planck tick". The tower
factor does not come out of route T; it stays ruled, not derived.

**The two temperatures conflict.** β = ln q (dictionary) is strictly below β_q = 1/ℏ_q
(`def:quantum-temperature`) for every 1 < q < 2 (`dictionary_beta_lt_quantum_beta`); at q₀ they
are 0.1043 and 10.093. They are not two forms of one definition. This is a corpus inconsistency,
recorded here, not resolved. Route D's cell in MeV depends on an unstated unit: 2m_e = 1.022 MeV,
or 2m_e·c_q² = 84.5 MeV (diagnostics only).

**Comparison (outside any proof).** Route T: +11.66 % against Q_β; it is below 2m_e for every q,
so it cannot be m_n − m_p (2.531 m_e). Route D with unit m_e: +30.6 % against Q_β, −21.0 %
against m_n − m_p. Nothing selected.

**What is derived and what is not.**
- Derived, given S and the partition-function reading: the log form, the sign, word-independence,
  and |c| = E₀ via route T.
- Not derived: which corpus temperature is the physical one (T or D); whether the tower factor
  belongs; and the reading (Q_β or m_n − m_p) of the cell.

## 9. Reconciled: one Gibbs state, two energy units (owner card "Reconcile first"; addendum 2)

**Correction to §8.** §8 called the two temperatures a corpus inconsistency. That was too strong.
Both readings use the same Boltzmann weight y of the same trace. Equal weights fix only the
product β·E (`same_weight_iff`), so β_D = ln q and β_q = 1/ℏ_q are one Gibbs state written in two
energy units. They would conflict only if a block stated T = 1/ln q in natural units, and none
does: the dictionary's own `.ts` note says "energies are relative to the weights" (grep of
`folio/` for `T = 1/\ln q` and `\beta = \ln q`: only the dictionary block). The inequality
`dictionary_beta_lt_quantum_beta` is true but compares numbers in different units, so it is not
evidence of a conflict. Nothing else repeated the "conflict" wording: this audit, the PR #8904
comment of f821e479a, and the thread reply only.

**The unit.** One dictionary unit is (β_D/β_q) natural units = ℏ_q·ln q·m_e·c_q² = **E₀·ln q**
(`dictionary_unit`). Route D's exact 2 units is then 2E₀·ln q, the route-T cell
(`routeD_converted_eq_routeT`; probe 15/15).

**So the scale is derived, given its premises:**
1. S (spectator invariance) ⇒ E = c·log ε + d (`eq_log_of_spectatorInvariant`);
2. the corpus reads the trace as a Gibbs state ⇒ |c| = k_B T;
3. `def:quantum-temperature` (k_B T_q = ℏ_q) and 𝔈 = 𝔪·c_q² with the CAL-1 unit m_e ⇒
   k_B T = E₀ exactly (`kT_eq_e0`); the dictionary agrees once its unit is fixed (§9).

Result: n − p cell = 2E₀·ln q = 2m_e·ln q/(q(q−1)) = **0.873537 MeV** at the proton q₀, and it
lies in (2m_e/q², 2m_e/q) for every q > 1. No fitted or selected quantity enters. Still not
derived: the tower factor (ruled, +1 %), and which observable the cell is. Comparison (outside any
proof): +11.66 % against Q_β; it cannot be m_n − m_p (below 2m_e at every q).

**Note (eigenphase thread, PR #8836 commit 6222f1f6c1).** `QOU/QBeta/QuarkWeightTrace.lean`
(sorry-free there) gives the same-trace premise a representation-theoretic proof: Jimbo R commutes
with Δ(F), Δ³(F) intertwines the two quark sectors, so ε_p = q²·ε_n. Its extension to the
K-weighted partial trace over extra strands is checked numerically (q = 2, 3/2, 79 gluon words),
not proved. Its epsP/epsN match this file's, so the two can be joined.

## 10. Spectator invariance is a consequence, not an axiom (owner, 18:00Z)

Owner: S "should follow from QOU, no hidden symmetry axioms". It does, from two facts the corpus
already holds:

1. **The trace multiplies over disjoint parts.** `markov-axioms-primitive` derives
   tr_M(K₁ ⊔ K₂) = tr_M(K₁)·tr_M(K₂) from the Markov axioms. For the convention-D quantum trace it
   is `trace_kron`: K^{⊗(n+m)} = K^{⊗n} ⊗ K^{⊗m} because K is grouplike (Δ(K) = K ⊗ K), and
   [2]^{n+m} = [2]^n·[2]^m.
2. **Energy adds over non-interacting parts.** The corpus's own energy reading of the trace,
   `prop:beta-eq-ln-q-dictionary` (E = −ln y/β), is additive outright. More basically, the generator
   H = log_q K of the grouplike weight is primitive, so weights q^i, q^j combine to exponent i + j
   (`grouplike_weight`).

Then `spectator_of_additive`: additive energy on a multiplicative trace satisfies S. A spectator is
just a non-interacting part: an unlinked lepton factor, an idle strand, a global normalisation.
With continuity, S and additivity are equivalent, and both force the log (§1). So the chain is
"trace multiplies + energy adds ⇒ energy = c·log(trace)". No symmetry is assumed beyond the
grouplike K of U_q(sl₂), which is the corpus's convention D.

**Direct route, without Φ.** Because the energy generator is H = log_q K, the n–p cell can be read
without any map of the full trace: n and p differ by ΔH = 2 (one u → d), and the plain traces are
equal (`trace_word_eq`), so the Gibbs energy difference is 2·k_B T·ln q = 2E₀·ln q (§8–9).

**What is still assumed.** That the n–p energy is an energy of the Gibbs state the trace
defines, i.e. the corpus's partition-function reading applied to the T³ sectors. The dictionary
block states it for Wedderburn blocks; applying it to weight-space sectors is one step beyond
that block, and is named here rather than hidden.

## 11. The Gibbs reading on T³ sectors is the dictionary's own microstates

§10 named one step: the dictionary (E = −ln y/β, β = ln q) is stated for Wedderburn blocks, and
the n–p cell uses T³ weight-space sectors. That step is not new. Under Schur–Weyl a block's
U_q(sl₂) factor V_λ has a K-eigenbasis, and its quantum trace is Tr(K|V_λ) = Σ_μ q^μ over the
weights μ of V_λ. Each q^μ is a Boltzmann weight at β = ln q with energy −μ (`state_weight`;
one strand: [2]_q = q + q⁻¹ is the two-state partition function, `qd2_is_partition`). So the
block weight is itself a partition function over the K-weight states, and the T³ sectors are
those states. The sector energy difference n − p is the weight difference ΔH = 2 times
k_B T·ln q.

**Chain, with nothing hidden:**
1. convention-D trace = Tr(K^{⊗n}·)/[2]^n (corpus, bean `qou-99qc`);
2. K grouplike ⇒ trace multiplies over disjoint parts, H = log_q K additive (§10);
3. the corpus Gibbs reading at β = ln q, whose microstates are the K-weight states (§11);
4. k_B T in MeV = m_e·c_q²·ℏ_q = E₀ (`def:quantum-temperature`, `def:information-speed-of-light`,
   CAL-1), with the dictionary unit reconciled (§9);
5. result: n–p cell = 2E₀·ln q = 0.873537 MeV at the proton q₀.

**Still open:** the tower factor (ruled, +1 %); the reading of the cell (Q_β or m_n − m_p). The
cell ignores the β-decay word (§3).

## 12. Owner "Both": the tower factor, and the reading of the cell (prereg Addendum 3)

**Q1, tower factor.** The tower factor T = 1/(1 − ℏ_q²) = Σ_N ℏ_q^{2N} is word-independent and
the same for n and p. Under the full-tower ruling (2026-09-03) it belongs to the fibre object,
that is, to the partition function, and a common factor of Z is a spectator. So it cancels from the
cell exactly: `common_factor_log_cell` (any T > 0) with `tower_factor_pos` (T > 0 for q > 1).
The derived cell is therefore the order-zero **2E₀·ln q = 0.873537 MeV**, not 2E₀^full·ln q.

The alternative, T rescaling k_B T, is the corpus's current E₀^full and gives 0.882197 MeV. Nothing
in the chain of §10–11 puts T into k_B T: `def:quantum-temperature` is ℏ_q with no tower sum.
That reading is reported beside the derived one and is not chosen.

**Q2, reading.** Under the ruled shared placement (owner 2026-11-21, "not one-sided yet") the
lepton factor L multiplies both nucleons, so by the same lemma the cell is
E(n⊗L) − E(p⊗L) = E(n) − E(p). That is a nucleon energy difference with no electron rest energy
in it, i.e. the shape of m_n − m_p, not of Q_β = m_n − m_p − m_e.

But the cell cannot be m_n − m_p at any q. `log_cell_bounds` and `log_cell_tower_lt_two` give
cell < 2·m_e for every q > 1. Measured m_n − m_p is 2.531 m_e (CODATA, compared only in the
probe, not in Lean). So under the derived map the m_n − m_p reading is excluded for every q,
scope (b), invariant `log_cell_bounds`. The Q_β reading is +11.66 % (order zero) or +12.77 %
(tower).

**Tension with D2.** D2 (Q_β) was ruled for the linear cell. The derivation's own placement points
at m_n − m_p, which the bound excludes. Both statements are true. Which one the cell is goes to the
owner; it is not changed here.

**Structural reading (new, proved as an identity only).** −2c·ln q = −c·ln(q/q⁻¹)
(`cell_eq_eigen_gap`): q and −q⁻¹ are the two eigenvalues of one Hecke crossing, so in the Gibbs
reading the cell is k_B T times the log-ratio of the symmetric and antisymmetric channels of
one reduction σ² → hσ + 1. With `E0ReductionWordCount` (E₀/m_e = the q⁻¹-weighted count of words
that need that reduction), this links the cell to the owner's GB proposal (2026-11-21: β-decay as
the difference between the unreduced and reduced interaction word). That link is an observation,
not a derivation. It is the next preregistered item.

## 13. Owner: "Reevaluate lepton placement"

Owner ruling recorded first: the cell is not assigned to an observable until the GB reduction is
done (card "Neither yet").

The "shared" placement (error-budget §10, "not one-sided yet") treats the lepton factor L as a
spectator on both sides. That is not what β-decay does: in the final state the lepton is either
**created** (it is absent from the initial state) or it **changes state** (ν → e⁻). Three
placements, each with what the derived log map gives. Nothing here is chosen.

**A. Shared spectator (current ruling).** L on both sides cancels (`common_factor_log_cell`), so the
cell is E(n) − E(p), with the shape of m_n − m_p. `log_cell_bounds` gives cell < 2·m_e for every
q > 1, and measured m_n − m_p is 2.53 m_e, so under the derived map this reading cannot hold at any
q. The placement is consistent with the map only if the cell is not an observable on its own.

**B. One-sided (pair created in the final state only).** E(n) = E(p) + E(e⁻) + E(ν̄) + Q_β, so
Q_β = cell − E(e⁻) − E(ν̄). With E(e⁻) = m_e (CAL-1) and E(ν̄) not fixed by the corpus, this is an
upper bound: Q_β ≤ (1.709469 − 1)·m_e = 0.362538 MeV. This number is computed after the comparison
in §5 was printed, so it is not blind; it is reported, not proposed.

**C. Active lepton strand (premise L, the 4-strand process word of
`2026-11-21-beta-pair-creation-word-proposal.md`).** The lepton strand carries ν = u and e⁻ = d.
In H = log_q K units: n ⊗ ν = (−1) + (+1) = 0 and p ⊗ e⁻ = (+1) + (−1) = 0. So the T³ weight is
conserved, which is principle Q of that audit (Hecke elements commute with U_q). The nucleon's
+2 log q is cancelled exactly by the lepton's −2 log q, and the whole T³ log cell of this thread is
zero for the full process. Whatever energy is released must then come from the non-weight part,
the CC block of the process word, i.e. from the GB reduction itself. Premise L is not ruled
(#8673).

**Consequence for this thread.** The derived 2E₀·ln q is the nucleon half of a T³ bookkeeping that
cancels in C, a cell with an excluded reading in A, and an input to a bound in B. In none of
the three is it Q_β by itself. That moves the weight of the question onto the GB reduction, as the
owner ruled.

## 14. β-decay as a GB reduction: first measurement (prereg Addenda 4–5)

Owner proposal: β-decay as the difference between the unreduced and reduced interaction word.
Worked under placement C (active lepton strand, premise L), which is pending the owner's card. The
word is the pair-creation proposal's minimal G ∧ CC ∧ R3 candidate X = V₁³ = (σ₁σ₂⁻¹)³, not ruled,
acting on β_Bor: W = X·β_Bor, 24 letters, normal form 17 terms (reproduces the pair-creation
witness). Probe `qbeta_gb_reduction_probe.py`, 6/6 checks; witness
`qbeta-gb-reduction.witness.json`. Exact in ℚ(q), proton q₀, 60 dps.

| measure | S1 (right mult.) | S2 (left mult.) | × E₀ (MeV) | vs Q_β |
|---|---|---|---|---|
| M1 rule firings in W | 76 | 78 | 318 / 327 | ×400 |
| M2 q⁻¹-weighted firings | 54.62 | 55.76 | 229 / 233 | ×290 |
| ΔM1 = M1(Xβ) − M1(β) − M1(X) | 48 | 46 | 201 / 193 | ×250 |
| ΔM2 (exact: (4q⁴+19q³+18q²+3q+4)/q⁶ and (q+1)(q⁴+4q³+6q²+10q+2)/q⁶) | 32.92 | 31.00 | 138 / 130 | ×170 |
| M3 kT·ln(‖CC block‖/‖diag block‖) | −12.31 MeV | | | ×16 |

**Result, scope (a).** With E₀ as the energy per reduction step, this word and these measures
give energies two orders of magnitude above Q_β (M3 one order). The counts also depend on the
rewriting strategy (76 vs 78, 48 vs 46), so a raw count is not yet a well-defined invariant.

**Structural point (why the counts cannot be the n–p cell).** M1, M2 and ΔM are functions of the
algebra element W alone. They take no state as input, so they are the same for n⊗ν → p⊗e⁻, for
the reverse, and for every other transition the word mediates. An n–p asymmetry can only come
from a quantity evaluated on states (the module V^{⊗4}): M3, or the T³ weight, which cancels under
premise L (§13 C). So within this route the GB reading has to be taken on the module, not on the
algebra. That is a statement about these measures. It does not exclude a state-level reduction
count (e.g. counting reductions in the matrix entry ⟨p⊗e⁻|ρ(W)|n⊗ν⟩ term by term), which was not
preregistered and is not run here.

Contamination: Addendum 5 (ΔM) was written after Addendum 4's numbers were printed.

## 15. State-level reduction count, three words, placements B and C (prereg Addenda 6, 6b)

Probe `qbeta_gb_state_reduction_probe.py`, 9/9 checks (each word's normal form is
strategy-independent; each marked block at t = 1 reproduces the `analyse_element` CC and reverse
block sums). Witness `qbeta-gb-state-reduction.witness.json`. A *firing* is a Jimbo step whose
weight comes from a reduction (the h·du branch or the −h of an inverse). ⟨k⟩ = E′(1)/E(1) is the
amplitude-weighted mean number of firings in a block. A = ⟨k⟩_forward − ⟨k⟩_reverse.

| X (W = X·β_Bor) | ⟨k⟩_f·E₀ | ⟨k⟩_r·E₀ | **A·E₀** | (F/P)_f·E₀ | ΔM2·E₀ (S1 / S2) |
|---|---|---|---|---|---|
| V₁³ | 11.88 | 12.52 | **−0.648** | 18.77 | 138 / 130 |
| V₀V₁V₀V₁ | 3.03 | 3.13 | **−0.099** | 21.97 | 83 / 158 |
| V₁V₀V₁V₀ | 2.74 | 3.01 | **−0.265** | 21.67 | 108 / 86 |

(MeV. Q_β = 0.782, m_n − m_p = 1.293, printed last in the witness.)

**B equals C on the module, exactly.** Under B the input lepton-strand colour is summed over
{u, d}. The d input has total T³ weight −2, the p⊗e⁻ output has 0, and the Jimbo Ř preserves
weight, so the d input contributes zero. The B block is the C block for every word and every
measure. So on V^{⊗4} the choice between B and C does not change any reduction count. They
differ only in how the lepton's own energy is booked (§13 B: Q_β ≤ cell − m_e = 0.3625 MeV with
E(ν̄) open).

**What the numbers say, scope (a).**
- Absolute state-level counts (⟨k⟩·E₀, F/P·E₀) are 3–22 MeV, between 3× and 30× Q_β. The
  element-level ΔM stays at 80–230 MeV. Neither family is the n–p release.
- The forward/reverse asymmetry A is the only state-level quantity that separates n⊗ν → p⊗e⁻ from
  its reverse. It is negative for all three words (the forward transition needs fewer reductions
  than the reverse), and |A|·E₀ is 0.099, 0.265 and 0.648 MeV. The three admissible words give
  three different values, spread over a factor of 6.5.
- **Caution, stated plainly.** |A|·E₀ for V₁³ is 17 % below Q_β. That is one word out of three,
  and V₁³ is a proposal, not a ruling. Selecting V₁³ because of this number would be selection
  against the target (AGENTS.md §NO FITTING). ⟨k⟩ is a signed-amplitude average (the diagonal block
  gives negative ⟨k⟩), so it is not a probability-weighted count, and E₀ as "energy per firing"
  is the §14 reading, not a derivation.

**Status.** The GB-reduction route has one state-level observable with the right sign structure
(A, forward cheaper than reverse) and the right order of magnitude (0.1–0.65 MeV). Its value
depends on the β-decay word, which is not ruled. Deriving A, or selecting the word by a principle
that does not read Q_β, is the open step.

## 16. Reversing the GB ordering (prereg Addendum 7; owner "1 2" and "reverse the GB ordering")

Probe `qbeta_gb_ordering_reversal_probe.py`, 6/6 (the marking never changes the amplitudes at
t = 1). Witness `qbeta-gb-ordering-reversal.witness.json`. A·E₀ in MeV:

| X | standard | R1 (σ⁻¹ leading) | R2 (d < u) | R1+R2 |
|---|---|---|---|---|
| V₁³ | −0.648 | −0.069 | +0.648 | +0.069 |
| V₀V₁V₀V₁ | −0.099 | +0.147 | +0.099 | −0.147 |
| V₁V₀V₁V₀ | −0.265 | −0.318 | +0.265 | +0.318 |

Preregistered tests:
- **R2 is the p ↔ n swap, exactly.** A ↦ −A for every word, as an identity in ℚ(q). Reversing the
  colour order turns n⊗ν → p⊗e⁻ into the reverse transition and nothing else. So yes, the ordering
  reversal "goes between p and n", but it only flips the sign. It does not change any magnitude.
- **R1 changes A**, for every word, in size and in one case in sign (V₀V₁V₀V₁). So A is **not an
  invariant of the algebra element**. It depends on which normal form the reductions are counted
  in.
- **Word-independence (criterion i): fails under all four orderings.** No ordering makes A the
  same for the three admissible words. Criterion (ii), a shared closed form, also fails: the exact
  A are distinct rational functions of degree ~30 (witness), vanishing at q = 1 to orders 1, 2, 2.

**What is fixed by the corpus, and what is not.** The corpus's GS basis is the standard one:
leading term σᵢ² → hσᵢ + 1 (`hecke_exact.py`, `E0ReductionWordCount.lean`) and the Jimbo colour
order u < d (`jimbo.py`, `ChargedCurrentW`). So the standard column is the corpus-fixed ordering,
R2 is a relabelling of n and p, and R1 is a different convention the corpus does not use. The word
is not fixed. The pair-creation proposal's own minimality principle (fewest crossings among
G ∧ CC ∧ R3, set before any Q_β reading) picks V₁³, but that proposal is not ruled.

**Owner item 2 (closed form).** The exact A are in the witnesses. They are high-degree rational
functions with no visible structure. A Lean statement of them would be a verified polynomial
identity, not a derivation, and given the R1 dependence it would certify an ordering artifact.
Not formalized, and the reason is stated here.

**Status, scope (a).** The ordering reversal is a clean p ↔ n symmetry (sign only). It does not make
the asymmetry word-independent or ordering-independent. The GB-reduction reading of Q_β, as
measured by A, therefore rests on two inputs the corpus does not derive: the β-decay word, and the
choice of normal form for counting (σ leading is the corpus convention, but a convention).

## 17. Ordering-averaged asymmetry and colour on strands (prereg Addendum 8; owner "Both")

**(a) Averaging over the 8 per-generator orderings** (colour order fixed, u < d). Probe
`qbeta_gb_ordering_reversal_probe.py`, 9/9. A·E₀ in MeV:

| X | mean of 8 | spread of the 8 (max − min) |
|---|---|---|
| V₁³ | −0.358 | 7.36 |
| V₀V₁V₀V₁ | +0.024 | 0.40 |
| V₁V₀V₁V₀ | −0.292 | 0.66 |

Not word-independent, and the sign is not even common to the three words. For V₁³ the spread across
orderings (7.4 MeV) is eleven times the standard-ordering value. **Result, scope (a):** the
forward/reverse reduction asymmetry is a property of the counting ordering at least as much as of
the word. The averaged version does not repair it. On this evidence A is not a candidate for a
derived Q_β; §15's "right order of magnitude" was specific to one ordering.

**(b) Colour on strands, against the corpus.**
- `bring_color_weighted` is the inter-nucleon p–n interface factor, f_pn = z − h(1/2 − δ/4). It does
  not act inside a single-nucleon β-decay word.
- The colour frame σᵢ^{sl} = q^{−1/N}σᵢ multiplies a word by q^{−writhe/N}. All three W have writhe 0
  (checked), so the frame changes nothing here. That is a consequence of the γγ rule:
  `writhe_eq_zero`.
- A flavour ⊗ colour strand space (dim 6, gl₆ Jimbo Ř) is not defined in the corpus, and would
  give weight to three-row shapes, which convention D sets to 0. Not built; put to the owner.

So in the corpus as it stands, colour does not enter this computation at all: one ruled
colour object acts between nucleons, the other is trivial on writhe-0 words.

## 18. p–n constructions: derived versus asserted (prereg Addendum 9; owner relaxed the p–n ruling)

The owner relaxed the 2026-08-15 p–n colour-weighting ruling and asked for derivation, not assertion.
The ledger is in Addendum 9. Result of reading the corpus:

- **One p–n quantity is derived at every step**: the cell 2E₀·ln q (§1, §12). Its assignment to an
  observable is open, and it cannot be m_n − m_p at any q (cell < 2m_e).
- **Every construction carrying δ is asserted.** δ = `flavor_split_leading` comes from
  prop:flavor-split-substrate, whose Step 2 is fitted to experiment (the proof says so) and whose Step 1
  is the convention-C pair-Skein formula with per-quark masses as inputs. `bring_color_weighted`, the
  Bring linking weight (0.887 MeV) and `flavor_split_subleading` all inherit it; the last is marked
  POSITED and the linking weight also inherits the λ_A absolute-mass fit.
- **The linear cell 0.325 MeV** fails spectator invariance (§1).

Derivation routes R-a to R-d are listed in Addendum 9 with their comparison values recorded in advance.
The only route that ties the derived cell to m_n − m_p, R-c, needs two derivations not yet done: the
pair-Skein crossing trace under z_D (which would give [2]_q·z_D = q² exactly), and μ_d − μ_u equal to
the cell. Its comparison value, q²·cell = 1.0762 MeV (−16.79 %), is not evidence for it.
