import { remark } from "../../schema/builders";

export default remark({
  label: "rem:braid-group-n-strand",
  interprets: "prop:categorical-chain-convergence-mechanisms",
  title:
    "$n$-strand braid group, Markov closure, and Hecke quadratic quotient: axiomatic scaffolding generalising the 2-strand $\\mathbf{B}_2$ foundation and 3-strand typed-$\\mathbf{B}_3$ infrastructure",
  uses: [
    "rem:markov-axioms-primitive",
    "rem:typed-b3-sub-braid-extraction",
  ],
  cites: [
    "jones1985",
    "kassel1995",
    "wenzl1988",
  ],
  tags: [
    "lean-infrastructure",
    "braid-group",
    "n-strand",
    "hecke-algebra",
    "markov-closure",
    "scaffolding",
  ],
});
