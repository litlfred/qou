import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-hom-set",
  title: "Hom-set",
  tags: ["glossary", "category-theory"],
  uses: [],
  defines: ["hom-set"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Mathlib reference.**\nWe denote the hom-set from `X` to `Y` by `X ⟶ Y`.\nImport: `Mathlib.Combinatorics.Quiver.Basic` (re-exported by `Mathlib.CategoryTheory.Category.Basic`).\nThe type is `Quiver.Hom X Y`: `CategoryTheory.Category` extends `CategoryTheory.CategoryStruct`, which extends `Quiver`, whose `Hom` field carries the morphism types, and `⟶` is notation for `Quiver.Hom`." },
  ],
});
