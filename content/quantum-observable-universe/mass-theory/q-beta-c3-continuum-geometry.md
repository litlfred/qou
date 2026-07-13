---
title: "The c_3 Mass Gap and Continuum Hyperbolic Geometry"
date: "2026-07-07"
tags: ["mass-theory", "q-beta", "continuum-limit", "hyperbolic-volume", "faddeev"]
---

# The Geometric Origin of the c_3 Mass Gap

> **⚠ CORRECTION (2026-07-11) — the `c_3 → −Vol(4₁)` identification is over-scoped.**
> `−Vol(4₁) ≈ −2.02988` is **anchor-blind** and misses **both** substrate anchors
> (muon **+0.479%**, proton **−1.907%**) while the actual $c_3$ **swings 2.43%**
> (muon −2.0202, proton −2.0693); at the muon (CAL-2) pin it is **6.9× worse**
> than the keystone's own `−Vol(4₁)+u−(10/3)u²` near-match. So the "continuum
> limit is exactly −Vol(4₁), rigorously banishing all algebraic truncations"
> claim is **not** supported — it makes the muon fit worse and fails cross-anchor
> (§8 guard). Moreover, `c_3 → −2 = J_Hopf(q=1)` is the **canonical** q=1 shadow
> (registry **KC10 / KC20** `C_Hopf(2)=−2`), **not** a "hallucination." The
> hyperbolic geometry below is real and kept (`Vol(4₁)=2·Cl₂(π/3)`, Lobachevsky
> saddle at `π/3`); only the $c_3$ **identification** and the "exact/rigorous"
> tier are corrected. Re-scope + measurement:
> [`2026-07-11-gemini-session-c3-overclaim-continuum-and-lean-audit.md`](../../../docs/audits/2026-07-11-gemini-session-c3-overclaim-continuum-and-lean-audit.md);
> companion keystone re-scope: `#3501`/`#3503`.

The third topological mass gap observable $c_3$ was initially measured via empirical extrapolation of the $N=3$ operator-valued calculations across the $Q_\beta$ manifold, resulting in a near-match physical measurement of:
$$ c_3^{\text{emp}} \approx -2.02162 $$

The canonical $q = 1$ shadow of this quantity is $J_{\text{Hopf}}(1) = -2$ (kernel-constraint registry KC10/KC20, $C_{\text{Hopf}}(2) = -2$). The question addressed below is whether the residual gap between $c_3^{\text{emp}}$ and $-2$ admits a continuum-geometric description. (Combinatorial constraints proposed over $S_5$ cells did not survive audit.)

## The Continuum Limit Kashaev Integral

By transitioning to the full continuous Faddeev non-compact integration $\Phi_b(z)$ over the analytic contour $\mathbb{R} + i\delta$, the operator expansion is replaced entirely by the thermodynamic saddle point of the continuum potential. 

For the ground-state $4_1$ (figure-eight pion) topology, the non-compact potential transforms exactly into the imaginary part of the quantum dilogarithm:
$$ V(\theta) = \text{Im}(\text{Li}_2(e^{i\theta})) $$

## The Saddle Point Construction

The critical saddle point of the continuous action sits at $\theta = \pi/3$, where the potential evaluates to the volume of a regular ideal tetrahedron ($V(\pi/3) \approx 1.01494$) and the two-tetrahedron gluing of the $4_1$ complement gives the total macroscopic physical action $\text{Vol}(4_1) \approx 2.02988$; the saddle derivation is carried out once in [the dilog saddle regime](#rem:dilog-saddle-regime).

## The asymptotic bound (scope-limited)

The full non-perturbative Kashaev invariant (calculated via high-precision [Borel–Padé extrapolation](#def:ecalle-borel-resummation) across $N \in [1000, 2050]$) pins the topological action of the geometric envelope:
$$ A = \frac{\text{Vol}(4_1)}{\pi} \approx 0.6461318 $$

The candidate identification
$$ c_3 \xrightarrow{N \to \infty} -\text{Vol}(4_1) \approx -2.02988 $$
is **scope-limited, not exact**: $-\text{Vol}(4_1)$ is anchor-blind, missing both substrate anchors (muon $+0.479\%$, proton $-1.907\%$) while the measured $c_3$ itself swings $2.43\%$ across anchors (muon $-2.0202$, proton $-2.0693$); at the muon (CAL-2) pin it is $6.9\times$ worse than the keystone near-match $-\text{Vol}(4_1) + u - (10/3)\,u^2$. The residual between the observed $-2.0216$ and $-2.02988$ was previously attributed to finite-size truncation scaling; the cross-anchor swing shows the identification itself does not close.

What stands is the hyperbolic geometry: $\text{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$, with the Lobachevsky saddle at $\theta = \pi/3$, supplies the geometric envelope that anchor-sensitive corrections (the keystone ladder) refine — not a rigorous continuum evaluation of $c_3$.


