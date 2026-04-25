import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:dq-squared",
  lean: { ref: "qou:QOU.dq_squared",
    validation: "not_checked",
  },
  title: "$d_q^2$ does not vanish",
  tags: ["q-deformation", "exterior-derivative"],
  uses: ["def:categorical-q-ext-deriv"],
  proofs: ["prf:dq-squared"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/dq-squared-0.svg", blockIndex: 0, hash: "4b6d1699abb9" },
  ],

});
