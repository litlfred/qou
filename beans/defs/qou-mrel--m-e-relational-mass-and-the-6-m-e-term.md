---
# qou-mrel
title: Where does m_e come from? — relational mass and the unexplained −6·m_e term
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-06T00:00:00Z
updated_at: 2026-11-18T09:58:42Z
parent: qou-wp3h
---

## Owner question (2026-08-05/06)

> "i still dont know where m_e comes from in mass and markov trace. it's been
> declared, but somehow what we are calculating is maybe the knot operation
> which is the electron convoluted with the knot we are calculating — more like
> the 'mass force' of an electron interacting with a particular knot/particle,
> like a point mass / test particle calculation. It is not an intrinsic mass but
> the measurement of the interaction between the particle and the electron, and
> so that's why m_e appears. … there isn't really intrinsic mass, but effective
> mass (cf. solid state) … in QOU mass is relative to q_0, and we don't have
> intrinsic things, just relational things. So mass has to be relational. See if
> in the canonical derivation of mass / binding we hid the m_e in there in such
> a way."

## What the code actually shows

`computations/canonical_mass.py`:

    m_p   = dim V_{(2,1)} · (m_μ · F_Bor − |S_3| · m_e) = 2·(m_μ·F_Bor − 6·m_e)
    m_μ   = m_e · Vol(4₁) / ℏ_q²
    F_Bor = |tr_M(β_Bor)| · [3]_q! / q³        (dimensionless)

Substituting the muon anchor:

    m_p = 2 · m_e · ( Vol(4₁)·F_Bor/ℏ_q² − 6 )

**m_e factors out completely.** The predicted object is the dimensionless ratio
m_p/m_e; m_e is pure unit conversion. So the owner's framing is *already*
literally true of the production formula: QOU predicts no intrinsic mass, only
ratios. `tr_M` itself is a q-polynomial and carries no m_e at all.

## The actual open question — the `− 6·m_e` term

m_e appears **twice**, and only one appearance is the scale:

1. as the overall unit (via the muon anchor) — absorbed, uncontroversial;
2. as `|S_3| · m_e = 6·m_e` **subtracted**, once per Hecke block, ×2 via
   `dim V_{(2,1)}` ⇒ `−12·m_e` in total.

A pure unit conversion cannot leave (2). It is a *discrete count of electron
masses*, structurally a binding / self-energy correction denominated in electron
quanta — which is exactly what the owner's "energy cost of the interaction
between the particle and the electron" reading predicts, and what the corpus's
"m_e = CAL-1, the dimensional unit" framing leaves unexplained.

## What is open

1. **Is `−|S_3|·m_e` an interaction/self-energy term?** The corpus takes the 6
   as `|S_3|` by construction (order of the symmetric group on 3 strands) and
   offers no physical reading. Derive it, or show the identification is
   coincidental.
2. **If yes, is the whole formula a test-particle (point-mass) measurement?**
   i.e. is `m_p` in QOU literally the interaction energy of the Borromean braid
   against an electron probe, rather than a property of the braid? That would
   make the electron's appearance structural rather than conventional.
3. **"Mass channels per force."** The owner's stronger claim: we observe only the
   long-range EM channel, so the m_e-denominated number is the *EM mass channel*,
   and there should be separate channels per force. Nothing in the corpus
   tracks per-force mass channels. Is that formalisable — e.g. as a decomposition
   of `tr_M` by Wedderburn block matched to interaction type?
4. **Effective-mass analogy.** Solid-state effective mass is a response
   coefficient, not an intrinsic property. If QOU mass is the same kind of
   object, the framework should say so explicitly in the mass chapter rather
   than calling m_e "the dimensional unit".

## Do not

Do not "resolve" this by re-deriving that m_e cancels in ratios — that is
already known and is not the question. The question is the `−6·m_e` term and
whether the electron's role is conventional or structural.

## Cross-refs

`docs/canonical-mass-formula-guardrail.md`; `observations/epistemic-status-of-calibrations.md`;
AGENTS.md §"Canonical derivation chain" (CAL-1 = m_e as "the dimensional unit").

### Progress Update (2026-11-16, PR #8171)
- Defined `protonOverMeDimensionless` in `folio/quantum-observable-universe/lean/QOU/AppendixQValues/ProtonBorromeanAssembly.lean` and proved `proton_mass_factors_mE` (`protonMassFromLoop m_e V_e = m_e * protonOverMeDimensionless V_e`) and `proton_mass_homogeneous_in_scale` (`protonMassFromLoop (λ * m_e) V_e = λ * protonMassFromLoop m_e V_e`) with `0` `sorry`.
- Verified at 80 dps at $q_0$ in `computations/probes/delta_split_mrel_four_phi_resummation_probe.py` (`computations/probes/delta-split-mrel-four-phi-resummation.witness.json`).
- Opened PR `litlfred/qou#8171` (`1c72739193707fef67fbebe3aa153f994c73933e`). Keeping status `in-progress` pending owner review.


## 2026-11-18 — owner ruling: the 12 is labelled a FIT

Owner tapped "Label as fit + open gap bean". PR #8418 / issue #8417 label the integer 12 (= 2·6 in −|S_3|·m_e) as fitted in `partition-sum-proton-residual` (prose + authorNotes) and in the `canonical_mass.py` docstring. Context: PR #8120 (merged 670bafd) showed the residual vs the live convention-D tower is −12 m_e at the proton pin (round trip, q₀ solved from the identity) and −11.99955 m_e at the muon pin (m_p 244 ppb low). Chance estimate: nearest integer multiple of m_e is always within ~272 ppm, so 244 ppb is ~1e-3 by chance, before look-elsewhere on the formula shape. This bean stays OPEN: the −6·m_e term still has no derivation (open conjecture-level gap, do not close).
