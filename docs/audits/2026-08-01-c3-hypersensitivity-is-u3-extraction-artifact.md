# c₃ "hypersensitivity" is the 1/u³ ladder-extraction amplification of a smooth numerator (2026-08-01)

**Axis:** Q_β c₃ bar-odd `S` — direction 4 (reconcile the [W]/singularity/
hypersensitivity pictures). **No c_k wired; no fit; registry untouched; no
`SDeformedVolumeChannel` instance fabricated.** This is a **diagnostic reframing** that
resolves the tension between the smooth argument-map radius (PR #4508) and the apparent
`dc₃/dq ≈ 10⁶` hypersensitivity — and reframes the `|S_p/S_m|` target.

## The tension this resolves

PR #4508 showed the figure-8 argument map `u(q₀)` (and `𝔙₄₁(u(q₀))`) is **smoothly
analytic**, radius `R = 2·log φ ≈ 0.962`, anchor at `0.108·R`. Yet the c₃ target is
empirically **hypersensitive** across the muon/proton anchor gap: `dc₃/dq ≈ 4×10⁶`
over a `1.28×10⁻⁸` pin difference produces the whole `S(muon)>0>S(proton)` flip. A
smooth geometric object cannot be hypersensitive. Where does the hypersensitivity
live?

## The answer: the `1/u³` in the c₃ extraction

The c₃ target is a **ladder inversion** (`qbeta_utils.c3_target_at`):

```
c₃ = (Q_codata / Q_N2(q) − 1) / u(q)³ ,   u = b·ℏ_q² ≈ 0.00852  ⇒  u³ ≈ 6.2×10⁻⁷ .
```

Write the numerator `g(q) = Q_codata/Q_N2(q) − 1`. Then `c₃ = g/u³` and
`S = c₃ + Vol(4₁)`. Measured across the anchor gap (`Δq ≈ 1.28×10⁻⁸`):

| quantity | value |
|---|---|
| `dg/dq` (smooth numerator) | `≈ 2.37` — **O(1), smooth** |
| `dc₃/dq` (amplified) | `≈ 3.84×10⁶` |
| `dc₃/dq ÷ dg/dq` | `1.6185×10⁶` |
| `1/u³` | `1.6185×10⁶` |

`dc₃/dq ÷ dg/dq = 1/u³` **exactly** (to 4 figures; the residual is the small
`−3g·u'/u⁴` term, tiny since `g ~ 10⁻⁶`). The entire hypersensitivity factor is `1/u³`
— the ladder-inversion divisor. The underlying numerator `g` is perfectly smooth.

Probe: [`qbeta_c3_hypersensitivity_u3_extraction_probe.py`](../../computations/qbeta/qbeta_c3_hypersensitivity_u3_extraction_probe.py)
(exit 0), witness
[`qbeta-c3-hypersensitivity-u3-extraction.witness.json`](../../computations/qbeta/qbeta-c3-hypersensitivity-u3-extraction.witness.json).

## What this means

**The `dc₃/dq ≈ 10⁶` hypersensitivity is an EXTRACTION artifact**, not a physical
near-singularity. It is the smooth numerator's O(1) variation divided by `u³ ≈ 6×10⁻⁷`.
This is exactly consistent with PR #4508: `u(q₀)`/`𝔙₄₁` are smooth (radius `0.962`);
there is no geometric hypersensitivity, and none is needed — the hypersensitivity lives
entirely in the `/u³` step of the c₃ *definition*.

Two consequences reframe the whole c₃ magnitude problem:

1. **The muon/proton SIGN FLIP of `S = c₃ + Vol(4₁)` is `c₃ = g/u³` crossing the
   threshold `−Vol(4₁)`.** `c₃(muon) = −2.0202 > −Vol(4₁) = −2.0299 > −2.0693 = c₃(proton)`.
   `g` varies smoothly by ~2.4% across the `10⁻⁸` gap; `/u³` turns that into
   `Δc₃ ≈ 0.049`, straddling `−Vol(4₁)`. **Neither an on-anchor singularity (#4508 ruled
   it out) nor a discrete winding change (the [W] reframe) is required** — the flip is a
   smooth threshold crossing, amplified.

2. **`|S_p/S_m| ≈ 4.075` is a ratio of two `1/u³`-amplified near-threshold residuals**
   `S = g/u³ + Vol(4₁)`, hypersensitive to the exact `10⁻⁸` pin difference. It is **not a
   fundamental geometric quantity.** This explains — from a single mechanism — why every
   parameter-free geometric route missed it: single canonical pair (#4497), multi-winding
   sum quadratic + full-`𝔙₄₁` (#4501/#4503), resurgent ratio (#4501). The target was
   never a clean geometric ratio; it is a near-cancellation extraction artifact. **The
   smooth object a geometric derivation should reproduce is `g(q)` (equivalently
   `Im 𝔙₄₁(u(q₀))`), not the amplified `|S_p/S_m|`.**

## Reconciliation of the three pictures (direction 4)

| picture | status after this + #4508 |
|---|---|
| on-anchor singularity / resurgence-at-anchor | **ruled out** (#4508: `R = 0.962`, smooth) |
| [W] discrete-winding change (muon↔proton) | **not needed, and mis-applied**: muon/proton is the *same* 4₁ at two q₀ pins differing by `10⁻⁸` — a continuous pin change, not a discrete winding change |
| smooth threshold crossing amplified by `1/u³` | **this is the mechanism** (this doc) |

The [W] winding-lattice arithmetic remains the right description of sign flips **across
different knots**; it was never the right frame for the **same-knot** muon/proton pin
flip, which is the `1/u³`-amplified threshold crossing above.

## What stays open (correctly reframed)

The genuine open object is the **smooth** numerator `g(q) = Q_codata/Q_N2(q) − 1`
(equivalently `Im 𝔙₄₁(u(q₀))` and its absolute normalization / the boost-enhancement
`A`). Reproducing `g` geometrically is the well-posed target; chasing the amplified
`|S_p/S_m| ≈ 4.075` is chasing an extraction artifact. This does not "close" the c₃
value — but it corrects the target of the search, which is a real advance.

-- Ref: [manuscript] docs/audits/2026-08-01-c3-uq0-radius-golden-ratio-on-anchor-singularity-refuted.md (#4508)
-- Ref: [manuscript] .beans/qou-iyj5 (single-structure survivor)
-- Ref: [manuscript] docs/coordination/udeform-spin-part-derivation.md ([W] reframe, scope)
-- Ref: [manuscript] docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md (qou-82w7)
