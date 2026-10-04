---
# qou-q95i
title: 'T2: extend i/b-periodicity of the ratio everywhere via the identity theorem (hibinv input)'
status: todo
type: task
priority: normal
tags:
    - alien-habiro
    - reorg-2026-10-04
created_at: 2026-07-18T18:22:29Z
updated_at: 2026-10-04T15:14:03Z
parent: qou-r9ih
---

PARTIAL (2026-07-18): the identity-theorem-free CORE landed — QOU/Common/PeriodicDense.lean periodic_of_continuous_of_eqOn_dense (continuous r + c-periodic on a DENSE set ⇒ c-periodic everywhere), lean-direct exit 0. So hibinv-everywhere does NOT need the full identity theorem: the dual pole lattice is discrete ⇒ complement dense, and continuity + dense agreement suffices. Remaining two inputs, both separable: (i) the ratio is continuous (from the entireness endowment, qou-2cvs); (ii) the dual-lattice complement is dense (a discreteness fact about {e^{2πz'/b}=-1}). Wire into FaddeevRigidityReduction once (i) lands.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-18 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
