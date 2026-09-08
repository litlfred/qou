# The raw-float64 ratchet reports `REGRESSED: 3` on PRISTINE main

Bean `qou-nwhg`. Measured 2026-09-08 on `origin/main` `e05244611`, in a tree with
**zero branch changes**.

## The claim

`computations/witness_raw_float64_audit.py --strict` exits **1** on pristine
`origin/main` with

```
NEW dirty witnesses            : 0
REGRESSED (count increased)    : 3

  REGRESSED — these witnesses gained raw float64:
         5 -> 20      computations/bar-pairing-binding-observable-extension.witness.json
         7 -> 12      computations/binding-rotation-phase-lead.witness.json
         3 -> 4       computations/chi-free-via-lr.witness.json
```

So a feature branch that runs this gate and reads `REGRESSED: 3` has **not**
necessarily walked the ratchet backwards. Main is already there. The counts are
inherited from `main`, not caused by the branch.

## Why this matters right now

A merge was stopped on exactly this reading. The stalled session had rebased onto
main, re-run `computations/binding_rotation_phase_lead.py` (its own producer —
"push the q-Reeb rotation-phase lead", which reads `atom-chi-rust-{d,t,3he,4he}`),
confirmed 296/296 agreement with main to 1e-15 and identical classification counts,
then ran the ratchet, read `REGRESSED: 3`, and stopped with

> REGRESSED: 3 — that's a stop. Merging now would walk a drain-only ratchet backwards.

`binding-rotation-phase-lead.witness.json` is **one of the three that is already
regressed on pristine main**. Its producer is the one that session had just re-run,
and the re-run reproduced main's values. The stop was therefore against a
pre-existing main-side condition.

**Scope, stated honestly.** This audit measured pristine main. It did **not** see
that branch, so it does not prove that session's three are these three — only that
the count matches exactly, that one of the three is the producer it named, and that
the same reading reproduces on a tree with no branch changes at all. The check that
settles it for any branch is the diff below, not the summary line.

## The environment does NOT change this count — a claim I made and retracted

A first draft of this audit asserted that the count is environment-dependent
(**16** without `qou-substrate` installed, **3** with it), on the strength of
counting the file lines in a `tail`-truncated first run whose summary line I never
saw. **That was not a measurement and it was wrong.** Re-measured by shadowing the
package with a module that raises on import (verified to actually block it):

| environment | `REGRESSED (count increased)` | exit |
|---|---|---|
| `qou_substrate` importable | **3** | 1 |
| `qou_substrate` import blocked | **3** | 1 |

Same three files either way. The 16 lines in that first run belong to some other
section of the report, not to the REGRESSED list.

What *is* real, and is worth knowing when reading any run of this audit: when
`qou_substrate.witness._EPHEMERAL_META_FIELDS` cannot be imported, the
runtime-duration carve-out is empty and the audit says so, warning that its counts
are "degraded in the strict direction (dirty UP, drained DOWN)". That warning is
about the per-field totals and the *drained* figures. On this commit it does not
move the REGRESSED count. Install the package anyway
(`pip install -e tools/qou-substrate`) so the totals mean what they say.

## What to run instead of reading the summary line

This is the ratchet-family instance of the rule `f622e5553` recorded for
`precision-gates.sh`: *"a matching list is not evidence the reds are real — only the
pristine-main baseline separates them."*

```sh
pip install -e tools/qou-substrate            # or the carve-out is empty
export PYTHONPATH="$PWD/computations:$PWD/tools/pyhecke/python:$PYTHONPATH"

# 1. baseline: pristine main, in a throwaway worktree
git worktree add /tmp/pristine origin/main
( cd /tmp/pristine && python3 computations/witness_raw_float64_audit.py --strict ) \
  2>&1 | sed -n '/REGRESSED —/,/^$/p' > /tmp/ratchet-main.txt

# 2. the branch
python3 computations/witness_raw_float64_audit.py --strict \
  2>&1 | sed -n '/REGRESSED —/,/^$/p' > /tmp/ratchet-branch.txt

# 3. the only informative artifact
diff /tmp/ratchet-main.txt /tmp/ratchet-branch.txt
```

An empty diff means the branch contributes nothing to the ratchet and the `exit 1`
is main's, not yours. A non-empty diff names the files that are actually yours.

**The producer writes its witness.** `witness_raw_float64_audit.py` rewrites
`computations/witness-raw-float64-audit.witness.json` on every run, so restore the
tree (`git checkout -- computations/witness-raw-float64-audit.witness.json`) before
committing, or a measurement lands as a diff.

## What this does NOT say

It is **not** licence to skip the ratchet, and **not** a reason to touch
`raw-float64-baseline.json`. Baselines drain, never grow (AGENTS.md §QA is
agent-owned). Three witnesses on main genuinely carry more raw float64 than the
baseline records; draining them is real work and stays open. The finding is only
that the *summary line* is uninformative on a feature branch while main is red, and
that the per-file diff against a main baseline still is.
