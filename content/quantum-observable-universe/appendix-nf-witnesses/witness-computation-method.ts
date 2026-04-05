import { remark } from "../../schema/builders";

export default remark({
  label: "rem:witness-computation-method",
  title: "Witness computation method: inductive Gröbner reduction",
  tags: ["hecke-engine", "groebner-basis", "symbolic-computation"],
  interprets: "prop:shell-closure-normal-form",
  uses: ["def:witness-4he", "def:witness-8be", "def:witness-12c"],
});
