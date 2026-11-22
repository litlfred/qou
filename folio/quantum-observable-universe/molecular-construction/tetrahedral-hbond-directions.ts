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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean sibling proves the four facts — balanced sum, squared length $3$, pairwise dot $-1$, and $\\cos\\theta_0 = -1/3$ — exactly over $\\mathbb{R}$." },
  ],
});
