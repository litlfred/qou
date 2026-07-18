# α_EM B2 lift — period-side q-deformation: structured null (2026-07-18)

**Bean:** `qou-tq20`, tranche 5 — the next falsifiable comparison after
consistency-1 ([#4019](https://github.com/litlfred/qou/pull/4019)), using the
θ-machinery of the #3934 front (per-factor 2-D lattice thetas of the isogeny
blocks, `τ₀ = −0.5 + 0.186676i`).

**Probe:** [`computations/alpha_em/alpha_em_period_qdeformation_probe.py`](../../computations/alpha_em/alpha_em_period_qdeformation_probe.py)
→ [`alpha-em-period-qdeformation.witness.json`](../../computations/alpha_em/alpha-em-period-qdeformation.witness.json)
— 4/4 PASS (exact Markov ratio + 40-dps θ numerics; decision rules
pre-stated).

**Scope guard (STRICT):** pre-stated candidates only, no post-hoc scoring;
no fit; nothing wired; `1/(8π)` stays phase-4.

## The check and its formalize-first pruning

The identification predicts the geometric side deforms the (3,1) isotypic
weights along the Markov ratio `r(q) = y_[2]/y_[1,1]`. The canonical
geometric deformation is the heat family
`R_geo(t) = 3·θ_{G(5τ₀)⁻¹}(t)/θ_{G(τ₀)⁻¹}(t)`.

**Pruning (pre-stated):** matching two monotone one-parameter curves under a
free reparameterization `t(q)` is vacuous. The dictionary-independent
content is only (i) the endpoints and (ii) whether the categorical image of
the geometric endpoint is a *distinguished* constant.

## Results

- **Endpoints exact** (V1/V2): `R_geo` spans `[3, 15]` — `3` at t→∞
  (factor multiplicities; the consistency-1 anchor) and
  `15 = 3·(Im 5τ₀/Im τ₀)` at t→0 (area ratio 5, canonical via the isogeny-
  block Grams); monotone. The Markov family covers the same range on
  `[q₁₅, 1]` with `r(1) = 3` exact.
- **Dictionary endpoint** (V3): `r(q₁₅) = 15` at
  `q₁₅ = 0.6255624478797316675325509…` (30-dps root of the exact ratio).
- **Distinguished-candidate test → NULL** (V4): against the pre-stated list
  {`1/q₀`, `|nome(τ₀)|`, `|nome(τ₀)|^{1/5}`, `1/√5`, `e^{−2π/5}`, `1/φ`,
  `1/φ²`, `1/5`} at exact-grade tolerance 1e-6: **no match** — nearest is
  `1/φ` at 1.22% relative, a clean miss for exact quantities. Recorded, not
  scored (post-hoc observation): `r(1/q₀) ≈ 4.0072`.

## Honest reading

The endpoint-to-distinguished-constant dictionaries are **killed**
(scope-(a)). The identification is **neither refuted nor doubly confirmed**:
the true dictionary, if any, need not send the t→0 endpoint to a
distinguished q — but it gains no second consistency point here. The
τ-identification remains **open and dictionary-gated**: pinning the
framework's actual `q ↔ heat-time` dictionary (a categorical input, not a
numerical one) is now clearly the load-bearing step, ahead of any further
numerics.

## Position

```
qou-tq20: #3985 interface → #3992 ℂ-model → #3999 constructor →
          #4019 consistency-1 (PASS) → THIS deformation check (STRUCTURED NULL)
Wall: the τ-identification — now sharpened to "pin the q↔t dictionary first;
further numerics are vacuous without it" (formalize-first).
```
