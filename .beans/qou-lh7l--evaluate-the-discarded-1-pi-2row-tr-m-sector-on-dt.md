---
# qou-lh7l
title: Evaluate the DISCARDED (1-pi_2row) tr_M sector on D/T/3He/4He -- the missing super-pairwise term
status: completed
type: task
priority: normal
created_at: 2026-08-07T09:39:34Z
updated_at: 2026-08-07T09:49:47Z
parent: qou-kemt
---

DONE 2026-08-07, and it REFUTED the hypothesis. Probe computations/two_row_vs_higher_row_binding_split.py, 0 free params, stdlib decimal 60dps over committed 50dps witnesses, no float64. Implementation validated against TWO independent corpus numbers: B(D) bare per-lambda sum 0.380 (mine 0.3801) and C_knot 5.852 (mine 5.8530). FINDING 1 (refutation): the binding formula does NOT truncate to two rows -- it already sums all partitions, so the missing term is not a discarded stratum. My inference was wrong; the N=2 <=> two-row <=> pairwise algebra still stands. FINDING 2 (new, the useful part): the binding sum is >=3-row DOMINATED and the trace is two-row dominated -- OPPOSITE. Delta_lambda = +-f^lambda weights by SYT count, largest for balanced many-row diagrams, which INVERTS the stratum dominance. >=3-row share of the binding sum: D 26.21%, T 62.07%, 3He 61.17%, 4He 100.02% (two-row contributes 0.0007 MeV of 3.0382 at 4He = 0.02%). FINDING 3: that share GROWS with A -- right direction for the extensive term, but 4 points with two at the same A, so a trend not a law. FINDING 4 (negative): including >=3-row does NOT close the magnitude. Deficit B_AME/B_full = 5.853 / 4.444 / 3.292 / 9.313, a 2.8x spread, WORST at 4He. ANTI-CORRELATION worth chasing: 4He has the highest >=3-row share AND the worst deficit -- more >=3-body content goes with a LARGER deficit, arguing the missing object is not simply more higher-row terms.
