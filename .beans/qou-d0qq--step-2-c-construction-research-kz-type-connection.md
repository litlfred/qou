---
# qou-d0qq
title: 'Step-2 C construction (research): KZ-type connection on the configuration space of the colour cubic''s six branch points at an IMAGINARY level, monodromy computed, Hecke quadratic read off; first measurement = does any level reproduce q0 ≈ 1.11 real'
status: todo
type: task
priority: normal
created_at: 2026-09-06T08:13:53Z
updated_at: 2026-09-06T08:16:00Z
parent: qou-2akx
---

2026-09-06 first measurement (exact, mpmath 40 dps at the proton pin): KZ at REAL level cannot give q0 (unit modulus, Lean KZUnitModulusPrune); at IMAGINARY level it can — with q = e^{2πi/(k+2)}, k+2 = 2πi/ln q0 = 60.2179598524791980753 i (ln q0 = 0.10434072031951951232); with q = e^{iπ/(k+2)}, k+2 = 30.1089799262395990377 i. So the prune does not kill C; it fixes the level to be non-unitary. Next: write the KZ connection on Conf of the six branch points at that level and compute its monodromy exactly (Kohno–Drinfeld gives Hecke; the question is whether the framework's connection IS this one).
