import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:quantum-peter-weyl",
  title:
    "Quantum Peter--Weyl theorem: completeness of the $\\mathrm{SU}_q(2)$ eigenbasis",
  uses: [
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
