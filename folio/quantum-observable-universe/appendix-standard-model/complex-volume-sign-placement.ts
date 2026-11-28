import { proposition } from "../../schema/builders";

/**
 * The Chern-Simons part of the complex volume can carry the hypercharge sign only on a chiral
 * knot complement, where the bit becomes the knot's mirror choice; it is blind on UT(Sigma4).
 */
export default proposition({
  label: "prop:complex-volume-sign-placement",
  title: "Where the complex volume can carry the hypercharge sign",
  uses: [
    "prop:hypercharge-sign-is-bring-orientation",
    "prop:braid-chirality-blind-to-hypercharge-sign",
  ],
  lean: {
    ref: "qou:QOU.StandardModel.ComplexVolumeSign.mirror_flips_readout",
  },
  tags: ["appendix", "standard-model", "brings-surface", "chirality"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Sorry-free (`ComplexVolumeSignPlacement.lean`). CS is abstract and orientation-odd; " +
        "no analytic value enters. Places the sign bit in the matter knot's mirror choice; " +
        "does not fix it. Owner idea 2026-11-28. Bean qou-h0zz.",
    },
  ],
});
