import { remark } from "../../schema/builders";

export default remark({
  label: "rem:brings-q-hyperbolic-geometry",
  title: "q-Hyperbolic Geometry on Bring's Curve",
  tags: ["brings-curve", "q-bessel", "quantum-hyperbolic-plane"],
  uses: [
    "rem:brings-curve",
    "proof:jackson-q-bessel-contiguity"
  ],
});
