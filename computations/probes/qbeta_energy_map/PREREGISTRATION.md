# Pre-registration: the ε → MeV map from spectator invariance, and the base E₀ (2026-11-21)

Thread "Derive the n–p cell's E0 and ε→MeV map" (sibling of the eigenphase thread, PR #8836, and of
the error-budget thread, PR #8868). Written before `qbeta_energy_map_probe.py` exists.

## Object

The ruled cell (owner rulings 2026-11-20, D1 = A, D2 = Q_β): ε_p(X) = q·tr_{W_p}(X)/[2]³,
ε_n(X) = q⁻¹·tr_{W_n}(X)/[2]³ (`FlavourWeightSplit`), X = V³ = (σ₁σ₂⁻¹)³. The corpus maps the cell
to MeV linearly, Q_β = E₀·|ε_n − ε_p|. Owner, earlier: the ε → MeV map may not be linear.

## Premise (the only new one), fixed in advance

**S (spectator invariance).** An energy *difference* between two states does not change when both
states are multiplied by the same positive factor λ. Written for a map E = Φ(ε):
Φ(λx) − Φ(λy) = Φ(x) − Φ(y) for all λ, x, y > 0.

Where S comes from in the corpus (none of these mentions Q_β's value):
- the owner ruling of 2026-11-21 (error-budget audit §10, "not one-sided yet"): the lepton factor
  f multiplies *both* ε_n and ε_p. Under the linear map that common factor rescales the cell by
  f(1) < 1. S says a common factor must not change the energy released;
- idle-strand invariance, one of the three premises the eigenphase thread used to derive the
  lepton normalisation (PR #8836, a0a6ae8303): an idle strand multiplies every trace by one
  common factor;
- the global normalisation 1/[2]³ is a choice among common rescalings (error-budget link L7).

**Not assumed:** which energy scale, which sign, which reading (Q_β or m_n − m_p).

## Questions, in order

1. **Lean first.** Prove: S together with continuity on (0, ∞) forces Φ = c·log + d
   (Cauchy's equation on the multiplicative group). Prove the linear map fails S.
2. **Lean.** Under Φ = c·log + d, the cell Φ(ε_n) − Φ(ε_p) = −2c·log q for *every* word whose
   two weight-space traces agree (`NucleonWeightSpaceTraces.trace_word_eq`) and are non-zero, and
   for every global normalisation. So V³, τ and [2]³ drop out. n heavier ⇔ c < 0 (a decreasing
   map: the free-energy form E = −|c|·log Z).
3. **The scale c is not fixed by S.** The corpus offers exactly one energy for this cell, E₀
   (`rem:energy-scale-planck`, "energy of one Hecke reduction step"), and one tower correction.
   It does not say whether E₀ is energy per unit of log-weight or per Hecke step (one factor q).
   Both readings are computed; neither is chosen:

   | id | c | cell = 2|c|·log q | corpus source |
   |---|---|---|---|
   | L0 | E₀ = m_e/(q(q−1)) (order zero) | 2E₀·log q | `energy-scale-planck.md`, `qbeta_e0.order_zero` |
   | LT | E₀^full = E₀/(1 − ℏ_q²) (tower) | 2E₀^full·log q | `qbeta_e0.canonical` (ruled 2026-09-03) |
   | S0 | E₀/log q (per Hecke step, order zero) | 2E₀ | same block, "one step" read as one factor q |
   | ST | E₀^full/log q (per step, tower) | 2E₀^full | same |

4. **E₀ re-examined (coordinator's ask): order zero vs tower.** Report E₀, E₀^full and their
   ratio q²/(2q − 1) at the proton q₀, the linear cell under each, and the log cell under each.
   Prove in Lean: for every q > 1, 2/q² < (2E₀·log q)/m_e < 2/q (bounds from
   1 − 1/q < log q < q − 1), and the tower ratio identity.
5. **Comparison, last and outside any proof:** CODATA Q_β and m_n − m_p against every row. Both
   readings shown for every row. **None is selected.**

## Contamination, stated plainly

Before writing this file I had seen: error-budget §14 (2E₀^full·log q = 0.88220 MeV, i.e. row LT),
and I estimated row L0 by hand while planning. So rows L0 and LT are not blind. The premise S and
the four rows are fixed here and nothing will be added after the comparison is printed.

## Addendum 1 (owner: "Try to derive" the scale |c|), written before any new code

S fixes the form E = c·log ε + d and forces |c| to be independent of the trace normalisation
(a scale that rescaled with ε would break S). So |c| = m_e·φ(q). The corpus already reads the
Markov trace as a partition function. Two definitions on record fix |c| as a temperature,
E(X) = −k_B T·log ε(X) (free energy):

| id | route | |c| | cell | corpus source |
|---|---|---|---|---|
| T | quantum temperature T_q = ℏ_q (k_B = 1, natural units), converted with 𝔈 = 𝔪·c_q² and the CAL-1 mass unit m_e | m_e·c_q²·ℏ_q = m_e/(q(q−1)) = E₀ | 2E₀·log q (row L0) | `def:quantum-temperature`, `def:boltzmann-constant`, `def:information-speed-of-light` |
| D | β = ln q dictionary: E_λ = −ln y_λ / ln q | 1/ln q in the dictionary's units | exactly 2 units; MeV per unit not fixed by the dictionary | `prop:beta-eq-ln-q-dictionary`, `QBetaEnergyDictionary.lean` |

Questions:
1. Lean: kT in MeV equals E₀ exactly (route T); route D gives exactly 2 units; the two inverse
   temperatures differ (ln q vs 1/ℏ_q) for every 1 < q < 2, so the corpus has two inconsistent
   temperatures and they must be reported, not reconciled by choice.
2. Probe: the route-T number is row L0, already computed. Route D in MeV needs a unit the
   dictionary does not give; report the cell for the two units the corpus uses for energy,
   m_e·c_q² and m_e, as diagnostics. None selected.

Contamination: route T reproduces row L0, which I had computed. I found route T after seeing L0,
by reading the corpus for a temperature; I did not search for it by its number.

## Addendum 2 (owner card "Reconcile first"), written before the new Lean

Hypothesis to test: the two temperatures are one Gibbs state in two energy units, not two
physical temperatures. Both read the same trace weight y as a Boltzmann weight,
y = e^{−β_D E_D} = e^{−β_q E_nat}, with β_D = ln q (dictionary, energies "relative to the weights",
no unit stated in the block or its `.ts`) and β_q = 1/ℏ_q (`def:quantum-temperature`, natural
units). If so, E_nat = (β_D/β_q)·E_D = ℏ_q·ln q·E_D, and the dictionary's unit in MeV is
ℏ_q·ln q·m_e·c_q² = E₀·ln q. Then route D's cell (2 units) equals route T's cell (2E₀·ln q).
Lean: the weight equality ⇔ the unit relation; the converted route-D cell = route-T cell.
What would refute it: any corpus block that states T = 1/ln q in natural units (grep, before Lean).
Grep result (done before writing this): no block states that.

## Addendum 3 (owner "Both": the tower factor, and the reading), written before new code

**Q1, tower.** The tower factor T = 1/(1 − ℏ_q²) = Σ_N ℏ_q^{2N} is word-independent and the same
for n and p. Under the full-tower ruling (2026-09-03) it belongs to the fibre object, i.e. to the
partition function, not to k_B T. Test: (a) in the Gibbs reading a common factor of Z is a
spectator, so it should cancel from the cell exactly (Lean); (b) the alternative, T rescaling
k_B T, is the corpus's current E₀^full and is reported beside it. No new number is chosen.

**Q2, reading.** Under the ruled shared placement the lepton factor L multiplies both nucleons, so
the cell is E(n⊗L) − E(p⊗L) = E(n) − E(p): a nucleon energy difference that contains no electron
rest energy. Test: state that in Lean as the spectator corollary, and compare the cell with
m_n − m_p using the existing all-q bound (cell < 2m_e). The D2 ruling (cell = Q_β) was made for the
linear cell; if the derivation points elsewhere, that goes to the owner, not changed here.

## Addendum 4 (owner: β-decay as a GB reduction, "unreduced vs reduced"), written before any code

Owner, 2026-11-21: *"beta decay is just a GB calculation, maybe difference of unreduced braid vs
reduced braid?"*; card "Neither yet: wait for GB reduction"; *"Reevaluate lepton placement."*
Placement card pending; this addendum works the recommended option C (active lepton strand,
premise L) and reports B beside it. If the owner picks otherwise, this is re-scoped, not re-run
silently.

**Object.** H₄(q), convention D. Nucleon core β_Bor = (σ₀σ₁⁻¹)³ on strands 0–2 (same element for
n and p, #8636). Process word W = X·β_Bor with X = V₁³ = (σ₁σ₂⁻¹)³, the unique minimal word of
G ∧ CC ∧ R3 in `2026-11-21-beta-pair-creation-word-proposal.md` (a proposal, **not ruled**; stated
as an input). Reused code: `computations/probes/beta_pair_creation_word/hecke_exact.py`.

**Precedent for the measure.** `E0ReductionWordCount.lean`: E₀/m_e = Hilbert(free words) −
Hilbert(normal forms) at t = q⁻¹, i.e. the q⁻¹-weighted count of words that need a reduction
(one generator only).

**Measures, all fixed now, all reported, none selected:**
- **M1, reduction count.** The number of rewriting steps (σᵢ² → hσᵢ + 1, σᵢ⁻¹ → σᵢ − h, and the
  braid moves needed to reach the GS normal-form order) taken to bring the unreduced word W to
  NF(W), for a fixed leftmost-first strategy. Rewriting counts depend on the strategy, so the
  strategy is stated and a second (rightmost-first) is run to show how large that dependence is.
- **M2, q⁻¹-weighted defect.** Σ over the expansion of W of q^{−len} for words not in normal form,
  the H₄ analogue of the E₀ precedent, as an exact function of q. Whether it converges or is
  finite here is part of the result (the E₀ file shows the infinite two-generator series diverges
  at q₀; W is a finite word, so its expansion is finite).
- **M3, CC block in the Gibbs reading.** The n⊗ν → p⊗e⁻ entry of ρ(W) on the T³-conserving
  sector, and kT·ln of its modulus ratio to the diagonal n⊗ν → n⊗ν entry, with kT = E₀
  (route T, derived).

**Checks fixed now:** T³ weight of n⊗ν and p⊗e⁻ both 0 (§13 C); M1 equals the length change
bookkeeping; NF(W) reproduces the 17-term normal form recorded in the pair-creation witness.

**Comparison, last and outside any proof:** each M in MeV (M1, M2 times E₀; M3 as is) against Q_β
and m_n − m_p. Nothing is selected by it. Contamination: I know the cell 2E₀·ln q and the B bound
0.3625 MeV; neither is a row here.

## Addendum 5 (written after Addendum 4's numbers, before this computation)

Defect in Addendum 4: M1 and M2 count every reduction in W = X·β_Bor, including those inside the
nucleon core β_Bor (present in the initial state, the same for n and p) and inside X alone. The
interaction's own reductions are the cross part ΔM = M(X·β_Bor) − M(β_Bor) − M(X), for both
strategies, and for M2 also exactly in q. Contamination, stated: Addendum 4's numbers (M1·E₀ ≈ 318
MeV, M2·E₀ ≈ 229 MeV, M3 ≈ 12.3 MeV) were printed before this was written. ΔM is the only new row.

## Addendum 6 (owner "1 2"), written before any code

**(1) State-level reduction count.** The module is V^{⊗4} with the Jimbo Ř (`jimbo.py`):
uu ↦ q uu, ud ↦ du, du ↦ ud + h·du, dd ↦ q dd, and Ř⁻¹ = Ř − h. A *firing* is a step whose weight
comes from the reduction: the h·du branch, or the −h term of an inverse. Mark each firing with a
formal t. For a transition |i⟩ → |f⟩, E(t) = Σ_paths (product of weights)·t^(firings), computed
exactly by dynamic programming over (state, t-degree). Summed over the CC block (n⊗ν inputs udd,dud,ddu ⊗ u
→ p⊗e⁻ outputs, strand-tracked as in `analyse_element`) this gives E_f(t). The reverse block
(p⊗e⁻ → n⊗ν) gives E_r(t), and the diagonal n⊗ν → n⊗ν block gives E_d(t).
- **SA, weighted mean reductions** ⟨k⟩ = E′(1)/E(1) for f, r, d. Asymmetry A = ⟨k⟩_f − ⟨k⟩_r.
  Energies ⟨k⟩·E₀ and A·E₀ (E₀ = energy per reduction step, `rem:energy-scale-planck`).
- **SB, unweighted paths.** Number of nonzero-edge paths P and total firings F over them, for f and r.
  Energies (F/P)·E₀.

**(2) Other admissible words.** The two other G ∧ CC ∧ R3 words of the pair-creation proposal,
V₀V₁V₀V₁ and V₁V₀V₁V₀ (Vᵢ = σᵢσᵢ₊₁⁻¹), each times β_Bor. Run Addendum 4–5 measures (M1, M2, ΔM,
M3) and Addendum 6 measures (SA, SB) on all three words. No word is selected by any number.

**Checks fixed now:** E_f(1) equals the CC block sum from `analyse_element`; the same for E_r(1)
and E_d(1); NF of each W is strategy-independent.

**Comparison** last, against Q_β and m_n − m_p, nothing selected. Contamination: Addendum 4–5
numbers for V₁³ are known (100–400× Q_β; M3 = 12.3 MeV).
