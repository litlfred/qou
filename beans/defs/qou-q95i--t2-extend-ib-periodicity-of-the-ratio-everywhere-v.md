---
# qou-q95i
title: 'T2: extend i/b-periodicity of the ratio everywhere via the identity theorem (hibinv input)'
status: in-progress
type: task
priority: normal
tags:
    - alien-habiro
created_at: 2026-07-18T18:22:29Z
updated_at: 2026-07-18T18:43:47Z
parent: qou-89f9
---

PARTIAL (2026-07-18): the identity-theorem-free CORE landed — QOU/Common/PeriodicDense.lean periodic_of_continuous_of_eqOn_dense (continuous r + c-periodic on a DENSE set ⇒ c-periodic everywhere), lean-direct exit 0. So hibinv-everywhere does NOT need the full identity theorem: the dual pole lattice is discrete ⇒ complement dense, and continuity + dense agreement suffices. Remaining two inputs, both separable: (i) the ratio is continuous (from the entireness endowment, qou-2cvs); (ii) the dual-lattice complement is dense (a discreteness fact about {e^{2πz'/b}=-1}). Wire into FaddeevRigidityReduction once (i) lands.
