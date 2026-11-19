import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:tetrahedral-hbond-directions",
  title: "The four H-bond directions are tetrahedral ($\\cos\\theta_0 = -1/3$)",
  lean: {
    ref: "qou:QOU.Molecular.tetrahedral_cos",
    validation: "not_checked",
  },
  uses: ["def:h2o-molecular-braid"],
  tags: ["water", "ice", "tetrahedral", "hydrogen-bond", "bond-angle"],
  authorNotes: [
    {
      kind: "status",
      body: "Lean sibling `QOU.Molecular.tetrahedral_cos` proves balanced sum, squared length 3, pairwise dot -1, and cos theta_0 = -1/3 over R.",
    },
  ],
});
