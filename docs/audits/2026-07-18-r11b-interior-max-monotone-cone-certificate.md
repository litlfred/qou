# R11-b — Farkas certificate: the ladder-miss k=3 interior maximum is outside the monotone additive cone (the missing channel is non-monotone/resonant)

**Date:** 2026-07-18 · **Task:** R11-b (round-11; follows merged R11-a [#3840](https://github.com/litlfred/qou/pull/3840)) · **Bean:** `z2bn`
**Probe:** [`computations/deltalambda/r11b_interior_max_monotone_cone_certificate.py`](../../computations/deltalambda/r11b_interior_max_monotone_cone_certificate.py)
**Witness:** [`r11b-interior-max-monotone-cone-certificate.witness.json`](../../computations/deltalambda/r11b-interior-max-monotone-cone-certificate.witness.json) (allPassed; consumes merged R10 witness — no recompute)
**Discipline:** scope-**(b)** via explicit certificate (a proved invariant, not a numerical near-miss); no fit; magnitudes not interpreted.

## Result

R10 established the Model-G miss peaks at a **fixed interior k=3** on all three `(kα)+X` ladders
(X = n/d/t, A_light = 1/2/3). R11-a ([#3840](https://github.com/litlfred/qou/pull/3840)) refuted the
multiplicative closure and pure Brunnian hard-gate. R9 **asserted** the P1 prune ("a non-negative
additive cone has no strict interior maximum"). This note upgrades that assertion to an **explicit
Farkas certificate** on the merged 3-ladder data, and shows the exclusion is **scope-(b)**.

## The certificate (elementary, exact)

Let `B = {f_i(k)}` be **any** family of basis functions **non-decreasing in k**
(`f_i(k+1) ≥ f_i(k)`) — every additive structural count is of this form: `1`, the α-count `k`, the
pair count `C(k,2)`, the triple count `C(k,3)`, the core–α interface `k·A_light`, … . Take the
linear functional

$$
\varphi \;:=\; e_{k=4} - e_{k=3}, \qquad \varphi(f) = f(4)-f(3).
$$

For every non-decreasing `f_i`, `φ(f_i) ≥ 0`; hence for any non-negative combination
`g = Σ_i c_i f_i` (`c_i ≥ 0`), `φ(g) = Σ_i c_i(f_i(4)-f_i(3)) ≥ 0` — **every element of the monotone
cone is non-decreasing from k=3 to k=4**. But on the miss:

| A_light | miss(3) | miss(4) | φ(miss) = miss(4)−miss(3) |
|--:|--:|--:|--:|
| 1 (n) | 2.838 | 1.377 | **−1.461** |
| 2 (d) | 5.818 | 1.632 | **−4.186** |
| 3 (t) | 8.048 | 2.679 | **−5.369** |

`φ(miss) < 0` on all three ladders, so `φ` **separates** the miss from the cone:
`miss ∉ cone(non-decreasing structural counts)`. The pair `(k=3, k=4)` with the strict decrease is
the Farkas witness. This holds for the **whole** monotone additive class simultaneously (via the
proved invariant "monotone ⇒ φ ≥ 0"), so it is a **scope-(b)** structural exclusion — not a fit to a
particular basis.

**⇒ the missing binding channel is necessarily NON-monotone in k — a genuine resonance** (interior
peak), consistent with and now certifying R9's P1/P2 prunes.

## The fall is not a separable parity factor either

#3808 floated a separable "bar-parity fall" as the third factor. The fall ratio `miss(4)/miss(3)` is
**0.485 / 0.281 / 0.333** across A_light = 1/2/3 (spread 1.73×) — **A_light-dependent**, so the fall
does not factor out of A_light. Combined with R11-a's A_light-dependent k=2 envelope, the miss is
**irreducibly 2D** in `(k, A_light)`: no product, no additive-monotone sum, and no separable parity
factor reproduces it.

## Redirect (formalize-first)

- **Lean target (R11-b proper):** the order lemma "a non-negative combination of non-decreasing
  functions is non-decreasing, hence has no strict interior maximum" — the certificate above, ready
  to formalize.
- **Closure route:** closed-form k-envelopes are excluded; the per-isotope binding closure belongs
  to the **operator-valued branching combiner / confinement SDP** (the mandated route), where a
  resonant (non-monotone) k-profile is natural. No fit; scope-(b) via explicit certificate.
