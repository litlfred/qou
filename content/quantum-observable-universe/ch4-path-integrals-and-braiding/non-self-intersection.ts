import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:non-self-intersection",
  title: "Obstruction to self-intersection",
  hasProof: true,
  tags: ["self-avoidance", "r-matrix", "non-cocommutativity", "knot-energy"],
  uses: [
    "prop:mobius-energy",
    "rem:r-matrix-braiding",
    "def:q-hodge-star",
    "def:substrate-parameter",
  ],
  lean: {
    decl: "QOU.NonSelfIntersection",
    validation: "not_checked",
  },
  rendered: [
    { mime: "image/svg+xml", url: "rendered/non-self-intersection-0.svg", blockIndex: 0, hash: "5471f3de17cb" },
  ],
});
