import { proof } from "../../schema/builders";

export default proof({
  label: "prf:confinement-phase-stratification",
  title: "Proof of confinement phase stratification",
  uses: ["prop:confinement-phase-stratification"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Both correspond precisely to the discrete-regime-switch phenomenology documented in [prop:parity-regime-selection](#thm:parity-regime-selection) and the [deconfinement golden threshold](#rem:deconfinement-golden-threshold)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): [prop:confinement-sdp](#prop:confinement-sdp)," },
  ],
});
