import { proposition } from "../../schema/builders";

/**
 * Quaternion conjugation reverses the orientation of the Bring cone and swaps left and right
 * multiplication but keeps the chirality grading; L_w composed with it flips both.
 */
export default proposition({
  label: "prop:quaternion-conjugation-orientation",
  title: "Quaternion conjugation, orientation and the cone chirality",
  uses: ["prop:hypercharge-sign-is-bring-orientation", "prop:complex-volume-sign-placement"],
  lean: {
    ref: "qou:QOU.Tetraplectic.leftMul_star_flips",
  },
  tags: ["brings-surface", "quaternions", "chirality"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Sorry-free (`QuaternionConjugationOrientation.lean`, generic CommRing). Whether " +
        "Bring's reflection acts on the cone as star or as L_w star is open, because the " +
        "S5 x C2 action on the cone is not established. Owner idea 2026-11-28. Bean qou-h0zz.",
    },
  ],
});
