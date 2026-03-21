import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-dq-squared",
  title: "Non-vanishing of $d_q^2$",
  tags: ["exterior-derivative", "deformation"],
  uses: [
    "def:categorical-q-ext-deriv",
    "def:weight-decomposition",
  ],
  proofs: ["prf:categorical-dq-squared"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-dq-squared-0.svg", blockIndex: 0, hash: "fdcf22bc0345" },
    { mime: "image/svg+xml", url: "rendered/categorical-dq-squared-1.svg", blockIndex: 1, hash: "9269fbe261dd" },
  ],

});
