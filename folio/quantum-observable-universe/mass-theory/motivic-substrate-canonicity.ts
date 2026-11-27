import { remark } from "../../schema/builders";

export default remark({
  label: "rem:motivic-base-ring-canonicity",
  renamedFrom: ["rem:motivic-substrate-canonicity"],
  title: "Canonicity, realizations, and scope of the motivic base ring",
  interprets: "def:motivic-base-ring",
  tags: [
    "motivic",
    "substrate",
    "realization-tower",
    "adelic",
    "habiro",
  ],
  uses: [
    "def:motivic-base-ring",
    "def:frobenius-hopf-aether",
    "def:adelic-base-ring",
    "def:arc-space",
    "def:motivic-mass-measure",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): - The [adelic substrate](#def:adelic-base-ring) is the place-decomposition $\\mathbb{A} = \\mathbb{R} \\times \\prod_p' \\mathbb{Q}_p$ indexing the realization tower. The adelic decomposition of a motivic class is the restricted product $\\rho_{\\mathrm{tot}}([X]) = (\\rho_v([X]))_v$." },
  ],
  cites: ["kontsevich1995", "denef-loeser2001"],
});
