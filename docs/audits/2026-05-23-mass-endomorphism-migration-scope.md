# `mass_endomorphism.py` migration — scope correction (post-#944)

> **Conclusion (TL;DR).** Cheat-sheet §5 Migration Backlog #2 ("20
> importers off SUPERSEDED `mass_endomorphism.py`") overstates the
> migration scope. **15 of 20 importers are utility-only** —
> they consume substrate utilities (`Phi_q`, `q0`, `z_mark`,
> Wedderburn weights, `proton_cross`/`neutron_cross`) from the
> module. The DEPRECATED API surface is `mass_from_tower` (+ its
> helpers `additive_wedderburn_volumes`, `tr_M_atomic_at_q0`).
> Only **4 importers** call the deprecated surface. The other 15
> require no migration — they should keep importing from
> `mass_endomorphism.py` as a substrate-utility module.

## Method

Post-#944 (H_12 Phase-1 extract landed), enumerate the 20 importers
identified by:

```bash
grep -lE "from mass_endomorphism|import mass_endomorphism" \
  computations/*.py | grep -v _deprecated
```

For each, classify by import target:

- **Deprecated API**: `mass_from_tower(...)`, `additive_wedderburn_volumes(...)`,
  `tr_M_atomic_at_q0(...)` — the operator-valued mass-tower
  surface superseded by `prop:mass-tower-operator-valued` (and its
  compute equivalent `mass_tower_operator_valued.py`).
- **Substrate utilities (NOT deprecated)**: `q0`, `qi0`, `HA`,
  `z_mark`, `Phi_q`, `qint`, `qfact`, `qdim`, `w_sym`, `w_std`,
  `w_alt`, `proton_cross`, `neutron_cross`. These are substrate
  constants / helper functions used across the framework.

## Inventory

### Substantive deprecated-API callers (5 scripts — true migration targets)

| Script | calls | Notes |
|---|:---:|---|
| `mass_endomorphism.py` | 10 | self-import (the module itself) — N/A |
| `m_p_m_e_li2q.py` | 3 | needs migration to `mass_tower_operator_valued` |
| `mass_at_3A_proper.py` | 2 | already imports H_12 extract indirectly; check for full path migration |
| `pn_alpha_lp_dual.py` | 2 | needs migration |
| `probe_t2_t3_proton_neutron_a1.py` | 1 | needs migration |

**Net: 4 scripts** require true migration of `mass_from_tower` call-sites to the post-#944 `mass_tower_operator_valued` API.

### Utility-only importers (15 scripts — NO migration needed)

| Script | What it imports |
|---|---|
| `adjacent_vs_full_probe.py` | `q0`, `Phi_q`, `z_mark` |
| `atom_level_wedderburn_tower.py` | `Phi_q` |
| `brane_tower_isospin_diagnosis.py` | `Phi_q` |
| `brane_tower_two_avenues_probe.py` | `Phi_q` |
| `canonical_plus_multibrane.py` | `Phi_q`, `z_mark` |
| `canonical_tower.py` | `Phi_q`, `z_mark` |
| `catalan_binding.py` | `w_sym`, `w_std`, `w_alt`, `Phi_q` |
| `crt_markov.py` | `proton_cross`, `neutron_cross` |
| `d_density_derivation.py` | `w_sym`, `w_std`, `w_alt` |
| `mass_formula_6term.py` | `Phi_q` |
| `murnaghan_nakayama.py` | `proton_cross`, `neutron_cross` |
| `paper_six_term_isotope_sweep.py` | `Phi_q` |
| `probe_brane_tower_finite_laurent.py` | `Phi_q` |
| `multi_level_jet_sum.py` | `q0`, `Phi_q`, `z_mark` |
| `sigma_shell_characterization.py` | `q0`, `qi0`, `z_mark`, `HA` |

These 15 should continue importing from `mass_endomorphism.py` (whose utility surface is not deprecated). The block-level supersession (`prop:mass-endomorphism-tower` → `prop:mass-tower-operator-valued`) is a CONTENT-OBJECT relation, not a Python-module deprecation.

## What this means for cheat-sheet §5 #2

The current cheat-sheet says:

> #2 SUPERSEDED `mass_endomorphism.py` migration (20 importers) — gated on Lean (Z+N) / H_12 Phase-2

After this audit, the corrected status is:

> #2 SUPERSEDED `mass_endomorphism.py` **operator API** migration:
> 4 substantive callers (`m_p_m_e_li2q.py`, `mass_at_3A_proper.py`,
> `pn_alpha_lp_dual.py`, `probe_t2_t3_proton_neutron_a1.py`)
> need migration to the post-#944 `mass_tower_operator_valued`
> equivalents. The other 15 utility-only importers consume
> substrate helpers from the module — no migration needed.

## Recommended downstream

Per the 4 substantive callers, individual follow-up PRs (one per script, or one consolidated PR if the call-pattern is mechanical):

1. **`m_p_m_e_li2q.py`** — uses `mass_from_tower` for proton + electron mass-tower computation. Likely the heaviest migration; needs replacement with `mass_tower_operator_valued`-API equivalents.
2. **`mass_at_3A_proper.py`** — imports `z_mark`, `mass_from_tower`. The `z_mark` import is utility (no change); the `mass_from_tower` call is the migration target. Should consume the post-#944 H_12 Phase-1 witness for ⁴He at A ≤ 4.
3. **`pn_alpha_lp_dual.py`** — imports `mass_from_tower`, `HA`, `z_mark`. Two of three are utility. The one substantive call needs migration.
4. **`probe_t2_t3_proton_neutron_a1.py`** — has 1 deprecated call; likely mechanical.

## Why this matters

Without the scope correction, downstream agents/sessions reading the cheat-sheet would attempt a 20-script migration when **75% of those scripts have nothing to migrate**. That work would be wasted effort + risk introducing bugs (changing import paths for utility helpers that don't need changing).

The corrected scope (4 scripts, all with clear substitution targets) is tractable in 1-2 follow-up PRs.

## Cross-references

- [PR #944](https://github.com/litlfred/qou/pull/944) — H_12 Phase-1 A-operator extract (unblock parent)
- [`docs/canonical-derivation-cheat-sheet.md §5 #2`](../canonical-derivation-cheat-sheet.md) — the row to update
- `mass_endomorphism.py:114 mass_from_tower` — the deprecated entry point
- `mass_tower_operator_valued.py` — the replacement (verification script for now; the API surface for downstream consumers needs concretisation)
