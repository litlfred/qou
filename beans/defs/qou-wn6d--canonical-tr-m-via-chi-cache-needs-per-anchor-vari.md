---
# qou-wn6d
title: 'canonical-tr-m-via-chi-cache needs per-anchor variants: one cache cannot serve a muon L1 cross-check and proton consumers'
status: completed
type: task
priority: normal
created_at: 2026-08-22T10:27:39Z
updated_at: 2026-08-22T19:08:55Z
---

## Scoped by measurement — and the attribution splits in two

### Who actually needs which pin

Of the **7** consumers that read `canonical-tr-m-via-chi-cache.witness.json`:

| consumer | declared anchor | |
|---|---|---|
| `canonical_tr_m_via_chi_cache` (the producer) | `physical_proton` | |
| `cross_check_trM_1ppb` | `ideal_muon` | **MUON-GUARD** |
| `he4_binding_k_averaged_interface_probe` | undeclared | proton default |
| `he4_binding_k_fingerprint_stage1_probe` | undeclared | proton default |
| `he4_binding_k_presentation_correction_probe` | undeclared | proton default |
| `qbeta_trm_crosscheck_convention_pin_split_probe` | undeclared | proton default |
| `binding_q_target_sweep` | undeclared | proton default |

**Exactly one consumer needs muon**, and it is the one carrying the explicit guard. So a unilateral flip to muon would break five consumers to satisfy one — the per-anchor pair is the right shape, mirroring `_Y_LAMBDA_BY_ANCHOR`, and the muon variant serves a single reader.

### The regeneration itself is cheap

`QOU_Q0_ANCHOR=ideal python3 canonical_tr_m_via_chi_cache.py` works, is fast, and emits `q0Anchor: muon` correctly. **But it writes to the same filename**, so it cannot simply be run and committed — that is the whole of the remaining work: give the producer a per-anchor output path.

### 🛑 The attribution splits, and only half is mine

With the muon cache in place `cross_check_trM_1ppb` runs to completion — and reports **6 atoms compared, 0 certified at 1 ppQ, 6 divergent**.

I was about to record that as further damage from the migration. It is not. `main`'s **committed** witness already carries:

```
allPassed: False
all_atoms_within_1ppQ:  computed=0  expected=1  passed=False
character_engine_matches_closed_form: passed=True
```

So **0 certified / 6 divergent is the pre-existing state on `main`**, not something the migration caused. What the migration caused is narrower and precise: the producer **cannot run at all**, because its manifest entry moved and its guard correctly refuses a proton binding.

Splitting these matters. "My migration broke the L1 cross-check" would have been false in the way that costs a later agent the most — it would send them hunting a numerical regression that does not exist.

### Remaining work

1. Per-anchor output path on `canonical_tr_m_via_chi_cache` (the pattern already exists in `tr_m_wenzl_bridge_mpfr._Y_LAMBDA_BY_ANCHOR`), then generate and commit the muon variant. **Mine — caused by the migration.**
2. The 6/6 divergence is a **separate, pre-existing** question and should not be folded into this bean.

Tree restored: the proton cache on disk is untouched, and nothing from this scoping run is committed.
