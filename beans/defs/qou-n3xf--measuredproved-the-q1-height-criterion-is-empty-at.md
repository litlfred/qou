---
# qou-n3xf
title: 'MEASURED+PROVED: the q=1 height criterion is empty at the critical ratio — bounds the whole height approach'
status: completed
type: task
priority: normal
created_at: 2026-08-29T18:25:10Z
updated_at: 2026-08-29T18:25:49Z
parent: qou-ifot
---

LANDED 2026-08-29, PR #6042, commit 784d4e5b96. This is the finding a later agent most needs from this arc, because it says where NOT to spend a session.

WHY IT WAS POSSIBLE NOW. The exact closed form wordNum_map_closed (same PR) made the criterion evaluable for an arbitrary word for the first time -- previously only the two shape-restricted families could be checked. So it became measurable.

MEASURED (computations/qcollatz_height_criterion_coverage.py, all 2^k words, k <= 18, exact integer arithmetic, no float): the excluded fraction does NOT grow with k. It DECLINES -- 0.375 at k=3 to 0.319 at k=18, monotone from k=5 on. And the reach stops right at the critical band: at k=18 exclusion reaches m <= 10 while the denominator height stays positive to m=11, and that m=11 band (31824 words) has ZERO exclusions.

PROVED, so this is not just an extrapolation from k<=18: height_criterion_vacuous_below_threshold. The criterion cannot fire for ANY word unless 2^k > 2*3^m - 2^m, because every word has height >= 3^m - 2^m (wordNum_map_lower) and once 2^k - 3^m falls to that level there is no room. Exactly complementary to qcollatz_no_front_loaded_cycle's D=m hypothesis 2*3^m - 2^m < 2^k, so the threshold is sharp in both directions.

THE CONSEQUENCE. A genuine cycle needs holonomy near one (2^k/3^m ~ 1); the criterion needs 2^k/3^m > 2 - (2/3)^m, i.e. roughly 2^k > 2*3^m. DISJOINT REGIMES (cycle_regime_is_below_threshold proves the containment for 2^k <= 3^m). The q=1 height is strong away from the critical ratio m/k ~ log2/log3 and provably empty at it.

SO: do NOT spend effort strengthening the height criterion, extending the front-loaded family, or adding more word shapes. None of it can reach cycle candidates. qcollatz_no_adj_tail_cycle, qcollatz_no_front_loaded_cycle and qcollatz_no_cycle_of_height_lt are all bounded by this. Closing the cycle question needs an invariant that SURVIVES at 2^k ~ 3^m -- which the q=1 height provably does not. That is the actual open problem, now stated sharply.

SCOPE (a): this bounds a METHOD. It refutes neither the conjecture nor any ingredient, and every exclusion already proved still stands.

Verified: lean-direct exit 0 first pass; axioms [propext, Classical.choice, Quot.sound] on both, no sorryAx. The probe sanity-checks both extremes against the proved bounds before running.
