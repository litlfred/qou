import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:topological-mass-eigenspace-decomp",
  lean: { ref: "qou:QOU.LiftingDescent.tm_eigenspace_decomp",
    validation: "not_checked",
  },
  title: "Eigenspace decomposition of the mass integrand (descent involution)",
  tags: ["descent-involution", "killing-form", "multiplicative-integral", "mass"],
  uses: ["def:mass-identity", "def:descent-involution", "prop:descent-eigenspaces"],
  proofs: ["prf:topological-mass-eigenspace-decomp"],
  cites: ["yekutieli2015"],
});
