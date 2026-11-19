import { remark } from "../../schema/builders";

export default remark({
  label: "rem:schrodinger-color-falsifiability",
  title:
    "Schrödinger's color metric, diminishing returns, and a falsifiable $q_0$ prediction",
  interprets: "rem:q-chromaticity",
  tags: [
    "color",
    "chromaticity",
    "color-perception",
    "schrodinger",
    "weber-fechner",
    "falsifiability",
    "non-riemannian",
    "skein",
    "substrate-parameter",
  ],
  uses: ["rem:q-chromaticity"],
  cites: ["bujack2022", "schrodinger1920color"],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
});
