import { proof } from "../../schema/builders";

export default proof({
  label: "prf:prolonged-periods-fixed-depth",
  title: "Proof that a fixed-depth recurrence for the prolonged periods exists",
  uses: [
    "prop:prolonged-periods-fixed-depth",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): where the middle step is `mul_smul_comm` (scalars commute past the operator product) ... (`map_sum`, `map_smul`)" },
  ],
});
