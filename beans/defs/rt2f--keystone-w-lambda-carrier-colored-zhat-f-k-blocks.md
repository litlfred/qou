---
# rt2f
title: 'Keystone W_λ carrier, route 2: colored Ẑ / F_K(x,q) knot-complement blocks (owner-gated)'
status: todo
type: task
created_at: 2026-07-03T00:40:00Z
updated_at: 2026-07-03T00:40:00Z
---

## Context

Successor to `s013` (closed 2026-07-03). The keystone value question — what realizes
`bwS0(λ) = d_q(λ)/D` (`BWVacuumRowIsHecke`) — was answered NEGATIVELY for every
constant geometric carrier: the Σ(2,3,5) false-theta S-matrix is D=2 with golden-ratio
row (#3208); the count-matching Σ(3,4,5) row is (1, √2, φ, √2φ) (refuted); and the
**constancy exclusion** closes the whole Seifert/plumbed S-matrix class — constant
algebraic entries (sine products, no q in Hikami eq. 3.8) cannot equal the
nonconstant-in-q family d_q(λ)/D (invariant: [4]_q strictly increasing for q>1).
Audits: `docs/audits/2026-07-02-keystone-valuemap-genuine-smatrix.md`,
`docs/audits/2026-07-03-keystone-route1-closed-route2-scoped.md`.

## The task (route 2 — the surviving type-correct class)

The carrier must be a **q-function family**. Concrete candidate: the two-variable
knot-complement blocks **F_K(x, q)** (Gukov–Manolescu; GPPV framework — radial-limit
theorem proved for negative-definite plumbed manifolds by Murakami,
`library/arxiv-2205.01282v2/2205.01282v2.pdf`; Seifert resurgence machinery in `library/arxiv-1811.05376v4/1811.05376v4.pdf`).
The λ-dependence enters through the colour variable x: state the x-specialization
hypothesis class realizing `bwS0(λ; q)` at real q₀ > 1, THEN probe.

## Discipline (formalize-first — this is new corpus infra)

1. **State before computing:** the hypothesis class (which x-points ↔ which λ ⊢ 5) and
   its invariants (transpose-symmetry λ↔λ′; the self-conjugate (3,1,1) = [4][3]/[2]
   discriminating block; q→1 classical dims 1,4,5,6; bar/chirality ℤ₂).
2. **Prune with invariants first** — the same gates that killed rounds 1–3 (constancy;
   L-value monotonicity; 1-dof overdetermination) apply to any candidate specialization.
3. No F_K formula from memory: build against the uploaded papers (+ Gukov–Manolescu
   when uploaded), validating each specialization against a known invariant (e.g.
   F_{4₁}, F_{trefoil} known expansions) before use.
4. Owner-gated: opening F_K infrastructure is a real tranche; coordinate on
   `docs/coordination/s5-so3-keystone.md` and #2503 (DG session's
   `QBesselRadialPartRealization` obligation class is the Lean-side target this would
   instantiate or refute).

## Cross-refs

- Constancy exclusion + Σ(3,4,5): `computations/probes/keystone_route1_sigma345_constancy_s013.py`
- Genuine S-matrix: `computations/probes/keystone_valuemap_genuine_smatrix_s013.py`
- Lean obligation (sibling DG session): `QOU/BraidKnot/KeystoneQBesselRadialTarget.lean`
- Ledger: `docs/coordination/s5-so3-keystone.md`
- Papers: `library/arxiv-math-ph-0405028v2/0405028v2.pdf`, `library/arxiv-1811.05376v4/1811.05376v4.pdf`, `library/arxiv-2205.01282v2/2205.01282v2.pdf`,
  `library/zagier-the-dilogarithm-function/zagier-the-dilogarithm-function.pdf`
