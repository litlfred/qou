---
# qou-yh67
title: 'GAP: derive boost-enhancement A≈2.05 (c=√A≈1.4305) from substrate — distinct angle: NZ ½ potential normalization κ_shape/κ_pot=2 + precision-ceiling prune'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T23:51:10Z
updated_at: 2026-11-15T17:33:11Z
parent: qou-avtq
blocked_by:
    - qou-cds1
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

## Attack options (2026-08-15 ledger)

- **B1 — consistency-forcing search** [formalize-first; small-medium]. Hunt
  the sorry-free corpus for an independent pin of the order-u² Im
  normalization (OhtsukiTowerBarParity odd_rung_imaginary,
  FigureEightComplexVolume, the q3np integrality) and attempt a Lean
  contradiction with one of the two conventions. Either outcome is progress:
  a contradiction forces the object choice; double-consistency proves the
  binary is genuinely undetermined by current assets.
- **B2 — conditional-class the choice** [honest scaffolding; small]. State
  "the τ-functor applies 𝔙 (κ_pot)" as a content-bearing §3b class; A=1
  downstream statements become conditional theorems; qou-pzzl's convention
  split becomes machine-tracked instead of prose-tracked.
- **B3 — normalization literature check** [evidence only; small]. Do
  Andersen–Kashaev / GGM state-integral conventions normalize the observable
  at 𝔙 or Φ? Import as evidence tier, never as the derivation.
- **B4 — the terminus** [blocked]. Full resolution = A_ω internal derivation;
  post-d999b21d7 the honest next rung there is M1 (see qou-rtec D1), not
  more normalization analysis.

## B1 result (2026-08-15, qou-uxwc — OhtsukiNZBridgeScale.lean, sorry-free)

The consistency-forcing search's outcome is the DOUBLE-CONSISTENCY branch,
with a new derived lock: conditional on a linear bridge u = c·b identifying
the quantum fluctuation with the geometric deformation, the order-b² match
between the Ohtsuki rung (κ₁ = 11√3π/108, exact) and the NZ leading form
forces (1) c² purely imaginary — the diagonal-ray geometry DERIVED rather
than assumed (cross-checks A2), and (2) κ_A²·‖c²‖ = (2πκ₁)² — the bridge
scale and the A-binary are one unknown, in ratio exactly 2 between the two
conventions. No sorry-free asset pins ‖c‖ independently, so the binary is
UNDETERMINED at order b² by current assets — but any future independent
bridge-scale pin now decides A mechanically, and vice versa.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: EVIDENCE-UNRELIABLE.** The Lean dictionary work stands, but the numeric target A≈2.05 is not a measurement: σ_A ≈ 268 from CAL-3 (±1.262 on S_mu), the value is 2.126 at the CODATA-2022 pin, and it is C-frame. Remove "≈2.05" as a target, and also record the factor-2 residual inherited via qou-u14x/pzzl.

Evidence: `ObservableComplexVolumeVsFullPotential.lean` (Φ=2𝔙) and `OhtsukiNZBridgeScale.lean` have 0 real sorries, and the structural analysis stands. But the target A≈2.054 uses the CODATA-2018 S_mu (2.126 at the live pin) and is convention-C. The bean's "sigma_A ~ 40%" contradicts the witness: σ_A ≈ 1.262/(κ ln²q0) ≈ 268.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

### Progress (Round 74 — PR litlfred/qou#8322)
- Formalized in PR `litlfred/qou#8322` (`feat/round74-kashaev-stokes3-stokesamp-ohtsukinz-pauli-43c1`, Commit 1 `82ec77a3b69cc6d79a85c01e64b63d422fa51c45`, Head `d13ffedea3175ba61da12a5b2abf5cf08d471608`, `scriptHash: 79ed375a0246`).
