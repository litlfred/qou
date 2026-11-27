import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-derived-category",
  title: "Derived category",
  tags: ["glossary", "homological-algebra", "derived"],
  uses: ["rem:glossary-distinguished-triangle"],
  defines: ["derived-category"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Mathlib reference.**\n`DerivedCategory C` (the localisation of `HomotopyCategory C (ComplexShape.up ℤ)` at quasi-isomorphisms).\nImport: `Mathlib.Algebra.Homology.DerivedCategory.Basic`." },
  ],
});
