import { proof } from "../../schema/builders";

export default proof({
  label: "prf:categorical-dq-squared",
  title: "Proof of Non-vanishing of $d_q^2$",
  uses: ["prop:categorical-dq-squared"],
  lean: { ref: "qou:QOU.categorical_dq_squared",
    validation: "leanok",
  },
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-dq-squared-proof-0.svg", blockIndex: 0, hash: "9269fbe261dd" },
  ],

});
