import { remark } from "../../schema/builders";

export default remark({
  label: "rem:adelic-tate-squeeze",
  title:
    "Adelic--Tate surreal squeeze: local Reeb-$\\varepsilon_p$ at each prime and the global Euler product",
  interprets: "thm:hasse-weil-bound",
  uses: [
    "rem:bsd-surreal-bound",
    "rem:fibre-functor-rigidity",
    "def:standard-part-functor",
    "prop:vol-through-tau",
    "def:reeb-epsilon",
    "lem:surreal-squeeze",
    "rem:rh-surreal-bound",
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
  cites: ["conway1976", "tate1967"],
});
