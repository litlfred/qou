import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-heat-equation-exists",
  title: "Well-posedness of the $q$-heat equation",
  lean: { ref: "qou:QOU.QHeatEquation.exists_solution",
    validation: "not_checked",
  },
  uses: ["def:q-heat-equation"],
  proofs: ["prf:q-heat-equation-exists"],
  tags: ["existence", "q-heat-equation", "well-posedness"],
});
