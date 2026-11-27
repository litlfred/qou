import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-pivotal-category",
  title: "Pivotal category",
  tags: ["glossary", "category-theory", "monoidal", "duality"],
  uses: ["rem:glossary-rigid-category"],
  defines: ["pivotal-category"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Mathlib reference.** None — there is no `CategoryTheory.PivotalCategory`. Mathlib's `Mathlib.CategoryTheory.Monoidal.Rigid.Basic` lists *\"Define pivotal categories (rigid categories equipped with a natural isomorphism `ᘁᘁ ≅ 𝟙 C`)\"* under its **Future work** heading, and supplies only the rigid layer: `ExactPairing`, `rightAdjointMate`, `comp_rightAdjointMate`.\n\nThe classes this paper needs are therefore built in-repo, as `PivotalStructure` and `SphericalStructure` in [`QOU/BraidKnot/KeystonePivotalSpherical.lean`](../lean/QOU/BraidKnot/KeystonePivotalSpherical.lean). They are kept **separate** there for the reason above: `leftQDim` is defined with the inverse braiding and is a genuinely different morphism from `qDimObj`, so sphericality is a real hypothesis rather than a consequence of the pivotor." },
  ],
});
