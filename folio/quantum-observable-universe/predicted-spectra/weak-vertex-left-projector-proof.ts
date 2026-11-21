import { proof } from "../../schema/builders";

export default proof({
  label: "prf:weak-vertex-left-projector",
  title: "Proof of the weak vertex insertion identity",
  uses: ["prop:weak-vertex-left-projector"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean declarations are `kills_right_iff` and `normalised_eq_augmentation` in `QOU/QuarkState/RightLineTraceObstruction.lean`." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean declarations are `weakVertex_sub_letter`, `insertion_mul_rightLine`, `one_sided_iff_smul_leftLine` and `skein_dominant_root`." },
  ],
});
