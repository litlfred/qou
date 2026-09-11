---
# qou-xumu
title: 'GAP: lean-library-sweep.py ABORTS on one slow module — 101 modules never attempted'
status: completed
type: task
priority: normal
created_at: 2026-09-07T11:26:54Z
updated_at: 2026-09-11T15:23:29Z
---

## 2026-09-11 — CLOSED. The abort path is gone by construction, and the fix cites this bean by name.

Off the `qou-bstl` queue. This bean has **no body** — title only — so the code is
the only thing that can settle it.

**The abort is fixed at the worker**, `scripts/lean-library-sweep.py:510-521`:

```python
except subprocess.TimeoutExpired:
    # A TIMEOUT IS NOT A RED.  It says the module was not verified, not
    # that it fails ... It is also not a reason to abandon the sweep: this
    # exception used to propagate out of ThreadPoolExecutor.map and kill the
    # whole run, so ONE slow module suppressed the verdict on every module
    # after it (measured 2026-09-07: QOU.Machinery.HeckeH4Semisimple
    # exceeded 1800s at module 527 of 628, and the remaining 101 were never
    # attempted AND no summary was printed -- bean qou-xumu).
    tmp.unlink(missing_ok=True)
    return m, None, f"TIMEOUT after {args.timeout}s"
```

It names this bean, the module, `527 of 628`, and **101** — matching this
title exactly. The exception is now caught inside the worker and converted to a
verdict, so it cannot reach `ThreadPoolExecutor.map`. The header states the
invariant independently at `:33-35` (*"**Continues past a failure**, marking that
module's dependents `skipped` rather than aborting — one break must not mask the
rest, which is the whole point of a sweep"*), and the summary at `:600` counts
`TIMEOUT + UNVERIFIED (NOT failing)` as their own bucket rather than as reds.

**Established BY THE CODE, which is the strongest form available here** — the
same distinction `qou-geqa` had to learn about `hadron_knot_table`: a catch that
converts the exception to a return value makes the abort impossible, whereas a
successful run would only be corroboration. I have **not** run a full 628-module
sweep, so this closes "it aborts" and does **not** claim "the sweep completes";
other failure modes are not excluded.

### 🛑 An exit-1 I hit that is NOT a defect — my branch's staleness

`python3 scripts/lean-library-sweep.py --help` exits **1** here with

    ValueError: unsupported format character ' ' (0x20) at index 314

from a literal `%` in an argparse help string. **That is fixed on `main`** by
`76ecd01eebb` (*"lean-library-sweep --help crashed on a literal % in an argparse
help string"*), which is not an ancestor of this branch — I am 28 commits behind.
A different defect from this bean's, already closed, and I nearly recorded it as
a live one.

Second time this session that my distance from `main` produced a
finding-shaped artifact (the first: a `Q0_PARSE_ERROR` on a witness that is 0
bytes here and 6018 on main). **Re-measure against the tree you are merging
onto** — `qou-tekx` states the same lesson from the other direction.

**qou-xumu closes.**
