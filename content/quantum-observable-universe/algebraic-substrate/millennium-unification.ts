import { remark } from "../../schema/builders";

export default remark({
  label: "rem:millennium-unification",
  title:
    "Millennium problems unified by the surreal squeeze $\\delta^2 / \\varepsilon > \\varepsilon^3$",
  interprets: "thm:macroscopic-stability-equivalence",
  uses: [
    "thm:macroscopic-stability-equivalence",
    "lem:surreal-squeeze",
    "prop:surreal-rate-calculus",
    "def:reeb-epsilon",
    "def:q-from-epsilon",
    "rem:rh-surreal-bound",
    "rem:ns-surreal-bound",
    "rem:collatz-surreal-bound",
    "rem:p-vs-np-surreal-bound",
    "rem:big-o-surreal",
    "rem:body-asymptotics-catalog",
  ],
  tags: [
    "millennium-problems",
    "riemann-hypothesis",
    "navier-stokes",
    "collatz",
    "p-vs-np",
    "surreal",
    "squeeze",
    "unification",
    "classical-limit",
  ],
  cites: ["conway1976", "gonshor1986", "lagarias2010", "cook1971"],
});
