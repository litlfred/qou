import { proposition } from "../../schema/builders";

/**
 * Algebraic identity (proposition with rigorous proof in R):
 *
 *   α_EM = h² / [q · δ_q(T_{2,9}) · δ_q(T_{3,5})]
 *
 * where h = q - q⁻¹ is the skein parameter, δ_q is the q-dimension
 * decoration (def:delta-q-decoration), and T_{2,9}, T_{3,5} are the
 * two genus-4-saturating torus knots (prop:force-carrier-bring-uniqueness).
 *
 * The identity is rigorous because δ_q(T_{2,k}) = q^k - q^-k = h·[k]_q
 * for odd k ≥ 1 (by direct categorical-trace computation in the
 * 2-strand Hecke representation), and similarly δ_q(T_{3,5}) =
 * q^10 - q^-10 = h·[10]_q. Substitution gives:
 *
 *   h²/(q · h·[9]_q · h·[10]_q) = 1/(q · [9]_q · [10]_q) = α_EM.
 *
 * Numerically verified to 10⁻¹² precision at q_0 in
 * delta-q-decoration.witness.json.
 *
 * Significance: refactors α_EM from "inverse Bring complex complexity"
 * into "h²/(force-carrier categorical-trace product)" — moving it from
 * the operator-selection LP layer into the q-dimension layer.
 *
 * Combined with prop:force-carrier-intertwining-correspondence, this
 * provides the post-round-18 closure path for
 * conj:e-hartree-categorical-derivation.
 */
export default proposition({
  label: "prop:alpha-em-categorical-trace-ratio",
  title:
    "Algebraic identity: $\\alpha_{EM} = h^2 / [q \\cdot \\delta_q(T_{2,9}) \\cdot \\delta_q(T_{3,5})]$",
  lean: { ref: "qou:QOU.ArchimedeanUniverse.alpha_em_categorical_trace_ratio" },
  // All three are named in the proposition's own setup sentence: the
  // q-dimension decoration it applies, the result identifying T_{2,9} and
  // T_{3,5} as the genus-4-saturating pair, and the 1/alpha_EM value the
  // decomposition is stated against.
  uses: [
    "def:delta-q-decoration",
    "prop:em-coupling-projection",
    "prop:force-carrier-bring-uniqueness",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-08-09",
      body:
        "**Base ring minimised (AGENTS.md §7c).** The Lean sibling moved from " +
        "`[Field K]` + `field_simp` to a generic `[CommRing R]` with the " +
        "modulus carried as a unit `q : Units R`. Two changes of substance: " +
        "(i) `q_int` is now the **division-free** symmetric q-integer " +
        "`[n]_q = ∑_{i<n} qⁱ·q^(−(n−1−i))`, with `q_int_mul_h_skein` proving " +
        "the previous quotient definition's relation `[n]_q · h = qⁿ − q⁻ⁿ` " +
        "(so nothing changes wherever `h ≠ 0`, which is the only place the " +
        "old definition meant anything, and the new one is total); " +
        "(ii) the identity is available in the R[h] multiplicative form " +
        "`α·(q·[9]_q·[10]_q) = 1 ↔ α·(q·δ₉·δ₁₀) = h²` " +
        "(`alpha_em_relation_iff`), over any commutative ring in which `h` " +
        "is a unit — the forward direction needs no hypothesis at all. Its " +
        "structural core, `delta_mul_delta_eq_h_sq_mul_q_int`, is " +
        "hypothesis-free. A field survives only in the `RatioForm` section, " +
        "where α_EM is written as an actual quotient as the narrative does; " +
        "`alpha_em_categorical_trace_ratio` keeps its exact previous " +
        "statement there.",
    },
  ],
  tags: [
    "alpha-em",
    "fine-structure",
    "categorical-trace-ratio",
    "delta-q",
    "force-carrier",
    "algebraic-identity",
    "bring-complex",
  ],
});
