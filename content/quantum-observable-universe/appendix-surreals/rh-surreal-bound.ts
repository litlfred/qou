import { remark } from "../../schema/builders";

export default remark({
  label: "rem:rh-surreal-bound",
  title:
    "Surreal bound for the Riemann hypothesis: why $\\delta = 0$ on the critical line",
  interprets: "thm:quantum-gap-collapse",
  uses: [
    "conj:classical-riemann-hypothesis",
    "def:q-from-epsilon",
    "def:reeb-epsilon",
    "prop:surreal-rate-calculus",
    "rem:conway-normal-form",
  ],
  tags: [
    "riemann-hypothesis",
    "millennium-problem",
    "surreal",
    "error-bounds",
    "squeeze",
    "critical-line",
    "classical-limit",
  ],
  cites: ["conway1976"],
});
