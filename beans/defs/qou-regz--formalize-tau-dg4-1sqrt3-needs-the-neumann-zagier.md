---
# qou-regz
title: 'Formalize tau_DG(4_1)=sqrt(3): needs the Neumann-Zagier gluing-equation determinant in Lean'
status: todo
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T02:14:00Z
updated_at: 2026-10-04T15:25:56Z
parent: b9cj
---

Scoped plan for the one leg of PR #4824 §7 that was deliberately **not**
formalized, recorded so the decision is durable rather than re-litigated.

## Why it was not done in #4824

#4824 §7 computed the DG 1-loop torsion numerically (SnapPy, in-session):
`τ_DG(4₁) = √3`, `τ_DG(L6a4) = 64` as calibration, then the honest negative
`τ_DG(8₁₁)/τ_DG(L6a4) = 1.1347` (+3.25%) vs Vol ratio 1.1308 (+2.90%) — the
canonical object does not beat volume for A=3.

The agent formalized the `archimedean_agreement` falsifiability theorems
(landed, sorry-free, axiom-clean) but declined to formalize `τ_DG(4₁)=√3`,
and the reasoning is right: the honest route requires formalizing the
Neumann–Zagier gluing-equation determinant over ℂ. The shortcut —

```lean
axiom tau_41 : tauDG figureEight = Real.sqrt 3   -- ← DO NOT
```

— is exactly the laundering AGENTS.md §"Axiomatization is NOT a Proof"
forbids: it would assert the numeric result as infrastructure and let
downstream Lean consume it as though derived.

## What an honest formalization actually needs

1. **Ideal triangulation as data** — a finite tetrahedron set with face
   pairings; the shape parameters `z_i ∈ ℂ \ {0,1}`.
2. **Gluing equations** — the edge-consistency relations
   `∏_i z_i^{a_ij} (1-z_i)^{b_ij} = ±1` plus the cusp equation. Needs the
   NZ integer matrices `(A|B)` and their symplectic property.
3. **The 1-loop invariant** — `τ = ± det(A·Δ_z + B·Δ_{1/(1-z)}) / 2`
   in Dimofte–Garoufalidis normalization, with the sign/branch convention
   pinned. This is the actual content; Mathlib has none of it.
4. **The 4₁ evaluation** — the two-tetrahedron triangulation with
   `z = e^{iπ/3}`, then `det = √3` by an explicit `ℚ(√-3)` computation.
   Only step 4 is easy; steps 1–3 are the project.

## Estimate and recommendation

Multi-session (steps 1–3 are a small NZ library, not a lemma). **Low
priority**: #4824 §7 already established the negative result that motivated
caring about `τ_DG` — the canonical object does not beat volume for A=3, so
formalizing its value buys no live derivation right now. Revisit only if
`τ_DG` re-enters a production path.

Until then the corpus position is: `τ_DG` values are **numerically
computed** (SnapPy/mpmath, witnessed in
`computations/probes/dg_torsion_binding_ratio_a3_probe.py`), **not Lean-proved**,
and no Lean declaration should assert them.
