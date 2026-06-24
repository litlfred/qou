import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:tetrahedral-hbond-directions",
  proofs: ["prf:tetrahedral-hbond-directions"],
  title: "The four H-bond directions are tetrahedral ($\\cos\\theta_0 = -1/3$)",
  lean: {
    ref: "qou:QOU.Molecular.tetrahedral_cos",
    validation: "not_checked",
  },
  uses: ["def:h2o-molecular-braid"],
  tags: ["water", "ice", "tetrahedral", "hydrogen-bond", "bond-angle"],
});
