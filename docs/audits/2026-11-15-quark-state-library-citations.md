# Quark-state library citations: Finkelstein, Klein-Kreisler & Ruiz-Altaba, Gresnigt

Bean `qou-qs3l` (epic `qou-qs0e`). Date 2026-11-15. Branch
`claude/quark-state-sm-eightfold-map-2026-11-15`, PR #7823.

**Question.** Three held papers are cited by no content block. What could each supply as a
**citation** (precedent, not derivation) for a quark-state definition on the Hecke tower
`H_n(q)`, real `q₀ ≈ 1.10998`?

**Answer in one line.** All three are precedent only. None uses Hecke normal forms. None works
at a real `q > 1` that matches `q₀`. None derives a charge formula: Finkelstein solves for his
constant, Klein-Kreisler postulates charge, and Gresnigt assigns charge by hand. Both
deformed-SL(2) papers put the **mixed (2,1)-type state** at the level of **preons**
(Finkelstein) or **nucleons** (Klein-Kreisler), never at a single quark. That bears directly
on the epic's working hypothesis (§4).

**How this was read.** The full `library/<id>/sections/*.md` of each paper, which are
LaTeX-sourced and complete; none of the three has an `ocr/` tier. The Klein-Kreisler nucleon
state and the Finkelstein `k = e/3` clause were spot-checked against the section text by the
author of this note. Bibliography: `folio/references/{finkelstein2008,kleinkreisler1996,gresnigt2019}.json`
all exist. Citations of each were found only in `folio/schema/references.ts`, the slug map, and
(for Finkelstein) `docs/audits/2026-09-04-carrier-derivation-held-literature-ledger.md` Route 1.

## 1. Finkelstein, *Knots and preons* — `finkelstein2008`, arXiv:0806.3105v3

**Construction.**
- **Algebra.** The coordinate algebra of SL_q(2), which the paper calls the "knot algebra"
  (§2, eq. 2.4). It is not U_q(sl₂), and not B_n or H_n(q).
- **States.** Matrix elements D^j_{mm'}(a,b,c,d).
- **Dictionary (eq. 2.7).** `j = N/2`, `m = w/2`, `m' = (r+1)/2`, where N counts crossings, w is
  the writhe and r the rotation.
- **Quarks.** The trefoil irreps D^{3/2}: (d,s,b) ↦ D^{3/2}_{3/2,−1/2}, (u,c,t) ↦ D^{3/2}_{−3/2,−1/2}
  (Table 1).
- **Charge (eq. 2.15).** Q_e = −(e/3)(m+m'), "**if and only if k = e/3**" (§2, line 171 of
  sec-001).
- **Preons (§3, Table 2, eq. 3.16).** d ~ ab², u ~ cd², with preon charges ∓e/3.
- **What is absent.** There is no colour assignment, no generation mechanism (§4 concedes "an
  unlimited number of excited states"), and q is generic, never given a value.

**Could supply.** Precedent for labelling electroweak quantum numbers of quarks by an
irreducible representation of a q-deformed SL(2), with a charge linear in knot invariants and
integral in units of e/3.

**Fitted content, called plainly.** The family ↔ trefoil ordering is *chosen* ("we have adopted
a particular relative order") so that one constant fits; `k = e/3` is then solved for. The
"if and only if" is uniqueness inside a one-constant ansatz, not a derivation of the charges.

**Conflicts with this corpus.**
1. **Algebra.** SL_q(2) is not Hecke. Reaching H_3(q) needs quantum Schur–Weyl duality as a
   separate citation, plus an explicit match of q normalisations.
2. **What j counts.** j counts *crossings*, not strands. The trefoil j = 3/2 is σ₁³ on two
   strands, not the three-strand (3) channel.
3. **Which irrep is the quark.** Under Schur–Weyl at N = 2 our (2,1) channel is spin ½, which is
   Finkelstein's **preon** D^{1/2}, not his quark D^{3/2}.
4. **Parity.** `QOU/Mass/SLq2LabelParity.lean` (corpus, per the ledger) shows the dictionary
   labels only even A.

**Suggested sentence.** "Assigning fermion quantum numbers to irreducible representations of a
q-deformed SL(2) has precedent: Finkelstein labels the four trefoil classes by
D^{N/2}_{w/2,(r+1)/2} and obtains Q_e = −(e/3)(m+m′) [finkelstein2008, §2, eqs. (2.7), (2.15)];
there the family-to-trefoil order is chosen so that a single constant k = e/3 fits."

## 2. Klein-Kreisler & Ruiz-Altaba, *The q-deformed quark model* — `kleinkreisler1996`, hep-ph/9612303

`kleinkreisler1996.json` has metadata taken from the PDF, unverified against a publisher record,
and no `issued` date.

**Construction.**
- **Algebra.** U_q(sl₂) as quantum **isospin**, with coproduct
  Δ(I±) = I± ⊗ q^{I₃} + q^{−I₃} ⊗ I± (§2).
- **Quarks.** (|u⟩, |d⟩) is the fundamental doublet. One family only; no colour, no generation.
- **Charge and mass.** Postulated, with trivial coproduct (§4).
- **q.** Real or a pure phase; all results are quoted for q real.
- **Δ⁺ (eq. 3.3).** (q|duu⟩ + |udu⟩ + q⁻¹|uud⟩)/√(q²+1+q⁻²).
- **Nucleon (eq. 3.5).** |p⟩ ∝ q⁻¹|udu⟩ + |duu⟩ − (1+q²)|uud⟩. This is the **mixed-symmetry
  doublet** in ½⊗½⊗½ = ½⊕½⊕3/2, chosen to be q-symmetric in the two spin-up quarks (§3,
  checked in section text).
- **Results.** For real q the additive baryon masses are q-independent (eqs. 4.2, 4.4), the
  pions stay degenerate (eq. 5.1), and only magnetic moments move (eqs. 4.7, 4.8).

**Could supply.**
- Precedent for quark flavour as a q-group doublet.
- An explicit q-deformed **mixed-symmetry three-quark state**, the U_q(sl₂) analogue of the (2,1)
  channel of V^{⊗3} at N = 2.
- A clean negative: for real q the additive mass operator does not see q.

**Fitted content.** Every q value is a fit, and the authors say so ("The reader ought to be
relieved that this numerology is over", line 262 of sec-001):
- q = 0.992 (≡ 1.008) is fitted to μ_n/μ_p under m_u = m_d.
- q = 0.991 is fitted using m_n − m_p.
- q = 0.324 is fitted to the pion splitting, which they conclude "cannot be naturally
  accommodated".

**Do not cite it in support of q₀.** Its q is a fit near 1 and is not q₀.

**Suggested sentence.** "Quark isospin has been modelled as a U_q(sl(2)) doublet, with the
nucleon as the q-deformed mixed-symmetry three-quark doublet [kleinkreisler1996, §3,
eq. (3.5)]; there q is fitted to the nucleon magnetic-moment ratio, and the additive mass
formulae are q-independent for real q [kleinkreisler1996, §4]."

## 3. Gresnigt, *Braided fermions from Hurwitz algebras* — `gresnigt2019`, arXiv:1901.01312

A review of the Bilson-Thompson helon model. The primary source, `bilson-thompson2005`, is held
and already cited at lepton level in `breit-wheeler-vertex-literature.md`.

**Construction.**
- **Quarks.** Three-ribbon braids in the circular B₃^c.
- **Charge.** "Quantized electric charges of ±e/3 are represented by integral twists of ±2π".
- **Colour.** "The color charges of quarks are accounted for by the permutations of twists"
  (§4.1).
- **Cl(6).** Twist vectors [a,b,c]·σ₂⁻¹σ₁ match Furey's Cl(6) minimal left ideal (§3.1, §5.1).
- **Representations.** Non-faithful quaternionic: σ = (1+I)/√2 and so on (§4.3).
- **q.** None anywhere; the model is undeformed.

**Our check, not a claim in the paper.** σ = (1+i)/√2 has eigenvalues e^{±iπ/4}. After rescaling
it satisfies the Hecke relation at q = e^{iπ/4}, an 8th root of unity, which is the opposite
regime from our real q > 1.

**Could supply.** Precedent for quark **colour coming from strand permutation** and charge from
twist. Cite `bilson-thompson2005` as primary and Gresnigt as secondary.

**Fitted content.** Nothing numerical. The twist ↔ charge and permutation ↔ colour dictionaries
are assigned by hand, and the "18 classes vs 16 fermions" count does not close (the paper says
so).

**Suggested sentence.** "In the helon model quarks are three-strand ribbon braids whose ±2π
twists carry charge ±e/3 and whose strand permutation carries colour [bilson-thompson2005;
reviewed in gresnigt2019, §4.1, §5.1]."

## 4. Bearing on the epic hypothesis

The working hypothesis in `qou-qs0e` takes the quark state as the degree-≥1 part of NF(γγ) in
H₃(q), projected to the (2,1) channel. Both deformed-SL(2) papers, read through Schur–Weyl at
N = 2, place the (2,1) three-strand state at **three-body** level:
- Klein-Kreisler: the (2,1) state is the **nucleon**;
- Finkelstein: spin ½ is the **preon**, while the quark is the crossing-count irrep j = 3/2.

`docs/audits/2026-11-15-quark-factor-relations-and-colour-channel.md` §2 reaches the same point
from the S₃ side. A three-strand (2,1) isospin channel at level 2 is an **isospin-½ three-quark
state**, a nucleon, not a single quark.

### Decision for the owner: how a future quark-state block uses these citations

**The decision.** When a quark-state block is written, does it cite these papers as general
precedent only, or does it also state the irrep mismatch? It needs the owner because it fixes how
the definition is framed against the literature.

**Option 1: cite general precedent only** ("quantum numbers as q-irrep labels").
- *Means:* one sentence, no irrep identification.
- *Costs:* minimal.
- *Risks:* a referee who reads Finkelstein or Klein-Kreisler finds that their (2,1)-type states
  are composites, which reads as an omission.
- *Commits to:* nothing.

**Option 2: cite and state the mismatch explicitly.**
- *Means:* add a sentence that in both papers the mixed channel is a preon or nucleon state.
- *Costs:* one paragraph.
- *Risks:* it advertises a tension with the epic hypothesis before that is settled.
- *Commits to:* settling, in `qou-qs1d`, whether "quark" means one strand or one channel.

**Recommendation (judgement).** Option 2. The mismatch is real and cheap to state, and §2 of the
factor-relations audit independently derives it.

**Default.** No content block cites these yet, so nothing changes and nothing breaks.

**Owner ruling 2026-11-15: Option 2.** A future quark-state block that cites these papers states the mismatch.
