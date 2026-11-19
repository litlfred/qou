import { remark } from "../../schema/builders";

export default remark({
  label: "rem:binding-knots-visual-inventory",
  title: "Visual inventory of binding knots",
  interprets: "prop:knot-particle-correspondence",
  tags: [
    "knot",
    "diagram",
    "visual",
    "inventory",
    "unknot",
    "hopf-link",
    "trefoil",
    "figure-eight",
    "borromean",
    "braid-word",
  ],
  computation: {
    engine: "python",
    script: "computations/catalan_binding.py",
    witness: [
      "computations/catalan-binding.witness.json",
      "computations/q-pinning-50-digit.witness.json",
    ],
    status: "verified",
  },
});
