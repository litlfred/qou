import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-exact-pairing",
  title: "Exact pairing",
  tags: ["glossary", "category-theory", "monoidal", "duality"],
  uses: ["rem:glossary-monoidal-category"],
  authorNotes: [
    {
      kind: "note",
      body: "Mathlib reference: `CategoryTheory.ExactPairing` (class) in `Mathlib.CategoryTheory.Monoidal.Rigid.Basic`.",
    },
  ],
});
