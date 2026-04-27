import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:descent-cocycle-deviation",
  lean: { ref: "qou:QOU.LiftingDescent.descent_cocycle_deviation",
    validation: "not_checked",
  },
  title: "Cocycle deviation at level $n+1$ as a twisted Cech 2-cocycle",
  tags: ["cocycle", "yekutieli-triple", "central-extension", "cech-cohomology"],
  uses: ["def:yekutieli-triple"],
  proofs: ["prf:descent-cocycle-deviation"],
});
