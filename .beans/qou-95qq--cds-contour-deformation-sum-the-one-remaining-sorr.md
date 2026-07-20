---
# qou-95qq
title: 'CDS: contour_deformation_sum — the ONE remaining sorry finishing the argument principle. Multi-punctured Cauchy ∮_{C(c,R)} h = Σ_{w∈S} ∮_{C(w,ρ)} h for h holomorphic off finite S. BUILD by induction on |S| from Mathlib''s single-puncture Cauchy + rectangle-vanishing (both PRESENT per ARG-SUM survey)'
status: completed
type: task
priority: normal
created_at: 2026-07-20T14:48:28Z
updated_at: 2026-07-20T15:56:18Z
---


## Outcome (2026-07-20) — REDUCED, not fully closed

`contour_deformation_sum` split into three separated pieces:
- `exists_puncture_radii` — radius selection (metric topology) — **PROVED sorry-free**
- `|S|=0` base case (Cauchy–Goursat) inside `contour_deformation_sum` — **PROVED sorry-free**
- `residue_theorem_deformation` — the `|S| ≥ 1` off-centre / multi-hole homology
  deformation — the **single remaining cited sorry**

Mathlib v4.24.0 survey (source-verified, not just #check): only the **concentric**
annulus deformation (`circleIntegral_eq_of_differentiable_on_annulus_off_countable`,
puncture at centre `w=c`) and the on-disc Cauchy integral formula are present. No
`windingNumber`, no `Complex.residue`, no off-centre/homology deformation — so even
`|S|=1` with `w ≠ c` is genuinely absent (the induction-from-single-puncture route in
the original plan does not close: peeling a puncture leaves a non-circular contour, and
`circleIntegral` only represents circles). Winding-number note: the small discs need
NOT be disjoint — each need only avoid other punctures' centres — which is why
`exists_puncture_radii` suffices without a disjointness clause.

`lean`-direct exit 0, one intended `declaration uses 'sorry'`. Commits `f5bb33e3`
(code) + `8e722328` (docs) on `claude/argument-principle-residue-sum-2026-07-20`.
Kept in-progress: the argument principle is fully closed for `|S|=0`; the general
statement still rests on the one topological gap.
