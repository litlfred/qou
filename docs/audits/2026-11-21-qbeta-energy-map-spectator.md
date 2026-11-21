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
