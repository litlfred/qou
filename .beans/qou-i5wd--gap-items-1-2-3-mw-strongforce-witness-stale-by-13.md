---
# qou-i5wd
title: 'GAP: items-1-2-3-mw-strongforce witness stale by +1.350 ppb after the m_e drain (PR #4975)'
status: completed
type: task
priority: normal
created_at: 2026-08-11T10:47:29Z
updated_at: 2026-08-18T21:09:59Z
---

## What is open

`computations/items_1_2_3_mw_strongforce_anchor_asymmetry.py` was swapped from
the truncated literal `M_E_MEV = mpf("0.510998950")` to the registry import
`from codata_constants import M_E_MEV` (PR #4975, commit `91fea71f5`, one of
the 9 m_e sites). The registry value is `0.51099895069`, so the swap moves any
m_e-scaled output by **+1.350 ppb** (`0.51099895069 / 0.510998950 =
1.000000001350`).

`M_E_MEV` reaches the committed witness at line 145:

```python
"T29_naive_mass_MeV": float(M_E_MEV * abs(tr_T29)),
```

`computations/items-1-2-3-mw-strongforce-anchor-asymmetry.witness.json`
currently records

```
item_2_strong_force_torus.T29_naive_mass_MeV = 0.6318874949446431
```

which is the **pre-swap** value. It should shift by +1.350 ppb. The witness is
therefore genuinely stale on the branch — this is a real gap, not drift.

## Why it was not closed in PR #4975

The producer cannot run in the prepare-merge sandbox:

```
File "computations/markov/markov_trace_for_knot.py", line 83, in <module>
    import pyhecke_native as pn
ModuleNotFoundError: No module named 'pyhecke_native'
```

`tr_T29` comes from the Rust Markov-trace kernel (`pyhecke-native`), which is
not installed. This is an **environment** limitation, distinct from the two
producers on the same PR that are broken on pristine `main`
(`pentagon_rt_torus_knot_higgs_probe.py` — `TypeError: Object of type mpf is
not JSON serializable`; `per_knot_density_borromean_q_locality_probe.py` —
`ImportError: cannot import name 'per_knot_density_borromean'`). Those two fail
identically on `main` and are not this branch's doing; this one would run fine
in an environment that has the kernel.

## Next honest step

In an environment with `pyhecke-native` installed (`maturin build` in
`tools/pyhecke-native/`, per the kernel's own error message):

1. `python3 -u computations/items_1_2_3_mw_strongforce_anchor_asymmetry.py 2>&1 | tee /tmp/items123.log`
2. Confirm `T29_naive_mass_MeV` moved by ≈ +1.350 ppb from `0.6318874949446431`
   and that nothing else in the witness moved beyond provenance.
3. Commit the regenerated witness naming the ppb shift.

Note the field is serialized through `float(...)`, so it is a raw float64 in
the witness — pre-existing, and a separate concern from this staleness.
