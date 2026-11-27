import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-monoidal-functor",
  title: "Monoidal functor",
  tags: ["glossary", "category-theory", "monoidal"],
  uses: ["rem:glossary-monoidal-category"],
  defines: ["monoidal-functor"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Mathlib distinguishes lax monoidal functors (arbitrary morphisms) from strong monoidal functors (isomorphisms)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Mathlib reference.**\n`CategoryTheory.Functor.LaxMonoidal` (class).\n`CategoryTheory.Functor.Monoidal` (class) for strong monoidal.\nImport: `Mathlib.CategoryTheory.Monoidal.Functor`." },
  ],
});
