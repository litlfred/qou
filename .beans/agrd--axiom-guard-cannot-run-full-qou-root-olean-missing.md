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
