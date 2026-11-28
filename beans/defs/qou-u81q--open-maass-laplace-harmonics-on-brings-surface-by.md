---
# qou-u81q
title: 'OPEN: Maass (Laplace) harmonics on Bring''s surface by S5 type (Transcendental)'
status: in-progress
type: task
created_at: 2026-11-27T21:59:36Z
updated_at: 2026-11-28T00:30:00Z
---

Owner picked 'Also Maass harmonics' (card, 2026-11-27). Done: exact discrete model (computations/probes/bring_discrete_harmonics_probe.py): vertex Laplacian 0,2,4,5,6,7 with S5 types; harmonic 1-cochains = 2 x std(x)sgn. Open: the true Maass spectrum by S5 type; reduces by Frobenius reciprocity to Maass forms on the triangle orbifolds B/H. Belongs in QOU/Transcendental/. No numerical eigenvalue may enter a proof.

## 2026-11-28 — PR #9855 (algebraic half done; analytic values stay open)
Lean, sorry-free: QOU/BringsSurface/BringHarmonicTypes.lean + QOU/Transcendental/BringsSurface/BringMaassTypes.lean.
- 7 types exhaustive (column orthogonality + unique class-function expansion).
- 19x7 table dim rho^H; std(x)sgn column = genus; spheres miss it.
- Typed spectrum = integer combination of untyped spectra of B/S3, B/(S3xS2), B/A4 (torus), B/F20, B/S4, B/A5, B/S5 (unimodular).
- Every type seen by genus-2 B/<(01)(23)> and B/C3; no Sunada pair in S5 (rows distinct).
- H^1(Bring map) = 2 x std(x)sgn by Hopf trace (cellular, no RH).
Open: the eigenvalues; reflection parity under S5 x C2; orbifold signatures of the 7 recovery quotients.

## 2026-11-28 — PR #9874: reflection parity under S5 x C2
T = (2 4) is the unique map reflection; c = xT is free (no real points), so B/c is non-orientable with chi = -3. The triangle sides are (T, ST, AT); triv+/- = Neumann/Dirichlet, and sgn+/- are mixed. H^1 = [2,1,1,1]+ + [2,1,1,1]-. 14 types are exhaustive; recovery uses 7 orientable + 7 non-orientable quotients.
Open: the eigenvalues only.

## 2026-11-28 — PR #9874 merged; PR #9877: typed spectral sunset
The triple selection table N for S5 types: 143/343 allowed, and the holomorphic cubic is forbidden. With parity, 572/2744 are allowed. The sunset on an energy-bounded cut over opaque labels equals the sum of partial sunsets over allowed typed triples (Transcendental/). The selection rule itself (invariance + Schur) is cited.
