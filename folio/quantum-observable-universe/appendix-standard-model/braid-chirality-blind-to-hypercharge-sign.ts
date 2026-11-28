import { proposition } from "../../schema/builders";

/**
 * Lifts of base isometries to UT(Sigma_4) preserve orientation, so braid crossing signs
 * cannot see Bring's orientation, and hence cannot fix the hypercharge sign.
 */
export default proposition({
  label: "prop:braid-chirality-blind-to-hypercharge-sign",
  title: "Braid chirality on the unit tangent bundle cannot fix the hypercharge sign",
  uses: ["prop:hypercharge-sign-is-bring-orientation"],
  lean: {
    ref: "qou:QOU.StandardModel.BraidChiralityBlind.no_equivariant_hypercharge_from_UT",
  },
  tags: ["appendix", "standard-model", "brings-surface"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Sorry-free (`BraidChiralityBlindToHyperchargeSign.lean`). Excludes the UT(Sigma_4) " +
        "crossing-sign route (geodesic alpha, q0 > 1; `BringUTContactChirality.lean`) as a " +
        "source of the hypercharge sign. A source seeing the base orientation directly is " +
        "not excluded. Bean qou-h0zz.",
    },
  ],
});
