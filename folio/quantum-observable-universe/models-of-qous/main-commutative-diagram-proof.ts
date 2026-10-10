import { proof } from "../../schema/builders";

export default proof({
  label: "prf:main-commutative-diagram",
  title: "Proof of Main Commutative Diagram",
  uses: ["prop:main-commutative-diagram"],
  lean: { ref: "qou:QOU.main_commutative_diagram",
    validation: "not_checked",
  },
});
