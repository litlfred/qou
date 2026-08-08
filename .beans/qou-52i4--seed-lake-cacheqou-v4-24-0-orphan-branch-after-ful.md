---
# qou-52i4
title: Seed lake-cache/qou-v4-24-0 orphan branch after full build (preserve for next agent)
status: in-progress
type: task
created_at: 2026-07-13T15:55:00Z
updated_at: 2026-07-13T15:55:00Z
---


## Claimed 2026-08-08 — branch `claude/sorry-audit-joo5`, PR #4785

This container holds exactly what 9h6x says the reseed needs: a tree produced by
real `lake build` runs, so the `.trace` files exist.

`lake-cache.sh status` here:

```
oleans:  4459  (deps + own)
own pkg: 888
traced:  4459/4459 oleans  (100%)
```

Against the incumbent `lake-cache/qou-v4-24-0`, as recorded in
`folio-assistant/scripts/lake-cache.sh`'s own comments and bean 9h6x:

| | incumbent | candidate |
|---|---|---|
| oleans | 7268 | 4459 |
| **own `QOU.*` oleans** | **0** | **888** |
| traces | 775 (~11%) | **4459 (100%)** |

The candidate is smaller in raw dependency count and better on both dimensions
that decide whether a cache does anything: it carries the paper's own modules
(the incumbent carries none — the exact defect `cmd_seed`'s `own == 0` guard was
written for) and every olean has its trace, so Lake honours rather than evicts
them.

**Expected obstacle:** `would_shrink()` refuses a candidate below 90% of the
incumbent's olean count, and 4459 < 0.9 × 7268. That guard is right in general
and wrong here — it would block the fix for the defect it was written to catch,
because it counts oleans without asking whether Lake will trust them. Resolving
that (a `--force` with the reasoning recorded, or a guard that weights traced
oleans) is the decision this bean now turns on; not forcing it silently.

## Guard verdict + a reordering (2026-08-08)

`lake-cache.sh seed` **succeeded** — `would_shrink()` did not trip, because the
incumbent branch carries no recorded counts (hand-seeded, so `branch_counts`
returns nothing and the guard is skipped). So the 4459-vs-7268 obstacle predicted
above is not actually enforced. The script stops short of pushing by design:

> Manual by default: seeding force-pushes an orphan branch, which is
> destructive and should be a deliberate act.

**Incumbent backed up before anything destructive:**
`lake-cache/qou-v4-24-0-pre-2026-08-08` → `3068be7b23` (2026-08-07 00:11,
18 parts). The reseed is now reversible with a single `git push -f` back.

### Why I did NOT push yet — a loss the "reseed" framing hides

Seeding from the tree as it stood would have shrunk mathlib **6990 → 3312**
oleans. For `lake build` consumers that costs nothing (untraced oleans are
evicted anyway, so the incumbent's extra 3678 are dead weight). But the
**sibling verifier does not use `lake`** — `scripts/lean-verify-siblings.sh`
runs `lean` directly against a LEAN_PATH into the restored oleans, and `lean`
does not check traces. For *that* consumer the incumbent's untraced mathlib
oleans are perfectly usable, and shrinking the cone would turn working
verifications into "cache-cone miss" neutral-skips (bean 2ti7 documents that
skip path).

So the naive reseed trades one consumer's breakage for another's.

### The fix: drain first, seed second

The wide-glob build (bean qou-rc7b) compiles 785 previously-unbuilt QOU modules,
and their mathlib dependencies come along with it — with traces, since it is a
real `lake build`. Sequencing the drain before the seed produces a cache that is
better on **both** axes (more mathlib *and* more QOU *and* 100% traced) instead
of trading one for the other.

Drain build started; seed to be re-run from the enriched tree afterwards. Note
the seeder deletes its `mktemp -d` on exit, so the parts do not survive the run —
the final seed must be the one that pushes.
