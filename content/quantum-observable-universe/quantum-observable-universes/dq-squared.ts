import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:dq-squared",
  lean: {
    decl: "QOU.dq_squared",
    validation: "not_checked",
  },
  title: "$d_q^2$ does not vanish",
  tags: ["q-deformation", "exterior-derivative"],
  uses: ["def:categorical-q-ext-deriv"],
  proofs: ["prf:dq-squared"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/dq-squared-0.svg", blockIndex: 0, hash: "8d93aec80ced" },
  ],

});
