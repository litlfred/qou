# The superseded-muon class is 19 actionable, not 260

**Date:** 2026-08-28
**Beans:** `qou-1c4y` (the migration umbrella)
**Branch:** `claude/superseded-muon-triage-2026-08-28`

## Why this measurement exists

[`2026-08-22-q0-migration-worklist-partition.md`](2026-08-22-q0-migration-worklist-partition.md)
established that the corpus carries **two** muon values agreeing to 11 digits —
the live ideal/CAL-2 pin `1.10997859555733471…` and a **superseded** one,
`1.10997859555418057…` — and that the superseded class was the *larger* of the
two. It was recorded as the largest untouched population in the q₀ arc and
recommended as the next work item on that basis.

**That recommendation was inflated, by the same error class the arc kept
correcting.** A population count is not a work count.

## Measured on `main`, 2026-08-28

```
witnesses carrying the superseded value          265
  under _deprecated/                             214   ← 81%, not live work
  live                                            51
    no scriptFile at all (orphan)                 13
    scriptFile names a missing producer            2
    scriptFile names a LIVE producer              36
      self-declaring (deliberate)                 17
      GENUINE candidates                          19
```

**265 → 19.** A 14× over-count of actionable work.

## The 17 deliberate ones declare themselves

They carry the superseded value under a field or a producer name that says so:

| signal | producers |
|---|---|
| `stale_muon_pin_q0` | `mp_dk_decisive_test`, `per_basis_row_invariants_probe`, `qbeta_multi_block_eigenphase_probe`, `qbeta_multi_block_eigenphase_full_eps_probe` |
| `q0_muon_pin` / `q_muon` / `q0_muon` | `c_3_categorical_derivation_attempt`, `probe_mup_dressing_attribution`, `qbeta_chain4_kashiwara_step3_cross_anchor`, `qbeta_chain4_kashiwara_step4_n5`, `qbeta_complex_c3_fibre_probe`, `qbeta_qbessel_crossanchor_smoothness_refutation` |
| subject *is* the pin history | `muon_pin_three_values_probe` (`q0_from_CODATA_2018`), `probe_trace_convention_production_impact` (`S2_q0_current_muon_pinned`) |
| subject *is* literals | `fitted_labelled_canonical_audit`, `hardcoded_q0_literal_families_audit` |

A producer whose subject is the pin history necessarily contains superseded
pins. Re-pinning it would destroy what it measures.

## The 19 genuine candidates

`alpha_em_smatrix_perloop_probe`, `build_six_term_substrate_model_b`,
`chirality_avg_content_chiral`, `compound_binding_via_differences`,
`confinement-operator-selection`, `d_from_scratch`,
`delta_coupling_closed_form_probe`, `derived_masses`, `deuteron_delta_i_audit`,
`garside-irrep-qvalues`, `he4_partition_dominance_audit_probe`,
`implied_h2_coefficient_audit_50dps`,
`lambda_scale_homflypt_skein_recursion_probe`, `neutron_error_diagnostic`,
`q_beta_predicted`, `qbeta_h4_route_a_gate_probe`, `snappy_cusp_seeding`,
`term5_aK_audit`, `universal-ilp`.

These carry the superseded value under a **bare pin key** (`q_0`, `q0`, `q`,
`q_0_50dps`, `q_0_mpf50`) with nothing declaring it deliberate.

**19 is still an upper bound, not a defect count.** Each needs an individual
read — the arc's standing lesson is that a count from a detector is a
hypothesis until one of its members has been opened by hand, and that rule has
already corrected numbers here in both directions (dual-purpose 21 → 3;
contradictions 2 → 11). Two in this list are worth flagging before anyone
starts: `q_beta_predicted` carries `CAL-2_q_0`, and naming CAL-2 identifies
*which calibration*, not *which pin* — the exact conflation
[the partition audit](2026-08-22-q0-migration-worklist-partition.md) retracts.
`confinement-operator-selection` is an LP/SDP witness, so the dual fields
matter to any re-run.

## 🛑 The "13 orphans" were my detector's blind spot, not a provenance gap

An earlier revision of this document called the 13 a provenance gap — *"nothing
can regenerate them and nothing identifies what did"* — and proposed a bean for
them. **That was wrong, and it is the fourth detector correction in this arc.**

The scan keyed on `scriptFile` / `script`. Opening the 13 by hand:

| how provenance is recorded | count | resolves? |
|---|---:|---|
| under `computation`, naming a producer path | 8 | **all 8 exist** — 6 under `docs/audits/scripts/`, which a `computations/`-scoped search cannot see |
| no provenance field, but the witness-name ↔ producer-name convention holds | 5 | **all 5 exist** |
| genuinely unregenerable | **0** | — |

The five that record nothing still resolve by name:
`alpha-k-jones-markov-h4` → `computations/alpha/alpha_k_jones_markov_h4.py`,
`consumer-control-arm-audit` → `computations/audits/consumer_control_arm_audit.py`,
`metallic-q-n4-character-sweep`, `q0-value-drift-audit`,
`two-quark-active-set-mahler-sweep` — the last of which this arc has been
regenerating all along, which should have been the tell.

So the real finding is smaller and different in kind: **13 live witnesses omit
`scriptFile`**, a field-completeness gap in how the schema is used, not a loss
of provenance. Nothing is unrecoverable and no bean is warranted for the
"orphans" as such.

### The pattern is now the finding

Four counts in this arc came from a field-keyed or shape-keyed detector of mine,
and **every one was wrong until a member was opened by hand** — twice too high,
twice too low:

| detector | direction | corrected |
|---|---|---|
| dual-purpose, by substring match | over 7× | 21 → 3 |
| contradictions, file-local scan | under 5.5× | 2 → 11 |
| superseded-muon "work", by population | over 14× | 265 → 19 |
| orphans, by `scriptFile` only | over ∞ | 13 → 0 |

That is not four unlucky scans. A detector encodes one spelling of the thing it
looks for, and the corpus has more spellings than any one scan carries —
`docs/audits/2026-08-15-detector-blindness-taxonomy.md` catalogues thirteen for
convention C alone, four of them found *by* detectors written to catch the
previous blind spot. Treat any count in this arc as a hypothesis with an error
bar of several fold until one of its members has been read.

## What this does not say

- It does not say the 19 are wrong. It says they are the only ones that could be.
- It does not authorise a sweep. The first bulk attempt broke `main` for 208
  producers (`qou-m9xp`); constraints 1–4 in AGENTS.md §"q₀ anchor convention"
  rule 4 stand.
- It does not touch the 214 deprecated witnesses. They are correct as recorded
  for retired code.
