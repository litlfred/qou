import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chebyshev-torus-coefficients-values",
  title: "Values of the Chebyshev crossing coefficients at the substrate parameter",
  interprets: "def:chebyshev-torus-coefficients",
  tags: ["torus-knot", "chebyshev"],
  uses: [
    "def:chebyshev-torus-coefficients",
  ],
});
