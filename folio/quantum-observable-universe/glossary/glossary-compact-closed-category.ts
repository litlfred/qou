import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-compact-closed-category",
  title: "Compact closed category",
  tags: ["glossary", "category-theory", "monoidal", "duality"],
  uses: ["rem:glossary-symmetric-monoidal-category", "rem:glossary-rigid-category"],
  defines: ["compact-closed-category"],
  authorNotes: [
    {
      kind: "note",
      body: "Mathlib reference: `CategoryTheory.CompactClosedCategory` (class) in `Mathlib.CategoryTheory.Closed.Monoidal`.",
    },
  ],
});
