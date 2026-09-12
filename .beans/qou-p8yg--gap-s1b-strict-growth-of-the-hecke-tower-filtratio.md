---
# qou-p8yg
title: 'GAP S1b: strict growth of the Hecke tower filtration -- H 1 < H 2 is a WIRE (H3 exists sorry-free); general n needs the (n+1)! lower bound'
status: todo
type: task
priority: normal
created_at: 2026-09-12T19:02:09Z
updated_at: 2026-09-12T19:02:10Z
---

Parent: qou-cins / plan qou-0fmb, epic qou-08a2. Opened 2026-09-12 after S1 merged (#7228, 3653e9ce).

## What S1 left open
QOU/MathlibExt/HeckeTowerWitness.lean proves twH_mono (<=) and twH_zero_lt_one (H 0 < H 1, via the rank-2 collapse). It does NOT prove H n < H (n+1) for n >= 1: the collapse map sends every generator to the same element, so it cannot separate H 1 from H 2.

## H 1 < H 2 is a WIRING job, not a build -- the separator already exists sorry-free
Corpus-grep 2026-09-12 (path 3) found the rank-6 object this needs, already proved:
  QOU/SchurWeyl/HeckeDim3Dim.lean   finrank_hecke3 : finrank R (Hecke R q q^-1 2) = 6
                                    sixBasis : Module.Basis (Fin 6), sixFamily_indep
  QOU/SchurWeyl/HeckeDim3Indep.lean sixWords_indep
  QOU/SchurWeyl/HeckeDim3.lean      braid3 : s0*s1*s0 = s1*s0*s1
All sorry-free (verified: the 10 'sorry' grep hits in HeckeCoset.lean are ALL the words "sorry-free" in docstrings -- prose, not code; qou-uoal's sorry-free claim HOLDS).

PROOF SKETCH (worked out, not guessed). Define phi : HeckeTower R h -> Hecke R q q^-1 2 by
    g0 |-> sigma0,  g1 |-> sigma1,  g m |-> q*1  for m >= 2.
Relation check:
  * far(m,k) for m >= 3 forces phi(g m) to commute with BOTH sigma0 and sigma1, i.e. to be central. A scalar is.
  * quad on a scalar c needs c^2 = h*c + 1; with h = q - q^-1 the root c = q works exactly.
  * braid(0) is g1 g0 g1 = g0 g1 g0 |-> sigma1 sigma0 sigma1 = sigma0 sigma1 sigma0 = HeckeDim3.braid3.
  * braid(m>=1) and far(2,0) reduce to scalar identities.
Then phi(twH 1) = adjoin{sigma0} = span{1, sigma0} (2-dim) while phi(g 1) = sigma1, and sigma1 is not in span{1,sigma0} by sixWords_indep. Hence twH 1 < twH 2.

NOTE the h = q - q^-1 specialisation: this separator needs a base ring carrying q, so the wired theorem is at R = the Hecke base ring, not the fully generic {R : CommRing}. That is a real scope narrowing and must be stated, not glossed.

## What is GENUINELY open: general n
H n < H (n+1) for all n needs dim H_n(q) >= n! -- the LOWER half of the Iwahori-Hecke basis theorem. qou-uoal (COMPLETED) supplies only the upper half, finrank_le_factorial <= (n+1)!, and its own closing note names the blocker: "Lower bound dim>=(n+1)! needs general Hoefsmit (qou-im9l)".

LEAD, not a claim: qou-im9l is itself now COMPLETED (general-lambda Hoefsmit seminormal rep + braid; residual qou-gjg6 also completed). So the stated blocker may already be discharged and the lower bound may ALSO be a wire. NOT verified -- whoever picks this up should corpus-grep whether the (n+1)! lower bound was ever derived from the completed Hoefsmit rep before assuming it is open.

## Also fix while here (minor, from the #7228 verification)
exists_tower_with_nonzero_h takes hne : h != 0 and concludes (forall m, quad) AND h != 0 -- the second conjunct merely restates the hypothesis. Not vacuous (the first conjunct is real content) but it is noise. Restate as the two genuine non-degeneracy facts: (forall m, twGen quad with the given h) AND twH 0 < twH 1, with no restated hypothesis.

## Discipline
No fit. Per rule 13a this stays open until the mathematics closes. Do NOT close it on the strength of the H 1 < H 2 wire alone -- that is one level, not the filtration.
