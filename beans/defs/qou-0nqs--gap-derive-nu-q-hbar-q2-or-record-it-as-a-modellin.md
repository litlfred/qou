---
# qou-0nqs
title: 'GAP: derive nu_q = hbar_q/2 or record it as a modelling choice'
status: todo
type: task
priority: normal
created_at: 2026-11-25T15:52:43Z
updated_at: 2026-11-25T16:32:15Z
parent: qou-qrrb
---

q-navier-stokes.md introduces nu_q = (1 - q^-1)/2 in the equation; q-navier-stokes.lean has it as a default field. Searched fluid-dynamics/ and stochastic-mechanics/ for a diffusion coefficient, eta/s or horizon condition fixing nu: nothing found (negative is about those surfaces). Candidate: Nelson diffusion hbar/(2m) has the same 1/2 but governs an osmotic term of an inviscid fluid. Open; do not close by renaming.

2026-11-25 (epic qou-i6e2, PR #9434): corpus-grep paths 0-7 found no derivation (table in docs/audits/2026-11-25-qns-literature-formalisation.md). Exact fact: nu_q = Nelson D = hbar_q/(2m) at the m=1 the corpus's Q_q uses (nelson_consistency, Lean, sorry-free). Not a dissipation mechanism. Put to owner: (1) record as modelling choice [recommended] (2) keep open (3) research a regularity condition. Stays open until owner rules.

2026-11-25T16:45Z: regularity routes tested (qou-gd5s): none forces hbar_q/2; Habiro integrality would exclude the 1/2. Strengthens option 1 (modelling choice).
