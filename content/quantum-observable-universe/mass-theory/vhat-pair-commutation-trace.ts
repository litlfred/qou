import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:vhat-pair-commutation-trace",
  proofs: ["prf:vhat-pair-commutation-trace"],
  title:
    "Pair commutation at the traced-volume level: $\\hat V_i \\hat V_j = \\hat V_j \\hat V_i$ in $\\mathbb{Z}[q^{\\pm 1/2}, z]$",
  lean: {
    ref: "qou:QOU.BraidKnot.VhatPairCommutationTrace",
    validation: "not_checked",
  },
  cites: [
    "kassel1995",
    "geckpfeiffer2000",
  ],
  tags: [
    "v-hat",
    "pentagon",
    "commutation",
    "markov-trace",
    "jet-tower",
    "narrative-replacement",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Status: provable** — the lemma's content is just commutativity of\na Laurent polynomial ring, and the trace identity follows by\nlinearity from\n[`prop:markov-pair-z2`](#prop\\:markov-pair-z2). The corresponding\nLean stub\n([qou:QOU.BraidKnot.VhatPairCommutationTrace](vhat-pair-commutation-trace.lean))\nstates the lemma in $\\mathbb{Z}[q^{\\pm 1/2}, z]$ and proves it\nby `mul_comm` on the underlying commutative ring.\n\nThis block closes audit GAP 17a\n([line 113 of `derivation-audit-.md`](../../../docs/audits/derivation-audit-.md))\nand the corresponding \"Pentagon $\\to$ uv-commutation\" subconjecture\nin\n[`rem:mass-endomorphism-jet-tower`](#rem\\:mass-endomorphism-jet-tower)\n§\"Remaining open subconjectures\" (item 2): the question is\nresolved by recognising that the V-hats commute as scalars and\nthe pentagon ascension's rigorous content is Markov-trace\nfactorization plus brane-tower jet ascension.",
    },
  ],
});
