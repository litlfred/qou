---
# qou-jtc6
title: 'BUG(q0 triage harness): restore() reverts the harness''s own source — it git-checkouts all of computations/, where it lives'
status: completed
type: task
priority: normal
created_at: 2026-08-23T08:40:18Z
updated_at: 2026-09-05T09:29:08Z
---

## CLOSED 2026-09-05 — fixed in `0d0f1d8d539`, verified live; and the SIBLING survey is the more useful half

The named defect is gone. `computations/audits/q0_muon_witness_staleness_triage.py:145-161`
now restores **only modified NON-`.py` paths**:

```python
out = subprocess.run(["git", "diff", "--name-only", "--", "computations/"], …)
targets = [f for f in out if not f.endswith(".py")]
```

with a docstring naming the cost — a fix written, tested green, and gone from
disk before `git add` ran, leaving commit `c10868ab92` carrying the message but
not the change.

### The blanket form is NOT simply a bug, and that is why it survived elsewhere

Surveying the tree for the same shape found **four other live blanket restores**,
and three of them are **deliberate and documented, each defending against the
OPPOSITE failure**:

| harness | blanket form is | its own stated reason |
|---|---|---|
| `computations/q0_muon_reproduction_sweep.py:167` | deliberate | a producer emits SIBLING witnesses; restoring only the diffed one "leaks a proton-drifted witness over a committed muon witness (the tnjb corruption)" |
| `computations/witness_assertion_replay_audit.py:90` | deliberate | *"Restore the WHOLE computations/ tree — producers write siblings."* |
| `computations/audits/q0_pin_flip_test.py:90` | deliberate, with the bug named | its docstring records that `git checkout -- computations/` reverts `q0_anchor_manifest.json` too, producing "a vacuous pass that would have been reported as seven confirmed verdicts" — and it uses the blanket form anyway, then re-applies the patch |
| `computations/witness_regen_wave.py:162` | already narrowed | its comment names the blanket form as what broke a previous run |
| `computations/audits/witness_dependency_residue_run.py:56` | **undocumented one-liner** | none — plus an unrestricted `git clean -fd` |

So there are two documented failures pulling in opposite directions: **blanket
reverts source** (this bean); **narrow leaks sibling witnesses** (tnjb). The
`qou-jtc6` form resolves both — excluding `.py` keeps every sibling-witness
defence intact, because producers write data artifacts and never source. It is a
safe drop-in at all five sites and is applied at one.

### One fixed here; the three deliberate ones left alone

`witness_dependency_residue_run.py` had the jtc6 shape with **no** justifying
comment, and a sharper variant besides: an unrestricted `git clean -fdq
computations/` that deletes a brand-new *untracked* `.py` an agent has just
written. Fixed to the jtc6 form plus `git clean … -e '*.py'`.

Verified behaviourally rather than by eye — `restore()` extracted and executed
against a perturbed tree:

```
tracked .json restored     : True
uncommitted .py SURVIVED   : True
untracked .py SURVIVED     : True
untracked .json CLEANED    : True
```

The other three are left as they are. Changing a defence its author documented
needs that author's eye, not a passing sweep — and each is correct today for the
reason it gives. Recorded here so the next agent finds the survey instead of
re-running it.

One mitigation worth noting for the one fixed: its own header already says *"RUN
THIS IN A `git worktree`, never in the session tree"* and remaps `ROOT` via
`RESIDUE_WORKTREE`. But `ROOT` defaults to `/home/user/qou` when that variable is
unset, so the defect is live on the default path.
