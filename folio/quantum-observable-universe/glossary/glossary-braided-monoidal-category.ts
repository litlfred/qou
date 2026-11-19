import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-braided-monoidal-category",
  title: "Braided monoidal category",
  tags: ["glossary", "category-theory", "monoidal"],
  uses: ["rem:glossary-monoidal-category"],
  defines: ["braided-monoidal-category"],
  authorNotes: [
    {
      kind: "note",
      body: "Mathlib reference: `CategoryTheory.BraidedCategory` (class) in `Mathlib.CategoryTheory.Monoidal.Braided.Basic`, notation `β_ X Y` for `braiding X Y`.",
    },
  ],
});
