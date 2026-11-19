import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-hom-set",
  title: "Hom-set",
  tags: ["glossary", "category-theory"],
  uses: [],
  defines: ["hom-set"],
  authorNotes: [
    {
      kind: "note",
      body: "Mathlib reference: `X ⟶ Y` (`Quiver.Hom X Y`) in `Mathlib.Combinatorics.Quiver.Basic` (re-exported by `Mathlib.CategoryTheory.Category.Basic`), via `CategoryTheory.Category` -> `CategoryTheory.CategoryStruct` -> `Quiver`.",
    },
  ],
});
