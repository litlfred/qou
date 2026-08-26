---
# qou-s7z2
title: WenzlTowerStep at the Markov trace over the TL_n quotient (successor to the refuted qou-vndn)
status: todo
type: task
created_at: 2026-08-26T17:57:00Z
updated_at: 2026-08-26T17:57:00Z
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
