import { remark } from "../../schema/builders";

export default remark({
  label: "rem:p-vs-np-surreal-bound",
  title:
    "Surreal bound for P vs NP: Reeb-period transfinite exceeds classical-budget standard",
  interprets: "conj:p-vs-np-qou",
  uses: [
    "conj:p-vs-np-qou",
    "lem:surreal-squeeze",
    "def:reeb-epsilon",
    "def:q-from-epsilon",
    "prop:surreal-rate-calculus",
    "rem:conway-normal-form",
    "rem:calculus-up-to-epsilon",
    "rem:millennium-unification",
  ],
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
