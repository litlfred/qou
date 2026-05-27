import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-trace-inductive-limit",
  interprets: "rem:markov-axioms-primitive",
  title:
    "Markov trace on the inductive limit $\\mathbf{B}_\\infty = \\bigcup_n \\mathbf{B}_n$ — single global trace operator $\\tau_M : \\mathbf{B}_\\infty \\to \\mathbb{R}$ deriving every per-$n$ $\\mathtt{MarkovTraceN}\\ n\\ q$ via Jones-Wenzl axioms M1-M4 on the inductive structure",
  uses: [
    "rem:markov-axioms-primitive",
    "rem:braid-group-n-strand",
  ],
  cites: [
    "jones1985",
    "wenzl1988",
    "kassel1995",
  ],
  tags: [
    "lean-infrastructure",
    "markov-trace",
    "inductive-limit",
    "consolidation",
    "scaffolding",
  ],
});
