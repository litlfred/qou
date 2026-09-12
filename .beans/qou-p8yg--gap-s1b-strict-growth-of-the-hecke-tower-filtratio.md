---
# qou-p8yg
title: 'GAP S1b: strict growth of the Hecke tower filtration -- H 1 < H 2 is a WIRE (H3 exists sorry-free); general n needs the (n+1)! lower bound'
status: todo
type: task
priority: normal
created_at: 2026-09-12T19:02:09Z
updated_at: 2026-09-12T20:12:36Z
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


--------
**2026-09-12, SAME DAY: THE PROOF SKETCH ABOVE IS REFUTED. Do not attempt it.**

The sketch sends g m |-> q*1 for m >= 2 and checks quad, far and braid(0). It does
NOT check braid(1), and braid(1) is what kills it.

With phi(g 2) = c*1 central and phi(g 1) = x:

    braid(1)   g2 g1 g2 = g1 g2 g1   =>   c^2 x = c x^2
    quad       x^2 = h x + 1         =>   c^2 x = c(h x + 1) = c h x + c
                                     =>   c (c - h) x = c

so if c is a unit, (c - h) x = 1 and x is a SCALAR. But x = sigma_1 is not a
scalar in H_3 (sixWords_indep). Contradiction: the algebra map DOES NOT EXIST.

This is not special to c = q. It is scope (b), a STRUCTURAL exclusion, and the
invariant is named: the braid relation together with the quadratic forces a
generator adjacent to a central-scalar generator to be a scalar itself. So EVERY
assignment sending all but finitely many generators to scalars collapses the low
generators too, and the whole "cheap finite separator" family is dead, not just
this member.

**Consequence: H 1 < H 2 is NOT a wire.** The rank-6 objects (HeckeDim3Dim /
HeckeDim3Indep) are real and sorry-free, but they cannot RECEIVE a map from the
N-indexed tower, so they do not yield strict growth. Strict growth needs the
Iwahori-Hecke coset basis, or the direct limit of HeckeInclusion.heckeIncl
together with injectivity of that inclusion -- i.e. exactly what the merged
HeckeTowerWitness docstring said before this bean narrowed it. The merged
docstring is CORRECT as written; this bean's narrowing was the error.

What survives from the narrowing, and is still worth having:
* HeckeMarkov3.markovTrace3 (finding 2) is untouched by this -- it is about the
  TRACE (S2 / qou-g8i1), not about separating the filtration, and remains a
  materially better S2 starting point than the rank-2 collapse.
* the obstruction itself is a formalize-first result worth recording in Lean,
  alongside #7153's braid_forces_eq_of_commuting_involutions, which is the same
  genre: a proved statement about which cheap witnesses CANNOT work.

Method note for the next agent: this was caught by reading the target's actual
API before writing the map, not by a probe. The sketch had been checked against
quad, far and braid(0) and looked complete; braid(m) for the INTERIOR index m=1
is the case a boundary-only check misses.


--------
**2026-09-12, THIRD PASS: the "genuinely open" item above is ALREADY DONE. Re-scope.**

This bean said general-n strict growth "needs the (n+1)! LOWER bound" and recorded
a LEAD that qou-im9l being completed might mean it exists. Measured: it does, and
it is not merely the lower bound but the EQUALITY.

  QOU/SchurWeyl/HeckeWedderburnGeneral.lean:77
    theorem finrank_hecke_eq_factorial {K} [Field K] [CharZero K] (q : K)
        (hq0 : q != 0) (hq2 : NotRootOfUnity q) (n : N) :
      Module.finrank K (Hecke K q q^-1 n) = (n + 1).factorial

Sorry-free, measured raw AND code-stripped: 0 sorry, 0 axiom declarations. Its own
docstring explains why the hard half was cheap -- "the lower bound is not proved by
hand here: it is forced by the surjection onto a space of dimension (n+1)!", via
heckeProduct_surjective onto the Wedderburn block product (finrank_blocks_eq_factorial,
which rests on sum_dLambda_sq / RSK-Burnside). So the Groebner-Shirshov route
(qou-auq3) was never on the critical path, and general Hoefsmit was not needed either.

**qou-uoal's closing note is STALE and is what misdirected this bean.** It reads
"Lower bound dim>=(n+1)! needs general Hoefsmit (qou-im9l)". That has been false
since HeckeWedderburnGeneral landed. Anyone reading qou-uoal for the state of the
basis theorem will conclude a build is required when the theorem is on main.

## The frontier, re-scoped -- ONE question, not a theory

No dimension theorem is missing. What is missing is the IDENTIFICATION between the
N-indexed presented tower and the finite Hecke algebras:

  There is a natural algebra map  Hecke K q q^-1 n  ->  HeckeTower R h
  sending sigma_i |-> twGen h i. The relations match exactly:
    - SchurWeyl HeckeRel.quadratic  sigma_i^2 = (q - qi) sigma_i + (q*qi) 1
      is twGen_quad with h = q - q^-1, using q*q^-1 = 1;
    - HeckeRel.braid                matches twGen_braid;
    - HeckeRel.commute (j+2 <= i)   matches twGen_far (k+1 < m).
  Its image is exactly twH n (adjoin of the first n generators).

  **OPEN: is that map INJECTIVE?**

If yes, then dim (twH n) = n! < (n+1)! = dim (twH (n+1)) by finrank_hecke_eq_factorial,
and twH n < twH (n+1) follows immediately for every n -- the whole of this bean,
discharged. If no, the presented N-tower is NOT the colimit of the finite ones and
that is itself a significant (and surprising) finding worth recording.

This is the classical embedding H_n -> H_infinity. It is one well-posed statement
about one map, not a program. Note the scope it carries: finrank_hecke_eq_factorial
needs [Field K] [CharZero K], q != 0 and NotRootOfUnity q, so any strict-growth
theorem derived this way inherits the GENERIC-q hypothesis and is not available over
a bare CommRing. State that, do not gloss it.

Do NOT re-attempt the tail-to-scalars route: it is refuted, and the refutation is now
a theorem on main (scalar_tail_forces_central + tail_scalar_is_automatically_a_unit,
#7231 / #7238), covering every tail assignment rather than the invertible ones.


**Method caveat on the re-scope above, added the same hour -- read before starting.**

The re-scope calls the injectivity of Hecke K q q^-1 n -> HeckeTower R h "one
well-posed statement, not a program". The STATEMENT is well-posed. The METHOD is
not obvious, and this bean has already over-narrowed once today, so state the
difficulty rather than discovering it.

The tempting route is a RETRACTION: build psi : HeckeTower R h -> Hecke K q q^-1 n
with psi . phi_n = id, which gives injectivity of phi_n immediately. But psi is an
algebra map OUT of a PRESENTED tower, so it must assign EVERY generator g m,
m in N, to an element of the finite H_n(q), satisfying quad + braid + far
throughout, with g m |-> sigma_m for m < n. The two obvious tail assignments are
both dead:

  * tail |-> a central scalar -- refuted by scalar_tail_forces_central, together
    with tail_scalar_is_automatically_a_unit (this bean's own theorems, merged in
    #7231 / #7238). They cover EVERY scalar, not just the invertible ones.
  * tail |-> sigma_{n-1} -- dies at far(m, n-2), which for m >= n demands
    sigma_{n-1} sigma_{n-2} = sigma_{n-2} sigma_{n-1}. False: adjacent generators
    do not commute.

So the obstruction this bean proved for the SEPARATOR route obstructs the
RETRACTION route too. That is a recurring structural feature of the presented
N-tower -- the infinite tail has to go somewhere and the relations constrain it
hard -- not a coincidence of one attempt. Whether ANY tail assignment into a
finite H_n exists is OPEN and is worth settling first, because a NEGATIVE there
would be informative: it would say the presented N-tower admits no algebra
retraction onto its finite stages, and injectivity must then come from a basis.

The classical route does not use a retraction at all: it uses the T_w basis of
H_infinity over the Coxeter group S_infinity, which for this carrier means
establishing a basis for the PRESENTED N-tower -- the analogue of qou-uoal's
spanning argument plus the Wedderburn lower bound, at S_infinity rather than S_n.
That is a build, and should be scoped as one.
