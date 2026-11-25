---
# qou-k5jb
title: DEC q-NS probe on the Bring {5,4} map (Mohamed-Hirani-Samtaney scheme)
status: in-progress
type: task
priority: normal
created_at: 2026-11-25T15:52:42Z
updated_at: 2026-11-25T16:28:30Z
parent: qou-qrrb
---

Linearised and nonlinear DEC Navier-Stokes on the exact Bring cochain complex (computations/probes/bring54_cochain_complex_probe.py). Exact or mpmath, no float64. Measure decay rates; expected: 8 harmonic velocity modes never decay (dim ker Delta_1 = 8), enstrophy decays at >= 5 - sqrt 5 under the linear part. Framed as a model computation; it says nothing about 3D regularity (2D NS is globally regular classically). Source library/arxiv-1508.01166v2.

2026-11-25: Mohamed-Hirani-Samtaney's stream-function form U = *d*dPsi (arxiv-1508.01166v2 §3.3, pp. 10-16) makes every velocity coexact, so on genus 4 it drops the 8 harmonic 1-cochains. The probe must add the harmonic component explicitly. The scheme also assumes a pairwise-Delaunay simplicial mesh (§3.1, pp. 7-8), while the Bring map is pentagonal: either subdivide into the 240 (2,4,5) triangles or use unit-weight combinatorial stars, and say which.

2026-11-25 handover. DONE: computations/probes/bring54_dec_qns_probe.py (shared builder bring54_map.py). Exact checks E1-E5 pass: div-free space 31 = 8 harmonic + 23 coexact; linear rates nu*{4^5,6^5,10,(5-sqrt5)^6,(5+sqrt5)^6} and harmonic 0^8; harmonic fields are exact steady states of the full Lamb-form model; dE/dt = -nu*enstrophy exactly. Numerics (mpmath dps 40, RK4, T=20, dt=1/40): pure harmonic data is stationary; pure coexact data at amp 1 transfers energy into the harmonic modes (0 -> 0.0014 of 0.5) while the rest decays. IN FLIGHT: amp-20 runs plus witness; then commit the witness. NEXT: report in the audit item 4; hand the data to the qou-0nqs child (session_01EucfRp1HyniH3qQb1YGVWb). BLOCKERS: none. ROUTE: the Lamb-form J is a modelling choice; a different advection discretisation changes N-numbers only, not E1-E5.
