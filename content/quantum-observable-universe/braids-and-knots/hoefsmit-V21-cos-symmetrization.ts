import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hoefsmit-V21-cos-symmetrization",
  lean: {
    ref: "qou:QOU.BraidKnot.hoefsmit_V21_cos_symmetrization",
    validation: "not_checked",
  },
  title:
    "Hoefsmit seminormal matrix for $V_{(2,1)}$ + Markov-symmetrized cos character: $\\chi^{(2,1),\\mathrm{symm}}_q(\\beta) = \\mathrm{tr}\\,\\rho_{(2,1)}(\\beta) \\cdot \\cos((z-1)h/2)$",
  uses: [
    "prop:hecke-1d-irrep-closed-form-character",
    "prop:q-beta-cos-resummation",
    "prop:beta-decay-transfer-matrix",
    "prop:hecke-branching-trace-decomposition",
  ],
  cites: [
    "hoefsmit1974",
    "wenzl1988",
    "jones1985",
  ],
  tags: [
    "hecke-algebra",
    "hoefsmit-seminormal",
    "2d-irrep",
    "markov-symmetrization",
    "cos-resummation",
    "V_(2,1)",
    "non-trivial-markov-machinery",
    "1ppb-roadmap",
  ],
  computation: {
    engine: "python+mpmath",
    script: "folio-assistant/computations/probe_q_beta_operator_valued_N2.py",
    witness: [
      "folio-assistant/computations/q-beta-operator-valued-N2.witness.json",
    ],
    status: "experimental",
  },
});
