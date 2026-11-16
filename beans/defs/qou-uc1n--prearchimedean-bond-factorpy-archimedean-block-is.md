---
# qou-uc1n
title: prearchimedean_bond_factor.py archimedean block is float64 end-to-end
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T07:55:29Z
updated_at: 2026-11-16T19:56:39Z
parent: qou-9nnz
---

Found while migrating this file from convention C to convention D (owner directive 2026-08-29, PR #5972).

The migration itself is done: `z` is now `q**3/(q**2+1)` and the emitted
symbolic forms are rational (`f_nn = 1/(q**3+q)`), so the half-integer powers
of q the file used to carry are gone with the square root rather than
relabelled.

What is NOT done, and is out of scope for a convention migration because it
changes no convention: the archimedean block (`main()`, roughly lines 100-125)
is float64 end to end. `q0 = float(Q0)`, `me = float(M_E_MEV)`, every
`arch[...]` and `e_bond[...]` entry is `float(...)` of a sympy subs, and the
witness carries 10 raw float64 fields. The file is already in
`computations/raw-float64-baseline.json`, so this is recorded, not new.

Sharp edge for whoever drains it: a HALF migration is worse than none. The
first attempt at the assertion comparand here wrote `mp.mpf(str(Q0))`, and
`precision-gates.sh` failed it on two counts at once -- `q_parameter.Q` is
itself a float64, so `mpf(str(<f64>))` is exactly the laundering pattern the
f64-into-mpmath tier catches, and the mpf was built at the default dps=15,
tripping the never-raises-dps ratchet as a NEW producer. A lone mpf comparand
among float64 neighbours buys no precision, only a false claim of it. The fix
is at the IMPORT: read q0 as mpf (`q_at(dps)`), call `set_compute_dps()` at
module scope, and carry mpf through the whole block and into `_precision.fmt`
on serialization -- all of it or none of it. Expect the published per-bond
energies to move in the last digits when it lands.

## Progress Update (Round 50 — PR #8178)

- Lifted the archimedean evaluation block in `computations/prearchimedean_bond_factor.py` from `float64` to `mpmath.mpf` at `compute_dps=70` (`set_compute_dps()`, `Q_50_DIGIT_STR`), serialized via `_precision.fmt`, added `--self-test`, and regenerated `computations/prearchimedean-bond-factor.witness.json` (`10 -> 0` raw float64 fields).
- PR: https://github.com/litlfred/qou/pull/8178 (`6465362ef2e7902778c4f8796f81286e3aeb81bc`)
