import { proof } from "../../schema/builders";

export default proof({
  label: "prf:categorical-self-duality",
  title: "Proof of Categorical self-duality",
  uses: ["prop:categorical-self-duality"],
  lean: { ref: "qou:QOU.categorical_self_duality",
    validation: "leanok",
  },
});
