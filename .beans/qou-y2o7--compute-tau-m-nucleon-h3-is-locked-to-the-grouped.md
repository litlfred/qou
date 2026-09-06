---
# qou-y2o7
title: compute_tau_M_nucleon_H3 is locked to the grouped ordering by its monotone-only chi kernel; 18 consumers inherit it
status: in-progress
type: bug
priority: normal
created_at: 2026-09-06T11:12:06Z
updated_at: 2026-09-06T11:12:40Z
---

## The mechanism

`closed_form_tau_M.compute_tau_M_nucleon_H3` does not call
`atom_braid_word_3A`. It builds its own word from the `hecke_core` chains:

```python
# The chain is (c, d, gen) and MONOTONE (all gen 0, then all gen 1),
# which is what `chi_all_lambda` requires.
word = [(mpf(c), mpf(d), 0) for c, d in g0] + \
       [(mpf(c), mpf(d), 1) for c, d in g1]
```

The comment states the cause outright. `chi_monotone_transfer.chi_all_lambda`
is the **monotone-only** transfer kernel, so the word has to be monotone, so
the generators are emitted grouped. The 2026-09-05 owner ruling (`qou-hu1f`)
says the canonical intra-nucleon core is **borromean**, `(σ₀σ₁⁻¹)³`, which is
non-monotone by construction:

    grouped   (as built here)   gen sequence [0,0,0,0,0,0,0,1,1,1,1]
    canonical (atom_braid_3A)   gen sequence [0,1,0,1,0,1,0,0,1,0,0]

This is not a stale constant that a re-run fixes. The function **cannot
express the canonical word** while it uses that kernel.

## Measured

At the proton pin, 50 dps, via `chi_general_word.chi_all_lambda_any` (the
dispatcher, which accepts both):

| | grouped (shipped) | canonical (ruling) | ratio |
|---|---:|---:|---:|
| τ_p | 1.145759692457300869689 | 0.629328402202921918165 | 1.8206 |
| τ_n | 0.987743688115809571634 | 0.475133517155682212506 | 2.0789 |

Cost is not the obstacle: at H₃ the general kernel is `d_λ ≤ 2`, sub-second.
Swapping `chi_all_lambda` → `chi_all_lambda_any` and the hand-built word →
`atom_braid_word_3A(1,0)` / `(0,1)` reproduces the canonical column exactly.
I verified this; I have **not** applied it (see scope below).

## Blast radius — 18 consumers

`legacy_marshalled_frame`, `nucleus_sdp_assembly`,
`per_knot_mass_table_demonstration`, `binding_channel_taxonomy_probe`,
`deuteron_from_scratch_ledger`, `probes/gap_a4_He3_residual_probe`,
`probes/nucleon_h3_marshalling_divergence_probe`, `probes/gap_a4_S_K_additive_probe`,
`probes/gap_a4_T2_per_knot_vol_probe`, `probes/gap_a4_L1_light_series_probe`
(+ `_perknot_rerun`), `probes/binding_triangle_3body_cluster_probe`,
`mass_table_comprehensive`, `binding_color_vs_charge_tn3he`,
`atomic_tr_m_helium4_canonical`, `qbeta/qbeta_delta_vs_deltaTbeta_settled_probe`,
`binding_channel_saturation_probe`, `closed_form_tau_M` itself.

Several feed published mass/binding tables. The reference witness the
docstring validates against — `habiro-coefficients-atomic.witness.json`,
τ_p = 1.14575969245730087 — is itself grouped-era, so the whole cluster is
*internally consistent* in the superseded ordering. That is why no
cross-check caught it.

## Why the qou-hu1f sweep missed all of it

Same selector gap as `binding_canonical`: the sweep selected witnesses whose
producers reference `atom_braid_word_3A` by name. This subsystem reaches the
nucleon braid through `hecke_core._PROTON_G0/_G1` instead, so it was invisible.
Two independent subsystems have now been found this way; the selector, not the
individual producers, is the thing to fix.

It is also a `word-provenance-gate` defect in spirit — a word built by hand
rather than obtained from its producer — but the gate looks for literal integer
lists and this is assembled from named constants, so it does not fire.

## Independent confirmation that borromean is the right target

Three structurally independent routes to canonical |tr_M(⁴He)| agree exactly
once borromean nucleon inputs are used (`qou-hft3`):

    Wenzl bridge on atom_braid_word_3A(2,2)   0.0112374176597674215641995493744
    markov_trace_canonical (binding_canonical) 0.011237417659767421564199549374…
    closed_form_tau_M, bring_color_weighted    0.0112374176597674215641995493744

The third is `closed_form_tau_M` **fed borromean τ_p, τ_n by hand**. Fed the
grouped values this function supplies, it returns 0.16097414544240738 — off by
14.325, which is exactly (1.8206)²·(2.0789)². So the closed form is correct and
its inputs are not.

That comparison also discriminates the pn convention independently:
`bring_color_weighted` matches to 30 digits while `chi_lambda_braid` /
`uniform` give 0.013547 (20 % off), confirming the owner's 2026-08-15 R3
ruling from a direction that did not assume it.

## Scope — deliberately not fixed here

Changing this moves numbers in 18 producers and contradicts a reference witness.
That is a subsystem-wide ruling application and an owner call, not a side effect
of a helium-4 fix. What I did instead: `atomic_tr_m_helium4_canonical.py` alone
is corrected at its call site, because its published value is *labelled
canonical* and is 14.3x wrong.

**Decision needed:** apply the ruling across this cluster (swap the kernel,
take the word from its producer, regenerate the 18 + the habiro reference), or
record a documented reason the nucleon H₃ blocks stay grouped.
