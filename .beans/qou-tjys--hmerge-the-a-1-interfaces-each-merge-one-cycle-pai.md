---
# qou-tjys
title: 'hmerge: the A-1 interfaces each merge one cycle pair -- discharge ClassicalTraceFloor''s second stated hypothesis'
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T22:01:59Z
updated_at: 2026-09-04T22:02:31Z
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
