import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-dg-category",
  title: "Differential graded category",
  tags: ["glossary", "homological-algebra", "dg"],
  uses: ["rem:glossary-derived-category"],
  defines: ["dg-category"],
  authorNotes: [
    {
      kind: "note",
      body: "Mathlib reference: none for dg-enriched categories; underlying complexes are `HomologicalComplex` and `CochainComplex` in `Mathlib.Algebra.Homology.HomologicalComplex`.",
    },
  ],
});
