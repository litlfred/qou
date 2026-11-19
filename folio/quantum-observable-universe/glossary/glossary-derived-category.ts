import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-derived-category",
  title: "Derived category",
  tags: ["glossary", "homological-algebra", "derived"],
  uses: ["rem:glossary-distinguished-triangle"],
  defines: ["derived-category"],
  authorNotes: [
    {
      kind: "note",
      body: "Mathlib reference: `DerivedCategory C` (localisation of `HomotopyCategory C (ComplexShape.up ℤ)` at quasi-isomorphisms) in `Mathlib.Algebra.Homology.DerivedCategory.Basic`.",
    },
  ],
});
