---
# qou-kwoa
title: 'Lean/Mathlib-scale: Hecke character theory for det(twGram) at rank >= 2 (Geck-Pfeiffer 7.2.6)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-02T21:39:20Z
updated_at: 2026-09-02T22:29:28Z
---

Successor to qou-0y6h, split out on owner instruction 2026-09-02 because that
bean's title reads as though a lemma is missing when the remainder is a
book-length development. qou-0y6h is CLOSED at what is proved; this carries the
rest.

## The single deliverable

  det (QOU.Hecke.TwBasis.twGram K q n) != 0  for n >= 2, in Lean.

Everything downstream of it already exists and is sorry-free on main:
isSemisimpleRing_of_twGram_det_ne_zero gives semisimplicity of H_n(q) at every
rank from that one input.

## What is already supplied — do NOT re-derive any of it

* THE BASIS. basisTwOfField, a Module.Basis indexed by Equiv.Perm (Fin (n+1))
  whose vectors are the T_w, with finrank_eq_factorial. Reached WITHOUT
  Matsumoto (still a Mathlib TODO at Coxeter/Basic.lean:78).
* THE MULTIPLICATION TABLE. TwMul.σ_mul_Tw, both branches. Handedness is
  T_v . T_w = T_{wv} (right factor acts first); it is documented, not a typo.
* THE GENERATOR TRACE. TwTrace.trace_lmul_σ and two_mul_trace_lmul_σ.
* THE RANK-ONE CASE, END TO END. twGram_det_rank_one = (1+q)^2 and
  isSemisimpleRing_rank_one, unconditional, no cited class.
* THE TARGET VALUES at n = 1,2,3, exactly, with the integer constant identified
  as prod_lambda d_lambda^(d_lambda^2) — computations/hecke/
  tw_gram_determinant_probe.py, n=3 verified as a POLYNOMIAL IDENTITY (degree
  bound 216, candidate 122, 298 points).
* THE CHARACTERS, SYMBOLICALLY, AT GENERAL n. This is the part that makes this
  bean tractable and it is easy to miss: qou-avt2 (in-progress, Halverson-Ram /
  Jing-Liu) put exact symbolic chi_lambda into
  computations/hecke/hecke_characters.chi_lambda_braid(precision='symbolic_q').

## The identity that ties them together — MEASURED, not assumed

computations/hecke/tw_trace_equals_character_sum_probe.py:

    tr(L_{T_u}) = sum_lambda d_lambda chi_lambda(T_u)

verified for every element of S_3 as exact rational functions, computing the two
sides by wholly independent routes (the T_w multiplication rule, which knows
nothing about Young tableaux, against the Hoefsmit seminormal engine, which
knows nothing about T_w).

CONVENTION BRIDGE, and the identity is FALSE without it:

    QOU.Hecke.IwahoriHecke / the T_w side :  sigma^2 = (Q - 1) sigma + Q
    hecke_characters (seminormal)         :  sigma^2 = (q - 1/q) sigma + 1
    =>  Q = q^2   and   sigma_mine = q sigma_theirs
    =>  tr_mine(L_{T_u}) = q^length(u) * sum_lambda d_lambda chi_lambda(word)

The engine wants a SIGNED, 1-BASED braid word: [(1, i+1), ...].

So the COMPUTE side of the blocker is solved at every rank. What is missing is
the LEAN formalisation of the character theory — the discovery is done.

## Two bounds on this bean, both measured, both permanent

1. THE ROUTE IS ONE-DIRECTIONAL. det(twGram) carries the integer constant
   prod_lambda d_lambda^(d_lambda^2), so in a characteristic dividing it the
   determinant VANISHES even where H_n(q) is semisimple (the regular trace form
   of M_d(K) is degenerate exactly when char K | d). det != 0 => semisimple is
   all this can ever give; the converse is FALSE, counterexample char 2 with q
   of order > 3 at n = 2. Any general theorem here MUST carry a characteristic
   hypothesis, which QGeneric q n does not supply. Costs nothing for the
   substrate (K = R, q > 1). Audit: docs/audits/
   2026-08-30-tw-gram-determinant-measured.md.
2. NO COMBINATORIAL SHORTCUT EXISTS. tr(L_{T_u}) is determined by NONE of
   length(u), cycleType(u), or the pair. Witness in S_5, same length 4 and same
   cycle type (2,2,1): u=(0,3,4,1,2) gives 5(q-1)^2(q^2+4q+1); u=(1,0,4,3,2)
   gives 10(q-1)^2(q^2+q+1). Exact finite computation => refutation with a
   witness. Audit: docs/audits/2026-09-02-tw-regular-trace-not-combinatorial.md.

## TRAP — read before claiming any new pattern here

S_2 satisfies all three of those statistics, S_3 two, S_4 the joint one, S_5
none. I generalised from S_3, then from S_4, and was wrong both times; each
reading was consistent with every datum available when I made it. In this corpus
a Hecke pattern first breaks at n = 4 or n = 5, because that is where S_n first
has two elements of equal length in one conjugacy class. TEST S_5 before
promoting any rank-3 or rank-4 pattern. The probe asserts both halves of the
S_4/S_5 split so a future edit that breaks either fails loudly.

## Scope

Mathlib-scale, multi-session, a research formalisation rather than a proof to be
typed out. Crosses no barrier: semisimplicity is a magnitude-axis fact and
nothing here bears on the P!=NP wall. SchurElementCriterion still has no
instance; both obligations that docs/audits/
2026-08-29-pneqnp-gap-inventory-refresh.md §3b separates (the combinatorial
schurElement equalling the algebra-theoretic one, and GP 7.2.6 proper) remain
open.

## Coordinate

qou-avt2 (in-progress) is the mathematical supplier — cite it, do not duplicate
it. qou-mtx9 records that the GP reduction is the compute bottleneck and scales
with WORD LENGTH, with a batched entry point (chi_lambdas_via_gp) unused in 9
producers; relevant if this bean's verification ever needs characters in bulk.


## Claimed 2026-09-02 by branch claude/p-neq-np-gaps-n8dxxl

First move is a SCOPING CHECK, not construction: is the character-sum route
this bean prescribes circular for the semisimplicity goal? See the entry below.

## 2026-09-02 — SUPERSEDED IN ITS CONCLUSION. Semisimplicity at every rank is DONE.

The bean asked for Geck-Pfeiffer character theory because det(twGram) at rank
>= 2 needs tr(L_{T_u}) for general u. That is still true and still Mathlib-scale.
But the CONCLUSION the determinant route was chasing — semisimplicity of the
Hecke algebra at every rank — did not need it, and was reachable by composing
four things that already existed in the corpus and had never been put together.

QOU/SchurWeyl/HeckeSemisimpleGeneral.lean (new, sorry-free, #print axioms clean
on all four declarations):

  isSemisimpleRing_hecke              q != 0, q^2 != 1  =>  IsSemisimpleRing (Hecke R q q^-1 n)
  isSemisimpleRing_hecke_of_one_lt    1 < q             =>  same, at every n
  wenzlCriterion_of_one_lt            a MODEL for the cited WenzlCriterion
  semisimple_of_one_lt_unconditional  the composition, no cited class left

### The four pieces, all pre-existing

* QOU.SchurWeyl.heckeWedderburn (SW-7): H_{n+1}(q) = prod_lambda M_{d_lambda}(R)
  at EVERY n. I verified the whole chain sorry-free: rskBurnsideHolds
  (sum d^2 = n! from Robinson-Schensted), heckeProduct_surjective, the
  dimension squeeze, heckeProduct_bijective, heckeWedderburn.
* QOU.MathlibExt.MatrixSemisimple.instIsSemisimpleRing_matrix — fills Mathlib's
  proof_wanted IsSemisimpleRing.matrix for division rings.
* Mathlib's finite-product IsSemisimpleRing instance.
* Mathlib's RingEquiv.isSemisimpleRing.

### What this discharges

WenzlCriterion (Information/PNeqNpEquivalence.lean) calls itself a "hypothesis
class, not a theorem of this development" and had NO INSTANCE anywhere in the
corpus. Every consumer of semisimple_of_one_lt was therefore conditional on an
assumption with no known model. It has one now.

NOT an instance, deliberately: a blanket instance over all q would be FALSE as
the class is stated, since WenzlGeneric 0 n holds vacuously (0^k = 0 != 1)
while q = 0 is degenerate. Hence a theorem taking 1 < q.

### What is NOT superseded — the bean stays open for this

* CARRIER. This is QOU.SchurWeyl.Hecke R q q^-1 n, NOT QOU.Hecke.IwahoriHecke
  K q n. Different RingQuots of different relations; bridging them is qou-img9.
  The T_w route remains the only one that reaches IwahoriHecke itself, so
  twGram is NOT retired.
* FIELD. R only. The genericity hypotheses are exactly right over the reals
  (q != 0 and q^2 != 1 force [k]_q != 0 for every k there) and would be wrong
  over a general field, where a root-of-unity hypothesis is needed.
* det(twGram) at rank >= 2 is still open and still Mathlib-scale. What changed
  is that it is no longer the only road to the conclusion — so pursue it for
  the IwahoriHecke carrier and for the determinant value, not because
  semisimplicity depends on it.

### Method note worth keeping

This is the corpus-grep discipline paying at maximum value: a bean scoped as
multi-session research collapsed to one composition file because the pre-build
check found the conclusion already reachable. Run the checklist BEFORE building.

### Tooling trap, recorded because it cost a repair

`beans update --body-append "..."` with a DOUBLE-QUOTED shell argument lets the
shell expand backticks as command substitution. Backticked identifiers were
executed ("proof_wanted: command not found") and their text was DELETED from
the bean, silently truncating the rest of the append. Pass long bodies through
a file, or single-quote the argument.

## 2026-09-03 — the CARRIER item is now CLOSED (qou-img9 / PR follow-on)

One of this bean's three remaining items is done. QOU/SchurWeyl/HeckeCarrierEquiv.lean:

  isSemisimpleRing_iwahoriHecke : 1 < Q -> IsSemisimpleRing (QOU.Hecke.IwahoriHecke R Q n)

at EVERY rank, sorry-free. That is the T_w / twGram carrier, which this bean recorded as
NOT reached by HeckeSemisimpleGeneral.

Mechanism: the two RingQuot relations differ in exactly one clause (the quadratic); braid
and far-commutation are verbatim identical on the same FreeAlgebra. A generator rescaling
sigma |-> c . T moves the quadratic under c(Q-1) = q - qi and c^2 Q = q qi, satisfied
identically by Q = q^2, c = q^-1 at qi = q^-1. Upgraded to an AlgEquiv of carriers, which
is what transports IsSemisimpleRing.

### Remaining items on this bean, now TWO not three

* GENERAL FIELD. Everything is over R, inherited from heckeWedderburn (SW-7), which is an
  R-only construction. carrierEquiv itself is over a CommRing and skeinIwahoriEquiv over
  any Field, so the restriction is upstream, not here.
* det(twGram) AT RANK >= 2 ITSELF. Still Mathlib-scale, still open, and still worth doing
  for the DETERMINANT VALUE — but no longer for the semisimplicity conclusion, which now
  has two independent routes to it. tr(L_{T_u}) is not combinatorial (refuted with an S_5
  witness, #6417); the closed form is Geck-Pfeiffer.

### Note for whoever reads twGram next

isSemisimpleRing_rank_one (#6134) proves semisimplicity of IwahoriHecke at n = 1 over ANY
field with 1 + q != 0, via the determinant. isSemisimpleRing_iwahoriHecke proves it at
EVERY n over R with Q > 1, via Wedderburn. Neither subsumes the other: one is general in
the field, the other general in the rank.
