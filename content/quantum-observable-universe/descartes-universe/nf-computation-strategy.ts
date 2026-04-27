import { remark } from "../../schema/builders";

export default remark({
  label: "rem:nf-computation-strategy",
  title: "Computational strategy for the Gröbner--Shirshov normal form",
  tags: [
    "groebner-basis",
    "normal-form",
    "computational-complexity",
    "optimization",
    "quotient-ideal",
    "hecke-algebra",
  ],
  interprets: "prop:shell-closure-normal-form",
  uses: ["rem:kummer-shell-closure"],
});
