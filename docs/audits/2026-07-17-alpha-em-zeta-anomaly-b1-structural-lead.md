# α_EM structural lead confirmed: ζ_Λ(0) = −b₁ (topological, metric-independent)

**Date:** 2026-07-17 · **Axis:** α_EM / L2 loop measure ·
**Executes:** [`2026-07-17-three-front-attack-specs.md §3`](2026-07-17-three-front-attack-specs.md)
(companion to [`2026-07-17-1ppq-path-reassessment.md`](2026-07-17-1ppq-path-reassessment.md)) ·
**Probe:** [`alpha_em_zeta_anomaly_b1_probe.py`](../../computations/alpha_em_zeta_anomaly_b1_probe.py) ·
**Tier:** scope-(a) partial-positive; no fit, nothing wired, not reverse-engineered to 8π.

## The wall and the lead

The α_EM single wall is the **photon 1-loop measure** `1/(π·b₁) = 1/(8π)` (b₁ = 8),
which would certify the θ-graph 2-loop candidate `−[3]_q/(8π)²` (1.3σ,
parameter-free). Spec §3's first structural lead: the flat-torus **scale anomaly**
`ζ_Λ(0) = −b₁` — "the one place a bare b₁ *count* (not an area/covolume)
canonically appears in a ζ-regularized determinant."

This audit establishes that lead **rigorously and metric-independently**, which
matters because it sidesteps the tool-limited Bring genus-4 period matrix
entirely (the `2026-06-24` keystone probe recorded Sage's RiemannSurface
integrator failing on Bring's conjugate singularities): `ζ_Λ(0) = −b₁` depends
only on `b₁`, not on the lattice or metric.

## Results

**1. `Z_Λ(0) = −1` for every flat torus (metric-independent).** The scalar
Epstein zeta `Z_Λ(s) = Σ_{m≠0} Q(m)^{−s}` is analytically continued by the
Jacobi/Mellin split; the `−1/s` pole against `1/Γ(s) ∼ s` forces `Z_Λ(0) = −1`.
Verified numerically (`|Z_Λ(0)+1| < 4×10⁻¹²`) across dimensions and covolumes:

| lattice | Z_Λ(0) |
|---|---|
| ℤ¹, ℤ², ℤ³, ℤ⁸ | −1.000000000 |
| rect. covolume 2 (n=8) | −1.000000000 |
| rect. covolume 6 (n=3) | −1.000000000 |
| rect. irrational (√2, π/2, 1) | −1.000000000 |

This is the Seeley–DeWitt statement `ζ_Δ(0) = a_{n/2} − dim ker Δ` with the flat
heat coefficient `a_{n/2} = 0`.

**2. `ζ_{1-form}(0) = −b₁ = −8` on the Jacobian torus `J(M) = H¹/H¹(ℤ) = T⁸`.**
The Hodge–de Rham 1-form (photon) Laplacian on `T^{b₁}` is `b₁` copies of the
scalar, so `ζ_{1-form}(0) = b₁·Z_Λ(0) = −b₁`; at `b₁ = 2g = 8` (g = 4) this is
`−8`. The `8` is a **bare topological integer**.

**3. The covolume is in the heat term, not in ζ(0).** The leading small-`t` heat
trace is `Tr e^{−tΔ}·t^{n/2} → π^{n/2}/V` (verified: `48.704546 = π⁴/2` at
covolume 2, n=8): the covolume `V` sits (as `1/V`) in the `t^{−n/2}` term — the
μ-scale-absorbable magnitude of `det'` — whereas `ζ(0) = −b₁` is covolume-blind.

## Reading (honest scope)

This **confirms the spec-§3 lead exactly**: a bare `b₁` count *does* appear
canonically in a ζ-determinant — at `ζ(0)`, **not** as an area — so the
topological loop measure `1/(π·b₁)` is the clean home for the `1/b₁` factor,
cleaner than the merged **metric-dependent** area form `2/(3π) = b₁/Area`
(Area = 12π; [`em-coupling-bring-zero-mode.md`](../../content/quantum-observable-universe/predicted-spectra/em-coupling-bring-zero-mode.md)),
which is the weight-1 additive correction, a different object.

**Not closed.** Per the pre-registered kill criteria, this forces only the
**b₁-count factor**. The remaining `1/π` per-mode weight — the analog of the
proved `1/(12π)` template's *geometric identity* factor — is **not** derived
here, and the ζ-determinant's μ-dependence still formally absorbs a constant.
So the result is **scope-(a) partial-positive**: the derivation is advanced one
concrete step (the count is now topological, not an area), with the per-mode
weight the identified next piece.

## Next piece

Derive the `1/π` per-mode weight of `1/(π·b₁)` — the Gaussian/geometric
normalization of the zero-mode measure on `J(M) = T⁸` — mirroring the second
factor of the proved `1/(12π)` template (mode count × **per-mode weight** ×
geometric identity). A μ-independent derivation of that factor, combined with
the topological `b₁` established here, would force `1/(8π)` without
reverse-engineering.

## Cross-references

- Spec / reassessment: `2026-07-17-three-front-attack-specs.md §3`, `2026-07-17-1ppq-path-reassessment.md`.
- Proved template: `em-coupling-bring-zero-mode.md` (`2/(3π) = 8/(12π) = b₁/Area`); open problems: `alpha-em-derivation-open-problems.md`.
- Tool limit sidestepped: `2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md` (Bring period matrix, Sage-limited).
- Ledger: `docs/coordination/alpha-em.md`.
