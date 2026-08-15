---
# qou-yh67
title: 'GAP: derive boost-enhancement A≈2.05 (c=√A≈1.4305) from substrate — distinct angle: NZ ½ potential normalization κ_shape/κ_pot=2 + precision-ceiling prune'
status: todo
type: task
priority: normal
created_at: 2026-08-01T23:51:10Z
updated_at: 2026-08-02T08:39:35Z
---


## Re-scope 2026-08-02 (PR #4552, branch claude/yh67-nz-half-structural-resolution)

The binary is pinned as a genuine geometric-OBJECT choice, not a free convention:
- κ_shape = √3/2 = Im(FULL NZ potential Φ = ∫₀ᵘ log(−L)dt) — no NZ ½.
- κ_pot   = √3/4 = Im(COMPLEX VOLUME 𝔙 = Φ/2) — the physical Chern–Simons invariant, WITH the NZ ½.
So Φ = 2·𝔙 (Lean-proved sorry-free, QOU/QBeta/ObservableComplexVolumeVsFullPotential.lean).
The A∈{1,2} boost factor IS the object choice {𝔙, Φ}.

VERDICT: STRUCTURALLY OPEN — not proved-forced either way (channel identity is
conjectural CAL-2/Subgoal-2; no u=0 anchor pins the order-u² coeff). Physical weight
FAVOURS κ_pot (𝔙 = the CS invariant): κ_shape/c=√2 would make the observable TWICE
the CS invariant (no mechanism), so it is within-ceiling coincidence, and measured
A≈2.054 reads as a REDUCED Stokes A_ω (integer-3 target, #4521) not a dropped ½.

MISSING INGREDIENT to close: derive which object the fibre→observable (τ/archimedean)
functor applies = the same categorical Stokes derivation as the G3 integer-A_ω=3 target.

Surfaced a live corpus inconsistency (beaned qou-pzzl): ArgUPhaseBranchSelection /
NZBarEvenVolumeFace use κ_shape for the S face; SDeformedVolumeChannel keystone uses
κ_pot·A_ω. See docs/audits/2026-08-02-nz-half-observable-normalization-structural-resolution.md.

## Status check (2026-08-15, session qou-gylf catch-up)

Re-examined from a fresh context; verdict UNCHANGED — structurally open,
and honestly BLOCKED. The candidate unification this pass produced (the
κ_shape convention ≡ κ_pot with prefactor 2, so qou-pzzl's "two conventions"
are one integer variable with candidate values {2, A_ω=3}) is ALREADY
recorded in docs/audits/2026-08-02-pzzl-kappa-shape-vs-pot-S-normalization.md
— not new. The missing ingredient remains the A_ω internal derivation
(qou-qnnq / qou-ujmw / qou-sfuo), whose remaining gap the 2026-08-11
consolidation localizes as open in DT/3d-index categorification itself
(Route A executed, R1 survives cross-knot; Route C scoped as a research
programme, qou-rtec). No distinct angle available from this context that
is not either a catalogued route or a numerology risk (c=√A is at the
proved precision ceiling, sigma_A ~ 40%). Do not measure; derive or wait.
