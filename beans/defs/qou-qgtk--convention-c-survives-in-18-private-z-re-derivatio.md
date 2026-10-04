---
# qou-qgtk
title: Convention C survives in 18 private z re-derivations that library fixes cannot reach
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T22:22:29Z
updated_at: 2026-10-04T15:18:08Z
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

## 2026-09-15 — re-measured: 18 -> 3 unannounced, and all three now DECLARED

Owner directive "excise convention C". Re-measured before acting, because the
"18 live sites" figure dates from 2026-08-15 and a month of excision has landed
since. The count is stale, and so was the framing.

### Measuring it needed two passes, and the first was wrong

A text sweep for the two disguises (`sqrt(q)/(q+1)` and `1/(√q + 1/√q)`, plus
the `t = √q` spellings `t/(t²+1)` and `1/(t + 1/t)`) returns **135 files, 205
occurrences** — useless as a work list, because nearly every one is a docstring
saying "excised", a C-vs-D comparison that needs z_C, or a detector defining the
pattern.

Narrowing to ASSIGNMENTS whose right-hand side is the shape: **93**, of which
**73 self-declare** — the target is named `z_C`/`zC`/`Z_C`, or the surrounding
lines say convention C / excised / was C. That leaves 20, and 17 of those are
dict or list literals whose KEY declares the convention
(`{'C': sqrt(q)/(q+1), 'D': q**3/(q**2+1)}`, `CONVENTION_Z`, `Z_SPELLINGS`) —
my target-name check could not see a key. A fourth,
`qbeta_c3_derivative_vs_value_precision_probe`, declares "Convention C" in its
MODULE docstring, outside the ±3-line window.

**Genuinely unannounced: three.**

    qbeta_eta_singularity_probe.py:180          zq = mp.sqrt(qq) / (qq + 1)
    qbeta_wenzl_c3_candidate_audit_probe.py:88  z  = mp.sqrt(q) / (q + 1)
    qbeta_h_frame_rungs_probe.py:73             z  = 1 / (sp.sqrt(q) + 1/sp.sqrt(q))

### They are not three sites, they are one — and swapping them is FORBIDDEN

All three feed `alpha = (z - 1)·h/2`, the qbeta ladder's `alpha_eff`. I checked
before touching them, and `qbeta_ladder_convention_fee_probe` is explicit: the
published agreement needs z_C, substituting z_D sends the ladder to 601192 ppb,
and **that number is NOT "what convention D gives"**. AGENTS.md and
`QOU.QBeta.decayLadder_zC_threeRow_ne_zero` both state the ladder must be
RE-DERIVED under D and that **a z-swap is not a valid move** — if the decay
channel's decomposition kills the third row then its trace IS z_D, and the
existing C-frame ladder is not that trace.

So excising C here means DECLARING it, not swapping it — the `qou-cexc`
precedent, "declared, not silent". All three now carry an explicit note giving
both z values, why the site is C, and why a swap is the wrong move with the
citation. Comment-only: both re-runnable probes pass unchanged (6/6 and clean),
and no witness value moved — the sole diff is a `pyhecke_native_build` hash from
this container's rebuilt Rust extension.

### Residue

**Unannounced private z_C re-derivations: 0.** What remains is the ladder's
re-derivation under D, which is a science task owned elsewhere in the arc, not a
detector or hygiene one.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: 73c2db9b41 "private z_C re-derivations 18 -> 3 -> 0"; body: residue 0, remainder is the ladder (cds1); 1 main commits
