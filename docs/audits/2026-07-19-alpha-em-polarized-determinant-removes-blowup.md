# α_EM: polarization removes the genus-4 blow-up (measure → 8.226), but the classical η is insufficient — the q-holomorphic determinant is the next object

**Date:** 2026-07-19 · **Axis:** α_EM 2-loop / 1ppQ (#3612, magnitude leg) · **Tier:**
numerical scope-(a) · **Discipline:** no fit, no c_k wired, nothing to production, no
tier change.

## Setup

The merged genus-4 Epstein result (#3934) found the **unpolarized** real Laplacian
determinant on `Jac(Bring) = E_{5τ₀}³ × E_{τ₀}` does **not** factorize (spectrum
`{λ+μ}`), and its near-degenerate `E_{τ₀}` block (`Im τ₀ = 0.187`) collapses `det′Δ`,
blowing the boson measure up to `~1.47·10¹²`. The #3941/#3949 coordination hint: the
α_EM per-loop `1/(8π)` needs a **fibre-level / compact-real-form** (`U_q(su(2))`
`*`-structure) **polarized** projection.

## Result — polarization removes the blow-up, but 8.226 ≠ a clean coefficient

[`alpha_em_polarized_determinant_removes_blowup_probe.py`](../../computations/alpha_em/alpha_em_polarized_determinant_removes_blowup_probe.py):
on the diagonal isogeny period `diag(5τ₀,5τ₀,5τ₀,τ₀)` the **polarized (holomorphic)**
determinant **factorizes** — it is exactly the product `m1(5τ₀)³·m1(τ₀)` that the
genus-4 work had "retracted" for the *wrong* (unpolarized) reason:

> polarized measure = `m1(5τ₀)³·m1(τ₀) = 8.2263`  (O(1), vs unpolarized `1.47·10¹²`).

So **polarization is essential** (confirms #3941) and the polarized object is the
factorized holomorphic measure. **But** `8.2263` is **not** a clean α_EM coefficient:
nearest simple candidate is `b₁ = 8` (`measure/8 = 1.028`, **2.8 % off**); it is **not**
`8π` (`measure/8π = 0.327`), `4π`, `2π`, or `π²`. Polarization fixes the **scale**; a
residual normalization (the compact-`*` projection / #3941's "½·a₀") is unaccounted.

## The next object — the q-holomorphic determinant

The computation above used the **classical** (`q=1`) Dedekind `η`. The #3941/#3949 hint
is explicitly **fibre-level (complex q)**, so the operative object is the
**q-holomorphic determinant**: the modular `η` replaced by its **q-deformed** (Faddeev
`Φ_b` / quantum-dilogarithm) version at the substrate `q₀`. That is where the
`q₀`-dependence — and plausibly the missing normalization to `8π` — enters. The
classical result is the baseline that says: *polarization removes the blow-up, but the
classical η is insufficient; the deformation matters.* Pursuing the q-holomorphic
determinant needs the corpus's `Φ_b` machinery (`FaddeevPhiBRealIntegral`, the phiB
probes) and overlaps the active τ-functor front (#3941/#3949, tau-functor scaffold on
main) — coordinate there.

## Scope (anti-laundering)

Identifies the polarized determinant + shows it removes the blow-up; reports the
residual normalization gap honestly; flags the q-holomorphic determinant as the next
object. Does **not** manufacture `8π`. No fit; no c_k; no tier change.

## Cross-references

- Genus-4 Epstein det′Δ (unpolarized, 1.47e12): merged #3934, `bring_genus4_epstein_theta_factorized_probe.py`
- Non-separability (8π not the bare determinant): `2026-07-18-alpha-em-perloop-reciprocal-form-forcedness.md`
- Fibre-level / compact-`*` hint: #3941 (`conj = swap∘R`), #3949 (compact real form)
- q-deformed modular machinery: `FaddeevPhiBRealIntegral.lean`, the phiB probes; τ-functor scaffold (main)
