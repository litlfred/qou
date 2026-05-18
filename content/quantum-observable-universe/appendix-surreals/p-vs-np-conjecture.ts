import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:p-vs-np-qou",
  title:
    "P vs NP in the QOU: classical-limit separation of BQP-width classes",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.PvsNPQou",
    validation: "not_checked",
  },
  tags: [
    "p-vs-np",
    "millennium-problem",
    "complexity",
    "bqp",
    "reeb-period",
    "classical-limit",
    "surreal",
    "speculative",
  ],
  cites: ["cook1971", "freedman2003"],
});
