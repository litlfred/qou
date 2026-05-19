# Where the Q_β precision-ladder c_k coefficients enter the framework

**Date:** 2026-05-19
**Branch:** `claude/track-a-b-per-isotope-and-rho-xi`
**Context:** user direction "give fuller context where c_k come in".

## The c_k chain — what they are, what they multiply, where they sit

The c_k are coefficients in **one specific formula** in the framework — the **Q_β categorical-derivation precision ladder**:

$$
Q_\beta^{\text{cat}}(q)
  \;=\; Q_\beta^A(q)
  \cdot \cos\!\bigl(\alpha - \tfrac{b\,\hbar_q^2}{2}\bigr)
  \cdot \prod_{k=2}^{\infty} \bigl(1 + c_k(q) \cdot b^k \cdot \hbar_q^{2k}\bigr).
$$

Each c_k(q) is a function of q (the substrate parameter); the product gives the **Q_β prediction** as a function of q. At q = q_0 ≈ 1.110, the prediction approximates the CODATA / CAL-3 value 0.78233341 MeV.

### Components

| Symbol | What it is | Where defined |
|--------|-----------|---------------|
| Q_β^A(q) | Form A baseline = m_e · \|q²−2q−1\|·(q+1)/(2q³) | `prop:neutron-qvalue-symbolic` |
| α(q) | single-wrap eigenphase = (z−1)·h/2 with z = 1/(√q + 1/√q) | `prop:q-beta-spectral-bridge` |
| b(q) | Hoefsmit off-diagonal coupling = √(q⁴+q²+1)/(q²+1) on V_(2,1) | `prop:hoefsmit-V21-cos-symmetrization` |
| ℏ_q(q) | quantum Planck constant = (q−1)/q | `def:hbar-q` |
| **c_k(q)** | **per-rung categorical coefficient** | **`prop:q-beta-categorical-precision-ladder`** (this audit's subject) |

## What the c_k determine

The c_k determine the **precision** of the Q_β prediction at each rung N:

| Rung N | Cumulative formula factor | Residual at q_0 vs CODATA Q_β |
|-------|----------------|---------------:|
| 0 (Form A only) | Q_β^A | +1 677 540 ppb (0.17%) |
| 1 (+ cos correction) | × cos(α − b·ℏ_q²/2) | +73 790 ppb |
| 2 (+ Kashiwara b²) | × (1 − b²·ℏ_q⁴) | +1 242 ppb |
| 3 (+ Hopf at q=1) | × (1 − 2 b³·ℏ_q⁶) | **+6.02 ppb** ← beats L2 target |
| 4 | × (1 − 2·b⁴·b⁴·ℏ_q⁸) | +0.055 ppb |
| 5 | × (1 − (b²+½)·b⁵·ℏ_q^10) | −0.0013 ppb |
| 6 | × (1 + 4·b²·b⁶·ℏ_q^12) | −0.00019 ppb |
| 7 | × (1 − 8·b⁷·ℏ_q^14) | −0.00021 ppb |

**The c_k drive the precision of the Q_β prediction. Each c_k closes a smaller-magnitude residual.**

## Where Q_β plugs into the framework downstream

Q_β is **CAL-3** — the third calibration anchor of the framework:

```
CAL-1: m_e                              (electron mass, leptonic scale)
CAL-2: q_0                              (substrate parameter, geometric scale)
CAL-3: Q_β = β-decay endpoint of free n  (hadronic energy scale)
```

The Q_β value sets `E_0 = Q_β / |Δ(net)|`, the hadronic energy scale, where |Δ(net)| is the symbolic Markov-trace difference between proton and neutron at H_3 (= h·(h−2)/2).

Downstream consumers of Q_β / E_0:

| Observable | How it uses Q_β | Effect of Q_β precision |
|-----------|-----------------|------------------------|
| m_p (proton mass) | Borromean tower: m_p = m_e · Vol(B_3)/ℏ_q² · λ_p; λ_p is closed against CODATA m_p | indirect (m_p has its own calibration chain) |
| m_n (neutron mass) | m_n = m_p + Q_β + m_e (additive convention) | **direct** — m_n inherits Q_β precision |
| Δm_pn = m_n − m_p | Δm_pn = Q_β + m_e | **direct** — Δm_pn inherits Q_β precision |
| Light-atom binding energies | indirect via m_p, m_n constituent masses | **indirect** (gated on Δ_λ — separate R&D) |

**So Q_β at sub-ppb precision (which the precision ladder achieves at N=4+) tightens:**

- Δm_pn predicted to sub-ppb (currently 254 ppb miss the 4.74 ppb L2 target by 54× — Q_β isn't the bottleneck; the Borromean λ_p/λ_n derivation is).
- m_n at the precision of m_p (~250 ppb post-Borromean) + Q_β precision (sub-ppb) ≈ m_p precision.

The c_k LOCALLY control Q_β; they DON'T directly control m_p, m_n. They're not in the per-isotope binding-energy formula `B(K) = m_e · Σ y_λ χ^λ Δ_λ` either (that's gated on Δ_λ, a completely separate R&D track).

## How c_k differ from other categorical coefficients in the framework

The framework has several "per-block" or "per-partition" coefficient families:

| Family | Used where | Indexed by |
|--------|-----------|-----------|
| c_k (this audit) | Q_β precision ladder | rung depth N = 1, 2, 3, ... |
| Δ_λ(K) | per-isotope binding `B(K) = m_e · Σ y_λ χ^λ Δ_λ(K)` | partition λ ⊢ 3A |
| λ_p, λ_n (Borromean λ_scale) | m_p, m_n = m_e · Vol(B_3)/ℏ_q² · λ | per nucleon (p or n) |
| ρ_K(q) | atom mass M = ρ_K · m_e · |tr_M| | per atom K |
| y_λ(q) | Wenzl bridge weight | partition λ |

These are **all distinct**. The c_k operate at a different layer than Δ_λ or λ_scale — they refine the **CAL-3 anchor itself**, not predict downstream observables.

## Why deriving c_k matters

Three reasons:

1. **L2 100×-experimental honesty for Q_β.** Currently L2 reports the N=3 categorical prediction (6.02 ppb residual) as "Q_β meets target". If c_3 = −2 is the ONLY derived rung, then everything beyond N=3 is empirical — including the sub-ppt closures at N=4+. Reporting those without honesty about derivation status would be a precision-discipline violation.

2. **Categorical completeness of the framework.** The framework's claim is that *all* observable predictions derive from the substrate parameter q_0 and the categorical machinery (Hecke / Markov trace / Hoefsmit / etc.). If c_4 = −2·b⁴ is an empirical fit, that's an unproved input — a kind of "fourth calibration anchor", which violates the three-calibration discipline.

3. **Predictive power for other observables.** If the generating function F(z, b, ℏ_q) for c_k were derived, the SAME function might apply to other categorical-trace expansions in the framework — extending the derivation reach. Currently this is unexplored.

## Reading guide for downstream agents

- **If you're working on Q_β prediction precision**: c_k drives it. Latest closed forms are in [`q-beta-categorical-precision-ladder.md`](../../content/quantum-observable-universe/braids-and-knots/q-beta-categorical-precision-ladder.md).
- **If you're working on m_p / m_n / Δm_pn**: c_k matters only via its effect on Q_β's CAL-3 precision — currently *not the bottleneck* (Borromean λ_p/λ_n derivation is the bottleneck on Δm_pn).
- **If you're working on light-atom binding energies**: c_k is **independent** of Δ_λ. The binding-energy R&D is on a different track.
- **If you're working on the three-calibration discipline**: c_4..c_7 are currently empirical fits. The 2026-05-19 closure-path audit ([`2026-05-19-qbeta-ladder-closure-path.md`](2026-05-19-qbeta-ladder-closure-path.md)) outlines three routes to derive them.

## Cross-references

- [`docs/precision-goals.md`](../precision-goals.md) — L1 / L2 precision targets framework-wide
- [`docs/audits/2026-05-19-qbeta-all-ck-categorical-extension.md`](2026-05-19-qbeta-all-ck-categorical-extension.md) — extended closed forms for c_1..c_7
- [`docs/audits/2026-05-19-qbeta-ladder-closure-path.md`](2026-05-19-qbeta-ladder-closure-path.md) — three concrete derivation routes
- [`docs/audits/2026-05-18-qbeta-n4-sign-investigation.md`](2026-05-18-qbeta-n4-sign-investigation.md) — original N=4 sign issue
- [`docs/audits/2026-05-18-qbeta-n5-cohomological-breakdown.md`](2026-05-18-qbeta-n5-cohomological-breakdown.md) — cohomological-strata hypothesis
- [`content/quantum-observable-universe/braids-and-knots/q-beta-categorical-precision-ladder.{md,lean}`](../../content/quantum-observable-universe/braids-and-knots/q-beta-categorical-precision-ladder.md) — the main content block
