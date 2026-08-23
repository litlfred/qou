# α_EM polarized photon determinant — Epstein `det'Δ` machinery + retraction of the "8.226" product

**Date:** 2026-07-18 · **Axis:** α_EM single wall (`1/(π b₁)`), polarized magnitude leg ·
**Tier:** structural-exact machinery (genus-1 EXACT validation) + scope-(a) genus-2 finding ·
**No q₀, no 8π, nothing wired, no tier change.** A self-correction of the earlier #3864 update.

Probe [`bring_polarized_epstein_determinant_probe.py`](../../computations/alpha_em/bring_polarized_epstein_determinant_probe.py)
→ [witness](../../computations/alpha_em/bring-polarized-epstein-determinant.witness.json) (3/3).

## The machinery (validated)

The polarized magnitude leg is the boson 1-loop measure `√Vol(J)/√det'Δ` on the Bring
Jacobian torus `T^{2g}=R^{2g}/Λ`. `det'Δ` is computed from the Epstein `ζ'(0)`
(Chowla–Selberg / heat-kernel analytic continuation):

```
Z_H(s) = Σ'_{m∈Z^n}(m^T H m)^{-s},   det'Δ = (4π²)^{-1} exp(-Z'_{G^{-1}}(0)),  G = P^T P,
Z'_H(0) = -ln π - γ - (2/n)·det(H)^{-1/2}
          + ∫_1^∞ t^{-1}(θ_H(t)-1) dt + det(H)^{-1/2} ∫_1^∞ u^{n/2-1}(θ_{H^{-1}}(u)-1) du,
θ_H(t) = Σ_{m∈Z^n} e^{-π t m^T H m}.
```

**Genus-1 validation (EXACT).** For `T² = C/(Z+τZ)` the machinery returns
`det'Δ = (Im τ)²|η(τ)|⁴` and `measure = 1/(√Im τ·|η(τ)|²)` to machine precision — exactly
the per-factor form used in #3864. This anchors trust in the higher-genus output.

## The finding — the naive product is the wrong object

Applying the *same* machinery at genus 2:

| object | value |
|---|---|
| `measure(E_{5τ₀} × E_{τ₀})` (genus-2 Epstein, R=3,4,5) | 3.814 → 3.928 → **3.944** (converging up) |
| naive product `m(5τ₀)·m(τ₀)` | **2.922** |
| **ratio** | **≈ 1.35 ≠ 1** |

The torus boson measure is **not** the product of per-`T²` factors — the Laplacian spectrum
on a product torus is `{λ_i + μ_j}` (sums), not a product, so the zeta functions do not
factor. **Consequence:** the #3864 (2026-07-18) per-factor product
`m(5τ₀)³·m(τ₀) ≈ 8.226` is **the wrong object** for the polarized photon determinant and is
**retracted as the magnitude value**. (This makes the `8.226 ≈ b₁=8` proximity doubly a
non-result — it was never the right quantity; #3864 already refused to interpret it.)

## What stands, and what is deferred

- **Stands:** the Epstein `det'Δ` machinery (genus-1 exact), the structural facts from the
  merged #3864 (`Jac(Bring) ≅ E_{5τ₀}³×E_{τ₀}`, `det(M)=125`, `spec(M)={1,5,5,5}`), and the
  genus-1 anchor. The genuine polarized magnitude leg **is** the full genus-4 Epstein `det'Δ`
  on `Jac(Bring)` with period `τ₀·M`.
- **Deferred (numerical):** the genus-4 value itself. The thin Bring modulus (`Im τ₀ = 0.187`)
  makes the 8-dim dual-lattice `θ` converge slowly and the naïve `Z^8` truncation OOM at
  `R≥5`; a clean value needs **Siegel reduction** of `τ₀·M` to the fundamental domain first
  (a well-posed but non-trivial step). No number is claimed rather than a wrong one.
  - **LLL update (2026-07-18):** LLL-reducing the two quadratic forms (relabel the θ-sum by
    `U∈GL(n,Z)`) **converges the genus-2 measure fast** — `E_{5τ₀}×E_{τ₀} → 3.949` (R=2,3,4:
    3.934, 3.949, 3.949), tightening the R=5 value 3.944 and confirming `≠` the product 2.922.
    But LLL fixes only the lattice *shape*; it does **not** raise the genuinely thin `τ₀` factor
    (`Im=0.187`, deep in the cusp), so the **genus-4** truncation still diverges (garbage
    product-form values at small `R`). The genus-4 value therefore genuinely needs the Siegel
    **`S`-transform** (`τ→−1/τ`, raising `Im`), not just `GL(n,Z)` LLL — confirming the deferral.
    No genus-4 number is published.

## Scope guard (STRICT)

- **Self-correction, not a closure.** Retracts the #3864 "8.226" magnitude value; the wall is
  not closed. The reciprocal `π` remains RT/Front-2 (and the `D(ζ)=8` shared-wall is falsified,
  `677b74277`/#3871).
- **No q₀, no 8π manufactured, nothing wired, no tier change.** Pure scope-(a) — a validated
  method + an honest retraction.

## Cross-references

- Superseded value: [`2026-07-18-bring-s4-elliptic-factor-genus-and-period-block.md`](2026-07-18-bring-s4-elliptic-factor-genus-and-period-block.md) (the 8.226 product, now retracted as the magnitude)
- Structure + period: Braden–Disney-Hogg arXiv:2208.13692 Thm 2.12 + Prop 4.6 (`library/arxiv-2208.13692v1/2208.13692v1.pdf`)
- The reduction this serves: `2026-07-17-alpha-em-kronecker-elliptic-determinant.md` (#3864, merged)
