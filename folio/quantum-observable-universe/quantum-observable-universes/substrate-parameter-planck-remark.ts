import { remark } from "../../schema/builders";

export default remark({
  label: "rem:substrate-parameter-planck-remark",
  title: "The substrate parameter as a measure of non-commutativity",
  interprets: "def:substrate-parameter-planck",
  uses: ["def:substrate-parameter-planck"],
  tags: ["substrate-parameter", "planck-constant", "q-deformation"],
});
