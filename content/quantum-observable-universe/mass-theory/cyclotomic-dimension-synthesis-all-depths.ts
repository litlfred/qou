import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cyclotomic-dimension-synthesis-all-depths",
  proofs: ["prf:cyclotomic-dimension-synthesis-all-depths"],
  title:
    "Cyclotomic dimension synthesis at every depth: $(K - 3)/2$ for $n$ odd, $(K - 1)/2$ for $n$ even",
  lean: {
    ref: "qou:QOU.BraidKnot.CyclotomicDimensionSynthesisAllDepths.dimension_synthesis_all_depths",
    validation: "not_checked",
  },
  uses: ["prop:cyclotomic-depth3-dimension-synthesis"],
  cites: ["bloch2000", "zagier1986"],
  tags: [
    "cyclotomic",
    "dimension-synthesis",
    "all-depths",
    "borel-saturation",
    "beilinson-conditional",
    "bloch-suslin-unconditional",
    "graded-mikusinski",
    "theorem-level",
  ],
});
