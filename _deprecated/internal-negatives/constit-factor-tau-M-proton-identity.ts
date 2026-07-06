import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:constit-factor-tau-M-proton-identity",
  title:
    "Constit-side per-Z step factor equals the proton's H_3 Markov trace (structural identity)",
  lean: {
    ref: "qou:QOU.BraidKnot.constit_factor_eq_tau_M_proton",
    validation: "not_checked",
  },
  uses: [
    "prop:interface-knot-markov-z",
    "prop:lr-tensor-character-bridge",
    "thm:jones-markov-trace",
  ],
  cites: ["wenzl1988", "jones1987"],
  computation: {
    engine: "python",
    script:
      "computations/rho_constit_equals_tau_M_proton_phase5l.py",
    witness:
      "computations/rho-constit-equals-tau-M-proton-phase5l.witness.json",
    status: "verified",
  },
  tags: [
    "markov-trace",
    "constit-factor",
    "categorical-derivation",
    "z-step",
    "structural-identity",
    "disjoint-product",
  ],
});
