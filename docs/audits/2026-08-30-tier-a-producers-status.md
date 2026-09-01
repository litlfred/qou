# Tier-A producerless witnesses: all four addressed — 2 producers, 2 findings

**Date:** 2026-08-30 · **Bean:** `qou-nro6` · **Upstream:**
[`2026-08-30-orphan-witness-triage.md`](2026-08-30-orphan-witness-triage.md)

The triage found four producerless witnesses that the paper consumes. All four
are now addressed. **Two got producers; two got findings, because writing a
producer would have been the wrong act.**

| witness | disposition |
|---|---|
| `hecke-core-symbolic-migration` | **producer written** — and its first run **FAILS**; see [audit](2026-08-30-hecke-symbolic-migration-check-now-fails.md) |
| `whitehead-volume-identification` | **producer wired** — the script existed and only printed; verified reproducing before wiring |
| `canonical-mass-table-242ppb` | **finding**, no producer — it disagrees with the code it cites, in both directions; see [audit](2026-08-30-canonical-mass-table-242ppb-disagrees-with-live-code.md) |
| `4he-binding-full-pipeline` | **finding**, no producer — this document |

Orphan count: **19 → 17**, measured.

## `4he-binding-full-pipeline` — why no producer here

Three facts decide it, and they point the same way.

**It declares itself float64.** `"precision": "f64_numeric_fallback"`. Under the
NO-FLOAT64 discipline a new producer may not carry float64 arithmetic, so a
producer would have to compute in `mpmath` — which changes the numbers. The
choice is therefore not "add provenance" but "recompute at a different
precision", and those are different acts.

**The Lean uses it qualitatively.** `BraneGeometricResummation.lean`:

> *The un-damped raw sum diverges at the archimedean substrate `q₀ > 1` (the
> `tower_MeV ≈ 2×10⁶` blow-up in `4he-binding-full-pipeline.witness.json`); the
> ℏ²-damping is exactly what makes the archimedean evaluation converge.*

The claim is **divergence**. `tower_MeV = 1987648.67` carries it by being huge,
not by its digits. An mpf recomputation would move the digits and leave the
Lean's statement untouched — which is the good case, but it means the
recomputation buys the Lean nothing.

**It is a 15-minute compute.** The witness records
`canonical_time_sec = 633.6`, `kahler_time_sec = 297.2`, `time_sec = 930.9`.
Not prohibitive, but not free either, and per the long-compute logging
discipline it needs a teed log and progress output rather than a blind run.

Its own `scriptFile` already reads *"(legacy — no matching producer found;
provenance pending manual triage)"* — it is honest about its state — and
`content/values/registry.ts` records that a prior agent **de-pinned** a value
from it, calling it *"a producerless artifact whose own run is recorded as a
FAILURE"*. So the corpus has already partly quarantined it.

### What is actually needed

An author decision:

- **Recompute in `mpmath` and update the witness.** Honest and reproducible;
  costs ~15 min of compute plus the pipeline reconstruction; moves numbers the
  Lean cites (though not its claim). The right end state if the ⁴He un-damped
  tower is still a live object.
- **Mark it `auditOnly` and leave the numbers.** Cheap, changes nothing, and
  matches what it already says about itself. Keeps the Lean citation valid,
  since the citation is qualitative.
- **Retire it** if the un-damped tower has been superseded — the `B_MeV`
  1987649 it reports is not a physical prediction, it is the divergence being
  demonstrated.

**My recommendation, marked as judgement:** option 2 now — mark it `auditOnly`,
which is what it already is in substance — and open the mpf recomputation as
its own bean if anyone still needs the tower numerically. Writing a float64
producer to reproduce float64 numbers would satisfy the orphan audit and
violate the precision discipline, which is the wrong trade.

## Scope

Two producers were written and are committed. **No number was recomputed for
the two findings, no manifest was edited, and no witness was retired.** The
disagreements reported are measurements; which side is correct is not claimed
in either case.
