---
# qou-qpj5
title: mpf_import_time_dps_audit never scans tools/pyhecke, where _PROTON_G0 is frozen — and test_nucleon_gen_chains_q_param fails on main because of it
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T06:42:55Z
updated_at: 2026-11-16T19:56:39Z
parent: qou-9nnz
---

## Measured

`computations/test_nucleon_gen_chains_q_param.py` FAILS on main, before and
after my qou-t29k changes (verified against a clean stash):

    AssertionError: q=None proton g0 != _PROTON_G0

The test does `set_compute_dps()` and then compares a fresh
`nucleon_gen_chains(['u','u','d'])` against the module constant. The constant
was built at **import-time** precision; the fresh call runs at **70 dps**:

    slot 4   fresh  -0.104530149397819657715423106565
             const  -0.104530149397819657715423106565
             delta   2.212e-62

Every element prints identically — the divergence is entirely below the repr,
which is why nothing surfaced it. At dps 15 (no `set_compute_dps()`) the
assertion passes, so the test is a precision straddle, not a value defect.

## The scope gap

`computations/mpf_import_time_dps_audit.py` is the detector for exactly this
class (288 findings, 185 proven lossy). It walks

    for p in sorted(HERE.rglob("*.py")):     # :320,  HERE = computations/

so **`tools/pyhecke/` is entirely outside its scope** — note `ROOT = HERE.parent`
is defined at :131 and then not used for the walk. That is where
`_PROTON_G0` / `_PROTON_G1` / `_NEUTRON_G0` / `_NEUTRON_G1` are frozen, and
`atom.py`'s own comment puts its reach at **1027 of the 1929 witness-writing
producers** in `computations/`. The most-consumed frozen constants in the
corpus sit in the one directory the frozen-constant audit does not read.

## Not a duplicate

Distinct from the two standing beans on this audit, which are about it being
**unwired** from `precision-gates.sh` and about a *baselined* finding going
red. This is about what it never looks at. Fixing the wiring would not have
found this.

## The decision the fix carries

Same shape as `qou-p4fr`: either the four constants become lazy (rebuilt at
compute dps, PEP 562 `__getattr__` as `derivation_chain` already does), or the
test compares at import dps and the constants are documented as import-pinned.
The first is right if any consumer needs them beyond ~30 digits; that wants
measuring before it is chosen, not assuming.

## Found how

Incidentally, while running this test to confirm my `atom.py` change for
`qou-t29k` had not broken anything. It had not — the failure reproduces on a
clean tree. Worth saying plainly: the only reason this surfaced is that I ran
an adjacent test I did not have to run.

## Progress Update (Round 50 — PR #8178)

- Raised the import-time `workdps` floor in `tools/pyhecke/python/pyhecke/atom.py::nucleon_gen_chains` from `60` to `70` (`COMPUTE_DPS`), so `_PROTON_G0` / `_PROTON_G1` / `_NEUTRON_G0` / `_NEUTRON_G1` match `nucleon_gen_chains` called after `set_compute_dps()` (fixing `computations/test_nucleon_gen_chains_q_param.py` on `main`).
- Added `--include-tools` to `computations/mpf_import_time_dps_audit.py` to scan `tools/pyhecke` alongside `computations/`.
- PR: https://github.com/litlfred/qou/pull/8178 (`6465362ef2e7902778c4f8796f81286e3aeb81bc`)
