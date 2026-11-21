---
# qou-w8es
title: 'GAP G3: derive the irreducibility of H1(M0) = 2W as an A5-representation (chi = -6 chain)'
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

**Statement.** H¹(M0) ⊗ ℂ = 2W with W an irreducible A5-representation is an input of the genus-4 chain (`hdim` / `hχ` in the Lean). Derive it from the QOU axioms.

**Known.**
- With H_W, the Lefschetz/RH enumeration (audit §3 table) gives g ∈ {4, 5}; S5 then gives 4.
- Without irreducibility, A5 admits g = 6, 9, 10, … (audit table).

**Candidate source named in the audit:** a "no proper invariant subsystem of periods" statement. The natural carrier is the Gauss–Manin system rank used in `prop:prolonged-periods-fixed-depth`, which currently reads rank 8 off Bring (circular).

**Open; do not close** (AGENTS.md §13a).
