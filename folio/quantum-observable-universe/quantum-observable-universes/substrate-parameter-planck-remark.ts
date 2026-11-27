import { remark } from "../../schema/builders";

export default remark({
  label: "rem:aether-parameter-planck-remark",
  renamedFrom: ["rem:substrate-parameter-planck-remark"],
  title: "The aether parameter as a measure of non-commutativity",
  interprets: "def:aether-parameter-planck",
  uses: ["def:aether-parameter-planck"],
  tags: ["substrate-parameter", "planck-constant", "q-deformation"],
});
