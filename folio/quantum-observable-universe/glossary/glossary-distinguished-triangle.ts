import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-distinguished-triangle",
  title: "Distinguished triangle",
  tags: ["glossary", "homological-algebra", "triangulated"],
  uses: ["rem:glossary-r-linear-category"],
  defines: ["distinguished-triangle"],
  authorNotes: [
    {
      kind: "note",
      body: "Mathlib reference: `CategoryTheory.Pretriangulated.Triangle` (structure) and `CategoryTheory.Pretriangulated` (class, field `distinguishedTriangles`) in `Mathlib.CategoryTheory.Triangulated.Pretriangulated`.",
    },
  ],
});
