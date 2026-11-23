import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-dg-category",
  title: "Differential graded category",
  tags: ["glossary", "homological-algebra", "dg"],
  uses: ["rem:glossary-derived-category"],
  defines: ["dg-category"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Mathlib reference.**\nNone for the dg-enriched notion. The underlying complexes are `HomologicalComplex` and `CochainComplex`.\nImport: `Mathlib.Algebra.Homology.HomologicalComplex`." },
  ],
});
