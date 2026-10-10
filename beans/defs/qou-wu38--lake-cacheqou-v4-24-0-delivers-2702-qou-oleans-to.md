---
# qou-wu38
title: lake-cache/qou-v4-24-0 delivers 2702 QOU oleans to the PRE-RENAME content/ path and exits 0
status: todo
type: task
priority: high
created_at: 2026-10-10T07:31:52Z
updated_at: 2026-10-10T07:31:52Z
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
