import { proposition } from "../../schema/builders";

/**
 * In the reflection-odd copy of H1(Bring), colour and isospin symmetry of hypercharge
 * survives, and orientation reversal flips its sign: the open sign is the orientation.
 */
export default proposition({
  label: "prop:hypercharge-sign-is-bring-orientation",
  title: "The hypercharge sign is the orientation of Bring's surface",
  uses: ["prop:bring-twist-flips-hypercharge", "prop:bring-reflection-parity"],
  lean: {
    ref: "qou:QOU.StandardModel.BringOrientation.minus_copy_restores_colour_isospin",
  },
  tags: ["appendix", "standard-model", "brings-surface"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Sorry-free (`HyperchargeSignIsBringOrientation.lean`), checked on generators of " +
        "S3 x S2. Identifies the open sign with the orientation of Bring's surface; does " +
        "not fix its value, since both orientations are isometric. Uses H1 = [2,1,1,1]+ " +
        "plus [2,1,1,1]- from PR #9874. Bean qou-h0zz.",
    },
  ],
});
