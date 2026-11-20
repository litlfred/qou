# Q_β from the flavour (T³) split of the convention-D trace on the γγ base

Owner ruling (Carl, 2026-11-20): derive the n ≠ p flavour ingredient on the U_q / weight side,
and score Q_β on the γγ base V³ with that ε. Owner correction (15:47): the photon is
**γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹**, with the chiral pair-production vertex V = σ₀σ₁⁻¹ as
the fourth term. Every result here uses that form. (`predicted-spectra/photon.md` on main still
writes σ₀σ₁; a separate task corrects it, and this branch does not edit it.)

Beans: `qou-99qc`, `qou-ales`. Stacks on PR #8564.

## 1. Result in one paragraph

Two arms, as the owner asked.

- **Arm γ (four-term chiral photon).** The corpus derives only one pair of colour weights: the
  two eigenvalues q and −q⁻¹ of σᵢ give γ(0,0,qh)·γ(0,0,−q⁻¹h) = V³. The other weights on record
  (φ = 0.0487 and s = 0.0978) are labelled in the corpus as fits to 2m_e and are not used. So the
  γγ product with derived weights is V³ for the proton and for the neutron alike. Reading 3 does
  not separate them (PR #8564). Δ = 0, and Q_β = 0 for every linear ε. The chirality of the
  product is real: its L₊ = σ₀σ₁ coefficient is h⁴ + h² and its L₋ = σ₁σ₀ coefficient is −h². But
  it is the same for p and n. Three ways of reading chirality into a trace all give zero
  (scope (b), invariants named in §3).
- **Arm W (weight split).** This arm gives a non-zero value. Write the z_D trace as a sum over
  T³ sectors. Its proton and neutron components on V³ differ by
  ε_flavour(V³) = (q² − 1)·P(q) / (q⁴(q² + 1)³), with
  P(q) = q¹² − 3q¹⁰ + 3q⁸ − 5q⁶ + 3q⁴ − 3q² + 1. This is **exactly bar-odd**: the bar involution
  carries the proton component to the neutron component. So the "bar-odd channel" and the
  "weight split" are the same object here. **Q_β = 0.325434 MeV, −58.40 % against CODATA**
  (F_required = 2.404). This value was not blind (§4).

**Relation to PR #8564.** #8564's Q_β = 0 was obtained with the old bare-vertex grammar
(`GammaGammaWordSelection`: products of σᵢσᵢ₊₁⁻¹, no colour weights). Arm γ redoes it with the
four-term σ₀σ₁⁻¹ photon and the corpus-derived colour weights. It lands on the same element V³
for both nucleons, so the zero survives the change of grammar, but only because the corpus fixes
one weight pair. Any p ≠ n assignment of other weights would be a choice; none is made.

Precision preflight (`scripts/precision-gates.sh --changed`): exits 1 on tree-wide reds
(q0-anchor flip, refill, dps ratchets, reference-literal, witness-value copy, q0-value drift).
None of them names a file of this branch; the new witness is skipped as a new file. The audit
witnesses the gate rewrote were reverted, not committed.

## 2. The functional and its corpus derivation (arm W)

| step | source |
|---|---|
| Convention D's Markov trace is the U_q(sl₂) quantum trace Tr(K^{⊗n}·)/[2]ⁿ, K = diag(q, q⁻¹) | bean `qou-99qc`, 2026-11-19 05:10Z; check Tr(K⊗K Ř)/[2]² = z_D, re-run here (D1) |
| On a weight space K^{⊗3} is a scalar: q on W_p = (2,1), q⁻¹ on W_n = (1,2) | `NucleonWeightSpaceTwoTerm.trace_Kp_word`, `trace_Kn_word` |
| Proton and neutron = the T³ = +½ and −½ sectors, with u = e₁ | `qou-99qc` 2026-11-15 note; np-splitting audit §13–§15 (orientation forced, PR #7971) |
| The element is V³ for both nucleons | PR #8564 (`frobeniusSelected_ten_unique`) |

So ε_p(X) = q·tr_{W_p}(X)/[2]³, ε_n(X) = q⁻¹·tr_{W_n}(X)/[2]³, and
ε_flavour = ε_n − ε_p. The normalisation [2]³ is not a choice. It is what makes the sum over all
four weight spaces equal the z_D Markov trace. The probe checks this sum against the Hecke /
Wedderburn route of PR #8564 for V⁰ … V¹⁰: they agree to 5e-31, which is the precision of that
witness (D2).

**A second normalisation is possible, and it gives zero.** Divide each sector by its own
dimension, i.e. take the plain trace per sector. The plain traces on W_p and W_n are equal for
every braid word (`NucleonWeightSpaceTraces.trace_word_eq`). So this functional vanishes
identically. That is scope (b) for that functional; the invariant is the intertwiner P(q). The
two normalisations are not equally corpus-backed: [2]³ is the one registered in `qou-99qc`. Both
are reported, and neither was chosen by its Q_β.

## 3. Lean (`QOU/QBeta/FlavourWeightSplit.lean`)

Generic `[Field R]`, except the non-vanishing (§7c: an order is needed, so ℝ after the wall).
Verified with `lean -DautoImplicit=false -s 65536`: exit 0, no `sorry`. `#print axioms` on all
eight results below gives only `propext`, `Classical.choice`, `Quot.sound`. The three imported
`NucleonWeightSpace*` modules were rebuilt from this branch's source into a private olean
directory (not the shared trees), so the check is against this branch's source.

| theorem | statement |
|---|---|
| `epsFlavour_V3_eq` | ε_n(V³) − ε_p(V³) = (q²−1)P(q)/(q⁴(q²+1)³) |
| `epsP_bar_eq_epsN` | ε_p at q⁻¹ = ε_n at q (bar swaps the T³ components) |
| `fV3_bar_odd`, `epsFlavour_V3_bar_odd` | ε_flavour(V³)(q⁻¹) = −ε_flavour(V³)(q) |
| `epsFlavour_V3_neg`, `_ne_zero` | ε_flavour(V³) < 0 on 1 < q ≤ 23/20 (the range of #8564's selection theorem) |
| `normalised_split_V3_eq_zero` | per-sector-normalised split = 0 |
| `trace_mirror_V3A` | antipode image (σ₁⁻¹σ₂)³ has the same weight-space trace as V³ |
| `trace_inv_V3A` | V⁻³ has the same weight-space trace as V³ |
| `trace_commutator_eq_zero` | γ(φ)γ(ψ) and γ(ψ)γ(φ) have equal trace on the weight space, for the σ₀σ₁⁻¹ photon |

The last three are the arm-γ zeros: the antipode-odd part, the mirror (V³ ↔ V⁻³), and the order
of the two photons are all invisible to every K-weighted weight-space trace of V³. In the probe
the same holds for the full 8-dim z_D trace, with V⁶ too (G2, G3).

V⁶ and V⁹ are exact in the probe (sympy over ℚ(q)), not in Lean. Their closed forms are in the
witness, and both are also exactly bar-odd (W2).

## 4. Numbers (computed first, compared after)

Proton q₀ = 1.10997858275138…, 70 dps, E₀ = `qbeta_e0.canonical` (tower-summed) = 4.22748335562903 MeV.

| element | ε_flavour at q₀ | Q_β (MeV) | vs CODATA 0.78233341 | F_required |
|---|---|---|---|---|
| **V³ (selected, cost-minimal)** | −0.07698053460 | **0.325433929** | −58.402 % | 2.40397 |
| V⁶ (survivor, reported) | −0.07653295538 | 0.323541795 | −58.644 % | 2.41803 |
| V⁹ (survivor, reported) | −0.07578988202 | 0.320400465 | −59.046 % | 2.44174 |
| arm γ (any linear ε) | 0 | 0 | −100 % | — |
| arm W, per-sector normalised | 0 | 0 | −100 % | — |

**Not blind, stated plainly.** The np-splitting audit (2026-11-15, §18 and §21) already records
|t_n − t_p| = 0.076981 for the same trace on V³ and 0.3254 MeV after E₀^full. There it was read
as m_n − m_p. I read that figure while searching the corpus, before computing anything here, and
put it in the pre-registration (commit `d70a51ff51`). The CODATA Q_β value is also printed in
AGENTS.md. So "computed before comparing" holds only in the weak sense that the probe reads the
comparison column last. Nothing was selected: the functional, the normalisation and the element
were all fixed by the corpus before any of these numbers.

## 5. What this means, and what it does not

- **Scope (a) for the value.** Under this functional, the selected base V³ undershoots Q_β by
  58 %. The ladder cap cos ≤ 1 (`LadderFactorBound`) excludes F_required = 2.40, as it does for
  the 1.759 of the earlier z_D base. So no c_k ladder of that form can close it.
- **The magnitude is O(h) and comes from the K-weight.** ε_flavour = (q⁻¹ − q)·tr_W(V³)/[2]³.
  The word enters only through tr_W(V³) ≈ 2.99, close to dim W = 3 (V⁶ and V⁹ move it by at most 1.5 %). The flavour content
  is entirely the factor q⁻¹ − q = −h. That is the same "the word does not matter" pattern
  np-splitting §13 found for n/p.
- **Sign.** ε_flavour < 0: the neutron component is smaller. Q_β uses |·|, so the sign does not
  enter Q_β. But it does enter the reading "mass ∝ trace", and under that reading the neutron
  comes out lighter, the wrong sign. That repeats np-splitting §21 for the same trace.
- **Q_β vs m_n − m_p.** The corpus now holds one number, |ε_flavour(V³)|·E₀ = 0.3254 MeV, under
  two incompatible identifications: Q_β (this ruling) and m_n − m_p (np-splitting §18). They
  differ by m_e under the kinematic identity m_n − m_p = Q_β + m_e. At most one of them can be
  right. That is an owner decision (§6, D2).
- **Bar parity.** AGENTS.md (2026-11-15, D-W2) removed the sentence "Q_β is the bar-odd sinh
  partner of m_π", because no Q_β functional on record had a definite parity. ε_flavour is a new
  functional, and it **is** exactly bar-odd: this is proved (`epsFlavour_V3_bar_odd`), not
  asserted. This does not reinstate the removed sentence: nothing here is about m_π, and the
  removed sentence was about the old functionals. It is consistent with the taxonomy block
  (weak = bar-odd). Whether it should change that block's wording is for the owner.

## 6. Owner decisions

**D1. Adopt ε_flavour as the ruled ε for Q_β on the γγ base?**
- *Adopt (global [2]³ normalisation).* Means: Q_β is scored as 0.3254 MeV (−58.4 %) on the
  scorecard. Costs: one witness re-score (`per-observable-100x-status`), the content blocks that
  quote the ruled base. Risks: the L2 Q_β row moves from the conflicting 0.449 / 0.652 cells to
  0.325. The move is reversible. Commits: the [2]³ normalisation becomes canonical, and the
  flavour sector of every later ε (e.g. a ladder) has to sit on it.
- *Keep Q_β = 0 (the γγ base's scope-(a) prediction, as recorded).* Means: flavour is not part
  of ε, and the 0.325 stays a diagnostic. Nothing to re-score.
- *Default if you say nothing:* nothing changes. The scorecard keeps its present cells, and this
  PR only adds a Lean file, a probe and this doc.
- **Recommendation (my judgement):** adopt as a *diagnostic row*, not as the scored cell. It is
  the first derived non-zero Q_β on an SDP-admissible element. But it is 58 % short and outside
  the ladder cap, so scoring it would display a gap that no admissible ladder can close.

**D2. Is |ε_flavour(V³)|·E₀ Q_β or m_n − m_p?**
- *Q_β (this ruling):* then m_n − m_p = 0.836 MeV (−35.3 %), and np-splitting §18's D1 row is
  wrong by m_e. Costs: one append to that audit.
- *m_n − m_p (np-splitting §18):* then Q_β = −0.186 MeV, which is negative. That is impossible
  for a Q-value, so this reading is excluded on its own terms.
- *Default:* both stay on record, contradicting each other.
- **Recommendation (my judgement):** Q_β. The other reading forces a negative Q_β.

## 7. Open gaps

- `qou-99qc` stays open (rule 13a). The ε question is not closed: this is one corpus-derived
  candidate with a 58 % miss and a sign problem under "mass ∝ trace".
- The photon definition on main (σ₀σ₁ vs σ₀σ₁⁻¹) is being corrected elsewhere. Arm γ uses
  σ₀σ₁⁻¹ throughout. Under σ₀σ₁ the derived factorisation is the same element V³ (the corpus
  block writes V = σ₀σ₁ − hσ₀), so arm γ's conclusion does not depend on which form wins.
- The corpus has no derivation of colour weights other than the eigenvalue pair. A derived
  weight assignment that differs between p and n would be needed for arm γ to give anything.
  Searched: `photon`, `gamma-gamma-generates-particles`, `breit-wheeler-pair-production-derivation`,
  `borromean-two-photon-factorisation`, `quark-antiquark-production*`, `meson-formation-chain`,
  `trivial-knot-photon-interpretation*`, `knot-basis-color-content`, `nucleon-derivation-intro`
  (content tree only, grep on "colour/color weights", "Hopf dressing", "varphi"). This is
  "I found none in those files", not "none exists".
- V⁶ and V⁹ are not in Lean.

Probe: `computations/probes/qbeta_flavour_weight_split/qbeta_flavour_weight_split_probe.py`
(24/24, witness `qbeta-flavour-weight-split.witness.json`). Pre-registration:
`PREREGISTRATION.md` in the same directory.
