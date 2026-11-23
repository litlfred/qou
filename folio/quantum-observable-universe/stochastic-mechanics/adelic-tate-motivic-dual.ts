import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:arc-space",
  label: "rem:adelic-tate-motivic-dual",
  title:
    "Motivic dual of the adelic zeta factorisation via the arc space and motivic measure",
  uses: [
    "def:arc-space",
    "rem:adelic-tate-squeeze",
    "rem:bsd-surreal-bound",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The leading-coefficient form of [BSD surreal bound](#rem:bsd-surreal-bound) is the motivic-measure read of the same data on $\\mathcal{L}(\\mathcal{E}_q)$." },
  ],
  tags: [
    "adeles",
    "motivic-integration",
    "arc-space",
    "tate-thesis",
    "surreal",
  ],
  cites: [
    "kontsevich1995",
    "denef-loeser2001",
  ],
});
