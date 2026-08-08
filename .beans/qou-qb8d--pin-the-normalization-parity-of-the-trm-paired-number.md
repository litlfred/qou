---
# qou-qb8d
title: 'Pin the normalization: bar-parity of the tr_M-paired NUMBER, not the class'
status: todo
type: task
priority: normal
created_at: 2026-08-08T09:30:00Z
updated_at: 2026-08-08T09:30:00Z
---

Successor to qou-qb8b, which established that the bar-parity of the HH^1 outer
class acting on the cocenter is normalization-dependent (Hilbert 90 over
Q(zeta)/Q(zeta)^+) and therefore carries no information. See
docs/audits/2026-08-08-hh1-outer-class-bar-parity-prune-does-not-exist.md.

The fix is to stop asking about the CLASS and ask about a NUMBER. The c_3 swing
S is a scalar, and bar-parity of a scalar IS well defined. So pin the whole
construction:

    S_candidate = < tr_M , Delta(x) >    for a canonical generator x in HH_0

where Delta is the induced outer action (class-canonical, already computed) and
tr_M is the Markov trace, which factors through HH_0 by the merged
CocenterTraceFactor.lean. Then read bar(S_candidate) vs -S_candidate.

The whole difficulty transfers to pinning TWO things, and neither may be chosen
to taste (that would be a fit):
1. the normalization of the outer representative D -- candidate: require D to
   preserve a Z[q,q^{-1}] lattice, leaving only unit scalings +/- q^k;
2. the canonical generator x in HH_0 -- candidate: the min-length conjugacy
   class basis of He-Nie (already cited in CocenterTraceFactor; this is the
   qou-dilv machinery).

ANTI-FIT GUARDRAIL (load-bearing): choosing the normalization or the generator
so as to make the parity come out bar-ODD is a FIT and must be labelled one and
not wired. The normalization must be pinned by a structural requirement stated
BEFORE the parity is read. If no structural pin exists, report that -- an honest
"the construction is not canonical" is the correct output, not a tuned choice.

Order of work: (2) first via qou-dilv (the He-Nie basis is a real structural
pin), then (1), then read the parity. If (1) cannot be pinned structurally,
stop and report -- do not pick a normalization to taste.
