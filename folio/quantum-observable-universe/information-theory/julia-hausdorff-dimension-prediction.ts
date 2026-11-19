import { remark } from "../../schema/builders";

export default remark({
  label: "rem:julia-hausdorff-dimension-prediction",
  interprets: "def:gravitational-constant",
  title: "Hausdorff-dimension prediction $d_H(q)$ of the Reeb Julia set",
  tags: [
    "hausdorff-dimension",
    "julia-set",
    "information-theory",
    "mcmullen",
    "testable-prediction",
    "gravitational-constant",
  ],
  uses: [
    "def:gravitational-constant",
    "prop:descent-eigenspaces",
  ],
  cites: [
    "mcmullen1998",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: ["computations/q-pinning-50-digit.witness.json"],
    status: "verified",
  },
});
