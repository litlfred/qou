---
# qou-bfdb
title: pyhecke.gram.q0 is a float64 module constant reached by ~1027 witness-writing producers
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-03T12:47:15Z
updated_at: 2026-11-17T11:39:37Z
parent: qou-9nnz
---

## Measured

```python
>>> from pyhecke import atom
>>> type(atom.q0).__name__, atom.q0
('float', 1.1099785827513808)
>>> type(atom.D_PN).__name__
'float'
```

`D_PN = pn_interface_offset(q0)` in `tools/pyhecke/python/pyhecke/atom.py:75`
therefore carries **2.0087e-16** relative error against the same identity
evaluated at 50 dps (`pn_interface_offset(q_at(50))`).

The blast radius is in that file's own comment, two lines above the binding:

> this module is the single largest consumer of the choice: **1027 of the
> 1929 witness-writing producers** in `computations/` reach it through this
> file.

## Why this is filed, not fixed

Found while draining `qou-b7cf` (PR #6489), where two probes launder
`D_PN` at 40 dps. Those two sites are fixed there by recomputing
`pn_interface_offset(q_at(mp.mp.dps))` locally - correct for those probes,
but it does not touch the module constant every other consumer reads.

Fixing at the producer means giving `pyhecke.gram` an mpf `q0` (or an
`_mp` twin, the pattern the module already uses for `h_mp` / `hm_mp` /
`build_nucleon_nf_mp`) and migrating consumers. That is a sweep across
~1027 producers with witness regeneration, and it needs scoping and
sign-off, not an idle-pass drain.

## Caution for whoever takes it

The additive-twin pattern is exactly how `build_nucleon_nf_mp` went stale:
a twin with **zero consumers** drifted four days behind its float sibling
while its docstring still claimed 1.4e-16 agreement, and the real
divergence was 2288 % (fixed in PR #6489). If this is done as a twin,
the twin needs a test that fails when the two disagree - not a docstring
recording a measurement that nothing re-runs.
