import { proposition } from "../../schema/builders";

/**
 * Antipode-induced polynomial symmetry of the Markov trace closed form
 * derived in PR #546 (`hoefsmit_symbolic` / `claude/hoefsmit-2x2-fix`):
 *
 *   tr_M(β_p) = p(q) / (12 q^10),
 *
 * where p(q) = q^20 + q^18 + 2q^12 - 2q^8 - q^2 - 1.
 *
 * The polynomial satisfies the EXACT identity
 *
 *   q^20 · p(1/q) = -p(q),
 *
 * equivalently tr_M(β_p)(1/q) = -tr_M(β_p)(q).  This is the Markov
 * trace's antipode symmetry — the Hopf antipode S(σ_i) = σ_i^{-1}
 * on H_n(q) descends through the Frobenius integral to a polynomial
 * identity on the closed-form trace.
 *
 * Proved via sympy in
 * `computations/poly_q_proof_probe.py`; the exactness
 * is symbolic, not numerical.
 */
export default proposition({
  label: "prop:markov-trace-antipode-polynomial-symmetry",
  proofs: ["prf:markov-trace-antipode-polynomial-symmetry"],
  title:
    "Antipode-induced polynomial symmetry $q^{20} p(1/q) = -p(q)$ of the proton Markov trace closed form",
  uses: [
    "prop:atomic-mass-gb-nf",
  ],
  cites: ["wenzl1988", "hoefsmit1974", "kassel1995"],
  computation: {
    engine: "sympy",
    script: "computations/poly_q_proof_probe.py",
    witness: ["computations/poly-q-proof.witness.json"],
    status: "verified",
    requires: ["sympy"],
  },
  lean: {
    ref: "qou:QOU.BraidKnot.markovTraceAntipodePolynomialSymmetry",
    validation: "not_checked",
  },
  tags: [
    "markov-trace",
    "hopf-antipode",
    "frobenius-integral",
    "polynomial-symmetry",
    "anti-self-reciprocal",
    "closed-form",
  ],
});
