import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:topological-mass-cat-descended",
  lean: { ref: "qou:QOU.TopologicalMass.cat_descended_is_base_mass",
    validation: "not_checked",
  },
  title: "Descended term equals the base-level mass",
  tags: ["descent", "categorical-trace", "ascent-embedding", "mass"],
  uses: ["lem:topological-mass-cat-eigenspace"],
  proofs: ["prf:topological-mass-cat-descended"],
});
