import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:algebraic-gns-embedding",
  title:
    "Markov-trace GNS embedding $H_\\infty(q) \\hookrightarrow L(\\mathcal{H})$ — operator-algebra route to the Archimedean side",
  lean: {
    ref: "qou:QOU.Observations.AlgebraicGnsEmbedding",
    validation: "not_checked",
  },
  uses: [
    "thm:jones-markov-trace",
    "prop:wedderburn-weight-canonical",
  ],
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
});
