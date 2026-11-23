import { proof } from "../../schema/builders";

export default proof({
  label: "prf:frobenius-s-classification",
  title: "Proof of frobenius s classification",
  uses: ["prop:frobenius-s-classification"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (Lean, over a\ngeneric field: `chi_swap`, `barHom_hmul`, `primitives_barHom`,\n`chiRatio_inverts`.)" },
  ],
});
