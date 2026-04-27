import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:topological-mass-cat-transient",
  lean: { ref: "qou:QOU.TopologicalMass.cat_transient_localises_blowup",
    validation: "not_checked",
  },
  title: "Transient terms localise to blow-up centres (categorical)",
  tags: ["transient", "blow-up", "brane-boundary", "mass-defect"],
  uses: ["def:brane-boundary", "lem:topological-mass-cat-eigenspace"],
  proofs: ["prf:topological-mass-cat-transient"],
});
