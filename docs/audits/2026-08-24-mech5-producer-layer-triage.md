# Mechanism 5 — per-producer LAYER triage

**Measured 2026-08-24 on `origin/main` @ `91e48f2586`.**
Beans: `qou-aj91` (mechanism 5), `qou-1c4y` (the migration this feeds).

Mechanism 5 is the fifth way a producer ends up holding a muon `q₀`: it binds
`q₀` straight out of **`computations/q-pinning-50-digit.witness.json`**, which
is not a source of `q₀` but the *definition of the muon anchor* —
`qou_substrate.witness._q0_value_for_anchor("muon")` reads
`derived_50_digit.q` out of that very file. A producer written this way
computes at muon whatever its manifest tag says, and `QOU_Q0_ANCHOR` cannot
reach it.

A sibling branch is fixing the **stamp** (`WitnessBuilder.q0Value` reporting
the anchor the payload used). This document is the complementary half: **which
layer does each quantity actually belong to.** The stamp fix makes the
witnesses honest; it does not decide that.

**Nothing here sweeps.** The classification is the deliverable.

---

## 0. Corrections to the population count, before anything is triaged

`qou-aj91` records the population as **85**. Measured here it is **95**, and
the difference is a **detector** difference, not corpus churn. Read this
section before quoting any number from it.

### 0.1 The in-tree detector under-reports by design, and by accident

[`computations/audits/q0_muon_population_partition.py`](../../computations/audits/q0_muon_population_partition.py)
reports **51**. Two separate reasons:

1. **By design** it `continue`s on any file matching `ROUTES_ANCHOR`
   (mentions `q_parameter` / `qou_substrate.constants` / `q_at(`). That is
   right for its question ("who never resolves an anchor at all") and wrong
   for this one: a file that reads the pin witness **and** imports
   `q_parameter` is the *rule-4 straddle inside one quantity*, which
   AGENTS.md forbids outright. **26 of the 95 are in exactly that state**
   and the in-tree detector cannot see any of them.
2. **By accident** it gates on
   `READS_JSON = json.load|read_text|open(`. The idiom the bean itself
   quotes —

   ```python
   q = mp.mpf(record_upstream(Q_PIN, _UPSTREAM_RECORDS)["derived_50_digit"]["q"])
   ```

   — opens nothing of its own, so a producer using it is invisible.
   [`per_atom_audit_witnesses.py`](../../computations/per_atom_audit_witnesses.py)
   is precisely that case, and it is **one of the two declared-proton
   straddles the bean names**. 16 of the 95 are invisible this way.

### 0.2 A sixth read shape: the same witness, a different field

Keying on the field `derived_50_digit` misses
[`probes/bwhk_st_matrix_corroboration.py`](../../computations/probes/bwhk_st_matrix_corroboration.py),
which binds

```python
Q0 = mpf(_pin.get("q0Value") or _pin.get("data", {}).get("q0Value"))
```

out of the *same* witness. Keying on `q0Value` instead over-reports, because
producers **emit** a field of that name. Measured terminal keys across the
population: `derived_50_digit.q` **59**, `q0Value` **17**.

### 0.3 So two independent detectors were run, and neither is sufficient

| detector | found | rationale |
|---|---|---|
| AST, keyed on the `["derived_50_digit"]["q"]` subscript chain | 79 | sees the field, blind to `q0Value` |
| AST taint from any pin-witness-mentioning expression, through `json.loads` / `read_text` / `record_upstream` / subscripts | 74 | sees any field, loses cross-function flow |
| **union — the population used below** | **95** | |
| seen by **both** | 58 | |

This is another instance of the pattern
[`docs/audits/2026-08-15-detector-blindness-taxonomy.md`](2026-08-15-detector-blindness-taxonomy.md)
catalogues: each detector was written to catch the previous one's blind spot
and acquired its own. **Do not treat 95 as final either** — treat the mech-5
surface as *measured by two methods that disagree by 21 files*, and re-measure
rather than trusting this count.

---

## 1. The headline correction: on `main` today the witnesses are mostly SILENT, not lying

The bean predicts a straddle in which `.q0Value` claims proton over a muon
payload. Measured across the **76** committed witnesses these 95 producers
emit:

| witness `q0Anchor` | count | value actually in the file |
|---|---|---|
| `muon` | 25 | muon — consistent |
| `proton` | 4 | proton string present |
| `independent` | 1 | muon |
| **absent** | **46** | 22 muon, 22 neither, 2 proton |

So the dominant live state is not a contradiction, it is **an omission**: 46
of 76 witnesses record no anchor at all, against AGENTS.md rule 4's last
bullet — *"Say which pin you used. Any new witness must record its q₀."*

That matters for how the sibling's stamp fix will read. Once `WitnessBuilder`
stamps the anchor the payload used, those 46 stop being silent — and the two
contradictions in §2 become **visible rather than created**. The stamp fix is
not what introduces them.

---

## 2. `D` — declaration/data contradiction (2) — the real defects

| producer | manifest tag | witness `q0Anchor` | pin fields co-read |
|---|---|---|---|
| [`gram_matrix_seminormal_h6.py`](../../computations/gram_matrix_seminormal_h6.py) | — | `proton` | — |
| [`per_atom_audit_witnesses.py`](../../computations/per_atom_audit_witnesses.py) | `physical_proton` | `proton` | — |

**[`per_atom_audit_witnesses.py`](../../computations/per_atom_audit_witnesses.py)**
— tagged **`physical_proton`** in
[`q0_anchor_manifest.json`](../../computations/q0_anchor_manifest.json), emits
`per-atom-audit-witnesses.witness.json` stamped `q0Anchor: "proton"` with
`q0Value: 1.10997858275138080759…` (the proton value), and at line 70 computes

```python
q0_f64 = float(mp.mpf(record_upstream(Q_PIN, _UPSTREAM_RECORDS)["derived_50_digit"]["q"]))
h_f64 = q0_f64 - 1.0 / q0_f64
```

from the **muon** anchor. Every `h`, `h²` and per-atom quantity downstream is
muon; the manifest, the stamp and the emitted `q0Value` all say proton. Three
declarations against one payload.

> **Separate defect, same file, not fixed here.** `float(mp.mpf(...))` and
> then all-`float` arithmetic violates the NO-FLOAT64 discipline
> (AGENTS.md §"PROBES ARE NOT EXEMPT"). It is noted rather than folded in, so
> the anchor change stays reviewable on its own. Note the interaction: at
> float64 the 11.54 ppb separation is ~7 orders above the arithmetic floor, so
> the anchor **does** move these numbers.

**[`gram_matrix_seminormal_h6.py`](../../computations/gram_matrix_seminormal_h6.py)**
— untagged (so runtime resolves proton), binds
`Q0_MP = mp.mpf(record_upstream(Q_PIN, …)["derived_50_digit"]["q"])` at line 78
(muon), and its committed `option-e-phase1-gram-h6.witness.json` carries
`q0Anchor: "proton"` with the full 50-dps proton `q0Value`. The Option-E
Phase-1 Gram matrices in that witness were computed at muon under a proton
header.

---

## 3. `G` — needs the author (8)

Each of these is **internally consistent** — muon read, `ideal_muon` tag, muon
stamp — and each computes a **Physical-Observations** quantity, which the
2026-08-07 directive puts on proton. The tag is a prior declaration by another
agent; overruling it means re-tagging *and* moving numbers. That is not an
agent's call to make silently.

| producer | manifest tag | witness `q0Anchor` | pin fields co-read |
|---|---|---|---|
| [`hydrogen_step_by_step.py`](../../computations/hydrogen_step_by_step.py) | `ideal_muon` | `muon` | — |
| [`low_isotope_sign_flip_diagnostic.py`](../../computations/low_isotope_sign_flip_diagnostic.py) | `ideal_muon` | `muon` | — |
| [`mass_sweep_wiring_status.py`](../../computations/mass_sweep_wiring_status.py) | `ideal_muon` | `muon` | — |
| [`probes/lambda_scale_substrate_probe.py`](../../computations/probes/lambda_scale_substrate_probe.py) | `ideal_muon` | `independent` | — |
| [`qbeta/qbeta_decay_sdp_extended_ck.py`](../../computations/qbeta/qbeta_decay_sdp_extended_ck.py) | `ideal_muon` | `muon` | `hbar_q_sq` |
| [`qbeta/qbeta_fsc_g_pattern_comparison.py`](../../computations/qbeta/qbeta_fsc_g_pattern_comparison.py) | `ideal_muon` | `muon` | — |
| [`qbeta/qbeta_symbolic_sdp_strict_complementarity.py`](../../computations/qbeta/qbeta_symbolic_sdp_strict_complementarity.py) | `ideal_muon` | `muon` | — |
| [`verify_isospin_bar_anomaly.py`](../../computations/verify_isospin_bar_anomaly.py) | `ideal_muon` | `muon` | — |

Two carry extra weight:

* **[`q1_mass_gap_probe.py`](../../computations/q1_mass_gap_probe.py)** — its
  own prose states **proton** intent while its manifest tag says `ideal_muon`
  and its witness is stamped `muon`. The declaration conflicts with itself.
  It also co-reads `plancherel_weights_n3` and `two_q` **from the pin
  witness**, so re-pointing only its `["q"]` read would leave those two on the
  muon anchor — a straddle created by the fix.
* **[`qbeta/qbeta_decay_sdp_extended_ck.py`](../../computations/qbeta/qbeta_decay_sdp_extended_ck.py)**
  — **do not touch pending `qou-cds1`.** The whole `c_k` ladder is
  convention-C-frame and awaits re-derivation under convention D; re-pinning a
  `c_k` producer now would mix an anchor change into a frame change.

---

## 4. `C` — legitimately muon (8)

| producer | manifest tag | witness `q0Anchor` | pin fields co-read |
|---|---|---|---|
| [`atomic_tr_m_mpfr_50dps.py`](../../computations/atomic_tr_m_mpfr_50dps.py) | `ideal_muon` | `muon`, `proton` | — |
| [`chi_lambda_he4_full_partition_table.py`](../../computations/chi_lambda_he4_full_partition_table.py) | `ideal_muon` | `muon` | — |
| [`cross_check_trM_1ppb.py`](../../computations/cross_check_trM_1ppb.py) | `ideal_muon` | `muon` | — |
| [`deltalambda/he4_stage2_ranking_seminormal_xcheck.py`](../../computations/deltalambda/he4_stage2_ranking_seminormal_xcheck.py) | `ideal_muon` | — | — |
| [`m_p_borromean_verification_50dps.py`](../../computations/m_p_borromean_verification_50dps.py) | `ideal_muon` | `muon` | — |
| [`probes/bwhk_st_matrix_corroboration.py`](../../computations/probes/bwhk_st_matrix_corroboration.py) | `ideal_muon` | — | — |
| [`q1_mass_gap_probe.py`](../../computations/q1_mass_gap_probe.py) | `ideal_muon` | `muon` | `plancherel_weights_n3`, `two_q` |
| [`terms_2_3_atom_per_gen_mpfr_50dps.py`](../../computations/terms_2_3_atom_per_gen_mpfr_50dps.py) | `ideal_muon` | `muon` | — |

* **`cross_check_trM_1ppb.py`** — AGENTS.md names it: *"L1 cross-check must
  run under the MUON q0 pin"*, one of the three producers that refuse a proton
  run by design.
* **`atomic_tr_m_mpfr_50dps.py`** — dual-layer by design; emits one witness
  per layer, which is why it is the only producer here stamped both.
* **`m_p_borromean_verification_50dps.py`** — deprecated for absolute mass by
  the 2026-06-24 owner ruling and retained as the record of the Family-A
  route. A frozen record must not be re-pinned; doing so would silently edit
  history.
* The rest are ideal/CAL-2-layer objects whose muon read **agrees** with their
  declaration. They are still *architecturally* wrong — the value is right but
  the mechanism bypasses `q_parameter`, so `QOU_Q0_ANCHOR` cannot reach them —
  and that is a `qou-1c4y` item, not a defect in the number.

---

## 5. `B` — declared two-anchor comparison (16)

The sanctioned carve-out in the owner's own words: *"we want proton unless for
an explicit reason (like comparison on proton vs muon results)"*. Each of
these binds **both** pins and labels each leg:

```python
Q0_MUON_STR   = record_upstream(_MUON_WITNESS, _UPSTREAM_RECORDS)["q0Value"]
Q0_PROTON_STR = qou_substrate.constants.Q_50_DIGIT_STR
...
{"muon": Q0_MUON_STR, "proton": Q0_PROTON_STR}
```

| producer | manifest tag | witness `q0Anchor` | pin fields co-read |
|---|---|---|---|
| [`alpha/alpha_em_form_comparison_probe.py`](../../computations/alpha/alpha_em_form_comparison_probe.py) | — | — | — |
| [`probes/borel_propertime_moment_attack_probe.py`](../../computations/probes/borel_propertime_moment_attack_probe.py) | — | — | — |
| [`probes/ksel1_singularity_selection_probe.py`](../../computations/probes/ksel1_singularity_selection_probe.py) | — | — | — |
| [`probes/ksel2_favard_jacobi_probe.py`](../../computations/probes/ksel2_favard_jacobi_probe.py) | — | — | — |
| [`probes/ksel2id_friedrichs_selection_probe.py`](../../computations/probes/ksel2id_friedrichs_selection_probe.py) | — | — | — |
| [`probes/ksel2id_sw_identification_probe.py`](../../computations/probes/ksel2id_sw_identification_probe.py) | — | — | — |
| [`probes/ksel2id_u1_promotion_probe.py`](../../computations/probes/ksel2id_u1_promotion_probe.py) | — | — | — |
| [`probes/ksel3_modular_double_probe.py`](../../computations/probes/ksel3_modular_double_probe.py) | — | — | — |
| [`probes/qbeta_habiro_integrality_kill_test.py`](../../computations/probes/qbeta_habiro_integrality_kill_test.py) | `ambiguous` | — | — |
| [`probes/qborel_confluence_pos_probe.py`](../../computations/probes/qborel_confluence_pos_probe.py) | — | — | — |
| [`probes/r2core_schwinger_measure_explore_probe.py`](../../computations/probes/r2core_schwinger_measure_explore_probe.py) | — | — | — |
| [`probes/rep_jackson_identification_probe.py`](../../computations/probes/rep_jackson_identification_probe.py) | — | — | — |
| [`probes/rep_tightness_probe.py`](../../computations/probes/rep_tightness_probe.py) | — | — | — |
| [`qbeta/qbeta_barodd_d_ladder_ord17_probe.py`](../../computations/qbeta/qbeta_barodd_d_ladder_ord17_probe.py) | — | — | — |
| [`qbeta/qbeta_c3_barodd_determined_solve_probe.py`](../../computations/qbeta/qbeta_c3_barodd_determined_solve_probe.py) | — | — | — |
| [`regenerate_y_lambda_mpfr.py`](../../computations/regenerate_y_lambda_mpfr.py) | — | — | — |

The `ksel*` / `rep_*` / `qborel` / `r2core` / `borel_propertime` cluster (10
probes) share one authored idiom and are clean. **Do not "migrate" any of
these** — removing the muon leg destroys the comparison the probe exists to
make.

---

## 6. `A` — infrastructure, and the exemplar to copy (4)

| producer | manifest tag | witness `q0Anchor` | pin fields co-read |
|---|---|---|---|
| [`_li_2_q_util.py`](../../computations/_li_2_q_util.py) | — | — | — |
| [`probes/qbeta_habiro_residual_probe.py`](../../computations/probes/qbeta_habiro_residual_probe.py) | — | `proton` | `physical_anchoring_bound` |
| [`probes/test_qbeta_habiro_anchor_guard.py`](../../computations/probes/test_qbeta_habiro_anchor_guard.py) | — | — | — |
| [`substrate/q_parameter.py`](../../computations/substrate/q_parameter.py) | — | — | — |

`substrate/q_parameter.py` **defines** the muon override;
`_li_2_q_util.py` implements `load_q_50dps(anchor=…)`;
`probes/test_qbeta_habiro_anchor_guard.py` must construct a straddle in order
to test that the guard fires on it.

**[`probes/qbeta_habiro_residual_probe.py`](../../computations/probes/qbeta_habiro_residual_probe.py)
is the pattern every `E` producer should be moved to.** It was in this
population and has already been fixed, and the fix keeps both reads with
distinct jobs:

```python
qpin = record_upstream(COMP / "q-pinning-50-digit.witness.json", _UPSTREAM_RECORDS)
from q_parameter import Q_50_DIGIT_STR as _Q50_PROTON   # <- the q0 that is USED
_assert_anchor_matches_value(qpin)                      # <- the pin, as a GUARD only
```

Its own comment records the reasoning verbatim: *"`derived_50_digit.q` out of
the pin witness … is the MUON value — q-pinning-50-digit is an `ideal_muon`
producer."* Reading the pin witness is not the defect; **binding `q₀` to it**
is.

---

## 7. `E` — should be proton (18)

Untagged, so `q_parameter` resolves **proton** at runtime and every emitted
witness will be stamped proton once the sibling's fix lands — while the
payload is muon. Each produces a Physical-Observations quantity (emits or
compares MeV / ppb / AME / CODATA / PDG values, or imports `codata_constants`).

| producer | manifest tag | witness `q0Anchor` | pin fields co-read |
|---|---|---|---|
| [`audit_delta_S_chain.py`](../../computations/audit_delta_S_chain.py) | — | — | — |
| [`c_k_beta_decay_witness.py`](../../computations/c_k_beta_decay_witness.py) | — | `muon` | — |
| [`cross_check_trM_cw_seminormal_leg.py`](../../computations/cross_check_trM_cw_seminormal_leg.py) | — | `muon` | — |
| [`derive_m_baryon_volume_form.py`](../../computations/derive_m_baryon_volume_form.py) | — | `muon` | — |
| [`derive_m_e_hecke_path_a.py`](../../computations/derive_m_e_hecke_path_a.py) | — | `muon` | — |
| [`derived_masses.py`](../../computations/derived_masses.py) | — | — | — |
| [`h4_habiro_closure.py`](../../computations/h4_habiro_closure.py) | — | — | — |
| [`hydrogen_qshuffle_compound.py`](../../computations/hydrogen_qshuffle_compound.py) | — | — | — |
| [`lambda_scale_derivation_probes_123.py`](../../computations/lambda_scale_derivation_probes_123.py) | — | — | — |
| [`mass-from-q-symbolic.py`](../../computations/mass-from-q-symbolic.py) | — | — | — |
| [`mass_sweep_bar_sym_h2_coefficient_hunt.py`](../../computations/mass_sweep_bar_sym_h2_coefficient_hunt.py) | — | — | — |
| [`q_beta_spectral_bridge_witness.py`](../../computations/q_beta_spectral_bridge_witness.py) | — | `muon` | — |
| [`qbeta/qbeta_ck_sseries_operator_match_probe.py`](../../computations/qbeta/qbeta_ck_sseries_operator_match_probe.py) | — | — | — |
| [`qbeta/qbeta_physics.py`](../../computations/qbeta/qbeta_physics.py) | — | — | — |
| [`qbeta/qbeta_symbolic_tbeta_min_l2.py`](../../computations/qbeta/qbeta_symbolic_tbeta_min_l2.py) | — | — | — |
| [`qbeta_habiro_probe.py`](../../computations/qbeta_habiro_probe.py) | — | — | — |
| [`qbeta_habiro_sweep.py`](../../computations/qbeta_habiro_sweep.py) | — | — | — |
| [`run_jones_markov_atlas_all_atoms.py`](../../computations/run_jones_markov_atlas_all_atoms.py) | — | — | — |

### 7.1 `derived_masses.py` carries a false all-clear — measured

This one is worth separating from the list, because its docstring is the
reason its muon read looks harmless. Before this branch, `_q_0()` was
documented as pulling the canonical CAL-2 `q₀` from the pin witness, with
`q_parameter.Q_50_DIGIT_STR` described as a *"legacy float64 fallback"* that
is *"identical to ~50 digits"*.

Both clauses are wrong, and measured:

```
pin  (muon) : 1.1099785955573347198997632204…
q_parameter : 1.1099785827513808075916690956…
first differing digit: index 9
relative separation:  -1.1537118e-8  =  -11.5371 ppb
```

They agree to **9** digits, not ~50 — the separation *is* the μ–p substrate
tension. And `q_parameter.Q_50_DIGIT_STR` is not a "legacy float64 fallback":
it is the **experimental (proton) pin**, the standing default for all
production code since 2026-08-07.

`derived_masses.py` is a production module — its own docstring says it
*"predicts both **MASS** observables (m_p, m_n, m_e via β-decay scale) and
**BINDING**-derived quantities"*. A false statement of equivalence sitting on
the accessor is exactly what stops a later agent from investigating, so the
docstring is corrected on this branch (no number moves).

### 7.2 One structural obstacle in this bucket

`derive_m_baryon_volume_form.py` already mixes layers *inside one quantity*:
it takes `q₀` from the muon pin (line 89) and `MASS_RATIO_MU_E_STR` from the
`q_parameter` registry (line 127). That is a rule-4 straddle today,
independent of any stamp.

---

## 8. `F` — hygiene (39)

Untagged structural / exploratory probes. The directive puts them on proton,
but 11.54 ppb cannot move any conclusion they state (they test structure —
exact rationality, singularity location, series matching, LP/SDP support — not
a number against an experimental one). **Batch these with the `qou-1c4y`
sweep; they are not worth a per-file review**, and several are long-computes.

| producer | manifest tag | witness `q0Anchor` | pin fields co-read |
|---|---|---|---|
| [`aK_via_lp_dual.py`](../../computations/aK_via_lp_dual.py) | — | `muon` | — |
| [`aK_via_lp_dual_full.py`](../../computations/aK_via_lp_dual_full.py) | — | `muon` | — |
| [`aK_via_lp_dual_hecke_basis.py`](../../computations/aK_via_lp_dual_hecke_basis.py) | — | `muon` | — |
| [`bring_2loop_weight3_coefficient_probe.py`](../../computations/bring_2loop_weight3_coefficient_probe.py) | — | — | — |
| [`bring_b3_closed_form_attempt.py`](../../computations/bring_b3_closed_form_attempt.py) | — | — | — |
| [`bring_d3_goncharov_probe.py`](../../computations/bring_d3_goncharov_probe.py) | — | — | — |
| [`bring_mapping_torus_residue_weight_probe.py`](../../computations/bring_mapping_torus_residue_weight_probe.py) | — | — | — |
| [`chi_lambda_multi_block_first_measurement.py`](../../computations/chi_lambda_multi_block_first_measurement.py) | — | — | — |
| [`deltalambda/he4_binding_k_presentation_correction_probe.py`](../../computations/deltalambda/he4_binding_k_presentation_correction_probe.py) | — | `muon` | — |
| [`deltalambda/he4_binding_k_stage2_probe.py`](../../computations/deltalambda/he4_binding_k_stage2_probe.py) | — | — | — |
| [`gram_matrix_seminormal_n.py`](../../computations/gram_matrix_seminormal_n.py) | — | — | — |
| [`habiro_borromean_cyclotomic_coefficients.py`](../../computations/habiro_borromean_cyclotomic_coefficients.py) | — | — | — |
| [`nuclide_braid_pipeline.py`](../../computations/nuclide_braid_pipeline.py) | — | — | `hbar_q` |
| [`probe_inter_knot_decoupling.py`](../../computations/probe_inter_knot_decoupling.py) | — | — | — |
| [`probes/fvk_selection_probe.py`](../../computations/probes/fvk_selection_probe.py) | — | — | — |
| [`probes/khovanov_at_q0_probe.py`](../../computations/probes/khovanov_at_q0_probe.py) | — | — | — |
| [`probes/lr_hecke_character_probe.py`](../../computations/probes/lr_hecke_character_probe.py) | — | — | — |
| [`probes/qbeta_c3_per_block_categorical_probe.py`](../../computations/probes/qbeta_c3_per_block_categorical_probe.py) | — | — | — |
| [`probes/qbeta_operator_identification_probe.py`](../../computations/probes/qbeta_operator_identification_probe.py) | — | — | — |
| [`pyhecke_jones_markov_atlas.py`](../../computations/pyhecke_jones_markov_atlas.py) | — | — | — |
| [`pyhecke_n_generic.py`](../../computations/pyhecke_n_generic.py) | — | — | — |
| [`qbeta/qbeta_bar_split_ord17_probe.py`](../../computations/qbeta/qbeta_bar_split_ord17_probe.py) | — | — | — |
| [`qbeta/qbeta_ck_sseries_exact_rational.py`](../../computations/qbeta/qbeta_ck_sseries_exact_rational.py) | — | — | — |
| [`qbeta/qbeta_dladder_barodd_borel_pade_laplace_probe.py`](../../computations/qbeta/qbeta_dladder_barodd_borel_pade_laplace_probe.py) | — | `muon` | — |
| [`qbeta/qbeta_dladder_ecalle_acceleration_probe.py`](../../computations/qbeta/qbeta_dladder_ecalle_acceleration_probe.py) | — | `muon` | — |
| [`qbeta/qbeta_dladder_generating_function_structure_probe.py`](../../computations/qbeta/qbeta_dladder_generating_function_structure_probe.py) | — | — | — |
| [`qbeta/qbeta_eta_singularity_probe.py`](../../computations/qbeta/qbeta_eta_singularity_probe.py) | — | — | — |
| [`qbeta/qbeta_eta_square_fibre_probe.py`](../../computations/qbeta/qbeta_eta_square_fibre_probe.py) | — | — | — |
| [`qbeta/qbeta_eta_square_functional_g_probe.py`](../../computations/qbeta/qbeta_eta_square_functional_g_probe.py) | — | — | — |
| [`qbeta/qbeta_even_channel_bar_split_probe.py`](../../computations/qbeta/qbeta_even_channel_bar_split_probe.py) | — | — | — |
| [`qbeta/qbeta_markov_trace_norm_probe.py`](../../computations/qbeta/qbeta_markov_trace_norm_probe.py) | — | — | — |
| [`qbeta/qbeta_markov_trace_steps_4_5.py`](../../computations/qbeta/qbeta_markov_trace_steps_4_5.py) | — | — | — |
| [`qbeta/qbeta_per_block_paper_closed_forms.py`](../../computations/qbeta/qbeta_per_block_paper_closed_forms.py) | — | — | — |
| [`qbeta/qbeta_per_block_symbolic.py`](../../computations/qbeta/qbeta_per_block_symbolic.py) | — | — | — |
| [`qbeta/qbeta_trm_crosscheck_convention_pin_split_probe.py`](../../computations/qbeta/qbeta_trm_crosscheck_convention_pin_split_probe.py) | — | `muon` | — |
| [`qbeta/qbeta_zeta4_eta_descent_probe.py`](../../computations/qbeta/qbeta_zeta4_eta_descent_probe.py) | — | — | — |
| [`qbeta/qbeta_zeta4_faithful_odd_probe.py`](../../computations/qbeta/qbeta_zeta4_faithful_odd_probe.py) | — | — | — |
| [`substrate/frakV_askey_wilson_recurrence_tie_probe.py`](../../computations/substrate/frakV_askey_wilson_recurrence_tie_probe.py) | — | — | — |
| [`yekutieli_borromean_h2_extraction.py`](../../computations/yekutieli_borromean_h2_extraction.py) | — | — | — |

`nuclide_braid_pipeline.py` co-reads `hbar_q` from the pin witness, so it
cannot be re-pointed by its `["q"]` read alone.

---

## 9. What was and was not done here

**Deliberately not swept.** The C→D precedent (`qou-2zjp`) shows a
convention-wide move reaching 14.741 %; routing 57 producers (`E` + `F`)
through `q_parameter` in one commit would move numbers in 57 places with no
per-file review. That is `qou-1c4y`, gated on the recorded 2026-08-19 owner
authorisation and its four constraints.

**Machine-readable ledger:**
[`2026-08-24-mech5-producer-layer-triage.json`](2026-08-24-mech5-producer-layer-triage.json)
— all 95 with bucket, rationale, manifest tag, witness stamps, co-read fields,
and which of the two detectors saw each.

**Not measured here:** whether each `E` producer's numbers actually move by
the full 11.54 ppb, or by less because the quantity is insensitive. Deciding
that needs a per-producer re-run, which is the sweep this document exists to
scope rather than to perform.
