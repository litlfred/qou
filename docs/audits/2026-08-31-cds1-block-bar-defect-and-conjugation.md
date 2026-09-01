# `qou-cds1` — the bar-defect at block resolution, and where the Kohno–Drinfeld duality lives

**Date** 2026-08-31 · **Bean** `qou-cds1` · **Scope (a)** throughout · **No `c_k`, no `K`, no Q_β movement**

Probe: [`computations/qbeta/qbeta_block_bar_defect_conjugation_probe.py`](../../computations/qbeta/qbeta_block_bar_defect_conjugation_probe.py)
— 14/14, sympy exact, **runs standalone with `PYTHONPATH` stripped**.

## What this answers

Entry 12 of `qou-cds1` established that bar-parity is **silent** on the free
constant `K(δ)` in the ladder's N=1 factor, because `δ = h²/2` is bar-invariant;
it closed with *"Closing `K` needs a genuinely different input."* Entry 14 then
withdrew entry 13, so `K` is free again and carries a residual **7656×** the
Q_β 100× target — the largest single L2 blocker on the arc.

Two candidate inputs were tested, both structural:

- **(A)** does resolving the defect **per Wedderburn block** restore a parity handle?
- **(B)** is the bar involution the **Kohno–Drinfeld conjugate-partition duality**
  `λ ↔ λ'`, which would make the C-frame cancellation a theorem rather than a
  coincidence?

**Both are refuted.** They were this probe's own hypotheses. What the attempt
produced instead is a mechanism statement and a second, independent closure of
the *z*-direction.

## Method

Built on the exact master identity of
[`qbeta_phase_block_resolution_probe.py`](../../computations/qbeta/qbeta_phase_block_resolution_probe.py)
(a sibling's, not re-derived here), valid for every `z`:

```
2α  =  Σ_λ [ a_λ − y_λ(z) ] · χ^λ(Δ)  +  net(dC)
```

with `a_λ`, `χ^λ(Δ)` and `net(dC)` all *z*-free and the convention entering at
the single factor `y_λ(z)`.

`z` is a function of `q`, so **`bar` acts on `(q, z)` jointly**. `zbar` is
carried as an independent symbol and specialised only at the end, by the two
conditions `MarkovZFullBarCondition.lean` proves sorry-free:

| condition | action | convention |
|---|---|---|
| bar-even | `zbar = z` | C |
| full-bar | `zbar = z − h` | D |

Holding `z` fixed under `bar` is the meaningless test this bean already
recorded and discarded; it is not done here.

## Result 1 — the two conventions differ in **kind**, not degree

Writing `d_λ = bar(B_λ) + B_λ` for each block's contribution:

| | `(3)` | `(2,1)` | `(1³)` | floor | sum |
|---|---|---|---|---|---|
| **bar-even (C)** | **z-dependent** | 0 | **z-dependent** | z-free | **0**, for *every* bar-even z |
| **full-bar (D)** | `(h²/2)·r` | 0 | `(h²/2)/r` | `−2q²h²/(q⁴+q²+1)` | **h²**, for *every* full-bar z |

with `r = (q²+q+1)/(q²−q+1)`, and the two D defects **exact reciprocal
multiples** of `h²/2`. At `q₀` (in units of `h²`): `(3)` 1.48922059503199,
`(1³)` 0.16787304770965, floor −0.6570936427416, `r(q₀)` = 2.97844119006.

`χ^(2,1)(Δ) = 0` identically, so the phase is blind to the 2-dimensional block
in both conventions.

**The C-frame's bar-oddness — the property the entire C ladder's bare cosine
rests on — is a cancellation between the symmetric and antisymmetric blocks,
not a property any block has.** Under D the cancellation is destroyed, and the
per-block defects become **constants**: the *z*-dependence cancels *inside* each
block instead of *between* blocks.

### Consequence

No choice of `z` within the full-bar class changes the D-frame defect — at block
resolution or in aggregate. The "choose a better z" repair direction is now
closed from **two independent directions**:

1. the **anchor** side — the two-constraint filter of
   [`qbeta_ladder_alpha_form_filter_probe.py`](../../computations/qbeta/qbeta_ladder_alpha_form_filter_probe.py),
   which showed no *constant* z satisfies both the value and slope rows;
2. the **parity** side — this result, which shows the defect does not depend on
   z at all within the class.

## Result 2 — hypothesis (A) is refuted

Every `d_λ` is **itself bar-invariant** — as a bar-defect always is, since
`bar(bar(X) + X) = X + bar(X)`. So entry 12's silence survives block resolution
*verbatim*: per-block bar-parity constrains a per-block `K` exactly as little as
aggregate bar-parity constrains `K`.

**Block resolution is not the different input entry 12 asked for.** Recorded as
a negative because the hypothesis was plausible enough to be worth someone
else's session.

## Result 3 — hypothesis (B) is half right, and the failing half is one scalar

```
bar(χ^λ(Δ)) = χ^{λ'}(Δ)      EXACT, all three blocks, convention-free
bar(a_λ)   ≠ a_{λ'}
bar(y_λ)   ≠ y_{λ'}
```

The **block characters do carry** the Kohno–Drinfeld duality: `bar` sends
`χ^(3)(Δ) ↔ χ^(1³)(Δ)` and fixes the self-conjugate `χ^(2,1)(Δ)`. The Markov
weights do not — but every one of the three residuals is proportional to the
**same factor `(z + zbar)`**, and solving the three simultaneously returns the
unique bar action

```
zbar = −z        i.e.   y_λ is conjugation-equivariant  ⟺  z is bar-ODD
```

Neither convention is that: C has `zbar = z`, D has `zbar = z − h`. **So the
C-frame's bar-oddness is not conjugate-partition equivariance**, and hypothesis
(B) in its strong form is refuted.

## Result 4 — a distinguished fourth value, excluded twice

The unique bar-**odd** member of the full-bar class is `z = h/2`: it satisfies
`bar(z) = z − h` *and* `bar(z) = −z`, so at `z = h/2` the Markov weights **are**
conjugation-equivariant. It is recorded rather than pursued because it is
excluded twice over:

- the **two-row cap** admits exactly `{q, z_D}` (`qou-06wh`, proved complete),
  and `h/2` is neither;
- the **anchor filter** needs `z(q₀) ≈ 0.499104480185` with slope `≈ +400.29`;
  `h/2` gives **0.104530149398** with slope **0.905826877183**.

## Not claimed

No `c_k`. No value for `K`. No Q_β number moves — L2 stays at 1279 ppb. Nothing
here says a D-frame resummation is impossible; only that neither block
resolution nor conjugate-partition equivariance supplies the input entry 12
identified as missing, and that the *z*-direction is closed.

`TR[5] = z(hz+1)`, not `z³` — the σ₀σ₁σ₀ Markov weight
([`2026-05-19-trm5-markov-bug.md`](2026-05-19-trm5-markov-bug.md)); noted
because three live files were found carrying the `z³` form earlier in this arc.

## A discarded test, recorded so it is not repeated

Results 1 and 3 together suggest a **scope-(b) structural exclusion**, and it
does not survive contact with Result 3 itself. The tempting argument:

> Under D the two-row cap gives `y_(1³)(z_D) = 0`, so any correction built as a
> Markov trace is blind to the `(1³)` block. But the phase's bar-defect has
> `(1³)` component `(h²/2)/r ≈ 0.1679·h² ≠ 0` — carried by the *counit* side
> `a_(1³)·χ^(1³)(Δ)`, which the cap does not kill. Hence **no** trace-built
> correction can cancel the D-frame defect.

**It is wrong**, and Result 3 is why. The bar involution acts on the block
characters as partition conjugation, `bar(χ^(3)) = χ^(1³)`. So for a trace-built
`T = Σ_λ y_λ χ_λ`, the bar-defect of the `(3)` term is
`bar(y_(3))·χ^(1³) + y_(3)·χ^(3)` — it **does** have a `(1³)` component even
when `y_(1³) = 0`. The blindness of `T` and the blindness of `Δbar(T)` are
different questions, and only the first one follows from the cap.

Dropped before it reached a claim. It is the same shape as the arity conflation
`da-arity-conflation` warns about: a property of one object read off as a
property of a different object derived from it.

---

# Addendum — the two-anchor filter on `K(δ)`, and a reframing of entry 12

Probe: [`computations/qbeta/qbeta_n1_constant_two_anchor_filter_probe.py`](../../computations/qbeta/qbeta_n1_constant_two_anchor_filter_probe.py)
— 9/9, mpmath at 60 dps, standalone with `PYTHONPATH` stripped.

Entry 12 named `K(δ)` the arc's largest single L2 blocker and asked for a
"genuinely different input". Block resolution and Kohno–Drinfeld conjugation
both failed to supply one (above). This applies instead the technique the z-form
filter already uses — the **two-anchor filter** — to `K`.

Requiring the ladder to reproduce Q_β gives, at each anchor,
`K_required = Q_codata / (Q_A·(1 − u²)·cos(α − δ/2))`. Both anchors carry the
**same** `Q_codata_MeV` (asserted, not assumed), so the difference is a genuine
q-derivative rather than a confound between two experimental values.

## 1 — Neither admitted candidate reaches the **value**

| | miss vs `K_required` | × the 7.797 ppb target |
|---|---|---|
| `K ≡ 1` | **281380 ppb** | 36088× |
| `K = cos(δ/2)` | **221686 ppb** | 28432× |
| *gap between the two candidates* | *59694 ppb* | *7656×* ← what entry 12 measured |

**The choice between the candidates is not the blocker.** The N=1 factor is
~2.8e-4 short whichever is chosen. Entry 12 is not wrong about the gap — it is
measuring the smaller of two quantities, and the larger one was never computed.

## 2 — The **slope** misses by three orders, with the wrong sign

```
required   dK/dδ  =  +6.2399501753   (D)      +6.2934180689   (C)
K = cos(δ/2)      =  -0.0054631674           ratio  -1142.19
K ≡ 1             =   0
```

## 3 — A candidate-free self-consistency test

`K(0) = 1` plus the required value fixes `K`'s **mean** slope over `[0, δ₀]`;
the filter fixes its **local** slope at `δ₀`:

```
mean slope   -0.0128759899
local slope  +6.2399501753
ratio          -484.62
```

Any `K` meeting `K(0) = 1`, the value and the slope must have local derivative
~485× its own mean slope, of opposite sign — strongly non-monotonic on the scale
of `δ`, with nothing in the arc motivating it.

## Convention-independent, which is what makes it a statement about the form

C and D require slopes agreeing to **0.85 %** (6.2934 vs 6.2400). The
obstruction is a property of `F = cos(a − δ/2)·K(δ)`, not of the convention.

## The slope is red-teamed — unlike the z-filter's

The z-filter's slope was a 2-point secant over `dq = 1.29e-8` and carried an
explicit caveat. This one is a central difference **stable to 12 significant
figures across twelve orders of magnitude of step size** (rel `1e-8` → `1e-20`,
max spread 3e-15), and the independent two-anchor secant reproduces it to 8. It
is a derivative, not an artifact.

## Scope — read the attribution carefully

Scope (a). `K_required` is computed holding `α` at the value **the form** gives
(`α = (z−1)h/2` at `z_D` or `z_C`), and this arc's standing position is that `α`
is **not** derived. A wrong `α` is therefore absorbed into `K_required`, so this
does **not** show that `K` itself must equal 0.99972. It shows that the **pair**
`(α, K)` drawn from this form cannot reproduce both anchors — a form-level
negative, consistent with and sharper than the arc's existing conclusion that
the form must change.

Not claimed: that no `K` exists (an oscillating one exists mathematically); any
`c_k`; any movement on L2, which stays at 1279 ppb. Nothing is chosen to match
data — the required values are reported and the candidates measured against
them, so this is a filter, not a fit.
