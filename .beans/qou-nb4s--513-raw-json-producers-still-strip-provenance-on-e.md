---
# qou-nb4s
title: 513 raw-JSON producers still strip provenance on every run — the two conversion passes were keyed on the wrong set
status: todo
type: task
created_at: 2026-08-23T22:51:05Z
updated_at: 2026-08-23T22:51:05Z
---

**513 producers** in the live tree mention a `*.witness.json`, write something,
and touch neither `WitnessBuilder` nor `stamp_staleness_metadata`. 259 do.

Every one of the 513 **strips provenance on every run**: it writes the witness
with a bare `json.dump` / `write_text`, so `scriptFile` and `scriptHash` are
absent, and a witness missing either cannot be checked against its producer. It
drops out of the self-staleness audit and reads as "not stale" **forever** —
and re-running it makes the staleness count go DOWN because the denominator
shrank, not because anything got fresh. A false drain.

## Why this was not caught by the first two passes

`e84f6249b` converted 29 raw writers; `07459fce7` four more. **Both worklists
were built the wrong way round.**

The 29 came from producers of SELF-STALE witnesses. But a witness carrying a
`scriptFile` and no `scriptHash` is not self-stale — it is UNVERIFIABLE — so
its producer was never in the worklist. The population that needs converting is
keyed on the **unverifiable** set, not the stale set, and those are nearly
disjoint by construction.

`probes/habiro_frobenius_probe.py` is the proof: it went through an unrelated
edit pass, ran clean, and dropped its `scriptFile` doing it — three commits
after the "all 29 raw writers converted" claim.

## Current corpus state (`witness_drain_audit.py`)

    2718  witnesses examined
     412  outside the self-staleness audit
     388    no scriptHash — no recorded value to compare
     279    no scriptFile — producer cannot be located to re-hash
     255    neither
      22  UNRESOLVABLE (declares a scriptFile no file in the tree bears)

**Every drain figure anyone quotes is computed over the remaining ~2300.**

## The recipe (unchanged, proven on 33 producers)

```python
try:
    from witness_base import WitnessBuilder  # noqa: E402
except ImportError:  # cluster subdir without the _path_bridge bootstrap
    import sys as _sys
    from pathlib import Path as _Path
    _sys.path.insert(0, str(next(
        _a / "substrate" for _a in _Path(__file__).resolve().parents
        if (_a / "substrate" / "witness_base.py").is_file())))
    from witness_base import WitnessBuilder  # noqa: E402
WitnessBuilder.stamp_staleness_metadata(
    payload, script_path=__file__, engine=payload.get("engine", "<default>"))
```

immediately before the existing raw write. Notes that cost time the first
time:

- **`stamp_staleness_metadata`, not `wrap_legacy().save()`.** It adds fields in
  place and leaves the on-disk shape untouched, so consumers of legacy
  `assertions` records (which key on `label`, not `name`) do not have to
  change.
- **Pass `engine` back from the payload.** The helper overwrites that field,
  and many of these producers write a descriptive engine string worth keeping.
- **Locate `witness_base` by landmark, not by counting `.parent` levels.**
  `witness_base` lives at `computations/substrate/witness_base.py` and is
  reachable only via `_path_bridge`; many subdirectory producers have no
  bootstrap, and parent-counting is the exact defect `qou-rug0` fixed.
- **Bind the payload to a NAME first if it is inlined into the `json.dumps`
  call** — an in-place stamp needs something to mutate.
- **Some producers have more than one raw write and only one is a witness**
  (`canonical_tower.py` dumps a cache at L238 and the witness at L653). Stamp
  the witness one only.

## Do this as a migration, with the gate already in place

`witness_drain_audit.py` is registered BLOCKING in `staleness-gates.sh` and
fails on any witness that HAD provenance at HEAD and lacks it now — so the
regression direction is already sealed. This bean is the standing BACKLOG, which
is reported and deliberately not gated (a gate red on arrival gets skipped).

Suggested order, cheapest signal first:

1. The ~279 producers behind witnesses with no `scriptFile` — those cannot be
   resolved to a producer at all, so they are the worst off.
2. The rest of the 388 with no `scriptHash`.
3. Re-run `witness_drain_audit.py` after each batch; when NO_PROV reaches 0 the
   backlog line can be promoted from reported to gated.

Do NOT batch-run producers to regenerate witnesses as part of this. Adding the
envelope is a source edit; regenerating is a separate decision with its own
assertion-diff and shape-guard discipline.
