import { remark } from "../../schema/builders";

export default remark({
  label: "rem:adelic-tate-squeeze",
  title:
    "Adelic--Tate surreal squeeze: local Reeb-$\\varepsilon_p$ at each prime and the global Euler product",
  interprets: "thm:hasse-weil-bound",
  uses: [
    "thm:hasse-weil-bound",
    "rem:rh-surreal-bound",
    "rem:bsd-surreal-bound",
    "lem:surreal-squeeze",
    "def:reeb-epsilon",
    "def:q-from-epsilon",
    "prop:surreal-rate-calculus",
    "rem:big-o-surreal",
    "rem:calculus-up-to-epsilon",
  ],
  tags: [
    "adeles",
    "tate-thesis",
    "fourier-transform",
    "euler-product",
    "riemann-hypothesis",
    "millennium-problem",
    "surreal",
    "squeeze",
    "local-global",
  ],
  cites: ["conway1976", "tate1950"],
});
