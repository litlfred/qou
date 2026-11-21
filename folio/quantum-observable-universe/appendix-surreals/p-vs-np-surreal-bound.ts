import { remark } from "../../schema/builders";

export default remark({
  label: "rem:p-vs-np-surreal-bound",
  uses: [
    "conj:p-vs-np-qou",
    "def:q-from-epsilon",
    "def:reeb-epsilon",
    "lem:surreal-squeeze",
    "prop:surreal-rate-calculus",
    "rem:calculus-up-to-epsilon",
    "rem:conway-normal-form",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): (see [millennium unification](#rem:millennium-unification))" },
  ],
  title:
    "Surreal bound for P vs NP: Reeb-period transfinite exceeds classical-budget standard",
  interprets: "conj:p-vs-np-qou",
  tags: [
    "p-vs-np",
    "millennium-problem",
    "complexity",
    "surreal",
    "squeeze",
    "reeb-period",
    "classical-limit",
  ],
  cites: ["conway1976", "cook1971", "freedman2003"],
});
