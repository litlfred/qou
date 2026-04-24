import { remark } from "../../schema/builders";

export default remark({
  label: "rem:yang-mills-surreal-bound",
  title:
    "Surreal bound for Yang--Mills: the mass gap $\\Delta_q \\asymp \\varepsilon^3$ is the Yang--Mills statement",
  interprets: "thm:quantum-gap-collapse",
  uses: [
    "thm:quantum-gap-collapse",
    "prop:surreal-rate-calculus",
    "lem:surreal-squeeze",
    "def:reeb-epsilon",
    "def:q-from-epsilon",
    "rem:big-o-surreal",
  ],
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
