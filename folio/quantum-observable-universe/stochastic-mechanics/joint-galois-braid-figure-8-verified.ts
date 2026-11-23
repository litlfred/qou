import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:joint-galois-braid-figure-8-verified",
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
  authorNotes: [
    { kind: "status", date: "2026-11-21", body: "Demoted from `conj:joint-galois-braid-figure-8-verified` (owner, #8526, 2026-11-21; bean qou-tm3c). The block restates `conj:joint-galois-braid-action` on the $4_1$ cell. No computation is given, and the Lean composes class fields on abstract types. Whether the bar involution commutes with the braid action on that cell needs checking, since $\\lambda = \\lambda'$ corresponds to the sign twist $\\sigma \\mapsto -\\sigma^{-1}$, not to bar." },
  ],
});
