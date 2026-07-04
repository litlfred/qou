import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:lepton-number-categorical",
  title:
    "Categorical Lepton Number",
  tags: [
    "lepton-number",
    "skein-relation",
    "smoothing",
    "conservation-law",
    "categorical",
    "weak-force",
  ],
  lean: { ref: "qou:QOU.Archimedean.LeptonNumber",
    validation: "not_checked",
  },
  uses: ["def:beta-decay-skein"],
});
