---
# qou-zmat
title: '#7092: is the duality/σ ratio a coboundary? solve the vertex-gauge system over K exactly (falsifiable form of qou-qjhc)'
status: completed
type: task
priority: normal
created_at: 2026-09-07T18:06:40Z
updated_at: 2026-09-11T15:25:52Z
parent: qou-6g7j
---

Issue #7092 restates qou-qjhc as a yes/no: do vertex scalars λ_v exist with σ(x_t)/x_π(t) = ∏ λ_{v_i}^{t_i} for every Ptolemy coordinate of the exact L6a4 class-1 point? Needs snappy's vertex-incidence data for the L6a4 triangulation, the multiplicative system over K^× (additive in the exponent lattice), and handling of the 5 coordinates eliminated by eliminate_fixed_ptolemys=True. yes → duality = σ-transport up to gauge; no → different maps, Sym² argument keeps resting on class-level agreement. Exact arithmetic, no floats, NO FITTING (no widening the ansatz, no coordinate subset selection).



**ROAST 2026-09-07 (qou-pbwj) — verdict: CONTINUE, re-scoped.** Two objections a referee raises. (1) Arity: the test runs on ONE point (the exact L6a4 class-1 point); a 'yes' establishes that this point is exchanged with its Galois conjugate by duality up to gauge — a point-level fact — not that ρ ↦ ρ^{-T} induces σ as a map on the variety (two rational self-maps can agree on a Galois orbit). Rewrite the deliverable as the point-level statement. (2) The system is multiplicative in K^×, an abelian group — not K-linear. The decisive exact form is integer: with M the (coordinates × vertices) exponent matrix, the ratios r_t are a coboundary iff ∏_t r_t^{a_t} = 1 for every a in the left ℤ-kernel of M (Smith normal form), modulo the μ₃ torsion the fifth pass identified. Fit exposure: ansatz widening on the 5 coordinates eliminated by eliminate_fixed_ptolemys=True (treat them as unknowns; do not add per-tetrahedron scalars) and subset selection (run the full system, not the 6 paired coordinates). Corpus-grep: not answered; GGZ §12 'Duality' in the library is the Ptolemy↔shape (Langlands) duality, not this. L2 relevance: none; the Sym² verdict is independent either way. Worth having even if negative: a definite NO closes qou-qjhc negatively and stops a decoration-formalisation tranche. Full frame: docs/audits/2026-09-07-takeover-fronts-roast.md §Front 2.

## 2026-09-11 — first attempt LOST to a rate limit before the probe ran

The dispatched agent died (API 429, 2026-09-07 ~18:45 UTC) at 'cleaning two leftover scratch lines before the first run'; its worktree was reclaimed, nothing committed. Roast steer (PR #7133) carried into the re-dispatch: decide by the ℤ-kernel (Smith normal form) of the exponent lattice acting on K^×, not a K-linear solve; treat the 5 eliminated coordinates as unknowns; a 'yes' is a point-level fact about the class-1 point, not an identity of maps. Re-dispatched 2026-09-11 on branch claude/ptolemy-sigma-coboundary-test-2026-09-11.

## 2026-09-11 — second attempt RAN: YES for sigma_b (PGL(3) gauge), NO for sigma_a, NO for the scalar ansatz

Branch `claude/ptolemy-sigma-coboundary-test-2026-09-11`, PR #7183, probe
`computations/ptolemy/ptolemy_duality_sigma_coboundary_test.py` + witness alongside.  Decided by
the Z-kernel of the gauge exponent lattice, exactly in K; snappy 3.3.2 had to be pip-installed
(it was NOT present in this container — the 2026-09-07 "installed" measurement was another one).

- **Correction to this bean's own text:** `eliminate_fixed_ptolemys=True` eliminates **6**
  coordinates, not 5 (`c_0012_0, c_0012_1, c_0102_1, c_0111_0, c_1002_0, c_2001_0`); the same
  6 for `P^{-c}`, differing only by `u -> u^2`.  And the verdict is gauge-invariant (measured),
  so "treat the eliminated coordinates as unknowns" is automatic.
- **sigma_a**: NOT a coboundary (91/122 torus kernel relations fail; simplest obstruction: two
  coordinates with identical gauge exponents, `c_0210_0` / `c_0120_0`, whose ratios differ by
  a non-root-of-unity element of K).
- **sigma_b**: all 122 kernel relations trivial => `r in Hom(L, K^x) = T_PGL(3)(K)`, a genuine
  coboundary of the PGL(3) decoration gauge over K, all 128 equations verified; it does NOT
  lift to a diagonal SL(3) matrix over K (`r(3e_0)` is not a cube in K — `Y^3 - w` irreducible).
- **scalar ansatz `lambda_v^{t_i}` (the issue as written)**: NOT a coboundary for either sigma.
- `Gal(K/Q) = Z/2 x Z/2`; both sigma are involutions — what makes the split verdict consistent
  with D being an involution.

Full record, scope and the remaining open content are on the parent bean `qou-qjhc` (sixth
pass), which stays OPEN per rule 13a: this bean's yes/no is answered; the representation-level
identification is not.

