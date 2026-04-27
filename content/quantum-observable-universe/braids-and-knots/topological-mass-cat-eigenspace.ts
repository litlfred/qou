import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:topological-mass-cat-eigenspace",
  lean: { ref: "qou:QOU.TopologicalMass.cat_eigenspace_decomposition",
    validation: "not_checked",
  },
  title: "Eigenspace decomposition of the categorical mass integrand",
  tags: ["descent-involution", "frobenius-norm", "categorical-trace", "mass"],
  uses: [
    "def:mass-identity",
    "prop:descent-eigenspaces",
  ],
  proofs: ["prf:topological-mass-cat-eigenspace"],
});
