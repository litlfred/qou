import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-closure-map-axiomatic",
  title:
    "Track C Step B: factorise the Markov-closure → Hopf-link content into two atomic Lean axioms (closure type at k=2 + classical Jones value), reducing the open content to a smaller surface",
  interprets: "prop:q-beta-c3-hopf-three-fold-markov",
  uses: [
    "prop:q-beta-c3-hopf-three-fold-markov",
    "rem:F3-eps6-leading-eq-neg-2b-cubed",
  ],
  cites: ["jones1985"],
  tags: [
    "lean-infrastructure",
    "track-C-step-B",
    "markov-closure",
    "hopf-link",
    "axiomatic-reduction",
  ],
});
