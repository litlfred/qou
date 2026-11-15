---
# qou-iav7
title: threerow_isospin_parity_probe has the same C/D straddle as qou-qdtk, and emits NO witness
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T19:29:30Z
updated_at: 2026-11-15T17:20:00Z
parent: qou-5vkl
---

FOUND 2026-08-25 while draining `qou-qdtk` (PR for that is in flight). Not previously
identified by the #5762 audit or by `qou-qdtk`'s own diagnosis — it is a FOURTH
instance of the class, reached by grepping for the symbols `qou-qdtk` removed.

## The defect — identical straddle, independently hardcoded

`computations/deltalambda/threerow_isospin_parity_probe.py`:

```
  82  U_STAR = mp.findroot(lambda u: -u**6 - u**4 + u**3 + u**2 + 1, mp.mpf("1.13"))
  83  Q_STAR = U_STAR ** 2                          <- convention C's pole
 101      Q, QR = _wenzl_constants(q)               <- convention D, r = 2
 159      print(f" real-level branch (1, q*), q* = ...; ray (q*, 4] is DIAGNOSTIC")
 198      br  = scan(f, Q_LO, Q_STAR * (1 - 1e-5), ...)
 199      ray = scan(f, Q_STAR * (1 + 1e-5), Q_RAY_MAX, ...)
```

It does NOT import these from `threerow_qcross_trend_probe` — it is an independent
copy of the same convention-C constant. So fixing that probe does not fix this one,
and a grep for importers finds nothing.

Its object is again the ≥3-row sign crossing, which convention D sets to zero
(`schurPrincipal_eq_zero_iff`, `wenzlLevel_conventionD`). Under D there is no pole, so
the "real-level branch (1, q*)" and the "DIAGNOSTIC ray (q*, 4]" are a partition of
`q > 0` into two halves either side of a point with no significance — and the crossings
being scanned for are round-off in an identically-zero object.

## Why this one is WORSE than qou-qdtk, and should not just be copied over

**It emits no witness.** `find computations -name "*isospin-parity*"` returns nothing.
Per AGENTS.md's probe discipline, that is the more dangerous case, not the safer one:
*"a witness is a number that gets re-derived; a probe conclusion is an ARGUMENT that
gets written into a bean, an audit doc, a PR body and a content block, where nothing
re-derives it."* So there is no green-but-vacuous witness to correct here — the damage,
if any, is already downstream in prose. **Whoever takes this must first grep for where
its conclusions landed** (bean `qou-prjo`, #4832, and any audit doc citing an
isospin-dependent crossing) rather than starting from the file.

## Its own thesis may be independently sound — check before retiring

Unlike `qou-qdtk`, this probe's headline argument is a *confound* argument: that among
{D(1,1), T(1,2), ³He(2,1), ⁴He(2,2)} isospin and strand count move together, so the
four points cannot separate "Z=N" from "n an even multiple of 6". That reasoning is
combinatorial and does not depend on the convention at all — it may survive intact even
though the numerical crossing scan beneath it does not. Retiring the whole file would
discard it. Read the two apart.

Its cost table (Σ_λ (dim V_λ)² = n! exactly; n=18 ≈ 14 years/grid point) is likewise
convention-independent and worth keeping.

## Not attempted here

`qou-qdtk`'s PR rewrites one probe; this is a second full rewrite with a different
thesis, so it is recorded rather than bundled. Scope-(a), about this probe.


## CORRECTION 2026-08-25 — "emits no witness" was the right observation, wrong reason

This bean says the probe **emits no witness**, and infers from that its conclusions
live only in prose. The observation stands — `find computations -name "*isospin-parity*"`
returns nothing — but the reason I gave was wrong, and the difference matters.

The probe **does** build one: `WitnessBuilder("threerow-isospin-parity", ...)` at line
241, `w.save()` at line 297. It is not witness-less by design. **It never gets there.**
Measured: the ⁴He leg reports `ETA 1248s` at grid point 2 of 26, and the file's own
cost table gives `Sum_lam (dim V_lam)^2 = n!` exactly, i.e. n=18 at ~14 years per grid
point.

So it is an **unfinishable** probe whose witness is absent because the run never
completes — not a probe that chose to record nothing. Practical consequences for
whoever takes this:

- Its conclusions still reach beans and docs unverified, so the "grep for where its
  conclusions landed first" instruction above is unchanged.
- But there is no stale committed witness to correct, and there never was one to go
  stale. Do not go looking for it.
- Any repair must decide what the probe is FOR at a runtime it can actually reach.
  Re-running it to regenerate a record is not an available option.

Related: its one self-fulfilling assertion (`isospin_pattern_survives_fixed_n_control`,
`add_assertion(name, holds, holds)`) is fixed in the `qou-ploj` PR — patched by AST and
verified well-formed, but **not executed**, because the probe cannot be run to
completion here. Flagged rather than claimed as verified.


## RESOLVED 2026-08-25 — it now completes in 0.8 s, and says something true

Repaired rather than retired: two of its three parts are convention-independent and
were worth keeping. It runs to completion and emits the witness it never previously
reached.

**Corrected figure from this bean.** Above I wrote "n=18 ≈ 14 years/grid point",
carried from the probe's own table. That table hardcoded `32.0 s/pt` at n=12. Measured
on this container: **54.5 s/pt** (one grid point, ⁴He at q₀). Every projection was
understated by ~1.7×, so n=18 is **23.1 yr/grid point**, not 14. The conclusion —
⁶Li/⁷Li out of reach by orders of magnitude — is unaffected.

### What it cannot do, measured

`F_iso` sums only `len(lam) >= 3`, which convention D sets to zero for every `n`. So the
controlled test returns the same answer for every isospin class *because it returns
nothing*. Whole n=6 control, 0.6 s:

```
 case  (Z,N)  class    F(1.001)   F(1.05)   F(q0)    F(1.2)     F(2)
 D     (1,1)  Z=N      0.0        0.0       0.0      7.42e-51   1.88e-46
 pp    (2,0)  Z!=N     0.0        0.0       0.0      4.60e-51   2.12e-46
 nn    (0,2)  Z!=N     0.0        0.0       0.0      7.41e-51   1.57e-46
```

### The trap, and it is this probe's own design that builds it

Those residuals are round-off, they are **(Z,N)-dependent** — the braid word is by
construction the only varying input, so the noise is exactly what varies with isospin —
and the ordering is **not stable in q**: `D > nn > pp` at q=1.2 inverts to
`pp > D > nn` at q=2.0. A bisect-on-sign-change over that yields isospin-correlated
crossings that are artifact, and the old verdict (`predicted == observed` over
`crosses_below_q0`) would have reported them as a surviving pattern.

**A well-designed control over a null object manufactures precisely the correlation it
was built to test for.** That is the generalisable lesson, and it is worse than an
ordinary stale record: the better the control, the more convincing the artifact.

### The unfinishable leg is unnecessary, not merely expensive

The n=12 sweep is ~71 min measured. It is not run — and does not need to be, because
the vanishing is proved for **all** n, so no compute returns anything but zero. 70 of
77 partitions at n=12 are weight-zero. That is the resolution to "what can it compute
at a runtime that exists": the expensive part was never the part that carried the
answer.

### Kept, dropped, added

- **Kept**: the confound argument (Z=N ⟺ A even across all six — verified, assertion),
  the cost law `Σ dim² = n!`, the interface census.
- **Dropped**: C's `U_STAR`/`Q_STAR`, the "real-level branch", the "diagnostic ray", the
  crossing sweep, `scan()`/`bisect()`, and the verdict-from-noise.
- **Added**: four real assertions with independent expectations —
  `wenzl_level_is_constant_two`, `controlled_object_is_structural_zero` (null tolerance
  1e-30, chosen once against the C-era O(1) magnitudes and f64 noise),
  `residual_ordering_is_unstable_in_q`, `a_ladder_confound_holds`.

### One thing I nearly shipped

Making the probe finish meant its cost table finally reached a witness — and the
raw-float64 ratchet flagged **26 raw float64 fields** that had been latent in the file
all along, invisible only because it never completed. `Σ dim²` and `n!` are exact
integers, so `float(21!)` was discarding precision for nothing; they are now `int`, and
the ratios/projections are `mpf`. Zero raw float64 in the emitted witness.

**Scope-(a), about this instrument.** The isospin question is neither answered nor
refuted. A probe that could address it must be built on an object D does not annihilate.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-25 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-11-15 closed (owner card)

The convention-D repair landed 2026-08-25. The last defect was a crash: an `mpf` in an
f-string with `:.0f` stopped the probe before `w.save()`. Fixed in PR #7932 (commit
799617af8): exit 0, 0.5 s, 4/4 assertions. Instrument bean only — the isospin question
itself stays open; this probe cannot address it under convention D.
