import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:joint-galois-braid-discharged",
  title:
    "Joint motivic-Galois $\\times$ braid action commutes on every bi-filtration cell — discharged",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.JointGaloisBraidDischarged.joint_action_discharged",
    validation: "not_checked",
  },
  uses: ["conj:joint-galois-braid-figure-8-verified"],
  cites: [],
  tags: [
    "joint-action",
    "discharged",
    "general-case",
    "centrality",
    "bar-transposition",
    "graded-mikusinski",
    "theorem-level",
  ],
});
