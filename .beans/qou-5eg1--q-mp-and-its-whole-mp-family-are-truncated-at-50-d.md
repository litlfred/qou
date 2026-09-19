---
# qou-5eg1
title: Q_MP and its whole *_MP family are truncated at 50 dps while OUTPUT_DPS is 60 — 10 fabricated digits, and no detector can see them
status: todo
type: bug
created_at: 2026-09-19T06:36:23Z
updated_at: 2026-09-19T06:36:23Z
---


## Surfaced by the `qou-oiz3` stage-1 cone audit; verified independently here

`tools/qou-substrate/python/qou_substrate/constants.py:331`

```python
Q_MP         = q_at(_DPS_DEFAULT)      # _DPS_DEFAULT = 50   (:247)
Q_INV_MP     = _mp.mpf(1) / Q_MP       # :333
HBAR_Q_MP    = _mp.mpf(1) - Q_INV_MP   # :336
HBAR_Q_SQ_MP = HBAR_Q_MP ** 2          # :337
```

against `qou_substrate.precision`: **`COMPUTE_DPS = 70`, `OUTPUT_DPS = 60`.**

Measured at `mp.dps = 120`:

```
Q_MP     = 1.10997858275138080759166909561076887987449912187357763605672
q_at(90) = 1.10997858275138080759166909561076887987449912187357873607281
|diff|   = 1.1000161e-51
```

They agree to **50 significant digits and diverge at the 51st**. Everything
`_MP` inherits that ceiling, because every one of them is derived from `Q_MP`:
`Q_INV_MP`, `HBAR_Q_MP`, `HBAR_Q_SQ_MP`, `TWO_Q_MP`, `TANH_LN_Q_MP`, `LN_Q_MP` —
all re-exported from `qou_substrate/__init__.py:71-81`, i.e. the public surface.

## The consequence, stated precisely

A producer that raises compute precision (`set_compute_dps()` / `COMPUTE_DPS = 70`)
and then serializes an `_MP`-derived value with `_precision.fmt` at `OUTPUT_DPS = 60`
publishes **digits 51 through 60 that carry no information**. They are not the
input value's digits; they are what 50-dps truncation error propagated into.

## Why NO detector in the tree can see it — and this is the point

Three separate instruments, all structurally blind:

1. **The float64-padding ratchet** looks for a short value padded with trailing
   **zeros**. These digits are not zeros — they are arbitrary. PR #7438
   independently found the padding audit blind to "16 real digits + 44 zeros"
   (its `tr_M_q0` case); this is the *same false-precision class with the
   trailing-zero signature removed*, so it is strictly harder to detect.
2. **`witness.scriptHash`** never drifts: a producer consuming `Q_MP` has
   byte-stable source. This is `cosmetic_import_cone_drift`, the one
   `witness_staleness_triage.py` bucket that has grown across five measurements.
3. **The raw-float64 ratchet** sees nothing: `Q_MP` is a genuine `mpf`. The
   arithmetic is exact — it is exact arithmetic on a *truncated input*.

## Blast radius — direct references, and say which count this is

Measured on this branch, `grep -rlnE "\b(Q_MP|Q_INV_MP|HBAR_Q_MP|HBAR_Q_SQ_MP|TWO_Q_MP|TANH_LN_Q_MP|LN_Q_MP)\b" --include=*.py`,
excluding `.claude/worktrees/`, the generated `qou-mass/src/qou_mass/_internal/`
mirror, and the two defining modules:

| population | count |
|---|---|
| **live files directly referencing an `*_MP` constant** | **356** (352 in `computations/`, 2 `docs/`, 1 `tools/`, 1 `scripts/`) |
| `computations/_deprecated/` | 107 |

**This is a DIRECT-REFERENCE count, not an import cone.** The cone is larger —
`qou-oiz3`'s audit measures the shim cone (importers of the constant modules) at
**3921 files**, and notes that figure is *not* a measure of the `q_int` defect.
For *this* defect it is closer to the right population, because `Q_MP` is a
module-level constant rather than a function, but it is still an upper bound.
Do not quote 3921 as this bean's blast radius without re-deriving it.

## Relation to `qou-oiz3` — separate defect, wider surface

`qou-oiz3` is the float64 `q_int` (`constants.py:190`), cone 1290 files / 917
witnesses. This is a different mechanism (exact arithmetic on a truncated input,
not float64 arithmetic) with a different and wider surface. The `qou-oiz3` stage-1
audit names it and explicitly puts it **out of scope**:

> Its consumer base is the shim cone, far wider than `q_int`'s. Not fixed by
> this arc and not in its plan.

Recorded here so it does not stay a paragraph inside another bean's audit doc.

## What is open

1. **Is 50 dps deliberate?** `_DPS_DEFAULT = 50` predates the 70/60 move
   (AGENTS.md's L1 row read "65 dps compute / 50 dps serialization" until
   2026-09-06 and had been stale since at least 2026-08-30, bean `qou-0z4i`).
   So the likeliest reading is that `_DPS_DEFAULT` is a **survivor of the old
   serialization floor** that was never raised with it — but that is a
   hypothesis, not a measurement. `git log -L` on `:247` would settle it.
2. **How many committed witnesses actually carry fabricated digits 51-60?**
   Unmeasured. A witness scan for `_MP`-derived fields at >50 significant
   digits would give the real number; nothing in the tree does this today.
3. **Whether the fix is `_DPS_DEFAULT = 70`, or making the `_MP` family
   lazy/parametric.** Raising the constant is one line and is exemption 1
   (it removes a truncation, makes numbers strictly more correct); the
   *witness refresh* it implies is not, and is the same trap `qou-oiz3`
   stage 2 is held on.

## NOT proposed here

No code change. Under the 2026-09-07 ASK-THE-OWNER directive the one-line
constant bump qualifies as exemption 1 in isolation, but landing it without
knowing population (2) reproduces exactly the failure `qou-oiz3` stage 1 declined:
converting known-wrong digits into wrong digits nothing can find. Measure (2)
first, or decide with the owner. Stays `todo`.
