import { remark } from "../../schema/builders";

export default remark({
  label: "rem:witness-computation-method",
  title: "Witness computation method: inductive Gröbner--Shirshov reduction",
  tags: [
    "hecke-engine",
    "groebner-shirshov",
    "symbolic-computation",
    "crossing-convention",
    "unimodular",
  ],
  interprets: "prop:shell-closure-normal-form",
  uses: [
    "def:witness-4he",
    "def:witness-8be",
    "def:witness-12c",
    "prop:nuclear-groebner-reduction",
  ],
});
