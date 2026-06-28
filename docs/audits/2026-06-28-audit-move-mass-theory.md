# Audit: Move Mass Theory Infrastructure Commentary

Extracted numerical/testing commentary from `mass-theory` files, replaced with canonical derivation prose.

## confinement-sdp.md
- Line 5: (`computations/multi_level_sdp.py`,
- Line 6: `sdp_cross_channel.py`, `misdp_cross_channel.py`); the LP
## chi-lambda-w0-sign-weighting.md
- Line 11: `per-wedderburn-block-ck` probe witness's `c5_match_status` and
- Line 54: ## Numerical verification
- Line 57: ( merge, per-Wedderburn-block probe at $q = 1 + \varepsilon$
- Line 75: The probe agent that surfaced this finding referred to
## mass-formula-regime-switching.md
- Line 98: $D$ chirality probe `d_chirality_probe.py` verified this: no
- Line 118: 2. *Max Specht dimension $f^\lambda = 16$ — tractable numerically.*
- Line 155: this fails by $-353\%$. Probe `d_chirality_probe.py` tested $13$
- Line 198: **Integrated witness table (from `mass_formula_6term.py`).**
## pachner-pentagon-borromean.md
- Line 140: 1. **Compute prototype**: extend a Pachner-state-sum probe for
## garside-as-compound-flow.md
- Line 69: | closed-form ODE per sub-interval | Python-verified (`computations/reeb_flow_garside_closed_form_verification.py`, witness status `verified`) |
## chirality-dual-space-derivation.md
- Line 64: Numerical match at $q_0 \approx 1.11$ confirmed.*
## sigma-shell-from-beta-chain-derivation.md
- Line 35: [`hecke_character_symbolic.q_character_on_braid_word`](../../../computations/hecke/hecke_character_symbolic.py).*
- Line 37: **Numerical verification — A_magic = 2 (deuteron).**
## outro-mass-theory.md
- Line 20: benchmarks.  Readers focused on the numerical predictions can
## phi-q-categorical-truncation-interpretation.md
- Line 20: ([`probe_tritium_k_star.py`](https://github.com/litlfred/qou/blob/claude/brane-tower-regularization-xTt8V/computations/probe_tritium_k_star.py))
- Line 55: $k_\star \leq 3$ (since they live in $H_3$). The uniform-$k$ probe
- Line 56: ([`probe_phiq_uniform_k.py`](https://github.com/litlfred/qou/blob/claude/brane-tower-regularization-xTt8V/computations/probe_phiq_uniform_k.py))
- Line 57: shows the Frobenius-paired truncation is far from numerically closed:
- Line 63: is a **categorical identity**, not a real-valued numerical identity;
- Line 66: numerical equality
## qdifference-kernel-prolongation-symbol.md
- Line 34: local monodromy, not searched numerically.
## markov-trace-ratio-exact-proof.md
- Line 15: [`homflypt_engine.py`](../../computations/homflypt_engine.py)
- Line 19: consumers — [`gram-matrix-dual.py`](../../computations/gram-matrix-dual.py),
- Line 20: [`confinement-operator-selection.py`](../../computations/confinement-operator-selection.py),
- Line 21: [`lp_dual_solver.py`](../../computations/lp_dual_solver.py) — the
## alpha-basis-knot-delta-q.md
- Line 26: [`delta_q_h_bracket_identity.py`](../../computations/delta_q_h_bracket_identity.py).
## z-eq-n-rho-correction.md
- Line 25: Numerical match at $q_0 = 1.10998\ldots$ for the four atoms in the table
- Line 26: ([per-atom δρ probe](../../../computations/per-atom-rho-deviation.witness.json)):
## frobenius-gram-matrix.md
- Line 26: At $q_0 = 1.109978595554181\ldots$ (50 dps), $hz^2 + z \approx 0.5514$ (the stale
## spectral-sequence-collapse-proof.md
- Line 50: *Numerical pipelines need only enumerate central idempotents $e_\lambda$,
## explicit-alpha-k-h4.md
- Line 31: value $q_0 \approx 1.110$ to numerical values in
- Line 33: verified to numerical precision against the Hoefsmit character matrix
- Line 57: numerical inverse is ill-conditioned — close via the sympy null-space
- Line 60: For $H_5$ and $H_6$, all $18$ partitions admit numerical $r_\lambda$
- Line 62: [`r_k_h5_h6_adaptive.py`](#). Symbolic forms for $y_\lambda$ at
- Line 69: [`computations/wedderburn_orthogonal_r_k.py`](#) —
## markov-chain-fluctuations.md
- Line 41: (`computations/substrate/hecke_core.py`), which selects the
## q-beta-direction-sanity-gate-proof.md
- Line 9: numerical deviations that survive into the more precise §4(a) radius-
## block-multiplicativity-v-free.md
- Line 27: Computed via [`per_generator_V_hat_3A`](https://github.com/litlfred/qou/blob/claude/log-delta-categorical-derivation/computations/mass_at_3A_proper.py)
- Line 28: on D, T, ${}^{3}$He at $H_6, H_9, H_9$ respectively (50 dps), as recorded in
- Line 135: [`binding_block_multiplicative.py`](https://github.com/litlfred/qou/blob/claude/log-delta-categorical-derivation/computations/binding_block_multiplicative.py)
## alpha-shift-torus-knot-proof.md
- Line 35: [`computations/alpha/alpha_shift_torus.py`](../../computations/alpha/alpha_shift_torus.py)
## wenzl-A-operator.md
- Line 50: [`a_operator/A_operator_extract_at_level.py`](../../../computations/a_operator/A_operator_extract_at_level.py),
## intro-cyclotomic-depth-3-trilog.md
- Line 6: conjecture from the numerical witnesses.
## descended-level-zero.md
- Line 183: The fix is not a numerical trick or heuristic: it is the
## quantum-dilogarithm-stratified-proof.md
- Line 133: **Open: numerical bound.**
- Line 134: The proof above is a Frobenius-paired *equality*, not a numerical
- Line 137: with $T_w$. To conclude that the *numerical* mass formula evaluated
## markov-axiom-recursive-ascent.md
- Line 38: (`computations/markov/markov_peel.py`) completes
## lr-coefficient-hecke.md
- Line 58: The script
- Line 59: [`computations/substrate/lr_coefficients.py`](../../computations/substrate/lr_coefficients.py)
- Line 65: [`pyhecke.skew_syt.skew_syt_count`](../../tools/pyhecke/python/pyhecke/skew_syt.py)
## gs-graded-markov-trace-existence.md
- Line 65: *The numerical values of $\mathrm{tr}_{M, \ell}(T_w)$ for the proton,
- Line 67: `markov_pipeline_cross_validator.py` and stored under
## y-lambda-closed-form-wenzl-bridge-proof.md
- Line 28: ## Numerical verification
- Line 34: All differences are at numerical precision ($10^{-16}$), confirming the
## crystal-isospin-degeneracy.md
- Line 11: [`mass_at_3A_proper.atom_braid_word_3A`](../../../computations/mass_at_3A_proper.py),
- Line 46: [`term7_alpha5_crystal_derivation.py`](../../../computations/term7_alpha5_crystal_derivation.py)
- Line 99: a direct probe of the **curvature** of the flat-transport map
- Line 113: [`term7_alpha5_crystal_derivation.py`](../../../computations/term7_alpha5_crystal_derivation.py)
- Line 115: [`mass_at_3A_proper.atom_braid_word_3A`](../../../computations/mass_at_3A_proper.py).**
- Line 116: The script's hardcoded `ATOMS` list treats each nucleon as a
- Line 152: for $D$ ($\sim 10^{-19}$) and small numerical residuals for the
- Line 184: [`global_wedderburn_sum_q_hecke_seminormal`](../../../computations/wedderburn_jones_markov.py)
- Line 201: $S_{\mathrm{crystal}}$ values match to within numerical precision
- Line 202: (50 dps via
- Line 203: [`term7_alpha5_crystal_derivation.py`](../../../computations/term7_alpha5_crystal_derivation.py)).*
## conj-psd-trace-orthogonality.md
- Line 62: Per Probe (1) and Probe (1b) in [`docs/audits/-dominant-partition-nucleon-structure.md`](../../../docs/audits/-dominant-partition-nucleon-structure.md):
- Line 72: - It does NOT predict the *specific* PSD-dominant shape at each $A$. At $A=4$ the dominant is the (A,A,A) rectangle; at $A=6$ it is the multi-step (3,3,3,3,2,2,2) (the rectangular-form conjecture was [empirically falsified at A=6](../../../docs/audits/-dominant-partition-nucleon-structure.md#gap-narrowing-probe-4c)).
- Line 78: - [`computations/probe_1_project_4he_on_dominant.py`](../../../computations/probe_1_project_4he_on_dominant.py) — Probe (1) at A=4
- Line 79: - [`computations/probe_1b_li6_orthogonality.py`](../../../computations/probe_1b_li6_orthogonality.py) — Probe (1b) at A=6
- Line 80: - [`computations/probe_4_li6_rectangular_python.py`](../../../computations/probe_4_li6_rectangular_python.py) — Lanczos LinearOperator framework
- Line 81: - [`computations/probe_4c_li6_large_d_scan.py`](../../../computations/probe_4c_li6_large_d_scan.py) — large-$d_\lambda$ scan that falsified the rectangular-form conjecture
## mass-tower-syt-cells.md
- Line 6: ([:refterm[descent]{#descent} rate empirical](#sim:descent-rate-probe)), which
- Line 60: ([:refterm[descent]{#descent} rate probe](#sim:descent-rate-probe)).
- Line 122: `computations/hecke/hecke_characters.py`).
- Line 135: (`computations/syt_cell_tower.py`) computes
## staircase-corner-hook-proof.md
- Line 17: $0.13\%$ ([`computations/close_321_weinberg_gap.py`](https://github.com/litlfred/qou/blob/main/computations/close_321_weinberg_gap.py));
- Line 20: ([`staircase_ew_residual_conjecture.py`](https://github.com/litlfred/qou/blob/main/computations/staircase_ew_residual_conjecture.py)).
## active-set-trace-concentration.md
- Line 13: This concentration is not a numerical artifact; it is a direct structural consequence of the **tensor factorization of the multi-nucleon interface**.
## cyclotomic-trilog-imaginary-closed-form.md
- Line 52: - Numerical witness (verified at $n = 3, 4, 5, 6, 7, 10, 11, 12, 13$ at 50 dps):
## prop-rigid-monoidal-structural-gap-invariance-proof.md
- Line 35: `tr_M_via_wenzl_bridge_mpfr` (50 dps Wenzl bridge).  All three
- Line 36: should give the same $|\tau|$ to 50 dps; the resulting
- Line 42: contributions vary by orders of magnitude across the six probe
## q-beta-q-eq-one-shadow-gate-proof.md
- Line 5: The $c_3$ anchor is conjectural at the value level (registry §3 records it as `EMPIRICAL — near-match`, refuted as a real-q fibre element by C1–C2) but **anchored as an integer shadow at q = 1**: it equals the Hopf-link Jones polynomial evaluated at $q = 1$, which is $-2$ in our normalization. A candidate whose $q \to 1$ limit gives anything other than $-2$ is structurally inconsistent with the registry anchor and is therefore REFUTED at the formalize-first level (before any numerical anchor sweep at $q_0$).
## hecke-generator-poly-reduction.md
- Line 55: `computations/chi_monotone_transfer.py`.
## intro-wenzl-bridge-cyclotomic.md
- Line 22: chapter's most concrete numerical content and is the natural
## habiro-expansion-atomic-proof.md
- Line 58: The symbolic pipeline `habiro_coefficients_atomic.py` implements
- Line 71: numerical-interpolation pipeline at $q_0 \approx 1.1100$ to 50
## crystal-isospin-degeneracy-proof.md
- Line 61: [`term7_alpha5_crystal_derivation.py`](../../../computations/term7_alpha5_crystal_derivation.py)*
- Line 86: [`mass_at_3A_proper.atom_braid_word_3A`](../../../computations/mass_at_3A_proper.py),
## archimedean-functor-uniqueness.md
- Line 198: No numerical witness is appropriate for a uniqueness claim. The
## explicit-alpha-k-h3-proof.md
- Line 36: The vanishing is exact (verified to numerical precision $10^{-16}$ in
- Line 71: Numerical evaluation at $q_0 \approx 1.110$ matches the symbolic
## six-term-mass-formula-complete.md
- Line 4: script(s) and witness JSON(s), and current derivation status.
- Line 39: - *Computation: `crt_markov.py` (witness `crt-markov.witness.json`);
- Line 40: `deuteron_first_principles.py` (witness `deuteron-first-principles.witness.json`);
- Line 41: `light_isotope_sweep.py` (witness `light-isotope-sweep.witness.json`).*
- Line 62: - *Numerical pathology at $q_0$ (documented ):
- Line 84: - *Computation: `mass_endomorphism.py`, `crt_markov.py`
- Line 85: (`tower_mass_symbolic_eval`), `tower_isotope_absolute.py`
- Line 124: - *Computation: `frobenius_partition_sum.py` (witness
- Line 126: `hochschild_h3.py` for $H_3(R, q)$ structure.*
- Line 158: - *Computation: `ribbon_content_average.py`,
- Line 159: `chirality_variants_probe.py`, `d_chirality_probe.py`
- Line 179: - *Computation: `gb_residue_tower.py` (first-pass numerical,
- Line 180: tiny residues at real q_0 approximation), `habiro_residue_symbolic.py`
- Line 197: `term5_aK_audit.py`).  Terms 2 and 3 satisfy it only in the R-side
- Line 202: dependent).  Numerical evaluation at $q_0$ amplifies this by $\sim 10^5$
- Line 223: itself a Markov trace.  See `kahler_lift.py` ('s recursion
- Line 227: #526.  The current `paper_six_term_isotope_sweep.py` evaluates the
- Line 228: literal $\Phi_q(|\hat V_i|)$ form, which is the **closed numerical
- Line 263: a numerical-interpolation path (`habiro_coefficients_interpolate.py`)
- Line 264: is scaffolded: Hoefsmit in `mpmath` at rational sample points, then
- Line 270: correction dominates (numerical, requires extending the BW
## flavor-split-habiro-derivation.md
- Line 3: To structurally derive (rather than numerically probe) the intrinsic $0.10\%$ residual for the nucleon flavor split $\Delta_{pn}$, we must treat the weak $\beta$-decay insertion precisely as we did the photon vertex in the $\alpha_{\text{EM}}$ derivation.
## intro-six-term-crystal-isospin-chirality.md
- Line 2: chapter's headline numerical prediction: an explicit
## three-halves-structural-factor.md
- Line 33: $q_0 \approx 1.110$ by specialisation; numerical cross-checks at
- Line 34: 50-dps mpmath verify each identity to $\leq 10^{-40}$ in the
- Line 35: [`tau-amphichiral-sdp-probe.witness.json`](../../../computations/probes/tau-amphichiral-sdp-probe.witness.json)
## borromean-markov-trace-closed-form-proof.md
- Line 90: >    `phase5/phase1c_proton_h3_symbolic_decomposition.py`), whose
## frobenius-antipode-unifies-chirality-and-tower.md
- Line 5: `alpha_blend_tower.py` — use the **same algebraic operation**:
- Line 48: (`computations/frobenius_antipode_symmetry.py`).**
- Line 74: (`computations/alpha/alpha_blend_tower.py`).**
- Line 129: - *`computations/frobenius_antipode_symmetry.py`
- Line 131: - *`computations/alpha/alpha_blend_tower.py`
- Line 133: - *`computations/tower_full_jet_filtration.py`
- Line 136: `computations/all_subsets_tower.py`).*
## figure-8-archimedean-illustration.md
- Line 95: Bloch-Wigner dilogarithm. The numerical value $:val[Vol_4_1]{precision=6}\ldots =
## knot-factor-amphicheiral-proof.md
- Line 55: [`docs/coordination/i1-probe-author-queue-.md`](../../../../docs/coordination/i1-probe-author-queue-.md)
- Line 57: [`computations/probes/knot_factor_amphicheiral_BD_probe.py`](../../../../computations/probes/knot_factor_amphicheiral_BD_probe.py).
## cyclotomic-depth3-dimension-synthesis-proof.md
- Line 115: ### Numerical PSLQ certification at $K = 5, 7$
- Line 117: [`cyclotomic_depth3_dimension_pslq.py`](https://github.com/litlfred/qou/blob/main/computations/cyclotomic_depth3_dimension_pslq.py),
- Line 130: same script works); each test takes ~30 seconds at 50 dps.
## t-beta-markov-frobenius-collapse-general.md
- Line 39: - [`docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md`](../../../docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md) — structural finding + numerical verification at $q_0$.
## conj-rho-prefactor-structural.md
- Line 7: is currently determined case-by-case as a numerical by-product of
- Line 41: The numerically verified rule (see "Critical structural finding" below)
- Line 70: (with $q_0 = 1.109978595554181\ldots$ (50 dps)), so $\dim_q((2,1)) \approx 2.01$. The
- Line 112: The B_3-level numerical evaluation
- Line 113: ([`computations/rho_prefactor_structural_verifier.py`](https://github.com/litlfred/qou/blob/main/computations/rho_prefactor_structural_verifier.py),
## per-braid-mass-tower.md
- Line 137: ## Numerical verification
- Line 140: [`computations/per_braid_tower.py`](https://github.com/litlfred/qou/blob/claude/audit-math-framework-FXlp2/computations/per_braid_tower.py),
## markov-trace-frobenius-selection.md
- Line 127: (`atomic_tr_m_mpfr_50dps.py`), `markov_peel`, the $\chi$-cache
- Line 128: combiner (`canonical_tr_m_via_chi_cache.py`), and the Habiro
## he4-two-row-dominance.md
- Line 10: [`mass_at_3A_proper.atom_braid_word_3A(2, 2)`](computations/mass_at_3A_proper.py).
- Line 65: [`delta_lambda_2row_stratum_analysis.py`](computations/delta_lambda_2row_stratum_analysis.py),
## interface-knot-markov-z.md
- Line 78: - Script: [`computations/delta_lambda_fr_identity_phase5c.py`](../../../computations/delta_lambda_fr_identity_phase5c.py)
## q-beta-over-e0-classical-vanishing.md
- Line 32: scalar** (numerical at $q_0$ — the affine target $n_{\text{target}} = S(q_0) \approx 0.18689$
- Line 37: (see [`qbeta_1ppq_achieved.py`](https://github.com/litlfred/qou/blob/main/computations/qbeta/qbeta_1ppq_achieved.py)).
## e-infinity-page-identifications.md
- Line 213: trace. Currently the $1 + h$ formula is derived numerically
## calibration-algebraic-mass-intro.md
- Line 1: _[draft]_ The previous section produced a categorical mass functor that is dimensionless and unfixed in scale. We now insert the minimum data needed to anchor it to physical units. The three inputs are aligned with the three Wedderburn channels of $H_3(R, q)$, so the calibration is structural rather than empirical: each channel takes one anchor, and the rest of the formula is forced. From the anchored mass we then derive the algebraic mass formula, the Hoefsmit seminormal $R$-matrix, the Habiro brane tower, and the quantum-dilogarithm $\Phi_q$ that compiles the whole chapter's numerical witnesses.
- Line 5: The body of the section develops the seminormal and convergence machinery. **Hoefsmit seminormal matrices as $R$-matrix evaluations in $H_n(q)$** (prop), with the figure-eight branching rule, supplies the explicit seminormal forms. The convergence backbone runs through **Hecke convergence bound** (prop), **Markov-trace inductive limit** (prop), and the long $\mathfrak{Q}_\beta$ ladder culminating in **$\mathfrak{Q}_\beta$ categorical-derivation precision ladder** (prop). The Habiro / brane-tower layer is filled in by **Habiro ring** (def), **$\widehat{Z}$ ring** (def), **Algebraic quantum volume** (def) and its specialisation, together with **Quantum dilogarithm stratified** (def) and **Q-Pochhammer partial product** (def) — the dilogarithm objects every numerical witness consumes. The realisation functor and its companion blocks package the bridge from the algebraic substrate to numerical evaluation.
## torus-knot-delta-q-writhe.md
- Line 43: [`rosso_jones_three_strand_delta_q.py`](../../computations/rosso_jones_three_strand_delta_q.py).
## alpha-k-categorical-closure.md
- Line 105: ## Numerical evidence (substrate level)
- Line 108: [`computations/derived_masses.py`](https://github.com/litlfred/qou/blob/main/computations/derived_masses.py)
## kashaev-density-equals-sdp-multiplicity.md
- Line 60: [`r5_full_canonical_knot_solver.py`](../../computations/r5_full_canonical_knot_solver.py)
- Line 85: [`mass_table_ppb.py`](../../computations/mass_table_ppb.py)
- Line 86: script self-declared the density rule $\rho_F \in \{1, 2\}$ as
- Line 112: - $\rho_F$ — Kashaev prefactor in `mass_table_ppb.py` (unnamed, compute-only)
- Line 115: [`mass_table_ppb.py`](../../computations/mass_table_ppb.py)
- Line 121: - [`mass_table_ppb.py`](../../computations/mass_table_ppb.py)
- Line 124: - [`predict`](../../computations/mass_table_ppb.py)
## jonquiere-cyclotomic-tate-rationality-proof.md
- Line 99: ### Numerical verification at 50 dps
- Line 101: [`jonquiere_cyclotomic_general.py`](https://github.com/litlfred/qou/blob/main/computations/jonquiere_cyclotomic_general.py),
## h3-markov-wenzl-weights.md
- Line 126: > $q$-dependent closed forms above, and numerical reproduction of the
## gb-depth-period-correspondence.md
- Line 88: explicit numerical witness in
## explicit-alpha-k-h4-proof.md
- Line 35: **Numerical evaluation at $q_0$.**  Hoefsmit characters computed via
- Line 37: `computations/hecke/hecke_characters.py`); the $5 \times 5$
- Line 49: verifies to $\sim 10^{-17}$ numerical precision against the
- Line 76: (only the depth-3 term survives).  Both sides agree to numerical
## markov-pair-z2.md
- Line 29: (cf. `adjacent-vs-full-probe.witness.json`,
## six-term-per-derivation-weights-proof.md
- Line 53: `computations/sweeps/paper_six_term_isotope_sweep.py`
## pn-averaging-uniqueness.md
- Line 33: `lambda_scale_refinement_h4_correction_bring.py` is **not purely
- Line 45: in `crystal_pole_order.py` (line 318: `pole_t35 == 10`).
- Line 58: (modulo the $h_q^4$ correction tracked in the refinement probe).
- Line 68: `probe_pn_flavor_asymmetry.py` Scheme 4).  Currently carried as a
- Line 83: The closed-form `closed_form_tau_M.py` already exposes the
## vc-as-depth-2-instance.md
- Line 76: For an explicit depth-2 numerical witness on the figure-8 knot
## three-calibration-inputs-proof.md
- Line 10: 1. **Dimensional analysis.** The modulus $q_0$ is pinned numerically by
## demazure-fiber-markov-trace.md
- Line 132: ## Numerical verification
- Line 134: The companion script
- Line 135: [`demazure_markov_trace.py`](https://github.com/litlfred/qou/blob/main/computations/demazure_markov_trace.py)
## spectral-sequence-h3-explicit.md
- Line 202: $R$ (paper's categorical base ring); no numerical evaluation is required
## q-rogers-pentagon-archimedean.md
- Line 76: [`pentagon_reduction_li2q.py`](https://github.com/litlfred/qou/blob/main/computations/pentagon_reduction_li2q.py)
- Line 80: ensures the reorganisation is numerically consistent.
- Line 108: The numerical residual at $u = v = 0.7$ is $2.3 \times 10^{-3}$ — the
## y-lambda-closed-form-wenzl-bridge.md
- Line 65: candidates in `schur_element_identify.py`).
- Line 78: ([`schur_element_identify.py`](#)) fails to recover the closed
- Line 90: available numerically via MPFR witness) derive symbolically via
- Line 101: [`computations/gb_filtration_gauge_invariance_test.py`](#)
- Line 106: [`computations/y_lambda_wenzl_bridge_extended.py`](#)
- Line 126: the larger ones, but they evaluate correctly via numerical
## binding-scale-catalan-proof.md
- Line 6: theorem of hyperbolic geometry, not a numerical approximation.
## confinement-nf-structure-forcing.md
- Line 29: LP is solved via [`solve_operator_selection_lp`](../../computations/lp_dual_solver.py)
- Line 57: - The Frobenius Gram in this probe is taken **diagonal**
- Line 63: requires a numerical / interval-arithmetic switch in the symbolic
## two-row-stratum.md
- Line 75: The companion probe
- Line 76: [`probe_he4_canonical_tr_m_fingerprint.py`](computations/probe_he4_canonical_tr_m_fingerprint.py)
- Line 84: [`delta_lambda_2row_stratum_analysis.py`](computations/delta_lambda_2row_stratum_analysis.py)
## gs-residue-at-root-existence.md
- Line 62: *The numerical residue values at $q_0 = :val[q_0]{precision=6}\ldots$ for proton,
- Line 63: neutron, deuteron are computed by `term6_full_pole_sum.py` and stored
## isospin-from-canonical-bowtie.md
- Line 1: > **CORRECTION NOTE ( surfaced by `verify_isospin_bar_anomaly.py`):**
- Line 43: [`_li_2_q_util.flavor_split_subleading`](../../computations/_li_2_q_util.py).
- Line 54: [`isotope_record_schema.py`](../../computations/isotope_record_schema.py)),
- Line 152: [`_li_2_q_util.flavor_split_subleading`](../../computations/_li_2_q_util.py)
- Line 154: [`m_p_borromean_verification_50dps.py`](../../computations/m_p_borromean_verification_50dps.py).
- Line 176: [`verify_isospin_bar_anomaly.py`](../../computations/verify_isospin_bar_anomaly.py)).
- Line 220: 3. The isospin-Z/2-anti-symmetric residue verification numerical witness
- Line 258: flavor split closed form (verified numerically at 305 ppm). -/
- Line 278: 1. **Author the verification compute script**:
- Line 279: `verify_isospin_bar_anomaly.py` — at $q = q_0$, evaluate the
- Line 318: [`m_p_borromean_verification_50dps.py`](../../computations/m_p_borromean_verification_50dps.py)
## q-rogers-pentagon-archimedean-proof.md
- Line 24: **Numerical evidence** at $q_0 \approx 1.110$, from
- Line 25: [`pentagon_reduction_li2q.py`](https://github.com/litlfred/qou/blob/main/computations/pentagon_reduction_li2q.py)
## staircase-ew-residual.md
- Line 36: [`close_321_weinberg_gap.py`](https://github.com/litlfred/qou/blob/main/computations/close_321_weinberg_gap.py),
- Line 48: [`staircase_ew_residual_conjecture.py`](https://github.com/litlfred/qou/blob/main/computations/staircase_ew_residual_conjecture.py),
## partition-sum-proton-residual.md
- Line 84: 2. *The numerical proton-mass calibration itself has uncertainty
- Line 88: *Script `computations/frobenius_partition_sum.py`
- Line 116: **Numerical witness at $q_0 \approx 1.11$.**
- Line 125: upstream (`kerov_walk_verify.py` confirms the reciprocal-dim
- Line 131: identity on the full Wedderburn decomposition. Numerical match
- Line 136: *Upstream `tower_isotope_absolute.py` tested whether the same
- Line 191: *Witnesses: `deuteron-residual-probe.witness.json`,
- Line 197: - [residual_partition_sum.py](https://github.com/litlfred/qou/blob/claude/1ppb-handover-docs-cyFlQ/computations/residual_partition_sum.py)
- Line 198: - [tower_isotope_absolute.py](https://github.com/litlfred/qou/blob/claude/1ppb-handover-docs-cyFlQ/computations/tower_isotope_absolute.py)
- Line 199: - [kerov_walk_verify.py](https://github.com/litlfred/qou/blob/claude/1ppb-handover-docs-cyFlQ/computations/kerov_walk_verify.py)
## jet-prefix-gb-filtration.md
- Line 1: Upstream `pure_hecke_binding.py` and `pure_hecke_binding_prefix.py`
- Line 94: *Script `gb_prefix_probe.py` implements a first-pass version
- Line 151: 3. *What is the numerical verification cost for $A = 3, 4$?*
## q-character-closes-parity-gap.md
- Line 34: **Numerical witness at $A = 1$ ($q_0 \approx 1.11$).**
- Line 94: prohibitive.  For $A \geq 2$ use the **numerical**
- Line 96: `computations/hecke/hecke_characters.py`
- Line 118: *Script: `computations/hecke/hecke_character_symbolic.py`.
- Line 124: *Apply the numerical pipeline in
- Line 125: `computations/hecke/hecke_characters.py` (full $H_{3A}$
- Line 128: numerical Hoefsmit handles the 2$\times$2 block $b^2$ sign robustly.
## categorical-higgs-mechanism.md
- Line 122: (Tier A2, this branch). Simple-multiplicity reading numerically
## brane-tower-z-habiro.md
- Line 23: $\Phi_q$ at $z = q_0 \approx 1.11$. Numerically
- Line 122: uniform-depth probe
- Line 123: ([`probe_phiq_uniform_k.py`](https://github.com/litlfred/qou/blob/claude/brane-tower-regularization-xTt8V/computations/probe_phiq_uniform_k.py))
- Line 204: The full probe record — sweep tables, error magnitudes, and the
- Line 243: `z-habiro-increment-probe`, verdict `cauchy-limit-exists-localised`:
## q-beta-c-2-eq-neg-one-structural.md
- Line 19: The earlier numerical observation $c_2 \approx -1$ (PR
- Line 30: [`qbeta_symbolic_chain_alpha_b.py`](https://github.com/litlfred/qou/blob/main/computations/qbeta/qbeta_symbolic_chain_alpha_b.py)
- Line 34: ## Numerical impact at $q_0$
## hecke-markov-transition-proof.md
- Line 47: the numerical evaluation is given in Chapter 7
## lepton-bring-surface-h3-3channel.md
- Line 157: - 1 Higgs (figure-eight $4_1$, "Higgs field / mass mechanism" per `knot-volumes.py:58`)
- Line 179: - Convention source: `tools/pyhecke/python/pyhecke/constants.py:156` (V_HAT_ELECTRON)
- Line 180: - Compute infrastructure: `computations/per_generator_V_hat_general.py` (generalises `per_generator_V_hat_3A`)
- Line 181: - T6 closure attempt: `computations/t6_lepton_h3_3channel_convention.py`
## q-beta-c-2-eq-neg-one-structural-proof.md
- Line 4: truncation of [`probe_q_beta_operator_valued_N3.py`](https://github.com/litlfred/qou/blob/main/computations/probe_q_beta_operator_valued_N3.py))
## borromean-bloch-group-element.md
- Line 113: $\mathrm{Vol}(\mathcal{B}_3)$ in [`mass_table_ppb.py`](../../computations/mass_table_ppb.py)),
- Line 154: 1. **Compute prototype**: at $q = q_0$, numerically evaluate both
## crystal-r-matrix-sub-lemma.md
- Line 49: was open for general multidim $\lambda$ (verified numerically 11/11
- Line 91: ## Numerical verification (witness)
- Line 93: [`computations/crystal_pole_order.py`](../../../computations/crystal_pole_order.py)
## cl3-zeta5-pslq-independence.md
- Line 14: *This proposition certifies, via PSLQ at 50 dps with coefficient
- Line 16: with any standard weight-3 period. Strong numerical evidence —
- Line 21: [`cl3_zeta5_pslq_search.py`](https://github.com/litlfred/qou/blob/main/computations/cl3_zeta5_pslq_search.py),
- Line 36: ### Numerical certification
- Line 41: PSLQ at 50 dps would have found it (with overwhelming probability).
- Line 59: So **at the level of accessible numerical certification**, the
- Line 64: - 1-dim: $X$ — *genuinely new*, with strong numerical evidence of
- Line 78: 2. **Higher PSLQ precision** (e.g., 100+ dps with $10^{12}$
- Line 79: coefficient bound) would extend the numerical certification but
- Line 85: The current PSLQ result is the **strongest unconditional numerical
## mass-spectrum-generating-function.md
- Line 52: the substrate value $q_0 = 1.109978595554181\ldots$ (50 dps; symbolic
## conj-lepton-tower-h-n-plus-1-branching.md
- Line 30: The factor $[3]_q \cdot [2]_q / [4]_q$ was numerically identified
- Line 32: + [`computations/t6_three_halves_factor_probes.py`](../../../computations/t6_three_halves_factor_probes.py)
- Line 52: | m | Lepton | Predicted ξ_m (corrected indexing m+2) | Numerical at q_0 |
- Line 116: All three readings are consistent with the muon (m=2) numerical
- Line 130: Numerical verification at $q_0 \approx 1.110$ (`tau_amphichiral_sdp_probe.py` witness):
- Line 170: - [`computations/t6_three_halves_factor_probes.py`](../../../computations/t6_three_halves_factor_probes.py) — muon empirical probe
- Line 171: - [`computations/probes/tau_amphichiral_sdp_probe.py`](../../../computations/probes/tau_amphichiral_sdp_probe.py) — tau amphichiral q-bracket probe
## p-from-braid-mirror.md
- Line 106: 1. **Verify numerically** that the Hecke quadratic preserves under P
- Line 111: holds (multiply the original by $\sigma_i^{-2}$). Concrete probe
## hecke-generator-poly-reduction-proof.md
- Line 24: $E_2 = \prod_j (-q^{-1} + d_j)$ used for numerical speed is a corollary that
## chirality-writhe-ribbon-derivation.md
- Line 116: **Numerical test at $H_6(R, q)$ (satellite $D$) — refuted (predicted $a_K = -2.164$ vs paper's $a_D = +1.209$).**
- Line 117: *Script `ribbon_content_average.py` computes
- Line 214: *`computations/ribbon_content_average.py` +
- Line 218: *Script `chirality_variants_probe.py` tested 8 candidate writhe-
## q-beta-c-k-leading-bias-correction-identity-proof.md
- Line 21: ## Numerical confirmation at $q_0$
- Line 23: The probe [`qbeta_ck_truncation_bias_correction_probe.py`](https://github.com/litlfred/qou/blob/main/computations/qbeta/qbeta_ck_truncation_bias_correction_probe.py)
## crystal-bases-path-a.md
- Line 6: [`per_irrep_pole_atom.py`](../../../computations/per_irrep_pole_atom.py)
- Line 24: [`crystal_pole_order.py`](../../../computations/crystal_pole_order.py)),
- Line 46: [`per_irrep_pole_atom_crystal.py`](../../../computations/per_irrep_pole_atom_crystal.py)
- Line 57: [`y_lambda_pole_order_cache.py`](../../../computations/y_lambda_pole_order_cache.py)
- Line 131: the budget of `per_irrep_pole_proton_h3.py` adapted to neutron
## geom-bridge-status.md
- Line 45: computation (`phi0_normalization_disproof.py`) gives
- Line 55: the degeneracy tell of a numerical accident, not a derivation).
## knot-mass-formula-unified.md
- Line 55: Markov-invariant. Numerically at $q_0 \approx 1.110$ this
- Line 95: model (`path-b-habiro-mass-probe.witness.json`). None of the
- Line 108: (or another structural reformulation) gives the canonical numerical
- Line 186: *Numerical values per
- Line 187: [`probe_term4_conventions.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/computations/probe_term4_conventions.py):*
- Line 204: ([`mass_formula_6term.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/computations/mass_formula_6term.py),
- Line 205: [`unified_low_isotope_predictor.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/computations/unified_low_isotope_predictor.py))
- Line 226: (`residual_partition_sum.py`).*
- Line 261: (`computations/bw_chirality_isotopes.py`) gives
- Line 288: per upstream `pure_hecke_binding.py`.*
## knot-factor-frobenius-pairing.md
- Line 171: - `computations/substrate/hecke_core.py::atom_markov_trace`:
- Line 174: - `computations/substrate/hecke_core.py::binding_from_frobenius_pairing`:
## q-pochhammer-partial-product.md
- Line 115: ## Numerical extraction (for the solver pipeline)
## kashaev-volume-conjecture.md
- Line 61: numerical computation is axiomatised so that the algebraic tower
## hoefsmit-V21-cos-symmetrization.md
- Line 102: [`probe_q_beta_per_irrep_cos.py`](../../computations/probe_q_beta_per_irrep_cos.py)
## frobenius-codim-universal-proof.md
- Line 217: [`computations/phase5/phase5_n8_dim_q_table.py`](https://github.com/litlfred/qou/blob/claude/wire-applied-uniqueness-mass-table/computations/phase5/phase5_n8_dim_q_table.py);
- Line 227: `phase5_n8_dim_q_table.py` script.
## pre-archimedean-derivation-chain.md
- Line 13: > derivation chain.  The **compute-pipeline mapping** (which script implements
## q-beta-c3-hopf-three-fold-markov.md
- Line 87: Per [`probe_q_beta_gamma_gamma_derivation.py`](../../computations/probe_q_beta_gamma_gamma_derivation.py),
## binding-alpha-shift-extension.md
- Line 133: `binding_rotation_phase_lead.py`;
- Line 136: - the q-Hamiltonian rotational-scale probe
- Line 137: (`binding_qhamiltonian_rotational_scale.py`) confirms $\mu_0 \approx 1.63$ MeV
## macdonald-hook-telescope.md
- Line 51: `y_lambda_macdonald_telescope.py` (every partition closes via
- Line 52: `sympy.cancel` to 0) and 191-sample numerical cross-check to
- Line 116: ## Numerical verification
- Line 118: The companion script
- Line 119: [`y_lambda_macdonald_telescope.py`](https://github.com/litlfred/qou/blob/main/computations/y_lambda_macdonald_telescope.py)
- Line 133: by the witness's 50-dps precision).
## chirality-residue-mass-term-proof.md
- Line 26: **Numerical witness (atomic isotopes).**
- Line 30: [`computations/atomic_chirality_residue.py`](#).
- Line 72: *Remark.* This proposition is a structural refinement of the unified mass formula. No new analytic content is added; the split exists by inspection.  The numerical witness shows that the chirality channel
## mass-endomorphism-jet-tower.md
- Line 115: (see `adjacent-vs-full-probe.witness.json`).
- Line 130: [`jet_tower_delta_max.py`](../../../computations/jet_tower_delta_max.py)
- Line 131: measurement script confirms `uniform_bound_pass = true` for
## phi-q-categorical-truncation-proof.md
- Line 118: **Remaining gap (numerical, not structural).**
- Line 122: conclude that the *numerical* mass formula at $q = q_0$ with $\Phi_q$
- Line 129: with $T_w$, but the **uniform numerical bound** on the truncated
- Line 141: real-valued numerical evaluation at $|\hat{V}|\approx 1$.
## qbeta-formalize-first-gates-intro.md
- Line 44: any future $F$ that fails a gate is excluded without a numerical search.
## he4-channel-active-set.md
- Line 58: [`he4-sdp-compositional-probe.witness.json`](computations/he4-sdp-compositional-probe.witness.json).)**
## cl3-zeta5-geometric-realization.md
- Line 4: The depth-3 numerical witness
- Line 62: > **Update (Numerical refutation)**: A PSLQ numerical experiment on the CS invariants of the seven Bring-natural torus-knot generators $\{T(2, 3), T(2, 5), T(2, 7), T(2, 9), T(3, 4), T(3, 5), T(5, 2)\}$ reveals that their Chern-Simons invariants are exactly rational (e.g., $\mathrm{CS}(T(2,5)) = 1/20, \mathrm{CS}(T(2,3)) = -1/12$). Therefore, their CS invariants cannot be expressed as non-trivial $\mathbb{Q}$-linear combinations of transcendental numbers like $\zeta(3)$ and $\mathrm{Cl}_3(2\pi/5)$. This strictly rules out torus knots as direct geometric realisations for this depth-3 period under Candidate 2.
- Line 107: numerical witness at depth 3, but no geometric image for the
- Line 116: script
- Line 117: ([`bring_trilog_zeta5_depth_3.py`](https://github.com/litlfred/qou/blob/main/computations/bring_trilog_zeta5_depth_3.py))
- Line 120: computation on a specific knot) and verify equality at 50 dps.
## frobenius-limits-substrate-cost.md
- Line 171: `kerov_walk_verify.py` ruled out the simplest Kerov random-walk
## t-beta-markov-frobenius-collapse.md
- Line 73: — structural finding + numerical verification at $q_0$.
## canonical-braid-interface-composition.md
- Line 4: [`mass_at_3A_proper.atom_braid_word_3A`](../../computations/mass_at_3A_proper.py)).
- Line 39: [`atom_braid_word_3A`](../../computations/mass_at_3A_proper.py);
- Line 43: [`interface_composition.py`](../../computations/interface_composition.py)
- Line 64: $\gamma \approx -1.295$ MeV closes the 4-atom probe set by definition
## q-beta-bar-even-kernel-typeclass.md
- Line 22: A future probe author evaluating a candidate $F(q)$ currently has to
- Line 78: checks, a probe author writes:
- Line 88: with each field hypothesis discharged by the corresponding probe.
## two-tier-scaling-pq.md
- Line 44: $q_0 = 1.109978595554181\ldots$ (50 dps) produces a dimensionless real number; converting
## binding-error-amplification-proof.md
- Line 39: is numerically hostile: it subjects the small binding signal to the same
## dim-master-pentagon.md
- Line 57: 2. Verify numerically at $q_0$ that the DIM master Pentagon's
## topological-mass-formula-algebraic-proof.md
- Line 29: the numerical mass; multiplication by $\hbar_q^{-2}$ and
## conj-atom-braid-exterior-algebra.md
- Line 1: **Conjecture (atom-braid exterior-algebra structure; partial-closure: verified at $A \leq 4$, general $A$ open).** *Let `A = Z + N` with $Z \geq 1$, $N \geq 0$, and let $T_w(Z, N) \in B_{3A}$ denote the canonical atom-braid word `atom_braid_word_3A(Z, N)` (`mass_at_3A_proper.py` recipe). Its image in the Iwahori–Hecke algebra $H_{3A}(q)$ under the standard $\sigma_i \mapsto T_i$ representation generates a sub-algebra whose GB-NF filtration shape is given by*
- Line 54: **Status:** the inference below was **FALSIFIED** by direct computation in [`atom_braid_active_partitions.py`](../../../computations/atom_braid_active_partitions.py). All `p(n_0)` partitions have non-trivial `χ_λ(T_w)` — the claimed "active set $\leq n^* + 1$" prediction does NOT hold on the Wedderburn basis. See [`docs/audits/-exterior-algebra-lp-claim-falsified.md`](../../../docs/audits/-exterior-algebra-lp-claim-falsified.md) for the full retraction.
- Line 99: 2. The specific structure of `_PROTON_G0 / _PROTON_G1 / _NEUTRON_G0 / _NEUTRON_G1` 3-strand patterns (cf. `mass_at_3A_proper.py`)
- Line 104: - [`computations/mass_at_3A_proper.py`](../../../computations/mass_at_3A_proper.py) — canonical `atom_braid_word_3A` recipe
## q-beta-categorical-precision-ladder.md
- Line 114: ## Numerical precision ladder
- Line 116: Verified at $q_0$ via [`binding_q_target_sweep.py`](../../computations/sweeps/binding_q_target_sweep.py) at 50 dps:
- Line 137: From [`audit_delta_S_chain.py`](../../computations/audit_delta_S_chain.py):
## typed-b3-sub-braid-extraction.md
- Line 44: This is **empirically verified** via two probe runs:
- Line 45: - [`probe_q_beta_cat_per_factor_decomposition.py`](../../computations/q-beta-cat-per-factor-decomposition.witness.json) — F_3's ε^6 leading coefficient is **exactly** $-3\sqrt{3}/4 = -2 \cdot b(1)^3$.
- Line 46: - [`probe_q_beta_operator_valued_N3.py`](../../computations/q-beta-operator-valued-N3.witness.json) — empirical residual after N=3 is $-0.0066$ ppm (112$\times$ tightening), validating the magnitude.
- Line 67: | **Step C (numerical-equivalence axiom)** | exact arithmetic match | closed (item 2) |
## jet-convergence-classical-limit.md
- Line 105: *Numerical verification ($k = 3 \ldots 9$): the
## frobenius-s-classification-proof.md
- Line 19: $m_e$, and binding scale $\alpha$ are real numerical constants
- Line 68: contribution to the categorical mass.  Numerically, since $S$
- Line 75: [`computations/wedderburn_3term_inter_only.py`](#)
- Line 76: verifies the eigenvalue assignments numerically at $q_0$ and
## flavor-dressed-mass-from-substrate-split.md
- Line 37: numerical evaluation at $q = q_0$ and the matching CODATA residual
- Line 40: (Observations chapter; per the manuscript convention numerical
## atom-knot-mass-derivation-proof.md
- Line 17: small cases by [`gb_filtration_jet_tracker.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/gb_filtration_jet_tracker.py)
## markov-trace-factorization-proof.md
- Line 46: trace compute the same algebraic object.  The numerical
## lp-dual-scaling-conjecture.md
- Line 72: follow-up (H)). The current probe sweeps $q \to 1^+$ only;
- Line 73: a separate $q \to 0^+$ probe is needed.
- Line 85: 1. **${}^4\mathrm{He}$ probe** ($A = 4, |T_3| = 0$, $n = 12$;
## qbeta-c4-from-c3-c8-product-identity.md
- Line 55: [`probes/qbeta_c4_structural_product_identities.py`](../../computations/probes/qbeta_c4_structural_product_identities.py)).
## cyclotomic-orbit-sum-all-depths-proof.md
- Line 26: Verified at 50 dps for $n \in \{2, 3, 4, 5\}$, $N \in \{3, 4, 5, 6, 7\}$
## depth-stratified-frobenius-reciprocity.md
- Line 79: [`binding_depth_stratified_knot_weighted.py`](https://github.com/litlfred/qou/blob/main/computations/binding_depth_stratified_knot_weighted.py)
- Line 193: ([`compute_atom_chi_rust.py`](https://github.com/litlfred/qou/blob/main/computations/compute_atom_chi_rust.py))
- Line 194: or the symbolic Hoefsmit pipeline. The script
- Line 195: [`fr_pullback_k3_test.py`](https://github.com/litlfred/qou/blob/main/computations/fr_pullback_k3_test.py)
## sdp-degeneracy-at-metallic-coincidence.md
- Line 40: (`computations/two_quark_active_set_mahler_sweep.py`)
- Line 44: is the **first non-null result** in a series of five prior numerical
- Line 79: (silver only).  For n=3 the empirical probe (with Gram approximation)
## pre-tau-vs-post-tau.md
- Line 38: * When a numerical equality bridges the two sides — e.g. the
- Line 43: either side alone. Numerical comparisons of such bridges with
## y-lambda-sign-pattern.md
- Line 26: substrate $q_0 = 1.109978595554181\ldots$ (50 dps), the Jones–Markov block weights
- Line 38: [`y_lambda_sdp.py`](https://github.com/litlfred/qou/blob/main/computations/y_lambda_sdp.py).
- Line 102: ([`y_lambda_symbolic.py`](#)) gives exact $q$-rational forms,
- Line 103: matching the numerical values to machine precision at $q_0$.  All
## conj-im-q-physical-role.md
- Line 50: $\approx 1.010$, radius $\approx 0.100$ per `q_beta_complex_q_test1_phaseA_v2.py`).
## magic-A-binding-formula.md
- Line 77: [`binding-ladder-catalog.py`](../../computations/binding_ladder_catalog.py)
- Line 84: ## Numerical witness
- Line 86: [`computations/binding_alpha_shift_witness.py`](../../computations/binding_alpha_shift_witness.py)
## q-beta-c-k-leading-bias-correction-identity.md
- Line 2: the joint-fit numerical extraction of the $\mathfrak{Q}_\beta$ precision-ladder
- Line 40: truncated at finite order and extracted numerically, would produce. The
- Line 53: This proposition's numerical confirmation shows the bias-corrected
## rho-k-h3a-refinement.md
- Line 60: [`computations/rho_k_h3a_refinement.py`](computations/rho_k_h3a_refinement.py);
## q-beta-bar-even-kernel-invariant-proof.md
- Line 14: (verified in the [`qbeta_symbolic_chain_alpha_b.py`](https://github.com/litlfred/qou/blob/main/computations/qbeta/qbeta_symbolic_chain_alpha_b.py)
- Line 30: [probe-B](https://github.com/litlfred/qou/blob/claude/qbeta-ck-habiro-operator-route-2026-06-04/docs/audits/2026-06-04-qbeta-ck-operator-route-kickoff.md)
## qmn-recursive-memoized.md
- Line 70: - [`q_mn_canonical.py`](https://github.com/litlfred/qou/blob/main/computations/q_mn_canonical.py)
- Line 76: - `q_mn_recursive_memoized.py` (this PR / follow-up): wrap
- Line 113: - **Implement**: `q_mn_recursive_memoized.py` driver. Mechanical
- Line 114: wrapper over existing `q_mn_canonical.py`; estimated 1-day work.
## knot-operator-lp-selection.md
- Line 113: [`wedderburn_pair_volumes.py`](https://github.com/litlfred/qou/blob/main/computations/wedderburn_pair_volumes.py)
## q-beta-c-k-recursion-from-habiro-q-difference.md
- Line 63: | $c_4$ at $1\,\mathrm{ppQ}$ | fit (CODATA residual), value $-0.97157$ | [`qbeta_1ppq_achieved.py`](https://github.com/litlfred/qou/blob/main/computations/qbeta/qbeta_1ppq_achieved.py) |
- Line 65: | Kernel $R(q,\xi)$ | structurally constrained: bar-ODD leading $a_1=-c_3$ (carrier $\kappa_{(2,1)}=(q-1)^3(q+1)/q^2$), period-3/$\zeta_6$ resonance, $\sqrt{u}$-to-$u^2$ lift. The $\zeta_4$ residue is **relaxed** — the root-of-unity residue program shows neither the content-Casimir $\mu_\lambda$ nor the framing $\cos\alpha_{\mathrm{eff}}$ supplies a bar-odd-compatible genuine $\zeta_4(q)$; it is a $\sqrt{q}$ double-cover reading of $\zeta_2$ (bar-fixed $q=-1$) or a post-$\cos$-wrap archimedean feature, **not** a fibre constraint. | [`habiro_ladder_bridge.py`](https://github.com/litlfred/qou/blob/main/computations/habiro/habiro_ladder_bridge.py), [root-of-unity program audit](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-13-qbeta-root-of-unity-residue-program.md) |
- Line 114: ([`qbeta_c_k_recursion_scaffold.py`](https://github.com/litlfred/qou/blob/main/computations/qbeta/qbeta_c_k_recursion_scaffold.py))
## derived-mass-formula-light-isotopes.md
- Line 30: **Empirical scorecard at $q_0 = 1.109978595554181\ldots$ (50 dps):**
## bring-trilog-depth-3-witness.md
- Line 2: 50-digit numerical witness with functional-equation cross-validation).**
- Line 23: ### Numerical witness (50-digit precision)
- Line 25: Computed via `mpmath.polylog` at `mp.dps = 50` (script
- Line 26: [`bring_trilog_zeta5_depth_3.py`](https://github.com/litlfred/qou/blob/main/computations/bring_trilog_zeta5_depth_3.py),
- Line 61: **Numerically verified** at 50 dps:
- Line 63: | Side | Value (50 dps) |
- Line 72: independent of `mpmath`'s polylog implementation** — the functional
- Line 115: This is the **first depth-3 numerical witness** for
- Line 123: *numerically tightest* graded-Mikusiński instance recorded.
## lambda-scale-substrate-form.md
- Line 48: - [`lambda_scale_all_c_i_family_a.py`](../../computations/lambda_scale_all_c_i_family_a.py) — the proved Family A closed form.
## mass-tower-open-problems-classes.md
- Line 34: $h = q - q^{-1}$) is recorded as a paper-empirical ansatz; a numerical
- Line 35: probe failed to match against eight candidate writhe-ribbon formulas.
## q-integer-mass-formula.md
- Line 200: *No intermediate fitting, no free parameters, no numerical
## exterior-square-borromean-proof.md
- Line 47: $9 + 36 = 45$; at $q_0 = 1.109978595554181\ldots$ (50 dps) the q-deformation differs from
- Line 66: [`computations/alpha_em_q9_q10_derivation.py`](#) and
- Line 67: the dimension formula directly: numerical match to the expected
## three-calibration-inputs.md
- Line 8: | ID | Canonical observable | Numerical proxy | What it fixes | DOF of $H^1 = 2W$ |
- Line 48: For every numerical observable $\mathcal{O}$ in the paper —
- Line 67: numerically through its proxy $m_\mu/m_e$). The two dimensional
- Line 75: - $q_0$ is a numerical constant *only* via CAL-2; downstream compute
- Line 77: the CAL-2 numerical value at the final reporting step
## qbeta-c8-c10-silver-rationals.md
- Line 28: SDP-extraction script's own caveat, the c_k values extracted at the
- Line 65: - Closed-form derivation probe + witness:
- Line 66: `probes/qbeta_c8_c10_closed_form_predictions.py`.
- Line 67: - Closed-form wiring outcome at $q_0$ (companion empirical probe):
- Line 68: `probes/qbeta_closed_form_wiring_n4_to_n10.py`.
## operator-valued-combiner-convergence.md
- Line 77: [`canonical_tr_m_via_branching.py`](../../../computations/canonical_tr_m_via_branching.py)
- Line 80: [`canonical_mass_table_extended.py`](../../../computations/canonical_mass_table_extended.py):
## q-beta-q-eq-one-shadow-gate.md
- Line 53: With all four §4 invariants formalized, the formalize-first gate chain is complete; any future $F(q)$ candidate is evaluable as a Lean class-instance attempt rather than as a numerical fit.
## tau-all-orders-bridge.md
- Line 88: [`tau_all_orders_h6_empirical.py`](../../../computations/probes/tau_all_orders_h6_empirical.py)
## y-lambda-cyclotomic-factorization.md
- Line 1: *Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data. The $n = 2$ case is formalised faithfully — both partitions factor through the genuine cyclotomic denominator $D_2 = \Phi_4\Phi_8 = (t^2+1)(t^4+1) \neq 0$; the $n = 3, 4$ denominators are numerically verified for all 18 partitions in the witness and tracked for formalisation.*
- Line 86: [`computations/y_lambda_cyclotomic_factor.py`](https://github.com/litlfred/qou/blob/main/computations/y_lambda_cyclotomic_factor.py)
## per-nucleon-shift-additive-linearity-proof.md
- Line 25: ([`dp_pole_probe.py`](../../computations/dp_pole_probe.py)),
- Line 40: [`per_irrep_pole_proton_h3.py`](../../computations/per_irrep_pole_proton_h3.py)
- Line 48: [`d_u_closed_form_proof.py`](../../computations/d_u_closed_form_proof.py))
- Line 52: [`per_irrep_pole_deuteron_h6.py`](../../computations/per_irrep_pole_deuteron_h6.py)
## mass-ordering-corrected.md
- Line 4: the nucleon traces at $q_0 = 1.109978595554181\ldots$ (50 dps) are:
## plancherel-term-7-formulation-proof.md
- Line 17: $q_0 = 1.109978595554181\ldots$ (50 dps) it deviates from $1$ — empirically
- Line 30: constant (numerically $\lesssim 2$ at $q_0$ for $n \leq 12$), giving
- Line 50: **Naming note.** *Earlier drafts (and the legacy script
- Line 51: `plancherel_term_7.py`) referred to $\tilde w_\lambda =
- Line 65: **Numerical witness.**
- Line 66: [`computations/plancherel_term_7.py`](#) computes
## wedderburn-weight-canonical.md
- Line 59: [non-self-conjugate empirical witness](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/probe-wedderburn-weight-scheme.witness.json),
- Line 170: [`probe-wedderburn-weight-scheme.witness.json`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/probe-wedderburn-weight-scheme.witness.json)
## graded-hecke-energy-truncation-bound.md
- Line 22: For numerical evaluation of $\mathrm{tr}_M(T_w(\mathcal{B}_K), q_0) =
- Line 39: The result also enables **resumable** numerical evaluation: a
- Line 49: [`computations/probes/graded_hecke_energy_probe.py`](https://github.com/litlfred/qou/blob/claude/wire-applied-uniqueness-mass-table/computations/probes/graded_hecke_energy_probe.py)
- Line 53: `graded-hecke-energy-probe.witness.json`.
## six-term-mass-formula-complete-table-data.md
- Line 1: | term | derivation source(s) | computation script | status |
- Line 3: | 1 | categorical-mass-markov, Jones-Markov | markov_peel.py + atomic-tr-m-mpfr-50dps.witness.json | TRACE (canonical Markov-invariant) |
- Line 6: | 4 | Frobenius co-Casimir (Lean-proved) | frobenius_partition_sum.py | TRACE (Markov-invariant) |
- Line 7: | 5 | dual-space symmetric-channel per-crossing | ribbon_content_average.py, chirality_variants_probe.py | TRACE (Markov-invariant within sign list) |
## markov-trace-product-proof.md
- Line 44: Numerically at $q_0$: vertex-product $z^3 \approx 0.1245$
## unified-curvature-rank-mass-formula-proof.md
- Line 47: ([atomic_chirality_residue.py witness](#)) and dominates the deepest
## habiro-residue-sum-equivalence.md
- Line 40: `computations/markov/markov_pipeline_cross_validator.py`.  The
- Line 57: `markov_pipeline_cross_validator.py`; output witness
- Line 68: `run_pipeline.py` automatically reruns it whenever either input
## mass-volume-factorization.md
- Line 117: ${}^4\mathrm{He}$ uses four ($4\cdot 8G$). The companion probe
## shared-denominator-cusp-holonomy.md
- Line 163: bijection cannot be a literal numerical identity
- Line 171: content (algebraic poles label cusps) while bounding its *numerical*
## bring-trilog-imaginary-tate-rational-proof.md
- Line 46: ### Numerical verification at 50 dps
- Line 48: Verified by [`kummer_reflection_zeta5.py`](https://github.com/litlfred/qou/blob/main/computations/kummer_reflection_zeta5.py)
- Line 51: | Quantity | Value (50 dps) |
- Line 53: | Direct: $\mathrm{Im}\,\mathrm{Li}_3(\zeta_5)$ via `mpmath.polylog` | $0.99220085376959424561524208214724464647120923410832\ldots$ |
## np-discrepancy-resolution.md
- Line 2: *Upstream `residual_probe_pn.py` reports a neutron/proton tower
- Line 7: CODATA $939.6$ MeV at full 50-dps symbolic eval), while
- Line 19: *The full mass-endomorphism tower at 50-dps symbolic
- Line 20: ([`mass_endomorphism.py`](../../computations/mass_endomorphism.py),
- Line 21: recomputed at 50 dps via sympy + mpmath, no float64):*
- Line 32: dps) sits far from the $q_0 = 1.11$ pole of $\Phi_q$ (distance
- Line 115: results (script `light_isotope_sweep.py`):*
- Line 137: likely wrong $a_K$ assignment — `d_chirality_probe.py`
- Line 154: - `computations/residual_probe_pn.py` (upstream): raw tower $n/p$ diagnosis
- Line 155: - `computations/sweeps/light_isotope_sweep.py`: Term 1 + Frob sweep
- Line 156: - `computations/bw_chirality_isotopes.py` (upstream): Term 5 (BW+χ) sweep
- Line 157: - `computations/mass_formula_6term.py`: integrated 6-term comparison
- Line 158: - `computations/d_chirality_probe.py`: shows paper's D-chirality is wrong
## mn-classical-parity-blind.md
- Line 11: *Using `computations/schur_weyl_mn_witness.py`:*
- Line 77: *Script: `computations/schur_weyl_mn_witness.py`.
- Line 78: Uses `murnaghan_nakayama.py` (classical MN recursion) and
- Line 79: `schur_weyl_symbolic.py` (global $H_{3A}$ sum with q symbolic).
## alpha-k-derivation-procedure-proof.md
- Line 64: [`y_lambda_jones_markov_witness.py`](#).  Each table records:*
- Line 68: - *Jones–Markov weight $y_\lambda$ (numeric at $q_0 = 1.109978595554181\ldots$ (50 dps));*
- Line 106: ([`y_lambda_jones_markov_witness.py`](#)) forces sparse Hoefsmit
- Line 118: any probe point.  Two reconstruction strategies:
- Line 121: Choose $m$ distinct probe values $q_1, \ldots, q_m$ (e.g.\
- Line 122: $\{1.02, 1.05, 1.08, 1.11, 1.15\}$ — [`crt_markov.py`](#)
- Line 129: probe points — not $5$.  Five probes suffice for: (i) a degree-$4$
- Line 143: and $5$ CRT probe points $\{(q_i, z_i, \mathbf{y}(q_i))\}$ for
- Line 145: recorded (probe-rebuild cost prohibitive in pure Python; defer to
## mass-element-nf.md
- Line 92: at $q_0 = 1.109978595554181\ldots$ (50 dps).
## mass-side-kernel-formalize-first-gates.md
- Line 14: [`mass_theory_formalize_first_invariants_probe.py`](https://github.com/litlfred/qou/blob/main/computations/mass_theory_formalize_first_invariants_probe.py),
- Line 29: | (a) | **Anchor-stable** | cross-anchor swing $|w(q_\mu) - w(q_p)| / |w(q_p)| < 10^{-6}$ | `MassAnchorStableGateClass swing` (where `swing` is the probe-computed magnitude) |
- Line 32: | (d) | **Direction sanity** | $|m - \text{target}| \le \text{threshold} \cdot \text{target}$ (additive form; substrate target $\approx 2.46$, the CODATA-implied near-match documented in [`_li_2_q_util.py:298-313`](https://github.com/litlfred/qou/blob/main/computations/_li_2_q_util.py)) | `MassDirectionSanityGateClass m_candidate` (where `m_candidate` $= |w(q_0)|$) |
- Line 39: > [`mass_theory_formalize_first_invariants_probe.py`](https://github.com/litlfred/qou/blob/main/computations/mass_theory_formalize_first_invariants_probe.py))
- Line 112: **No sympy probe.** The mass-side $\S 4$ $4 \times 3$ verdict matrix
- Line 114: [`mass_theory_formalize_first_invariants_probe.py`](https://github.com/litlfred/qou/blob/main/computations/mass_theory_formalize_first_invariants_probe.py).
## flavor-mass-splitting-bound.md
- Line 63: is committed in this revision). The numerical evaluation at $q_0$
## jet-tower-uniform-delta-max.md
- Line 20: infrastructure (`unified_lift.py` + the new
- Line 50: The measurement script
- Line 51: [`computations/jet_tower_delta_max.py`](../../../computations/jet_tower_delta_max.py)
- Line 53: `delta_n` per jet level — see `unified_lift.py` line 158) for
- Line 75: (Concrete numerical entries are produced on each run; the
- Line 139: support at $n = 1, 2, 3$ for D, T, ${}^{3}$He via `jet_tower_delta_max.py`.
## lepton-mass-tower-canonical.md
- Line 132: | **B** | Compute $|\mathrm{tr}_M(K_\ell)|$ at substrate $q_0$ + tower corrections; fit a functional form for $\xi_\ell$ that matches CODATA for all 3 leptons; check consistency | 4-6 hours numerical |
## wenzl-bridge-applicability-qou.md
- Line 38: witness at $n = 3, \ldots, 11$ (193 partitions) to MPFR 50-dps
## meson-kaon-pion-hecke-seifert.md
- Line 30: *The numerical value $3.5361$ matches the PDG ratio
## lr-tensor-character-bridge.md
- Line 148: [`computations/markov/markov_trace_via_wenzl_lr.py`](https://github.com/litlfred/qou/blob/main/computations/markov/markov_trace_via_wenzl_lr.py)
- Line 153: [`computations/cross_check_trM_wenzl_lr_1ppb.py`](https://github.com/litlfred/qou/blob/main/computations/cross_check_trM_wenzl_lr_1ppb.py)
- Line 158: [`computations/wenzl_lr_convention_adapter.py`](https://github.com/litlfred/qou/blob/main/computations/wenzl_lr_convention_adapter.py)
## hecke-1d-irrep-closed-form-character-proof.md
- Line 60: Bit-exact at 50 dps for all atoms in $\{p, n, D, T, {}^{3}\mathrm{He}\}$
## phi-q-tower-jsj-bridge.md
- Line 86: $\mathrm{Vol}_{\mathrm{hyp}}(P)$ numerically with SnapPy. Fast on
- Line 100: while JSJ remains the numerical workhorse.
## cyclotomic-cl3-orbit-sum-general.md
- Line 42: - Numerical witness (verified at $N = 3, 4, 5, 6, 7, 10, 11, 12, 13$ at 50 dps):
## q-beta-radius-of-convergence-gate-proof.md
- Line 23: ## Numerical anchor (verified)
## commutative-chirality-vanishes-proof.md
- Line 30: representation theory. Numerical scan
- Line 31: ([`commutative_case_diagnostic.py`](#)) confirms that the
## topological-mass-formula-algebraic.md
- Line 83: recovers the numerical Archimedean value $\Phi_1(\beta)$, but
- Line 108: Archimedean numerical value of $\mathrm{Vol}(K)$ may cite either.
## per-nucleon-shift-additive-linearity.md
- Line 42: [`mass_endomorphism.proton_cross`/`neutron_cross`](../../computations/mass_endomorphism.py).)
- Line 52: [`docs/audits/-ocneanu-cancellation-numerical-verification.md`](../../docs/audits/-ocneanu-cancellation-numerical-verification.md)
- Line 53: for the high-precision (200 dps) verification.
- Line 80: 3. **Pole-counting consumer.** [`dp_pole_probe.py`](../../computations/dp_pole_probe.py)
## tower-binding-energy.md
- Line 16: [`mass_at_3A_proper.atom_braid_word_3A`](https://github.com/litlfred/qou/blob/main/computations/mass_at_3A_proper.py)).
- Line 111: ## Numerical results
## conj-canonical-knot-id-sdp.md
- Line 81: Numerical SDP witnesses (stored in
- Line 82: `computations/probe-sdp-canonical-paper-formula.witness.json`)
- Line 92: ([`r5_full_canonical_knot_solver.py`](../../../computations/r5_full_canonical_knot_solver.py),
- Line 117: documented in `probe-sdp-canonical-paper-formula.witness.json`).
- Line 131: 1. The R5-full numerical witness (`R5FullWitness LightNucleus.helium3`)
- Line 136: hypothesis upgrading numerical PSD-feasibility to unique-minimizer
- Line 144: feasible set, not a numerical certificate), the historical
- Line 192: The numerical evidence from
- Line 217: numerically* by the R5-minimal verifier
- Line 218: ([`joint_tower_sdp_solver_v2.py`](https://github.com/litlfred/qou/blob/main/computations/joint_tower_sdp_solver_v2.py)).
## wedderburn-bratteli-recursion.md
- Line 40: [`computations/y_lambda_bratteli_extract.py`](#) —
## bring-trilog-imaginary-tate-rational.md
- Line 3: verified at 50 dps via Kummer reflection).**
- Line 5: The depth-3 numerical witness
## mass-tower-deeper-fillers.md
- Line 57: - **Wiring follow-up:** `crt_markov.py` currently has no
- Line 61: in `markov_weights_symbolic.py`, leave the symbolic version
- Line 62: intact for `y_lambda_equivalence_proof.py:60` to consume.
## alpha-shift-torus-knot.md
- Line 27: The numerical evidence
## plancherel-weight-boundedness-proof.md
- Line 38: **Plancherel distribution at $q_0 = 1.109978595554181\ldots$ (50 dps) (small $n$).**
## partition-sum-proton-residual-table5-data.md
- Line 1: | probe | best candidate | residual vs gap |
- Line 3: | Deuteron gap (`deuteron_residual_probe.py`) | $(5/2) \cdot m_e$ at $n = 3$ | $+3.92\%$ |
## rho-k-h3a-refinement-interpretation.md
- Line 17: $q_0 = 1.109978595554181\ldots$ (50 dps), $[2]_{q_0}^2 \approx 4.04$, so each level
## cl3-zeta5-orbit-sum-identity-proof.md
- Line 47: ### Numerical verification at 50 dps
- Line 49: [`cl3_zeta5_orbit_sum.py`](https://github.com/litlfred/qou/blob/main/computations/cl3_zeta5_orbit_sum.py),
- Line 52: | Quantity | Value (50 dps) |
## interface-knot-markov-z-proof.md
- Line 49: ### Empirical verification (4 atoms, 50-dps Rust kernel)
- Line 51: Computed via [`delta_lambda_fr_identity_phase5c.py`](../../../computations/delta_lambda_fr_identity_phase5c.py)
## habiro-pochhammer-bridge.md
- Line 26: ## Numerical verification (proton, $n = 9$)
## delta-q-decoration.md
- Line 84: [`computations/delta_q_decoration.py`](computations/delta_q_decoration.py),
- Line 86: [`hecke_characters.py`](computations/hecke/hecke_characters.py).
## mass-tower-coefficient-stratification-proof.md
- Line 20: [`computations/wedderburn-strata-witness.py`](#)
- Line 26: - $\dim_q V_\lambda$ at $q_0 = 1.109978595554181\ldots$ (50 dps, categorical $q$-dim)
## q-beta-direction-sanity-gate.md
- Line 21: numerical anchor sweep.
- Line 39: Lean class-instance attempt rather than as a numerical fit.
- Line 66: numerical anchor sweep) of the checklist.
## habiro-precision-ladder-equivalence.md
- Line 26: Planck quantum (categorical; numerical value at the substrate q_0
## jet-tower-convergence.md
- Line 63: [`computations/jet_tower_delta_max.py`](../../../computations/jet_tower_delta_max.py)
- Line 64: and `unified_lift.py`) the per-level terms for $\mathrm{D}$,
## confined-knot-binding.md
- Line 5: ([`mass_at_3A_proper.atom_braid_word_3A`](https://github.com/litlfred/qou/blob/main/computations/mass_at_3A_proper.py))
## kashiwara-jones-alternation-interpretation.md
- Line 120: Per [`probe_q_beta_c5_c6_multilink.py`](../../computations/probe_q_beta_c5_c6_multilink.py),
## wenzl-qmn-synergy.md
- Line 8: `computations/_deprecated/q_mn_canonical.py`,
- Line 64: in `depth_resolved_phi_k_hoefsmit.py` can replace its Hoefsmit
- Line 78: [`computations/_deprecated/q_mn_canonical.py`](https://github.com/litlfred/qou/blob/main/computations/_deprecated/q_mn_canonical.py)
- Line 81: [`hecke_characters.chi_lambda_braid`](https://github.com/litlfred/qou/blob/main/computations/hecke/hecke_characters.py),
- Line 87: [`computations/y_lambda_wenzl_bridge_extended.py`](https://github.com/litlfred/qou/blob/main/computations/y_lambda_wenzl_bridge_extended.py)
- Line 91: [`computations/wenzl_qmn_trace_cross_check.py`](https://github.com/litlfred/qou/blob/main/computations/wenzl_qmn_trace_cross_check.py)
## spin-involution-lp-dual-invariance-proof.md
- Line 111: [`atom_braid_word_3A`](../../../computations/mass_at_3A_proper.py))
- Line 135: [`probe-phiq-pair-knot-markov-trace.witness.json`](../../../computations/probe-phiq-pair-knot-markov-trace.witness.json)
- Line 143: \;=\; 0.06216177120816107\ldots \quad \text{(50-dps evaluation; algebraic equality via the Hoefsmit seminormal form's $\sigma_{pp} = \sigma_{nn}$ identity on the $V_{(2,1)}$ block, independent of dps)}.
- Line 148: [`probe_phiq_pair_knot_magic_shell.py`](../../../computations/probe_phiq_pair_knot_magic_shell.py)
- Line 155: [operator-selection LP dual](../../../computations/lp_dual_solver.py)
- Line 160: [brane-tower-z-habiro §"Pair-knot magic-shell probe"](#conj:brane-tower-z-habiro).
## knot-factor-spectral-summary.md
- Line 21: hand-fits in `computations/atomic_mass_pipeline.py`
## plancherel-weight-boundedness-interpretation.md
- Line 7: $q_0 = 1.109978595554181\ldots$ (50 dps) for $n = 12$ — so $\widetilde{w}$ is **not** a
## hoefsmit-ew-cell-content.md
- Line 236: Numerical comparison at $q_0 = 1.109978595554181\ldots$ (50 dps):
## bring-figure-eight-depth-2-witness.md
- Line 2: 50-digit numerical witness).**
- Line 20: ### Numerical witness (50-digit precision)
- Line 22: Computed via `mpmath.polylog` at `mp.dps = 50` (script
- Line 23: [`gb_depth_period_bring_fig8.py`](https://github.com/litlfred/qou/blob/main/computations/gb_depth_period_bring_fig8.py),
- Line 71: The keystone predicts analogous numerical witnesses at every depth:
## chi-lambda-w0-sign-weighting-proof.md
- Line 79: selects the same signed combination (numerical verification at
## explicit-alpha-k-h3.md
- Line 68: [`computations/alpha/alpha_k_jones_markov_h3.py`](#)
- Line 72: verified to numerical precision.
## meson-kaon-pion-hecke-seifert-proof.md
- Line 65: 2. **The numerical match to the PDG ratio** ($\approx 290$ ppm) is a
## weak-symmetric-normalization.md
- Line 19: > framing with N_sym(q_0) = 213.11 numerically pinned from
- Line 97: ### Numerical evaluation (for cross-checks)
- Line 99: At $q_0 \approx :val[q_0]{precision=6, witness=computations/q-pinning-50-digit.witness.json}$ (50 dps):
## atom-knot-mass-derivation.md
- Line 49: [Workplan 0b](../../../docs/audits/-workplan-0b-script-rewire-handoff.md)
- Line 51: $\rho_K$ closure; only its numerical instantiation is currently
- Line 87: naive numerical substitution of $\mathrm{Li}_2^q$ at $q = q_0$; the
- Line 111: [`probe-sdp-canonical-paper-formula.witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/computations/probe-sdp-canonical-paper-formula.witness.json):
- Line 314: - **Python prototypes** ([`gb_filtration_jet_tracker.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/gb_filtration_jet_tracker.py),
- Line 315: [`joint_tower_sdp_solver.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/joint_tower_sdp_solver.py),
- Line 316: [`joint_tower_sdp_solver_v2.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/joint_tower_sdp_solver_v2.py)) — design-spec
- Line 327: ### PSD-cone $\alpha^*$ ranking (Rust R5-minimal, $q_0 = 1.109978595554181\ldots$, 50 dps)
- Line 379: [`computations/r5_full_canonical_knot_solver.py`](https://github.com/litlfred/qou/blob/main/computations/r5_full_canonical_knot_solver.py)
- Line 400: [`probe-sdp-canonical-paper-formula.witness.json`](https://github.com/litlfred/qou/blob/main/computations/probe-sdp-canonical-paper-formula.witness.json),
- Line 407: [`joint_tower_sdp_solver_v2.py`](https://github.com/litlfred/qou/blob/main/computations/joint_tower_sdp_solver_v2.py).
## joint-galois-braid-action.md
- Line 83: **commute**. Numerical evidence: the orbit-sum
## option-e-isospin-test.md
- Line 3: [`rho_k_h3a_crystal.py`](../../../computations/rho_k_h3a_crystal.py)
- Line 22: $q_0 = 1.109978595554181\ldots$ (50 dps).  This is the structural Kashiwara weight on
- Line 26: The probe forms the $c_\lambda$-weighted observable
- Line 49: to canonical words.  The probe therefore tests the
- Line 56: [`option-e-isospin-probe.witness.json`](../../../computations/probes/option-e-isospin-probe.witness.json),
- Line 58: [`option_e_isospin_probe.py`](../../../computations/probes/option_e_isospin_probe.py).)*
- Line 137: [`rho_k_h3a_crystal.py`](../../../computations/rho_k_h3a_crystal.py)
- Line 142: [`rho_k_h3a_crystal.py`](../../../computations/rho_k_h3a_crystal.py)),
- Line 154: and re-run the isospin probe.  If $W_{c^{\mathrm{sym}}}(T) =
## wedderburn-mass-formula.md
- Line 54: (`atom_mass_partition.py`) computes all partitions exactly via
## calibration-inputs.md
- Line 37: > Numerically the Skein formula closes $m_\mu/m_e = 206.77$ at
- Line 96: production compute ([`derived_masses.py:e_0_full_mev`](https://github.com/litlfred/qou/blob/main/computations/derived_masses.py#L145)),
## alpha-em-categorical-trace.md
- Line 21: multiplicative q-rational family was ruled out by the 100-dps 54-element scan;
## derived-mass-formula-light-isotopes-proof.md
- Line 21: Numerical evaluation at $q_0 = 1.109978595554181\ldots$ (50 dps) uses
- Line 22: [`computations/derived_only_formula.py`](#)
- Line 39: `he3_tighten_pp.py`, `d_tighten_k3.py`, `he4_tighten_doubly_magic.py`),
## joint-tower-sdp-confinement.md
- Line 151: [`gb_filtration_jet_tracker.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/gb_filtration_jet_tracker.py).
## a8-partition-function-identity.md
- Line 69: - Empirical source: [`qbeta_habiro_recursion_probe.py`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/computations/probes/qbeta_habiro_recursion_probe.py)
- Line 75: **Mathematical Novelty:** This result records the numerical coincidence that the $a_8$ coefficients $(1,2,3,5,7)$ match the partition numbers $p(1..5)$. It is an empirical Habiro-shell observation rather than a new deductive argument, utilizing standard partition values, with the identity proved formally via ring equivalences.
## y-lambda-recipe-from-partition.md
- Line 38: Numerically at $q_0 \approx 1.110$: $X \approx 1.7203$.
- Line 148: ## Numerical sanity at $q_0 \approx 1.110$
- Line 188: [`computations/y_lambda_recipe_from_partition.py`](https://github.com/litlfred/qou/blob/main/computations/y_lambda_recipe_from_partition.py)
## mass-endomorphism-tower.md
- Line 103: *Numerical probe (`kashaev-integration-identity.witness.json`): the
- Line 108: identity does NOT hold numerically.*
- Line 126: parameters — but the integration probe shows the
- Line 152: [`canonical_plus_multibrane.py`](computations/canonical_plus_multibrane.py)
- Line 154: [`paper_six_term_isotope_sweep.py`](computations/sweeps/paper_six_term_isotope_sweep.py)
- Line 159: [`brane_tower_isospin_diagnosis.py`](computations/brane_tower_isospin_diagnosis.py)
- Line 195: `brane_tower_plancherel_scaffold.py` for a numerical scaffold; the
- Line 198: via `kahler_lift.py` (recursion-fixed).
- Line 229: (asymmetric $(q^n - 1)$ vs symmetric $[n]_q$).  Numerical probe
## terms-2-6-higher-operations.md
- Line 54: *Direct symbolic computation in `hochschild_h3.py`:*
- Line 120: `computations/deformation_cohomology_s3.py`:*
- Line 320: *Script `cup_product_tower_probe.py` tested the simplest proxy:
## mass-endomorphism-tower-proof.md
- Line 45: *Numerical verification: the integration value matches
## delta-max-uniform-bound.md
- Line 123: ## Numerical scale
- Line 160: For light atoms ($A \le 16$) at $q_0$, numerical evaluation
- Line 164: (cf. `computations/unified_lift.py` with
- Line 179: are subadditive), but the numerical prefactor degrades.
## wedderburn-bratteli-recursion-proof.md
- Line 33: [`y_lambda_bratteli_extract.py`](https://github.com/litlfred/qou/blob/main/computations/y_lambda_bratteli_extract.py)):
- Line 96: $q$ ([Geck--Pfeiffer]).  Sympy and numerical witness agree to
## gs-archimedean-agreement-residue.md
- Line 26: `habiro_coefficients_atomic.py` for $(Z=1, N=0,
- Line 31: computed by `term6_full_pole_sum.py` from the descended trace
- Line 59: *The numerical agreement is empirically certified to machine precision
## q-beta-bar-even-kernel-invariant.md
- Line 39: the bar-evenness check before the numerical anchor sweep runs*.
- Line 42: Before any numerical anchor sweep on a new candidate $F(q)$ / kernel
- Line 54: to the refuted-class map §2 and abort the numerical sweep.
## curvature-rank-gb-stratification-proof.md
- Line 58: [`computations/hecke_knot_ideal_tracker.py`](#) and
- Line 59: [`computations/knot_ideals_gb_jet_locations.py`](#)
## atom-knot-mass-derivation-table2-data.md
- Line 4: | 1b (GB-filtration certificate) | Python `gb_filtration_jet_tracker.py` (PoC) + Rust `gb_nf_reducer.rs` (R2; 6 unit tests; bit-for-bit match) | ✓ |
- Line 9: | 2 (Markov trace symbolic) | [`y_lambda_wenzl_bridge_extended.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/y_lambda_wenzl_bridge_extended.py) + [`q_mn_recursive_memoized.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/q_mn_recursive_memoized.py) | ✓ for $n \leq 12$ |
- Line 12: | 5 (Archimedean realization at $q_0$ + $m_e$) | MPFR via SymPy/mpmath | ✓ |
- Line 13: | 6 (AME comparison) | mass-table-ppb witness + [`recursive_atom_knot_atlas_render.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/recursive_atom_knot_atlas_render.py) | ✓ |
