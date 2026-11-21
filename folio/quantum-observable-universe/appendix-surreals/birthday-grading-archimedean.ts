import { remark } from "../../schema/builders";

export default remark({
  label: "rem:birthday-grading-archimedean",
  title: "Birthday grading as a depth gauge and its archimedean sub-category",
  interprets: "def:birthday-grading",
  tags: [
    "surreal-numbers",
    "birthday",
    "archimedean",
    "grading",
    "filtration",
  ],
  uses: [
    "def:birthday-grading",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The relaxed axioms ([infinitesimal Frobenius](#conj:infinitesimal-frobenius)) allow corrections of the form $\\mathrm{id} + O(\\varepsilon)$. These corrections live at birthday $\\leq \\omega$ but are distinguished from the classical $\\mathrm{id}$ by having a non-zero standard part for the $\\varepsilon$-coefficient." },
  ],
});
