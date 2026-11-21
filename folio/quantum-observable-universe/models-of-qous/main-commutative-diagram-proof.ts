import { proof } from "../../schema/builders";

export default proof({
  label: "prf:main-commutative-diagram",
  title: "Proof of Main Commutative Diagram",
  uses: ["prop:main-commutative-diagram"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([GR substrate geometry](#rem:gr-substrate-geometry))" },
  ],
  lean: { ref: "qou:QOU.main_commutative_diagram",
    validation: "not_checked",
  },
});
