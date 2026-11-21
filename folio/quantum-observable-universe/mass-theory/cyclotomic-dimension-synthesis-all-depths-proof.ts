import { proof } from "../../schema/builders";

export default proof({
  label: "prf:cyclotomic-dimension-synthesis-all-depths",
  title: "Proof of cyclotomic dimension synthesis all depths",
  uses: ["prop:cyclotomic-dimension-synthesis-all-depths"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Depth-2 identification of $G^{(2)}(\\mathcal{H}_q)$ with $K_3^{\\mathrm{ind}}(F) \\otimes \\mathbb{Q}$](#prop:depth-2-identification-bloch-suslin))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Borel's theorem partially discharges the depth correspondence's sharpness target — explicit dimensions](#prop:borel-partial-resolution))" },
  ],
});
