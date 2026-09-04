---
# qou-ba21
title: 'Lean: markovParam N IS the SU(N) Markov parameter (hook-content principal specialisation)'
status: completed
type: task
priority: high
created_at: 2026-09-04T03:04:50Z
updated_at: 2026-09-04T03:23:15Z
parent: qou-8lxd
---

PROVED 2026-09-04, commit 6a1ca05322. hookContent_markovParam for every N>=1, sorry-free. The stated obstruction ('Mathlib has no hook-content API') was NOT one: the Markov parameter is DEFINED at n=2, and that instance needs only [m]_q plus one algebraic identity. Mutant-tested (RHS -> markovParam (N+1) fails at linear_combination; a changed hook length fails earlier), so it is not true by unfolding. Producer cross-check to 4.6e-41 for N=1..6. Still open: the general hook-content identity for arbitrary lambda; that these weights come from a Markov trace rather than matching the producer; f^lambda=1 unformalised.
