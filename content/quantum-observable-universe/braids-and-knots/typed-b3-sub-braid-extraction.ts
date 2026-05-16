import { remark } from "../../schema/builders";

export default remark({
  label: "rem:typed-b3-sub-braid-extraction",
  title:
    "Track C n-strand: typed-B_3 sub-braid extraction reduces to the 2-strand chain via a single focused combinatorial axiom (`DominantSubBraidAtEps6`); composes to fully Lean-proved $c_3 = -2$",
  interprets: "prop:q-beta-c3-hopf-three-fold-markov",
  uses: [
    "prop:q-beta-c3-hopf-three-fold-markov",
    "rem:braid-link-types",
    "rem:markov-closure-map-axiomatic",
  ],
  cites: ["jones1985"],
  tags: [
    "lean-infrastructure",
    "track-C-n-strand",
    "typed-b3",
    "sub-braid-extraction",
    "axiomatic-reduction",
  ],
  computation: {
    witness: [
      "../../folio-assistant/computations/q-beta-cat-per-factor-decomposition.witness.json",
      "../../folio-assistant/computations/q-beta-operator-valued-N3.witness.json",
    ],
  },
});
