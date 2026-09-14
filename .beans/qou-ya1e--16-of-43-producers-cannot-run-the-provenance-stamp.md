---
# qou-ya1e
title: '16 of 43 producers cannot run: the provenance stamp imports qou_substrate, which is not on sys.path'
status: todo
type: bug
priority: high
created_at: 2026-08-30T15:43:31Z
updated_at: 2026-09-14T15:00:40Z
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


---

## Not reproducible in this container — and the prescribed fix is INERT (2026-09-14)

Attempted the fix, could not verify it, reverted it. Three findings, in the
order they overturned each other.

### 1. This container has the substrate INSTALLED, so the defect is invisible here

    _editable_impl_qou_substrate.pth  ->  /home/user/qou/tools/qou-substrate/python
    importlib.util.find_spec("qou_substrate")  ->  .../qou_substrate/__init__.py
    PYTHONPATH: unset

The bean's cause section says "not pip-installed, no `.pth`, `PYTHONPATH`
empty, `find_spec` returns None". **All four are false here.** Someone ran
`pip install -e tools/qou-substrate` in this image. Every one of the candidate
producers imports the stamp fine, bootstrap or no bootstrap.

So a fix cannot be validated in this container: it passes before and after.
**Check `find_spec("qou_substrate")` before believing either state** — the
measurement and its absence are both environment artifacts.

### 2. The corrected injector's bootstrap does not work

`migrate_bare_producer_provenance.apply_one` was corrected on 2026-08-30 (this
bean) to emit an upward search. What it emits is:

    for _anc in _pl.Path(__file__).resolve().parents:
        if (_anc / '_path_bridge.py').exists():
            _sys.path.insert(0, str(_anc)); break
    from qou_substrate.witness import WitnessBuilder as _WB

That puts **`computations/`** on `sys.path` and then imports `qou_substrate` —
but `qou_substrate` is not under `computations/` (checked: no
`computations/qou_substrate`). It lives in `tools/qou-substrate/python`, and
the thing that adds that directory is **`_path_bridge.py:61`**:

    _add_to_path(_HERE.parent / "tools" / "qou-substrate" / "python")

The emitted block never imports `_path_bridge`. It locates the bridge and then
does not use it. **On a genuinely bare container this block still raises
`ModuleNotFoundError`** — the correction is inert, and it cannot be caught by
running it here for reason 1.

The missing line is `import _path_bridge` immediately after the insert.

**0 files in the tree carry the emitted bootstrap**, so the corrected injector
has not been run since; nothing in the corpus depends on the broken form yet.

### 3. My own attempt copied the same idiom, and my first rig lied

Patched all 389 candidates with that block, then reverted — it is inert for
the reason above and unverifiable here for reason 1.

Worth recording because it nearly became a fabricated confirmation: my first
runtime rig did `sys.path[:] = [script_dir]`, which wipes the **stdlib** too.
It reported "12 of 12 candidates fail", which looked like a clean
reproduction of this bean. It was an artifact — the imports were failing for
want of `__future__`, not `qou_substrate`. A faithful rig sets `sys.path[0]`
and keeps the rest, and then all 12 PASS.

### Current numbers, on the static criterion only

    import qou_substrate, no _path_bridge reachable (transitively)  389
    ...of which carry the injector's bootstrap                        0
    bean's 2026-08-30 figure                                        243

Do not read 389 vs 243 as growth: I could not reproduce the bean's transitive
method exactly, and 389 includes `audits/` and `tools/` entries that may never
reach a stamp. It is a ceiling on a looser criterion, not a re-measurement.

### What the fix actually needs

1. Add `import _path_bridge` to the injector's emitted block, or
2. decide that the substrate is INSTALLED (as here) and say so, in which case
   this bean's class dissolves and the bootstrap is unnecessary — but then the
   default-bare-container assumption in `AGENTS.md` needs updating to match.

Either way it must be validated on a container **without** the `.pth`. Set back
to `todo`: not progressed, since neither branch is verifiable from here.
