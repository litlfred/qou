---
# z2bn
title: 'Lever 1 [FOCUS]: derive/test fibre q-difference kernel R(q,x) for binding genfun; kill-switch = magic-A ⁴He +5.87%'
status: in-progress
type: task
priority: normal
created_at: 2026-06-23T14:19:27Z
updated_at: 2026-06-23T14:39:13Z
---


## Coordination breadcrumb (2026-06-24) — ⁴He binding falsification thread

Empirical input for the R(q,x) derivation + the magic-A ⁴He kill-switch, from the
merged binding thread (PRs #2630/#2681/#2703):

- **B_joint^model (|χ| joint trace) is nearly A-INDEPENDENT**: ³H 3.25 → ³He 3.47 →
  ⁴He 3.80 MeV, while B_AME explodes (8.48 / 7.72 / 28.30). ⁴He captures only **13%**
  of its binding. The multiplicative deficit `1−∏f` **saturates**
  (`productModel_3body_nonpos`).
- **Implication for R(q,x):** its solution **must grow with A** (the `Iν` q-Bessel
  growth regime). A saturating/intensive trace object cannot source the extensive
  binding — that is the dominant gap, bigger than any phase/sign correction.
- The q-Reeb phase `|Δθ_λ|` is only a **directional** correlate (the constant-scale
  `0.206 MeV/rad` relation was falsified at ⁴He, +69%), not the magnitude source.

Witnesses: `he4-qreeb-phase-falsification.witness.json`,
`yardstick-free-phase-binding.witness.json`.
Audit: `docs/audits/2026-06-24-he4-qreeb-phase-falsification.md`.

## Deliverable (2026-06-24, PR #2718) — spectral bridge: the kernel IS extensive

The depth-2 kernel `R=x²−τx+1` (τ(q₀)=2.6424 from the selection-rule anchors,
#2612) has characteristic roots **λ₊=2.1846, λ₋=0.4577** (product 1, det=1). The
dominant root **λ₊>1 is the extensive-growth eigenvalue** the saturating `|χ|`
trace (λ_eff≈1, the degenerate τ=2 boundary) lacks — so the *existing* kernel
already supplies the extensive (A-scaling) binding PR #2703 found missing. The
`a_D⁽ⁿ⁾` body-order sequence grows with ratio → λ₊.

Formalized sorry-free: `QOU/Mass/BindingRecurrenceSpectral.lean`
(`lambdaPlus_gt_one`: τ>2 ⇒ λ₊>1). Probe:
`binding_recurrence_spectral_bridge_probe.py`. Non-overlapping with the geometric
monodromy derivation of τ (sibling `lever1-trB`, owner-gated DG). Does NOT close
the magic-A ⁴He +5.87% (finite-truncation residual).
