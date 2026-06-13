import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-trace-inductive-limit",
  interprets: "rem:markov-axioms-primitive",
  title:
    "Markov trace on the inductive limit $\\mathbf{B}_\\infty = \\bigcup_n \\mathbf{B}_n$ — single global trace operator $\\tau_M : \\mathbf{B}_\\infty \\to \\mathbb{R}$ deriving every per-$n$ $\\mathtt{MarkovTraceN}\\ n\\ q$ via Jones-Wenzl axioms M1-M4 on the inductive structure",
  uses: ["rem:braid-group-n-strand"],
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
  authorNotes: [
    {
      kind: "status",
      body: "**Scaffolding only.** The substantive content (von Neumann inductive\nlimit on the infinite-dim affine Hecke algebra, plus the bicommutant\nclosure constructing the global trace) is open R&D. The scaffold\nsuffices to consolidate the per-$n$ class discharges into a single\nglobal hypothesis with a clear API.\n\nThe default instance discharges by definition via the explicit-residual\npattern; a future Mathlib-tier construction would supply a\nsubstantive witness without changing the surrounding API.",
    },
  ],
});
