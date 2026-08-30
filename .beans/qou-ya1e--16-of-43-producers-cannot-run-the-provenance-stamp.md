---
# qou-ya1e
title: '16 of 43 producers cannot run: the provenance stamp imports qou_substrate, which is not on sys.path'
status: todo
type: bug
priority: high
created_at: 2026-08-30T15:43:31Z
updated_at: 2026-08-30T15:43:31Z
---

Measured 2026-08-30 by running the `qou-j0nv` regeneration batch — 43 producers,
serial, 600s cap each.

## Result

| outcome | count |
|---|---|
| rc=0 | 21 |
| rc=1 | 20 |
| rc=124 (600s timeout) | 2 |

**16 of the 20 failures are a missing module**, and it is the same one:

```
ModuleNotFoundError: No module named 'qou_substrate'      15
ModuleNotFoundError: No module named 'codata_constants'    1
```

## Cause

`qou_substrate` is **not importable** in this environment on its own — not
pip-installed, no `.pth`, `PYTHONPATH` empty, `find_spec` returns None. It is
reachable only through `_path_bridge`, which producers import to put the
substrate on `sys.path`.

The provenance migration (`migrate_bare_producer_provenance.py`) inserts

```python
from qou_substrate.witness import WitnessBuilder as _WB
```

at the stamp site — **without** ensuring the file imports `_path_bridge`. The
import sits at function scope, so it fires only when the producer goes to write
its witness: the run does all its work, then dies at the save.

Worked example: `a3_magnitude_berezinian_crossterm_probe.py` imports only
`json`, `math`, `datetime`, `pathlib` and then, at line 161,
`from qou_substrate.witness import ...`. No bridge anywhere.

## Scope — measured floor, static ceiling

- **16 confirmed** by execution, in a 43-producer sample (37%).
- **243 producers** import `qou_substrate` with no `_path_bridge` directly and
  none via any module they import. That is a static upper bound, not a
  confirmed count — some may never reach the stamp.

Do not quote 243 as broken. 16 are confirmed; 243 is the population to check.

## Not caused by the restamp

`142b183be` changed only `q0_anchor=False` → `q0_anchor=None`. The
`from qou_substrate` import predates it. These producers were already unrunnable.

## Todo

- [ ] Decide the fix: have the migration script also insert `_path_bridge`, or
      make the stamp import tolerate its absence, or install the substrate.
- [ ] Re-run the 243 to convert the static ceiling into a measured count.
- [ ] Separately: 2 producers hit the 600s cap
      (`he4_binding_k_fingerprint_stage1_probe`, `q0_migration_decompose`) and
      1 fails an assertion (`baldfn_theta_limit_probe`: "reliable window too
      short"). Different defects, not this one.
