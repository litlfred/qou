import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:quantum-peter-weyl",
  lean: {
    decl: "QOU.FluidDynamics.quantum_peter_weyl",
    file: "QOU/FluidDynamics.lean",
    validation: "not_checked",
  },
  title:
    "Quantum Peter--Weyl theorem: completeness of the $\\mathrm{SU}_q(2)$ eigenbasis",
  uses: [
    "def:quantum-observable-universe",
    "def:frobenius-pairing",
    "prop:pawlowski-leitner-inner-product",
    "prop:q-spectral-sobolev",
  ],
  tags: [
    "peter-weyl",
    "completeness",
    "orthonormal-basis",
    "matrix-coefficients",
    "quantum-group",
    "spectral-theory",
  ],
});
