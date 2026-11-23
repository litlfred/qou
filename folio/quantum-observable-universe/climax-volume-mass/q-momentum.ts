import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Both facts are proved in `QOU/StandardModel/WritheMarkovInvariance.lean`." },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:q-momentum",
  title: "$q$-Momentum from the braid writhe",
  tags: [
    "momentum",
    "q-deformed",
    "writhe",
    "braid",
    "hecke",
    "crossing",
    "kinematic",
  ],
  lean: { ref: "qou:QOU.Archimedean.QMomentum",
    validation: "not_checked",
  },
  uses: [],
});
