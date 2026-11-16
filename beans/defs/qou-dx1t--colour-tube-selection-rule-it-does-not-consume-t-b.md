---
# qou-dx1t
title: 'Colour-tube selection rule: it does NOT consume t, but it cannot produce it either -- floor overshoots 2H by 3.2%'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T14:12:47Z
updated_at: 2026-11-16T18:04:00Z
parent: qou-10v9
---


Branch: claude/anchor-followups-2026-08-08.
Source: 7-agent adversarial workflow (2 independent refuters), 964k tokens.
Both refuters REFUTED the positive claims of the first draft and the negative
conclusion SURVIVED both. Numbers below are the ones that survived refutation.

## RETRACTION FIRST -- my own premise was wrong

I briefed the workflow with "no Lean file mentions the colour-tube selection
rule". FALSE. It is
folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/ColorFlavorIsospinSelection.lean
128 lines, added by b86ae520, imported at QOU.lean:399, in the build graph.

## WHAT IS ACTUALLY IN LEAN

  inductive NucleonPair (pp | nn | pnSym | pnAlt)          :52-54
  NucleonPair.isospin, a 4-entry table                     :58-59
  inductive ColorSystem (altT1 | symAH)                    :71-74
  def select p := if p.isospin = 1 then altT1 else symAH   :79-80
  class InterfaceExchangeAntisymmetry, NO instance         :87-91
    field: antisymmetry_forces_select : coupling = select

Every downstream theorem is `rw [h.antisymmetry_forces_select]; rfl`.
NO colour weights, NO contraction, NO rational arithmetic, NO t in the file.
The numbers 1/6, 1/3, 2/15, 1/10 appear ONLY in a docstring at :103-104.

## DEFECT FOUND AND FIXED THIS SESSION

The class docstring claimed it "is not vacuously satisfiable". That is FALSE:
`<select, rfl>` inhabits it in one line. Fixed -- docstring corrected and the
witness is now MACHINE-VERIFIED as `trivially_inhabited : Nonempty
InterfaceExchangeAntisymmetry`. Deliberately a Nonempty theorem, NOT an
instance: an instance would let typeclass resolution silently discharge every
`[InterfaceExchangeAntisymmetry]` below and convert four conditional theorems
into unconditional ones about `select` -- true, worthless, and easily misread as
the physics being proved. lake build exit 0.

The class's real content is a PHYSICAL identification -- "the coupling the
physical interface induces is `select`" -- which no Lean instance can establish.
Conditional for that reason, not the stated one.

## THE GOOD NEWS: COLOR_WEIGHTS DOES NOT CONSUME t

Provenance re-derived and MEASURED clean.
computations/color_tube_flavor_isospin_selection.py:65-69 are diag/trace of the
three isotypic projectors hardcoded at color_tube_t1_tensor_decomposition.py
:141-145, normalised :150-152:
    P_A = (1/3) v v^T      traces 1, 3, 5  ->  (1/3, 0), (0, 1/6), (2/15, 1/10)
    P_alt = (1/2)(I - swap)
    P_H = P_sym - P_A
No h, no z, no delta, no alpha, no target enters. FIRST object in this whole
investigation that is genuinely independent of t.

## THE FATAL NEWS: IT CANNOT PRODUCE t EITHER

To get a number you must contract W against a flavour->t dictionary tau
(InterNucleonChannelColorTube.lean:129-133). EVERY tau in the corpus contains
the answer slot:
  * pyhecke/atom.py:400   _d_avg = -h_loc/2          set by fiat
  * closed_form_tau_M.py:322  z - h*(1/2 - delta/4)  set by fiat again
So the self-consumption is INHERITED, not escaped -- and it is TOTAL, not
partial. MEASURED: under chiralitySign, p=(u,u,d) x n=(u,d,d) gives 4
flavour-matched contacts (t=0) and 5 mixed (t=x), so for EVERY admissible W and
every colour alignment t_pn = c*x with c a pure number. The colour tube supplies
ONLY A MULTIPLIER ON THE ANSWER. Not "55.6 % of the weight in the answer slot"
as I briefed -- 100 %.

Under the atom.py dictionary, t_pn = x + w_dd(1-2x), which at x = 1/2 is
IDENTICALLY 1/2 for all three colour systems and all six alignments. Rank zero.
(That dictionary is also intra-nucleon: pairs = [(0,1,0),(0,2,0),(1,2,1)] at
atom.py:408 braids the three quarks of ONE nucleon.)

## THE MISS -- and it converges with qou-4g4a

Scanning the one open parameter lambda on a 1/100 grid x all 6 colour
alignments, mpmath 30 dps, z = 0.61268804, h = 0.20906030, alpha = 4.18598136:

                            t range        B_pn range (MeV)
  corpus eps rule (R2)      [1/6, 1/2]     [2.29580, 2.83375]
  S_3-averaged (confinement) 5/18=0.27778   2.46755
  atom.py dictionary (R1)   {1/2}          {2.83375}
  REQUIRED                  0.1192267      2.224566

The FLOOR of the entire family -- pure A, most favourable alignment -- is
B = 2.29580 MeV, overshooting B_AME(2H) by 0.0712 MeV (3.2 %). THE TARGET LIES
BELOW THE CLOSED FAMILY. Averaging over S_3 as confinement demands annihilates
all W-freedom and lands on 2.46755 MeV, 11 % high. Reaching the target needs
x = 0.35768, not 1/2 -- i.e. you must already know the answer.

CONVERGENCE: this is a THIRD independent route to the same wall. qou-4g4a shows
the interface band lies strictly between the two isospin weights; this shows the
colour-tube family's floor sits above the deuteron. Different mechanisms, same
verdict: the deuteron's d = -0.11923h has no derivation in the present arena.

## t_req CORRECTED

t_req = 0.119226678, NOT the 0.119453 I briefed (traced to .beans/qou-kj4v).
0.119453 back-solves to alpha = 4.185346, not the corpus alpha, and gives
B = 2.224903, high by 3.4e-4 MeV. My own independent computation this session
gave d_req/h = -0.1192268103, confirming the corrected value.

## THE CATEGORY ERROR -- decisive on its own, independent of any number

Contracting COLOR_WEIGHTS against a definite product (F1,F2) = (p,n) violates
the rule's OWN premise. The surviving couplings are entangled colour(x)flavour
states; the deuteron line is (pn - np)/sqrt(2), on which F1 and F2 are NOT
definite. But InterNucleonChannelColorTube.weight (:148) has type
  ColorSheet -> ColorSheet -> NucleonColorContent -> NucleonColorContent -> Q
-- it consumes DEFINITE nucleon content. The rule selects a state the type
cannot express. Any t extracted by that contraction is already outside the
rule's scope, which makes the 3.2 % numeric miss a courtesy, not the argument.

## VERDICT

Do NOT write a new Lean scaffold -- it exists. Do NOT pursue the colour tube as
a source of t. The remaining honest options are the ones qou-4g4a leaves:
enlarge the arena (H_4), or find a genuinely different pairing between the
isospin label and the bond.

## HOUSEKEEPING

One workflow agent deleted and re-cloned /workspace/qou/.lake/packages
(mathlib et al), ~3.8 GB. VERIFIED HEALTHY afterwards: root .lake 626M with all
9 packages present, content/.../lean/.lake 2.4G with all 9, and every build this
session exits 0. No action needed, but read-only briefs need to say "do not
touch .lake" explicitly.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-09 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-16 — Proton–neutron contact split and linear contraction `t_{pn} = c(W)*x` formalized in `InterNucleonChannelColorTube.lean` (PR #8145)

- Verified `ColorFlavorIsospinSelection.lean` (`trivially_inhabited : Nonempty InterfaceExchangeAntisymmetry`) and extended `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/InterNucleonChannelColorTube.lean` with sorry-free theorems:
  - `proton_neutron_contact_counts`: proves by `decide` that across the 9 colour-sheet contacts of `(proton, neutron)` (`uud x udd`), there are exactly `4` matched contacts (`epsilon = +1`), `5` mixed contacts (`epsilon = 0`), and `0` conjugate contacts (`epsilon = -1`).
  - `pnContractedOffset_eq_mixedWeightSum_mul`: proves that for any colour-pair weight tensor `W` and mixed-contact offset datum `x`, `pnContractedOffset W x = pnMixedWeightSum W * x` (`t_{pn} = c(W) * x`), confirming in Lean that `W` scales `x` linearly by `c(W)` and cannot eliminate `x` unless `c(W) = 0`.
  - `uniform_pnMixedWeightSum` & `uniform_pnContractedOffset`: proves `pnMixedWeightSum uniformWeight = 5 / 9` and `pnContractedOffset uniformWeight x = (5 / 9) * x`.
- Status kept `in-progress` pending merge of PR #8145 (`ed78b60a0ffe233f132df45a37bb1456ec237832`).
