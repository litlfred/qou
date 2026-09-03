---
# qou-s7z2
title: WenzlTowerStep at the Markov trace over the TL_n quotient (successor to the refuted qou-vndn)
status: in-progress
type: task
priority: normal
created_at: 2026-08-26T17:57:00Z
updated_at: 2026-08-26T18:55:10Z
---

Successor to qou-vndn, whose premise ("Hecke radical vanishing") is refuted at
convention D: the radical does not vanish on H_n, it IS the TL ideal. See
qou-vndn for the proved invariant and the exact symbolic determinant.

## The target

Discharge `QOU.Machinery.HeckeTower.WenzlTowerStep`'s field at the MARKOV trace
over the quotient TL_n(delta), where the pairing IS nondegenerate:
`QOU.QBeta.MarkovGramDegenerate.pairing_descends` +
`mem_radical_of_pairing_zero`, both already proved.

## Why this is real work and not a rename

Both hypotheses of the class are stated on H_n objects:
- `HeckeBraidedPresentationOfRank q rank Hn1 sigma_n1` -- the braided
  presentation has to be restated for the quotient (the generators descend, but
  that needs saying).
- `iota : Hn ->a[R] Hn1` -- the tower inclusion has to be shown to descend to
  TL_n -> TL_(n+1) compatibly with the radical.

Neither is automatic and neither is currently in the corpus in that form.

## Already available, do not re-derive (this is the qou-kzjl lesson)

- `TraceNilpotent` -> `TraceFormSemisimple` -> `RegTraceGram` ->
  `HeckeGenericSemisimple` -> `HeckeGramFactorial`: the whole abstract ladder
  from a nondegenerate trace form to semisimplicity, sorry-free.
- `QOU.Machinery.HeckeRank.wenzlTowerStep_regTrace` (PR #5842): the class
  discharged at general rank for the REGULAR trace, plus the finding that
  hypothesis 1 (`IsSemisimpleRing Hn`) is not consumed.
- `QOU.QBeta.TemperleyLiebTower`: convention-D weights, radical two-sidedness.

## Open input, unchanged from HeckeGramFactorial's own note

The general determinant value in the n!-dimensional T_w basis -- the classical
Schur-element product formula. n=2 is done
(`QOU.Hecke.H2CompanionRep.h2GramFromRep_det`, det = [2]_q^2). n=3 is computed
symbolically in gram-matrix-h3-symbolic.md but for the MARKOV form, where it is
0 at convention D -- that is the refutation above, not a rung of this ladder.
No fabricated instance may stand in for the general value.


## Brick 1 LANDED (PR #5850, 2026-08-26): the quotient now exists as an object

`QOU/QBeta/MarkovTraceQuotient.lean`, sorry-free, 10 declarations, 3 of them
depending on no axioms at all.

The gap turned out to be more concrete than this bean anticipated. The corpus
says "H_n / rad tau = TL_n(delta)" in several places, but that phrase had NO
OBJECT in Lean: traceRadical is a Set A, and pairing_descends is a congruence
statement, not a descent to a quotient type. Mathlib's TwoSidedIdeal.mk' wants
six fields and the corpus had two -- the three ADDITIVE closures were missing,
because TemperleyLiebTower states the radical for a bare tr : A -> R with only
[Zero R], so there was no addition on the target to close under.

Supplied: the additive closures, traceRadicalIdeal (TwoSidedIdeal), TraceQuot
(the quotient ring), quotTrace (descended; rad is inside ker tau by taking
b = 1, which is where unitality is spent), and quot_pairing_nondegenerate in
exactly WenzlTowerStep.semisimple_ascend's shape.

Non-vacuity guarded (one_not_mem_traceRadical / quot_one_ne_zero /
quot_pairing_one): without them the nondegeneracy would hold trivially on the
zero ring. Base ring [Module R A] not [Algebra R A], per 7c.

## What brick 1 is NOT

It is not WenzlTowerStep discharged at the Markov trace. Still needed, and
neither is automatic:

1. The braided presentation restated for the quotient -- the generators descend,
   but that needs proving, not asserting.
2. The tower inclusion TL_n -> TL_(n+1) shown to descend from H_n -> H_(n+1)
   compatibly with the radical.

Unchanged: HeckeGramFactorial's open input, the general T_w-basis determinant
(the classical Schur-element product formula). n=2 done; no fabricated instance
may stand in for the general value.


## Brick 3 LANDED as PR #5853 (2026-08-26): the tower is INJECTIVE

`QOU/QBeta/TLTowerRadicalDescent.lean`, 4 declarations, sorry-free, axiom-clean.

Set out to prove preservation (iota carries rad tau_n into rad tau_{n+1}) and
got REFLECTION as well, which is worth more:

  iota a in rad(tau_{n+1})  <->  a in rad(tau_n)

Preservation alone gives a map of quotients. Reflection makes it INJECTIVE, so
TL_n embeds in TL_{n+1} rather than merely mapping to it -- i.e. the quotients
are a TOWER, not a sequence of unrelated algebras. Unexpected, and it is the
brick's real content.

Mechanism: a bare inclusion cannot do this, because membership in rad(tau_{n+1})
quantifies over all of H_{n+1}, not over iota's image. The conditional
expectation is what connects them, via the bimodule law at z = 1
(epsilon_inclusion_mul) moving a test element back down. Preservation spends
BIMODULE; reflection spends RETRACT. Both fields of HeckeConditionalExpectation
are load-bearing.

CONDITIONAL (3b-cond): HeckeConditionalExpectation has NO instance. The
implications are proved; the premise is not established.

## Bricks 1-3 status

1. #5850 MERGED -- the quotient exists as an object (TwoSidedIdeal + quotient
   ring + descended trace + nondegeneracy in WenzlTowerStep's shape).
2. #5852 OPEN -- the braided presentation descends (needed an Algebra instance
   Mathlib does not supply; a scalar-action diamond shaped the proof).
3. #5853 OPEN -- the tower inclusion detects the radical exactly; injectivity.

## What is STILL not done

No WenzlTowerStep instance at the Markov trace. Remaining: assemble bricks 2
and 3 into the class. And untouched by all three bricks --
HeckeGramFactorial's own open input, the general T_w-basis determinant (the
classical Schur-element product formula). n=2 done; no fabricated instance may
stand in for the general value.

MERGE NOTE: #5852 and #5853 both anchor guard-registry entries at the same line
and will conflict in scripts/lean-axiom-guard.py. Both sides are pure additions;
keep both.
