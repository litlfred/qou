---
# qou-5le1
title: q0 classifier is blind to inline q0 re-derivation and to cross-module Q0 imports
status: todo
type: task
priority: normal
created_at: 2026-08-23T22:25:50Z
updated_at: 2026-08-23T22:26:45Z
---

## What

`q0_producer_pin_classifier.classify()` reads a file for muon **accessors**
(`q_muon_at`, `Q_MUON`, …), muon **artifacts** (`q-pinning-50-digit`,
`y-lambda-at-q0`) and the hardcoded muon **literal**. Two ways of being a muon
producer carry none of those tokens, so both classify as `none`.

### Mode A — inline re-derivation of the anchor

```python
from codata_2022_source import M_MU_OVER_M_E
hbar_q_sq = Vol_4_1 / M_MU_OVER_M_E
q0        = mp.mpf(1) / (mp.mpf(1) - mp.sqrt(hbar_q_sq))
```

This is `q_muon_at()`'s closed form, `q = 1/(1 − √(Vol(4₁)/(m_μ/m_e)))`, retyped
— so the producer is muon by construction. Nothing in it matches an accessor,
an artifact or a literal. Confirmed instances, all three verified by reading:
`t6_three_halves_factor_probes`, `xi_ell_phi_q_probe`,
`probes/t6_tau_h5_embedding_probe`.

**Population, measured:** 20 `.py` files import `M_MU_OVER_M_E`; **9** of those
also compute the `1/(1 − √…)` closed form.

### Mode B — cross-module `Q0` import

```python
from hecke_channel_binding_probe import channels, BONDS, E0, Q0, h, z
from he3_brane_tower_structural_gap import Q0, VHAT, Z_N, B_AME, …
```

The classifier is **per-file**, so a producer that imports `Q0` from another
producer inherits its layer invisibly. Both upstreams here were re-bucketed to
`ideal_muon` in #5588, so the two importers are muon — and both classified
`none`. Instances: `probes/deuteron_fpn_wlambda_wiring`,
`probes/he3_tower_charge_asymmetry_probe`.

## Why I did not just add a name

The obvious move is `MUON_NAMES |= {"M_MU_OVER_M_E"}`. **That over-fires**: of
the 20 importers, 11 use the ratio for something other than deriving q₀
(reporting `m_μ/m_e` as an observable is anchor-neutral). The correct signal for
Mode A is compound — *imports the ratio* **and** *computes the closed form* —
which is a shape check, not a name entry.

This caution is not hypothetical. Promoting `y_lambda_at` to an identifier check
in the same classifier reclassified **56 producers** `proton → BOTH`, and `BOTH`
shields a producer from triage. Caught by a spot-check; see `qou-vu19`.

Mode B needs cross-module resolution — following a `from <sibling> import Q0`
to the sibling's own verdict. That is a real capability change, not a constant.

## Next

1. Mode A: a shape check for `1/(1 − sqrt(<expr involving the muon ratio>))`,
   measured against the 9 candidates and inspected before landing.
2. Mode B: resolve `Q0` imports one hop and inherit the source's verdict. One
   hop is probably enough; measure whether any chain is deeper.
3. Re-run the `qou-bdkx` triage after each and report the delta, so the effect
   is visible rather than assumed.
