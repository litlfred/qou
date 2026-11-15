---
# qou-wu38
title: lake-cache/qou-v4-24-0 delivers 2702 QOU oleans to the PRE-RENAME content/ path and exits 0
status: completed
type: task
priority: high
created_at: 2026-10-10T07:31:52Z
updated_at: 2026-10-10T12:30:00Z
parent: qou-n4r9
---

Found 2026-10-10 while setting up Lean verification for PR #7546 (the `*_iff*`
rename tranche, bean `qou-bybn`). This is the **fourth** instance of the
`content/` -> `folio/` rename breaking a hardcoded path, and the first one that
is not in the tree at all.

## The finding

`lake-cache/qou-v4-24-0` head is **`a792c46d01b`, 2026-09-06T12:58:26Z**
(verified via the GitHub API, not a local fetch -- the branch has had no commit
since). The `content/` -> `folio/` move landed on main in **`114b24ba5b`,
2026-09-27 18:25:38 +0000** (`qou-yqko`). So the tarball's path prefixes are
**three weeks older than the layout they extract into**.

`scripts/lean-cache-restore.sh` extracts with

    tar xzf "$tgz" -C "$REPO_ROOT"

i.e. the destination comes **from the tar entries**, not from
`.github/lake-packages.json` (which was correctly updated to
`lake-root: folio/quantum-observable-universe/lean` in the same commit as the
move). The tarball carries two kinds of entry:

| tar prefix | moved in the rename? | lands |
|---|---|---|
| `.lake/packages/*` (workspace root) | **no** | correctly |
| `content/quantum-observable-universe/lean/.lake/build/...` | **yes** | a directory that no longer exists |

Measured in this container after the restore: **2702 QOU-own oleans** were
deposited under `content/quantum-observable-universe/lean/.lake/`, where nothing
reads them, while **3480 mathlib oleans** landed correctly at the root. Both
figures match AGENTS.md's recorded per-tree seed counts exactly (`mathlib 3480`,
`QOU 2702`), which is the corroboration that this is the whole QOU-own tree and
not a partial extraction.

## Why it is SILENT, and this is the reusable half

The restore's own success check is

    count=$(find "$REPO_ROOT/.lake/packages/mathlib" -name '*.olean' | wc -l)
    echo "lean-cache-restore: restored -- $count mathlib oleans present."

It counts **mathlib at the workspace root** -- the one location the rename did
*not* touch. So the check passes, the script exits **0**, it prints
`restored -- 3480 mathlib oleans present`, and it goes on to
`lean_mathlib_url_fix` and the "verify a file with scripts/lean-verify.sh"
hint. Every QOU-own olean is in the wrong place and **no signal says so.**

The agent then runs `lean`-direct against a `LEAN_PATH` built from
`.github/lake-packages.json` (the *new* path), finds no `QOU.*.olean`, and
concludes the library was never built -- which is the wrong diagnosis and leads
to a multi-hour from-source rebuild. That is exactly the cost
`docs/audits/2026-09-07-mathlib-cache-gap-closed.md` records for the previous
misdiagnosis of this family (attributed to a container resource limit; it was 79
missing oleans).

## Why the move's own audit could not have caught it

`qou-yqko`'s pre-move measurement -- *"ZERO sites block the content/ -> folio/
move, and TWO are repaired by it"* (`a3cc2d4bcd`) -- was a sweep of **in-tree**
sites, and it was correct about them. The cache payload lives on an **orphan
branch**, outside every tree a corpus-wide audit walks. `qou-yqko` touches
`.olean` exactly once (line 260) and there only to exclude `.olean` binaries as
grep noise.

So this is not a miss by that audit; it is a surface that audit's method
structurally cannot reach. Same class as the forty-nine rows in
`docs/audits/2026-08-15-detector-blindness-taxonomy.md` -- and it belongs in that
table, because the blind spot is *the scan's universe*, not a spelling.

## The three earlier instances, for the pattern

1. `scripts/qa-sidecar-agent-union.py:88` -- hardcoded `"content/"` as a
   `git ls-tree` pathspec, so it scanned **0 of 3653** sidecars and reported a
   clean union. `git ls-tree` does **not** error on an absent pathspec. Fixed in
   PR #7546 with a `_TREE_ALIASES` tuple and a `SystemExit` on an empty scan --
   *refusing to report a clean union on an empty scan* is the part that matters.
2. `--rev`'s `DEFAULT_ROOTS` -- same shape, fixed in #7401.
3. This one.

All three are the **silent empty scan**: a hardcoded path that matches nothing
reports success rather than an error.

## Options

1. **Reseed the branch.** Correct and expensive. `qou-snh8` documents what that
   costs: a full from-source `lake build` is ~6000 modules / 2.5h+ and this
   container was reclaimed twice mid-build; the seed guard (correctly) refuses a
   partial or trace-mixed tree; and the agent proxy **rejects a single ~2.25 GB
   push** (HTTP 500, consistently) so the payload must go up as ~90 MB
   per-commit fast-forwards. CI (`lake-cache-refresh.yml`) is designed for this
   architecture but has **never run** (0 runs; `workflow_dispatch`-only under the
   2026-06-30 Actions-billing directive).
2. **Teach the restore to relocate.** After extraction, if
   `content/quantum-observable-universe/lean/.lake` exists, `mv` its contents to
   the `lake-root` that `.github/lake-packages.json` declares. Cheap (a few
   lines), reversible, and it fixes every existing stale-prefix branch at once
   rather than one reseed at a time. Needs the declaration read, which
   `scripts/lib/lake-cache-family.sh` already does.
3. **Make the check honest without fixing the delivery.** Count the **QOU-own**
   oleans at the declared `lake-root` and fail loudly when zero. Does not restore
   anything, but converts a silent wrong answer into a legible one -- which is
   the half that actually costs sessions.
4. **Do nothing.** Every agent doing Lean work here keeps getting an exit-0
   restore with no QOU library, and keeps re-diagnosing it. Three sessions have
   now paid for some version of this.

**Recommendation (judgement, not a finding): option 3 now, option 2 next, option
1 when CI billing allows.** Option 3 is in both §ASK-THE-OWNER exemptions --- it
makes a wrong answer impossible rather than tidying near one, and the corpus
already fixes what the right path is (`.github/lake-packages.json` declares it).
Option 2 changes delivery behaviour and is a larger ask. Option 1 is the only
one that makes the branch itself correct, and it is gated on infrastructure
nobody in a sandbox controls.

Note this interacts with `qou-hb5v` (migrating the family to
`cat/folio-assistant-sci/lake-cache/`): that migration moves **where the branch
lives**; this bean is about **what is inside it**. Either can land first, but a
reseed under the new name would close both at once.

## Reproduce / the workaround that works today

The restore's exit code is not evidence. Check the declared lake-root directly:

    find "$(python3 -c 'import json;print(json.load(open(".github/lake-packages.json"))["packages"][0]["lake-root"])')/.lake/build/lib/lean/QOU" \
      -name '*.olean' | wc -l

Zero after an exit-0 restore means the payload is stale-prefixed. Until the
restore is fixed, move it by hand:

    mv content/quantum-observable-universe/lean/.lake/build \
       folio/quantum-observable-universe/lean/.lake/build

That is what unblocked PR #7546 -- 2.5 s per file warm after the move, against
the multi-hour rebuild the wrong diagnosis implies.

**Do NOT verify this by re-fetching the branch into `.git`.** AGENTS.md records
the cost: two verification fetches took the repo's `.git` to 9.0 G and the
container to 402 M free, where the Bash harness cannot write its own output
capture and *every* command fails including the `rm` that would fix it. Fetch
into a throwaway repo under the scratchpad so `rm -rf` reclaims it, or -- as
here -- use the GitHub API for the branch's head and date and measure the
extracted tree locally.


## 2026-10-10 — FIXED on main by a sibling session, and the diagnosis held exactly

`94b88ccbbb` (session `016AEU7xkxdUcw9r7adTXgyr`, on main via #7546's base) takes
**option 2** of the three framed above — relocate the payload on extraction:

```sh
-tar xzf "$tgz" -C "$REPO_ROOT"
+tar xzf "$tgz" -C "$REPO_ROOT" --transform 's,^content/,folio/,'
```

Their independent measurement of the tarball confirms this bean's diagnosis
**exactly**: *"13670 `content/` members, 0 `folio/`"*. So every paper olean in the
payload was stale-prefixed, not merely some, and the 2702 counted here was the
whole QOU-own tree rather than a sample.

The same commit repaired four more rename casualties the bean did not reach —
`lean-library-sweep.py` found **0 of 3** packages, `lean-content-sweep.sh` **0**
targets against its documented 938, `lean-shadow-verify.sh` dead at three
pinning sites, and `lean-olean-cache-seed.sh`'s `SEED_PAPER=1` glob would have
seeded **0** paper oleans. That last one matters most for this bean: a reseed
under the old glob would have produced an *empty* paper tree, so the branch
could not have been repaired by reseeding until this landed.

### What is fixed, and what is NOT — do not read this closure as the class being closed

**Fixed:** delivery. The transform is a no-op once the branch is re-seeded from a
`folio/` tree, so it is correct in both regimes.

**NOT fixed: the silent success.** `lean-cache-restore.sh`'s check still counts
mathlib at `$REPO_ROOT/.lake/packages/mathlib` — the workspace-root path, which
no rename has touched — so it still cannot distinguish "payload delivered" from
"payload delivered somewhere nothing reads". Today's instance is repaired; the
**next** path change will be just as silent. That was option 3 and the
recommendation above, and it is deliberately not part of this closure.

Carried forward rather than lost: the remaining work is a check that counts
QOU-own oleans at the declared `lake-root` and fails loudly on zero. Small, and
in both §ASK-THE-OWNER exemptions by the reasoning above — but it is a change to
a gate's behaviour, so it waits on the owner rather than riding this closure.

**Measured consequence while this was open**, worth keeping as the cost record:
the two-location split it describes is what made `/prepare-merge` on #7546 read
worse than the code was. The content sweep reported RED on both changed siblings
with `Mathlib/Tactic.olean does not exist` at the *paper* path (root tree: 3480
oleans, `Mathlib/Tactic.olean` PRESENT; paper tree: 1674, absent), and the
library sweep's 2 UNVERIFIED were the same shape. Both were environment, not
corpus — the library sweep says so in its own words, *"(NOT a corpus defect on
this evidence)"*.


## 🛑 2026-10-10 (same hour) — THE "NOT FIXED" HALF ABOVE IS FALSE. It was fixed, and the fix was already in my tree.

The closure note above says the silent-success half remains open:

> **NOT fixed: the silent success.** `lean-cache-restore.sh`'s check still counts
> mathlib at `$REPO_ROOT/.lake/packages/mathlib` […] the **next** path change
> will be just as silent.

**That is wrong on every clause.** `334752248a` ("lean-cache-restore: count the
paper half, and repair a pre-rename restore", **08:41:31Z**, #7564) implements
exactly the option this bean recommended, and more:

```sh
qou_oleans() {            # counts the PAPER half at the DECLARED folio lake root
  find "$REPO_ROOT/folio/quantum-observable-universe/lean/.lake/build/lib/lean/QOU" \
    -name *.olean 2>/dev/null | wc -l | tr -d ' '
}
```

| what the closure claimed open | what `334752248a` does |
|---|---|
| check counts mathlib only | counts **both halves**; `qou_oleans` added |
| exit 0 on an empty paper half | **`exit 1`**, with the message naming the branch |
| a later run SKIPs because mathlib is present | skip now requires **both**; a mathlib-only tree **re-extracts** |
| an already-stranded restore stays stranded | `relocate_legacy_paper_trees()` **moves it into place**, and refuses when a real build exists |

Its own comment states the defect and the measurement this bean reported, from
the other side: *"3480 mathlib oleans at the root, 0 QOU oleans under folio/,
2734 paper oleans under content/."* And the new guard's comment is the sentence
this bean was holding open: *"Fail loudly on an empty paper half: exit 0 with no
QOU oleans is the silent failure this check replaces."*

### How I got it wrong, which is the part worth recording

Not staleness. **`334752248a` was an ancestor of my own branch head when I wrote
the claim** — `git merge-base --is-ancestor` confirms it, via my merge
`9667b114fa`, made *before* the closure was appended. The corrected file was on
disk in front of me; I asserted the state of a script from a commit message
(`94b88ccbbb`, the earlier `--transform` fix) instead of reading the script.

That is this corpus's most-documented failure mode — asserting a source file's
state from a record about it — committed while writing a closure whose whole
subject is a check that reports success without looking. The bean's own rule for
`y_lambda_at` says it in one line: **read at the body, not the docstring.**

**Contaminated, and corrected in both:** PR #7571's body, and the same claim
relayed in chat as "an owner call, not a follow-up commit". It was neither.

**`qou-wu38` is fully closed.** Both halves — delivery (`94b88ccbbb`,
`--transform`) and the silent success (`334752248a`) — are fixed on main. No
owner decision is outstanding on this bean.

---

## 🛑 CORRECTION 2026-10-10 — the cost figure is cited to a document that
## records the OPPOSITE, and two different gaps are conflated

Caught by a sibling agent filing the taxonomy row for this class (PR #7583),
and left to me to fix because the error is mine. Two sentences in this bean
are wrong:

1. **The citation.** This bean says a wrong "library was never built"
   diagnosis "leads to a multi-hour from-source rebuild. That is exactly the
   cost `docs/audits/2026-09-07-mathlib-cache-gap-closed.md` records for the
   previous misdiagnosis of this family (attributed to a container resource
   limit; it was 79 missing oleans)." **That document records neither half.**
   Measured: it contains the string `resource limit` **zero** times, and its
   only cost line reads *"no `lake`, no network, a few minutes total.
   Packaged: **2.3 MB**"* (line 32). It is the **3-target / 7-module** gap,
   and it states the state it found was correctly a *cache* defect rather
   than a corpus one.

2. **Two gaps, one of them cheap.** The sentence actually cited exists
   verbatim one document over —
   `docs/audits/2026-09-11-gap-cache-branch-seeded-7-to-86.md` lines 33-35:
   *"That was attributed to a container resource limit (bean `qou-ed8a` …).
   **It is not one.** It is 79 missing oleans: **188 s** to build from
   source, **22 MB** to fetch."* That is the **79-module** gap. So the bean
   merged a figure from one gap with a citation to another, and **neither
   gap cost hours**: a few minutes / 2.3 MB, and 188 s / 22 MB.

**What survives.** The structural claim is untouched: an exit-0 restore that
strands every QOU olean under `content/` makes an agent diagnose an unbuilt
library, and the repair is the one-line `mv` recorded above (2.5 s per file
warm afterwards). A *genuine* from-source QOU rebuild is expensive — AGENTS.md
puts a `lake build` Mathlib-closure rebuild at 30 min+ and records a 50-minute
run that produced zero QOU oleans — but that is **not measured in this
session and not what either cited document says.** State it as unmeasured
here, or cite the AGENTS.md figures; do not re-attach a cost to the 09-07 doc.

**Where it propagated** (all three now carry the correction): the body of
PR #7546, the body of PR #7571, and taxonomy row 55 in
`docs/audits/2026-08-15-detector-blindness-taxonomy.md`, which the sibling
filed with a *"Do not inherit the cost figure this row was first filed with"*
note rather than repeating it.

**The discipline this is an instance of, for the third time this arc:** a bean
is not a primary source. I asserted a document's content from a bean's summary
of it, in a bean whose own subject is asserting a script's state from a commit
message about it. `y_lambda_at`'s rule generalises past docstrings — **read at
the body.** Opening the file costs one `grep`; the citation survived into two
merged PR bodies.

**Status unchanged: `completed`.** Both halves of the defect are fixed on main
and no conjecture is open here — this is a correction to the record, not a
reopening.
