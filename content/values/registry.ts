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
 *
 * All paths are repo-root relative.
 *
 * @module content/values/registry
 */

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
}

/**
 * Authoritative registry.  Keys mirror `entry.name` for fast lookup
 * by the renderer; `Object.freeze` keeps the table immutable at
 * runtime so accidental mutation in hot reload cannot corrupt the
 * source of truth.
 */
export const WITNESSED_VALUES: Readonly<Record<string, WitnessedValueEntry>> =
  Object.freeze({
    // ── Substrate parameter q_0 ─────────────────────────────────
    // Most-cited derived value in the paper (~30 .md files).
    // Backed by the 50-digit pinning witness which records q to
    // exactly 50 decimal digits via mpmath.
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

    // ── ℏ_q = q - q^{-1} ─────────────────────────────────────────
    // The categorical Planck constant ℏ_q.  Same witness file,
    // different path, so a single q update propagates atomically.
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

    // ── q^{-1} ───────────────────────────────────────────────────
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
  });

/** Return the entry registered under `name`, or `undefined`. */
export function lookupValue(name: string): WitnessedValueEntry | undefined {
  return WITNESSED_VALUES[name];
}

/** Iterate over all registered names — useful for validation. */
export function registeredNames(): readonly string[] {
  return Object.freeze(Object.keys(WITNESSED_VALUES));
}
