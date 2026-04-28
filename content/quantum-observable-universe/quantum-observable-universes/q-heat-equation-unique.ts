import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-heat-equation-unique",
  title: "Uniqueness of solutions of the $q$-heat equation",
  lean: { ref: "qou:QOU.QHeatEquation.unique_solution",
    validation: "not_checked",
  },
  uses: ["prop:q-heat-equation-exists"],
  proofs: ["prf:q-heat-equation-unique"],
  tags: ["uniqueness", "q-heat-equation"],
});
