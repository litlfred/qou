import { proof } from "../../schema/builders";

export default proof({
  label: "prf:categorical-dq-squared",
  title: "Proof of Non-vanishing of $d_q^2$",
  uses: ["prop:categorical-dq-squared"],
  lean: {
    decl: "QOU.categorical_dq_squared",
    validation: "leanok",
  },
  status: "proved",
});
