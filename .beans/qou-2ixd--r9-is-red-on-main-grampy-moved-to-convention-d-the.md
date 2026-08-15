---
# qou-2ixd
title: 'R9 is RED on main: gram.py moved to convention D, the registry still says C'
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T12:46:10Z
updated_at: 2026-08-15T12:51:32Z
---


## What was red

`docs/coordination/trace_convention_registry_validate.py` on `origin/main`:

    ERROR : R9 pyhecke.gram.z: registry says convention C
            (z = 0.49932033418369445241...) but the CODE returns
            0.6126880371464652 (|d| = 0.1134 > 1.0e-15)
            -- it is actually convention D
    FAIL  (1 error(s), 22 warning(s))

`gram.py:175` reads `z = q0 ** 3 / (q0 ** 2 + 1)` and inverts `G` on the
quotient `H_3/rad`. That is the migration from bean `qou-w8zz` (in-progress,
sibling) — owner-approved and correct. The `blocked_migrations` row asserting
`stays: C` simply did not move with it.

**The gate worked.** The registry's own note said, in advance: *"If this ever
reports D without blocked_migrations being cleared, something switched it."*
It reported exactly that. R4/R5 compare a docstring to a registry field and
stay green whenever both sides go stale together; R9 evaluates the code.

## Fixed

1. `blocked_migrations: []`; the row moved to a new `resolved_migrations` with
   the resolution recorded. Moved rather than deleted — its `reason` is the
   clearest statement in the repo of why the full Wedderburn Gram cannot be
   inverted under D, and that is still true.
2. `evaluators/z[4]` `pyhecke.gram.z`: `convention` C → D.
3. The `.md` twin (`qou-ungx`: the twin drifts silently) and the
   `historical_c_sites` cross-reference, both of which still said "three
   places" and "BLOCKED".
4. R9 re-run: **PASS (0 errors, 22 warnings)** — the 22 are the pre-existing
   R5 "Borromean trace without a declared convention" warnings, unchanged.

## Two findings this exposed

### The detector trusted the record

`scripts/convention-c-producer-audit.py::scan_reexports` reads
`blocked_migrations` to decide what counts as a leak, so with a stale row it
reported **25 production sites "receiving convention C"** that were receiving
D. A detector that trusts a record inherits its staleness — the exact failure
the excision has been unpicking, arriving inside the tool built to find it.

Now verifies the premise: `_defines_convention_d(src, sym)` checks the named
file actually still defines the symbol as C before deriving anything from the
row, and prints `REGISTRY STALE` if not.

### `gram.py` has a live INTERNAL C/D split

Classification was `path.startswith("tools/pyhecke/") -> blocked by design`.
One registry row covered `gram.py::z`; three function-local C definitions
sheltered under the same blanket:

| site | |
|---|---|
| `tools/pyhecke/python/pyhecke/gram.py:650` | `z_ = 1 / (_mp.sqrt(q) + _mp.sqrt(qi_))` |
| `tools/pyhecke/python/pyhecke/gram.py:746` | same |
| `tools/pyhecke/python/pyhecke/atom.py:691` | `z_mark = 1.0 / (q0 ** 0.5 + qi ** 0.5)` |

The `gram.py` docstring above line 650 says:

> **Convention C**, in lockstep with the module's `z` — see the blocking note
> at that definition.

The module's `z` is now **D**. They are no longer in lockstep, and the
docstring asserts they are. So the 50-dps mpmath trace path — the one you
reach for when precision matters — disagrees with the module's own declared
convention by 22%. R9 does not see it: it evaluates the module attribute
`pyhecke.gram.z`, not `_tr_m_mp`.

Classification is now registry-derived, so these three report as **"C with NO
registry row (unexplained)"** and count as actionable: `0 -> 3`.

## Next

- **Not fixing the three sites here.** `gram.py` is `qou-w8zz`'s active scope
  (sibling, in-progress, branch `claude/gram-convention-d-quotient-2026-08-15`,
  14 commits ahead of main and NOT carrying this registry fix). Changing the
  mpmath trace path underneath an in-flight migration is how the original
  block's "silently corrupts every consumer" warning comes true.
- Worth an R9-style evaluator for FUNCTION-level returns, not just module
  attributes — that is the hole these three sat in.
