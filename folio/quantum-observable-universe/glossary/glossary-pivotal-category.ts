import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-pivotal-category",
  title: "Pivotal category",
  tags: ["glossary", "category-theory", "monoidal", "duality"],
  uses: ["rem:glossary-rigid-category"],
  defines: ["pivotal-category"],
  authorNotes: [
    {
      kind: "note",
      body: "Mathlib has no `CategoryTheory.PivotalCategory` (`Mathlib.CategoryTheory.Monoidal.Rigid.Basic` supplies `ExactPairing`, `rightAdjointMate`, `comp_rightAdjointMate`). Built in-repo as separate classes `PivotalStructure` and `SphericalStructure` in `QOU/BraidKnot/KeystonePivotalSpherical.lean` (`leftQDim` uses the inverse braiding and differs from `qDimObj`).",
    },
  ],
});
