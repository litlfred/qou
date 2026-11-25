---
# qou-k5jb
title: DEC q-NS probe on the Bring {5,4} map (Mohamed-Hirani-Samtaney scheme)
status: todo
type: task
priority: normal
created_at: 2026-11-25T15:52:42Z
updated_at: 2026-11-25T16:11:55Z
parent: qou-qrrb
---

Linearised and nonlinear DEC Navier-Stokes on the exact Bring cochain complex (computations/probes/bring54_cochain_complex_probe.py). Exact or mpmath, no float64. Measure decay rates; expected: 8 harmonic velocity modes never decay (dim ker Delta_1 = 8), enstrophy decays at >= 5 - sqrt 5 under the linear part. Framed as a model computation; it says nothing about 3D regularity (2D NS is globally regular classically). Source library/arxiv-1508.01166v2.

2026-11-25: Mohamed-Hirani-Samtaney's stream-function form U = *d*dPsi (arxiv-1508.01166v2 §3.3, pp. 10-16) makes every velocity coexact, so on genus 4 it drops the 8 harmonic 1-cochains. The probe must add the harmonic component explicitly. The scheme also assumes a pairwise-Delaunay simplicial mesh (§3.1, pp. 7-8), while the Bring map is pentagonal: either subdivide into the 240 (2,4,5) triangles or use unit-weight combinatorial stars, and say which.
