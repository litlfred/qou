import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:partition-sum-proton-residual",
  title:
    "Proton tower residual equals $m_e \\cdot \\sum_{\\lambda \\vdash 3} 1/d_\\lambda = (5/2) m_e$",
  lean: {
    decl: "QOU.BraidKnot.proton_tower_residual_5halves",
    validation: "not_checked",
  },
  uses: [
    "prop:mass-endomorphism-tower",
    "prop:schur-weyl-mass-decomposition",
    "prop:categorical-mass-markov",
    "def:hecke-mass-element",
  ],
  tags: [
    "proton",
    "residual",
    "partition-sum",
    "hook-length",
    "mass-endomorphism",
    "closed-form",
    "5/2",
  ],
});
