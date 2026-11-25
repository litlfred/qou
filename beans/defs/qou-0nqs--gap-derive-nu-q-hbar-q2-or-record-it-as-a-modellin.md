---
# qou-0nqs
title: 'GAP: derive nu_q = hbar_q/2 or record it as a modelling choice'
status: todo
type: task
created_at: 2026-11-25T15:52:43Z
updated_at: 2026-11-25T15:52:43Z
parent: qou-qrrb
---

q-navier-stokes.md introduces nu_q = (1 - q^-1)/2 in the equation; q-navier-stokes.lean has it as a default field. Searched fluid-dynamics/ and stochastic-mechanics/ for a diffusion coefficient, eta/s or horizon condition fixing nu: nothing found (negative is about those surfaces). Candidate: Nelson diffusion hbar/(2m) has the same 1/2 but governs an osmotic term of an inviscid fluid. Open; do not close by renaming.
