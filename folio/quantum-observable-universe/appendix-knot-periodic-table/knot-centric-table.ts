import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:shell-transition-knot",
  label: "rem:knot-centric-table",
  title:
    "Knot-centric periodic table: reorganization by nuclear and electronic knot structure",
  tags: [
    "periodic-table",
    "knot-centric",
    "visualization",
    "nuclear-shell",
    "borromean",
    "magic-receptive",
    "transfer-matrix",
    "skein-polynomial",
  ],
  uses: [
    "prop:shell-structure-eigenvalues",
    "thm:generation-completeness",
    "rem:knot-exhaustiveness",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: ["computations/q-pinning-50-digit.witness.json"],
    status: "verified",
  },
});
