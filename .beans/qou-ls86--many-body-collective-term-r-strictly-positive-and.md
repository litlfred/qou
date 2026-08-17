---
# qou-ls86
title: 'Many-body collective term R: strictly positive and bounded on the well-bound regime'
status: in-progress
type: task
priority: normal
created_at: 2026-08-17T00:44:48Z
updated_at: 2026-08-17T00:45:33Z
---

Opened working the many-body R term at owner direction ('go on many body').
First action was formalize-first: check what the existing screens rest on before
searching for a candidate. One of the three screens does not survive the check —
and it is one I wrote.

## The sign screen is REGIME-CONFINED, and was over-stated

collective_term_budget_probe (PR #4973) measured on a **14-isotope convenience
sample** and concluded R is 'MIXED-SIGN in A', which 'kills anything manifestly
non-negative by construction — an entropy, a KL divergence, a dimension count, a
sum of squares, a positive Plancherel weight'.

Over the **full AME2020 table** (3554 nuclides, Z>=1, N>=1, B>0):

* **7 rows have R < 0. Every one has B_AME/A < 1.73 MeV/nucleon.**
  5Be 0.0180 | 7H 0.9400 | 6H 0.9616 | 2H 1.1123 | 4Li 1.1538 | 5H 1.3364 |
  4H 1.7204. **Six of seven are particle-UNBOUND** drip-line exotics; the
  seventh is the deuteron, the weakest-bound stable nucleus.
* **Among the 3519 nuclides with B_AME/A > 5 (99.0% of the chart): ZERO
  negatives.** R in [+2.1009, +5.8926] — strictly positive, one-signed, bounded
  within a factor of 2.8.

**The negatives measure a different, already-proved defect.** B_sym with every
L > 0 is positive for every (Z,N), so the framework cannot produce an unbound
nucleus at all (single_crossing_binds; the two-nucleon floor). Exactly where
nature has ~zero binding the chain must over-bind and R < 0. Those rows re-measure
the KNOWN interface defect, not the collective term's sign structure.

**Withdrawn as stated:** 'mixed-sign in A, so non-negative candidates are
excluded.' **Replacement (scope-(a)):** on the well-bound regime R is strictly
positive and bounded in [2.10, 5.89] MeV/nucleon; an entropy / KL divergence /
dimension count / positive Plancherel weight is NOT excluded there. Do not cite
the old screen against them.

## A hypothesis of mine the measurement killed

I expected the negatives to be **2H alone** — R(2H) is by construction the
deuteron's single-bond error, hence contaminated. Wrong: seven rows, six not the
deuteron. The right claim is about the binding REGIME, not one contaminated
point. Recorded because the wrong version was the tidier story and I nearly
wrote it up.

## Where this leaves the search

A strictly-positive bounded target is far better conditioned than a mixed-sign
one. Surviving screens, unaffected:
* magnitude — plateau R/alpha = 1.3240 per nucleon, 1.90x the chain's asymptote;
* scaling — per (A-1) 19.4% spread on A>=24 vs per C(A,2) 184.6% falling
  monotonically, so an unsuppressed all-pairs term stays excluded.

Next honest step is NOT an ansatz: it is to decide whether R should be fitted at
all, or whether the well-bound regime's boundedness is itself derivable from the
step-7 functional (R must be a sum of log-suppressions over some additional
structure, since S = -sum log mu is the confirmed functional — so R's positivity
on the well-bound set says those extra factors are all < 1 there).

Probe: computations/probes/collective_term_sign_screen_regime_confined_probe.py
