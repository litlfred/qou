import { definition } from "../../schema/builders";

/**
 * Definition of the q-dimension decoration map δ_q for the Iwahori-Hecke
 * algebra H_n(q). It refines the Markov trace by recording the per-irrep
 * q-character of each NF basis element:
 *
 *   δ_q : H_n(q) → R^|Par(n)|, b → (χ_λ(b))_{λ⊢n}
 *
 * This is the missing layer identified in the round-11 investigation
 * (conj:e-hartree-categorical-derivation): α_EM lives in the q-dimension
 * layer, not the Markov-trace layer, and δ_q is what carries it.
 *
 * Key application: round-18 finding that the H_2 molecular braid's δ_q
 * decoration projects onto the (3,1) and (2,1,1) Wedderburn channels
 * (transpose pair), corresponding to T_{3,5} and T_{2,9} intertwining
 * the 4-strand bound state — see conj:force-carrier-intertwining-correspondence.
 *
 * Computational implementation: computations/delta_q_decoration.py
 * Cached witness: computations/delta-q-decoration.witness.json
 */
export default definition({
  label: "def:delta-q-decoration",
  title:
    "$q$-dimension decoration $\\delta_q : H_n(q) \\to R^{|\\mathrm{Par}(n)|}$ of the NF basis",
  uses: ["prop:operator-selection-lp"],
  defines: ["delta-q-decoration"],
  computation: {
    engine: "python",
    script: "computations/delta_q_decoration.py",
    witness: "computations/delta-q-decoration.witness.json",
    status: "verified",
  },
  lean: { ref: "qou:QOU.BraidKnot.delta_q" },
  tags: [
    "delta-q",
    "q-dimension",
    "wedderburn-decomposition",
    "hecke-algebra",
    "categorical-trace",
    "force-carrier",
    "infrastructure",
  ],
});
