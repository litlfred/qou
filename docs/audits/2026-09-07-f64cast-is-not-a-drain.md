# F64_CAST is not a drain: it is 105 ports, and LAUNDERED's fix does not apply

**2026-09-07.** Written on `claude/f64cast-stage1-isolated-2026-09-07`, a branch
opened to drain "stage 1" of the F64_CAST tranche and closed without draining
anything. The measurement is the deliverable.

## What was planned, and why it was wrong

`qou-840k` records 188 `F64_CAST` sites over 105 files, and a four-stage plan
whose stage 1 was *"the 29 isolated files / 46 sites — witness-free and imported
by nobody, so local, verifiable in place, no published number moves."* The plan
also said 74 % of the tranche shares one origin (`q_parameter.Q`) and therefore
**one repair pattern**, naming the fix `qou-b7cf` had just established:
`_Q = q_at(mp.mp.dps)`.

Both halves of that were checked before editing. The isolation half holds. **The
repair half does not, and the two tiers are opposite defects.**

## LAUNDERED and F64_CAST are inverse operations

    LAUNDERED   mpf(str(Q))     an mpf is CONSTRUCTED from a float64
    F64_CAST    float(Q)        an mpf is DESTROYED into a float64

In the LAUNDERED case the float64 is an accident of construction: the producer
wanted a high-precision `q` and reached it through a 17-digit string. `q_at(dps)`
fixes it in place, the surrounding code is already mpmath, and nothing else
moves. That is why it drained 34 → 0 in a day.

In the F64_CAST case the cast is **deliberate and load-bearing** — it sits at the
boundary of a float64 kernel that cannot accept an `mpf`. Measured over the 46
isolated sites:

| shape | n |
|---|---:|
| rebinds the name to float, destroying the mpf (`q0, qi0 = float(q0), float(qi0)`) | **38** |
| passes `float(...)` straight into a call (`build_seminormal_fast(shape, float(q0))`) | **11** |
| isolated files using numpy or a float-typed signature | **17 of 29** |

`build_seminormal_fast` is declared `def build_seminormal_fast(shape, q: float)`.
Substituting `q_at(mp.mp.dps)` at its call site does not raise the precision of
anything — it hands an `mpf` to a function typed for a float, and the arithmetic
inside it (`1.0 /`, numpy) is float64 regardless.

**So there is no in-place fix.** Each site is a *port of the kernel behind it*,
which is precisely the work `qou-b7cf` scoped out as "de-floating the probe
bodies … a separate, larger job". F64_CAST is 105 of those jobs, not one pattern
applied 188 times.

This also explains the drain rates, which otherwise look inconsistent:
LAUNDERED 34 → 0 in a day; F64_CAST 222 → 188 in a month.

## A second finding: 12 of the 29 are fit-search scripts

`derive_b2.py` is the clearest. It reads the AME deuteron binding as `target`,
casts every constant to float, and loops combinations of
`quaternion_quantum = 2.277455`, `kashiwara = 1/32`, `E0`, `me`, `g8` looking for
a product that lands on it. Twelve of the 29 isolated files match that shape
(`target` / `best` / `combination`).

Raising the precision of a search for a numerical coincidence does not make it
less of one. Under 🟥 NO FITTING these files want a **disposition** — is this a
recorded historical search, or something that feeds a claim? — before anyone
spends effort on their arithmetic. Precision is the wrong axis for them entirely.

## Corrected disposition for `qou-840k`

1. **The stage plan is withdrawn.** Stage 1 was defined by *risk* (does a fix move
   a published number) and that was the wrong axis. The axis that decides the
   work is **what sits behind the cast**.
2. **Re-stage by kernel**, if it is staged at all: sites whose receiver is already
   mpmath-capable are genuinely small; sites whose receiver is a numpy or
   float-typed kernel are ports and should be counted as such.
3. **Triage the 12 fit-search files separately**, on the anti-fit axis, not the
   precision one.
4. **Do not quote "74 % share one repair pattern."** They share one *origin
   constant*. The repair is a property of the receiver, not the source.

## What was NOT done, deliberately

No file was edited. A 29-file PR applying `q_at(mp.mp.dps)` to these sites would
have compiled, passed the F64_CAST gate by removing the matched shape, and
changed no result — the arithmetic downstream is float64 either way. That is the
shape of a green gate over an unchanged defect, which is the failure mode the
whole precision-gate family exists to prevent.
