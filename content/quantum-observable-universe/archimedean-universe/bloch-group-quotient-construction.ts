import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bloch-group-quotient-construction",
  title:
    "Concrete construction of $B(F)$ as `FreeAbelianGroup ⧸ pentagonSubgroup` (closes substantive Mathlib gap 1)",
  uses: [
    "rem:three-substantive-mathlib-fillers",
    "prop:archimedean-functor-uniqueness",
  ],
  cites: ["bloch2000", "suslin1991"],
  tags: [
    "mathlib-filler",
    "bloch-group",
    "free-abelian-group",
    "quotient-group",
    "pentagon-relation",
    "lean-construction",
  ],
  lean: {
    ref: "qou:QOU.Descartes.BlochQuotient.BlochGroup",
    validation: "not_checked",
  },
});
