import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-braided-monoidal-category",
  title: "Braided monoidal category",
  tags: ["glossary", "category-theory", "monoidal"],
  uses: ["rem:glossary-monoidal-category"],
  defines: ["braided-monoidal-category"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Mathlib reference.**\n`CategoryTheory.BraidedCategory` (class).\nImport: `Mathlib.CategoryTheory.Monoidal.Braided.Basic`.\nNotation: `β_ X Y` for `braiding X Y`." },
  ],
});
