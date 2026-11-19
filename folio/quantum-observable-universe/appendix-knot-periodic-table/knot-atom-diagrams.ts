import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:stable-nucleus",
  label: "rem:knot-atom-diagrams",
  title:
    "Knot diagrams of light atoms ($Z \\leq 4$)",
  tags: [
    "knot-diagram",
    "trefoil",
    "hopf-link",
    "sub-link",
    "atom",
    "transfer-matrix",
    "antineutrino",
    "borromean",
  ],
  uses: ["prop:shell-structure-eigenvalues"],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: ["computations/q-pinning-50-digit.witness.json"],
    status: "verified",
  },
});
