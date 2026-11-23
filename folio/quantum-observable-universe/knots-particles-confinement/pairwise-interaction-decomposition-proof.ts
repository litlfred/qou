import { proof } from "../../schema/builders";

export default proof({
  label: "prf:pairwise-interaction-decomposition",
  title: "Proof of the pairwise decomposition of interactions",
  uses: ["prop:pairwise-interaction-decomposition"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean structure\n\nThe formalization is [`pairwise-interaction-decomposition.lean`](pairwise-interaction-decomposition.lean), namespace `QOU.Braiding`. The declaration `pairwise_interaction_decomposition` is the conjunction of all three parts, each proved separately.\n\nParts 1 and 2 are inherited from Mathlib's braided-category library: `composite_crossing_eq_two_elementary` is `braiding_tensor_left_hom`, and `triple_crossing_route_independent` is `yang_baxter`.\n\nPart 3 is proved from scratch. The locality step is `AdjSwap.eq_of_reverses`, the per-letter bound is `card_crossedPairs_step`, the induction is `card_crossedPairs_le_length`, and the conclusion is `card_allPairs_le_length`; the pair count $|P| = \\binom{n}{2}$ is `card_allPairs`. The three-strand instance is `three_crossings_needed`.\n\nEvery declaration depends only on `propext`, `Classical.choice`, and `Quot.sound`." },
  ],
});
