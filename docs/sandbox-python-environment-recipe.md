# Restoring the recorded Python environment in a bare container

**Bean `qou-f8lit`, recorded 2026-08-30.**

A fresh remote container here starts **without** `numpy`, `scipy`, `sympy` or
`clarabel`, and with `mpmath` at a version the corpus does not use. Every
`computations/` producer records the environment it ran under, so re-running one in
that state writes numbers whose provenance disagrees with the corpus.

**The recorded environment is reachable with pip.** I spent a session asserting
otherwise — observing the packages absent and concluding they were unavailable, without
testing whether they could be installed. They can, in about a minute.

## The recipe

```sh
pip install numpy scipy sympy clarabel
pip install "mpmath==1.4.1"          # MUST come last -- see below
```

Verify against any committed witness's `environment` block:

```sh
python3 -c "
import json, importlib, platform
e = json.load(open('computations/audits/q0-anchor-consistency-audit.witness.json'))['environment']
got = {'python': platform.python_version()}
for m in ('numpy','scipy','sympy','mpmath','clarabel'):
    try: got[m] = getattr(importlib.import_module(m), '__version__', '?')
    except Exception: got[m] = 'MISSING'
for k in ('python','numpy','scipy','sympy','mpmath','clarabel'):
    print(('OK      ' if got.get(k)==e.get(k) else 'MISMATCH'), k, got.get(k), 'vs', e.get(k))
"
```

Expected on this corpus: `python 3.11.15`, `numpy 2.4.6`, `scipy 1.17.1`,
`sympy 1.14.0`, `mpmath 1.4.1`, `clarabel 0.11.1`.

## ⚠ `pip install sympy` DOWNGRADES mpmath, and that is the trap

`sympy 1.14.0` declares `mpmath<1.4`, so installing it pulls `mpmath` down to `1.3.0` —
**below the `1.4.1` every witness records.** `mpmath` is *the* precision library here, so
a producer run after that step carries a silently wrong arithmetic backend while every
other version matches. The failure is invisible: the run succeeds, the numbers differ.

Reinstall `mpmath==1.4.1` last. pip will print

    sympy 1.14.0 requires mpmath<1.4,>=1.1.0, but you have mpmath 1.4.1 which is incompatible

and that warning is **safe to ignore here** — verified: `sympy 1.14.0` imports and runs
with `mpmath 1.4.1`. The constraint is over-strict, and the corpus's own recorded
environment is the pairing to match.

## What this does NOT fix

The audit witnesses still regenerate with **moved counts** after a full-environment
run — `Q0_OK 1087→1108`, `witness-provenance computed 94→76`,
`q0-value-drift proton-pin 1906→1970`. So the environment was **not** the whole story,
and the earlier diagnosis blaming it was at best partial. Those movements are most
plausibly genuine re-measurement against a `main` that has moved (117 commits in one
stretch of this session), not an artifact — but that is **not established here**, and
draining them belongs to whoever owns those witnesses.

Do not commit regenerated audit witnesses on a branch that does not otherwise touch
them; check whether a **count** moved (substantive) or only `computedAt`/`commitSha`
(drift — revert it).

## The environment was necessary, not sufficient — measured on a real producer

Having fixed the environment, I claimed the ~30 flagged `computations/` producers were
"now unblocked". **Tested on one before leaving that claim standing**, and it needs
qualifying.

`computations/mmu_r9_consistency_check.py` — one of the six carrying the wrong
`VOL_4_1` variant `2.0298832128193072500115970029` — **runs clean** in the restored
environment: exit 0, witness written, assertions evaluated. So the environment really
was the barrier to *running* them.

**But it emits a raw-float64 warning on the way:**

```
⚠ raw-float64: mmu-r9-consistency-check.witness.json: 7 raw float64 field(s) would
  enter the witness — .data.sigma_exp_ppb, .data.target_100x_ppb, .data.bare_err_ppb,
  .data.bare_miss_factor, .data.r9_err_ppb, .data.r9_miss_factor,
  .data.improvement_factor
```

So re-running it **as-is** would introduce float64 dirt that the ratchet forbids, and
the fix has to happen **at the producer** — carry `mpmath.mpf` from source, serialize
with `_precision.fmt` — before any re-run is committable.

All six of the bad-variant producers are in the same state:

| producer | `float(` calls |
|---|---|
| `mmu_r9_two_rung_extension_probe.py` | 7 |
| `mmu_r9_two_rung_v2_probe.py` | 6 |
| `mmu_simpler_form_search_probe.py` | 6 |
| `mmu_r9_consistency_check.py` | 6 |
| `mmu_categorical_correction_first_probe.py` | 4 |
| `mmu_categorical_correction_refined_probe.py` | 3 |

**So the correct scoping is: fix the float64 at each producer, then correct the constant,
then re-run.** Not "re-run them". That is a substantially larger piece of work than
installing four packages, and anyone reading "unblocked" as "cheap" would have found
this out the expensive way — by committing a witness that fails the ratchet.

The two facts are independent and both true: the environment barrier is gone, and a
different barrier is in front of the same sweep.
