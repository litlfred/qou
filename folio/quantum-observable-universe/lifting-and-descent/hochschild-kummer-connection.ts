import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-characteristic-classes",
  label: "rem:hochschild-kummer-connection",
  title: "The Hochschild--Kummer connection",
  tags: [
    "kummer",
    "hochschild",
    "hkr",
    "deformation",
    "obstruction",
    "motivic-galois",
  ],
  uses: [
    "def:hochschild-homology",
    "def:quantum-characteristic-classes",
    "def:motivic-substrate",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): , [Descartes Yekutieli](#ex:archimedean-yekutieli)" },
  ],
  cites: ["yekutieli2010"],
});
