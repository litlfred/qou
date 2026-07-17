# α_EM 1/π per-mode weight: the flat-determinant route is a fitting trap; 1/π reduces to the open dilog conjecture

**Date:** 2026-07-17 · **Axis:** α_EM / L2 loop measure ·
**Follows:** [`2026-07-17-alpha-em-zeta-anomaly-b1-structural-lead.md`](2026-07-17-alpha-em-zeta-anomaly-b1-structural-lead.md) (PR #3831, the b₁-count lead) ·
**Probe:** [`alpha_em_permode_weight_probe.py`](../../computations/alpha_em_permode_weight_probe.py) ·
**Tier:** scope-(a) — one route ruled out, the remainder reduced to a named open conjecture. No fit; not reverse-engineered to 8π.

## The question

PR #3831 established the **b₁ count** of the photon loop measure `1/(π·b₁)=1/(8π)`
as a bare topological integer (`ζ_Λ(0)=−b₁`). The identified next piece is the
**`1/π` per-mode weight** — the analog of the proved `1/(12π)` template's
geometric-identity factor. Spec §3's fitting-trap test governs it: *"the
ζ-determinant μ-dependence can absorb any constant; a derivation must force it."*

## Findings (all machine-verified exact)

**1. The flat ζ-determinant per-mode weight is NOT the source of `1/π` — fitting
trap confirmed.** `det'(−∂²)` on a circle S¹ of circumference `L` is exactly `L²`
(verified to 6.3e−30 for `L∈{1,2,π,2π}`): `ζ_{S¹}'(0)=−2ln L`, the `2π` cancels.
It is **scale-dependent and μ-absorbable, with no bare `1/π`**. So the naive
"per-mode weight = flat ζ-determinant" route is precisely the trap the spec
warned of — **ruled out (scope-(a))**. (`ζ_{S¹}(0)=−1`, consistent with the
b₁-count lead.)

**2. The proved `1/(12π)` template's π is topological — Gauss–Bonnet `2πχ`.**
`Area = −2πχ = 4π(g−1) = 12π` at g=4, and `2/(3π) = 8/(12π) = b₁/Area` (exact).
The π there is the **Euler-characteristic** `2π`, not a Gaussian/loop `2π`.

**3. The loop measure is `1/(8π) = 1/(π·b₁) = 1/(2π·g)`.** Its π, if topological,
needs a **`2π·g` (genus)** source — **distinct** from the template's
**`2π·χ = 4π(g−1)` (Euler-characteristic)** source. So `1/(8π)` is *not* the same
geometric identity as `2/(3π)`; a fresh `2πg` identification is required.

## Conclusion (honest scope)

The `1/π` per-mode weight **does not close by ζ-determinant bookkeeping**: the
flat per-mode determinant gives `L²` (the fitting trap), and a μ-independent
`1/π` must be topological. The framework's canonical μ-independent π is the
**archimedean dilogarithm regulator** — Bloch–Suslin pentagon-uniqueness forcing
the Bloch–Wigner `D`
([`conj:dilogarithm-archimedean-limit`](../../content/quantum-observable-universe/predicted-spectra/em-coupling-bring-zero-mode.md);
`alpha-em-derivation-open-problems.md`).

So closing `1/(8π)` **reduces to** that named open conjecture **plus** an explicit
**`2π·g` (genus, not Euler-χ) identity on Bring's surface**. The b₁ count
(PR #3831) is topological; the `1/π` per-mode weight is *not* forced by the
ζ-determinant alone. This confirms the spec's own warning and localizes the
remaining α_EM-measure work to two precise items:

1. the explicit Bloch-group class on Bring realizing the archimedean `1/π`
   (already the open item in `alpha-em-derivation-open-problems.md`);
2. a `2π·g` geometric identity for the loop measure, distinct from the
   `2π·χ` area of the proved weight-1 correction.

## Cross-references

- b₁-count lead: `2026-07-17-alpha-em-zeta-anomaly-b1-structural-lead.md` (PR #3831).
- Proved template + open dilog conjecture: `em-coupling-bring-zero-mode.md`, `alpha-em-derivation-open-problems.md`.
- Spec / reassessment: `2026-07-17-three-front-attack-specs.md §3`, `2026-07-17-1ppq-path-reassessment.md`.
- Ledger: `docs/coordination/alpha-em.md`.
