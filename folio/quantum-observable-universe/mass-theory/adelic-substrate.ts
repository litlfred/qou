import { definition } from "../../schema/builders";

export default definition({
  label: "def:adelic-substrate",
  title: "Adelic substrate $\\mathbb{A}$",
  tags: ["adeles", "macroscopic-limit", "global", "non-archimedean"],
  uses: [],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): , accessible only through the\n[classical limit functor](#def:classical-limit-functor) and the\n[archimedean realization functor](#def:archimedean-realization-functor)" },
  ],
  cites: ["tate1967"],
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.AdelicSubstrate",
    validation: "not_checked",
  },
});
