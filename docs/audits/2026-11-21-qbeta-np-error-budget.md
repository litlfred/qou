# Where the Q_β and m_n − m_p error comes from: one closed form, and a bound

Date 2026-11-21. Thread "Find where the n–p mass error comes from". Main at `cf14745ac`.
Diagnostic. CODATA appears only in §6, as a comparison, never in a proof.

Lean: `QOU/QBeta/QBetaErrorBudget.lean`. Probe:
`computations/probes/qbeta_error_budget/qbeta_error_budget_probe.py` (9/9, witness
`qbeta-error-budget.witness.json`), pre-registered in `PREREGISTRATION.md` beside it.

## 1. Result

- **There is one error, not two.** m_n is scored as m_p + m_e + Q_β
  (`computations/l2_row_independence_probe.py` lists m_n and Δ_pn as redundant rows). m_p is off by
  0.23 keV. The m_n miss is 0.45690 MeV, which is the Q_β miss to the keV. So the −486 ppm on m_n,
  the −35.3 % on m_n − m_p and the −58.4 % on Q_β are the same number seen three ways.
- **The whole scored cell is one rational function of q, times m_e.**
  Q_β = m_e · R(q), with R(q) = −(q+1)·P(q) / (q³ (2q−1) (q²+1)³),
  P(q) = q¹² − 3q¹⁰ + 3q⁸ − 5q⁶ + 3q⁴ − 3q² + 1 (`qbetaOverMe_eq`). The scale E₀ ∝ 1/h and the
  flavour split ∝ h cancel exactly (`e0_mul_h`).
- **R(1) = 3/4, and R(q) ≤ 3/4 for every q ≥ 1** (`rClosed_one`, `rClosed_le_three_quarters`).
  So this cell can never exceed 0.383 MeV, whatever the pin. Measurement needs Q_β/m_e = 1.531.
- **So the missing 2.404 splits as 2.041 × 1.178.** At least 2.041 of it has to come from a link
  that is still there at q = 1: the counting 3/8, the factor 2, or the identification of the cell
  with Q_β. The O(h) effects together are only 1/0.849 = 1.178. This is why every q-correction
  lever tried so far (c_k ladder, cosh, GPMT, the γγ tower) failed. They all go to 1 at q = 1.
- **The base is the error, not a missing small correction.** The pin moves Q_β by 19 ppb, and
  E₀'s q-dependence cancels. The element cannot lift the q = 1 value above 3/8 · 2, because the
  weight-space trace at q = 1 counts fixed points, and that count is at most 3 for every braid
  word. The normalisations in the corpus, or one step from it, give a q = 1 coefficient of 0,
  1/2, 3/4 (scored) or 1, never the 1.80 needed. What is left is the identification itself: the
  scored functional is a nucleon-only trace difference. The β-decay interaction (ruling
  2026-11-20) and the electron word σ₀σ₁σ₀ (ruling 2026-11-21) do not enter it. The electron
  appears only as the kinematic + m_e.

## 2. The pipeline, link by link

The cell (owner ruling 2026-11-20, D1 = A, D2 = Q_β) is
Q_β = E₀^full · |ε_n(V³) − ε_p(V³)|, with ε_{p,n} = q^{±1}·tr_{W_{p,n}}(V³)/[2]³. The plain traces
on W_p and W_n are equal (`NucleonWeightSpaceTraces.trace_word_eq`), so ε_n − ε_p = −h·τ/[2]³,
τ = tr_{W_p}(V³) = −P(q)/q⁶.

| # | link | value at q₀ | value at q = 1 | status | source |
|---|---|---|---|---|---|
| L0 | m_e | 0.51099895069 MeV | same | **calibration** (CAL-1) | `qou_substrate.constants` |
| L1 | q₀ (proton pin) | 1.10997858275… | — | **calibration** (CAL-2), proton pin is the canonical one | `Q_50_DIGIT_STR` |
| L2 | E₀ = m_e/(q(q−1)) = m_e·c_q²·ℏ_q | 8.1918 m_e | diverges like 1/h | **chosen form**: a dimensional reading ("one Hecke reduction step"), stated in a remark, not derived from the axioms | `rem:energy-scale-planck`, `qbeta_e0.py` |
| L3 | tower factor 1/(1 − ℏ_q²) | 1.009915 | 1 | **ruled**, series not derived | 2026-09-03 full-tower ruling; bean `qou-y3bm` |
| L4 | h = q − q⁻¹ from K = diag(q, q⁻¹), u = e₁ | 0.209060 | 0 | **derived** (K forced by convention D; u = e₁ from the over-strand result) | `MarkovOrientationForced.lean`, `OverStrandWeight.lean` |
| L5 | element V³ = (σ₁σ₂⁻¹)³ = γγ product | — | identity of S₃ | **derived/selected** by the SDP cost (not by Q_β) | PR #8564, `borromeanV3A_eq_switched_photon_product` |
| L6 | τ = tr_{W_p}(V³) | 2.994186 | 3 | **derived** given L5 | `trace_borromeanV3A` |
| L7 | normalisation 1/[2]³ (global, over all 8 states) | 0.122979 | 1/8 | **chosen** from two; the other (per sector) gives 0 | `qou-99qc`; `normalised_split_V3_eq_zero` |
| L8 | Q_β := E₀·\|ε_n − ε_p\| | — | — | **ruled** (D1 = A, D2 = Q_β); linear E₀ form is the corpus's | `2026-11-20-qbeta-flavour-weight-split.md` §6 |
| L9 | m_n − m_p = Q_β + m_e | — | — | **kinematics** at the comparison boundary | np-splitting §20, §23 |
| L10 | m_n = m_p + m_e + Q_β | — | — | **scoreboard construction** | `l2_row_independence_probe.py` |

**Nothing in the cell is fitted.** Two links are chosen (L2's form, L7), two are ruled (L3, L8),
and the rest are derived or calibrations.

L2 × L4 collapses: E₀·h = m_e·(q+1)/q² (`e0_mul_h`). At q = 1 this is 2·m_e. The 2 is
lim h/(q − 1): the K-weight gap q^{+1} vs q^{−1} spans two of E₀'s ticks q − 1.

## 3. Where the 2.404 sits

R(q) = [(q+1)/q²] · τ · [1/[2]³] · T. At q = 1: 2 · 3 · 1/8 · 1 = **3/4**.

| piece | ratio to its q = 1 value, at q₀ |
|---|---|
| (q+1)/q² vs 2 | 0.856286 |
| τ vs 3 | 0.998062 |
| 8/[2]³ | 0.983831 |
| tower T | 1.009915 |
| **all O(h) effects** | **0.849144** |

F_required = 2.40397 = (1.53099 / 0.75) × (1 / 0.849144) = **2.0413 (q = 1 part) × 1.1777 (O(h) part)**.

The split is not unique: a different true formula could carry a different O(h) shape. The bound
is what is firm. Since R(q) ≤ 3/4 for all q ≥ 1, no pin and no change to E₀ or the tower can
lift the cell above 0.75·m_e. Even a perfect O(h) shape (all corrections equal to 1) leaves
×2.04.

**Why the excluded levers had to fail.** A single correction 1 + c·h^k closing F needs
|c| = 6.7, 32, 154, 735, 3516, 16 816 for k = 1 … 6. That matches the c_k ladder's need for
|c_k| ≥ 7982 (PR #8794): a q-correction is being asked to supply a q = 1 factor.

## 4. Is the base the error?

**The pin (L1): no.** d ln Q_β / d ln q = −1.68 at q₀. The frozen muon pin moves Q_β by −19 ppb.
The m_p residual (−244 ppb) and the μ–p tension are irrelevant here. Scope (b) within this cell:
`qbetaOverMe_le_three_quarters` holds for every pin q > 1.

**E₀ (L2, L3): not as a scale.** Its 1/h cancels the h of the split, so its size never reaches
Q_β. It reaches Q_β only through the tick that makes the 2. The forms on record keep that 2 or
lower it: E₀ = m_e/(q−1) also gives 2, E₀ = m_e/h gives 1. The tower factor is +0.99 %.

**The element (L5, L6): not at q = 1.** At q = 1 a braid word acts on W_p (3-dim, a permutation
module) by its permutation, so τ counts fixed points: ≤ 3 for every word. Checked over all 5460
words in σ₁^{±1}, σ₂^{±1} of length ≤ 6. V³ is already at the maximum. At q₀ the same words give
τ ∈ [−0.61, 4.28], but only by long words of large positive writhe (q^L growth); picking one for
its τ would be selection. V⁶ and V⁹ move Q_β by ≤ 1.5 % (#8586).

**The normalisation (L7): not enough alone.** q = 1 coefficient of Q_β/m_e under the variants
(diagnostic, none selected):

| normalisation of the T³ split | q = 1 coefficient |
|---|---|
| per sector (each space by its own trace) | 0 |
| isospin-½ isotypic part only, global [2]³ | 1/2 |
| **global [2]³ (scored)** | **3/4** |
| W_p ⊕ W_n quantum dimension 3[2] | 1 |
| needed, keeping the scored O(h) shape | 1.803 |

**The identification (L8): this is where the q = 1 factor has to come from.** L4 and L6 are
derived, L5 is at its classical maximum, and L7's whole family stops at 1. The remaining link
that survives q = 1 is what the cell is taken to be. As scored, it is a difference of two nucleon
traces. No lepton word and no interaction (GS reduction of n → p e ν̄ or γγ pair production) enters
it. The ruled electron σ₀σ₁σ₀ with Hopf closure and the two-term trace are not in the cell. This is
scope (a): it says the missing factor is in what the cell counts, not that any particular
interaction functional will supply it.

**Sign.** Under "mass ∝ trace" the neutron component is the smaller one (t_n = q⁻²t_p). Q_β uses
|·|, so the scored row does not see it. A replacement functional has to get the sign as well.

## 5. Corrections to keep (owner rule: keep every derivable correction)

All four O(h) pieces in §3 are derived from the corpus or ruled. They stay, whatever fixes the
q = 1 coefficient: (q+1)/q² vs 2 (−14.4 %), 8/[2]³ (−1.6 %), τ/3 (−0.19 %), tower (+0.99 %).

## 6. Comparison (outside any proof)

| quantity | model | CODATA | miss |
|---|---|---|---|
| Q_β / m_e | 0.6368583 | 1.5309883 | ×2.40397 |
| Q_β | 0.3254339 MeV | 0.78233341 MeV | −58.40 % |
| m_n − m_p | 0.8364329 MeV | 1.2933325 MeV | −35.33 % |
| m_n miss | 0.4568995 MeV | | = the Q_β miss |

## 7. What this does not claim

- It does not identify the correct functional. It bounds the scored one and says which link has
  room.
- "The identification carries the factor" is scope (a): among the links of this cell, only L8 is
  not either derived, at its classical maximum, or capped below the need. A new functional may
  change several links at once.
- The τ ≤ 3 bound is checked over words of length ≤ 6 and argued for all words (fixed-point
  count); the general statement is not in Lean.

## 8. Reproduce

`python3 computations/probes/qbeta_error_budget/qbeta_error_budget_probe.py` (sympy, mpmath;
about 3 minutes, most of it the word enumeration).

## 9. Q_β as an interaction, q = 1 first (owner card 2026-11-21 13:33Z)

Pre-registered in `computations/probes/qbeta_interaction_q1/PREREGISTRATION.md` (questions 1–4,
then an addendum 5–6 written before `lepton_factor_q1.py` ran). Exact sympy; CODATA last.

**The reduction (Lean, `e0Tower_mul_sub_one`, `e0Tower_mul_order_two`).** E₀^full·(q − 1) =
q/(2q − 1)·m_e. So for a functional F of order k at q = 1:
- k ≥ 2: Q_β/m_e → 0 at q = 1. F can only be an O(h) correction.
- k = 1: Q_β/m_e → F′(1), a finite number (the scored cell: 3/4).
- k = 0: Q_β ~ E₀·F(1) plus O(m_e) terms of the same size, so q = 1 alone does not decide it.

**Every interaction energy on record is order ≥ 2.** All 67 one-term cross terms
C₁(X) = tr_D(Xβ) − tr_D(X)tr_D(β) in the pair-creation probes (A = V₁³, B = σ₀σ₁σ₂, B̄, C = σ₂, the
D family, and their products with P_L and the weak vertex) vanish to order ≥ 2. So none of them
can supply the ×2.04; as corrections they are O(h). The non-covariant two-term connected terms
(T2lep) are order 1 with F′(1) = 1/8 or 1/4: added to 3/4 they give at most 1, still short of 1.80.
The charged-current block entries (transition amplitudes, not energies) are order 1 with
F′(1) ∈ {±1, ±2, 4}; reading Q_β as E₀·|amplitude| would be a new identification, not a correction.

**One-sided lepton factor (lead from the eigenphase thread, #8836).** If the lepton factor f
multiplies only the final state, F = ε_n(V³) − ε_p(V³)·f is order 0.
- K-weight conservation K(n) = K(p)·K(e)·K(ν̄) has no solution without a ν̄ strand. With ν̄ of
  weight q⁻¹ it forces the electron sector b = 2 (two d strands); with q⁺¹, b = 3.
- The plain trace of Δ = σ₀σ₁σ₀ is q³ on every sector.
- F(1) and E₀^full·|F| at q₀ under each rule on record (none chosen):

| lepton factor rule | f(1) | F(1) | E₀^full·\|F\| at q₀ |
|---|---|---|---|
| nucleon rule (K × plain sector trace / [2]ⁿ), electron sector forced by K, times ν̄ | 1/16 | 45/128 | 1.28513 MeV |
| same, b = 3 with ν̄ of weight q⁺¹ | 1/16 | 45/128 | 1.28513 MeV |
| nucleon rule, no ν̄ factor | 1/8 | 21/64 | 1.14062 MeV |
| plain per-sector trace | 1/3 | 1/4 | 0.61477 MeV |
| Markov value t(Δ) | 1/2 | 3/16 | 0.20818 MeV |

The values span 0.21 to 1.29 MeV, so the normalisation of the lepton factor decides the number.
The O(h) terms are not small here: the Markov row has F(1) = 3/16 but lands at 0.21 MeV.
The two K-allowed sectors give the same value.

**Comparison (outside any proof).** CODATA Q_β = 0.78233 MeV, m_n − m_p = 1.29333 MeV. The
nucleon-rule row is −0.63 % from m_n − m_p and +64 % from Q_β. This is reported, not used. The
2026-11-20 ruling D2 read the old cell as Q_β, and this row would reopen that question. Choosing a
row because of where it lands would be selection against the target.

**What is settled (scope (b), invariant: order at q = 1).** No interaction energy on record can be
the missing q = 1 factor. **What is open:** whether the lepton factor is one-sided, and which
normalisation it carries. The one rule already ruled for ε (the nucleon rule) is the
corpus-consistent candidate. It is not adopted here.

## 10. Owner ruling 2026-11-21: not one-sided yet

Owner card choice "Not one-sided yet". The lepton factor stays on both sides of the transition.
It is then a common factor of ε_n and ε_p, and the functional stays order 1 at q = 1.

Recorded result: **no interaction functional on record closes the Q_β gap.**
- Cross terms are order ≥ 2 at q = 1 (§9).
- The two-term connected terms lift the q = 1 coefficient to at most 1, against the ≈ 1.80 needed.
- A shared lepton factor f multiplies the scored coefficient by f(1).
  - Nucleon rule: f(1) = 1/16.
  - Markov t(Δ): f(1) = 1/2.
  - In both cases f(1) < 1, so the factor lowers the coefficient further.

The one-sided rows of §9 stay as unadopted diagnostics. The ruling is in
`docs/coordination/owner-rulings.md`.

What remains open is a q = 1 counting factor ≥ 2.04 that none of the following supplies:
- the derived links (h, V³, τ);
- the normalisation family (≤ 1);
- the interactions on record.

## 11. Both lepton-factor rules, in both placements (owner: "explore both of the options")

This is an exploration only. The ruling of §10 stands, and nothing here is adopted. It was
pre-registered as addendum 2 before `both_rules.py` ran. Lean: `QOU/QBeta/OneSidedLeptonFactor.lean`
(lean-direct exit 0, standard axioms only).

| rule | placement | respects K-conservation | sign at q₀ | q → 1 | E₀^full·F (order-zero E₀) |
|---|---|---|---|---|---|
| nucleon rule, f = q/[2]⁴ | shared (ruled) | yes | − (neutron lighter) | F′(1) = −3/64 | −0.0221 MeV (−0.0219) |
| Markov t(Δ) | shared (ruled) | **no**: sums all four sectors | − | F′(1) = −3/8 | −0.2249 MeV (−0.2227) |
| **nucleon rule, f = q/[2]⁴** | **one-sided** | **yes** (b and ν̄ forced, `kConservation_*`) | **+ (neutron heavier)**, `fOneSided_pos` | order 0, F(1) = 45/128 | **1.28513 MeV** (1.27251) |
| Markov t(Δ) | one-sided | **no** | + | order 0, F(1) = 3/16 | 0.20818 MeV (0.20614) |

**What can work, and what cannot.**
- **Shared placement (the current ruling): cannot work under either rule.** Both give the wrong
  sign and at most 0.22 MeV. A shared factor below 1 only shrinks the scored cell.
- **Markov rule: inadmissible for a transition factor, scope (b).** The invariant is U_q
  weight conservation. t(Δ) sums all four electron sectors, including the ones that K-conservation
  forbids for n → p e⁻ ν̄.
- **Nucleon rule, one-sided: the only row that passes every structural test.**
  - It respects K-conservation, which forces the ν̄ strand and the electron sector.
  - Both K-allowed sectors give the same f.
  - It uses the same rule already ruled for ε, so it adds no new choice of rule.
  - It gives the neutron-heavier sign, which the scored cell does not.
  - Its closed form is exact, F = −(q²+q+1)·S(q)·P(q)/(q⁴(q²+1)⁷), so it has no truncated O(h) tail.

**The open reading (owner decision).**
- *E₀·F = Q_β:* 1.28513 MeV, +64.3 % against CODATA Q_β.
- *E₀·F = m_n − m_p* (F is a nucleon-energy difference whose lepton factor only selects the
  K-allowed sector; the electron rest energy is not in it): −0.63 % against CODATA, and then
  Q_β = E₀·F − m_e = 0.77413 MeV (−1.05 %). With the order-zero E₀: 0.76151 MeV (−2.66 %).
- The 2026-11-20 ruling D2 chose the Q_β reading for the *old* cell. Its reason was that the
  other reading made Q_β negative. That reason does not apply here: Q_β comes out positive.
- **Selection caution, stated plainly:** I saw these numbers before writing this paragraph. The
  rule (nucleon rule), the sector (forced by K), and both readings were all on record before the
  comparison was printed, but which reading to adopt has not been decided, and it must not be
  decided by which number lands closer.

**Still not derived:**
- *One-sided placement.* Overruled for now; it would need a ruling.
- *The reading.* Either reading still needs a ruling.
- *The tower factor (bean `qou-y3bm`).* It moves the result by 1 %.

## 12. Deriving the reading of E₀·F (owner: "not yet, derive the reading")

**Question.** For the one-sided nucleon-rule F = ε_n − ε_p·f, is E₀·F the Q_β or the m_n − m_p?
Each reading is tested against the energy map it has to use. No comparison value decides
anything. Pre-registered in `computations/probes/qbeta_interaction_q1/PREREGISTRATION.md`,
Addendum 3. Probe: `reading_probe.py`, 8/8; witness `qbeta-one-sided-reading.witness.json`.
Lean: `QOU/QBeta/OneSidedReading.lean`, lean-direct exit 0, no `sorry`.

**Linear map E(X) = E₀·ε(X), multiplicative traces.** This is the map the scored cell already uses.
- Identity (Lean `fOneSided_eq_flavour_add`, any field): F = ε_flavour + ε_p·(1 − f).
- *Q_β reading.* E(n) − E(p e⁻ ν̄) = E₀·F > 0, but the map then gives the lepton pair
  E(p e⁻ ν̄) − E(p) = E₀·ε_p·(f − 1), which is **negative** (Lean `leptonPair_neg`: ε_p > 0 and
  f < 1). Numbers: −1.611 MeV (tower E₀), −1.595 MeV (order-zero E₀). Kinematics needs it to be
  m_e + E_ν̄ > 0. **The reading contradicts its own map.**
- *m_n − m_p reading.* The same map on the two nucleons gives E(n) − E(p) = E₀·ε_flavour < 0,
  while E₀·F > 0 (Lean `fOneSided_ne_flavour`). Numbers: −0.3254 vs +1.2851 MeV. **The reading
  contradicts the map applied to the nucleons.**

**Logarithmic map E(X) = ±E₀·ln ε(X).** For sign +1 the lepton pair is −11.37 MeV and Q is
+10.49 MeV; for sign −1 both flip. Under neither sign are both positive, and the pair magnitude
(11.4 MeV) is not m_e (0.511 MeV).

**Result, scope (a).** Under a linear or logarithmic energy map with multiplicative traces,
**neither reading is derived**: each is inconsistent with the map it would use. So the closeness
of E₀·F = 1.28513 MeV to CODATA m_n − m_p (−0.63 %, §11) has no derivation behind it, and must not
be quoted as evidence. This does not exclude an energy map that is neither linear nor logarithmic;
none is on record. What a one-sided placement would need is a map under which the lepton factor
carries a positive rest energy. That is the open item, not the choice between the two readings.

## 13. Nonlinear energy maps (owner: "Q_beta I don't think is a linear map")

**Question.** §12 tested a linear and a log map. Is there any map E(X) = g(ε(X)) of the trace
under which the one-sided lepton factor carries positive energy (lepton pair g(ε_p f) − g(ε_p) > 0)
while Q_β = g(ε_n) − g(ε_p f) > 0? Pre-registered as Addendum 4; probe
`nonlinear_maps_probe.py` 11/11; Lean `QOU/QBeta/OneSidedNonlinearMaps.lean`.

**The deciding fact is an ordering, not a formula.** On 1 < q ≤ 23/20,
ε_p·f < ε_n < ε_p (Lean `ordering`). Its two halves are ε_n = ε_p/q² (`epsN_V3B_eq`) and
f < q⁻² (`leptonFactor_lt_inv_sq`, true for every q > 1 because q³ < [2]⁴).

**Result 1, scope (b), invariant = the ordering.** For **every** monotone or antitone g, the two
conditions cannot both hold (Lean `monotone_excluded`). An increasing g makes the lepton pair
negative; a decreasing g makes Q_β negative. This covers every map on record that is a function
of the trace: linear, |tr_M| (the corpus mass form m_e·ρ·|tr_M| at fixed ρ), ±log (the binding
form), 1/x (the Q_β = ℏ/𝔇_β form), and all powers. It also covers every additive map
g(xy) = g(x) + g(y) that is monotone, and the continuous ones of those are c·log. Numbers in the
witness: e.g. 1/x gives lepton pair +142 MeV and Q_β −140 MeV.

**Result 2.** A g that meets both conditions must rise and then fall across the three points
ε_p f < ε_n < ε_p (Lean `nonmonotone_needed`). No such map is on record. Picking one to make the
signs work would be a fit.

**Result 3, maps that are not functions of the trace alone.**
- *Density-weighted* E = c·ρ_X·ε(X): a positive lepton pair forces ρ_final/ρ_p > 1/f = [2]⁴/q
  ≈ 14.73 at q₀ (Lean `weighted_needs_density_jump`). No density rule on record assigns the
  final state such a jump.
- *Proton-style affine*, with each state's q = 1 value subtracted: lepton pair −0.124 MeV,
  Q_β −0.201 MeV. Fails.

**What is left open.** An energy that is not a function of the product trace at all. One example
is an energy that is additive over the outgoing particles, with the electron carrying its own
m_e (CAL-1). That is the two-sided kinematic reading already on record (m_n − m_p = Q_β + m_e),
and in it the lepton factor does not set the electron's rest energy. So under the multiplicative
one-sided trace, **no map on record gives the lepton factor a positive rest energy**. A one-sided
placement would need the final-state trace to stop being a plain product, for example through
the γγ construction of the ν̄ the owner asked for. That is the next question, not a choice of
map.

## 14. A non-product final-state trace (owner: "not a product because of the flavor/color terms")

Let x = ε(p e⁻ ν̄) be free: the product ε_p·f plus the flavour/colour cross terms. Pre-registered
as Addendum 5; probe `nonproduct_window_probe.py`; Lean `QOU/QBeta/NonProductFinalState.lean`
(lean-direct exit 0, no `sorry`).

**Proved, for every x.**
- *Increasing maps are excluded however large the cross terms are* (`increasing_excluded`). A
  positive lepton pair and a positive Q_β would need ε_p < x < ε_n, and ε_n = ε_p/q² < ε_p.
- *Decreasing maps* (−log, ℏ/𝔇 = 1/x) work **exactly** when ε_n < x < ε_p (`decreasing_window`).
- *The plain product is below that window* (`product_outside_window`).

**Size of what the flavour/colour terms must supply (q₀).** The window is
(0.33174, 0.40872), but the product is only 0.02774. So the cross terms must add between 0.304 and
0.381, which is at least **11× the product term itself**. They would be the leading part of the
final-state trace, not a correction to it.

**What a decreasing map fixes, independent of x.** E(n) − E(p) = g(ε_n) − g(ε_p) uses the nucleons
only:
- −log: 2E₀·ln q = 0.88220 MeV. If the lepton pair is set to m_e, then x = 0.36218 (inside the
  window) and Q_β = 0.37120 MeV.
- 1/x: E₀(q² − 1)/ε_p = 2.40018 MeV. If the pair is set to m_e, then x = 0.38948 and
  Q_β = 1.88918 MeV.

The cross terms only decide how a fixed n − p difference splits between Q_β and the lepton pair.
The difference itself is decided by the map, and the map is not derived. (Comparison, printed
after the fact: CODATA m_n − m_p = 1.29333 MeV, Q_β = 0.78233 MeV.)

**Next step, not done here.** The γγ construction of ν̄ (eigenphase thread) must compute x. It
then has to answer: does x land in (ε_n, ε_p), and which decreasing map does the construction
itself force?

## 15. γγ final states checked against the window (result from the eigenphase thread)

Source: PR #8836, commit 5503ac443c; witness
`computations/probes/qbeta_gg_process_word/qbeta-gg-process-word.witness.json` on that branch.
Option 3 (6 strands with a neutral start, e⁻ + ν̄ + an unknot), embedded as 1560 words
W = X·β_Bor·L on 9 strands. Each is normalised by the nucleon rule,
x = Tr(K⁹ P ρ(W))/[2]⁹, the same normalisation as ε_p and ε_n here. The unlinked words factorise
as ε_p·f_L, which confirms the normalisation matches.

**Result, scope (a):** every x lies in [0.0034, 0.024] and f_L ≤ 0.054. None reaches the window
(0.33174, 0.40872) from §14. The largest x falls short of its lower edge by a factor of 14. So
across this word set, flavour/colour linking does not lift the final-state trace into the window;
it stays at or below the product scale. With option 2 already excluded (§14) and option 1 not yet
computed, no γγ final state on record supports a one-sided reading.

## 16. With the lepton normalisation forced by invariance (eigenphase thread)

Source: PR #8836, commit a0a6ae8303; witness `qbeta-lepton-normalisation.witness.json`. Three
premises force the lepton normalisation [2]^(−components), with the lepton strands summed over
rather than restricted to one sector (Lean, sorry-free there): agreement with D1, invariance
under adding an idle strand, and Markov invariance. This **replaces** the sector-restricted
f = q/[2]⁴ of §11. The unlinked factor becomes f = 0.7432.

What changes and what does not, at q₀:
- *Ordering still holds:* f = 0.7432 < q⁻² = 0.8116. So `monotone_excluded` (§13) still applies,
  and every increasing or decreasing map of a product trace fails.
- *Window, which is in nucleon units and does not change:* (0.33174, 0.40872).
  - Unlinked e⁻ν̄: x = 0.7432·ε_p = 0.3038, below the window.
  - Linked e⁻ν̄ over 1560 words: [0.1747, 0.3151], all below.
  - Mirror (e⁺ν): [0.4094, 0.5884], all above. Its lower edge misses the window's upper edge by
    only 0.0007.
- So the window falls in the gap between the e⁻ν̄ values and the mirror values: **no hits, scope
  (a)**.
- The one-sided linear F from §11 shrinks to ε_n − 0.7432·ε_p = 0.0280, which is E₀F ≈ 0.118 MeV.
  The 1.285 MeV figure of §11 belonged to the superseded sector-restricted f.
