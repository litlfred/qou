import { remark } from "../../schema/builders";

export default remark({
  label: "rem:kummer-shell-closure",
  title: "Shell closure as $\\mu_n$ torsion in the Kummer tower",
  tags: [
    "kummer-tower",
    "shell-closure",
    "pauli-exclusion",
    "torsion",
    "normal-form",
    "gm-torsion",
  ],
  interprets: "prop:shell-closure-normal-form",
  uses: [
    "rem:kummer-filtration-obstruction",
    "rem:groebner-nf-computation",
  ],
});
