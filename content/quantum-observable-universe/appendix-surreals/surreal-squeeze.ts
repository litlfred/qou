import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:surreal-squeeze",
  proofs: ["prf:surreal-squeeze"],
  title:
    "Surreal squeeze: standard-scale cost dominates infinitesimal dissipation",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.surreal_squeeze",
    validation: "not_checked",
  },
  uses: ["rem:millennium-unification"],
  tags: [
    "surreal",
    "squeeze",
    "error-bounds",
    "millennium-problem",
    "classical-limit",
  ],
});
