---
# qou-qgtk
title: Convention C survives in 18 private z re-derivations that library fixes cannot reach
status: todo
type: task
created_at: 2026-08-15T22:22:29Z
updated_at: 2026-08-15T22:22:29Z
---


## Why the library fix could not reach these

`be59f0137` moved `pyhecke.gram.z` to convention D and replaced `G_INV` with the
quotient inverse `G_PINV`. That closed the blocker — and did nothing for a probe
that computes `z` **itself**.

Found via `mu4_rhoF_cluster_derivation_probe`, which looked like a deliberate
convention-C comparison and was not. It defines its own `markov_z` at line 72:

```python
def markov_z(q):
    t = mp.sqrt(q)
    return 1 / (t + 1 / t)      # convention C
```

Sweeping for the shape: **18 live sites**, in two algebraic disguises that are
the same number — `1/(√q + 1/√q)` and `sqrt(q)/(q+1)`. The square root is the
portable tell: C must leave ℚ(q), D never does.

## Triage — the half-integer-power count decides it

A site is a one-line change only if the surrounding algebra is generic in `z`.
Where the file also carries `q**1.5` terms, the *closed forms themselves* are
convention-C derivations, and changing only `z` leaves an internal straddle —
worse than uniform C.

**RE-DERIVE (4)** — widens `qou-102c` from one file to four:

| file | half-int powers |
|---|---|
| `bond_extensivity_equal_weight.py:61` | 2 |
| `charge_symmetric_coulomb_binding.py:56` | 2 |
| `lepton_t2n_torus_tower.py:78` | 2 |
| `mirror_split_coulomb_diagnosis.py:68` | 1 |

**ONE-LINE, done (9)** — `mu4_rhoF_cluster_derivation_probe`,
`inter_nucleon_linked_channel`, `knot_operator_census_group_actions`,
`log_delta_categorical_derivation`, `probes/ground_state_ordering_argmin_sweep`,
`probes/qbeta_5two_categorical_markov_volume_probe`,
`probes/qbeta_habiro_integrality_kill_test`,
`qbeta/qbeta_ck_sseries_operator_match_probe`,
`qbeta/qbeta_framing_zeta4_subprobe`.

**DELIBERATE, leave alone** — `markov_z_fibre_rank_bar_covariance_probe:148`
(`z_C_num`) and the `interface_factor_enhancing_check_probe` print, which name C
as the comparison arm.

Verified on `mu4_rhoF`: `z` 0.4993203341836945 → 0.6126880371464652, C
fingerprint gone.
