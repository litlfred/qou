---
# qou-tjys
title: 'hmerge: the A-1 interfaces each merge one cycle pair -- discharge ClassicalTraceFloor''s second stated hypothesis'
status: in-progress
pr: 8197
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T22:01:59Z
updated_at: 2026-11-16T20:55:10Z
parent: qou-v2om
---

Successor to qou-qro1 (OrbitCount.lean, merged as a08dce2497). That bean proved
the general transposition step; this one applies it to the specific word.

TARGET. ClassicalTraceFloor.lean states step 2 as TWO hypotheses:
    hfree  : cFree = 2 * A
    hmerge : cFree = cAtom + (A - 1)
both 'verified for A = 2..20 directly from the words'. hfree is already
addressed by orbitCount_prod_of_disjoint_unit_defect (qou-qro1). hmerge is
A-1 applications of orbitDefect_swap_mul_of_not_sameCycle.

WHY IT IS FORMALIZABLE AT ALL. atom_braid_word_3A is NOT a braid word -- every
letter is a Hecke element c*sigma_g + d*1 and 2A+1 of them are averaged, so the
object is outside the image of rho : B_n -> H_n(q). But at q = 1,
h = q - 1/q = 0, so EVERY offset template {0, -h, -h/2, -h(1/2 - delta/4)}
vanishes at once and the letter degenerates to the transposition s_g. So the
q=1 shadow is determined by the g-INDEX SEQUENCE ALONE, which is q-independent
by nucleon_gen_chains' own docstring ('the structural pattern is q-INDEPENDENT;
only h carries q'). That sequence is integer data -- extracting and reasoning
about it involves no arithmetic at all, so NO-FLOAT64 is satisfied trivially
rather than by care.

WHY IT IS WORTH DOING AFTER #6611. That PR refutes B = Q_beta*Delta_tr (p5-p95
1592x) and replaces it with B = E_0*log(tr_free/tr_atom). The replacement is
LOG OF THE SAME NUMBERS, so tr_free and tr_atom remain load-bearing. At q = 1,
Schur-Weyl gives tr = 2^(c - n), hence
    log(tr_free/tr_atom) = (cFree - cAtom) * log 2
and hmerge says that bracket is exactly A - 1. So hmerge IS the classical limit
of the surviving law, and the limit is (A-1)*log 2 -- a pure bond count with no
ansatz, matching #6611's own finding that 'layout-free bond counting beats every
isospin-resolved variant'.
NOT YET VERIFIED: that last paragraph is my inference from combining #6611's law
with ClassicalTraceFloor's step 1. It is the first thing the probe below checks;
do not repeat it as established until it does.

NO MAGNITUDE IS CLAIMED. E_0 is a calibration, not a derivation (qou-59j5), and
#6611 leaves 'E_0 is 2.656x below the best single scale' open. (A-1)*log 2 is a
SHAPE claim, scale-free in the same sense the mirror-sign test of qou-z4ba was.


LEAN HALF DONE 2026-09-05, PR #6716, sorry-free. BOTH hfree and hmerge follow from
ONE lemma: orbitDefect_freshProd -- a list of transpositions whose right endpoints
are each FRESH (never an endpoint of an earlier letter) has orbit defect exactly its
length. Each step is orbitDefect_swap_mul_of_not_sameCycle from qou-qro1; its
not-SameCycle hypothesis comes free because a fresh endpoint is still a FIXED POINT
of everything applied before it.

THE MEASUREMENT THAT MADE IT EASY, and it was not what I predicted. I expected to
have to model the intra-nucleon chain (sigma_0 sigma_1^-1)^3 plus quark pairs. In
fact each block's ELEVEN letters collapse to ONE transposition, swap(3k, 3k+1) --
the same one for every k, proton or neutron. So the whole shadow is 2A-1
transpositions in word order:
    swap 0 1,  then for k = 1..A-1:  swap(3k-1, 3k), swap(3k, 3k+1)
whose right endpoints run 1, 3, 4, 6, 7, 9, 10, ... strictly increasing. Freshness
is then immediate, and it is exactly WHY every interface merges rather than splits.

WHAT IS AND IS NOT CLOSED. Lean does not know what the producer returns, so the
corollaries read 'IF the shadow is this list, THEN the counts are 2A and A+1' --
the same epistemic shape as ClassicalTraceFloor's own hypotheses. The gain is that
TWO NUMERICAL hypotheses become ONE STRUCTURAL one about the word's letters, which
is far more directly checkable against the producer than a tabulated count. It is
NOT a formalisation of atom_braid_word_3A, and the file says so.

TRAP FOR THE NEXT AGENT. freeIdx/atomIdx are a TRANSCRIPTION of a measured pattern.
A transcription slip yields TRUE theorems about the WRONG word, and nothing in the
Lean would notice. Four 'example ... := rfl' anchors now pin them to the measured
sequences so a drift fails the build. If you extend the pattern, extend the anchors.

STILL OPEN, unchanged: the Schur-Weyl leg tr = 2^(c-n) (ClassicalTraceFloor step 1,
assumed as a published theorem because Mathlib has no Schur-Weyl duality).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (PR #8197 — `status: in-progress`)

- [x] Formalized pure Lean 4 module(s) (`QOU/MassTheory/BorromeanShadowCycleMerge.lean`, `QOU/MassTheory/SecondOrderContentCancellation.lean`, `QOU/Hecke/DeltaLongEMinusOrderingSplit.lean`, `QOU/MassTheory/LoopValueNormaliserAndFrameDiff.lean`) with `0 sorry` and `0` findings across all 6 static vacuity audits.
- [x] Added 50-dps `mpmath` + exact rational probe `computations/probes/borromean_shadow_c2_deltal_loop_frame_probe.py` and 2-commit stamped witness `computations/probes/borromean-shadow-c2-deltal-loop-frame-probe.witness.json` (`allPassed: true`, `0` raw `float64`).
- [x] Opened and signed [PR #8197](https://github.com/litlfred/qou/pull/8197) (`ready: 4a2ed9a21b68b7d23b2e693b68f472d7dcf102a6`).
