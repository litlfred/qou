import { remark } from "../../schema/builders";

export default remark({
  label: "rem:nf-computation-strategy",
  title: "Computational strategy for the Gröbner normal form",
  tags: [
    "groebner-basis",
    "normal-form",
    "computational-complexity",
    "optimization",
    "quotient-ideal",
    "hecke-algebra",
  ],
  interprets: "prop:shell-closure-normal-form",
  uses: [
    "rem:groebner-nf-computation",
    "rem:kummer-shell-closure",
    "prop:nuclear-groebner-reduction",
  ],
});
