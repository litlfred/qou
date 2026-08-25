---
# agrd
title: 'Keystone axiom guard still cannot run: the full QOU root import is not buildable here'
status: completed
type: task
priority: normal
tags:
    - qa-gate
    - lean
    - infrastructure
created_at: 2026-08-10T05:00:00Z
updated_at: 2026-08-10T05:00:00Z
---

`scripts/lean-axiom-guard.py` — the keystone `#print axioms` gate, whose whole purpose is
to catch a declaration that silently starts depending on `sorryAx` — **could not run at
all**, and the reason was invisible.

**Half fixed (2026-08-10).** `scripts/lean-direct-env.sh` built `LEAN_PATH` from
`find .lake …`, i.e. **relative** paths. The guard writes its probe to a **temp file** and
runs `lean` there, so every entry missed and it failed with

    error: unknown module prefix 'QOU'
    No directory 'QOU' or file 'QOU.olean' in the search path entries: …

while `QOU.olean` sat in a listed directory the whole time — a maximally misleading
message. The env script now roots its `find` at the script's own repo and emits absolute
paths, fixing every consumer at once.

**Still broken, and this is the bean.** With the path fixed the guard gets further and
reports a genuinely missing olean:

    object file '…/QOU/BraidsAndKnots/PlancherelNormalisation.olean' … does not exist

The guard imports the **`QOU` root**, which transitively needs the whole tree built. This
container's build state is incomplete, so the gate is still unusable here.

**To do:**
1. Decide whether the guard should import the root at all. It only needs the modules
   containing its registry entries — importing just those would make it runnable without
   a full-tree build, which is the difference between a gate that runs in CI and one that
   nobody can run locally.
2. Failing that, ensure the build step that precedes it actually builds the root.
3. Either way, make the failure mode legible: "cannot run" must not be reachable without a
   loud message, or the gate silently protects nothing — which is exactly the failure this
   gate exists to prevent in the corpus's *proofs*.

---
**2026-08-15 — DONE. The gate runs, exit 0 on all seven declarations. This bean's
diagnosis was wrong, and the wrong diagnosis is what kept it unrun.**

Branch `claude/fivetwo-level7-ladder-numerators`.

### The diagnosis above is false

> "The guard imports the **`QOU` root**, which transitively needs the whole tree built.
> This container's build state is incomplete, so the gate is still unusable here."

It does not import the root and never did. `run_axiom_check` builds its probe as

```python
modules = sorted({m for m, _, _ in entries})
body = "".join(f"import {m}\n" for m in modules)
```

— the registry's **own five modules**, nothing more. Checked before acting on the
bean's premise rather than after.

### What was actually wrong: one module

Of the five registry oleans, **four were already present**. Exactly one was missing:

```
QOU/BraidsAndKnots/YoungDiagramTailFirstInstance   olean PRESENT
QOU/BraidKnot/SYTEncodingBridgeTwo                 olean PRESENT
QOU/BraidKnot/OVTopAssembly                        olean PRESENT
QOU/BraidKnot/RSKBurnsideDischarge                 olean PRESENT
QOU/BraidsAndKnots/PlancherelNormalisation         olean MISSING   ← the whole blocker
```

`lake build QOU.BraidsAndKnots.PlancherelNormalisation` — exit 0 in **329 s**. The gate
then ran clean:

```
[ok] …YoungDiagramTailFirstInstance.nuV_top_nonneg:            clean   (recorded clean)
[ok] …SYTEncodingBridge.numSYT_eq_numStandardYoungTableaux:    clean   (recorded clean)
[ok] …SYTEncodingBridge.numStandardYoungTableaux_le_numSYT:    clean   (recorded clean)
[ok] …OVTopAssembly.sum_numSYT_sq_eq_factorial:                sorryAx (recorded sorryAx)
[ok] …RSKBurnsideDischarge.rskBurnsideHolds:                   sorryAx (recorded sorryAx)
[ok] …PlancherelNormalisation.sum_sytDim_sq_eq_factorial:      sorryAx (recorded sorryAx)
[ok] …PlancherelNormalisation.nuV_top_closed_form_unconditional: sorryAx (recorded sorryAx)
```

exit 0, no regressions, no promotions. **This is the first time the gate has run.** The
blocker was five minutes of build time, not a whole-tree build — the estimate in this
bean was off by the difference between "one module" and "1,655 modules", and the task
sat untouched on the strength of that estimate.

### Worse than "cannot run": NOTHING INVOKED IT

The bean's item 3 worried the gate "silently protects nothing" *because it could not
run*. Grepping `.github/`, `scripts/` and `.claude/` for `lean-axiom-guard` returns
**one hit, a passing mention in a comment inside `scripts/lean-direct-env.sh`**. No
workflow, no skill, no command, no `/prepare-merge` step ever called it. A gate nobody
invokes protects nothing whether or not it works — which is exactly the failure mode it
was written to catch in the corpus's proofs.

Fixed: **`.github/workflows/lean-axiom-guard.yml`**, following the repo's conventions —
`workflow_dispatch` only (2026-06-30 billing directive), elan + olean cache restore,
neutral-skip on a cold runner like `lean-content-siblings.yml`.

**With one deliberate departure from that pattern.** Once the cache is warm, exit 2
(environment/setup) **fails the job** instead of skipping:

```
::error::axiom guard could not run (exit N) with a WARM cache. This is a real
failure: the gate declined to check anything. Do not merge on the assumption it
passed.
```

Neutral-skipping a warm-cache "cannot run" would rebuild the exact hole this bean is
about. A gate that can decline to run without anyone noticing is not a gate.

### Items, resolved

1. ~~"Decide whether the guard should import the root"~~ — **moot, it never did.**
   Added `--print-modules`, which emits the registry's modules for
   `lake build $(scripts/lean-axiom-guard.py --print-modules)`, so the prerequisite list
   lives in one place. Duplicating it in CI would let the two drift, and the symptom of
   that drift is a gate that cannot run.
2. ~~"Ensure the build step builds the root"~~ — **not wanted.** Building the root is
   the expensive thing this gate does not need; the workflow builds five modules.
3. ~~"Make the failure mode legible"~~ — it already was (loud message, exit 2, verified
   by running it). The *illegible* part was one level up: nothing called it at all.

### Verified, not assumed

- Guard exit 2 before the build, exit 0 after — real exit codes, captured without a pipe
  (`$?` after `| tail` is tail's, which reported a misleading 0 on the first attempt).
- `--print-modules` output fed back through the guard: still exit 0.
- Workflow YAML parses (`yaml.safe_load`), and both scripts it references exist.

### Left for a successor

The registry has **five modules and seven declarations**, all from the 2026-08-07 OV-cone
audit. Nothing added since — including this session's 492 generated gluing theorems, none
of which any gate pins. Worth deciding what else belongs in the registry now that running
it is cheap; that is a scoping question, not this bean.

---
**2026-08-15 (later) — a sibling landed a staleness check on main the same day, and it
would have disabled the gate this bean just enabled.**

Merging `origin/main` (35 commits) conflicted in `scripts/lean-axiom-guard.py`. Main had
added `check_freshness`, motivated by a real failure:

> "the guard reported all-match against 9-day-old oleans while five of the underlying
> sorries had been closed upstream and three declarations had moved files"

**Their concern is correct and I verified it rather than assuming.** A stale olean gives a
verdict about an old snapshot, which is worse than no verdict because it looks like
assurance. That is the same class of defect this bean is about.

### But their mtime heuristic false-fires in the environment the gate runs in

Running the merged guard here: **exit 2, 15 modules flagged stale**, refusing to report.
Checked whether that was real:

- the merge did **not** touch any of those sources (`git log ebc21d1..origin/main` on them
  is empty);
- `Specht.lean` source mtime 10:08 vs olean 03:33, but its last **commit** was the
  previous day — the olean postdates the content;
- decisive: `lake build` on the registry modules **replayed all 3285 jobs as up to date**
  and rebuilt nothing. Lake hashes content; it disagrees with mtime.

So the oleans matched their sources, and the refusal was false. Cause: a clone or checkout
stamps every file with the checkout time, which is later than any olean restored from a
build cache — so raw mtime reports the whole import cone stale on any fresh container or
CI runner.

### The interaction is what makes this urgent

`.github/workflows/lean-axiom-guard.yml`, added earlier on this bean, **fails the job on
exit 2 once the cache is warm** — deliberately, so a warm-cache "cannot run" can't pass
silently. Combined with mtime-based freshness, the gate would have refused on **every
single CI run**. That is the same "protects nothing" outcome this bean exists to fix,
reached from the opposite direction, and neither change is wrong on its own.

### Fix: keep the protection, lose the false positive

`_effective_source_time` compares against the time of the **commit that last touched the
file** — stable across clones — falling back to mtime for files with **uncommitted
changes**, since a local edit is exactly the case the check exists for and there is no
commit to trust.

Verified in **both** directions, not just the one I wanted:

| case | result |
|---|---|
| fresh clone, no local edits | exit 0, all seven declarations match |
| real local edit to `Specht.lean` | exit 2, names `Specht`, refuses to report |

The positive control matters: a "fix" that only removed the refusal would have deleted a
sibling's protection while appearing to work.

### ⚠ Correcting this bean's own earlier entry

The entry above says "**This is the first time the gate has ever run**" and reports exit 0
on all seven. That claim stands — `lake build` replaying 3285 jobs is what establishes the
oleans matched — **but I did not check that at the time**. The verdict was right and the
verification was absent; it was luck, not method. The freshness check is what makes it
method, which is why the sibling's instinct was better than mine even though their
implementation misfires here.

Their bean is untouched.
