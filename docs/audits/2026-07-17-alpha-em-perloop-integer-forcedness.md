# α_EM per-loop measure: the integer 8 = dim H¹(Bring) is uniquely data-selected (forcedness measurement)

**Date:** 2026-07-17 · **Axis:** α_EM 2-loop / 1ppQ (#3612 headline) · **Tier:**
numerical (scope-(a) forcedness measurement — **NOT a derivation**) · **Discipline:**
no fit wired, no c_k, no tier change; the value is *solved from* CODATA, which is
the fit, not a derivation.

## Question

The α_EM ladder closes as the fixed point of `1/α = T + α·H`, with
`T = q[9]_q[10]_q + b₁/Area` (tree + zero-mode, both **derived**) and
`H = [2]_q/(π·D)`, `D` the per-loop-measure denominator. Every ingredient is
pinned except `D`: the phase-4 "identification" `D = dim H¹(M_Bring) = 2g = 8`
is an admitted **pattern match** (its own HONEST CAVEAT), and the 9500σ
falsification (`D = Area/π = 12` → −1419 ppb) shows the residual is
hypersensitive to `D`. Sharp question: **is `D = 8` *pinned* to the topological
integer (a precise coincidence a derivation must explain), or *loose*
numerology?**

## Method + result

Closed form: at the fixed point `1/α = C` (CODATA), the cubic `α²H + αT − 1 = 0`
gives `H* = C·(C − T)` exactly, hence the data-selected `D* = [2]_q/(π·H*)`.

| anchor | `D*` | `D* − 8` | 7 excluded | 8 (dim H¹) | 9 excluded |
|---|---|---|---|---|---|
| **proton** | **8.00314 ± 0.00029** | +0.0031 | 3484σ | 10.9σ | 3462σ |
| muon | 8.15408 ± 0.00030 | +0.154 | 3861σ | 515σ | 2830σ |

At the (precision) proton anchor, **`D = 8` is the uniquely data-selected integer**
— neighbours 7 and 9 are excluded at **~3500σ** — and it equals `dim H¹(Bring) =
2g = 8` **exactly**. The residual `|D* − 8| = 0.0031` (the 10.9σ offset) is the
still-underived **2-loop-and-higher tail** (consistent with the +1.67 ppb 1-loop
residual that the θ-graph 2-loop candidate brings to 1.3σ), **not** a free knob.
The muon anchor's larger offset (0.154) is the known substrate μ–p tension.

## What this does and does NOT establish

**Does:** the `1/(8π) = 1/(π·dim H¹)` identification is a **precise, uniquely
data-selected coincidence**, not the loose numerology a "1/(8π) happens to equal
1/(π·8)" reading might suggest. The topological integer is pinned to the 4th
decimal by CODATA. This *sharpens* the derivation target and raises the stakes.

**Does NOT (anti-laundering, STRICT):** `D*` is **solved from** CODATA — it is the
FIT. A small `|D* − 8|` is **not** a derivation of `1/(8π)`. The open target is
unchanged and well-posed: derive **per-loop measure = `1/(π·dim H¹)`** from the
RT / heat-kernel **zero-mode measure** on `Jac(Bring) ~ E⁴` — with the value
**forced by the physics**, never reverse-engineered from CODATA (the
reassessment's standing rule). The recon's structural lead (the flat-torus scale
anomaly `ζ_Λ(0)` as the canonical home of a bare mode-count factor) remains the
first computation of that open derivation.

## Cross-references

- Wall + template: [`2026-07-14-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md), [`2026-07-14-alpha-em-theta-graph-two-loop-candidate.md`](2026-07-14-alpha-em-theta-graph-two-loop-candidate.md)
- Proved zero-mode template (`1/(12π)`): [`../../content/quantum-observable-universe/lean/QOU/Archimedean/PhotonIRZeroMode.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/PhotonIRZeroMode.lean)
- Bring Jacobian ~ E⁴: [`2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md`](2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md)
- Attack specs: [`2026-07-17-three-front-attack-specs.md`](2026-07-17-three-front-attack-specs.md)
- Probe + witness: [`../../computations/alpha_em_perloop_integer_forcedness_probe.py`](../../computations/alpha_em_perloop_integer_forcedness_probe.py)
