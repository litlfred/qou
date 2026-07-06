# Q_β silver/Q_A pole: genuine but SUBDOMINANT (corrects PR #2445)

**Date:** 2026-06-17
**Probe:** [`computations/qbeta/qbeta_silver_pole_subdominant_probe.py`](../../computations/qbeta/qbeta_silver_pole_subdominant_probe.py)
(witness `qbeta-silver-pole-subdominant.witness.json`)
**Corrects:** PR #2445 (`QOU.QBeta.SilverAnchorGrounding`) interpretive claim.

## What PR #2445 claimed, and what is actually true

PR #2445 proved (correct, sorry-free Lean) that the substrate-branch `Q_A`
numerator `2q+1−q² = −(q²−2q−1)` vanishes on the silver locus `q = 1+√2`, and
that Hoefsmit `b² = 7/8` there. It then **claimed** this is "the F-pole fixing
the **dominant** `1/u_substrate ≈ 117.4` characteristic root" of the `c_k`
C-finite recurrence (`F = Q_β/[Q_A·cos α_eff]`). That dominance claim is **half
wrong**; this audit corrects it.

### 1. The pole is GENUINE (not a removable cancellation)

A first check used the **cheat-sheet closed-form** `Q_β = m_e·|q²−2q−1|(q+1)/(2q³)`
— which is the *leading* (N=1) term `≈ Q_A` — giving `F = Q_A/[Q_A·cos] = 1/cos`,
trivially regular at silver. **That check was circular** and must not be
repeated: it does not use the true `Q_β`.

The *true* `Q_β = |Δ(net)|·E₀` uses the **GB-reduced trefoil coefficient**
`Δ(net)(q)` (canonical producer `free-neutron-decay.py`). Computing it
symbolically:

```
Δ(net)(1+√2) = 82216 + 58136·√2 ≠ 0      (q²−2q−1) ∤ Δ(net)  (remainder 58136q+24080)
Q_A(1+√2)    = 0
```

So the numerator does **not** vanish where the denominator does — `F` has a
**genuine pole** at silver. PR #2445's "pole exists" is correct.

### 2. The pole is SUBDOMINANT (not the dominant root)

| pole | u | char root `1/u` | role |
|---|---|---|---|
| dominant (tail) | `u_substrate ≈ 0.00852` | **117.4** | `prop:q-beta-radius-of-convergence-gate` (PR #1727); **non-`Q_A`** source |
| silver / `Q_A` | `u_silver = u(1+√2) ≈ 0.321` | **3.12** | this audit |

Since `u_substrate < u_silver`, the **nearest-to-0** (dominant) pole is at
`u_substrate`, and the silver/`Q_A` pole is **subdominant**. PR #2445's
"…fixing the *dominant* `1/u_substrate ≈ 117.4` root" is therefore wrong: the
silver pole gives `≈ 3.12`, and the dominant `117.4` root comes from a
**different, non-`Q_A`** singularity.

## Why this is (modest) progress on the 1ppQ Q_β kernel

`RationalCoeffRecurrence` reduces "find the kernel `R`" to "find the minimal
denominator `Q`", whose roots are `1/pole`. This audit:

- **Pins one root of `Q`** — the subdominant `≈ 3.12`, now *categorically
  grounded* (the `Q_A` zero, proved in `SilverAnchorGrounding`, × the
  GB-computed `Δ(net)(silver) ≠ 0`).
- **Prunes the dominant-root search**: `117.4` is **not** the `Q_A` zero —
  look elsewhere (the structure `#2106` / `#1839` / `#1727` are after).

It does **not** make any `c_k ≥ 3` canonical, and changes no rung tier.

## Corrections applied (this PR)

- `QOU/QBeta/SilverAnchorGrounding.lean` docstring: "dominant `1/u_substrate`
  root" → "genuine but **subdominant** pole (char root ≈ 3.12), dominant `117.4`
  is non-`Q_A`"; Lean theorems unchanged (the algebra was always correct).
- `docs/coordination/ck-dk-canonical-registry.md`: added the correction entry.

## Discipline note

The circular cheat-sheet check is logged so it is not re-run. The decisive test
is always the **GB-reduced `Δ(net)`** (true `Q_β` numerator), never the
leading-term closed form (`≈ Q_A`, which cancels by construction).
