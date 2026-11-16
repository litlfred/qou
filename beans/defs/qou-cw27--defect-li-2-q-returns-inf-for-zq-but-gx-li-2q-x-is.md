---
# qou-cw27
title: 'DEFECT: li_2_q returns inf for |z|>=q, but g(x)=-Li_2^q(-x) is finite for ALL x>0 -- ''atom-word tower diverges'' is false as stated'
status: in-progress
pr: 8208
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T22:45:51Z
updated_at: 2026-10-04T15:18:40Z
parent: qou-r9ih
---


Branch: claude/anchor-followups-2026-08-08. Full write-up:
docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md §8.

`_li_2_q_util.li_2_q` sums Li_2^q(z) = SUM_n z^n/(n [n]_q), radius |z| < q, and
HARD-RETURNS mp.mpf('inf') when |z| >= q. That guard -- not the function -- is
what makes the atom-word brane tower "diverge for Z >= 2"
(`borromean_binding_recompute` docstring; the dashboard's m_can0 note repeats it).

CLOSED FORM. With [n]_q = (q^n - q^-n)/h,

    z^n/(n [n]_q) = (h/n) * SUM_{m>=0} (z q^{-1-2m})^n
  =>  Li_2^q(z) = -h * SUM_{m>=0} ln(1 - z q^{-1-2m})

a q-product convergent off the poles {q^{1+2m}}, and it IS the analytic
continuation. Verified against the series to 1.2e-45 at z in {-1, -0.5, 0.5,
0.9, 1.05}, and finite where the guard returns inf:
  z = -2 -> -1.43814272667888284
  z = -5 -> -2.75275536231868014

WHY IT MATTERS. The tower only evaluates g(x) = -Li_2^q(-x) at x > 0, where
every product factor is 1 + x q^{-1-2m} > 0. So g is real and finite for ALL
x > 0 -- there is no singularity anywhere on the path the tower takes. Only one
argument even crosses the radius: tau_p^2 = 1.13488 vs q = 1.10998, over by 2.2%.

NOT A BOREL PROBLEM. Ratio test gives |a_(n+1)/a_n| -> |z|/q, a GEOMETRIC
divergence (measured 0.9053 at n=10, 1.0024 at n=50, 1.0173 at n=200, limit
1.022432). Borel resummation targets factorial growth; on a geometric series it
reproduces the same singularity. Analytic continuation is the right tool and the
q-product above is it in closed form.

ATOM-WORD TOWER WITH THE CONTINUED g:

    atom     1-body     2-body    B_tower     B_AME     err %
    2H     2.061309  0.3863699   2.447679   2.224566    +10.03
    3H     3.250086  1.2786696   4.528756   8.481798    -46.61
    3He    3.292395  1.2036063   4.496002   7.718043    -41.75
    4He    3.756166  2.4822759   6.238442  28.295673    -77.95
    6Li    3.940721  6.2877182  10.228440  31.994564    -68.03
    7Li    3.665575  8.9646174  12.630193  39.244524    -67.82

2H at +10.03% is the best deuteron any route in the framework produces. The rest
is worse than Borromean, so this does NOT replace it -- but the stated reason for
preferring Borromean ("the atom-word tower diverges") is false as written and
should be restated as a magnitude/accuracy argument or dropped.

FIX (not applied here -- wave 3 is running, and li_2_q has many consumers):
  1. add the product-form branch to `li_2_q` for |z| >= q instead of returning
     inf, or expose it as `li_2_q_continued`;
  2. keep a guard only for the genuine poles z = q^{1+2m}, z > 0;
  3. repoint the two docstrings that assert divergence
     (`borromean_binding_recompute`, `mass_binding_dashboard` m_can0 note).
Auditing every current consumer of the inf return is part of the fix -- some may
be relying on inf as a sentinel.

FORMALIZABLE: yes. The product identity is Fubini on a doubly-indexed absolutely
convergent sum; finiteness for x > 0 is positivity of each factor. Neither needs
the Markov axiom the rest of the binding work is conditional on.

## Progress Note (2026-11-16, PR #8208)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/QuantumDilogContinuationAndKVCTower.lean` (wired into `QOU.lean`, `0` `sorry`, `0` `axiom`, `0 CRITICAL / 0 advisory` across all 8 Lean static vacuity/borrowed-name audits).
- Verified by 80-dps `mpmath` / exact rational probe `computations/probes/quantum_dilog_continuation_and_kvc_tower_probe.py` and witness `computations/probes/quantum-dilog-continuation-and-kvc-tower.witness.json` (`scriptCommitSha: c308a076161bc1c0a1b46834008400b1576dfd38`, `allPassed: true`, `0` raw `float64` fields).
- PR: https://github.com/litlfred/qou/pull/8208 (`64261818e4f35a4581697173acc357da9b7b92f8`).
