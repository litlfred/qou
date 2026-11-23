import { proof } from "../../schema/builders";

export default proof({
  label: "prf:skein-polynomial-transfer-matrix",
  title: "Proof of skein polynomial transfer matrix",
  uses: ["prop:skein-polynomial-transfer-matrix"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The 2-jet cross-term $\\Delta_{p_1 p_2}$\n([generator volume decomposition](#prop:generator-volume-decomposition))\ncorresponds to the **interference** between two Skein\npolynomial modifications.  In the polynomial language:" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([jet expansion](#prop:generator-volume-decomposition))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([transition energy](#def:Q-value-transition))" },
  ],
});
