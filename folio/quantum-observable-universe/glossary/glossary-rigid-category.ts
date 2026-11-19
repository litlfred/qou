import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-rigid-category",
  title: "Rigid category",
  tags: ["glossary", "category-theory", "monoidal", "duality"],
  uses: ["rem:glossary-left-dual", "rem:glossary-right-dual"],
  defines: ["rigid-category"],
  authorNotes: [
    {
      kind: "note",
      body: "Mathlib reference: `CategoryTheory.RigidCategory` (class) in `Mathlib.CategoryTheory.Monoidal.Rigid.Basic`.",
    },
  ],
});
