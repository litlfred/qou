import { remark } from "../../schema/builders";

export default remark({
  label: "rem:rh-surreal-bound",
  title:
    "Surreal bound for the Riemann hypothesis: why $\\delta = 0$ on the critical line",
  interprets: "thm:quantum-gap-collapse",
  uses: [
    "thm:quantum-gap-collapse",
    "conj:classical-riemann-hypothesis",
    "thm:macroscopic-stability-equivalence",
    "lem:surreal-squeeze",
    "def:reeb-epsilon",
    "def:q-from-epsilon",
    "prop:surreal-rate-calculus",
    "rem:conway-normal-form",
    "rem:calculus-up-to-epsilon",
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
