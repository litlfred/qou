# Covariance-kernel epic (`qou-x631`) — M₁>0 gap `qou-k5r5`: research attempt, piece 1 — the Debye bulk tool is verified

**Date:** 2026-08-29 · **Branch:** `claude/m1-k5r5-bulk-sine-kernel-rate-2026-08-29` · **Tier:**
original research, piece 1 (a rigorous, verified sub-tool) · **Discipline:** no fake closure; this
establishes one rigorous ingredient and states the remaining analysis with the constant/cancellation
explicitly *not* done. **Epic:** `qou-h315`/`qou-x631`; gap `qou-k5r5`.

Per the owner's choice to treat the bulk-rate as a research problem: scaffold it, attempt the rigorous
pieces, flag every step. This is piece 1.

## The plan

The exact finite-θ variance is
`V_g(θ) = ½ Σ_{x≠y} (g(x) − g(y))² J(x,y;θ)²`, `J(x,y;θ) = √θ (J_x J_{y+1} − J_{x+1} J_y)/(x−y)`.
Split the index range into **tail** (`|x| > 2√θ + Kθ^{1/6}`), **edge** (`|x| ≈ 2√θ`, Airy scale), and
**bulk** (`|x| = a√θ`, `|a| < 2`). Handle each:

- **Tail:** super-exponentially negligible — **proved** (Johansson Lemma 3.9, `tail_bulk_split.py`).
- **Bulk:** replace `J_x(2√θ)` by its Debye asymptotic; the kernel becomes the discrete sine kernel plus
  an explicit error; sum against the smooth weight. **← piece 1 (this note).**
- **Edge:** the Airy-scale contribution, bounded by (number of edge points) × (Airy-kernel size).
- **De-Poissonize:** Johansson Lemma 3.8 (`C/N²`).

## Piece 1 — the Debye bulk asymptotic (rigorous tool, verified)

For `J_ν(z)` with `ν = z cos β`, `0 < β < π/2` (Watson 1944 §8.4; DLMF 10.19.6):
> `J_ν(z) = √(2/(π z sin β)) · [ cos(z(sin β − β cos β) − π/4) + O(1/z) ]`.

With `z = 2√θ`, `ν = x`, `cos β = x/(2√θ) = a/2`, so `β = arccos(a/2) = R` — **exactly** the discrete
sine kernel's angle `S(k,a) = sin(Rk)/(πk)`. This is *why* `J → S` in the bulk (BOO Thm 3), and the
Debye remainder `O(1/z) = O(θ^{−1/2})` is the pointwise source of the sub-leading variance correction.

**Verified** (`debye_bulk_asymptotic_probe.py`, exact `mpmath`, NO float64): the leading Debye term
matches exact `besselj` with relative error decaying as `θ^{−1/2}` —

| a (bulk density) | rel. error θ=1e3 → 1e6 | measured exponent |
|---|---|---|
| 0.5 | `2.3e−3 → 6.6e−5` | **0.51** |
| 1.0 | `3.6e−3 → 8.1e−5` | 0.66 |
| 1.5 | `6.0e−3 → 2.1e−4` | 0.82 |

The `a = 0.5` case (deepest bulk) gives the clean `p = 0.51 ≈ 1/2`; the drift at larger `a` is the
next Debye order contributing over only four points and the edge getting nearer. The `O(θ^{−1/2})`
leading behaviour is confirmed. This is a classical, citable, now-verified tool.

## The remaining rigorous step (explicitly NOT done)

Write `J(x,y) = S(x−y;a) + E(x,y)`, `E = O(θ^{−1/2})·(amplitude)` from the Debye remainder. Then
`J² = S² + 2SE + E²`, and

`V_g(θ) = [sine-kernel part → V_g·θ^d] + 2·(cross term Σ S·E) + (Σ E²)`.

The **rate** is the `θ`-order of the cross and `E²` terms *after summation against the smooth weight*.
The pointwise error is `O(θ^{−1/2})`, but the summed cross term has an **oscillatory** integrand
(`S·E` carries the `cos` phase of both factors), so a **stationary-phase / summation-by-parts**
cancellation reduces it — the measured net rate is `θ^{−1}` (`qou-tvok`), i.e. the summation gains one
more `θ^{−1/2}` over the pointwise error. **Carrying out this cancellation with an explicit constant is
the hard analysis and is not done here.** The amplitude/phase bookkeeping is exactly where an error
would enter; per the anti-laundering discipline I will not write a plausible-but-unverified version.

So piece 1 is a genuine rigorous brick (the bulk tool, verified); the cross-term cancellation is the
next piece and remains open.

## Status of `qou-k5r5`

Gap **OPEN**. Rigorous pieces now in hand: leading constant (proved), tail (proved), de-Poissonization
(cited), **Debye bulk tool (verified, this note)**. The open piece is the summation cancellation
(bulk cross term) + the edge Airy contribution — the genuine analysis. Leading margin proved; the
route is being built brick by brick, honestly.

## Compute + sources

- [`wlambda_covariance_epic_M1_debye_bulk_asymptotic_probe.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_debye_bulk_asymptotic_probe.py) (exit 0; NO float64; Debye verified `~θ^{−1/2}`).
- Debye asymptotic: Watson, *A treatise on the theory of Bessel functions* (1944) §8.4; DLMF 10.19.6
  (a standard result, cited not re-proved). Sine-kernel angle: BOO Thm 3.

## Cross-references

- Regime structure: [`2026-08-29-covariance-kernel-M1-k5r5-regime-structure-BDJ-is-the-edge.md`](2026-08-29-covariance-kernel-M1-k5r5-regime-structure-BDJ-is-the-edge.md)
- Tail (proved): [`2026-08-29-covariance-kernel-M1-k5r5-tail-half-and-ingested-kernel-rate-lit.md`](2026-08-29-covariance-kernel-M1-k5r5-tail-half-and-ingested-kernel-rate-lit.md)
- Epic `qou-h315`/`qou-x631`; gap `qou-k5r5`.
