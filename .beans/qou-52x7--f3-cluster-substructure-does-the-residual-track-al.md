---
# qou-52x7
title: 'F3 cluster substructure: does the residual track alpha-clustering rather than body order?'
status: completed
type: task
priority: normal
created_at: 2026-08-26T03:37:40Z
updated_at: 2026-08-26T04:10:24Z
---

VERDICT 2026-08-26 (pre-registered).

Prereg: docs/audits/2026-08-26-cluster-substructure-prereg.md @ 843391340b7511f131fcd8342f1e1ea1e925384b (pushed BEFORE any computation).
Probe:  computations/probes/cluster_substructure_edgeset_prereg_probe.py @ fc9ab4e045
Verdict: docs/audits/2026-08-26-cluster-substructure-verdict.md @ 2c7183b4c7

H_all (clustering explains THE residual): REFUTED, scope (b). 4He IS the alpha, so
it is a single cluster under every scheme, its edge set is K_4 identically, and
r = B_AME/B = 1.647031 is invariant across all four pre-registered evaluations
(R-ii fired). Under maximal-alpha the immovable set {2H,3H,3He,4He} has
r = 0.785/0.945/0.940/1.647 — it ALREADY straddles 1, so the entire
non-monotonicity lives where clustering is a no-op.

H_partial (A>=6 over-binding only): NEITHER supported nor refuted. Best of the four
evaluations is C2+E2 at max|r-1| = 0.1806 — above the 0.10 support threshold,
below the 0.25 refutation threshold, i.e. the band declared in advance.

New bracket (holds for ANY inter-cluster bond typing, since E2 bounds B above):
r(6Li) >= 1.18 and r(7Li) >= 1.06 under both schemes. Clustering moves 6Li/7Li
from 0.743/0.639 in the right direction and PAST 1 — it over-corrects. Truth sits
strictly between the cluster edge set and the complete graph (required bond weight
is 74.3%/63.9% of K_A; E2 supplies 54.2%/47.9%). Tuning to land on it would be a
fit and is barred by the prereg.

NOT excluded: cluster structure as a NEW MANY-BODY TERM (different arity). The
connected-sum / volume-additivity route already EXISTS in the corpus
(computations/deltalambda/alpha_cluster_volume_additivity_probe.py, 8Be +0.16%)
and the SU(4) [1^4] gate is Lean-proved with the magnitude still empirical.

Two corrections recorded: (1) S-C1(ii) fails for the E2 rule because the
B-maximising inter-cluster typing RE-TYPES rather than removes edges — my
construction, not the mathematics; (2) the structural argument the front requested
is not available as posed, because B_allpairs is not over undifferentiated
nucleons (it carries three distinct (Z,N)-differentiated bond constants).

precision-gates.sh --changed: all blocking gates green. mpf end to end, 60 dps.
