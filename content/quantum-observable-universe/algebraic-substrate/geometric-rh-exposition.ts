import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:hasse-weil-bound",
  label: "rem:geometric-rh-exposition",
  title: "The geometric reason for the critical line",
  tags: ["exposition", "riemann-hypothesis", "unitary", "chern-classes", "flatness"],
  uses: [
    "rem:unitary-stability",
    "conj:classical-riemann-hypothesis",
  ],
});
