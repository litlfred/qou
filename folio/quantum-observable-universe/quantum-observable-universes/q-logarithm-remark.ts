import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-logarithm-remark",
  title: "The $q$-logarithm as an adjoint",
  interprets: "def:q-logarithm",
  uses: ["def:q-logarithm", "def:q-exponential"],
  tags: ["hopf-algebra", "primitive", "q-logarithm", "adjoint"],
});
