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
 *      (look in `folio-assistant/computations/*.witness.json`).
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
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.q",
      defaultPrecision: 4,
      units: null,
    }),

    q_inv: Object.freeze({
      name: "q_inv",
      description: "Reciprocal substrate parameter q_0^{-1}.",
      symbol: "q_0^{-1}",
      witnessFile:
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.q_inv",
      defaultPrecision: 4,
      units: null,
    }),

    H_A: Object.freeze({
      name: "H_A",
      description: "Planck constant ℏ_q = q - q^{-1} at the substrate.",
      symbol: "H_A",
      witnessFile:
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.H_A",
      defaultPrecision: 4,
      units: null,
    }),

    hbar_q: Object.freeze({
      name: "hbar_q",
      description: "Categorical Planck constant ℏ_q = (q-1)/q.",
      symbol: "\\hbar_q",
      witnessFile:
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.hbar_q",
      defaultPrecision: 4,
      units: null,
    }),

    hbar_q_sq: Object.freeze({
      name: "hbar_q_sq",
      description: "Squared Planck constant ℏ_q^2 — denominator of ξ(q).",
      symbol: "\\hbar_q^{2}",
      witnessFile:
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.hbar_q_sq",
      defaultPrecision: 4,
      units: null,
    }),

    two_q: Object.freeze({
      name: "two_q",
      description: "Quantum integer [2]_q = q + q^{-1}.",
      symbol: "[2]_q",
      witnessFile:
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.two_q",
      defaultPrecision: 4,
      units: null,
    }),

    qint_3: Object.freeze({
      name: "qint_3",
      description: "Quantum integer [3]_q.",
      symbol: "[3]_q",
      witnessFile:
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
      witnessPath: "quantum_integers.[3]_q",
      defaultPrecision: 4,
      units: null,
    }),

    qint_4: Object.freeze({
      name: "qint_4",
      description: "Quantum integer [4]_q.",
      symbol: "[4]_q",
      witnessFile:
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
      witnessPath: "quantum_integers.[4]_q",
      defaultPrecision: 4,
      units: null,
    }),

    qint_5: Object.freeze({
      name: "qint_5",
      description: "Quantum integer [5]_q.",
      symbol: "[5]_q",
      witnessFile:
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
      witnessPath: "quantum_integers.[5]_q",
      defaultPrecision: 4,
      units: null,
    }),

    z_markov: Object.freeze({
      name: "z_markov",
      description: "Markov parameter z = 1/(q^{1/2} + q^{-1/2}).",
      symbol: "z",
      witnessFile:
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.z_markov",
      defaultPrecision: 4,
      units: null,
    }),

    rho_q: Object.freeze({
      name: "rho_q",
      description: "Hecke trace density ρ_q.",
      symbol: "\\rho_q",
      witnessFile:
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.rho_q",
      defaultPrecision: 4,
      units: null,
    }),

    s_skein: Object.freeze({
      name: "s_skein",
      description: "Skein normalisation s = z · (q - q^{-1}).",
      symbol: "s",
      witnessFile:
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
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
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
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
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
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
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
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
        "folio-assistant/computations/4he-binding-full-pipeline.witness.json",
      witnessPath: "B_AME_MeV",
      defaultPrecision: 6,
      units: "MeV",
    }),

    B_2H_AME_MeV: Object.freeze({
      name: "B_2H_AME_MeV",
      description: "AME experimental binding energy of deuterium (2H).",
      symbol: "B_{\\mathrm{AME}}(\\mathrm{D})",
      witnessFile:
        "folio-assistant/computations/canonical-mass-table.witness.json",
      witnessPath: "results.0.B_AME_MeV",
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
        "Proton rest mass in MeV/c^2 (CODATA).  Canonical witness pending.",
      symbol: "m_p",
      witnessFile:
        "folio-assistant/computations/canonical-mass-table.witness.json",
      witnessPath: "parameters.q0",
      defaultPrecision: 6,
      units: "MeV",
      needsReview: true,
    }),

    m_n_MeV: Object.freeze({
      name: "m_n_MeV",
      description:
        "Neutron rest mass in MeV/c^2 (CODATA).  Canonical witness pending.",
      symbol: "m_n",
      witnessFile:
        "folio-assistant/computations/canonical-mass-table.witness.json",
      witnessPath: "parameters.q0",
      defaultPrecision: 6,
      units: "MeV",
      needsReview: true,
    }),

    m_e_MeV: Object.freeze({
      name: "m_e_MeV",
      description:
        "Electron rest mass in MeV/c^2 (CODATA).  Canonical witness pending.",
      symbol: "m_e",
      witnessFile:
        "folio-assistant/computations/canonical-mass-table.witness.json",
      witnessPath: "parameters.q0",
      defaultPrecision: 6,
      units: "MeV",
      needsReview: true,
    }),

    inv_alpha: Object.freeze({
      name: "inv_alpha",
      description:
        "Inverse fine-structure constant 1/α (CODATA).  Canonical witness pending.",
      symbol: "\\alpha^{-1}",
      witnessFile:
        "folio-assistant/computations/alpha-high-precision.witness.json",
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
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
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
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
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
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
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
        "folio-assistant/computations/q-pinning-50-digit.witness.json",
      witnessPath: "derived_50_digit.q",
      defaultPrecision: 4,
      units: null,
      needsReview: true,
    }),

    // ── Hyperbolic volumes (encounter chapter) ──────────────────
    // Vol(4_1) computed via the Clausen-function identity
    // 2 · Cl_2(π/3) at 50 dps in `hyperbolic_volumes.py`; the
    // 15-digit serialisation feeds the Lean literal
    // `MostowRigidity.figureEight.volume` via the `:leanval[vol_4_1]`
    // tag and the `codemod-leanval.ts` codemod.

    // Vol_4_1 (uppercase) is registered above pointing at the
    // canonical q-pinning witness; consume that entry for the
    // figure-eight volume.  The hyperbolic-volumes witness retains
    // a parallel `data.vol_4_1_decimal_15` field for self-tests
    // and for cross-validating against the q-pinning value, but
    // the Lean tag uses :leanval[Vol_4_1]{precision=15}.

    vol_5_2: Object.freeze({
      name: "vol_5_2",
      description:
        "Hyperbolic volume of the 5_2 knot complement " +
        "Vol(5_2) ≈ 2.82812 (literature constant; " +
        "Adams-Hildebrand-Weeks 1991, SnapPy verified). " +
        "Second-smallest known orientable cusped hyperbolic " +
        "3-manifold volume.",
      symbol: "\\mathrm{Vol}(5_2)",
      witnessFile:
        "folio-assistant/computations/hyperbolic-volumes.witness.json",
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
        "Replace with SnapPy-computed value once SnapPy is in CI.",
      symbol: "\\Delta_{\\mathrm{Mostow}}(4_1)",
      witnessFile:
        "folio-assistant/computations/hyperbolic-volumes.witness.json",
      witnessPath: "data.gap_lower_bound",
      defaultPrecision: 1,
      units: null,
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
