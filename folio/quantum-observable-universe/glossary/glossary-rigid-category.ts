import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-rigid-category",
  title: "Rigid category",
  tags: ["glossary", "category-theory", "monoidal", "duality"],
  uses: ["rem:glossary-left-dual", "rem:glossary-right-dual"],
  defines: ["rigid-category"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Mathlib reference.**\n`CategoryTheory.RigidCategory` (class).\nImport: `Mathlib.CategoryTheory.Monoidal.Rigid.Basic`." },
  ],
});
