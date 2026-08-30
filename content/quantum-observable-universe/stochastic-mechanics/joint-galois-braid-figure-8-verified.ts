import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:joint-galois-braid-figure-8-verified",
  title:
    "Joint Galois $\\times$ braid action commutes on the figure-8 bi-filtration cell — verified directly",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.JointGaloisBraidFigure8.figure_8_joint_action",
    validation: "not_checked",
  },
  uses: [
    "conj:joint-galois-braid-action",
    "def:hq-bi-filtration",
  ],
  cites: [],
  tags: [
    "joint-action",
    "figure-8-knot",
    "self-conjugate-cell",
    "verification",
    "graded-mikusinski",
    "theorem-level",
  ],
});
