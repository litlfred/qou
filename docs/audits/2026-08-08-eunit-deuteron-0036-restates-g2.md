# The E_unit deuteron −0.036% restates g₂, it does not corroborate it (2026-08-08)

**Tier:** critical-distance note on an existing result · **Wired:** nothing ·
**No fit, no new computation of the underlying quantities.**
Subject: [`2026-07-24-eunit-magnus-order2.md`](2026-07-24-eunit-magnus-order2.md).

---

## 1. The audit under review is already honest

Worth saying first, because it is: the 07-24 Magnus-order-2 audit does **not**
overclaim. It labels `g₂ = 1.0087` explicitly as **"NEAR-MATCH — underived"**, the
`E⁺(1+h²)` row as **"near-match tier, NOT wired"**, states plainly that
**"A≥3 is untouched"** (T −43.4%, ³He −37.8%, ⁴He −69.4%), cites the c₃ flip-flop
lesson by name, and carries an anti-fit accounting section. Nothing below is a
correction to it.

The observation is about how the **−0.036%** figure will be read downstream.

## 2. The identity

`g₂` is *defined* as the measured ratio `gap/h²`. So `E⁺(1 + g₂h²) = AME` holds
**by construction**, and the quoted deuteron residual is algebraically forced:

```
E⁺(1 + h²) − AME  =  −(g₂ − 1)·h²·E⁺
```

Numerically, from the audit's own values (`E⁺ = 2.13064`, `h² = 4.3707%`,
`g₂ = 1.0087`, AME = 2.2245662):

```
E⁺(1+h²)   = 2.2237639   ->  err = -0.03607 %
(g₂-1)·h²  =              +0.03803 %
```

The same number. **The −0.036% is not an independent measure of how well the
order-2 term works — it is the 0.87% miss of `g₂` from 1, scaled down by
`h² ≈ 4.4%`.** The two figures are one datum stated twice.

## 3. Why this matters for how it gets cited

A residual quoted at 0.036% reads as a two-significant-figure agreement. The
underlying claim is that an *underived* coefficient sits within **0.87%** of
unity — a factor of ~24 less precise, and precisely the claim the audit itself
flags as a near-match.

The audit anticipates the substance of this in one line — *"If it is not exactly
1, the −0.036% is partly accidental"* — but stops short of the identity. Making it
explicit converts a hedge into an equality: the −0.036% is **entirely**
determined by `g₂ − 1`, not partly. There is no residual accuracy left over to
credit to anything else.

The corpus has been bitten by exactly this shape before: the Δ_λ deuteron
"+0.91% closure" that turned out to be a single-isotope fit with `C_knot`
back-solved from AME (corrected 2026-06-17). This is *not* that — no AME
inversion occurred, and the audit says so credibly — but the reporting surface is
similar enough to be worth pinning down before the number propagates into a
status board as "deuteron closes to 0.036%".

## 4. Recommended phrasing

State the deuteron result as the coefficient miss, not the residual:

> The order-2 unit `h²` reproduces the deuteron bar-even gap with measured
> coefficient `g₂ = 1.0087` — within 0.87% of unity, **underived**. The quoted
> −0.036% on `E⁺(1+h²)` is that same 0.87% scaled by `h²` and carries no
> additional information.

And keep the A≥3 line adjacent, since it is the load-bearing caveat: the same
recipe leaves T/³He/⁴He at −43% to −69%, which an `h²`-size term cannot reach and
the audit does not claim it does.

## 5. What is actually open

Unchanged and correctly identified by the 07-24 audit: **derive `g₂`** — from the
octahedral `e₂` term or the surface-curvature pairing. Until then the deuteron
agreement is one underived coefficient near 1, and the tier is near-match.

Scope-(a) throughout. Nothing here refutes the Magnus route, the counit
identification (`μ₀ = m_e/(3h/2)`, 0 free parameters, merged #4117), or the
bar-even projection. It narrows what the −0.036% is evidence *of*.
