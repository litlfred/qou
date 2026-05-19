import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-trace-operator-construction",
  interprets: "rem:markov-trace-inductive-limit",
  title:
    "Operator-theoretic construction of the Jones-Wenzl Markov trace on the inductive limit $\\mathbf{B}_\\infty$ — per-$n$ Hilbert reps + inductive embeddings + GNS / bicommutant von Neumann factor scaffolding",
  uses: [
    "rem:markov-trace-inductive-limit",
    "rem:hecke-algebra-type-scaffold",
    "rem:markov-axioms-primitive",
  ],
  cites: [
    "jones1985",
    "wenzl1988",
    "kassel1995",
  ],
  tags: [
    "lean-infrastructure",
    "markov-trace-operator",
    "von-neumann-factor",
    "inductive-limit",
    "scaffolding",
    "open-rd-item-4",
  ],
});
