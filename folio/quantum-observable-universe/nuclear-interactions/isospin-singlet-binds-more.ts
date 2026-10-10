import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:isospin-singlet-binds-more",
  title:
    "$\\mu_- < \\mu_+$ for every $q>0$ under convention D: the isospin singlet is always the more strongly bound channel",
  lean: {
    ref: "qou:QOU.QBeta.InterfaceScalar.mu_singlet_lt_mu_triplet",
    validation: "not_checked",
  },
  uses: [
    "prop:interface-knot-markov-z",
    "prop:h3-markov-wenzl-weights",
  ],
  proofs: ["prf:isospin-singlet-binds-more"],
  tags: [
    "isospin",
    "nn-channel",
    "convention-d",
    "deuteron",
    "trace-convention",
  ],
});
