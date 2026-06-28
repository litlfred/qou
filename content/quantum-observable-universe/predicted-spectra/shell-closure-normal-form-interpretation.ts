import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:shell-closure-normal-form",
  label: "rem:shell-closure-normal-form-interpretation",
  title: "Bruhat-symmetric shell filling and the shell-closure permutations",
  uses: [
    "prop:shell-closure-normal-form",
    "prop:nuclear-groebner-reduction",
  ],
});
