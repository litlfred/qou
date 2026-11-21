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
