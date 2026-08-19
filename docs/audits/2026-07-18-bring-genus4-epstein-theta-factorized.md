# Genus-4 Epstein det′Δ on Jac(Bring) — the deferred α_EM magnitude value, via θ-factorization

**Date:** 2026-07-18 · **Axis:** α_EM 2-loop / 1ppQ (#3612, magnitude leg #3911) ·
**Tier:** structural-exact machinery (genus-1 EXACT + genus-2 sibling cross-check),
plus a scope-(a) computed magnitude value · **Discipline:** no fit (nothing tuned to
CODATA), no c_k, nothing wired, no tier change.

## What was deferred

The sibling probe
[`bring_polarized_epstein_determinant_probe.py`](../../computations/alpha_em/bring_polarized_epstein_determinant_probe.py)
([audit](2026-07-18-bring-polarized-epstein-determinant.md)) validated the genus-`g`
Epstein det′Δ machinery on genus 1 (reproduces `(Im τ)²|η|⁴` exactly) and corrected
the naive per-factor product framing (genus-2 measure ≈ 3.949 ≠ the naive product
2.922), but **deferred the genus-4 value itself**: its full 8-dimensional θ-grid
`_pts(8,R)` OOMs at `R≥5`, and the thin Bring modulus (`Im τ₀ = 0.187`) was said to
need Siegel reduction of `τ₀·M` to the fundamental domain first.

## The fix — factorize the θ-function, not the determinant

`Jac(Bring)` in its isogeny basis has a **block-diagonal** period
`diag(5τ₀, 5τ₀, 5τ₀, τ₀)` (`M` is `O(4)`-equivalent to `diag(5,5,5,1)`, `det M = 125`,
`spec{1,5,5,5}` — Braden–Disney-Hogg, 2208.13692). So the direct-sum lattice's
heat-kernel θ **factorizes exactly**,

    θ_H(t) = θ_{G(5τ₀)}(t)³ · θ_{G(τ₀)}(t),

each factor a cheap 2-D lattice θ that converges at small radius for `t ≥ 1`. The
Epstein `det′Δ` does **not** factorize (its spectrum is `{λ_i + μ_j}` sums, not a
product — the sibling's correct genus-2 finding), but it is computed *from* the
product-θ via the same Chowla–Selberg `ζ′(0)` split. **No 8-dim grid, no OOM, no
Siegel reduction needed** — the block-diagonal structure that makes the naive
product wrong is exactly what makes the θ (and hence the honest det′Δ) cheap.

The one arithmetic subtlety the first draft got wrong: the flat-torus Laplacian
spectrum is `4π²·(mᵀ G⁻¹ m)`, so the Epstein form is the **dual** `H = G⁻¹`, not the
Gram `G` (mirrors the sibling's `_zeta_prime0(inv(G), …)`). For a block-diagonal `G`
the dual is block-diagonal too, `G⁻¹ = blockdiag(Gᵢ⁻¹)`, so both θ's still
factorize: `θ_{G⁻¹}(t) = ∏ θ_{Gᵢ⁻¹}(t)`, `θ_G(u) = ∏ θ_{Gᵢ}(u)`.

## Result

[`bring_genus4_epstein_theta_factorized_probe.py`](../../computations/alpha_em/bring_genus4_epstein_theta_factorized_probe.py)
(witness `bring-genus4-epstein-theta-factorized.witness.json`):

| Genus | quantity | value | check |
|---|---|---|---|
| 1 | det′Δ vs `(Im τ)²·‖η‖⁴` | `0.4525101839` = `0.4525101839` | **exact** |
| 1 | measure vs `1/(√Im τ·‖η‖²)` | `1.758935196` = `1.758935196` | **exact** |
| 2 | measure `E_{5τ₀}×E_{τ₀}` | **`3.949374523`** | matches sibling `≈ 3.949` |
| **4** | **det′Δ(Jac Bring)** | **`7.00187969·10⁻²⁶`** | R-stable (see below) |
| **4** | **boson measure** | **`1.472396·10¹²`** | R-stable (see below) |

The genus-2 value `3.949374523` is the *converged* (`R = 20`) figure; the sibling's
`3.949` was an under-converged `R = 5` truncation still climbing — they agree, which
double-validates both the sibling machinery and the θ-factorization.

**Convergence + discrepancy resolution.** An early draft of this probe reported
`det′Δ ≈ 0.00446`, `measure ≈ 5.83`. That was a **bug**: it fed the Gram `G`
directly into the Epstein zeta, but the flat-torus Laplacian spectrum is
`4π²·(mᵀ G⁻¹ m)`, so the Epstein form is the **dual** `H = G⁻¹`. The corrected code
(mirroring the sibling's `_zeta_prime0(inv(G), …)`) passes genus-1 exactly and
genus-2 against the sibling grid, and gives the values above. The genus-4 figure is
**R-stable** (factorized θ, `dps = 25`): `R = 4 → 7.146·10⁻²⁶`, `R = 8 → 7.0019·10⁻²⁶`,
`R = 12 → 7.00188·10⁻²⁶` (5 sig figs by `R = 8`), so it is a genuine converged value,
not a truncation artifact.

## The honest anti-laundering reading (the important part)

The deferred genus-4 boson measure is **`≈ 1.47·10¹²`** (det′Δ `≈ 7.0·10⁻²⁶`). It is:

- **not** `8π ≈ 25.13` (`measure/8π = 5.86·10¹⁰`),
- **not** `8 = b₁` (`measure/8 = 1.84·10¹¹`),
- **not** the retracted naive product `8.226` (`measure/naive = 1.79·10¹¹`),
- **not** `4π` or `π²` — it is ~10 orders of magnitude larger than all of them.

So the raw *unpolarized* genus-4 Epstein magnitude on `Jac(Bring)` **does not
manufacture the α_EM `8π`** — it overshoots by ~10¹⁰. The near-degenerate `E_{τ₀}`
block (thin modulus `Im τ₀ = 0.187`, Gram eigenvalue `λ_min ≈ 0.028`) drives det′Δ
to `≈ 7·10⁻²⁶`, blowing the bare boson measure up to `10¹²`. This is a **useful
negative for #3911**: the bare unpolarized Epstein determinant is *not* the right
object — the polarization / projection that removes or reweights the near-zero modes
is essential, and no naive normalization of the raw determinant reaches `8π`.

It is fully consistent with — and independent confirmation of — the merged
non-separability finding
([`2026-07-18-alpha-em-perloop-reciprocal-form-forcedness.md`](2026-07-18-alpha-em-perloop-reciprocal-form-forcedness.md),
#3918): the `8π` is **not** the bare determinant, nor a naive-mode-count, so it
cannot be read off arithmetically from either leg alone. The magnitude leg now has
an actual converged number, not a deferral — and that number, honestly reported, is
emphatically *not* the coefficient. No `8π` is fabricated here.

## Scope

Computes the previously-deferred magnitude value with genus-1/genus-2-validated,
R-converged machinery. Makes **no** claim that `1.47·10¹²` (or `7·10⁻²⁶`) equals
`8`, `8π`, or any α_EM coefficient — the opposite: it shows the raw determinant is
~10¹⁰ off, so the polarization matters. No `q₀`; no fit; nothing wired; no tier
change. The result is a data point for the sibling #3911 magnitude-leg computation —
it closes the "value deferred / needs Siegel reduction" gap and shows the honest raw
number is not the coefficient.

## Cross-references

- Deferred-by / machinery: [`2026-07-18-bring-polarized-epstein-determinant.md`](2026-07-18-bring-polarized-epstein-determinant.md) (#3911)
- Non-separability (why 8π isn't arithmetically recoverable): [`2026-07-18-alpha-em-perloop-reciprocal-form-forcedness.md`](2026-07-18-alpha-em-perloop-reciprocal-form-forcedness.md) (#3918)
- Settled ingredients: [`2026-07-18-alpha-em-pi-origin-adjudication.md`](2026-07-18-alpha-em-pi-origin-adjudication.md) (`1/(4π)`, #3909); `b₁ = 2g = 8` (#3896)
- Action plan: [`2026-07-18-1ppq-action-plan.md`](2026-07-18-1ppq-action-plan.md)
- Jac structure: `Jac(Bring) ≅ E_{5τ₀}³ × E_{τ₀}`, `det M = 125` (Braden–Disney-Hogg, `library/arxiv-2208.13692v1/2208.13692v1.pdf`)
