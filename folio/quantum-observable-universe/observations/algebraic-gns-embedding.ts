import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:algebraic-gns-embedding",
  title:
    "Markov-trace GNS embedding $H_\\infty(q)/\\mathcal{N} \\hookrightarrow L(\\mathcal{H})$ — operator-algebra route to the Archimedean side",
  lean: {
    ref: "qou:QOU.Observations.AlgebraicGnsEmbedding.HasMarkovGnsEmbedding",
    validation: "leanok",
  },
  uses: ["prop:wedderburn-weight-canonical"],
  cites: ["jones1985", "wenzl1988"],
  tags: [
    "causal-fermion-systems",
    "gns",
    "markov-trace",
    "operator-algebra",
    "subfactor",
    "pre-archimedean",
    "established-not-conjectural",
  ],
  proofs: ["prf:algebraic-gns-embedding"],
  authorNotes: [
    {
      kind: "status",
      body: "**Established, not conjectural.** This is the Jones–Wenzl subfactor construction (`jones1985`, `wenzl1988`): the Markov trace's positivity for every real $q > 0$ (under convention D it factors through Temperley–Lieb with loop value $[2]_q \\geq 2$, which is Jones's positivity range), consistency under the inductive system $H_n(q) \\subset H_{n+1}(q)$ (Markov property), and the GNS construction are all standard. The four-step derivation lives in the proof block `prf:algebraic-gns-embedding`.",
    },
    {
      kind: "caveat",
      date: "2026-08-26",
      body: "**Qualified to the trace-quotient (bean `qou-phlk`).** The statement previously asserted a faithful representation of $H_\\infty(q)$ itself. That was correct under the excised convention C, where the trace ideal collapses to $0$, and became false when convention D was made canonical on 2026-08-15: under D the ideal is the Temperley–Lieb radical and the representation is faithful only on the quotient. The proof block `prf:algebraic-gns-embedding` already carried the qualification (\"$a = 0$ in the trace-quotient\"), as does the Lean class `QOU.Observations.AlgebraicGnsEmbedding.HasMarkovGnsEmbedding`, whose `trM_faithful` and `repr_faithful` fields land in `traceIdeal` rather than at $0$ — so no Lean change was needed. A convention-migration casualty, not an original error.",
    },
  ],
});
