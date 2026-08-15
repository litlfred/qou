---
# qou-52i4
title: Seed lake-cache/qou-v4-24-0 orphan branch after full build (preserve for next agent)
status: in-progress
type: task
priority: normal
created_at: 2026-07-13T15:55:00Z
updated_at: 2026-08-15T15:53:58Z
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

---

## Seeded and verified 2026-08-09 — NOT yet promoted

Seeded from the fully-drained tree (bean qou-rc7b: `lake build` exit 0,
1681/1681 modules).

    branch:  lake-cache/qou-v4-24-0-test
    oleans:  5267  (3590 deps + 1677 own)
    traces:  5267/5267 (100%)
    verify:  clean-clone restore replayed all 5267 — own=1677, traces=100% OK

**Not a downgrade.** Candidate tarball is 1.84 GB / 21 parts against
production's 1.53 GB / 18. An earlier note in this session worried the reseed
would shrink Mathlib coverage; that was measured pre-drain at 888 own oleans
and no longer holds.

### Why it had never been promotable

`scripts/reseed-lean-cache.sh` phase 5 parsed the OLD status format
(`traces: N (P% coverage)`) while `lake-cache.sh status` prints
`traced: N/M oleans (P%)`. The capture came back empty, `${cov:-0}` made it 0,
and the gate died with "verify FAILED: trace coverage 0%" — on a tree whose
own output two lines above read 100%. Since `--promote` implies verify,
**the reseed workflow could not publish at all.**

Phase 2 reads the same line and had already been fixed; its comment even warns
the two are coupled. Fixed in folio-assistant (`claude/agent-stalled-pickup-n79db3`,
commit 46febe3) by routing both phases plus the two regression-check counts
through three shared readers. Verify now reports `own=1677, traces=100% OK`.

### Remaining

Promotion force-pushes the production branch and was **blocked by the sandbox
permission classifier** — correctly; it rewrites a branch everyone pulls. The
run is one command, gated on verify + the no-shrink check:

    bash scripts/reseed-lean-cache.sh --repo /workspace/qou --package qou --auto-promote --yes

Note the no-shrink guard is inert here: it reads counts from the production
branch's commit message, and the incumbent's message
(`seed lean cache @ v4-24-0: lake-oleans.tgz.part17 ...`) predates count
recording, so `prod_counts` returns empty and the check passes by default. The
manual size comparison above is what actually establishes no regression.

Incumbent backed up at `lake-cache/qou-v4-24-0-pre-2026-08-08` -> 3068be7b23.

---

## Re-seeded from merged main 2026-08-09 — verified, still not promoted

The earlier candidate predated PR #4785's merge, so it was re-seeded from
`main` @ `258d802ed6` after a clean build:

    build:   exit 0, 1728/1728 modules
    branch:  lake-cache/qou-v4-24-0-test
    oleans:  5319  (3591 deps + 1728 own)
    traces:  5319/5319 (100%)
    verify:  clean-clone restore replayed all 5319 — own=1728, traces=100% OK

Third consecutive growth against the incumbent (888 own pre-drain -> 1677 ->
1728), so promotion is not a downgrade on any reading.

**Promotion attempted and refused by the sandbox permission classifier**, twice.
Correctly — it force-pushes an orphan branch that every consumer pulls. The run
is one command, and it is gated on verification plus the no-shrink check:

    bash scripts/reseed-lean-cache.sh --repo /workspace/qou --package qou --auto-promote --yes

Caveat on that gate, unchanged from the note above: the no-shrink guard reads
counts out of the production branch's commit message, and the incumbent's
message predates count recording, so `prod_counts` returns empty and the check
passes vacuously. The size comparison recorded here is what actually
establishes no regression — not the guard.

Verify itself only started working today: phase 5 had been parsing a status
format `lake-cache.sh` no longer prints, so it read 0% on a 100% tree and
`die`d. Fixed in folio-assistant PR #88 (`46febe3`). Before that, promotion was
unreachable regardless of permissions.

Incumbent still backed up at `lake-cache/qou-v4-24-0-pre-2026-08-08` ->
`3068be7b23`.


---

### Note from another session (2026-08-15, `qou-xz6t` / branch `claude/mtcx-7c-verify-close-2026-08-15`) — NOT a takeover

Not claiming or resolving this bean; leaving one measured fact that bears directly on it, because the mistake it prevents is easy to make.

**A `lean-direct` corpus build is NOT a cache-seeding candidate.** While surveying the tree with `scripts/lean-direct-cone.sh --all -k` (for `qou-kljb`), this container accumulated ~1,490 QOU oleans. Measured in the same build dir:

```
oleans: 1493
traces: 0          # zero, and 0/50 sampled newly-built oleans have a .trace sibling
```

`scripts/lean_cone_build.py` contains no trace handling at all — by design, since its whole purpose is to bypass Lake. So those oleans are exactly the artifact class this bean's own table calls worthless: untraced oleans that Lake treats as stale and evicts (bean `02kc`), which is the incumbent cache's recorded defect (775/7268 traced, ~11 %).

The distinction this bean turns on therefore still stands: **only a real `lake build` run produces the traced set** described in the claim above (4459/4459, 100 %). A future agent who sees a container with a mostly-built QOU tree should check `find … -name '*.trace' | wc -l` before treating it as a reseed candidate — a full-looking olean count is not evidence of a seedable cache.

The `would_shrink()` decision recorded above is untouched and still needs the owner's call.
