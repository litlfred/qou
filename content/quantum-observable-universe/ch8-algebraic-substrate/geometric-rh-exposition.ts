import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:hasse-weil-bound",
  label: "rem:geometric-rh-exposition",
  title: "The geometric reason for the critical line",
  tags: ["exposition", "riemann-hypothesis", "unitary", "chern-classes", "flatness"],
  uses: [
    "prop:hasse-weil-bound",
    "prop:spectral-half-line",
    "rem:yekutieli-stokes",
    "prop:unitary-stability",
    "conj:classical-riemann-hypothesis",
  ],
});
