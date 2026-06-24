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
  proofs: ["prf:alpha-em-categorical-trace-ratio"],
  title:
    "Algebraic identity: $\\alpha_{EM} = h^2 / [q \\cdot \\delta_q(T_{2,9}) \\cdot \\delta_q(T_{3,5})]$",
  lean: { ref: "qou:QOU.ArchimedeanUniverse.alpha_em_categorical_trace_ratio" },
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
