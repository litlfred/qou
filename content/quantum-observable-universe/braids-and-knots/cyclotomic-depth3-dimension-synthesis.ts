import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cyclotomic-depth3-dimension-synthesis",
  title:
    "Cyclotomic depth-3 dimension synthesis: $(K - 3)/2$ at every prime $K \\geq 5$",
  lean: {
    ref: "qou:QOU.BraidKnot.CyclotomicDepth3DimensionSynthesis.dimension_synthesis_upper_bound",
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/cyclotomic_depth3_dimension_pslq.py",
    witness:
      "folio-assistant/computations/cyclotomic-depth3-dimension-pslq.witness.json",
    status: "verified",
  },
  uses: [
    "prop:cyclotomic-trilog-imaginary-closed-form",
    "prop:cyclotomic-cl3-orbit-sum-general",
    "prop:two-filtration-bridge-general",
    "prop:borel-partial-resolution",
    "prop:cl3-zeta5-pslq-independence",
    "rem:transcendental-accounting",
    "rem:b1-current-status",
  ],
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
