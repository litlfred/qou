import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:levi-form-defect",
  label: "rem:levi-form-defect-remark",
  title: "Matter as the failure of the Frobenius structure",
  uses: ["def:levi-form-defect", "def:frobenius-hopf-substrate"],
});
