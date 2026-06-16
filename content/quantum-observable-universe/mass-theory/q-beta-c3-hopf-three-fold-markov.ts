import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-c3-hopf-three-fold-markov",
  lean: {
    ref: "qou:QOU.BraidKnot.q_beta_c3_hopf_three_fold_markov",
    validation: "not_checked",
  },
  title:
    "Categorical derivation of $c_3 = J_{\\mathrm{Hopf}}(q=1) = -2$ in the $\\mathfrak{Q}_\\beta$ precision ladder via 3-fold Markov closure → 2-strand sub-braid Hopf-link substructure → KL classical-limit decategorification",
  uses: ["rem:q-beta-gamma-gamma-canonical-derivation"],
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
    script: "computations/probe_q_beta_operator_valued_N3.py",
    witness: [
      "computations/q-beta-operator-valued-N3.witness.json"
    ],
    status: "experimental",
  },
  authorNotes: [
    {
      kind: "status",
      body: "The classical-limit Jones evaluation $J_{\\text{Hopf}}(1) = -2$ is\nelementary; the 2-strand sub-braid extraction at order 3 is the\nsubstantive open step. Empirical observation (112$\\times$ tightening),\nMarkov cyclicity, and KL decategorification give strong support, but a\nfully-formalised proof requires:\n\n- Per-crossing Hecke-quadratic expansion in $\\hbar_q$ (mechanizable\n  via existing symbolic-computation infrastructure).\n- Sub-braid combinatorial extraction at order 3 (combinatorial\n  formalisation of \"choose 2 strands from $\\beta$ and Markov-close\").\n- Cross-Wedderburn-block coupling identification (categorical proof\n  that the Hopf-link factor survives the $V_{(3)} \\oplus V_{(2,1)}\n  \\oplus V_{(1,1,1)}$ decomposition at the third order).\n\nThese three steps form a concrete path to closing the open Track-C\nformalisation gap, beyond the present empirical-observation status.",
    },
  ],
});
