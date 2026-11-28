import { proposition } from "../../schema/builders";

/**
 * Removes "the strand count is odd" as an input: for n strands, the matter part
 * (even exterior part) is closed under conjugation iff n is even, and then it is
 * vector-like. Chiral matter is equivalent to odd n.
 */
export default proposition({
  label: "prop:odd-strands-force-chirality",
  title: "Chiral matter forces an odd number of strands",
  uses: ["prop:even-strand-generation"],
  lean: {
    ref: "qou:QOU.StandardModel.OddStrands.evenPart_dichotomy",
  },
  tags: ["appendix", "standard-model", "chirality", "anomaly"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-27",
      body:
        "Sorry-free (`OddStrandsForceChirality.lean`), general n. Oddness now " +
        "follows from chirality. Still open: why n = 5 rather than another odd " +
        "number, and the chirality sign. Bean qou-h0zz.",
    },
  ],
});
