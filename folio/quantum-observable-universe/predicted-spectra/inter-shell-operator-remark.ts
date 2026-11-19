import { remark } from "../../schema/builders";

export default remark({
  label: "rem:inter-shell-operator-remark",
  title: "Reading of the inter-shell operator",
  interprets: "def:inter-shell-operator",
  tags: ["shell", "torus-knot"],
  uses: [
    "def:inter-shell-operator",
    "def:chebyshev-torus-coefficients",
  ],
});
