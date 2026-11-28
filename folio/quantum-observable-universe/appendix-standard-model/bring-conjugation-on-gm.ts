import { proposition } from "../../schema/builders";

/**
 * Complex conjugation equals inversion on the unit circle of Gm but fixes a real
 * point q > 1, so Bring's complex structure ties to the Gm orientation only on the circle.
 */
export default proposition({
  label: "prop:bring-conjugation-on-gm",
  title: "Bring's complex conjugation on the multiplicative group",
  uses: ["prop:hypercharge-sign-is-bring-orientation", "prop:braid-chirality-blind-to-hypercharge-sign"],
  lean: {
    ref: "qou:QOU.StandardModel.BringConjGm.conj_eq_inv_of_normSq_one",
  },
  tags: ["appendix", "standard-model", "brings-surface"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Sorry-free (`BringConjugationOnGm.lean`). Which locus of Gm the chirality is read " +
        "on (unit circle / roots of unity, or the real anchor) is a modelling question left " +
        "open. Coordinates with the formal-groups thread (PR #9935). Bean qou-h0zz.",
    },
  ],
});
