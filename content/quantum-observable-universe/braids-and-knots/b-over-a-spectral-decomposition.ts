import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:b-over-a-spectral-decomposition",
  title:
    "Spectral decomposition of $B/A$ from the $6 \\times 6$ transfer matrix of $H_3(R, q)$",
  lean: {
    ref: "qou:QOU.BraidKnot.b_over_a_spectral_decomposition",
    validation: "not_checked",
  },
  uses: [
    "prop:eigenvalue-product-expansion",
    "prop:transfer-matrix-identities",
    "prop:unified-curvature-rank-mass-formula",
  ],
  tags: [
    "binding-energy",
    "spectral-decomposition",
    "transfer-matrix",
    "hecke-h3",
    "wedderburn",
    "plancherel",
    "bethe-weizsaecker",
    "approach-2",
  ],
});
