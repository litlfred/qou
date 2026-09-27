import { remark } from "../../schema/builders";

export default remark({
  label: "rem:adelic-tate-squeeze",
  title:
    "Adelic--Tate surreal squeeze: local Reeb-$\\varepsilon_p$ at each prime and the global Euler product",
  interprets: "thm:hasse-weil-bound",
  uses: ["prop:adelic-reeb-restricted-product"],
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
  cites: ["conway1976",
    "tate1967",
  ],
});
