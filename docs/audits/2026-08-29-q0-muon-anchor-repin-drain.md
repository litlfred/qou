# The two RED q₀ gates are one unfinished migration, not two defects

**Date:** 2026-08-29 · **Bean:** `qou-3f7a` · **Status:** scoped, drain not yet run

## What is red

`scripts/precision-gates.sh` on a clean `main` (`0222d637e8`):

```
RED: q0-anchor flip   q0-value drift ratchet
```

- **`q0-anchor flip`** — 83 `Q0_FLIP`: witnesses stamped `q0Anchor: "muon"`
  carrying `q0Value = 1.10997859555733…` where the anchor now defines
  `1.109978595642…`.
- **`q0-value drift ratchet`** — 383 stale / baseline 329 / **165 NEW**, and
  every drifting site reports the **same** delta: `−0.0769 ppb`.

## They are the same defect

`−0.0769 ppb` is exactly the gap between the two muon values:

| | value | |
|---|---|---|
| **A** | `1.1099785955573347…` | the old frozen pin |
| **C** | `1.1099785956427390…` | CODATA-2022, derived live |

`(A − C)/C = −7.69e-11 = −0.0769 ppb`. The anchor-flip gate reads the
`q0Anchor`/`q0Value` pair; the drift gate reads value sites anywhere in the
tree. Both are seeing one population of stale witnesses from two angles.

## Why the anchor moved — it was deliberate, and it was right

Commit `fca08de7d2` (2026-08-22), on an owner ruling:

> *"2022 CODATA better than 2018. A → CODATA 2022."*

The old pin **A** was self-certifying. `q_pinning_50_digit.py` is listed
`ideal_muon`, so `q_parameter` rebound `q_at` for that very producer and it
wrote back the value it had just read. **A** inverts to
`m_μ/m_e = 206.768282989315`, matching no published CODATA and disagreeing by
1.4 ppb with the ratio the same witness declares in its own
`calibration_inputs`. The witness contradicted its own stated input.

The fix derives rather than re-freezes: `q_parameter`'s muon branch now takes
`q_muon_at()`, the live closed form over `constants.MASS_RATIO_MU_E_STR`, so
the anchor follows the next CODATA revision with no digit edited by hand.

## What remains, and it is stated in that commit

> *"WHAT REMAINS — 53 witnesses, measured not estimated. Stamped
> `q0Anchor: muon` with `q0Value = A`, so moving the anchor makes them stale…
> Each needs its producer re-run at C. NOT done here."*

The commit landed the core deliberately unfinished. **53 has since become 83**
as further muon-pinned witnesses landed on top.

So the red is not a regression, not a phantom, and not this branch's: it is
the tail of an authorised mid-migration, and it grows while it is left alone.

## Scope, measured

**83 witnesses → 75 distinct producers.** 9 witnesses carry no `scriptFile`
and need their producer identified by hand.

Three groups, and only the first is a plain re-run:

1. **Re-run at C** — the bulk. Cost is uneven: `atomic_tr_m_mpfr_50dps`,
   `ame_2020_binding_energies` and `derived_chi_catalogue_matrix_m_mu_n_mpfr`
   are long-compute; `hadron_knot_table` is documented in AGENTS.md as
   running > 50 min for one bound atom and **not finishing**.
2. **By design, so a re-run is not the fix** — `muon_pin_three_values_probe`
   and `muon_pin_stored_vs_live_gate` exist precisely to record A, C and the
   CODATA-2018 value side by side. A producer whose job is to hold the old
   value will hold it again after any re-run. These need the audit to know
   they are comparisons, not a producer change.
3. **Anchor-defining** — `q_pinning_50_digit.py`. Per AGENTS.md rule 1 of the
   migration constraints, **never re-pin it as a consumer**; it is what
   `witness._q0_value_for_anchor("muon")` reads. It is already at C.

## The order is load-bearing

Several of these producers read each other's witnesses. Running them
alphabetically re-emits stale upstream values into freshly-run downstreams —
the defect `q0_repin_sweep.topo_order()` exists to prevent (`qou-lt8x`). Any
drain must build producer → witness → reader edges from the actual files and
run in topological order.

## What must not be done

Per AGENTS.md: **never make a red run green by widening a baseline.** No
`--rebaseline`, no adding a file to `raw-float64-baseline.json`, no
hand-editing a digit. Baselines drain, they do not grow. The fix is at the
producer, and it is a re-run.

## Environment caveat for whoever runs it

This container reports **mpmath 1.3.0** where `main`'s committed witnesses
record **1.4.1**, and **clarabel is absent**. The audit itself warns that
committing from here would replace the environment stamp with a weaker
record. A drain run must either install the missing libraries first or
declare the degradation explicitly in its commit.
