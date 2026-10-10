---
# qou-k16h
title: Close the A_w zero-asymptotics residual (extremal class = tropical class)
status: completed
type: task
priority: normal
created_at: 2026-08-01T20:25:40Z
updated_at: 2026-08-01T21:26:57Z
---


## Artifacts (2026-08-01)

- Audit: `docs/audits/2026-08-01-awzero-asymptotics.md`
- Probe: `computations/probes/awzero_asymptotics_probe.py` → `awzero-asymptotics.witness.json`
- Lean: `content/quantum-observable-universe/lean/QOU/Archimedean/AwZeroLocalization.lean` (sorry-free, `lean`-direct exit 0)
- References registered (metadata-verification level only): `bergweiler-hayman2003`, `ismail2005qairy`

## Result

PROVED: zeros of `A_w(z) = Σ w^{m²}(−z)^m/(w;w)_m` satisfy
`ζ_n = w^{1−2n}(1 + θ_n)`, `|θ_n| ≤ 2κ(w)w^n`, for every `0 < w < 1` and every
`n ≥ n₀(w)`, with `κ(w) = (w;w²)_∞²/[(1−w)(w²;w²)_∞²]` (κ(0⁺)=1, κ(1⁻)=2/π) and
`n₀` explicit from closed-form majorants. `n₀ = 135` at the muon pin
(w = q̃⁻¹ ≈ 0.949167), where the bound is 1.1e−3.

Method: recentre `A_w` at index n; the recentred series converges to a Jacobi
theta function whose zero set IS the tropical lattice; Rouché against that limit,
with the defect's q-shifts telescoping exactly so the theta cancellation is kept
on both sides (a single-term Rouché discards it and closes only for w < 0.4535).

## Honest residual

- The theorem is silent for `n < n₀(w)` (sufficient, not necessary).
- Indexing ("that zero is the n-th") is claimed for `n > n₀`, not at `n = n₀`.
- The refinement `θ_n = −κ(w)w^n + O(w^{3n})`: leading term derived, remainder
  order measured, not separately proved.
- Ismail–Zhang, Adv. Math. 209 (2007) 363–380 could not be verified (proxy 403
  on every publisher and arXiv); if its reported convergent-series result is
  correct it is stronger than the above. Follow-up from an unblocked environment.
