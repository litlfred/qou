import { remark } from "../../schema/builders";

export default remark({
  label: "rem:surreal-squeeze-interpretation",
  title: "Interpretation: cost dominates budget, and the downstream bounds",
  interprets: "lem:surreal-squeeze",
  uses: ["lem:surreal-squeeze"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): * [RH surreal bound](#rem:rh-surreal-bound);" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): * [Collatz surreal bound](#rem:collatz-surreal-bound);\n* [P vs NP surreal bound](#rem:p-vs-np-surreal-bound);\n* [millennium unification](#rem:millennium-unification)." },
  ],
  tags: [
    "surreal",
    "squeeze",
    "error-bounds",
    "millennium-problem",
    "classical-limit",
  ],
});
