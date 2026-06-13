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
  authorNotes: [
    {
      kind: "status",
      body: "**Scaffolding only.** This block defines the n-strand types and\nclasses; substantive theorems (specific closures, sub-braid\nextractions at higher $n$) plug in as separate per-$n$ blocks.\n\n`Braid2_writhe_eq` is **closed** by structural recursion mirroring\nthe `toBraidWord` construction — no `sorry`s remain in this module.",
    },
  ],
});
