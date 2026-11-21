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
