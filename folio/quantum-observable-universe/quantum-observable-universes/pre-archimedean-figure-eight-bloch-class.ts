import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pre-archimedean-figure-eight-bloch-class",
  title:
    "The figure-eight Nahm equation gives a class in the Bloch group of $\\mathbb{Q}(\\sqrt{-3})$",
  lean: {
    ref: "qou:QOU.Archimedean.PreArchimedeanBloch.fig8Class_cyclotomic",
    validation: "not_checked",
  },
  uses: [
    "prop:bloch-group-quotient-construction",
    "rem:q-dilog-habiro-ring",
  ],
  cites: ["suslin1991", "zagier-dilogarithm", "garoufalidis-scholze-wheeler-zagier2024"],
  tags: ["bloch-group", "habiro-ring", "figure-eight-knot", "pre-archimedean", "dilogarithm"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-27",
      body:
        "Lean: `QOU/MassTheory/PreArchimedeanBloch.lean` (namespace `QOU.Archimedean.PreArchimedeanBloch`), sorry-free, lean-direct exit 0; axioms `propext`, `Classical.choice`, `Quot.sound`. Statements used here: `habiro41_succ`, `nahm41_iff_phi6`, `nahm41_mem_blochGroup`, `delta_gen_of_phi6`, `fig8Class_mem_blochGroup`, `fig8Class_cyclotomic`. Owner chose this Stage A block on 2026-11-27 (audit `docs/audits/2026-11-27-dilog-bloch-pre-archimedean.md`).",
    },
  ],
});
