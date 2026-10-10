---
# qou-mcus
title: 'Route 3 (parent: qnnq): multi-cusp effects — proton = Borromean (3 cusps), deformation space is (u₁,u₂,u₃) ∈ ℂ³ (6 real DOF), not one 2D cusp torus. Probe: Murakami-style cone-manifold volume of Borromean with independent per-component cone angles; test if the proton ϑ ≈ 0.203 arises as an asymmetric filling (two components at ln q₀, third carrying the angular datum). Lean: extend SDeformedVolumeChannel u-field to a 3-vector for links.'
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-31T19:30:00Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---

Literature anchors:
- H. Murakami et al. — colored Jones limits ↔ hyperbolic cone-manifold volumes with per-component cone angles α₁..α_ℓ, worked explicitly for the Borromean rings (see survey arXiv 1002.0126 "An Introduction to the Volume Conjecture").
- Neumann–Zagier applies verbatim to multi-cusp: Vol(u₁,u₂,u₃) with the symplectic pairing on ⊕ᵢ H¹(∂ᵢ).

Caveat from T3 finding (PR #4415): the A-polynomial accepts but does not pin ϑ — for a 3-cusp link the A-variety is higher-dimensional, so this route needs an additional selection principle (e.g. the SDP confinement constraint) to close, else it only reparametrizes the gap.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: DUPLICATE.** Duplicate of qou-ay84 (Borromean multi-cusp deformation). Its ϑ≈0.203 test target is not determined by the data.

Evidence: Both are about Borromean 3-cusp (u₁,u₂,u₃) deformation. mcus adds a test against proton ϑ≈0.203, a target that is evidence-unreliable. No commits.

Status: `todo` → `scrapped`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
