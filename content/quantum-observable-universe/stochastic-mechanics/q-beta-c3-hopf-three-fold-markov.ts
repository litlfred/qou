import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-c3-hopf-three-fold-markov",
  lean: {
    ref: "qou:QOU.BraidKnot.q_beta_c3_hopf_three_fold_markov",
    validation: "not_checked",
  },
  title:
    "Categorical derivation of $c_3 = J_{\\mathrm{Hopf}}(q=1) = -2$ in the $Q_\\beta$ precision ladder via 3-fold Markov closure → 2-strand sub-braid Hopf-link substructure → KL classical-limit decategorification",
  uses: [
    "prop:q-beta-categorical-precision-ladder",
    "prop:hoefsmit-V21-cos-symmetrization",
    "prop:markov-trace-frobenius-selection",
    "rem:q-beta-gamma-gamma-canonical-derivation",
  ],
  cites: [
    "jones1985",
    "kashiwara1990",
    "hoefsmit1974",
  ],
  tags: [
    "q-beta",
    "c_3-derivation",
    "hopf-jones",
    "markov-closure",
    "three-fold-cyclic",
    "KL-decategorification",
    "track-C-formalization",
    "1ppb-roadmap",
  ],
  computation: {
    engine: "python+mpmath",
    script: "folio-assistant/computations/probe_q_beta_operator_valued_N3.py",
    witness: [
      "folio-assistant/computations/q-beta-gamma-gamma-derivation.witness.json",
      "folio-assistant/computations/q-beta-operator-valued-N3.witness.json",
    ],
    status: "experimental",
  },
});
