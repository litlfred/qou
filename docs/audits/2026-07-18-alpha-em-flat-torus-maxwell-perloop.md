# α_EM per-loop measure: flat-torus Maxwell 1-loop partition function — deriving the π and the reciprocal

**Date:** 2026-07-18 · **Axis:** α_EM per-loop measure · **Tier:** measurement
(scope-(a); no `α_k` wired; no fit; `1/(8π)` stays an identification until
genuinely derived) · **Branch:** `claude/alpha-em-perloop-flat-torus-maxwell-2026-07-18`.

## The residual wall (post-Front-3)

The Front-3 lead landed (#3834): `ζ_{Δ₁}(0) = −b₁ = −8`, exactly and **area-free**
— the canonical home of the bare mode-count. And `D = 8` is uniquely
data-selected to ~3500σ (`2026-07-17-alpha-em-perloop-integer-forcedness.md`).
Two pieces of the per-loop measure `1/(π·b₁) = 1/(8π)` remain **OPEN** (the
ζ(0) probe's own "not derived" list):

1. the **bare π**, and
2. the **reciprocal** form `1/(π·b₁)` — the full determinant + per-mode weight,
   not `ζ(0)` alone.

Both live on the photon target `J(M) = H¹/H¹(ℤ) = T^{b₁}` (`Jac(Bring) ~ E⁴`,
`b₁ = 8`). The derived surface zero-mode measure `1/(12π) = b₁/Area`
(Lean `PhotonIRZeroMode`, Gauss–Bonnet) is the template.

## Approach (STRICT — anti-laundering)

Compute the **flat-torus Maxwell 1-loop partition function** `Z_Maxwell(T^{b₁})`
independently — the harmonic-1-form moduli Gaussian measure × `det'Δ₁^{-1/2}`,
ζ-regularized (reusing the Epstein-zeta machinery of the #3834 probe) — and
**measure** which power of π and which b₁-dependence the standard photon path
integral produces. Then **compare** to `1/(π·b₁)`. The value is never solved
from CODATA; `D = 8` is not tuned.

## Results (probe [`alpha_em_flat_torus_maxwell_perloop_probe.py`](../../computations/alpha_em/alpha_em_flat_torus_maxwell_perloop_probe.py), witness [`alpha-em-flat-torus-maxwell-perloop.witness.json`](../../computations/alpha_em/alpha-em-flat-torus-maxwell-perloop.witness.json))

<!-- RESULTS -->

The standard abelian-gauge 1-loop partition function on the flat torus `T^d = ℝ^d/Λ`
(Ray–Singer / Schwarz resolvent form), with the FP ghost in Feynman gauge, is

$$
  Z_{\mathrm{Maxwell}}(T^d) = \mathrm{Vol}\big(J(M)\big)\cdot
  (2\pi)^{\frac12 \zeta_{\Delta_1}(0)}\cdot(\det{}'\Delta_1)^{-1/2}\cdot
  (\det{}'\Delta_0)^{+1},
$$

with `J(M) = H¹(M;ℝ)/H¹(M;ℤ) = T^{b₁}` the flat-connection moduli (Jacobian).
Since the torus is parallelizable, `Δ₁ = Δ₀ ⊗ Id` (`b₁` decoupled scalar copies),
so `ζ_{Δ₁}(s) = d·E_Λ(s)` with `E_Λ` the scalar Epstein zeta — **reused verbatim
from the #3834 probe** (the zeta is not reimplemented).

**Controls (both pass, all `d`).** `ζ_{Δ₁}(0) = d·E_Λ(0) = −b₁` reproduced for
`d = 1,2,3,8` (`|err| < 9e−8`); the single-mode Gaussian bookkeeping
`∫da e^{−½λa²} = (2π)^{½}·λ^{−½}` is exact to `< 1e−20` for `λ = 0.5, 1, 3.7`.

**Extracted, independently of any α data:**

| axis | flat-torus Maxwell produces | target `1/(π·b₁)` wants | match |
|---|---|---|---|
| **(a) π-power** | `½·ζ_{Δ₁}(0) = −b₁/2 = −4` (each mode one real Gaussian ⇒ one `(2π)^{½}`), plus a companion `2^{−b₁/2}` (the measure is `2π`, not `π`) | `π^{−1}` — power exactly `−1` | ✗ |
| **(b) `b₁`-dependence** | `b₁` in the **exponent** — exponential `(2π)^{−b₁/2}` | reciprocal `b₁^{−1}` | ✗ |
| **(c) area / covolume** | zero-mode `Vol(J(T^d)) ∝ L^{d(d−2)/2}` under `Λ → LΛ` (exponent `24` at `d=8`; verified numerically at `L = 1, 2`) | area-free (as `ζ_{Δ₁}(0) = −b₁` is) | ✗ |

The eigenvalue normalization `λ_k = 4π²·|k|²` supplies a *second* π-source, also
`∝ b₁` (via `(det'Δ₁)^{−1/2}`), so **every** π in `Z_Maxwell` enters to a power
**linear in `b₁`**, never the reciprocal `π^{−1}·b₁^{−1}`.

## Verdict — scope-(a) NEGATIVE

The flat-torus Maxwell 1-loop partition function **does not** produce the per-loop
measure `1/(π·b₁)`. It produces the Gaussian bookkeeping `(2π)^{−b₁/2}` times a
covolume-dependent moduli volume. The three named failing factors, matching the
pre-stated kill criteria exactly:

1. **π-power `= b₁/2 = 4 ≠ 1`** — from the `2π`-per-mode Gaussian bookkeeping
   (and a spurious `2^{−b₁/2}`).
2. **`b₁` appears exponentially**, not reciprocally as `1/b₁`.
3. **Covolume dependence survives** in `Vol(J(T^{b₁}))` — removable only by a
   *normalization choice*, which is precisely the forbidden fitting trap; no
   convention was stretched to manufacture `8π`.

**This is a real, redirecting result** (per the stub's anticipated outcome and the
Front-3 lead's own "residual wall" list). The per-loop measure is **not** the naive
Maxwell partition function on the photon target `T^{b₁}`: the reciprocal-in-`b₁`,
single-`π`, area-free `1/(π·b₁)` must come from a **different normalization object**
than `Z_Maxwell(T^{b₁})`. The #3834 area-free *numerator* count `ζ_{Δ₁}(0) = −b₁`
is untouched — only the MEASURE claim fails. No `α_k` wired; no fit; no tier
change; `1/(8π)` stays a phase-4 identification.


## Kill criteria (pre-stated)

- **Negative** if the partition-function measure carries area / covolume
  dependence, or a π-power ≠ 1, or a b₁-dependence that is not the reciprocal —
  report scope-(a) negative, do NOT stretch normalization conventions to
  manufacture `8π` (the spec's fitting trap).
- **Positive-partial** only if the `π^{-1}` and the reciprocal-in-b₁ emerge
  from the path-integral normalization independently of CODATA.

## Cross-references

- Front-3 lead: [`2026-07-17-alpha-em-zeta-anomaly-b1-count.md`](2026-07-17-alpha-em-zeta-anomaly-b1-count.md)
- Forcedness: [`2026-07-17-alpha-em-perloop-integer-forcedness.md`](2026-07-17-alpha-em-perloop-integer-forcedness.md)
- Wall map: [`2026-07-14-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md)
- Ledger: [`alpha-em.md`](../coordination/alpha-em.md)
