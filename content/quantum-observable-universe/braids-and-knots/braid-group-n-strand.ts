import { remark } from "../../schema/builders";

export default remark({
  label: "rem:braid-group-n-strand",
  lean: {
    ref: "qou:QOU.BraidKnot.braid_group_n_strand",
    validation: "not_checked",
  },
  interprets: "prop:categorical-chain-convergence-mechanisms",
  title:
    "$n$-strand braid group, Markov closure, and Hecke quadratic quotient: axiomatic scaffolding generalising the 2-strand $\\mathbf{B}_2$ foundation and 3-strand typed-$\\mathbf{B}_3$ infrastructure",
  uses: [
    "rem:braid-link-types",
    "rem:markov-axioms-primitive",
    "rem:markov-closure-map-axiomatic",
    "rem:typed-b3-sub-braid-extraction",
    "prop:hoefsmit-V21-cos-symmetrization",
  ],
  cites: [
    "jones1985",
    "kassel1995",
    "wenzl1988",
  ],
  tags: [
    "lean-infrastructure",
    "braid-group",
    "n-strand",
    "hecke-algebra",
    "markov-closure",
    "scaffolding",
  ],
});
