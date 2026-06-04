import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:algebraic-gns-embedding",
  title:
    "Markov-trace GNS embedding $H_\\infty(q) \\hookrightarrow L(\\mathcal{H})$ — operator-algebra route to the Archimedean side",
  lean: {
    ref: "qou:QOU.Observations.AlgebraicGnsEmbedding.HasMarkovGnsEmbedding",
    validation: "not_checked",
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
      body: "**Established, not conjectural.** This is the Jones–Wenzl subfactor construction (`jones1985`, `wenzl1988`): the Markov trace's positivity in the Wenzl regime, consistency under the inductive system $H_n(q) \\subset H_{n+1}(q)$ (Markov property), and the GNS construction are all standard. The four-step derivation lives in the proof block `prf:algebraic-gns-embedding`.",
    },
  ],
});
