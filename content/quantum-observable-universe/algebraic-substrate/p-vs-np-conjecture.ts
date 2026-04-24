import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:p-vs-np-qou",
  title:
    "P vs NP in the QOU: classical-limit separation of BQP-width classes",
  lean: {
    decl: "QOU.AlgebraicSubstrate.PvsNPQou",
    file: "lean/QOU/AlgebraicSubstrate/PvsNPQou.lean",
    validation: "not_checked",
  },
  uses: [
    "def:reeb-epsilon",
    "def:q-from-epsilon",
    "def:classical-limit-functor",
    "thm:quantum-gap-collapse",
    "prop:surreal-rate-calculus",
    "rem:big-o-surreal",
  ],
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
