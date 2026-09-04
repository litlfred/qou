---
# qou-7o7h
title: 'Register the balanced-convention Plancherel gap: dim_q^2/[n]_q! is not a probability measure (c_n up to 1.517 at H_12); re-read the k3-test 1.82x/1.55x figures against it'
status: completed
type: task
priority: normal
created_at: 2026-09-03T20:39:57Z
updated_at: 2026-09-04T02:32:07Z
---

## DONE 2026-09-04

Registered in the trace-convention registry (both twins: row B carries a
normalization_gap block in the JSON; the MD gains section B-norm), with a
producer + witness + audit doc.

MEASURED: c_n = Sum_lambda dim_q^2/[n]_q! = 0.99107952 / 1.11092313 / 1.51713321
at n = 6/9/12 (proton pin, 60 dps) -- not a probability measure in the balanced
convention, and GROWING with n.

MECHANISM (this is the part to quote): w_textbook = c_n * w_selfnormalized
exactly (dev < 1e-40), and the depth-stratified functional is linear in the
weights, so B scales by exactly c_n. The factor cancels WITHIN an atom and does
NOT across atoms, since n = 3A differs. Cross-atom metrics are therefore
distorted.

CONSEQUENCE: the FR family's published 1.82x baseline variance is 1.5307x
inflated by normalization alone; self-normalized it is 1.19x. The scaling law
reproduces the recorded textbook run to 5.5e-5 (that residual = the 4-sig-fig
rounding of the recorded ratios). fr_pullback_k3_test.py is on the textbook
side; fr_pullback_borromean_h3a_test.py was migrated 2026-09-03. Figures from
the two are NOT comparable.

TWO TRAPS RECORDED: (1) I first tested the scaling law with the factor inverted
(divided by c_n), got 1.290 vs a recorded 1.8217, and nearly dismissed a real
mechanism as coincidence. (2) The shortcut '1.8217/1.1901 = 1.5307 = c_12/c_6'
is TRUE but CONDITIONAL on the argmax/argmin atoms being the extreme-c_n ones
under both normalizations -- quote the scaling law, not the ratio identity.

NOT RESOLVED (left open, not asserted): whether the k3-test's own conclusions
change under the corrected normalization. That needs the k3-test re-run.
