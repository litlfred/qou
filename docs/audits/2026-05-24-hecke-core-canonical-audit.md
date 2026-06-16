# `hecke_core.py` canonical vs exploratory audit

**Date.** 2026-05-24
**Branch.** `claude/hecke-core-audit-2026-05-24` (based on `origin/main` @ `d128bdee`)
**Target file.** [`computations/substrate/hecke_core.py`](../../computations/substrate/hecke_core.py) (3 183 LOC, 72 top-level `def`/`class`, 52 importers)
**Prereq for.** pyhecke 1.0 hardening (workplan §3.5 — split canonical surface from Phase-5 probes before promoting the canonical surface into `pyhecke`).
**Companion docs.**

- [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) — the canonical 11-step chain that defines the CANONICAL classification.
- [`docs/pyhecke-optimization-workplan.md`](../pyhecke-optimization-workplan.md) §B1 — flags `hecke_core` cold-import (42 s) as the highest-ROI cleanup; the canonical/exploratory split is the structural prerequisite.

---

## 1. Methodology

For every top-level `def` / `class` / module-level cached constant in
[`hecke_core.py`](../../computations/substrate/hecke_core.py),
classification was derived from three signals:

1. **Cheat-sheet match.** Does the symbol appear in the canonical chain
   ([cheat-sheet §2 table](../canonical-derivation-cheat-sheet.md)) as the
   canonical compute script for a step?  Direct hits (`build_atom_nf`,
   `_PROTON_G0/G1`, `_NEUTRON_G0/G1`, `q_factorial`, `q_hook_product`,
   `partition_dimension`, `q_dimension`, `wedderburn_weight`,
   `partitions_of`, `partition_conjugate`, `partition_is_self_conjugate`)
   are the canonical seed set the workplan called out.
2. **Importer scan.** Grepped all 52 importers under
   `computations/` for each symbol.  A symbol consumed
   by a canonical script (`mass_table_ppb.py`,
   `mass_formula_6term_mpfr_50dps.py`, `binding_canonical.py`,
   `m_p_borromean_verification_50dps.py`, `closed_form_tau_M.py`,
   `mass_at_3A_proper.py`, `pn_alpha_lp_dual.py`, etc.) inherits the
   CANONICAL tag; one only consumed by `alpha_blend_tower.py`,
   `rho_k_h3a_gg_trajectory.py`, or test/probe scripts is treated as
   EXPLORATORY.
3. **Adjacent-comment scan.** Read the docstring + the comment block
   directly above each symbol.  `[DEPRECATED ...]`, `LEGACY`,
   `replaces ad-hoc`, `WARNING`, `NO well-defined ...`, `coincidence,
   not identity`, etc. were treated as strong demotion signals;
   `prop:...`, `Reference: ...`, `canonical`, `core` as promotion
   signals.

For utility helpers (private `_underscore` functions), classification
follows the **highest-tier caller in the same file** — a private helper
called only from EXPLORATORY functions is itself EXPLORATORY.

**`chi_lambda_braid` clarification (per starting allowlist).**  The
cheat-sheet step 6 cites `chi_lambda_braid`, but a grep confirms it
lives in `computations/hecke/hecke_characters.py:280`, not
in `hecke_core.py`.  No row is added here for it — out of scope for
this audit.

---

## 2. Classification table

The table below has 73 rows total: 72 top-level `def` / `class`
declarations (matching
`grep -cE '^(class |def )' computations/substrate/hecke_core.py`)
plus 1 inline tuple-assignment (row #28, `_PROTON_G0/G1`,
`_NEUTRON_G0/G1`, emitted at module load by `nucleon_gen_chains`).
A supplementary table at §C below covers 8 more module-level cached
objects whose classification deserves its own line (the α-EM
derivation block, the partition table cache, the Chebyshev magic
cache, the ID NF vector, the categorical-shell cache, the
YSN-attached flag, the precomputed nucleon NFs, and the E_0
calibration constant). Non-callable scalar constants (`q2`,
`K_PARTITION_MAX`, `K_GAUSSIAN_MAX`, `E_HARTREE_EV`, `E_MOL`,
`KAPPA`, `TWO_Q`, `S_REEB_PLANCK`, `H_Q_22`, `DELTA_22`, `FIG8_*`,
`ALPHA_*`, `V_HAT_ELECTRON`, `MAGIC_NUMBERS`, `NOBLE_GAS_Z`, the
four α-EM CS scratch variables, the `_M22_*` matrices) are not
listed individually but their canonical/exploratory status is
captured by the function that consumes them.

**Cross-reference convention.** Rationale entries below cite other
symbols by name (e.g. "feeds `unified_iterative_correction_jet`")
rather than by row number — the row-number indirection drifted
once during drafting, and the name is stable across reorderings.

| # | Function / class | Line | Classification | Rationale |
|---|---|---|---|---|
| 1 | `classify_nuclear_knot` | 195 | **EXPLORATORY** | Pre-Phase-5 knot-classification table (trivial / satellite / figure-8 / Borromean → `ALPHA_*`). Only consumer is `classify_nuclear_knot` itself (no importer calls it); superseded by `mass_at_3A_proper.atom_braid_word_3A` per cheat-sheet §7. |
| 2 | `q_hook_product` | 222 | **CANONICAL** | Cheat-sheet step 5 (Wedderburn): seed allowlist. Consumed by `mass_formula_6term_mpfr_50dps`, `mass_at_3A_proper`, `proton_residual_rootcause`, `paper_six_term_isotope_sweep`, `sdp_cross_channel`. |
| 3 | `q_factorial` | 246 | **CANONICAL** | Seed allowlist; the [n]_q! denominator in Wedderburn weights. Used internally by `q_dimension`, `wedderburn_weight`, `lp_shadow_price`. |
| 4 | `partitions_of` | 254 | **CANONICAL** | Seed allowlist; partition enumerator for cheat-sheet step 5. Imported by `sdp_cross_channel`, `paper_six_term_isotope_sweep`. |
| 5 | `partition_dimension` | 269 | **CANONICAL** | Seed allowlist; classical dim d(λ). Imported by `sdp_cross_channel`, `mass_at_3A_proper`. |
| 6 | `partition_conjugate` | 288 | **CANONICAL** | Seed allowlist; consumed by SDP cross-channel pair detection (line 2556 in this file + `sdp_cross_channel.py`). |
| 7 | `partition_is_self_conjugate` | 301 | **CANONICAL** | Seed allowlist; small structural helper, conjugation-symmetric. |
| 8 | `partition_jet_depth` | 305 | **EXPLORATORY** | Cheat-sheet §1 row I (Q_β refinement) — jet-prefix order is a canonical concept but this helper only feeds `unified_iterative_correction_jet`, itself EXPLORATORY. No canonical caller. |
| 9 | `q_dimension` | 333 | **CANONICAL** | Seed allowlist; the d_q(λ) entering w_λ. |
| 10 | `wedderburn_weight` | 341 | **CANONICAL** | Seed allowlist; w_λ = d_q(λ)²/[n]_q!. Imported by `proton_residual_rootcause`, `paper_six_term_isotope_sweep`. |
| 11 | `q_laplacian_eigenvalue` | 349 | **EXPLORATORY** | Phase-5 q-heat-kernel probe (μ_λ via JM Casimir). Cited from `prop:q-heat-kernel-peter-weyl` but the substrate Wedderburn / Markov-trace chain in the cheat-sheet does NOT route through Laplacian eigenvalues; this is the "resolvent-damped" alternative ansatz consumed by `unified_iterative_correction`. |
| 12 | `q_resolvent_weight` | 392 | **EXPLORATORY** | Consumes #11; "categorical Laplace transform" of the q-Laplacian. Replacement for the "ad-hoc Kerov Plancherel multiplier" — *another* Phase-5 ansatz, not a cheat-sheet step. |
| 13 | `lp_shadow_price` | 420 | **EXPLORATORY** | "LP-dual shadow price" — note CLAUDE.md `## LP / SDP duals` mandates the canonical LP entry is [`lp_dual_solver.py`](../../computations/lp_dual_solver.py) (`solve_operator_selection_lp`), NOT this file. This is an internal per-partition shadow used by `unified_iterative_correction`. No production importer. |
| 14 | `_count_syts_by_12_relation` | 471 | UTILITY-of-`partition_character_sigma1` | Counts SYTs by (1,2)-relation; only consumed inside this file. The transitive parent `partition_character_sigma1` is EXPLORATORY (row 15), so this helper is UTILITY-of-EXPLORATORY. |
| 15 | `partition_character_sigma1` | 514 | **EXPLORATORY** | YSN-derived character of σ_1 in irrep λ. Only consumer is `partition_spectral_log_rate`; used in the q-Gaussian fallback (`_q_gaussian_character_approx`), explicitly tagged as a Perron-Frobenius approximation that is "not Bozejko-Speicher". |
| 16 | `partition_spectral_log_rate` | 525 | **EXPLORATORY** | Phase-5 spectral log-rate ρ_λ used only by the q-Gaussian fallback. |
| 17 | `_partition_table` | 563 | UTILITY-of-`_LazyPartitionTable` (used by `unified_iterative_correction`, `_contrib_single_partition`, `atom_markov_trace`, `atom_frobenius_norm_sq`, `sdp_cross_channel_contribution`, `unified_iterative_correction_jet` — all EXPLORATORY) | The "pre-computed partition table" with 20 000 partitions; ~30 s cold build. The exported `_PARTITION_TABLE` (line 646) is its lazy proxy. Imported externally only by `sdp_cross_channel:705`. |
| 18 | `_LazyPartitionTable` | 613 | UTILITY-of-`_partition_table` | Lazy proxy. |
| 19 | `_q_exp` | 658 | **EXPLORATORY** | q-exponential series, no caller in this file or anywhere else; dead code (grep yields zero hits in `computations/`). |
| 20 | `_chebyshev_magic` | 670 | **EXPLORATORY** | Cheat-sheet §1 magic-numbers note: "{2, 8, 20, 28, 50, 82, 126} are EMPIRICAL and not derived". This helper attempts a derivation from a Chebyshev recurrence in q; explicitly tagged as inadequate above `MAGIC_NUMBERS` (line 711-712: "These values are CODATA-class inputs, not canonical predictions"). Strong EXPLORATORY candidate per the workplan; confirmed. |
| 21 | `build_atom_nf_exact` | 727 | **CANONICAL** | Sibling of `build_atom_nf`: exact-Fraction version for verification (e.g. `pn_alpha_lp_dual.py`, `closed_form_tau_M_verification_phase5q.py`). Verified-precision path; canonical. |
| 22 | `nf_channel_exact` | 799 | UTILITY-of-`build_atom_nf_exact` | Exact-Fraction Wedderburn channel decomposition. Used by the same verification pipeline. |
| 23 | `knot_factor` | 819 | **EXPLORATORY** | Hard-coded `A=2/3/4` knot-classification factors with literal h-polynomial. Pre-Phase 5; superseded by [`closed_form_tau_M.py`](../../computations/closed_form_tau_M.py) (per cheat-sheet §5 closure #4). |
| 24 | `check_frobenius` | 845 | UTILITY (general) | Frobenius positivity check on NF vectors. Used by `molecular_binding_frobenius`; canonical Frobenius pairing infra. |
| 25 | `build_atom_nf` | 857 | **CANONICAL** | Seed allowlist; cheat-sheet step 4 (the canonical H_3 atomic-braid NF). Production consumers: `mass_at_3A_proper`, `binding_canonical`, etc. |
| 26 | `vertex_volume` | 939 | **CANONICAL** | Cheat-sheet step 6 — Wedderburn-weighted traced volume per generator. Sibling of `atom_per_generator_volumes`. |
| 27 | `nucleon_gen_chains` | 959 | **CANONICAL** | Builds the per-generator quark/gluon chains; produces `_PROTON_G0/G1` and `_NEUTRON_G0/G1` (line 997-998). Seed allowlist. |
| 28 | `_PROTON_G0/G1`, `_NEUTRON_G0/G1` | 997-998 | **CANONICAL** | Seed allowlist (cheat-sheet step 4 explicit). 6 external importers including `pn_alpha_lp_dual`, `alpha_blend_tower`, `mass_at_3A_proper`, `closed_form_tau_M_verification_phase5q`, `rho_k_h3a_gg_trajectory`, `braid_encoding_audit`, `alpha_high_precision`. |
| 29 | `atom_gen_chains` | 1001 | **CANONICAL** | Cheat-sheet step 4; combines `_PROTON_G*` / `_NEUTRON_G*` into the full atomic braid. Used by `vertex_volume` and `atom_per_generator_volumes`. |
| 30 | `atom_V_full` | 1061 | **CANONICAL** | Mass-tower formula entry (prop:mass-endomorphism-tower per docstring). |
| 31 | `_chain_V_full` | 1080 | UTILITY-of-`atom_V_full` | Wedderburn-weighted traced volume from a crossing chain. |
| 32 | `_crossing_coeff` | 1105 | UTILITY-of-`_phi1_from_ordering` (EXPLORATORY) | Crossing coefficient for strand pair, only used by Φ_1 family. |
| 33 | `_phi1_from_ordering` | 1116 | **EXPLORATORY** | Φ_1 = Σ ln\|V̂_i\| — strong EXPLORATORY candidate confirmed. Sole callers are `_phi1_nuclear` and `compute_phi1_full`, themselves EXPLORATORY. |
| 34 | `_alternating_ordering` | 1151 | UTILITY-of-`_phi1_nuclear`/`compute_phi1_full` (EXPLORATORY) | Ground-state seed used by the Φ_1 fallback. |
| 35 | `_phi1_nuclear` | 1169 | **EXPLORATORY** | Strong EXPLORATORY candidate confirmed. Sole canonical caller is `q_value_beta` (row 72), itself EXPLORATORY (deprecated by `qbeta_*.py`). |
| 36 | `compute_phi1_full` | 1223 | **EXPLORATORY** | Strong EXPLORATORY candidate confirmed. Pure Φ_1 transfer-matrix product; called only by `atom_mass` (row 73, EXPLORATORY). |
| 37 | `valence_Z` | 1276 | **CANONICAL** | Seed allowlist; small purely-structural helper (noble-gas valence count). Used by molecular-binding scripts (`molecular_binding_nf`). |
| 38 | `_vertex_channels` | 1290 | UTILITY-of-`molecular_binding_nf` | Per-irrep channel decomposition for the molecular binding pipeline. |
| 39 | `molecular_binding_nf` | 1308 | **CANONICAL** | Full Wedderburn decomposition for molecular binding; matches cheat-sheet step 6 pattern, just in the molecular (rather than nuclear) regime. Many importers (`h2-molecular-binding`, `hh-trefoil-corrected`, `h2-integer-lp`, `molecular-trefoil-scan`, `molecular-frobenius-lp`, `co2-molecular-binding`, etc.). |
| 40 | `molecular_binding_frobenius` | 1360 | **CANONICAL** | Sibling of #39; Frobenius bilinear-form variant. Same canonical role. |
| 41 | `_load_categorical_shell` | 1423 | **EXPLORATORY** | Chebyshev γ(Z) → "categorical shell" — adjacent to `_chebyshev_magic` and shares its non-canonical status. Only consumer is `magic_proximity`. |
| 42 | `magic_proximity` | 1452 | **EXPLORATORY** | Shell proximity from `_CATEGORICAL_SHELL` cache; no canonical consumer. |
| 43 | `_matmul2` | 1523 | UTILITY-of-`_chain_M22` (EXPLORATORY) | 2×2 matrix multiply. |
| 44 | `_crossing_M22` | 1529 | UTILITY-of-`_chain_M22` | (2,2)-rep crossing matrix. |
| 45 | `_chain_M22` | 1536 | **EXPLORATORY** | "(2,2) iterative correction" — explicitly the "replaces D + knot_factor + Wigner" experiment (line 1466-1468). Pre-Phase-5l, no caller outside this file. |
| 46 | `_step_chain_22` | 1553 | UTILITY-of-`_chain_M22` (EXPLORATORY) | (2,2)-specific step chain. |
| 47 | `_standard_tableaux` | 1601 | UTILITY-of-`_build_ysn_matrices` | SYT enumerator. Used externally by `sdp_cross_channel:475`. Itself canonical infra (SYT enumeration is part of Wedderburn step), but only consumed by EXPLORATORY code today; classify as UTILITY-of-`_build_ysn_matrices`. |
| 48 | `_content_at` | 1625 | UTILITY-of-`_build_ysn_matrices` | Tableau content lookup. |
| 49 | `_swap_tab` | 1634 | UTILITY-of-`_build_ysn_matrices` | Tableau swap. Used externally by `sdp_cross_channel:475`. |
| 50 | `_build_ysn_matrices` | 1657 | UTILITY-of-`unified_iterative_correction*` (EXPLORATORY) | Generic-partition YSN matrices. The canonical YSN path lives in `hecke_characters.chi_lambda_braid` (per cheat-sheet step 6). |
| 51 | `_matmul_dim` | 1757 | UTILITY-of-`_build_ysn_matrices`/`atom_character_raw` | dim×dim multiplication. |
| 52 | `_trace_dim` | 1772 | UTILITY-of-same as #51 | Trace helper. |
| 53 | `_identity` | 1778 | UTILITY-of-same as #51 | Identity-matrix helper. |
| 54 | `_crossing_in_partition` | 1785 | UTILITY-of-`atom_character_raw` (EXPLORATORY) | Generic-partition crossing matrix. Imported by `sdp_cross_channel:475`. |
| 55 | `_ensure_ysn_attached` | 1810 | UTILITY-of-`_LazyPartitionTable` | Lazy YSN attachment to partition entries. |
| 56 | `_step_chain_generic` | 1825 | UTILITY-of-`unified_iterative_correction*` and `atomic_chirality_residue` (line 45) | Generic-partition step chain. Has one external importer (`atomic_chirality_residue.py`) but that's a probe script. |
| 57 | `_q_gaussian_character_approx` | 1857 | **EXPLORATORY** | The docstring warns: "Bozejko-Speicher q-Gaussian does NOT apply here … Attempting to use Bozejko-Speicher at q₀ would conceptually misapply the framework." Phase-5 ad-hoc Perron-Frobenius approximation. |
| 58 | `unified_iterative_correction` | 1917 | **EXPLORATORY** | Whole-of-file flagship of the Phase-5 LP-dual approach; sums shadow prices y_λ across partition channels. Production consumer: `binding_energy` (row 70) only. Not on the cheat-sheet chain. |
| 59 | `_jet_witness_path` | 2237 | UTILITY-of-`unified_iterative_correction_jet` | Witness path helper. |
| 60 | `atom_character_raw` | 2243 | **EXPLORATORY** | Raw χ_λ via running YSN matrix product; superseded by `hecke_characters.chi_lambda_braid` (cheat-sheet step 6, plus the Rust kernel `pyhecke_native`). |
| 61 | `_contrib_single_partition` | 2311 | UTILITY-of-`unified_iterative_correction_jet` (EXPLORATORY) | Single-partition LP-dual contribution. |
| 62 | `conjugate_pair_cross_term` | 2393 | **EXPLORATORY** | Conjugate-pair cross-channel coupling — uses the same `_contrib_single_partition` (EXPLORATORY) infra; SDP path is the canonical pipeline (cheat-sheet step 10). |
| 63 | `unified_iterative_correction_jet` | 2467 | **EXPLORATORY** | Jet-filtered variant of #58. |
| 64 | `atom_markov_trace` | 2631 | **EXPLORATORY** | Docstring opens with: `"[DEPRECATED — Plancherel-weighted]"` (line 2632). Explicit redirection: `"Use markov_trace_canonical.tr_M_element for the canonical axiomatic Markov trace"`. No production consumers. |
| 65 | `atom_frobenius_norm_sq` | 2701 | **EXPLORATORY** | Companion to `atom_markov_trace`; same Plancherel-weighted construction. |
| 66 | `atom_per_generator_volumes` | 2756 | **CANONICAL** | Per-generator V̂_i^full for the mass-tower formula (prop:mass-endomorphism-tower); cheat-sheet step 9 (mass identity). Production importers: `mass_formula_6term_mpfr_50dps.py:71`, `brane_tower_isospin_diagnosis.py:162`, `mass_formula_6term.py:117`, `entanglement_orders.py:33`, `mass_table_no_fit.py:43` (deprecated), `catalan_binding.py:42`, `unified-mass-molecular.py`. |
| 67 | `free_nucleon_frobenius_norm_sq` | 2896 | **EXPLORATORY** | Single-line wrapper around `atom_frobenius_norm_sq`; docstring acknowledges it's an "empirical simpler form" with TODO for proper decomposition. |
| 68 | `binding_from_frobenius_pairing` | 2941 | **EXPLORATORY** | Comment in body: `"Legacy Plancherel path (default)"` (line 2991-2992). Marked as fallback when `canonical=True` fails. Cheat-sheet step 9 canonical path is `binding_canonical.binding_canonical` (per the docstring's own redirection at line 2643). |
| 69 | `sdp_cross_channel_contribution` | 2997 | **EXPLORATORY** | Phase-5 cross-channel SDP probe via `sdp_cross_channel.sdp_with_atom_observables`. Canonical SDP entry is `lp_dual_solver.solve_psd_operator_selection_sdp` (per CLAUDE.md `## LP / SDP duals`). |
| 70 | `binding_energy` | 3087 | **EXPLORATORY** | "Replaces the retired 11-term Bethe-Weizsäcker formula path" — sums `unified_iterative_correction` + `sdp_cross_channel_contribution` + `binding_from_frobenius_pairing`, all EXPLORATORY. Despite the canonical-sounding name, this is the Phase-5 unified aggregate, not on the cheat-sheet chain. Canonical binding entry is `binding_canonical.binding_canonical` or `mass_formula_6term_mpfr_50dps.py`. |
| 71 | `build_nucleon_nf` | 3108 | **CANONICAL** | Builds the per-nucleon H_3 NF; consumed by `_PROTON_NF` / `_NEUTRON_NF` at lines 3145-3146. Cheat-sheet step 4. |
| 72 | `q_value_beta` | 3149 | **EXPLORATORY** | Uses `_phi1_nuclear` (EXPLORATORY) — superseded by `free-neutron-decay.py` + `qbeta_*.py` (cheat-sheet step 11). |
| 73 | `atom_mass` | 3171 | **EXPLORATORY** | "M = Z·m_p + N·m_n + Z·m_e + κ·Φ₁" — uses `compute_phi1_full` (EXPLORATORY). Pre-canonical mass formula; superseded by `mass_table_ppb.py` / `mass_formula_6term_mpfr_50dps.py` (cheat-sheet step 9). |

**Plus eight cached module-level objects with classification follow-on:**

| # | Symbol | Line | Classification | Rationale |
|---|---|---|---|---|
| C1 | α_EM derivation block (`_bare_alpha_*`, `_CS_*`, `_kappa_gram`, `ALPHA_EM_INV_DERIVED`, `alpha_em`) | 63-126 | **CANONICAL** | `alpha_em` is consumed by 7 molecular-binding scripts (`h2-*`, `hh-*`, `molecular-*`, `unified-mass-molecular.py`, `h2-integer-lp`, `co2-molecular-binding`, `shell-aware-halflife`). Derivation chain prop:alpha-em-shift-multiplicative-chain. |
| C2 | `_PARTITION_TABLE` cache | 646 | UTILITY-of-EXPLORATORY consumers | See #17. |
| C3 | `_CHEBYSHEV_MAGIC` cache | 706 | **EXPLORATORY** | See #20. |
| C4 | `_ID_NF` | 724 | **CANONICAL** | Identity NF vector — trivial structural constant; canonical. |
| C5 | `_CATEGORICAL_SHELL` cache | 1449 | **EXPLORATORY** | See #41. |
| C6 | `_YSN_ATTACHED` flag | 1807 | UTILITY-of-`_LazyPartitionTable` | Idempotency flag. |
| C7 | `PROTON_NF`, `NEUTRON_NF` | 3145-3146 | **CANONICAL** | Per-nucleon NF caches consumed by canonical scripts. |
| C8 | `E_0_CALIBRATION_MEV` | 2932 | **CANONICAL** | The single calibration constant E_0 per prop:categorical-mass-markov (cheat-sheet 3-input rule); imported by `adjacent_vs_full_probe.py` and many others. |

---

## 3. Counts summary

Counting only the 72 top-level `def`/`class` rows (row #28 in §2 is
an inline tuple-assignment, not a `def`, so the tally is 72):

- **CANONICAL** : **19** — `q_hook_product`, `q_factorial`,
  `partitions_of`, `partition_dimension`, `partition_conjugate`,
  `partition_is_self_conjugate`, `q_dimension`, `wedderburn_weight`,
  `build_atom_nf_exact`, `build_atom_nf`, `vertex_volume`,
  `nucleon_gen_chains`, `atom_gen_chains`, `atom_V_full`, `valence_Z`,
  `molecular_binding_nf`, `molecular_binding_frobenius`,
  `atom_per_generator_volumes`, `build_nucleon_nf`.
- **EXPLORATORY** : **29** — `classify_nuclear_knot`,
  `partition_jet_depth`, `q_laplacian_eigenvalue`,
  `q_resolvent_weight`, `lp_shadow_price`,
  `partition_character_sigma1`, `partition_spectral_log_rate`,
  `_q_exp`, `_chebyshev_magic`, `knot_factor`,
  `_phi1_from_ordering`, `_phi1_nuclear`, `compute_phi1_full`,
  `_load_categorical_shell`, `magic_proximity`, `_chain_M22`,
  `_q_gaussian_character_approx`, `unified_iterative_correction`,
  `atom_character_raw`, `conjugate_pair_cross_term`,
  `unified_iterative_correction_jet`, `atom_markov_trace`,
  `atom_frobenius_norm_sq`, `free_nucleon_frobenius_norm_sq`,
  `binding_from_frobenius_pairing`,
  `sdp_cross_channel_contribution`, `binding_energy`, `q_value_beta`,
  `atom_mass`.
- **UTILITY** : 72 − 19 − 29 = **24** (private `_underscore` helpers
  classified UTILITY-of-X in §2; see rows #14, #17, #18, #22, #24,
  #31-34, #38, #43, #44, #46-56, #59, #61).

The 1 inline-tuple row (#28: `_PROTON_G0/G1`, `_NEUTRON_G0/G1`) and
the 8 cached module-level objects in the §C table are classified
separately and not counted toward the 72-`def`/`class` tally above.

**Total = 19 + 29 + 24 = 72**, matching
`grep -cE "^(class |def )" computations/substrate/hecke_core.py` = 72.
Sanity-check passes.

The strong-exploratory candidates the workplan flagged (`_chebyshev_magic`,
`_phi1_full`/`_phi1_from_ordering`, `compute_phi1_full`, `_phi1_nuclear`,
`_alternating_ordering`, `_count_syts_by_12_relation`,
`partition_jet_depth`, `q_laplacian_eigenvalue`, `q_resolvent_weight`,
`partition_spectral_log_rate`, `lp_shadow_price`) all confirmed
EXPLORATORY or UTILITY-of-EXPLORATORY.

---

## 4. Recommended split

Move the following 29 top-level symbols (and the 4 caches / private
helpers that serve only them) into a new sibling file
`computations/_deprecated/hecke_core_legacy.py`.  The
surviving `hecke_core.py` keeps the 19 CANONICAL functions plus the
24 utilities they need.

### 4a. Symbols to move into `_deprecated/hecke_core_legacy.py`

**EXPLORATORY (29):**

```
classify_nuclear_knot              # line 195
partition_jet_depth                # line 305
q_laplacian_eigenvalue             # line 349
q_resolvent_weight                 # line 392
lp_shadow_price                    # line 420
_count_syts_by_12_relation         # line 471
partition_character_sigma1         # line 514
partition_spectral_log_rate        # line 525
_q_exp                             # line 658
_chebyshev_magic                   # line 670   (+ _CHEBYSHEV_MAGIC cache + MAGIC_NUMBERS)
knot_factor                        # line 819
_crossing_coeff                    # line 1105  (UTILITY-of-Φ_1)
_phi1_from_ordering                # line 1116
_alternating_ordering              # line 1151  (UTILITY-of-Φ_1)
_phi1_nuclear                      # line 1169
compute_phi1_full                  # line 1223
_load_categorical_shell            # line 1423  (+ _CATEGORICAL_SHELL cache)
magic_proximity                    # line 1452
_matmul2                           # line 1523  (UTILITY-of-(2,2))
_crossing_M22                      # line 1529  (UTILITY-of-(2,2))
_chain_M22                         # line 1536
_step_chain_22                     # line 1553  (UTILITY-of-(2,2))
_q_gaussian_character_approx       # line 1857
unified_iterative_correction       # line 1917
_jet_witness_path                  # line 2237
atom_character_raw                 # line 2243
_contrib_single_partition          # line 2311
conjugate_pair_cross_term          # line 2393
unified_iterative_correction_jet   # line 2467
atom_markov_trace                  # line 2631
atom_frobenius_norm_sq             # line 2701
free_nucleon_frobenius_norm_sq     # line 2896
binding_from_frobenius_pairing     # line 2941
sdp_cross_channel_contribution     # line 2997
binding_energy                     # line 3087
q_value_beta                       # line 3149
atom_mass                          # line 3171
```

**Plus their UTILITY support** (move with their parents — they are
useless on the canonical side):

```
_standard_tableaux                 # line 1601  (UTILITY only-of EXPLORATORY consumers)
_content_at                        # line 1625
_swap_tab                          # line 1634
_build_ysn_matrices                # line 1657
_matmul_dim                        # line 1757
_trace_dim                         # line 1772
_identity                          # line 1778
_crossing_in_partition             # line 1785
_ensure_ysn_attached               # line 1810  (+ _YSN_ATTACHED flag)
_step_chain_generic                # line 1825
_partition_table                   # line 563   (+ _LazyPartitionTable + _PARTITION_TABLE + _PARTITION_TABLE_CACHE)
                                   # NOTE: kept under _deprecated because every consumer is EXPLORATORY,
                                   # but a few external scripts (sdp_cross_channel:475, :637, :705;
                                   # atomic_chirality_residue:45) currently import it directly.
                                   # Migration: those importers should switch to importing from
                                   # _deprecated/hecke_core_legacy.py (or be migrated to
                                   # hecke_characters/chi_lambda_braid).
```

### 4b. Imports the `_deprecated` file would need

Top-of-file imports for `hecke_core_legacy.py` (consolidated):

- **stdlib**: `math`, `json`, `os`, `pathlib.Path`, `fractions.Fraction`.
- **3rd-party**: `numpy as np`; `scipy.sparse` (lazy inside functions,
  already the pattern in the current file).
- **`q_parameter`**: `Q as q0`, `Q_INV as qi`, `HA as h`, `q_int`,
  `E_CROSS`.
- **`experimental_constants`**: `M_E_MEV`, `M_P_MEV`, `M_N_MEV`,
  `Q_NEUTRON_MEV`, `Q_NEUTRON_MEV_ERR`.
- **`pyhecke.gram`**: `z`, `W_SYM`, `W_STD`, `W_ALT`, `NF_BASIS`,
  `NF_NAMES`, `TR_M`, `INV_TREFOIL_G0/G1`, `hm`, `hm_exact`, `nf_tr`,
  `nf_net`, `G`, `G_INV`, plus the `_*_FRAC` exact-rational constants.
- **`knot_volumes`** (only because `classify_nuclear_knot` ships
  ALPHA_BORROMEAN / ALPHA_FIGURE8 / VOL_FIGURE8): `CATALAN_G`,
  `VOL_BORROMEAN`, `VOL_4_1 as VOL_FIGURE8`.
- **Re-imports from the surviving `hecke_core`** (to keep
  EXPLORATORY code working while the migration lands): the 19
  CANONICAL functions + `_PROTON_G0/G1`, `_NEUTRON_G0/G1`,
  `K_PARTITION_MAX`, `K_GAUSSIAN_MAX`, `S_REEB_PLANCK`, `H_Q_22`,
  `DELTA_22`, `W_22`, `D_Q_22`, `Y_22`, `E_0_CALIBRATION_MEV` (+
  `_ERR`).

### 4c. Estimated surviving `hecke_core.py` size

Counting the line spans of CANONICAL functions + the structural
imports / α-EM block / cached constants they need:

- α-EM derivation block (63-126): ~64 lines
- FIG8_*, ALPHA_*, V_HAT_ELECTRON, classify_nuclear_knot **stays-or-moves** decision: `classify_nuclear_knot` moves; the `FIG8_*` / `ALPHA_BORROMEAN` / `ALPHA_FIGURE8` / `V_HAT_ELECTRON` constants are only consumed by `classify_nuclear_knot`, so they move too. Frees ~50 lines.
- `q_hook_product` (222-243), `q_factorial` (246-251), `partitions_of` (254-266), `partition_dimension` (269-285), `partition_conjugate` (288-298), `partition_is_self_conjugate` (301-302), `q_dimension` (333-338), `wedderburn_weight` (341-346): ~50 lines.
- `valence_Z` (1276-1287): ~12 lines.
- `nucleon_gen_chains` (959-993) + `_PROTON_G0/G1`, `_NEUTRON_G0/G1` (997-998): ~37 lines.
- `build_atom_nf` (857-932) + `build_atom_nf_exact` (727-796) + `nf_channel_exact` (799-816): ~190 lines.
- `vertex_volume` (939-956) + `atom_gen_chains` (1001-1058) + `atom_V_full` (1061-1077) + `_chain_V_full` (1080-1102): ~150 lines.
- `_vertex_channels` (1290-1305) + `molecular_binding_nf` (1308-1357) + `molecular_binding_frobenius` (1360-1406) + `check_frobenius` (845-850): ~115 lines.
- `atom_per_generator_volumes` (2756-2893): ~138 lines.
- `build_nucleon_nf` (3108-3141) + `PROTON_NF` / `NEUTRON_NF` (3145-3146): ~36 lines.
- `_ID_NF` (724): ~1 line.
- `E_0_CALIBRATION_MEV` block (2922-2938): ~17 lines.
- Imports + docstring + section headers: ~80 lines.

**Estimated surviving file** ≈ **900-950 LOC** (down from 3 183),
with **19 CANONICAL functions + ~12 small UTILITY helpers + 8 cached
constants** — the canonical-only surface the pyhecke 1.0 promotion
needs.

---

## 5. Surprises

Compared to the workplan's "strong EXPLORATORY candidates" list:

1. **All flagged candidates confirmed.**  Every name on the workplan
   shortlist (`_chebyshev_magic`, `_phi1_full` (= `compute_phi1_full`),
   `_phi1_nuclear`, `_alternating_ordering`, `_phi1_from_ordering`,
   `_count_syts_by_12_relation`, `partition_jet_depth`,
   `q_laplacian_eigenvalue`, `q_resolvent_weight`,
   `partition_spectral_log_rate`, `lp_shadow_price`) was independently
   classified EXPLORATORY or UTILITY-of-EXPLORATORY.  No reclassification
   surprises among the flagged set.

2. **Bigger-than-expected EXPLORATORY surface.**  29 EXPLORATORY
   functions (40%) is larger than the workplan's "Strong" shortlist
   of 11.  The new additions all live in the Phase-5 LP-dual /
   Plancherel-trace cluster (#58 `unified_iterative_correction`,
   #60 `atom_character_raw`, #62 `conjugate_pair_cross_term`, #63
   `unified_iterative_correction_jet`, #64 `atom_markov_trace`, #65
   `atom_frobenius_norm_sq`, #67 `free_nucleon_frobenius_norm_sq`,
   #68 `binding_from_frobenius_pairing`, #69
   `sdp_cross_channel_contribution`, #70 `binding_energy`, #72
   `q_value_beta`, #73 `atom_mass`) — i.e. ~12 functions that are
   structurally entwined with the unified iterative correction
   pipeline.  They share `_PARTITION_TABLE` + the YSN-attached
   machinery (#17, #18, #50, #54, #55, #56).

3. **`atom_markov_trace` and `binding_from_frobenius_pairing` have
   self-documented deprecation banners.**  Line 2632:
   `"[DEPRECATED — Plancherel-weighted]"`; line 2991-2992:
   `"Legacy Plancherel path (default)"`.  These should have been
   moved to `_deprecated/` already — they're not just exploratory,
   they're explicitly marked stale and redirect to the canonical
   path.  Splitting them out is overdue.

4. **`binding_energy` (the top-level entry point) is EXPLORATORY,
   not CANONICAL.**  Line 3094 confesses `"Replaces the retired
   11-term Bethe-Weizsäcker formula path"`; it sums three EXPLORATORY
   contributions (#58, #68, #69). Canonical binding entry is
   `binding_canonical.binding_canonical` or
   `mass_formula_6term_mpfr_50dps.py`. The name is misleading.

5. **`atom_per_generator_volumes` is the most-imported CANONICAL
   function** (7 external importers, all canonical mass pipelines).
   Right anchor for the surviving `hecke_core.py`.

6. **Scope expansion vs the workplan shortlist.**  No symbol
   classification changed direction (every seeded CANONICAL was
   confirmed CANONICAL; every "strong EXPLORATORY" was confirmed
   EXPLORATORY), but the EXPLORATORY surface (29 functions) is
   ~3× the 11-name shortlist. Most additions are in the Phase-5
   LP-dual / Plancherel-trace cluster sharing `_PARTITION_TABLE`
   infrastructure.

---

## See also

- [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
- [`docs/pyhecke-optimization-workplan.md`](../pyhecke-optimization-workplan.md) §B1
- [`computations/lp_dual_solver.py`](../../computations/lp_dual_solver.py) — canonical LP/SDP entry (per CLAUDE.md `## LP / SDP duals`)
- [`computations/hecke/hecke_characters.py`](../../computations/hecke/hecke_characters.py) — where `chi_lambda_braid` lives (line 280)
- [`computations/binding_canonical.py`](../../computations/binding_canonical.py) — canonical binding entry referenced by deprecated `binding_from_frobenius_pairing`
- [`computations/_deprecated/`](../../computations/_deprecated/) — destination directory for the recommended split
