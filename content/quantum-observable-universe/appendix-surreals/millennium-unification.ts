import { remark } from "../../schema/builders";

export default remark({
  label: "rem:millennium-unification",
  title:
    "Millennium problems unified by the surreal squeeze $\\delta^2 / \\varepsilon > \\varepsilon^3$",
  interprets: "thm:macroscopic-stability-equivalence",
  uses: [
    "conj:p-vs-np-qou",
    "conj:q-birch-swinnerton-dyer",
    "def:q-from-epsilon",
    "rem:adelic-tate-squeeze",
    "rem:collatz-surreal-bound",
    "rem:yang-mills-surreal-bound",
  ],
  tags: [
    "millennium-problems",
    "riemann-hypothesis",
    "navier-stokes",
    "collatz",
    "p-vs-np",
    "birch-swinnerton-dyer",
    "yang-mills",
    "adeles",
    "tate-thesis",
    "surreal",
    "squeeze",
    "unification",
    "classical-limit",
  ],
  cites: ["conway1976", "gonshor1986", "lagarias2010", "cook1971", "tate1967", "jaffe2006"],
});
