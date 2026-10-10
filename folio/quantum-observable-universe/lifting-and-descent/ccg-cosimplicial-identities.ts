import { definition } from "../../schema/builders";

export default definition({
  label: "def:ccg-cosimplicial-identities",
  lean: { ref: "qou:QOU.LiftingDescent.ccg_cosimplicial_identities",
    validation: "not_checked",
  },
  title: "Cosimplicial identities for the jet/descent face and degeneracy maps",
  tags: ["cosimplicial", "face", "degeneracy", "ascent", "descent", "retraction"],
  uses: ["lem:descent"],
});
