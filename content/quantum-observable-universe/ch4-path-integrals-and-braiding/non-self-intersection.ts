import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:non-self-intersection",
  title: "Obstruction to self-intersection",
  hasProof: false,
  tags: ["self-avoidance", "r-matrix", "non-cocommutativity", "knot-energy"],
  uses: [
    "prop:mobius-energy",
    "rem:r-matrix-braiding",
    "def:q-hodge-star",
    "def:substrate-parameter",
  ],
});
