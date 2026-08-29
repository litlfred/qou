---
# qou-y98b
title: 'Gate the q0Anchor refill: ~50% of newly-added witnesses land unstamped'
status: in-progress
type: task
priority: normal
created_at: 2026-08-28T15:24:07Z
updated_at: 2026-08-28T15:42:09Z
---

Claimed by branch `claude/q0-anchor-refill-gate-2026-08-28`, PR #5891.

## The refill is measured on ARRIVALS, not on the standing count

Standing counts move for two reasons at once (drains and arrivals), which is
why two endpoint readings mislead. Measured instead on witness files *added*
between two revs, reading blobs out of git:

    ADDED origin/main~500..HEAD   n=101   unstamped=60  (59.4%)
    ADDED origin/main~250..HEAD   n= 44   unstamped=20  (45.5%)
    ADDED origin/main~100..HEAD   n= 31   unstamped=16  (51.6%)

**~50% of every newly-added witness lands with no q0Anchor.** The stamped half
is essentially all `proton`. Confirms qou-kx04's "growing faster than it is
being drained" with a rate rather than two counts.

Standing population, read from git at eight revisions (census excludes nothing;
raw `computations/**`):

    2026-08-10 ~3000   2887 total  2240 MISSING  77.6%
    2026-08-19 ~1500   2998        2277          76.0%
    2026-08-24 ~1000   3055        2223          72.8%
    2026-08-25  ~500   3069        2015          65.7%   <- a drain landed
    2026-08-27  HEAD   3170        2066          65.2%   <- +51 in two days

## Two numbers, both real

    raw computations/**              2066
    audit scope (live)               1678

The audit skips `_deprecated` (line 280) and `AUDIT_SUFFIXES`. The 388 gap is
bookkeeping scope, not stamping. Quote which one you mean.

## Cause partition (new: computations/audits/q0_anchor_missing_cause_partition.py)

    UNDECLARED        1199   71.5%
    NOT_BUILDER        365   21.8%
    NO_PRODUCER         55    3.3%
    DECLARED_STALE      59    3.5%
    GENERATED_MIRROR     0    0.0%

**Using WitnessBuilder is NOT sufficient to get stamped.** `build()` writes
`q0Anchor` only when the pin is POSITIVELY DECLARED — a manifest entry or
`QOU_Q0_ANCHOR`. Undeclared producers are left unstamped on purpose (defaulting
one in would assert a pin nobody established). The manifest lists 410 stems
against ~2800 producers, so absence is the common case, and 71.5% of the
missing population is exactly that gap.

`UNDECLARED` spans **1154 distinct producers** — a long tail, top producer
contributing 5. A per-producer drain is the wrong shape of fix.

## Why nothing blocks it

`q0_anchor_consistency_audit.py` IS wired into `precision-gates.sh:61` and
`witness-staleness.yml:76`, both `--strict`. But line 328 is
`if args.strict and n_flip:` — Q0_FLIP only, and Q0_FLIP is 0. The audit's own
header calls Q0_ANCHOR_MISSING "pre-backfill; not a failure". Correct for a
CONTRADICTION detector; it just means the inflow is ungated.


## OUTCOME — gate built, validated, wired (PR #5891)

`computations/audits/q0_anchor_ratchet.py` + `computations/q0-anchor-missing-baseline.json`,
wired into `scripts/precision-gates.sh` as BLOCKING with a self-test.

Follows the repo's own idiom (witness_raw_float64_audit + raw-float64-baseline):
the 1678 existing unstamped witnesses are baselined and tolerated; an unstamped
witness NOT in the baseline fails --strict; the baseline drains, never grows.

Blocking is safe here — green at its own baseline, so it can only fire on a NEW
regression. It never writes or guesses an anchor: WitnessBuilder's principle that
an undeclared producer stays unstamped is untouched.

### Validated, not asserted

- historical replay: baseline at ~500, run at HEAD -> RED with **exactly 60**,
  matching the independent added-file measurement (two methods, same number)
- --rebaseline REFUSES to grow 1627 -> 1678, file byte-unchanged; accepts a drain
- fixture test of default path resolution: backlog tolerated / new caught /
  stamped ignored / audit-emitted out of scope
- `--self-test` mutation-tested: two blinding mutants (scan dropping every hit,
  _is_in_scope excluding all witnesses) are both KILLED. A self-test that cannot
  fail is theatre.
- flag is `--self-test`, the spelling precision-gates.sh line 467 actually
  invokes. An unknown flag would make the self-test error, and the harness prints
  the same gate name either way — a gate that never ran reads exactly like a gate
  that passed.

### Corrected numbers (rev-pinned; supersede the working-tree figures above)

At cdbdc84af1, all read from git:

    UNSTAMPED          1678
    UNDECLARED         1193  71.1%
    NOT_BUILDER         356  21.2%
    DECLARED_STALE       65   3.9%
    NO_PRODUCER          55   3.3%
    INERT_DECLARATION     9   0.5%   <- NEW class

**Why the earlier figures were wrong, and it matters beyond this bean.** They
were computed against the working tree, which a concurrent agent switched to its
own branch mid-session — moving the manifest from 410 declared stems to 728
between two of my reads. Everything now reads from git at a named rev. In a
repo worked by several agents against one checkout, a working-tree measurement
is not reproducible even by its own author.

### INERT_DECLARATION — a manifest entry that cannot fire

`build()` reads the manifest, so a declaration on a producer that hand-rolls
`json.dump` never executes. Worked case found while validating:
`signed-crossing-feasibility` oscillates muon -> missing -> muon -> missing.
It was dropped by `5baf5a45c3`, whose subject is *"register the producer's real
pin"* and which DID add the stem under `physical_proton`. The producer ends in
`out.write_text(json.dumps(w, indent=2))`. The declaration reads as done and
does nothing.

### One deliberate escape hatch, named rather than hidden

Growth is permitted ONLY via `--establish "<reason>"`, which records the reason
and the added entries INTO the baseline for review. It exists because main moves
while this PR is open and those arrivals are not this branch's doing — without
it the gate blocks its own landing and the way through would be to delete the
baseline file so `prev` is empty. That hatch exists either way; this makes it
visible. It must never absorb a witness the branch itself created.

### NOT closed by this bean

The 1678 backlog. The gate stops the inflow; draining is separate work, and the
partition says how to scope it: UNDECLARED (1193) is a manifest+builder problem
over 1149 producers, NOT_BUILDER (356) needs producer migration, NO_PRODUCER (55)
are orphans needing a producer or a deletion.
