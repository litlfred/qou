---
# qou-lnog
title: Drain the a_m-differencing defect from the Q_beta Habiro-element cluster
status: in-progress
type: task
priority: normal
created_at: 2026-08-18T21:53:54Z
updated_at: 2026-08-18T23:16:02Z
---

## Scope

Five scripts form the "Q_beta-relevant Habiro element" as `Da_m := a_m(n) - a_m(p)`
(or `a_m(D) - a_m(n)`), which is the qou-0ndb defect: a witness's `a_m` expand its
own denominator-cleared numerator `p = d*t`, so the coefficient difference is
`d_X*t_X - d_Y*t_Y`, not the pair difference.

    qbeta/qbeta_habiro_delta_am_factorization.py     publishes a witness
    qbeta/qbeta_habiro_cross_pair_factorization.py   publishes a witness
    probes/qbeta_habiro_element_probe.py             publishes a witness
    qbeta/qbeta_habiro_delta_a_m_pattern_probe.py    reads only
    qbeta/qbeta_habiro_phase5q_dn_refactorize.py     reads only

The fix is mechanical: `habiro_coefficients_atomic.trace_diff_numerator(tr_x,
tr_y, sym)` takes the two `tr_M_in_q` strings directly and is convention-agnostic.
Then Habiro-expand the difference (`cyclotomic_expansion`) and analyse THOSE
coefficients, rather than differencing two expansions.

## Why this was left as a separate tranche, not folded into the qou-0ndb PR

Measured for n-p, the two objects are not close:

                       Sum Da_m (u;u)_m      numerator of t_n - t_p
    degree             44                    54
    cyclotomic         {P3, P6, P12}         {P1, P2, P4, P16}
    integer content    1                     4

Disjoint factor sets, not proportional. The correct object is divisible by P1 --
it must be, since the two traces coincide at q=1 -- and the computed one is not.

BUT all three published witnesses record NEGATIVE / PARTIAL verdicts. So unlike
the mass-table summary (which published a wrong positive-looking `phi_8_mult: 0`),
this cluster published REFUTATIONS computed on the wrong object. That is the
over-narrowing failure mode of AGENTS.md "Before declaring refuted", and it needs
a careful per-claim re-measurement rather than a sweep.

First re-measurement is already done and is a caution against assuming the
negatives flip: the headline negative of `qbeta-habiro-delta-am-factorization`
-- "no single polynomial factor unites all m; the C6 conjecture is FALSIFIED" --
SURVIVES on the correct object (the gcd across the corrected Da_m is the constant
4, not a polynomial). What changes is the published `integer_content_gcd: 1`,
which is 4, and the support, which moves m=0..8 -> m=1..9.

So: do NOT re-open the C6 falsification on the strength of the defect alone.
Re-measure each published claim individually.

## Next step

1. Patch the five scripts to `trace_diff_numerator` + `cyclotomic_expansion`.
2. Regenerate the three witnesses.
3. Diff each verdict field old-vs-new and record which claims move.
4. If any NEGATIVE flips, that is a real result -- an ingredient that was
   excluded on a normalisation artifact.

Ref: docs/audits/2026-08-18-mirror-pair-a-m-differencing-normalisation-defect.md
Parent: qou-0ndb
