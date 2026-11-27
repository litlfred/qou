import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-compact-closed-category",
  title: "Compact closed category",
  tags: ["glossary", "category-theory", "monoidal", "duality"],
  uses: ["rem:glossary-symmetric-monoidal-category", "rem:glossary-rigid-category"],
  defines: ["compact-closed-category"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Mathlib reference.**\n`CategoryTheory.CompactClosedCategory` (class).\nImport: `Mathlib.CategoryTheory.Closed.Monoidal`." },
  ],
});
