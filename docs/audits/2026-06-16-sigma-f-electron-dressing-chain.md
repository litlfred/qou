# σ_F(Z) electron-dressing chain — confinement-SDP dual at level 6

**Date:** 2026-06-16
**Branch:** `claude/zealous-hypatia-05xyp9` (PR #2348)
**Compute:** [`computations/electron_sigma_f_chain.py`](../../computations/electron_sigma_f_chain.py)
**Class:** exploratory diagnostic — no fit, no witness.

## What this delivers

The faithful continuation of the electron-shell SDP demo: the **dual** of the
confinement SDP ([`prop:confinement-sdp`](../../content/quantum-observable-universe/mass-theory/confinement-sdp.md))
computed at the **atom-electron level (level 6)**, tracing the Frobenius
stability index

$$
  \sigma_F(P^{(Z)}, q) \;=\; n_{\text{target}} \cdot y_0^*(P^{(Z)}, q)
$$

along the electron dressing chain, with the binding multiplicity
`μ = rank Φ*` (= |active support|).

This **fixes the first-class-dual anti-pattern**: the canonical
`pyhecke.sdp` carries level 6 only as a *skeleton*, and the deprecated
`multi_level_sdp.py` is *primal-only* (`min Σ V`, no `y₀*`/`active_set`). The
SDP is set up per the proposition (`min ⟨T,Φ⟩`, `Φ ⪰ 0`, per-block Frobenius
positivity `⟨π_λ,Φ⟩ ≥ 0`, `tr Φ = n_target`; `T` = Markov weighting) and the
dual is emitted via cvxpy + Clarabel.

## Results

`q₀ = 1.109979`, `z = 0.49932`.

### §1 — Claim 1: σ_F monotone non-decreasing (He-like, A=4 dressing chain)

| e⁻ (Z) | n_target | σ_F | y₀* | μ | gap |
|--:|--:|--:|--:|--:|--:|
| 0 | 12 | 1.4939 | 0.12449 | 1 | 8e-10 |
| 2 | 14 | 1.7429 | 0.12449 | 1 | 1e-9 |
| 4 | 16 | 1.9919 | 0.12449 | 1 | 1e-9 |
| 6 | 18 | 2.2408 | 0.12449 | 1 | 2e-9 |
| 8 | 20 | 2.4898 | 0.12449 | 1 | 2e-9 |

**σ_F monotone non-decreasing: True**, feasible throughout, duality gap ≈ 1e-9
(strong duality / Slater verified). The SDP never goes infeasible —
confirming `prop:shell-closure-stability` claim 1 and refuting the
"add-until-infeasible capacity" notion with the *canonical dual* (not the
raw-Gram interlacing branch).

### §2 — Claim 2 mechanism: degenerate cost-min ⇒ μ ≥ 2

| shell degeneracy d | μ = rank Φ* | σ_F | |
|--:|--:|--:|:--|
| 1 | 1 | 0.2000 | open |
| 2 | 2 | 0.2000 | μ≥2 (closed) |
| 3 | 3 | 0.2000 | μ≥2 (closed) |
| 4 | 4 | 0.2000 | μ≥2 (closed) |

When the lowest cost level is `d`-fold degenerate — a closed shell, all
magnetic/spin labels of principal `n` at one energy — the optimal `Φ*`
occupies the `d`-dim eigenspace and `μ = d`. `μ ≥ 2` is the binding-multiplicity
signature of shell closure (claim 2); σ_F sits at the shell minimum
independent of `d`.

## What is deliberately NOT faked

The σ_F **local maxima exactly at the noble-gas** `Z ∈ {2,10,18,36,54,86}`
(claim 2 + the ionisation-energy corollary `I₁(Z) ∝ σ_F`) need the multi-level
cost operator that encodes the `2n²` shell degeneracies and the Madelung
sub-shell ordering. Hand-coding those would make the periodic-table peaks an
**input**, not an emergent result — so they are left to the level-6
cost-operator infra cut, **not** manufactured here. Per the critical-distance /
no-numerology discipline, this script delivers the dual machinery + claim 1 +
the claim-2 mechanism, and reports the peaks as the open infra item.

## Notes

- **Dual-sign convention.** cvxpy returns the equality-constraint multiplier
  with the opposite sign to the Lagrangian convention here; flipped so
  `σ_F = n_target·y₀* = primal_obj` (gap ≈ 1e-9 confirms it).
- **Follow-up.** The level-6 cost operator (2n² degeneracies + Madelung order)
  would let σ_F(Z) reproduce the ionisation peaks; this is the genuine
  research-infra tranche, distinct from the dual machinery delivered here.
