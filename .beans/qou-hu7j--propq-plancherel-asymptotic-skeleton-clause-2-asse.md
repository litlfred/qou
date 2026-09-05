---
# qou-hu7j
title: 'prop:q-plancherel-asymptotic-skeleton clause 2 asserts feray2010 ''holds'' but that theorem has TWO hypotheses the corpus does not meet: measure is M_{n,q} not dim_q^2/[n]_q!, and ''Suppose q < 1'' while substrate q0 = 1.11 > 1'
status: completed
type: task
priority: normal
created_at: 2026-09-05T05:57:12Z
updated_at: 2026-09-05T06:05:12Z
---

DONE 2026-09-05. Clause 2 re-scoped in the .md from 'holds' to 'holds for
M_{n,q}; transfer to w_lambda^(n)(q) unestablished', with the measurement.

VERIFIED MYSELF (50 dps, substrate q0), not taken from the survey:
  sum_lambda M_{n,q} = 1.0 EXACTLY at n = 3,4,5,6,9,12
  sum_lambda w_lambda = 0.9874/0.9822/0.9822/0.9911/1.1109/1.5171
  per-partition max rel difference = 0.158/0.320/0.575/0.951/3.53/12.6
So they are not one normalization apart -- at n=12 they differ by >10x on
some lambda. They coincide only at q=1, which is why clause 1 (q=1,
vershik-kerov) is untouched and clause 2 ('at generic q') is not.

CORRECTED MY OWN FRAMING: I initially flagged the paper's 'Suppose q < 1'
as a second hypothesis failure against the substrate q0 = 1.11 > 1. It is
NOT a blocker -- sec-002-12-results.md:47 records 'in the case q > 1, our
result gives the asymptotic behavior of the columns', so q>1 costs an
orientation (rows <-> columns), not the theorem. The measure mismatch is
the real defect and is the only one asserted.

The Lean sibling was already honest (the bound is a class-field input
under the 3b-cond conditional pattern, cited as external); only the .md
asserted it flatly. Not changed.

NOT closed by this: whether Feray-Meliot Thm 1.1's hypothesis class is
broad enough to cover w_lambda^(n) anyway. That is the one check that
would restore 'holds' and it is named in the block.
