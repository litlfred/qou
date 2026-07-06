import { example } from "../../schema/builders";

export default example({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "ex:hadron-half-life-verification",
  title: "Half-life predictions for selected beta emitters",
  tags: [
    "half-life",
    "beta-decay",
    "verification",
    "numerical",
    "tritium",
    "cobalt-60",
    "carbon-14",
  ],
  lean: { ref: "qou:QOU.Archimedean.HalfLifeVerification.all_six_agree",
    validation: "not_checked",
  },
  uses: ["rem:hadron-half-life-regimes"],
});
