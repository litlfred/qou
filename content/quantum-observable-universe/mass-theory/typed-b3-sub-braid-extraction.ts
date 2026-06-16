import { remark } from "../../schema/builders";

export default remark({
  label: "rem:typed-b3-sub-braid-extraction",
  title:
    "Track C n-strand: typed-B_3 sub-braid extraction reduces to the 2-strand chain via a single focused combinatorial axiom (`DominantSubBraidAtEps6`); composes to fully Lean-proved $c_3 = -2$",
  interprets: "prop:q-beta-c3-hopf-three-fold-markov",
  uses: ["rem:braid-link-types"],
  cites: ["jones1985"],
  tags: [
    "lean-infrastructure",
    "track-C-n-strand",
    "typed-b3",
    "sub-braid-extraction",
    "axiomatic-reduction",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/probe_q_beta_operator_valued_N3.py",
    witness: [
      "computations/q-beta-operator-valued-N3.witness.json"
    ],
    status: "experimental",
  },
  authorNotes: [
    {
      kind: "status",
      body: "Lean stub: **no `sorry`s**. The chain is fully proved conditionally on\nthe single remaining axiom (`DominantSubBraidAtEps6`). All other\nsubstantive content is Lean-theorem-closed.",
    },
  ],
});
