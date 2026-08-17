---
# qou-ls86
title: 'Many-body collective term R: strictly positive and bounded on the well-bound regime'
status: in-progress
type: task
priority: normal
created_at: 2026-08-17T00:44:48Z
updated_at: 2026-08-17T01:40:08Z
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


## 2026-08-17 — R is extensive at leading order; the count is DEGENERATE; R is not one term

Ran the structural test the confirmed step-7 functional poses. Since S = -sum log
mu is the archimedean functor (settled in qou-y0mc), any additive collective term
must itself be a sum of log-suppressions over some structure, so
T := R*A/alpha should be proportional to that structure's COUNT. One free
parameter (overall scale), not a fit.

**1. Scaling.** Over 3519 well-bound nuclides: C(A,2) all-pairs excluded at 110%
spread (this UPGRADES the existing scaling screen from the A>=24 band to the whole
chart); pure surface A^(2/3) excluded at 17.4%. Everything linear in A sits at
9.7-9.9%.

**2. THE COUNT IS DEGENERATE — the important negative.** The six 'good' rows
differ by 0.2pp. Rescaled to the A column at A=100 they all collapse to ~1.207:
A-1 -> 1.2075, A-2 -> 1.2094, A -> 1.2062, 3A -> 1.2062, 3A-1 -> 1.2066,
blocks -> 1.2077. They are ONE fit in different units. Reporting 'A-1 is tightest
at 9.7%' as an identification would be over-reading. The test constrains the
SCALING (extensive), NOT the structure.

Discriminating among linear counts needs the O(1) offset — i.e. the light nuclei —
which are exactly the rows contaminated by the two-nucleon defect. That is a real
obstruction, not a gap in the probe.

**3. The 10% residual is not noise, and correlation cannot identify it.**
Residual range [-70.69, +15.64] alpha, sd 17.70, against a leading term of 252.5
alpha at A=208. Extremes are physically identified: most POSITIVE at A=90 Z=40
(N=50, a shell closure); most NEGATIVE at A=295 Z=118 (the superheavy Coulomb
limit). But the liquid-drop correlations are Coulomb +0.827, surface +0.702,
asymmetry +0.689, volume -0.767 — all strong, because all are monotone in A and
mutually collinear. Same failure mode as the count degeneracy; a single Pearson r
is not an identification.

**Framing conclusion: 'find the missing collective term' is the WRONG FRAMING.**
R is at least three things: (1) an extensive piece ~1.207 alpha/nucleon,
scaling-identified but structure-degenerate; (2) shell structure; (3) a large
negative high-Z piece consistent with Coulomb, which the framework does not model
AT ALL. Only (1) is plausibly categorical. A search treating R as one object is
looking for something that is not there.

Scope-(a) throughout. Established: leading behaviour is extensive; all-pairs and
pure-surface excluded. NOT established: which extensive count, the residual's
decomposition, or that a categorical object supplies (1).

Probe: computations/probes/collective_term_shape_degeneracy_probe.py
