---
# qou-kdh5
title: 'GAP: Peter–Weyl step 3 — Haar biorthogonality of L-eigenbases on dual components (Lean)'
status: in-progress
type: task
priority: normal
created_at: 2026-11-27T23:10:57Z
updated_at: 2026-11-27T23:10:59Z
---

Thread 'Audit the q-Bessel special-function dictionary' 2026-11-27. After PR #9804 + #9812 (L = X₊X₋ lower bidiagonal with eigenbasis on all four PBW quadrants alpha^a beta^m, alpha^a gamma^m, delta^a beta^m, delta^a gamma^m times K[zeta]).

MEASURED (exact sympy, PBW model, eigenvectors n,n' <= 3, (a,m) in {(1,0),(1,1),(2,1)}): for the dual pairs (alpha^a beta^m <-> delta^a gamma^m) and (alpha^a gamma^m <-> delta^a beta^m), the bilinear Haar Gram matrix h(u p_n(zeta) * v p_n'(zeta)) is DIAGONAL with nonzero diagonal, in both orders, 12/12 cases. The paired eigenvalues are NOT equal (e.g. aB (1,0): 1, [2]^2/q^2 ...; dG (1,0): 0, q^-2[3]...), so this is biorthogonality, not plain L-symmetry. Script: scratchpad orth.py (not committed).

Not established: any Lean proof. Candidate route: h o X± = 0 (q_ns_haar_field_invariance_full) gives twisted integration by parts h(x L y) = h(L' x y) with L' ~ X₋X₊; on each torus weight X₊X₋ - q^2 X₋X₊ is a scalar [n]_{q^-2} (checked in model, not formalized), so L' is affine in L and shares its eigenbases. Then distinct cdiag eigenvalues give orthogonality via cdiag_injective. Algebraic, no empirical values.
