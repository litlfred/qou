import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:beta-decay-skein",
  title:
    "Beta decay as a Skein crossing change on the Gröbner normal form",
  tags: [
    "beta-decay",
    "skein-relation",
    "groebner-basis",
    "hecke-algebra",
    "weak-force",
    "crossing-change",
    "lepton",
    "normal-form",
  ],
  lean: { ref: "qou:QOU.Archimedean.BetaDecaySkein",
    validation: "not_checked",
  },
  uses: ["def:positron-knot"],
});
