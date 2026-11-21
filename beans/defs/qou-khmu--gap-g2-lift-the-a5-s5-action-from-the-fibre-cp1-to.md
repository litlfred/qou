---
# qou-khmu
title: 'GAP G2: lift the A5/S5 action from the fibre CP1 to the base curve M0 (chi = -6 chain)'
status: todo
type: task
priority: high
tags:
    - bring-foundations
    - research
    - open-derivation
created_at: 2026-11-21T07:30:00Z
updated_at: 2026-11-21T07:30:00Z
parent: qou-qhcr
---
Created 2026-11-21 by W9 (session_01VQDpPcjxVSqN8ELUBjiBHk). The gap was named in `docs/audits/2026-11-17-bring-foundations-trace-sites-and-genus-attack.md` §3 and had no bean.

**Statement.** The corpus has A5 (and the EM involution in S5 \ A5) acting on the fibre P(V) ≅ CP¹ (`klein-bring-icosahedral-bridge`), not on the base curve M0. The genus-4 chain needs a faithful A5 action on M0, extending to S5.

**What is proved downstream.** Granted the lift and G3, the genus is 4 and χ = -6. This is sorry-free on main: `IrreducibleH1ForcesGenusFour`, `A5NoSixDim`, `RiemannHurwitzCellular`, `GenusFourFromGermStabilisers`, `GenusFourFromEquivariantMap`.

**Constraint (NO FITTING).** Every order-5 structure in the corpus is downstream of Bring (audit §2 item 4, qou-qhcr sessions of 2026-09-15). The lift must not be chosen because it yields 4.

**Open; do not close** (AGENTS.md §13a).
