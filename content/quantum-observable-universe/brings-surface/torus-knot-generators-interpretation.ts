import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:torus-knot-generators",
  label: "rem:torus-knot-generators-interpretation",
  title: "Physical interpretation of the torus-knot generators",
  uses: [
    "prop:torus-knot-generators",
    "prop:s5-equivariant-torus-knots",
    "prop:cohomological-embedding",
    "rem:color-tube-interpretation",
    "def:recursive-brane-tower",
  ],
});
