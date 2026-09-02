# Is the cosine in the Q_β ladder justified? The phase yes, the cosine no

**Date:** 2026-08-31 · **Bean:** `qou-cds1` · **Scope:** (a) — nothing derived,
proposed, wired or readmitted.

**Artifacts.**
[`QOU/QBeta/CosineParametrisationUnfalsifiable.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/CosineParametrisationUnfalsifiable.lean)
(3 theorems, sorry-free, axioms `[propext, Classical.choice, Quot.sound]`) ·
[`qbeta_cosine_parametrisation_justification_probe.py`](../../computations/qbeta/qbeta_cosine_parametrisation_justification_probe.py)
(7/7). Companion to the pre-existing
[`QOU/QBeta/BraidImageEigenphaseExclusion.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/BraidImageEigenphaseExclusion.lean).

---

## Why this is the question

The whole `c_k` program exists because the N=1 rung is written
`Q_N1 = Q_A · cos(α − u/2)`, with `α = (z−1)h/2`. Remove the cosine and there is
no tower — no `c₂ = −1`, no `c₃ ≈ −2 = J_Hopf(1)`, no `c_{k≥4}`.

## What was already closed

`BraidImageEigenphaseExclusion` leaves three ways a transfer matrix with spectrum
`{e^{±iα}}` could earn the cosine, and closes two:

| branch | status |
|---|---|
| `M` in the braid image | **excluded**, in every convention, by an elementary boundedness argument |
| `M` arbitrary | **circular** — `rotationOfPhase` satisfies it for any `α` |
| `M` a holonomy of an independently-defined connection (KZ / Kohno–Drinfeld) | **untouched** — the only contentful branch |

The class meant to carry the spectral reading, `EigenphaseCarrier`, is **vacuous**.
Nothing in the corpus supplies a connection.

## What this audit adds: the quantitative half

Proton pin, convention C, 50 dps:

| quantity | value | in σ of `Q_β/Q_A` |
|---|---|---|
| 1σ on the measured `Q_β/Q_A` | 7.784e-7 | 1 |
| `cos(θ)` explains, of the 0.167 % deviation | **95.599 %** | — |
| …without the `−u/2` offset | 81.756 % | — |
| `\|cos θ − (1 − θ²/2)\|` — the cosine's **own signature** | 4.274e-7 | **0.549** |
| residual the `c_k` tower must absorb | 7.382e-5 | **94.836** |
| **ratio** residual / signature | | **172.7×** |

Under convention D it is worse on both counts: the cosine explains **59.762 %**,
and the ratio is **4039×**.

### The reading

**The phase does real work.** `θ = (z−1)h/2 − u/2`, with `z` fixed by the
convention, captures 95.6 % of the deviation from `Q_A` with **zero free
parameters**, and the `−u/2` offset is part of that (81.8 % without it). Whatever
is wrong here, it is not the phase.

**The cosine does none the data can see.** Everything distinguishing `cos θ` from
its quadratic truncation is **half a standard deviation** of the measurement,
while the residual it fails to explain is **ninety-five**. Any function agreeing
with `cos` to second order fits identically well and leaves the same `c_k` tower.
The cosine is not *tested* by the `Q_β` anchor.

### And it loses information the exact form keeps

`cos` is even, so two distinct Markov parameters give the *same* correction:
`z = 0.4993` and `z' = 1.5822` share `cos = 0.998399` while their exact
corrections are **0.4409** and **1.6501**. The exact correction is affine in `z`
(`traceDelta_cross_mul`) hence injective. This is the algebraic form of the
"square-root branch point 0.062 % above q₀" the corpus already met.

### Formalised

| theorem | statement |
|---|---|
| `cos_departure_le` | `\|θ\| ≤ 3/50 → \|cos θ − (1 − θ²/2)\| ≤ 7e-7` — below the 7.784e-7 resolution; the bound covers both conventions (`0.0566` C, `0.0447` D) |
| `ck_residual_dominates_cos_departure` | with `r ≥ 7e-5`, the cosine's whole signature is `≤ r/100` |
| `cos_parametrisation_not_injective` | two distinct `z` give the same `cos` correction |

## What is and is not warranted

**Warranted:** the correction is `1 − θ²/2` to within the experimental
resolution, with `θ` the convention-fixed discrepancy phase.

**Not warranted by anything measured here:** that the correction is a *cosine*;
that `θ` is an *angle*; that a rotation or unitary sits behind it; or that the
residual should be expanded **in powers of `u`** at all. A `c_k` tower in `u` is a
second modelling choice on top of the first, and the anchor constrains exactly
**one** number (7.382e-5) — so `c₂ = −1` is an assumption and `c₃` is what is
left after it. *One measurement cannot determine a series.*

**Not claimed:** that the cosine is wrong. Branch 3 remains open and a
KZ/Kohno–Drinfeld derivation would justify it independently of anything measured
here.

## 🛑 Correction to the Step-16 audit (mine)

[`2026-08-31-qbeta-decay-functional-unification.md`](./2026-08-31-qbeta-decay-functional-unification.md)
concluded *"the two decay functionals are one functional in two coordinates"* and
*"the `c_k` are the affine-vs-cosine reparametrisation residual"*. **Overstated.**

The identity `Π_k(1 + c_k u^k) = affine(z)/cos(θ(z))` is a valid rearrangement
only if **both sides are evaluated at the same `z`**. The corpus's ladder does not
do that: it **fixes** `z = z_conv` and sets `Π = data/cos(θ(z_conv))`, while the
trace route **frees** `z` and sets `affine(z) = data`. Concretely at `z_C`:

```
affine(z_C)            = 0.4409      ← 55.84 % from the data
corpus ladder product  = 0.999926
Step 16 printed          0.441582    ← affine/cos, which the corpus's ladder is not
```

**Accurate statement:** the two routes are two *allocations* of the same 0.167 %
residual, with different free parameters — a `c_k` tower against a free `z`. They
share `Q_A` identically and agree at `z = 1`, so leading-order agreement between
them is automatic and carries no information; beyond that they are different
models.

**Surviving Step 16 unchanged:** the bridge `𝔈₀·(−ε(Δ_S)) ≡ Q_A` (Lean-proved,
pre-existing as `prop:neutron-qvalue-symbolic`); both corrections `= 1` at `z = 1`;
the protium findings (`Δ_S` is an **atomic** object, 235× discrimination; the
protium *element* refuted); and `F_REQUIRED_TRM = (Q_β/Q_A)/affine(z_D)` to
3.6e-9, which is a statement about the trace route alone. Step 15's withdrawal of
"K off by 2.2656×" therefore also stands.

## Where this leaves `qou-cds1`

The bean's primary item — *re-derive the `c_k` ladder under D* — now has three
separate problems, none of which is "the algebra is hard":

1. **No anchor** (Step 15): `c₂ = −1` is a 1.6 σ C-frame statement, excluded at
   773 σ under D.
2. **No derivation for the parametrisation** (`BraidImageEigenphaseExclusion` +
   this audit): two of three branches closed, and the surviving cosine is
   empirically indistinguishable from a parabola.
3. **Under-determination**: one measured number, a series of coefficients.

The productive direction is branch 3 — supply a KZ/Kohno–Drinfeld connection
whose holonomy *is* the phase — or drop the cosine and state the correction as
what the data supports, `1 − θ²/2`, with no tower.

Anchor: experimental (proton) pin, per the 2026-08-07 owner directive.
