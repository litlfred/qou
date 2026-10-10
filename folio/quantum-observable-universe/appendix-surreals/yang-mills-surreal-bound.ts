import { remark } from "../../schema/builders";

export default remark({
  label: "rem:yang-mills-surreal-bound",
  uses: [
    "def:q-from-epsilon",
    "def:reeb-epsilon",
    "lem:surreal-squeeze",
    "prop:surreal-rate-calculus",
    "rem:calculus-up-to-epsilon",
    "rem:conway-normal-form",
    "thm:quantum-gap-collapse",
  ],
  title:
    "Surreal bound for Yang--Mills: the mass gap $\\Delta_q \\asymp \\varepsilon^3$ is the Yang--Mills statement",
  interprets: "thm:quantum-gap-collapse",
  tags: [
    "yang-mills",
    "mass-gap",
    "millennium-problem",
    "surreal",
    "squeeze",
    "confinement",
    "classical-limit",
  ],
  cites: ["conway1976"],
});
