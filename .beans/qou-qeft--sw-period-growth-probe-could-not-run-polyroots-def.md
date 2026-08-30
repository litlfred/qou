---
# qou-qeft
title: 'sw_period_growth_probe could not run: polyroots default maxsteps too low at a double root'
status: completed
type: bug
priority: normal
created_at: 2026-08-30T14:35:36Z
updated_at: 2026-08-30T14:35:36Z
---

Found while working `qou-0hnz` (it was the one Q1 file that produced no witness);
diagnosed and fixed 2026-08-30.

## Symptom

`computations/sw_period_growth_probe.py` aborted before doing any work:

```
File ".../sw_period_growth_probe.py", line 52, in <module>
    roots = sorted(mp.polyroots([1, zk + 1, zk**2 + zk + 1, zk**3 + zk**2 + zk + 1]), ...)
mpmath.libmp.libhyper.NoConvergence: Didn't converge in maxsteps=50 steps.
```

Initially recorded as "pre-existing, independent of the pin" — correct, but not
a diagnosis.

## Cause

`z_k` is a **branch point**, taken as a root of the discriminant, so the cubic
has a genuine **double root** there. That is the very thing the next two lines
assert (*"gap → 0 ⇒ square-root branch, exponent 1/2"*). mpmath's `polyroots`
uses Durand–Kerner, which degrades to linear convergence on a repeated root, so
the default 50 iterations cannot reach the tolerance implied by the ambient
`set_compute_dps()`.

**The failure is precision-dependent**, which is why it looked arbitrary:

| dps | result |
|-----|--------|
| 15 | OK |
| 30 | OK |
| 50 | NoConvergence |
| 60 | NoConvergence |

So the probe worked until the ambient dps was raised, then silently became
unrunnable.

Ruled out: coefficient accuracy. Feeding the discriminant's **exact rational**
coefficients instead of the current `complex(c)` float64 cast does **not** fix
it — this is the repeated root, not the input precision.

## Fix

`maxsteps=200` on that one call. Works at every dps tried.

It sharpens the result rather than merely unblocking it: the measured minimum
sheet-gap falls with precision — 4.5e-16 at dps=30, **4.17e-26** at dps=50 —
which is the signature of a true double root and exactly what the probe asserts.

## Notes

- This producer writes **no witness**, so nothing needed regenerating.
- The `complex(c)` cast on the discriminant coefficients is a float64 that does
  not enter any witness (there is none), so the ratchet never saw it. Left
  alone: it is not the cause, and changing it would be unmotivated churn.
