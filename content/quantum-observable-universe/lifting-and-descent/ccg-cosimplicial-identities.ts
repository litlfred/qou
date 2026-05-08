import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:ccg-cosimplicial-identities",
  lean: { ref: "qou:QOU.LiftingDescent.ccg_cosimplicial_identities",
    validation: "not_checked",
  },
  title: "Cosimplicial identities for the jet/descent face and degeneracy maps",
  tags: ["cosimplicial", "face", "degeneracy", "ascent", "descent", "retraction"],
  uses: ["lem:descent"],
  proofs: ["prf:ccg-cosimplicial-identities"],
});
