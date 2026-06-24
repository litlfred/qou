---
# z2bn
title: 'Lever 1 [FOCUS]: derive/test fibre q-difference kernel R(q,x) for binding genfun; kill-switch = magic-A ⁴He +5.87%'
status: in-progress
type: task
priority: normal
created_at: 2026-06-23T14:19:27Z
updated_at: 2026-06-24T11:45:00Z
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
## Frontier (2026-06-24, post #2674 / #2701 / #2704) — reduced to ONE owner-gated number

The lever-1 binding kernel `R(q,x)` is the depth-2, `det = 1` recurrence `R = x² − τx + 1`.
Everything reduces to the single trace `τ = tr B`:

- **Selection rule confirmed** at c=1 (muon `lw(1)=1`) + c=3 (proton `lw(3)=Family-A`, bit-for-bit
  production `linking_weight_family_a`). `a_D^(n) = lw(n−1)`, `lw(c) = (1/(c+1))·Σ_{λ⊢c+1} dim_q`.
- **Whole identification = one checkable number:**
  `τ = (a_D^(2)+a_D^(4))/a_D^(3) = 3(3q⁴+8q²+3)/(4q(q+1)²) = 2.6424 at q₀`
  (algebra: num `(3q⁴+8q²+3)/(4q²)` ÷ `(q+1)²/(3q)`; cross-checked this session).
- **Torus shortcut REFUTED (#2701):** `τ_torus = 2cosh(2η₀) = 2.0437 ≠ 2.6424`. The binding W-plane is a
  genuinely separate genus-4 Bring object, not the substrate torus.

## The decisive step is OWNER-GATED (sharp reframing, #2701)

`tr B` is a q-FAMILY Gauss–Manin **monodromy** trace, not a fixed-curve period — a single fixed curve
has no monodromy. So the Sage fixed-curve period work (done) cannot supply it; `tr B(q₀)` needs the
**q-family matrix M = the s5-so3 keystone (owner-gated, residual i)**. Fixed-curve facts settled exactly
(Sage + character theory): `H^{1,0}(Bring)` is the standard 4-dim S₅ irrep, A₅-irreducible ⇒
`H¹(Bring)=2W` is NOT an A₅-form-subspace; `W` must be a **CM/isogeny factor of `Jac(Bring)`**
(Riera–Rodríguez), at the de Rham level.

## Three sub-directions (none a quick win; pick with owner)

| # | direction | gating |
|---|-----------|--------|
| A | q-family Gauss–Manin monodromy `M` on the W-plane (supplies `tr B`) | **owner-gated** (keystone residual i; the decisive step) |
| B | Riera–Rodríguez CM/isogeny decomposition of `Jac(Bring)` → exhibit the rank-2 `W` | tool-gated (Sage, fixed-curve; deep, NOT owner-gated) |
| C | non-circular c=2 mass-consumer to TEST `lw(2)=(q+1)²/(3q)≈1.337` | research-grade, circularity-gated (Hopf link non-hyperbolic → no Kashaev/Vol route) |

Refs: `docs/audits/2026-06-24-lever1-trB-geometric-target.md`,
`2026-06-24-lw2-c2-prediction-untested-status.md`, `2026-06-23-delta-lambda-three-lever-status.md`.
Kill-switch (magic-A ⁴He +5.87%) unchanged. No fit; nothing wired. Owner closes (§4a).
