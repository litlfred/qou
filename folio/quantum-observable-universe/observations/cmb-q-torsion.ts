import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:substrate-parameter",
  label: "rem:cmb-q-torsion",
  title: "CMB non-uniformity from $q$-torsion",
  uses: ["ex:q-torsion-leaf"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Descartes CMB](#rem:cmb-photon-color-content))" },
  ],
  tags: ["cmb", "torsion", "observation"],
});
