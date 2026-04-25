import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:non-self-intersection",
  lean: { ref: "qou:QOU.Braiding.non_self_intersection",
    validation: "not_checked",
  },
  title: "Obstruction to self-intersection",
  tags: ["self-avoidance", "r-matrix", "non-cocommutativity", "knot-energy"],
  uses: [
    "prop:mobius-energy",
    "rem:r-matrix-braiding",
  ],
  proofs: ["prf:non-self-intersection"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/non-self-intersection-0.svg", blockIndex: 0, hash: "5471f3de17cb" },
  ],
});
