import { remark } from "../../schema/builders";

export default remark({
  label: "rem:motivic-substrate-canonicity",
  title: "Canonicity, realizations, and scope of the motivic substrate",
  interprets: "def:motivic-substrate",
  tags: [
    "motivic",
    "substrate",
    "realization-tower",
    "adelic",
    "habiro",
  ],
  uses: [
    "def:motivic-substrate",
    "def:frobenius-hopf-substrate",
    "def:adelic-substrate",
    "def:arc-space",
    "def:motivic-mass-measure",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): - The [adelic substrate](#def:adelic-substrate) is the place-decomposition $\\mathbb{A} = \\mathbb{R} \\times \\prod_p' \\mathbb{Q}_p$ indexing the realization tower. The adelic decomposition of a motivic class is the restricted product $\\rho_{\\mathrm{tot}}([X]) = (\\rho_v([X]))_v$." },
  ],
  cites: ["kontsevich1995", "denef-loeser2001"],
});
