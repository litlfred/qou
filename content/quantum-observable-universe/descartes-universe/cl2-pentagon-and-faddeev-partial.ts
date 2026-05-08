import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cl2-pentagon-and-faddeev-partial",
  title:
    "Partial closures: $\\mathrm{Cl}_2$ pentagon at boundary + Faddeev-Kashaev limit at boundary (closes parts of substantive Mathlib gaps 2+3)",
  uses: [
    "rem:three-substantive-mathlib-fillers",
    "rem:clausen-function-mathlib-filler",
    "conj:dilogarithm-archimedean-limit",
  ],
  cites: ["zagier1986", "faddeev1994", "kashaev1997"],
  tags: [
    "mathlib-filler",
    "cl2-pentagon",
    "faddeev-kashaev",
    "boundary-case",
    "lean-construction",
    "partial-closure",
  ],
  lean: {
    ref: "qou:QOU.Descartes.PartialClosures.partial_closures_at_boundary",
    validation: "not_checked",
  },
});
