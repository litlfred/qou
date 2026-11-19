import { proof } from "../../schema/builders";

export default proof({
  label: "prf:weak-vertex-left-projector",
  title: "Proof of the weak vertex insertion identity",
  uses: ["prop:weak-vertex-left-projector"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Lean declarations: `weakVertex_sub_letter`, `insertion_mul_rightLine`, `one_sided_iff_smul_leftLine`, `skein_dominant_root`; right-line trace obstruction `kills_right_iff` and `normalised_eq_augmentation` in `QOU/QuarkState/RightLineTraceObstruction.lean`.",
    },
  ],
});
