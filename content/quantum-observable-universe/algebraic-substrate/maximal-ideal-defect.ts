import { definition } from "../../schema/builders";

export default definition({
  label: "def:maximal-ideal-defect",
  title: "Maximal ideal at the unit coordinate",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.MaximalIdealDefect",
    validation: "not_checked",
  },
  uses: ["def:levi-form-defect"],
  tags: ["maximal-ideal", "unit-coordinate", "defect", "singularity"],
});
