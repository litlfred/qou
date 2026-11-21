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

**6b (owner card "Compute both B and C"), still before code.** Every Addendum 6 measure is run
twice. **C**: the input lepton strand is u (premise L). **B**: no lepton is present in the initial
state, so the input lepton-strand colour is not fixed; the B block sums over both input colours
{u, d} on strand 3 → p⊗e⁻. Under B the closed-form bound Q_β ≤ cell − m_e = 0.362538 MeV (§13) is
printed beside, with E(ν̄) left open.

## Addendum 7 (owner: "Can we reverse the GB ordering to go between p and n? If so, does that fix it?"), before code

Two orderings enter the state-level count, and each is reversed separately.
- **R1, generator order.** Take σ⁻¹ as the leading generator: σ⁻¹ acts by Ř⁻¹ (uu ↦ q⁻¹uu,
  ud ↦ du − h·ud, du ↦ ud, dd ↦ q⁻¹dd), and σ = Ř⁻¹ + h. Firings are the −h·ud branch and the
  +h term. The same matrices, a different marking.
- **R2, colour order (u < d reversed to d < u).** The branch moves from du to ud:
  Ř′: uu ↦ q uu, du ↦ ud, ud ↦ du + h·ud, dd ↦ q dd. Ř′ is the Jimbo Ř with u and d exchanged, so
  it intertwines the n-sector with the p-sector. This is the reading of "reverse to go between p
  and n".
- **R1+R2** both.

For each of the three words and each ordering: ⟨k⟩_f, ⟨k⟩_r, A = ⟨k⟩_f − ⟨k⟩_r, exact and at q₀.
**What "fixes it" means, fixed now, without reading Q_β:** (i) A becomes word-independent across
the three admissible words; or (ii) A has a closed form shared by the three words. Also
reported: whether R2 maps A ↦ −A (the expected p ↔ n swap), and whether R1 changes A at all.
The comparison with Q_β is printed last and does not decide (i) or (ii).

## Addendum 8 (owner "Both": flavour + colour on strands, and an ordering-independent asymmetry), before code

**(a) Ordering-independent asymmetry, flavour only.** The generator-order choice can be made per
generator: for each i ∈ {0, 1, 2}, σᵢ or σᵢ⁻¹ is leading (2³ = 8 orderings; the "standard" and R1 of
Addendum 7 are two of them). The colour order stays u < d, because reversing it is the p ↔ n swap
(§16), so averaging over it would give 0 by construction. Measure: Ā = mean of A over the 8
orderings, exact in q, for the three words. Also the spread (max − min). Tests, fixed now:
Ā word-independent? Ā equal to a simple closed form shared by the words?

**(b) Colour on strands: what the corpus defines, checked before building anything.**
- `bring_color_weighted` (ruled 2026-08-15) is a convention for the p–n *interface* factor between
  nucleons in binding, f_pn = z − h(1/2 − δ/4) (`closed_form_tau_M.py`). It acts between nucleons,
  not on quark strands inside one nucleon word. So it does not enter a single-nucleon β-decay word.
- The colour frame (`sl-n-color-frame-scope`) reads colour observables with σᵢ^{sl} = q^{−1/N}σᵢ.
  On a word of writhe w this multiplies the element by q^{−w/N}. Every γγ word has writhe 0
  (`writhe_eq_zero`), so the frame is the identity on β_Bor, on all three X, and on W. Test, fixed
  now: check writhe(W) = 0 for the three W.
- A strand space V = flavour ⊗ colour (dim 6, Jimbo Ř of gl₆) is not defined in the corpus, and on
  V^{⊗4} it would turn on shapes with three or more rows, which convention D sets to weight 0.
  Building it would be a new construction, not a corpus-derived one, so it goes to the owner
  instead of being run.

## Addendum 9 (owner: "Relax ruling on p-n....explore possibilities. need to derive things, not assert"), before code

**Reading.** The 2026-08-15 ruling R3 (`bring_color_weighted` canonical for p/n) is relaxed to a working
conjecture. Task: ledger every p–n construction in the corpus as *derived* or *asserted*, keep only the
derived steps, and name what would have to be derived to use the rest. Nothing is selected by CODATA;
CODATA numbers appear only in the comparison column.

**Ledger (read from the corpus, before any new code).**

| # | construction | step | status | source |
|---|---|---|---|---|
| P1 | n–p cell 2E₀·ln q (this thread) | K-weight ratio ε_n/ε_p = q⁻², log map, kT = E₀ | derived (Lean: `common_factor_log_cell`, `cell_eq_eigen_gap`) | `SpectatorEnergyMap.lean` |
| P1′ | same | assignment to an observable | **open** (ruling 2026-11-21); bound cell < 2m_e excludes m_n − m_p directly | audit §12 |
| P2 | prop:flavor-split-substrate | Step 1 pair-Skein difference | asserted twice: the pair-Skein formula takes per-quark masses μ as inputs, and is convention C | `flavor-split-substrate-proof.md`, `pair-skein-mass-formula.md` |
| P2′ | same | Step 2 (μ_d − μ_u)/μ_avg = h²ℏ/√q | asserted: fitted to experiment (the proof says so) | same |
| P3 | `flavor_split_subleading` (1 + ℏ³) | — | asserted (marked POSITED) | `_li_2_q_util.py` |
| P4 | `bring_color_weighted` f_pn = z − h(1/2 − δ/4) | δ = P2′ | asserted by inheritance | `closed_form_tau_M.py` |
| P5 | Bring linking weight, m_n − m_p = 0.887 MeV | δ and the λ_A absolute-mass fit | asserted by inheritance (two fits) | `2026-06-01-bring-color-weighted-…` audit |
| P6 | linear map, E₀^full·\|ε_n − ε_p\| = 0.325 MeV | linear map | excluded by spectator invariance | audit §3 |

**Consequence.** P1 is the only p–n quantity whose every step is derived. Everything carrying δ rests on
one fitted ansatz (P2′).

**Exploration routes (each a derivation target, not a number to adopt).**

- **R-a. Re-derive the pair-Skein crossing trace under convention D.** If the crossing-pair trace gives
  m_n − m_p = [2]_q·z·(μ_d − μ_u) under z_D, then [2]_q·z_D = q² exactly. Needed: the trace itself, re-derived
  (the formula's own text says substitution is not valid).
- **R-b. Derive μ_d − μ_u from the strand weight.** Two readings, measured before any choice:
  (i) multiplicative, μ_d/μ_u = q^{ΔH} = q², gives (μ_d − μ_u)/μ_avg = 2(q²−1)/(q²+1) = 0.2079 at q₀;
  (ii) logarithmic, μ_d − μ_u = the cell P1.
- **R-c. Combine R-a and R-b(ii)** only if both are derived. Comparison values, recorded now so they cannot
  steer: cell 0.873537 MeV (−32.46 % vs m_n − m_p); q²·cell 1.076243 MeV (−16.79 %); [2]_q·z_C·cell 0.877102
  MeV (−32.18 %, convention C, excised).
- **R-d. Assign the cell P1 through the GB reduction** (Addenda 4–8): already measured, scope-(a) negative.

**What will not be done.** No route is adopted because its number is closer. R-c is not a result until R-a
and R-b(ii) are both derived; the −16.79 % is a comparison, not support.
