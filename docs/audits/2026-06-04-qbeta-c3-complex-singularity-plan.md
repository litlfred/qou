# c_3 complex-singularity probe — the genuine (non-real-q) direction (plan)

**Date:** 2026-06-04
**PR:** (this branch — `claude/qbeta-c3-complex-singularity-probe-2026-06-04`)
**Status:** DONE — see [verdict](2026-06-04-qbeta-c3-complex-singularity-verdict.md) (b ≈ 4.4e-7; framing supported, root-of-unity refuted)
**Registry:** [`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)

## Why

The c_3 cross-anchor rigidity falsification
([`2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`](2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md))
proved **no real-q formula `c_3 = f(q)` can track the empirical c_3 swing**
(`dc_3/dq ≈ 4.6×10⁶`). [`AGENTS.md`](../../AGENTS.md) §"Im(q) at fibre vs
observable level" says the genuine object must be **complex-analytic /
root-of-unity** at the fibre level. This probe tests that framing concretely —
the only legitimate remaining direction for c_3 (and the residue-A precision
unblock).

## Concrete, falsifiable test

A function whose value `c_3 ≈ -2` has derivative `dc_3/dq ≈ 4.6×10⁶` near q₀
is dominated by a **nearby singularity**. The characteristic distance to that
singularity is

```
b ≈ |c_3| / |dc_3/dq|.
```

Two falsifiable checks:

1. **Complex-analytic framing:** is `b` tiny (near-real singularity) — the
   signature of a fibre-level complex-analytic Habiro element, NOT a smooth
   real-q function (since `b → 0` implies a diverging derivative, which is
   impossible for a smooth `f`)?
2. **Root-of-unity mechanism:** for real q₀ ≈ 1.11 (just outside the unit
   circle) the nearest root of unity is `ζ₁ = 1`, at distance `|q₀ - 1| ≈ 0.11`
   (every other `ζ_n = e^{2πik/n}` is farther). Is `b` comparable to that, or
   `b ≪ 0.11`? If `b ≪ 0.11`, roots of unity are **too far** to be the
   mechanism — refuting that specific sub-hypothesis while leaving the
   complex-analytic framing intact.

Inputs (published anchor values, from the falsification doc):
`c_3(proton q₀) = -2.0693`, `c_3(muon q₀) = -2.0097`, `Δq ≈ 1.28×10⁻⁸`.

## Anti-pattern guards

- This is a **feasibility / geometry** probe, NOT a closure attempt. It pins
  the singularity distance; it does NOT produce a categorical c_3 formula.
- TIERED honesty: report what is supported (framing) vs refuted (root-of-unity
  mechanism) vs open (the actual element).
- ℏ_q / q₀ from canonical values; diagnostic-only.

## Deliverables

```
docs/audits/
  2026-06-04-qbeta-c3-complex-singularity-plan.md      # this file
  2026-06-04-qbeta-c3-complex-singularity-verdict.md   # verdict
computations/qbeta/
  qbeta_c3_complex_singularity_probe.py
  qbeta-c3-complex-singularity-probe.witness.json      # auto-emitted
```
