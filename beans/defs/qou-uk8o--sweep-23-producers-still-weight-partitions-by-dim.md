---
# qou-uk8o
title: 'Sweep: 23 producers still weight partitions by dim_q^2/[n]_q!; triage by CROSS-ATOM exposure (c_n cancels within one n)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T05:55:41Z
updated_at: 2026-10-04T15:14:02Z
parent: qou-10v9
---

## Sweep complete (2026-09-05)

Audit: docs/audits/2026-09-05-plancherel-weight-sweep.md

**22 producers** (not 23). **8 fixed**, **3 affected-but-deliberately-unchanged**,
**10 unaffected**, **1 excluded by design**.

**The triage rule in this bean's title needed correcting.** "c_n cancels at
fixed n" is right about the cross-n case and wrong as a sufficient condition.
It cancels iff the reported quantity is a RATIO OF TWO w-WEIGHTED SUMS at the
same n. It also fails to cancel when a w-weighted quantity at ONE n is compared
against something not w-weighted — an experimental magnitude, a closed-form
scalar, a y_lambda-weighted object. Two of the eight fixes
(`deuteron_fpn_wlambda_wiring`, `yekutieli_volume_join`) are fixed-n and were
exposed that way; a fixed-n screen waves them through.

**Do not reuse the audit's c_n.** The two log-delta producers bind `dim_q` to
the chi witness's classical f^lambda, so their normalizer is n!/[n]_q! =
0.980/0.858/0.612/0.326 at n=3/6/9/12 — 3.0x spread, DECREASING in n, against
the audit's 0.987/0.991/1.111/1.517, increasing. Measure per producer.

**Conclusions that moved:** the log-delta pair's 9.35x cross-atom "variance" was
a partial cancellation between two errors; self-normalized, T/3He/4He agree to
1.10x and the whole spread is the deuteron, whose SIGN defect (B_pred < 0) also
disappears. The growth-bound probe's q0-vs-q=1 check is STRENGTHENED (21% gap ->
1.1%). No verdict string changed anywhere.

**Not fixed, with reasons:** alpha_5_jucys_murphy_central (482% spread against a
10% threshold, and it already carries a c_n-free stratum-self-normalized
control); sigma_shell_characterization (the normalizer needs p(60)=966467 and
p(84)=26.5M partitions — NOT computable; this is a live unclosed exposure);
atom_level_wedderburn_tower (retired by the owner ruling of 2026-08-15, its own
witness carries the deprecation block).

**Side finding worth promoting:** the corpus already PROVES the leading
n-dependence of c_n. `QOU/BraidKnot/WLambdaDefectClosedForm.lean` (sorry-free)
gives 1 - Z(n) = C(n)h^2 + O(h^4), C(n) = -n(n-1)(2n-13)/144, which reproduces
the measured c_n to 4 significant figures at n = 2..9 AND predicts the sign
change (2n-13 crosses zero at n=6.5; c_n crosses 1 between n=6 and n=7). The
2026-09-04 audit and the trace-convention registry both describe c_n's growth
as unexplained without citing it.

**Second-order finding:** `wlambda_identity_i_structure_probe` was already
recording `Sum d_q^2 = [n]_q!` as FAILING while its docstring, witness
description and Lean-infra verdict all said "verified". Prose corrected; the
assertion is left EXPECTED-TRUE/measured-FALSE on purpose (it is the corpus's
own detector). Re-measured symbolically in the process: the identity is false in
sympy exactly, not merely numerically — the n=2 ratio is 2q/(q^2+1). That is
stronger evidence than the upstream numerical table and is independent of it.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- **Round 55 Progress (`2026-11-16T21:09:27Z`)**: Opened [`litlfred/qou#8202`](https://github.com/litlfred/qou/pull/8202) (`61d4706edbc97c195108082e38b072c982ba2984`, Commit 1 `842a8da69cdb997861cc48f6f16593cc33e1e707`). Keeping bean at `status: in-progress` pending owner review.
