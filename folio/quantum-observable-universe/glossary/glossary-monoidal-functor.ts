import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-monoidal-functor",
  title: "Monoidal functor",
  tags: ["glossary", "category-theory", "monoidal"],
  uses: ["rem:glossary-monoidal-category"],
  defines: ["monoidal-functor"],
  authorNotes: [
    {
      kind: "note",
      body: "Mathlib reference: `CategoryTheory.Functor.LaxMonoidal` (lax) and `CategoryTheory.Functor.Monoidal` (strong) in `Mathlib.CategoryTheory.Monoidal.Functor`.",
    },
  ],
});
