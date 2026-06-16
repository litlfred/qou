import { proposition } from "../../schema/builders";

/**
 * The unified ρ_K formula — graded expansion replacing the empirical
 * LO ansatz from `prop:atomic-mass-gb-nf`.  Categorically derived
 * from Markov multiplicativity (Wenzl 1988) for the constituent
 * piece, plus the Wedderburn-decomposed brane tower for binding
 * corrections matching T_2, T_3, ... of `thm:knot-mass-formula-unified`.
 *
 * Status:
 *   - constituent (LO) piece: PROVED via Markov multiplicativity
 *     (`rho-k-markov-multiplicativity.witness.json`).
 *   - single-gen log-volume correction: PROVED via
 *     `prop:atomic-braid-mass` (0.18 % across Z=1..20).
 *   - pair-gen Wedderburn-coupling correction: OPEN — the naive
 *     log-additive form fails (`rho-k-pair-gen-extension.witness.json`);
 *     proper Wedderburn-block coupling needed.
 */
export default proposition({
  label: "prop:rho-k-graded-expansion",
  title:
    "Graded expansion of the categorical density $\\rho_K = \\rho_K^{\\mathrm{LO}} + \\rho_K^{\\text{single-gen}} + \\rho_K^{\\text{pair-gen}} + \\dots$",
  cites: ["wenzl1988"],
  computation: {
    engine: "numpy",
    script: "computations/probes/rho_k_markov_multiplicativity_probe.py",
    witness: [
      "computations/probes/rho-k-markov-multiplicativity.witness.json",
    ],
    status: "verified",
    requires: ["numpy", "sympy", "mpmath"],
  },
  lean: {
    ref: "qou:QOU.BraidKnot.rhoKGradedExpansion",
    validation: "not_checked",
  },
  tags: [
    "mass",
    "categorical-density",
    "graded-expansion",
    "markov-multiplicativity",
    "brane-tower",
    "wedderburn-coupling",
  ],
});
