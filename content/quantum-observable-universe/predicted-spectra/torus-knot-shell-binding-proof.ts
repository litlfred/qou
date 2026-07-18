import { proof } from "../../schema/builders";

export default proof({
  label: "prf:torus-knot-shell-binding",
  title: "Proof of shell binding from the torus knot hierarchy",
  uses: ["prop:torus-knot-shell-binding", "def:inter-shell-operator", "def:chebyshev-torus-coefficients"],
});
