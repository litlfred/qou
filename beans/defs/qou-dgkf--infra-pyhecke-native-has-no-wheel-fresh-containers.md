---
# qou-dgkf
title: 'INFRA: pyhecke_native has no wheel — fresh containers cannot run any deltalambda probe without a 3.5-min maturin build'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T00:45:42Z
updated_at: 2026-10-04T15:20:52Z
parent: qou-5vkl
---


## What happened

Hit while running the μ₃ per-block Fréchet probe (PR #4657). A fresh session
container could not run **any** `computations/deltalambda/*` probe because the
Hecke character engine is unavailable:

```
ModuleNotFoundError: No module named 'pyhecke_native'
```

`pyhecke_native` (`chi_q_atomic_all_partitions`, `chi_lambda_braid`, …) ships as
**Rust source only** — `tools/pyhecke-native/` — with no prebuilt wheel on PyPI, no
wheel committed to the repo, and no pure-Python fallback. Recovery required:

1. `pip install maturin` (1.14.1)
2. `python3 -m maturin build --release` → **3 min 21 s** compiling `hecke-engine`
3. `pip install target/wheels/pyhecke_native-0.9.0-cp311-cp311-manylinux_2_35_x86_64.whl`

Plus `numpy` / `scipy` / `sympy` / `mpmath`, also absent, which cost a second
failed launch (`mass_at_3A_proper` imports numpy at module scope).

Prior probe witnesses record `pyhecke_native 0.9.0`, so this ran fine in whatever
environment those were produced in — the gap is environment provisioning, not the
package.

## Why it matters

Every idle-time drain that touches `computations/deltalambda/`, `computations/`
mass-table work, or witness regeneration pays this ~4-minute tax **per fresh
container**, and pays it as a confusing `ModuleNotFoundError` rather than a
documented setup step. It also silently pushes agents toward "the probe can't run"
instead of "the probe needs a build".

## Candidate fixes (not yet chosen — owner call)

1. **Publish `pyhecke-native` wheels to PyPI** (manylinux + macOS, cp311+). Cleanest;
   matches how `pyhecke` / `qou-substrate` / `witness-schema` are already packaged.
   `AGENTS.md` already lists it as a "PyPI wheel", which is currently aspirational.
2. **Add a `scripts/setup-compute.sh`** alongside `setup-folio-assistant.sh` that
   installs the Python deps and builds/install the wheel, and reference it from
   `AGENTS.md` §compute so agents run it once instead of rediscovering the failure.
3. **Bake it into the container image** (same argument as the `lake-cache/*` orphan
   branches for Lean oleans — a prebuilt artifact beats a 3.5-min rebuild).
4. **Cheapest stopgap:** a `-- Ref:`-style note in
   `computations/deltalambda/README` (or the probe docstrings) giving the three
   commands, so the recovery path is greppable.

Option 4 is ~10 minutes and unblocks the next agent; options 1–3 are the real fix.

## Not a Mathlib gap

Filed under "infra" per the request to bean up infra/Mathlib gaps. No Mathlib
shortfall was hit in this arc — every Lean obligation for `Mu3SlotExclusion` closed
with existing Mathlib (`Finset.exists_lt_of_sum_lt`, `Finset.sum_nonneg`,
`nlinarith`). This is purely a Python/Rust environment-provisioning gap.
