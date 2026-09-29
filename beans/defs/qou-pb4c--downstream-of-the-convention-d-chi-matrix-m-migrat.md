---
# qou-pb4c
title: 'Downstream of the convention-D chi-matrix-m migration: 23 consumers, 14 witnesses, tr_M moved 15.4%'
status: todo
type: task
priority: normal
---

## Why this exists

Eight `chi-*-at-q0-50dps-matrix-m` witnesses were migrated C → D
(`qou-lt8x`). The numbers moved **materially**, not marginally:

| | old (C) | new (D) | shift |
|---|---|---|---|
| proton `y_λ(1,1,1)` | 0.0227449425 | 3.50e-72 (dead) | → 0 |
| proton `tr_M(q₀)` | 1.6331535901 | 1.8843194673 | **+15.4 %** |

Anything that read those witnesses and committed a number is now stale by
roughly that order. This bean is the downstream sweep; it is deliberately
separate from `qou-lt8x`, which is the migration itself.

## Measured blast radius

**23 live producers** reference `matrix-m` / `at-q0-50dps-matrix`
(`_deprecated/` excluded):

    chi_4he_via_rust_lossless            delta_lambda_empirical_tabulation
    deltalambda/li6_h18_amplification_discriminator_probe
    deltalambda/carrier_saturation_mechanism_probe
    deltalambda/deltalambda_icosahedral_smatrix_magnitude_probe
    derived_chi_catalogue_matrix_m       derived_chi_catalogue_matrix_m_mpfr
    derived_chi_catalogue_matrix_m_mu_n
    derived_chi_catalogue_matrix_m_multi_a_benchmark
    chi_via_rust_lossless                atom_vhyp_closure_matrix_m
    chi_at_q0_via_matrix_m_mpfr          hoefsmit_symbolic
    spectral_selector_validate           nucleus_operator_selection_sdp
    chi_convention_audit                 active_set_truncation_prototype
    chi_convention_trM_ratio_probe       low_isotopes_binding_sweep
    cap_free_trm_prototype               (+ 3 more)

They emit **14 witnesses**:

    active-set-truncation-prototype      atom-vhyp-closure-matrix-m
    cap-free-trm-prototype               carrier-saturation-mechanism
    chi-at-q0-rust-lossless-helium-4     chi-convention-audit
    chi-via-rust-lossless-general        delta-lambda-empirical-tabulation
    delta-lambda-energy-scale-extensivity
    deltalambda-icosahedral-smatrix-magnitude
    li6-h18-amplification-discriminator  low-isotopes-binding-sweep
    nucleus-operator-selection-sdp       spectral-selector-validate

## Sequencing — do NOT just re-run all 23

`qou-lt8x` established that a re-run is not automatically a migration, and
three of its lessons apply directly here:

1. **Self-caching producers.** `chi_via_rust_lossless` treats its own output
   witness as a cache and prints *"cached — skip recompute"*; there is no
   `--force`. A plain re-run reads the stale value back. Check each consumer
   for the same pattern before believing a green run.
2. **Dependency order matters.** Several of these read each other
   (`derived_chi_catalogue_matrix_m*` family, `chi_4he_via_rust_lossless`).
   Running alphabetically re-emits stale upstream values into freshly-run
   downstreams — the exact defect `topo_order()` was added to fix in the
   earlier campaign.
3. **A flag is not a diagnosis.** Before "fixing" any of these, classify:
   genuinely stale, solver residue, placeholder literal, or symbolically
   zero. On the `qou-lt8x` sample, 3 of 4 flags were not convention C at all.

## Watch items

- **`chi_convention_audit` and `chi_convention_trM_ratio_probe`** audit the
  convention itself. Like `weight-factor-audit`'s C8 criterion, they may
  legitimately *evaluate* the C formula — a changed number there may be the
  audit doing its job, not staleness. Read before regenerating.
- **`nucleus_operator_selection_sdp`** is an LP/SDP producer, so per
  AGENTS.md it must emit primal **and** dual (`y0_star`, `y_star`,
  `active_set`, `duality_gap`). If it is re-run, that is the moment to check
  the dual is present rather than after.
- **`low_isotopes_binding_sweep`** and the `delta-lambda-*` witnesses feed
  binding numbers. A 15.4 % tr_M shift is far above any accuracy target in
  `docs/precision-goals.md`, so any L2 figure derived from them is currently
  unreliable and should not be quoted until re-run.

## Related, and worth settling first

**Proton ≡ neutron identically in this family** — before *and* after the
migration. Same for tritium ≡ ³He. Since `Δ(tr_M(n) − tr_M(p))` is what sets
E₀ / Q_β, a family that cannot distinguish the species is a problem for
anything downstream that wants the p–n split. This is **not** a regression
from the migration (the old committed values were equal too), but it means a
downstream consumer reading these for an asymmetry gets zero. Bean this
separately if it is not already covered.

## To close

1. Build the consumer → witness dependency graph and topologically order it.
2. Per producer: classify the flag, check for a self-caching guard, re-run in
   order, record the per-quantity ppm/percent movement.
3. Report the impact by *physical quantity*, not by file count — the
   `qou-eea0` "total impact" standard.
