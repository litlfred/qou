import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cyclotomic-dimension-synthesis-all-depths",
  title:
    "Cyclotomic dimension synthesis at every depth: $(K - 3)/2$ for $n$ odd, $(K - 1)/2$ for $n$ even",
  uses: [
    "prop:jonquiere-cyclotomic-tate-rationality",
    "prop:cyclotomic-orbit-sum-all-depths",
    "prop:cyclotomic-depth3-dimension-synthesis",
    "prop:cl3-zeta5-pslq-independence",
    "prop:borel-partial-resolution",
    "prop:depth-2-identification-bloch-suslin",
    "rem:b1-current-status",
  ],
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
