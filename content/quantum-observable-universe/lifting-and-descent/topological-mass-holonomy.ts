import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:topological-mass-holonomy",
  lean: { ref: "qou:QOU.LiftingDescent.tm_descended_is_holonomy",
    validation: "not_checked",
  },
  title: "Descended term is the unknot-core holonomy",
  tags: ["holonomy", "ascent-embedding", "blow-up", "nonabelian-stokes"],
  uses: ["lem:topological-mass-eigenspace-decomp"],
  proofs: ["prf:topological-mass-holonomy"],
  cites: ["yekutieli2015"],
});
