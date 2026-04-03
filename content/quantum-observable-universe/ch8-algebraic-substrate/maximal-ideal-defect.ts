import { definition } from "../../schema/builders";

export default definition({
  label: "def:maximal-ideal-defect",
  title: "Maximal ideal at the unit coordinate",
  lean: {
    decl: "QOU.AlgebraicSubstrate.MaximalIdealDefect",
    validation: "not_checked",
  },
  uses: ["def:frobenius-hopf-substrate", "def:levi-form-defect"],
  tags: ["maximal-ideal", "unit-coordinate", "defect", "singularity"],
});
