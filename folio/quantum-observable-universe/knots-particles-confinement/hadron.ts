import { definition } from "../../schema/builders";

export default definition({
  label: "def:hadron",
  title: "Hadron (stable knot composite)",
  tags: ["hadron", "knot", "composite", "stable", "crossing-energy"],
  lean: { ref: "qou:QOU.Hadron",
    validation: "not_checked",
  },
  uses: [],
  examples: ["rem:hadron-operations", "rem:knot-factorization", "rem:knot-particle-dictionary"],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
