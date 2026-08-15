---
# qou-8v3k
title: 'Route 8: transport the 5₂ sum rule along GGM''s deformation to the cyclotomic point x = −1'
status: in-progress
type: task
priority: normal
tags:
    - qbeta
    - dilogarithm
    - 5two
    - reduction
created_at: 2026-08-07T16:40:00Z
updated_at: 2026-08-07T16:40:00Z
parent: 0yqu
---


## Result: a REDUCTION, not a proof. The sum rule is equivalent to a 7th-root-of-unity identity.

Routes 1–7 all attacked the sum rule **at** `x = 1`. This one moves in `x`.

Probe `computations/probes/qbeta_5two_route8_envelope_deformation_cyclotomic_probe.py`,
witness `computations/qbeta-5two-route8-envelope-deformation-cyclotomic.witness.json`,
7 gates at 40 dps, all pass.

## The statement

> **The sum rule `Σⱼ Re Vⱼ = −3π²/2` is equivalent to**
>
>     Σₖ Re[ Li₂(yₖ) + 2·Li₂(−yₖ) + (log(−yₖ))² ] = −π²/2,
>       yₖ = −1 − 2cos(2πk/7),   k = 1,2,3
>
> an identity at the **totally real cyclotomic field ℚ(ζ₇)⁺**, discriminant 49.

Verified directly to residual `9.2e-41`; the root identification `yₖ = −1 − 2cos(2πk/7)`
is exact to `2.3e-41`.

## The mechanism — four elementary steps, all formalizable

**(1) The saddles are critical points of `V`.** Solving `∂V/∂y = 0` for
`V(x,y) = Li₂(y) + Li₂(xy) + Li₂(y/x) + (log(−y))²` gives
`(1−y)(1−xy)(1−y/x) = y²`, which clears to

    x·y³ − (x²+1)·y² + (x²+x+1)·y − x = 0

— **exactly GGM's deformed 5₂ curve**, already Lean-proved in the corpus as
`FiveTwoSaddleCurve.lean`. Not an assumption: derived.

**(2) Two Vieta identities.** With `e₁ = (x²+1)/x`, `e₂ = (x²+x+1)/x`, `e₃ = 1`,
and `∏ⱼ(1 − a·yⱼ) = 1 − a·e₁ + a²·e₂ − a³`:

    ∏ⱼ (1 − x·yⱼ) = x            ∏ⱼ (1 − yⱼ/x) = 1/x

Pure symmetric-function algebra. **This is the step that makes everything
collapse**, and it is a one-liner in Lean given Vieta.

**(3) Envelope theorem.** `∂V/∂y = 0` at `yⱼ`, so
`d/dx V(x,yⱼ(x)) = ∂V/∂x = (1/x)·log[(1 − yⱼ/x)/(1 − x·yⱼ)]`.

**(4) Sum, then integrate.** Summing over branches and applying (2):

    S'(x) = (1/x)·log[(1/x)/x] = −2·log(x)/x      ⟹     S(x) = S(1) − log²x

where `S(x) := Σⱼ Re V(x, yⱼ(x))`. Verified to `<1e-30` on `x ∈ [0.2, 5]`.

**Branch bookkeeping.** The ambiguity enters as `+2πik·log x`: purely *imaginary*
for real `x > 0`, so it cannot touch `Re` — which is why G4 is exact regardless of
`k`. On `|x| = 1` it is *real* (`2πik·iφ = −2πkφ`), and is **measured to be
`k = 0`** at eight points up to `φ = π` (G6, implied `k < 1e-30`).

Hence on `|x| = 1`, `S(e^{iφ}) = S(1) + φ²`, and at `φ = π`:
`S(−1) = −3π²/2 + π² = −π²/2`.

**(5) The degeneration.** At `x = −1` the curve becomes `y³ + 2y² − y − 1 = 0`,
**discriminant 49**, roots exactly `−1 − 2cos(2πk/7)`; and `xy = y/x = −y`, so
`V(−1,y) = Li₂(y) + 2Li₂(−y) + (log(−y))²`.

## ⚠ What this does NOT do

**It does not prove the sum rule.** `S(1)` is the constant of integration —
steps (1)–(4) transport the unknown, they do not evaluate it. The cyclotomic
identity is **not proved here**; it is verified numerically, exactly as the sum
rule was. Nothing stubbed. **Status: verified to 80 dps, unproved.**

## Why the transport is nevertheless worth having

This is the first route that changes the *arithmetic regime* rather than
reshuffling transformations at a fixed point.

* At `x = 1` the trace field is the **complex** cubic of disc −23. Bloch–Wigner
  `D ≠ 0` there, and every classical ladder result for that field computes
  `ζ_F(2)` via `D` — the **volume/imaginary** side. That mismatch is the caveat
  recorded in `qou-0yqu` and confirmed by the full GGM/GGMW read (`qou-g2wr`):
  it is what has blocked every literature route.
* At `x = −1` the field is **totally real and abelian** (ℚ(ζ₇)⁺). All embeddings
  are real, so `D ≡ 0` *identically* — the volume side carries nothing, and
  Rogers-type sums over such fields are expected to land in `π²ℚ`. That is the
  Frenkel–Szenes / Y-system / Watson regime, **the one regime in which `−π²/2` is
  the natural kind of answer** and where a classical proof technique exists.

So the obstruction that killed Routes 2, 6 and 7 — real part vs volume side —
is *structurally absent* at the new point.

## Next step

Prove the cyclotomic identity. Concretely: expand
`Σₖ Re[Li₂(yₖ) + 2Li₂(−yₖ)]` into Rogers `L` at 7th-root arguments and look for
a Y-system / Watson identity. The `Σₖ Re(log(−yₖ))²` term is elementary (logs of
units of ℚ(ζ₇)⁺). **Not attempted.**

Worth checking first, cheaply: whether other roots of unity appear at other
degeneration points of the family (the discriminant of the deformed curve
vanishes at `x ≈ 0.235344`, `4.24909` — GGM eq 236), which would give more
than one boundary condition.

## Refs

* parent `qou-0yqu`; siblings `qou-r7ml` (refuted), `qou-g2wr` (lit closed)
* `QOU/QBeta/FiveTwoSaddleCurve.lean` — the curve, sorry-free, already on `main`
* GGM `library/arxiv-2012.00062v3/2012.00062v3.pdf` §6.1, eq (234)–(236), eq (306) palindromy
* PR #4658

---

## Lean status — NONE of this is Lean-proved

Stated plainly because the reduction above is numerical throughout, and the
corpus's discipline is that "verified" and "proved" are different words.

**Not Lean-proved:** every step of Route 8. Also not Lean-proved: Route 7's
refutation (`qou-r7ml`) and the GGM/GGMW read (`qou-g2wr`). **No Lean was written
in this session at all** — the toolchain is unavailable here (`elan`/`lake`
absent, `release.lean-lang.org:443` denied by network policy, see `qou-clx8`).

**Already Lean-proved and reused, sorry-free:** `FiveTwoSaddleCurve.lean` on
`main` gives `curve_at_one`, `u0_cubic_discriminant` (= −23),
`curve_pair_certificate`, `curve_palindromic` — so the deformed curve and its
palindromy (G5) are formal. The PR's eleven theorems are likewise sorry-free.

### Formalizability, step by step — honest triage

| step | Lean difficulty |
|---|---|
| (1) `∂V/∂y = 0` ⟺ the curve | **algebraic half is a `ring` one-liner** — `x·[(1−y)(1−xy)(1−y/x) − y²] = −(xy³−(x²+1)y²+(x²+x+1)y−x)`. The *derivative* half needs the complex `Li₂` derivative → blocked on `qou-clx8`. |
| (2) the two Vieta products | **easiest and most valuable.** Pure symmetric-function algebra over a `CommRing`; the corpus already has this exact shape at `x = 1` (`prod_one_sub_mul_eq`). Should be short. |
| (3) envelope theorem | needs differentiability of `V` in both variables → **blocked on `qou-clx8`/`qou-ph1k`**, same gap as everything else. |
| (4) integrate the ODE + branch tracking | the delicate analytic part. See below — it is better than it first looked. |
| (5) the cyclotomic identity | **unproved mathematics**, not merely unformalized. |

### Step (4) upgraded: `k = 0` is now an argument, not a sample

Initially `k = 0` was measured at 8 points, which left "could `k` jump between
samples?" open. It is now much tighter (gate **G6b**):

* `k` is **integer-valued**, and locally constant wherever the three branches do
  not collide.
* The discriminant of the deformed cubic is **bounded away from zero on the whole
  arc** — `min |disc| = 0.348` over 200 points, attained near `φ/π = 0.765`. So
  there is **no collision on the arc**.
* Hence `k` is *constant* on the arc, and `k → 0` as `φ → 0`. Therefore `k = 0`
  throughout.
* 200-point sweep: `max |implied k| = 1.6e-29`.

That is a genuine argument modulo continuity of the branches, not a sampling
claim. It is still not Lean.

### Where the remaining mathematical risk actually sits

Not in (1), (2) or (4). It is **entirely in (5)** — the cyclotomic identity is
verified to `9.2e-41` and unproved, exactly as the sum rule itself is. Route 8
moved the difficulty; it did not remove it.

---

## ⚠ 2026-08-08 — this bean quotes a REFUTED constant

Any statement here resting on `min |disc| = 0.348` on the arc is **wrong**. The
discriminant **vanishes** on `|x| = 1` at `θ = 137.9206708879635°`, where two of
the three `y`-branches collide. Proved in integer arithmetic (palindromic
reduction `Q(u) = u⁴−6u³+7u²+6u−31`, `Q(−2) = +49 > 0 > Q(−1) = −23`, IVT).

See `qou-trns` and `qbeta_5two_route16_discriminant_vanishes_probe.py`. The
transport is **open** again: the branch-labelled formulation presumes a labelling
that does not survive the arc. `Σⱼ Vⱼ` is symmetric in the roots, so the repair
is probably to work symmetrically or deform off the circle — neither is written.
