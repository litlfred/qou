/**
 * Witnessed-value registry — single source of truth for numerical
 * values quoted in paper prose.
 *
 * Author guidance lives in `.claude/skills/local/witnessed-values.md`.
 *
 * Each registry entry maps a short, stable `name` (e.g. `q_0`,
 * `m_n_MeV`) to the canonical witness JSON file and the dotted path
 * within it that holds the current value.  Markdown content cites
 * the entry via the `:val[name]` directive (see render-latex.ts);
 * the build pipeline substitutes the live witness value at render
 * time, so the paper cannot drift away from its computations.
 *
 * Adding a new entry:
 *   1. Identify the canonical witness JSON the value should track
 *      (look in `computations/*.witness.json`).
 *   2. Pick a stable, snake-case name (mirror the symbol when
 *      possible — `q_0`, `m_n_MeV`, `inv_alpha`).
 *   3. Set `defaultPrecision` no larger than the underlying witness
 *      precision (`dps` for PrecisionScalar, count of significant
 *      digits otherwise).  Authors can request fewer digits per
 *      occurrence via `:val[name]{precision=N}`.
 *   4. `units` is rendered after the number as plain text (e.g.
 *      `MeV`, `\\text{MeV}`).  Use `null` for dimensionless values.
 *   5. If the canonical witness is not yet identified, set
 *      `needsReview: true` and provide a placeholder `witnessFile`
 *      pointing at the closest existing witness.  The codemod skips
 *      such entries and the validator emits a warning (not an error).
 *
 * All paths are repo-root relative.
 *
 * @module content/values/registry
 */

/** Default rendering format for a witnessed value occurrence. */
export type WitnessedValueFormat = "decimal" | "scientific" | "measured";

/** A single registered witnessed value. */
export interface WitnessedValueEntry {
  /** Short stable identifier — used in `:val[name]`. snake_case. */
  readonly name: string;
  /** Human-readable description of what the value represents. */
  readonly description: string;
  /** Canonical TeX symbol — used in commentary, not for rendering. */
  readonly symbol: string;
  /** Repo-root-relative path to the canonical witness JSON. */
  readonly witnessFile: string;
  /**
   * Dotted JSON path inside the witness file.  Each segment is a
   * literal key; numeric segments index arrays.  Example:
   * `derived_50_digit.q` or `result.0.B_MeV`.
   */
  readonly witnessPath: string;
  /**
   * Default number of significant decimal digits to render when no
   * `precision=` attribute is supplied on the directive.  Must not
   * exceed the underlying witness precision.
   */
  readonly defaultPrecision: number;
  /**
   * Units rendered immediately after the number, separated by a
   * non-breaking space.  Plain text — no math delimiters.  Example:
   * `MeV`, `fm`, `s^{-1}`.  `null` for dimensionless values.
   */
  readonly units: string | null;
  /**
   * Optional sibling registry entry holding the symmetric uncertainty
   * (one-sigma).  Rendered as `value ± err units` when the directive
   * carries `format=measured`.
   */
  readonly errorEntry?: string;
  /**
   * Default rendering format when the directive does not specify one.
   * Defaults to "decimal".
   */
  readonly format?: WitnessedValueFormat;
  /**
   * If true, this entry is a name reservation only — its
   * `witnessFile`/`witnessPath` have not been confirmed by the repo
   * owner.  The codemod skips entries with `needsReview: true`, and
   * the validator downgrades resolution failures from error to
   * warning.  Resolve by verifying the canonical witness and
   * removing the flag.
   */
  readonly needsReview?: boolean;
}

/**
 * Authoritative registry.  Keys mirror `entry.name` for fast lookup
 * by the renderer; `Object.freeze` keeps the table immutable at
 * runtime so accidental mutation in hot reload cannot corrupt the
 * source of truth.
 *
 * Entries are grouped by witness file for auditability — every
 * entry whose `witnessFile` points at the same JSON tracks a
 * coherent computation, so a single witness update propagates
 * atomically to every value in its group.
 */
export const WITNESSED_VALUES: Readonly<Record<string, WitnessedValueEntry>> =
  Object.freeze({
    // ── q-pinning (50-digit, mpmath) ────────────────────────────
    // The most-cited witness in the paper.  Every value below is
    // backed by the same JSON file and was derived from Vol(4_1)
    // and CODATA m_μ/m_e in a single mpmath run.

    q_0: Object.freeze({
      name: "q_0",
      description:
        "Substrate parameter, derived from Vol(4_1) and CODATA m_μ/m_e.",
      symbol: "q_0",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.q",
      defaultPrecision: 4,
      units: null,
    }),

    q_inv: Object.freeze({
      name: "q_inv",
      description: "Reciprocal substrate parameter q_0^{-1}.",
      symbol: "q_0^{-1}",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.q_inv",
      defaultPrecision: 4,
      units: null,
    }),

    // ── CO bond-order active-set probe (orthogonal-channel binding) ──
    sigma_channel_eV: Object.freeze({
      name: "sigma_channel_eV",
      description:
        "Binding of one orthogonal covalent channel (the bound σ pair) " +
        "of CO, from the bond-order active-set probe.",
      symbol: "b_\\sigma",
      witnessFile:
        "computations/co-bond-order-active-set.witness.json",
      witnessPath: "data.sigma_channel_eV",
      defaultPrecision: 4,
      units: "eV",
    }),

    observed_D0_CO_eV: Object.freeze({
      name: "observed_D0_CO_eV",
      description:
        "Observed CO bond dissociation energy D_0(CO) — experimental " +
        "reference for the bond-order active-set probe.",
      symbol: "D_0(\\mathrm{CO})",
      witnessFile:
        "computations/co-bond-order-active-set.witness.json",
      witnessPath: "data.observed_D0_CO_eV",
      defaultPrecision: 4,
      units: "eV",
    }),

    // ── Molecular experimental comparison refs (organic-chem WS-B B1) ──
    d0_co2_double_ev: Object.freeze({
      name: "d0_co2_double_ev",
      description:
        "Observed CO₂ C=O double-bond comparison energy (per-bond reference).",
      symbol: "D_0(\\mathrm{CO_2})",
      witnessFile:
        "computations/molecular-experimental-refs.witness.json",
      witnessPath: "data.d0_co2_double_ev",
      defaultPrecision: 3,
      units: "eV",
    }),

    d0_h2_ev: Object.freeze({
      name: "d0_h2_ev",
      description:
        "Observed H₂ bond dissociation energy D_0(H₂) — experimental reference.",
      symbol: "D_0(\\mathrm{H_2})",
      witnessFile:
        "computations/molecular-experimental-refs.witness.json",
      witnessPath: "data.d0_h2_ev",
      defaultPrecision: 4,
      units: "eV",
    }),

    d0_cc_ev: Object.freeze({
      name: "d0_cc_ev",
      description:
        "Observed C–C single-bond dissociation energy — experimental reference.",
      symbol: "D_0(\\mathrm{C\\text{-}C})",
      witnessFile:
        "computations/molecular-experimental-refs.witness.json",
      witnessPath: "data.d0_cc_ev",
      defaultPrecision: 3,
      units: "eV",
    }),

    bond_len_benzene_ang: Object.freeze({
      name: "bond_len_benzene_ang",
      description: "Observed benzene aromatic C–C bond length.",
      symbol: "r_{\\mathrm{C-C}}^{\\mathrm{benzene}}",
      witnessFile:
        "computations/molecular-experimental-refs.witness.json",
      witnessPath: "data.bond_len_benzene_ang",
      defaultPrecision: 3,
      units: "Å",
    }),

    bond_len_cc_single_ang: Object.freeze({
      name: "bond_len_cc_single_ang",
      description: "C–C single-bond length reference.",
      symbol: "r_{\\mathrm{C-C}}^{\\mathrm{single}}",
      witnessFile:
        "computations/molecular-experimental-refs.witness.json",
      witnessPath: "data.bond_len_cc_single_ang",
      defaultPrecision: 3,
      units: "Å",
    }),

    bond_len_cc_double_ang: Object.freeze({
      name: "bond_len_cc_double_ang",
      description: "C=C double-bond length reference.",
      symbol: "r_{\\mathrm{C=C}}^{\\mathrm{double}}",
      witnessFile:
        "computations/molecular-experimental-refs.witness.json",
      witnessPath: "data.bond_len_cc_double_ang",
      defaultPrecision: 3,
      units: "Å",
    }),

    benzene_resonance_kcal: Object.freeze({
      name: "benzene_resonance_kcal",
      description: "Observed benzene resonance (delocalization) energy.",
      symbol: "E_{\\mathrm{res}}^{\\mathrm{benzene}}",
      witnessFile:
        "computations/molecular-experimental-refs.witness.json",
      witnessPath: "data.benzene_resonance_kcal",
      defaultPrecision: 2,
      units: "kcal/mol",
    }),

    // ── Predicted bond angles (braid-weight VSEPR master table) ────────
    predicted_ch4_deg: Object.freeze({
      name: "predicted_ch4_deg",
      description: "Predicted CH₄ H–C–H angle (braid-weight VSEPR, no fit).",
      symbol: "\\theta_{\\mathrm{CH_4}}",
      witnessFile:
        "computations/molecular-angle-master-table.witness.json",
      witnessPath: "data.table.CH4.predicted_deg",
      defaultPrecision: 5,
      units: "deg",
    }),
    predicted_nh3_deg: Object.freeze({
      name: "predicted_nh3_deg",
      description: "Predicted NH₃ H–N–H angle (braid-weight VSEPR, no fit).",
      symbol: "\\theta_{\\mathrm{NH_3}}",
      witnessFile:
        "computations/molecular-angle-master-table.witness.json",
      witnessPath: "data.table.NH3.predicted_deg",
      defaultPrecision: 5,
      units: "deg",
    }),
    predicted_h2o_deg: Object.freeze({
      name: "predicted_h2o_deg",
      description: "Predicted H₂O H–O–H angle (braid-weight VSEPR, no fit).",
      symbol: "\\theta_{\\mathrm{H_2O}}",
      witnessFile:
        "computations/molecular-angle-master-table.witness.json",
      witnessPath: "data.table.H2O.predicted_deg",
      defaultPrecision: 5,
      units: "deg",
    }),
    predicted_c2h4_deg: Object.freeze({
      name: "predicted_c2h4_deg",
      description: "Predicted C₂H₄ H–C–H angle (braid-weight VSEPR, no fit).",
      symbol: "\\theta_{\\mathrm{C_2H_4}}",
      witnessFile:
        "computations/molecular-angle-master-table.witness.json",
      witnessPath: "data.table.C2H4.predicted_deg",
      defaultPrecision: 5,
      units: "deg",
    }),
    predicted_co2_deg: Object.freeze({
      name: "predicted_co2_deg",
      description: "Predicted CO₂ O–C–O angle (linear, braid-weight VSEPR).",
      symbol: "\\theta_{\\mathrm{CO_2}}",
      witnessFile:
        "computations/molecular-angle-master-table.witness.json",
      witnessPath: "data.table.CO2.predicted_deg",
      defaultPrecision: 5,
      units: "deg",
    }),
    predicted_h2s_deg: Object.freeze({
      name: "predicted_h2s_deg",
      description:
        "Predicted H₂S H–S–H angle (pure-p base, braid-weight VSEPR).",
      symbol: "\\theta_{\\mathrm{H_2S}}",
      witnessFile:
        "computations/molecular-angle-master-table.witness.json",
      witnessPath: "data.table.H2S.predicted_deg",
      defaultPrecision: 5,
      units: "deg",
    }),

    // ── Bring trefoil + cinquefoil channel (H₂S 1/√5 geometry) ─────────
    bring_g_trefoil: Object.freeze({
      name: "bring_g_trefoil",
      description:
        "Seifert genus of the trefoil T_{2,3} (the chiral channel) in Σ₄.",
      symbol: "g(T_{2,3})",
      witnessFile:
        "computations/bring-trefoil-cinquefoil-channel.witness.json",
      witnessPath: "data.g_trefoil_chiral_channel",
      defaultPrecision: 0,
      units: null,
    }),
    bring_g_cinquefoil: Object.freeze({
      name: "bring_g_cinquefoil",
      description:
        "Seifert genus of the cinquefoil T_{2,5} (the ζ₅ carrier) in Σ₄.",
      symbol: "g(T_{2,5})",
      witnessFile:
        "computations/bring-trefoil-cinquefoil-channel.witness.json",
      witnessPath: "data.g_cinquefoil_zeta5",
      defaultPrecision: 0,
      units: null,
    }),
    bring_sigma4_genus: Object.freeze({
      name: "bring_sigma4_genus",
      description: "Genus of Bring's Seifert fibre Σ₄ (both knots embed: ≤ 4).",
      symbol: "g(\\Sigma_4)",
      witnessFile:
        "computations/bring-trefoil-cinquefoil-channel.witness.json",
      witnessPath: "data.brings_genus_sigma4",
      defaultPrecision: 0,
      units: null,
    }),
    bring_gauss_sum_sqrt5: Object.freeze({
      name: "bring_gauss_sum_sqrt5",
      description:
        "Quadratic Gauss sum over the cinquefoil's ℤ₅-orbit, g = Σ ζ₅^{k²} = √5.",
      symbol: "\\textstyle\\sum_k \\zeta_5^{k^2}",
      witnessFile:
        "computations/bring-trefoil-cinquefoil-channel.witness.json",
      witnessPath: "data.gauss_sum",
      defaultPrecision: 5,
      units: null,
    }),
    bring_inv_sqrt5: Object.freeze({
      name: "bring_inv_sqrt5",
      description:
        "The Bring constant 1/√5 — leading chiral coefficient of the H₂S residual.",
      symbol: "1/\\sqrt5",
      witnessFile:
        "computations/bring-trefoil-cinquefoil-channel.witness.json",
      witnessPath: "data.inv_sqrt5_bring",
      defaultPrecision: 5,
      units: null,
    }),

    // ── Hydrogen-bond cohesion / phase transitions (q-PV=nRT temperature) ──
    hbond_h_squared: Object.freeze({
      name: "hbond_h_squared",
      description:
        "h² = (q₀−q₀⁻¹)² — the predicted H-bond/covalent energy ratio (~0.044).",
      symbol: "h^2",
      witnessFile:
        "computations/hbond-categorical-action.witness.json",
      witnessPath: "data.h_squared_hbond_ratio",
      defaultPrecision: 4,
      units: null,
    }),
    hbond_h2o_L_pred: Object.freeze({
      name: "hbond_h2o_L_pred",
      description:
        "Predicted H₂O latent heat = 2·h²·E_OH (no fit), kJ/mol.",
      symbol: "L_{\\mathrm{H_2O}}^{\\mathrm{pred}}",
      witnessFile:
        "computations/hbond-categorical-action.witness.json",
      witnessPath: "data.H2O_L_pred_kJmol",
      defaultPrecision: 1,
      units: "kJ/mol",
    }),
    hbond_h2o_err_pct: Object.freeze({
      name: "hbond_h2o_err_pct",
      description:
        "H₂O latent-heat prediction error vs measured 40.66 kJ/mol (no fit), %.",
      symbol: "\\varepsilon_{\\mathrm{H_2O}}",
      witnessFile:
        "computations/hbond-categorical-action.witness.json",
      witnessPath: "data.H2O_err_pct",
      defaultPrecision: 1,
      units: "%",
    }),

    // ── van der Waals = Hopf symmetric block (operator-selection SDP) ──
    vdw_sigma1sq_pct_symmetric: Object.freeze({
      name: "vdw_sigma1sq_pct_symmetric",
      description:
        "Symmetric-block fraction q²/(q²+q⁻²) of the Hopf link σ₁² (vdW-dominated).",
      symbol: "q^2/(q^2+q^{-2})",
      witnessFile:
        "computations/hbond-vdw-sdp.witness.json",
      witnessPath: "data.sigma1sq_pct_symmetric",
      defaultPrecision: 1,
      units: "%",
    }),
    vdw_e_plus_qdim: Object.freeze({
      name: "vdw_e_plus_qdim",
      description:
        "Markov q-dimension of the symmetric block e₊ (the van der Waals channel).",
      symbol: "\\mathrm{tr}_M(e_+)",
      witnessFile:
        "computations/hbond-vdw-sdp.witness.json",
      witnessPath: "data.tr_M_e_plus_symmetric_vdw",
      defaultPrecision: 3,
      units: null,
    }),

    vdw_cosh_2lambda: Object.freeze({
      name: "vdw_cosh_2lambda",
      description:
        "cosh(2λ)=(q²+q⁻²)/2 — the retained bar-even carrier of the Hopf link.",
      symbol: "\cosh 2\lambda",
      witnessFile:
        "computations/vdw-pskew-sinh-probe.witness.json",
      witnessPath: "data.cosh_2lambda",
      defaultPrecision: 5,
      units: null,
    }),
    vdw_bar_odd_residual: Object.freeze({
      name: "vdw_bar_odd_residual",
      description:
        "The van der Waals bar-odd residual sinh(2λ)·(e₊−e₋) (P_skew channel, exact).",
      symbol: "\sinh(2\lambda)(e_+-e_-)",
      witnessFile:
        "computations/vdw-pskew-sinh-probe.witness.json",
      witnessPath: "data.vdw_bar_odd_residual",
      defaultPrecision: 5,
      units: null,
    }),

    H_A: Object.freeze({
      name: "H_A",
      description: "Planck constant ℏ_q = q - q^{-1} at the substrate.",
      symbol: "H_A",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.H_A",
      defaultPrecision: 4,
      units: null,
    }),

    hbar_q: Object.freeze({
      name: "hbar_q",
      description: "Categorical Planck constant ℏ_q = (q-1)/q.",
      symbol: "\\hbar_q",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.hbar_q",
      defaultPrecision: 4,
      units: null,
    }),

    hbar_q_sq: Object.freeze({
      name: "hbar_q_sq",
      description: "Squared Planck constant ℏ_q^2 — denominator of ξ(q).",
      symbol: "\\hbar_q^{2}",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.hbar_q_sq",
      defaultPrecision: 4,
      units: null,
    }),

    two_q: Object.freeze({
      name: "two_q",
      description: "Quantum integer [2]_q = q + q^{-1}.",
      symbol: "[2]_q",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.two_q",
      defaultPrecision: 4,
      units: null,
    }),

    qint_3: Object.freeze({
      name: "qint_3",
      description: "Quantum integer [3]_q.",
      symbol: "[3]_q",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      witnessPath: "quantum_integers.[3]_q",
      defaultPrecision: 4,
      units: null,
    }),

    qint_4: Object.freeze({
      name: "qint_4",
      description: "Quantum integer [4]_q.",
      symbol: "[4]_q",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      witnessPath: "quantum_integers.[4]_q",
      defaultPrecision: 4,
      units: null,
    }),

    qint_5: Object.freeze({
      name: "qint_5",
      description: "Quantum integer [5]_q.",
      symbol: "[5]_q",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      witnessPath: "quantum_integers.[5]_q",
      defaultPrecision: 4,
      units: null,
    }),

    z_markov: Object.freeze({
      name: "z_markov",
      description: "Markov parameter z = 1/(q^{1/2} + q^{-1/2}).",
      symbol: "z",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.z_markov",
      defaultPrecision: 4,
      units: null,
    }),

    rho_q: Object.freeze({
      name: "rho_q",
      description: "Hecke trace density ρ_q.",
      symbol: "\\rho_q",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.rho_q",
      defaultPrecision: 4,
      units: null,
    }),

    s_skein: Object.freeze({
      name: "s_skein",
      description: "Skein normalisation s = z · (q - q^{-1}).",
      symbol: "s",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.s_skein",
      defaultPrecision: 4,
      units: null,
    }),

    codata_rel_unc: Object.freeze({
      name: "codata_rel_unc",
      description:
        "CODATA relative uncertainty on m_μ/m_e — bounds physical anchoring of q_0.",
      symbol: "\\sigma(q_0)/q_0",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      witnessPath: "physical_anchoring_bound.codata_relative_uncertainty",
      defaultPrecision: 3,
      units: null,
      format: "scientific",
    }),

    Vol_4_1: Object.freeze({
      name: "Vol_4_1",
      description: "Hyperbolic volume of the figure-eight knot 4_1.",
      symbol: "\\mathrm{Vol}(4_1)",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      // The witness JSON exposes the 50-digit value as a string under
      // `..._str`, with a parallel f64 mirror at `..._float`.  We
      // dereference the string field to preserve full precision.
      witnessPath: "calibration_inputs.Vol_4_1_str",
      defaultPrecision: 6,
      units: null,
    }),

    m_mu_over_e: Object.freeze({
      name: "m_mu_over_e",
      description: "CODATA muon-electron mass ratio (calibration input).",
      symbol: "m_\\mu/m_e",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      witnessPath: "calibration_inputs.m_mu_over_e_str",
      defaultPrecision: 7,
      units: null,
    }),

    // ── Binding energies (canonical mass tables) ────────────────
    // Verified against the canonical-mass-table and 4He pipelines.

    B_4He_AME_MeV: Object.freeze({
      name: "B_4He_AME_MeV",
      description: "AME experimental binding energy of 4He (helium-4).",
      symbol: "B_{\\mathrm{AME}}({}^4\\mathrm{He})",
      witnessFile:
        "computations/4he-binding-full-pipeline.witness.json",
      witnessPath: "B_AME_MeV",
      defaultPrecision: 6,
      units: "MeV",
    }),

    // NOTE: `data.rows.2` indexes the deuteron row. The row order
    // in `canonical-mass-table-extended.witness.json` is fixed by
    // DEFAULT_ATOMS in canonical_mass_table_extended.py and must
    // not be reordered (proton=0, neutron=1, D=2, T=3, ³He=4,
    // ⁴He=5, ⁵Li=6, ⁶Li=7). A (Z, N)-keyed lookup is the long-term
    // fix; tracked as a follow-up. See Gemini #781 review.
    B_2H_AME_MeV: Object.freeze({
      name: "B_2H_AME_MeV",
      description: "AME experimental binding energy of deuterium (2H).",
      symbol: "B_{\\mathrm{AME}}(\\mathrm{D})",
      witnessFile:
        "computations/canonical-mass-table-extended.witness.json",
      witnessPath: "data.rows.2.B_AME_MeV",
      defaultPrecision: 5,
      units: "MeV",
    }),

    // ── Pending entries (needsReview) ───────────────────────────
    // Reserved names whose canonical witness has not been confirmed
    // by the repo owner.  Codemod skips these; validator emits a
    // warning if they appear in `.md` content.
    //
    // Resolve by:
    //   1. Identifying the canonical witness file + dotted path
    //   2. Verifying the value matches paper prose
    //   3. Removing the `needsReview: true` flag
    //
    // The placeholder `witnessFile`/`witnessPath` point at the
    // closest existing witness so resolution does not crash; do not
    // rely on the placeholder values.

    m_p_MeV: Object.freeze({
      name: "m_p_MeV",
      description:
        "Proton rest mass in MeV/c^2.  CODATA 2022 value " +
        "938.27208816 MeV, re-exported from codata_constants.py " +
        "via the codata-masses witness.",
      symbol: "m_p",
      witnessFile:
        "computations/codata-masses.witness.json",
      witnessPath: "data.m_p_MeV",
      defaultPrecision: 11,
      units: "MeV",
    }),

    m_n_MeV: Object.freeze({
      name: "m_n_MeV",
      description:
        "Neutron rest mass in MeV/c^2.  CODATA 2022 + AME 2020 " +
        "value 939.56542052 MeV, re-exported from " +
        "codata_constants.py via the codata-masses witness.",
      symbol: "m_n",
      witnessFile:
        "computations/codata-masses.witness.json",
      witnessPath: "data.m_n_MeV",
      defaultPrecision: 11,
      units: "MeV",
    }),

    m_e_MeV: Object.freeze({
      name: "m_e_MeV",
      description:
        "Electron rest mass in MeV/c^2.  CODATA 2022 value " +
        "0.51099895 MeV, re-exported from codata_constants.py " +
        "via the codata-masses witness.",
      symbol: "m_e",
      witnessFile:
        "computations/codata-masses.witness.json",
      witnessPath: "data.m_e_MeV",
      defaultPrecision: 8,
      units: "MeV",
    }),

    E_0_N0_MeV: Object.freeze({
      name: "E_0_N0_MeV",
      description:
        "Single Planck-tick (N=0) hadronic energy scale " +
        "E_0^(N=0) = m_e / (q_0 (q_0 - 1)) ≈ 4.186 MeV.  Framework-" +
        "derived from CAL-1 (m_e) and CAL-2 (q_0) alone; no CAL-3 input.",
      symbol: "\\mathbf{E}_0^{(N=0)}",
      witnessFile:
        "computations/q-beta-form-a-n1-extension.witness.json",
      witnessPath: "data.E0_N0_MeV_50dps",
      defaultPrecision: 6,
      units: "MeV",
    }),

    E_0_full_MeV: Object.freeze({
      name: "E_0_full_MeV",
      description:
        "Tower-summed (N → ∞) hadronic energy scale " +
        "E_0^full = E_0^(N=0) / (1 - ℏ_q²) ≈ 4.228 MeV.  Geometric " +
        "brane-tower closed form; framework-derived from CAL-1 + CAL-2.  " +
        "Note: currently overshoots E_0^(cal) by +1.75% — the geometric-" +
        "series direction is an open finding pending categorical Li_2^q " +
        "derivation review (conj:alpha-k-categorical-closure).",
      symbol: "\\mathbf{E}_0^{\\text{full}}",
      witnessFile:
        "computations/q-beta-form-a-n1-extension.witness.json",
      witnessPath: "data.E0_full_MeV_50dps",
      defaultPrecision: 6,
      units: "MeV",
    }),

    E_0_full_li2q_MeV: Object.freeze({
      name: "E_0_full_li2q_MeV",
      description:
        "Substrate symmetric q-dilogarithm tower form, candidate " +
        "closure for conj:alpha-k-categorical-closure: " +
        "E_0^(full,Li2q) = E_0^(N=0) · (1 + (-Li_2^q(-ℏ_q²))) ≈ 4.227 MeV. " +
        "Bounded analog of the geometric series form. At the substrate " +
        "level (no atom), agrees with geometric to 0.012% — both " +
        "overshoot E_0^(cal) by ~1.74%. Per-atom Li_2^q evaluations " +
        "(prop:mass-endomorphism-tower) require braid input.",
      symbol: "\\mathbf{E}_0^{\\text{full},\\mathrm{Li}_2^q}",
      witnessFile:
        "computations/q-beta-form-a-n1-extension.witness.json",
      witnessPath: "data.E0_full_li2q_MeV_50dps",
      defaultPrecision: 6,
      units: "MeV",
    }),

    E_0_calibrated_MeV: Object.freeze({
      name: "E_0_calibrated_MeV",
      description:
        "Symbolic CODATA-calibrated hadronic energy scale " +
        "E_0^(cal) = Q_β(n) / |h(h-2)/2| ≈ 4.179 MeV using the symbolic " +
        "single-wrap Δ(net) = h(h-2)/2 (closed-form, no typed-crossings " +
        "noise).  Distinct from the typed-crossings value 4.155 MeV " +
        "computed by `derived_masses.e_0_calibrated_mev()` (which loads " +
        "Δ(net) = -0.18829 from beta-decay-energy-scale.witness.json — " +
        "a 6-term decomposition that picks up finite-size noise).  The " +
        "0.6% typed-vs-symbolic gap is itself a recorded finding.",
      symbol: "\\mathbf{E}_0^{(\\text{cal})}",
      witnessFile:
        "computations/q-beta-form-a-n1-extension.witness.json",
      witnessPath: "data.E0_calibrated_MeV_50dps",
      defaultPrecision: 6,
      units: "MeV",
    }),

    inv_alpha: Object.freeze({
      name: "inv_alpha",
      description:
        "Inverse fine-structure constant 1/α (CODATA).  Canonical witness pending.",
      symbol: "\\alpha^{-1}",
      witnessFile:
        "computations/alpha/alpha-high-precision.witness.json",
      witnessPath: "computation",
      defaultPrecision: 6,
      units: null,
      needsReview: true,
    }),

    c_q: Object.freeze({
      name: "c_q",
      description:
        "Categorical speed of light c_q = 1/(q-1).  Canonical witness pending — derive from q-pinning.",
      symbol: "c_q",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.q",
      defaultPrecision: 4,
      units: null,
      needsReview: true,
    }),

    eta_q: Object.freeze({
      name: "eta_q",
      description:
        "Operational entropy η_q = (2q-1)/q^3.  Canonical witness pending.",
      symbol: "\\eta_q",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.q",
      defaultPrecision: 4,
      units: null,
      needsReview: true,
    }),

    chi_q: Object.freeze({
      name: "chi_q",
      description:
        "q-deformed Lyapunov exponent χ_q = 1/(2q-1).  Canonical witness pending.",
      symbol: "\\chi_q",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.q",
      defaultPrecision: 4,
      units: null,
      needsReview: true,
    }),

    d_H: Object.freeze({
      name: "d_H",
      description:
        "Hausdorff dimension d_H(q) = (2q-1)^2/q^3.  Canonical witness pending.",
      symbol: "d_H",
      witnessFile:
        "computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.q",
      defaultPrecision: 4,
      units: null,
      needsReview: true,
    }),

    // ── Hyperbolic volumes (encounter chapter) ──────────────────
    // Vol(4_1) computed via the Clausen-function identity
    // 2 · Cl_2(π/3) at 50 dps in `hyperbolic_volumes.py`; the
    // 15-digit serialisation feeds the Lean literal
    // `MostowRigidity.figureEight.volume` via the
    // `:leanval[Vol_4_1]{precision=15}` tag and the
    // `codemod-leanval.ts` codemod.  (Note: the registered name is
    // `Vol_4_1` — uppercase — registered earlier in this file.)

    // Vol_4_1 (uppercase) is registered above pointing at the
    // canonical q-pinning witness; consume that entry for the
    // figure-eight volume.  The hyperbolic-volumes witness retains
    // a parallel `data.vol_4_1_decimal_15` field for self-tests
    // and for cross-validating against the q-pinning value, but
    // the Lean tag uses :leanval[Vol_4_1]{precision=15}.

    vol_4_1_decimal_50: Object.freeze({
      name: "vol_4_1_decimal_50",
      description:
        "Hyperbolic volume of the figure-eight knot complement " +
        "Vol(4_1) = 2 Cl_2(π/3) at 50-digit precision.",
      symbol: "\\mathrm{Vol}(4_1)",
      witnessFile:
        "computations/hyperbolic-volumes.witness.json",
      witnessPath: "data.vol_4_1_decimal_50",
      unit: "",
    }),

    vol_5_2: Object.freeze({
      name: "vol_5_2",
      description:
        "Hyperbolic volume of the 5_2 knot complement " +
        "Vol(5_2) ≈ 2.82812 (SnapPy ManifoldHP 3.3.2, 50 dps, " +
        "2026-06-12; Adams-Hildebrand-Weeks 1991). " +
        "Second-smallest known orientable cusped hyperbolic " +
        "knot-complement volume.",
      symbol: "\\mathrm{Vol}(5_2)",
      witnessFile:
        "computations/hyperbolic-volumes.witness.json",
      witnessPath: "data.vol_5_2_decimal_15",
      defaultPrecision: 15,
      units: null,
    }),

    mostow_gap_4_1: Object.freeze({
      name: "mostow_gap_4_1",
      description:
        "Conservative lower bound on the volume gap " +
        "Vol(5_2) - Vol(4_1) ≈ 0.798; consumed by " +
        "MostowRigidity.figureEight.mostow_gap. " +
        "Deliberately coarse (0.5); the precise gap is " +
        "gap_5_2_minus_4_1_15 in the same witness.",
      symbol: "\\Delta_{\\mathrm{Mostow}}(4_1)",
      witnessFile:
        "computations/hyperbolic-volumes.witness.json",
      witnessPath: "data.gap_lower_bound",
      defaultPrecision: 1,
      units: null,
    }),

    // ── Frobenius Gram matrix / NF basis (H_3) ──────────────────
    // Backed by the rebuilt TR_M[5] Markov trace.  Witnesses
    // regenerated 2026-05-19 after the pyhecke.gram bug fix.

    gram_h: Object.freeze({
      name: "gram_h",
      description:
        "Hecke parameter h = q - q^{-1} = HA at q_0 — substrate Hecke-algebra structure constant.",
      symbol: "h",
      witnessFile:
        "computations/gram-matrix-dual.witness.json",
      witnessPath: "parameters.HA",
      defaultPrecision: 5,
      units: null,
    }),

    gram_z: Object.freeze({
      name: "gram_z",
      description:
        "Markov parameter z = 1/(q^{1/2} + q^{-1/2}) at q_0 — Gram-matrix entry tr_M(σ_0) = tr_M(σ_1).",
      symbol: "z",
      witnessFile:
        "computations/gram-matrix-dual.witness.json",
      witnessPath: "parameters.z",
      defaultPrecision: 5,
      units: null,
    }),

    gram_z_sq: Object.freeze({
      name: "gram_z_sq",
      description:
        "Markov trace z^2 of L_± = σ_0σ_1 / σ_1σ_0 at q_0.",
      symbol: "z^2",
      witnessFile:
        "computations/gram-matrix-dual.witness.json",
      witnessPath: "markov_trace_basis.L₊",
      defaultPrecision: 5,
      units: null,
    }),

    gram_tr_M_e_minus: Object.freeze({
      name: "gram_tr_M_e_minus",
      description:
        "Markov trace of e^- = σ_0σ_1σ_0 at q_0: tr_M(e^-) = h·z² + z (post-2026-05-19 TR_M[5] fix per docs/audits/2026-05-19-trm5-markov-bug.md). The earlier z^3 value was a bug.",
      symbol: "h \\cdot z^2 + z",
      witnessFile:
        "computations/gram-matrix-dual.witness.json",
      witnessPath: "markov_trace_basis.e⁻",
      defaultPrecision: 5,
      units: null,
    }),

    gram_det: Object.freeze({
      name: "gram_det",
      description:
        "Determinant of the 6×6 NF Gram matrix at q_0 (post TR_M[5] fix).",
      symbol: "\\det G",
      witnessFile:
        "computations/confinement-operator-selection.witness.json",
      witnessPath: "gram_det",
      defaultPrecision: 4,
      units: null,
    }),

    // ── Confinement operator selection (B_3 ranking) ────────────

    confinement_B3_net_proton: Object.freeze({
      name: "confinement_B3_net_proton",
      description:
        "Net constraint net(B_3 · uud) at q_0 — selects the Borromean operator as the unique confinement choice.",
      symbol: "\\mathrm{net}(\\mathcal{B}_3 \\cdot uud)",
      witnessFile:
        "computations/confinement-operator-selection.witness.json",
      witnessPath: "candidates.proton.B₃ = (σ₀σ₁⁻¹)³.net",
      defaultPrecision: 4,
      units: null,
    }),

    confinement_Lplus_net_proton: Object.freeze({
      name: "confinement_Lplus_net_proton",
      description:
        "Net constraint net(L_+ · uud) at q_0 — runner-up in candidate-operator ranking (no confinement, mesonic pairing).",
      symbol: "\\mathrm{net}(L_+ \\cdot uud)",
      witnessFile:
        "computations/confinement-operator-selection.witness.json",
      witnessPath: "candidates.proton.L₊ = σ₀σ₁.net",
      defaultPrecision: 4,
      units: null,
    }),

    confinement_id_net_proton: Object.freeze({
      name: "confinement_id_net_proton",
      description:
        "Net constraint net(𝟙 · uud) for the unconfined (identity) candidate at q_0.",
      symbol: "\\mathrm{net}(\\mathbf{1} \\cdot uud)",
      witnessFile:
        "computations/confinement-operator-selection.witness.json",
      witnessPath: "candidates.proton.𝟏 (identity, no binding).net",
      defaultPrecision: 4,
      units: null,
    }),

    // ── Molecular Frobenius LP (covalent bond derivation) ───────

    E_mol_eV: Object.freeze({
      name: "E_mol_eV",
      description:
        "Per-crossing molecular energy scale E_mol = m_e · q^{-5} (eV) at q_0 — input parameter to molecular Frobenius LP.",
      symbol: "\\mathbf{E}_{\\mathrm{mol}}",
      witnessFile:
        "computations/molecular-frobenius-lp.witness.json",
      witnessPath: "parameters.E_mol_eV",
      defaultPrecision: 4,
      units: "eV",
    }),
  });

/** Return the entry registered under `name`, or `undefined`. */
export function lookupValue(name: string): WitnessedValueEntry | undefined {
  return WITNESSED_VALUES[name];
}

/** Iterate over all registered names — useful for validation. */
export function registeredNames(): readonly string[] {
  return Object.freeze(Object.keys(WITNESSED_VALUES));
}

/**
 * Names of entries that are **fully verified** (no `needsReview` flag).
 * The codemod uses this list to decide which literals to rewrite —
 * pending entries are never auto-applied.
 */
export function verifiedNames(): readonly string[] {
  return Object.freeze(
    Object.values(WITNESSED_VALUES)
      .filter(e => !e.needsReview)
      .map(e => e.name),
  );
}
