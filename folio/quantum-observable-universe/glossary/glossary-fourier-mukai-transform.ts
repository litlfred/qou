import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-fourier-mukai-transform",
  title: "Fourier–Mukai transform",
  tags: ["glossary", "homological-algebra", "derived", "integral-transform"],
  uses: ["rem:glossary-derived-category"],
  defines: ["fourier-mukai-transform"],
  cites: ["orlov1997"],
  authorNotes: [
    {
      kind: "note",
      body: "Mathlib reference: none for Fourier–Mukai transforms (derived categories are `DerivedCategory` in `Mathlib.Algebra.Homology.DerivedCategory.Basic`; sheaf derived pushforward and derived tensor product are not formalised).",
    },
  ],
});
