# Saddle-offset probe — 4₁/5₂ certified Stokes data as a q-deformed saddle vector

**Date:** 2026-08-02
**Branch/PR:** `claude/saddle-offset-probe-fourone-fivetwo-2026-08-02` / #4578
**Kind:** exploratory numerical probe (derive-then-check, anti-fit, honest-negative)
**Siblings:** #4577 (Lean structural gate `offset = 0 ⇔ ι-fixed`), #4573 (`qou-fk19` red-flag ledger)
**Arc ledger:** [`docs/coordination/2026-08-02-c3-odd-aomega-unification.md`](../coordination/2026-08-02-c3-odd-aomega-unification.md)

## The picture under test

Owner's saddle-vector picture: a knot-particle is a **vector** (angle + magnitude)
sitting at a saddle point of the covering surface; it is **origin-centred only at
`q = 1`**, and for `q ≠ 1` it is **offset**, the offset being the **ι-odd**
(bar-odd, `q ↔ q⁻¹` antisymmetric) component. The knot winds *near-but-not-on* the
saddle. This probe is the **numerical complement** to the Lean structural gate
(#4577, `offset = 0 ⇔ ι-fixed`): it lifts the merged 5₂ `{3,4}` distinguisher
([`FiveTwoDTSpectrumSplit.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/FiveTwoDTSpectrumSplit.lean),
`chiralityOdd 4 3 = 1`) into a genuine 2-D saddle vector with an angle and a
magnitude, computed from the certified Stokes q-series.

## Method — reuse of certified corpus, no recompute

[`computations/probes/saddle_offset_fourone_fivetwo_probe.py`](../../computations/probes/saddle_offset_fourone_fivetwo_probe.py)
imports the certified 5₂ sandwich machinery
([`qbeta_g3_5two_stokes_sandwich.py`](../../computations/probes/qbeta_g3_5two_stokes_sandwich.py),
K1/K2/K3 ✓, unflipped W-convention) **unchanged** and reads the off-diagonal
Stokes q-series. It stays clear of every `qou-fk19` red-flag: **no** `v_offset(q)`
ODE, **no** `q = exp(2πiτ)` pin, **no** invented θ-function `R(q,x)` — only the
actual certified `S±(q)` matrices are used as the saddle data.

### Definitions (locked BEFORE compute — not tuned)

- Saddle vector `v(q) = (c⁺(q), c⁻(q))`, where `c^ε` is the certified off-diagonal
  Stokes series carrying the DT constant. Chirality→slot identification reused from
  the merged distinguisher: `c⁺ = S⁺(q)[0][1]` (the (96) factorization, leading 4),
  `c⁻ = S⁻(q)[0][2]` (the (97) factorization, leading 3). 4₁ is amphichiral — the
  DT spectrum collapses to `{3}`, both chiralities carry the same 3, `v = (3,3)`.
- Classical (ι-fixed / amphichiral) axis = the diagonal `c⁺ = c⁻`.
- **ι-odd OFFSET** `o(q) = c⁺(q) − c⁻(q)` — perpendicular displacement off the
  diagonal, the bar-odd grade of `ω = βp − β⁻¹q`.
- **Saddle angle** `θ(q) = atan2(o, c⁺+c⁻)`; **magnitude** `|v| = hypot(c⁺,c⁻)`.

## Findings

### 1. Certified saddle vector and its ι-odd offset

```
5₂  c⁺(q) = S⁺[0][1] = 4 − 33q − 18q² + 151q³ + …    (leading 4)
    c⁻(q) = S⁻[0][2] = 3 − 24q + 10q² + 126q³ + …    (leading 3)
    o(q)  = c⁺ − c⁻  = 1 −  9q − 28q² +  25q³ + …
```

| datum | 5₂ (chiral) | 4₁ (amphichiral) |
|---|---|---|
| saddle vector `v(0)` | `(4, 3)` | `(3, 3)` |
| ι-odd offset `o(0) = c⁺(0)−c⁻(0)` | **1** | **0** |
| saddle angle `θ(0)` | **8.13°** (`atan2(1,7)`) | **0°** |
| magnitude `|v(0)|` | 5 | 4.24 |
| perpendicular offset `|o|/√2` | 0.707 | 0 |

**The q→0 (DT / semiclassical) offset reproduces the ι-odd `{3,4}` difference
exactly** (`o(0) = 1`), matching the merged distinguisher's `chiralityOdd 4 3 = 1`
and #4577's `offset numerator = 1` / `offset = (½, −½)`. Amphichiral 4₁ sits **on**
the classical diagonal (offset 0). This is the confirming numerical complement to
the Lean gate.

### 2. The saddle is genuinely q-deformed

`o(q)` is **not** a q-constant (`1 − 9q − 28q² + …`): the saddle vector genuinely
moves as q deforms. The off-diagonal magnitudes also drift (independently, the
certified 4₁ off-diagonal entry runs `3` at q→0 → `1.5852` at the substrate,
`StokesSymmetryConstant` reading R1 — the magnitude moves while 4₁'s offset stays
0 by amphichirality). This quantifies the "winds near-but-not-on" picture: the
saddle position is q-dependent, its q→0 displacement being exactly the ι-odd DT
datum.

### 3. Honest negative — the "origin-centred **only** at q=1" leg is NOT supported

Two independent reasons the *specific* q=1 claim fails to be established by the
certified data:

1. **Domain.** The certified Stokes series are Taylor series around `q → 0` (the
   DT limit where GGM read `{3,4}`); the `(q;q)`-type factors **diverge at q=1**,
   so the offset cannot be evaluated there. `o(q)` is a q→0-anchored cross-chirality
   datum (leading `1 ≠ 0`), not an object continued to the ι-fixed point.
2. **Sign structure within the radius.** Within the convergent region the offset
   `o(q)` **crosses zero at a small finite `q ≈ 0.08`** (it is `+0.81` at q=0.02,
   `+0.48` at q=0.05, `−0.14` at q=0.10; q≥0.2 is past the truncation radius). So
   the saddle passes through the classical diagonal at a *small finite* q, **not**
   at q=1.

The algebraic gate `offset = 0 ⇔ ι v = v` (#4577) is solid and is confirmed here at
its 5₂/4₁ grounding; but the *physical identification* "ι-fixed locus = q=1" is a
modelling convention (correctly flagged scope-(a) in #4577), and the certified
Stokes series do **not** independently place the offset-zero at q=1.

## Verdict (scope-labelled, honest)

- **CONFIRMED [scope-(a)] at the DT limit:** the ι-odd saddle offset reproduces the
  `{3,4}` datum (5₂ → 1, 4₁ → 0), with a quantified near-but-not-on geometry
  (angle 8.13° vs 0°) and a genuinely q-deformed offset. This is the numerical
  complement to #4577.
- **OPEN:** the "origin-centred **only** at q=1" leg — beaned (see below). It is a
  distinct claim the q→0-anchored certified data cannot reach, and the within-radius
  zero-crossing at small finite q argues *against* the specific q=1 placement.

This is a **scope-(a)** result: it constrains the *reading* of the picture (where
the offset-zero sits, what is testable from the DT series) — it excludes **no**
ingredient (no proved invariant is invoked), per the "refuted/ruled out" STRICT rule.

## Anti-numerology guards respected

- Definitions + `expected` assertions locked before the compute; none tuned to pass.
- No fit; no `c_k` wired; no axiomatization; **nothing wired to any dashboard / the
  Q_β ladder**; scope-(a).
- Reuses the certified sandwich (no recompute); avoids all `qou-fk19` red-flags.

## Formalization note (no new Lean — sibling owns it)

The clean structural claim (`offset = 0 ⇔ ι-fixed`, plus the 5₂/4₁ grounding) is
formalized by the sibling in
[`IotaOddSaddleOffsetAmphichiral.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/IotaOddSaddleOffsetAmphichiral.lean)
(#4577). This probe deliberately does **not** duplicate it; the q→0 offset value is
already the certified `chiralityOdd 4 3 = 1` of `FiveTwoDTSpectrumSplit`. The one
numerical observation with no clean Lean lift is the finite-q zero-crossing (§3.2),
recorded here and in the witness as data, not as a theorem.

## Next / open

- **Bean:** the "origin-centred only at q=1" leg — establish (or refute) that the
  saddle offset vanishes at the ι-fixed point `q=1`, which requires an object valid
  *at* q=1 (the certified DT series are not). Candidate route: a two-sided /
  resummed representation of `S±` valid near `|q|=1`, or recasting the offset as a
  genuinely ι-covariant object `o(q) = f(q) − f(q⁻¹)` whose q=1 vanishing is
  structural — neither available from the current q→0 sandwich.
