---
# qou-dkm2
title: _li_2_q_util.load_q_50dps() defaults to the MUON pin — 28 live no-arg call sites
status: todo
type: task
priority: normal
created_at: 2026-08-22T19:53:28Z
updated_at: 2026-08-22T21:27:16Z
---

Found while measuring dual-purpose reads for `qou-1c4y` / `qou-v90i`.

## The trap

[`computations/_li_2_q_util.py`](../computations/_li_2_q_util.py):

```python
_Q_WITNESS_DEFAULT = Path(__file__).parent / "q-pinning-50-digit.witness.json"   # :124

def load_q_50dps(path: Path | None = None) -> tuple[mpf, mpf, mpf]:
    if path is None:
        path = _Q_WITNESS_DEFAULT        # :191  <- MUON-anchored
    ...
    q = mpf(d["derived_50_digit"]["q"])
    z = mpf(1) / (mp.sqrt(q) + mp.sqrt(qi))
    return q, qi, z
```

`q-pinning-50-digit.witness.json` carries `q0Anchor: "muon"`. So
**`load_q_50dps()` with no argument silently returns the muon pin**, against
the 2026-08-07 owner directive that compute defaults to proton — and with no
signal that a layer boundary was crossed. Same shape as the
`wedderburn_jones_markov.y_lambda_at` trap `qou-1c4y` already names, but via a
**default argument** rather than a cache-hit gate.

**Measured: 28 live no-arg call sites across 26 files.**
`_li_2_q_util` has 104 importers overall.

## Already found once, fixed point-wise, never at the source

`delta_lambda_v_hat_z_transfer_phase5d_4.py:80` carries a prior agent's marker:

> `# 🛑 Was: load_q_50dps(), which reads the MUON q-pinning-50-digit`

So the trap is corroborated and was patched in **one** file. The default was
left in place, and 28 call sites still take it.

## Second, separate observation — NOT claimed as a defect

The same function returns `z = 1/(√q + 1/√q)`. Verified at 50 dps:

    z from load_q_50dps  0.4993203340335612717689664
    z_C = √q/(q+1)       0.4993203340335612717689664   (agree to 1.3e-51)
    z_D = q³/(q²+1)      0.6126880505488901570445168   (differs by 18%)

So it is **convention C exactly**, and the pinning witness records the identical
value under `z_markov`. `scripts/convention-c-producer-audit.py` reports
**1 actionable site** and does **not** flag this one — a C value returned as a
**tuple element** is a spelling the detector does not scan, i.e. a further entry
for `docs/audits/2026-08-15-detector-blindness-taxonomy.md`.

**What is NOT claimed:** that this `z` is *the* Markov parameter subject to
owner ruling R1. A brane-tower pair weight and the Markov trace parameter
sharing a formula is exactly the glyph-collision hazard AGENTS.md §"Grep the
claim SHAPE" warns about; `compute_t2_t3_from_vols` uses it as `T3 = z²·Σ_{i<j}`,
which is not obviously the Markov role. That needs a corpus read or an owner
call, not a grep.

## Next

1. **Do not mass-rewrite the 28 call sites.** Some may be legitimately
   ideal-layer. The fix is at the source: make `path` required, or resolve
   through `q_parameter` and let callers opt into muon explicitly.
2. Decide whether the returned `z` is in R1 scope before touching it.
3. Add the tuple-element return form to the detector-blindness taxonomy.


## The callers measured (2026-08-22) — and they are contradictions, not just risk

26 files / 28 live no-arg call sites, by manifest declaration:

| declared | files |
|---|---:|
| `physical_proton` | **9** |
| UNDECLARED | 17 |
| **`ideal_muon`** | **0** |

**No caller legitimately wants muon.** The nine declared `physical_proton` are
the same defect as the direct readers, one hop out — verified by sampling
(`volume_def_reconcile`, `e0_lambda_composite`, `complex_fibre_cross_ratio`,
`vhat_tower_im_cancellation` all carry `q0Anchor: proton` with muon data).

The nine: `binding_block_multiplicative`, `binding_via_interface_knot`,
`complex_fibre_cross_ratio`, `convergence_safe_vhat_tower`,
`e0_lambda_composite`, `flavor_dependent_cusp_shape`,
`probe_9b_perlambda_brane_tower`, `vhat_tower_im_cancellation`,
`volume_def_reconcile`.

`q0_muon_population_partition.py` now follows this one-hop path, so the gate
counts them: **contradictions 2 -> 11**, producers reaching the muon pin
**53 -> 78**.

## What this settles, and what it does not

**Settles:** there is no legitimate-muon caller to protect, so changing the
default cannot break a correct consumer. That was the main unknown.

**Does not settle:** whether to (a) make `path` required — loud, 28 call sites
to touch; (b) resolve through `q_parameter` — silent, changes 28 producers'
numbers by ~11.5 ppb in one commit; or (c) add an explicit `anchor=` parameter
defaulting to proton. (b) is a bulk numerical change of exactly the shape that
broke main once (`qou-m9xp`), so it wants a deliberate call rather than an
idle-pass decision.
