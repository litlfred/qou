---
# qou-wee5
title: xi_ell_phi_q_probe and t6_tau_h5 shift 1.1e-7 on a manifest entry they never reference
status: todo
type: bug
priority: normal
created_at: 2026-08-23T22:25:49Z
updated_at: 2026-08-23T22:26:45Z
---

## What

Two probes change their computed output when a stem is added to
`computations/q0_anchor_manifest.json` — **a file neither of them references**,
directly or through any visible import.

Isolated properly, one stem at a time on an otherwise clean tree:

```
ideal_muon += {"xi_ell_phi_q_probe"}      # nothing else changed
-> max_abs_V   0.3164349897485959  ->  0.3164350254931353     (1.13e-7 rel)
   m_li2q_sym  0.29449812380443614…  ->  0.29449815487914650…
   m_phi_direct, m_log_phi, and 38 further fields also move
```

`t6_tau_h5_embedding_probe` behaves the same way, 15 fields.

## Why this is a straddle, not a re-pin

Both probes derive q₀ **inline**, from the muon ratio:

```python
from codata_2022_source import M_MU_OVER_M_E
cal2_target = M_MU_OVER_M_E
hbar_q_sq   = Vol_4_1 / cal2_target
hbar_q      = mp.sqrt(hbar_q_sq)
q0          = mp.mpf(1) / (mp.mpf(1) - hbar_q)
```

That is `q_muon_at()`'s closed form retyped, and it does **not** consult the
manifest. So the q₀ these probes use is muon *whatever the manifest says* — and
yet a manifest entry moves their numbers by 1.1e-7. **Something else in their
import cone resolves through the anchor**, and the two sources are combined in
one computed quantity. That is the layer straddle AGENTS.md calls a defect
regardless of size.

Grepped and confirmed absent from `xi_ell_phi_q_probe.py`: `q_parameter`,
`qou_substrate`, `Q_50_DIGIT_STR`, `q_at(`, any `from constants` import. So the
dependence arrives through the cone (`_path_bridge`, `codata_2022_source`,
`_precision`, or a sibling probe), and **which input carries it is not yet
located** — that is the open question here, not the existence of the effect.

## Scale

1.13e-7 relative is ~113 ppb: about **10× the 11.5 ppb μ–p substrate tension**
and ~1e8 × the 1 ppQ L1 compute-precision target. Large enough that any
conclusion drawn from these probes depends on a manifest entry nobody would
think to check when reading them.

## Not fixed here, deliberately

The guard in the `qou-bdkx` re-bucketing run caught this and **reverted** both
(the rule being: keep a manifest move only if the stamp moved and no
mathematical field did). Both stems stay out of `ideal_muon`. Re-bucketing them
would be a *migration* — it changes numbers — not the label correction the rest
of that arc was.

Their sibling `t6_three_halves_factor_probes`, with the **identical** inline
derivation, was stamp-only and was re-bucketed. So the dependence is not a
property of the shared formula; it is something these two reach and it does not.
That contrast is the cheapest lead.

## Next

1. Bisect the import cone. Add the stem, then re-run with each cone module
   swapped for a stub, until the 1.1e-7 moves or stops.
2. Diff the cone against `t6_three_halves_factor_probes`, which does **not**
   show the effect despite the same q₀ derivation — the difference between the
   two cones is where to look first.
3. Once located, decide whether the correct fix is to pin the second source
   explicitly or to remove it. Do **not** re-bucket the stems until then.
