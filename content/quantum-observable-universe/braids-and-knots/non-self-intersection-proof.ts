import { proof } from "../../schema/builders";

export default proof({
  label: "prf:non-self-intersection",
  title: "Proof of Obstruction to self-intersection",
  uses: ["cor:non-self-intersection"],
  lean: { ref: "qou:QOU.NonSelfIntersection",
    validation: "not_checked",
  },
});
