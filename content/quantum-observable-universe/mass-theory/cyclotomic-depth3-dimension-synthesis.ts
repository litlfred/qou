import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cyclotomic-depth3-dimension-synthesis",
  proofs: ["prf:cyclotomic-depth3-dimension-synthesis"],
  title:
    "Cyclotomic depth-3 dimension synthesis: $(K - 3)/2$ at every prime $K \\geq 5$",
  lean: {
    ref: "qou:QOU.BraidKnot.CyclotomicDepth3DimensionSynthesis.dimension_synthesis_upper_bound",
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    script: "computations/cyclotomic_depth3_dimension_pslq.py",
    witness:
      "computations/cyclotomic-depth3-dimension-pslq.witness.json",
    status: "verified",
  },
  uses: ["prop:two-filtration-bridge-general"],
  cites: ["bloch2000", "zagier1986"],
  tags: [
    "cyclotomic",
    "depth-3-dimension",
    "borel-saturation",
    "beilinson-conditional",
    "K-5-certified",
    "K-7-certified",
    "synthesis",
    "graded-mikusinski",
    "theorem-level",
  ],
});
