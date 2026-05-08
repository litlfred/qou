import { definition } from "../../schema/builders";

export default definition({
  label: "def:levi-form-defect",
  title: "Matter as Frobenius failure via the Levi form",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.LeviFormDefect",
    validation: "not_checked",
  },
  uses: ["def:frobenius-hopf-substrate"],
  tags: ["levi-form", "frobenius-failure", "matter", "defect"],
});
