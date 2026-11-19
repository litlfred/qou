import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:knot-particle-correspondence",
  label: "rem:knot-particle-dictionary",
  title: "Knot–particle dictionary",
  tags: [
    "knot",
    "particle",
    "dictionary",
    "mass",
    "borromean",
    "fermion",
    "boson",
    "torus-knot",
    "jones-polynomial",
  ],
  uses: [
    "def:localized-knot",
    "prop:knot-eigenbasis-complete",
    "rem:building-block-knots",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
});
