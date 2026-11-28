import { proposition } from "../../schema/builders";

/**
 * Consolidates the matter-content inputs: with five odd strands, the even
 * exterior part is 1 + 10 + 5bar and the odd part is its conjugate. One Z/2
 * sign (which part is matter) replaces Fermi exchange, the 5bar:10 ratio,
 * anomaly cancellation and the vector-like exclusion.
 */
export default proposition({
  label: "prop:even-strand-generation",
  title: "One generation is the even part of five odd strands",
  uses: ["prop:fermi-pair-wedge", "prop:hecke-sign-channel-is-fermi"],
  cites: ["baez-huerta2010"],
  lean: {
    ref: "qou:QOU.StandardModel.OddExterior.evenExterior_cubic",
  },
  tags: ["appendix", "standard-model", "hypercharge", "fermi-statistics", "anomaly"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-27",
      body:
        "Sorry-free (`OddExteriorAnomalyFreedom.lean`, even-part section). Input " +
        "left: the Z/2 sign choosing the even part as matter (chirality). That " +
        "strands are odd follows from chirality (prop:odd-strands-force-chirality). " +
        "Owner: try to derive the sign from upstream. Bean qou-h0zz.",
    },
  ],
});
