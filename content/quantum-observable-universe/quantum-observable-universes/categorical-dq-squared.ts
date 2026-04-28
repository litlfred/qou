import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-dq-squared",
  lean: { ref: "qou:QOU.categorical_dq_squared",
    validation: "not_checked",
  },
  title: "Non-vanishing of $d_q^2$",
  tags: ["exterior-derivative", "deformation"],
  uses: ["def:categorical-q-ext-deriv"],
  proofs: ["prf:categorical-dq-squared"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-dq-squared-0.svg", blockIndex: 0, hash: "fdcf22bc0345" },
  ],

});
