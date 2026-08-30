---
# qou-5v24
title: 'lean-direct-cone.sh and lean-axiom-guard.py disagree on freshness: verify-then-commit deadlocks the documented compose'
status: completed
type: task
priority: normal
created_at: 2026-08-26T07:08:18Z
updated_at: 2026-08-26T08:47:31Z
---

Reproduced 2026-08-26 while merging PR #5820.

The two tools use DIFFERENT CLOCKS for 'is this olean current':
  * scripts/lean_cone_build.py  -- olean mtime vs source MTIME
  * scripts/lean-axiom-guard.py -- olean mtime vs _effective_source_time, which
    for a CLEAN file is the COMMIT TIME of the last commit touching it.

Measured instance (QOU.HeckeAlgebra.MarkovTrace):
  source mtime  06:45:09
  olean mtime   06:45:12   -> rebuilder: up-to-date, SKIP
  commit time   06:47:15   -> guard: STALE, refuse (rc=2)

So the compose documented in the guard's own docstring,
  bash scripts/lean-direct-cone.sh $(python3 scripts/lean-axiom-guard.py --print-modules)
  python3 scripts/lean-axiom-guard.py
DEADLOCKS: the rebuilder will not rebuild and the guard will not report. Neither
is wrong on its own terms.

Trigger is the NATURAL workflow order: verify, then commit. Building before
committing always leaves commit time > olean mtime. It does not reproduce if you
commit first and build after.

Workaround used: delete the one olean, then rerun lean-direct-cone.sh. 4s.

Candidate fixes, not yet chosen:
  * give lean_cone_build.py a --force/-B flag (smallest);
  * have the guard treat a clean file whose CONTENT is unchanged since the olean
    as fresh -- i.e. compare content, not times. Note the guard's
    _effective_source_time docstring explains carefully why raw mtime is wrong
    (clone stamps everything), so the commit-time rule is deliberate; the corner
    is specifically clean-file-committed-after-build.
  * make the rebuilder use the guard's _effective_source_time so the two agree.

Hit a THIRD time, 2026-08-26, same session. Raising priority: this is not a one-off, it fires whenever the natural verify-then-commit order is used, which is every time.

MITIGATED 2026-08-26 (rides on PR #5822). Not yet fully fixed -- the two notions are still different, this just makes the documented path terminate.

  * scripts/lean_cone_build.py gains -B/--force, which makes fresh() always return
    False. Its docstring now states the mtime-vs-commit-time divergence and the
    exact reproduction.
  * scripts/lean-axiom-guard.py's failure message now EMITS the working command:
      scripts/lean-direct-cone.sh --force <the stale modules>
    and explains why --force is needed. Following the old message literally is
    what looped.

Demonstrated end to end on a live instance (QOU.Machinery.MarkovCosetLift, built
then committed):
  without --force:  'done: up-to-date=2 in 0s' -> guard still rc=2   (deadlock)
  with    --force:  'done: ok=2 in 4s'         -> guard rc=0         (resolved)

STILL OPEN: unifying the freshness notion so --force is unnecessary. The candidates
in the original note stand; the guard's commit-time rule is deliberate (a fresh
clone stamps every source with checkout time, so raw mtime would flag everything),
so the fix is probably to teach the REBUILDER the same rule rather than to weaken
the guard.


## FIXED 2026-08-26 — 593cdea2c4 (PR #5822)

`scripts/lean_freshness.py` now holds the ONE definition; both tools import it.
The rebuilder gates on `effective_source_time` — the same commit-time rule the
guard uses — so it can no longer call fresh an olean the guard calls stale.

`-B/--force` (68b2634a3e) was the first fix and was a workaround: it made the
operator supply by hand the agreement the tools should have had. It survives as a
manual override; the guard's failure message no longer prescribes it.

Commit time is also the RIGHT rule for the rebuilder on its own merits, not merely
for agreement: a clone stamps every source with the checkout time, later than any
olean restored from a build cache, so the old mtime rule recompiled a correctly
restored cache. Verified live — a clean source with mtime 07:35:14 against an olean
of 07:24:45 now reports `up-to-date=2 in 0s`; the old rule would have rebuilt it.

Verification (all with LEAN_PATH via lean-direct-env.sh):
  * genuinely edited source still rebuilds: `ok=1` in 2s
  * documented compose end to end: rebuilder `ok=10, up-to-date=197 in 29s`,
    then guard rc=0 — it terminates
  * guard `--selftest` PASS

Also fixed here: dirty-set matching is worktree-relative rather than cwd-relative
(a cwd-relative path silently fails to match `git status` output, making an edited
file read as clean), and the guard prints its own registry size — PR #5822's body
said 53 entries against a measured 51.


## CORRECTION 2026-08-26 — the commit-time fix above was itself defective (d5d76e6f01)

The entry above says commit time is "the RIGHT rule for the rebuilder on its own
merits". **That is wrong**, and I found out by merging main into the branch rather
than by reasoning about it.

Merging 45 commits of `main` dated EARLIER than my local oleans:
`QOU.AlgebraicSubstrate.qou_obstruction_reduction` **changed in the merge**, commit
time 07:38:27, existing olean 07:40:35. Commit time calls that fresh and serves a
build of the old source. The mtime rule it replaced would have caught it.

So each clock is wrong exactly where the other is right:
  * mtime -> STALE after a clone/cache restore (2026-08-15, 15 modules)
  * commit time -> FRESH when merged content is older-dated than the build

**Content decides.** The rebuilder now stamps every olean with the SHA-256 of the
source it was built from (`<olean>.srcsha`, under gitignored `.lake/`), and
`olean_is_current` compares hashes when a stamp exists — no clock consulted.

Where no stamp exists the two callers want OPPOSITE errors, so the fallback is
asymmetric: rebuilder must beat BOTH clocks (may over-rebuild, never serves
stale); guard uses commit time only (never refuses to report on a fresh clone).
Since max(commit, mtime) >= commit the rebuilder's stale set CONTAINS the
guard's, so a rebuild always satisfies the guard — that containment is what keeps
the deadlock fixed, and the self-test asserts it over four clock configurations.

`scripts/lean_freshness.py --selftest` — 11 checks, PASS — exists because this
shipped broken once. It runs the clocks backwards on purpose; no test that does
not would have caught it.

Verified on the merged tree (main +45): rebuilder ok=4 / up-to-date=203 of 207,
all stamped; the module that exposed the bug now reports current=False; guard
rc=0 on 51; both selftests PASS.
