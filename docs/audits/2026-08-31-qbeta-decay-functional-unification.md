# The two Q_β decay functionals are one functional

**Date:** 2026-08-31 · **Bean:** `qou-cds1` · **Scope:** (a) — nothing derived,
proposed, wired or readmitted; no convention adjudicated.

**Artifacts.**
[`QOU/QBeta/DecayFunctionalUnification.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/DecayFunctionalUnification.lean)
(5 theorems, sorry-free, axioms `[propext, Classical.choice, Quot.sound]`) ·
[`qbeta_decay_functional_unification_protium_probe.py`](../../computations/qbeta/qbeta_decay_functional_unification_protium_probe.py)
(6/6) ·
[`qbeta_d_frame_z_determinations_experimental_budget_probe.py`](../../computations/qbeta/qbeta_d_frame_z_determinations_experimental_budget_probe.py)
(8/8).

---

> ## 🛑 CORRECTED the same day — see [the cosine-justification audit](./2026-08-31-qbeta-cosine-parametrisation-justification.md)
>
> **"They are the same functional in two coordinates" is OVERSTATED**, as is
> "the `c_k` are the affine-vs-cosine reparametrisation residual". The identity
> `Π = affine(z)/cos(θ(z))` needs both sides at the **same `z`**; the corpus's
> ladder **fixes** `z = z_conv` and lets the `c_k` absorb, while the trace route
> **frees** `z`. At `z_C` the affine correction is `0.4409` — 55.84 % from the
> data — while the ladder's product is `0.999926`. The two routes are two
> **allocations** of one residual, with different free parameters, not one
> functional.
>
> **Unaffected below:** the bridge `𝔈₀·(−ε(Δ_S)) ≡ Q_A`, agreement at `z = 1`
> (hence that leading-order agreement is automatic and uninformative), every
> protium finding, and `F_REQUIRED_TRM = (Q_β/Q_A)/affine(z_D)` to 3.6e-9.


## The question, and why it was malformed

`qou-cds1` Step 15 left the bean asking which of two readings of the decay
channel is correct:

| reading | form | wants |
|---|---|---|
| **trace** | `Q_β = K · tr_M^z(Δ_S)` | `z = 0.998500` |
| **ladder** | `Q_β = Q_A · cos(α − u/2) · Π_k(1 + c_k u^k)` | `z = 0.499110` |

Both claim to reproduce the same `Q_β`, so at most one looked right. **Neither
is more right: they are the same functional in two coordinates.** The question
dissolves rather than resolves, and what remains is a different and smaller
question.

## What protium settles

The owner's framing is what makes this checkable. β decay's daughter is the
neutral atom, so the simplest decay is

```
n  →  ¹H + ν̄_e ,        Q_β = m_n − m(¹H)
```

— an **atomic** mass difference, not the nucleon difference `m_n − m_p`, which
is larger by exactly `m_e`. The corpus's decay element is written
`Δ = NF(n) − NF(p)`, which reads as the nucleon difference. Priced against both
targets with the corpus's own derived scale `𝔈₀ = m_e/(q₀(q₀−1))` — the
canonical hadronic energy scale, CAL-1 and CAL-2 only, no fit:

| | vs atomic `Q_β` | vs nuclear `m_n − m_p` |
|---|---|---|
| `𝔈₀ · \|ε(Δ_S)\|` | **0.168 %** | −39.41 % |
| `𝔈₀ · \|net(Δ_L = n−p)\|` | 21.55 % | −26.48 % |
| `𝔈₀ · \|net(Δ_β = n−¹H)\|` | 5.60 % | −36.12 % |

**A 235× discrimination with zero free parameters.** `Δ_S` is already an
**atomic** object: the emitted electron is accounted for inside it, and the
`NF(n) − NF(p)` notation is misleading about what the element is.

### And therefore building the element from protium double-counts

`Δ_β := NF(n) − NF(protium)` — the naively correct β-decay difference — is
**refuted**. On the physical pairing (atomic element against the atomic target)
the nearest `z` it requires is **0.4439** from the derived cap `z_D = 0.61269`,
*worse* than the corpus's own **0.3858**. One off-diagonal cell (atomic element
against the *nuclear* target) is nearer at 0.3386, but that pairing is unphysical
and is still 55 % of the way from `z_D`.

> Recorded because the first draft of the probe asserted *"every protium `z` is
> further from the cap"* and the data refuted it. The obvious move does not work,
> and it does not nearly work either.

## The unification

`ε(Δ_S) = h²/2 − h` is `tr_M^z(Δ_S) = h²/2 − h·z` at `z = 1`, and

```
𝔈₀ · (−ε(Δ_S))  ≡  Q_A          identically in q and m_e
```

**This identity is not new** — it is `prop:neutron-qvalue-symbolic`, restated in
`qbeta_delta_tr_vs_formA.py` as *"`Q_A = m_e × |Δ(net)_A| × E_0`, `E_0 =
1/(q(q−1))`, `Δ(net)_A = h(h−2)/2`"*. What is new is the consequence nobody had
drawn from it: **the ladder's leading term IS the trace functional at `z = 1`
with `K = 𝔈₀`**, so the two readings share that term *by construction*, and
equating them forces

```
Π_k (1 + c_k u^k)  =  affine(z) / cos((z−1)h/2 − u/2),
        affine(z) = (2qz − q² + 1)/(2q − q² + 1),   affine(1) = 1
```

The trace side is **exact and affine in `z`**. The ladder writes the same
correction as a cosine of an affine function of `z`, times a power series. So the
`c_k` are the mismatch between those two parametrisations — a **reparametrisation
residual**, not an independent expansion.

That is the **third instance in this corpus of the "defined residual ≠ derived
decomposition" class** named STRICT in `AGENTS.md`, after `S_leak := c₃ + Vol(4₁)`
and `S := −c₃/κ₍₂,₁₎`. It is also consistent with what the corpus already
recorded about the coordinate — *"α was shown to be a bad coordinate (a
square-root branch point 0.062 % above q₀, manufactured by writing a smooth
correction as a cosine)"*.

### Proved

`DecayFunctionalUnification.lean`, generic over any characteristic-zero field:

| theorem | statement |
|---|---|
| `E0_mul_counit_eq_QA` | `𝔈₀·(−ε(Δ_S)) = Q_A` |
| `traceDelta_cross_mul` | `tr_M^z·(2q−q²+1) = ε·(2qz−q²+1)` — the correction is affine in `z` |
| `traceFunctional_eq_QA_mul_affine` | `𝔈₀·(−tr_M^z)·(2q−q²+1) = Q_A·(2qz−q²+1)` |
| `traceRatio_sub_one` | departure from 1 is linear in `z−1`, slope `2q` |
| `alpha_two_mul` | `2α = ε − tr_M^z` — the corpus's own definition of the phase |

## Why the two routes reported different `z`

Both invert *their own* correction function to the same measured
`Q_β/Q_A = 0.998325`. At `z = 1`:

```
affine slope  =  1.116732        →  z = 0.998500
cosine slope  =  4.4515e-4       →  z = 0.486995
slope ratio   =  2508.65 ×
```

A correction 0.17 % below 1 therefore needs `z` a hair off 1 on the affine route
and far off 1 on the cosine route. **That is the whole of "0.9985 vs 0.4991."**
It was never two physical claims.

## Two withdrawals, both from Step 15 and both mine

1. *"The two decay-side functionals disagree … reconcilable only by a scale `K`
   off by 2.2656×, 20× outside Step 14's 6.31 % wall."* **Withdrawn.** There is
   no scale gap — the leading terms are identical. The committed
   `F_REQUIRED_TRM = 1.75923699` is exactly `(Q_β/Q_A) / affine(z_D)`,
   reproduced to **3.6e-9**: a statement about where `z_D` sits on the affine
   line, not a missing normalisation.
2. *"At most one of the two functionals is the right reading."* **Withdrawn** —
   both are the same reading.

Step 15's other findings are untouched: mass-vs-cap at 9.49 σ, decay-vs-cap at
5.5e5 σ, `c₂ = −1` as a 1.6 σ C-frame statement excluded at 773 σ under D, and
the three-corpus-facts-one-measurement identity.

## What this leaves open

**"Re-derive the `c_k` ladder under D" has no hidden answer to find.** Given `z`,
the ladder is *defined* by the equation above; under D you substitute `z_D` and
read off whatever comes out. That is why both routes were "blocked at the
anchor" (Step 15): there is no independent object for an anchor to pin.

The live question is narrower and different in kind: **should the cosine
parametrisation exist at all?** The trace side is exact, affine and needs no
series. The ladder's entire `c_k` tower exists because the exact affine
correction was rewritten as `cos(affine)`. Removing the cosine removes the
tower — and with it the `c₂ = −1`, `c₃ ≈ −2 = J_Hopf(1)` and `c_{k≥4}` program.

**Not claimed:** that the cosine is wrong, that the framework is wrong, or that
`Q_β` is closed. The decay channel's tension with the derived cap
(`z = 0.9985` against `z_D = 0.6127`, 5.5e5 σ) is **untouched by this** and
remains the open problem — this file says only that the tension has one form, not
two, and that the `c_k` are not where it lives.

## Ledger of figures

| quantity | value |
|---|---|
| `𝔈₀ = m_e/(q₀(q₀−1))` | 4.1859813632945 MeV |
| `Q_A` | 0.7836458273746212 MeV |
| `\|𝔈₀·(−ε) − Q_A\|` | 0.0 (exact) |
| measured `Q_β/Q_A` | 0.99832524167325 |
| affine / cosine slope at `z=1` | 1.116732 / 4.4515e-4 → **2508.65×** |
| `(Q_β/Q_A)/affine(z_D)` vs committed `F_REQUIRED_TRM` | 1.7592369942 vs 1.7592369905 (3.6e-9) |

Anchor: experimental (proton) pin, per the 2026-08-07 owner directive. The `Δ_S`
closed forms are the corpus's, valid for the **short** model
(`qbeta_delta_element_fork_pricing_probe.py`); this audit inherits that scope
rather than re-establishing it.
