---
# qou-lnog
title: Drain the a_m-differencing defect from the Q_beta Habiro-element cluster
status: completed
type: task
priority: normal
created_at: 2026-08-18T21:53:54Z
updated_at: 2026-08-18T23:33:38Z
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


## 2026-08-18 RESOLVED — and the framing in this bean's original body was wrong

This bean was opened saying the cluster "published refutations computed on the
wrong object". That was measured against the CURRENT convention-D atomic
witness; the three witnesses date 2026-06-02 / 2026-07-07, in the C era.
Recovered the C-era denominators from cf5318a97b:

    n - p      4u^19(u^2+1) vs 4u^19(u^2+1)        IDENTICAL -> VALID
    D - n      32u^40(u^2+1)^3 vs 4u^19(u^2+1)     differ    -> invalid
    3He - D    64u^55(u^2+1)^5 vs 32u^40(u^2+1)^3  differ    -> invalid
    4He - 3He  256u^76(u^2+1)^7 vs 64u^55(u^2+1)^5 differ    -> invalid

The n-p element WAS computed on the right object. Only the atomic-STEP legs
were ever invalid. Under D, n-p needs the fix too (p/n diverged 2026-08-15).

No published conclusion moves. The SPECIFIC verdict rested entirely on the two
broken legs and is CONFIRMED on the correct object:

    n - p     {P1,P2,P4,P16}  Phi_1*Phi_2 PRESENT
    D - n     {}              absent
    3He - D   {P8^3}          absent
    4He - 3He {P4^2,P8^4}     absent

and now has a structural reason: mirror_traceDiff_eq_zero_of_tau_eq -- Phi_1
divides a difference exactly where the traces coincide at q=1, true for the
mirror pair and for none of the atomic-number jumps. C6 also survives.

## Delivered

Added `require_am_differenceable` / `am_difference_is_valid` /
`AmDifferenceInvalid` to habiro_coefficients_atomic, and wired all five scripts
to call it as a preflight. Verified by RUNNING them, not by inspection. They now
fail loudly under D instead of emitting a plausible wrong polynomial.

Deliberately did NOT rewrite the five scripts: the conclusions stand, so a port
would be churn. What remains open is only the D port itself (expand
trace_diff_numerator instead of differencing two expansions) if anyone needs
D-frame numbers from these producers.

Key generalisable lesson: whether a_m-differencing is valid is a property of the
CONVENTION, not the code. The same script is correct under C and wrong under D
with no edit between. That is why the check has to run, not be documented.
