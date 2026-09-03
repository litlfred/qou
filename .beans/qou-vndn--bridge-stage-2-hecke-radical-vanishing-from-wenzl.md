---
# qou-vndn
title: 'Bridge stage 2: Hecke radical vanishing from Wenzl criterion (repo Hecke infra; multi-session)'
status: scrapped
type: task
priority: normal
created_at: 2026-07-19T01:32:15Z
updated_at: 2026-08-26T17:57:25Z
---

## REFUTED AS STATED, at the canonical convention (measured 2026-08-26)

This bean asks for "Hecke radical vanishing". **The radical does not vanish on
H_n(q) under convention D.** It is the Temperley-Lieb ideal. So the target as
worded cannot be reached, and an agent picking this bean up cold would spend a
tranche proving something false.

Scope **(b) structural exclusion**, per AGENTS.md's refutation rule -- not a
scope-(a) "this construction alone did not work". The invariant is proved, and
det G = 0 is EXACT, not small:

1. `QOU.QBeta.TemperleyLiebTower.conventionD_kills_antisymmetriser` -- the
   convention-D pin z(q^2+1) = q^3 forces the antisymmetric Wedderburn weight
   y_(1^3) = 0.
2. `QOU.QBeta.MarkovGramDegenerate.block_mem_radical` -- a zero-weight block
   lies in the radical of the trace form. (Depends on NO axioms.)
3. `QOU.QBeta.MarkovGramDegenerate.gram_det_eq_zero_of_radical_combination` --
   hence a nonzero vector in ker G, hence det G = 0.

All sorry-free; axioms clean ([propext, Classical.choice, Quot.sound] or none).

## Independent confirmation, and the detail worth keeping

`content/quantum-observable-universe/nuclear-interactions/gram-matrix-h3-symbolic.md`
gives the n=3 determinant on the 6-element GS basis in closed form:

  det G = -(z-q)^5 (qz+1)^5 ((q^2+1)z - q^3) (q^3 z + qz + 1) / q^8

Re-derived symbolically here (sympy, exact -- no float64): at
z_D = q^3/(q^2+1) the value is **0 identically in q**, and at
z_C = sqrt(q)/(q+1) it is a nonzero rational function.

**The third factor IS the convention-D pin rearranged.** `(q^2+1)z - q^3 = 0`
and `z = q^3/(q^2+1)` are the same equation. So the convention ruling of
2026-08-15 did not perturb this determinant -- it selected precisely the root
of it. Under C the antisymmetric weight is 0.0227449..., small but nonzero and
G invertible; under D it is 0, full stop. A G^-1 computed under C is not an
approximation to one under D, because the latter does not exist.

## Where the live claim goes

`H_n / rad tau = TL_n(delta)`, and the pairing is nondegenerate there:
`pairing_descends` + `mem_radical_of_pairing_zero`, both already proved. This
matches prop:markov-trace-frobenius-selection (iii): (TL_n, tr_M), not
(H_n, tr_M), is the symmetric Frobenius algebra.

## Consequence for the WenzlTowerStep work (PR #5842)

That PR discharges `WenzlTowerStep` at general rank for the REGULAR trace, and
records the Markov-trace version as "still open". That is understated in the
wrong direction: on H_n the Markov version is not merely unproved, it is
**false**, so the field can never be discharged there. The constructive
continuation is the same class over the quotient TL_n -- which is real work,
not a rename, since the tower inclusion and the presentation both have to be
restated for the quotient.

## How this was found

By running the corpus grep this bean's sibling (qou-kzjl) skipped: `grep -rli
"gram determinant|schur element|markov.*nondegener" content/` returns
gram-matrix-h3-symbolic.md in the first ten hits, and the Lean grep returns
GramNondegenerate / RegTraceGram / HeckeGramFactorial / MarkovGramDegenerate.
The answer was four greps away the whole time.


## Superseded by qou-s7z2

The live route is `WenzlTowerStep` at the Markov trace over the TL_n quotient.
Status set to scrapped rather than todo: this bean's title asks for something
false at the canonical convention, and leaving it actionable sends the next
agent at a refuted target.
