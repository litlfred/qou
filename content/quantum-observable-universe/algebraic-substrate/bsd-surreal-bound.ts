import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bsd-surreal-bound",
  title:
    "Surreal bound for Birch--Swinnerton-Dyer: rank--order matches $\\omega$-order of $L$-series",
  interprets: "conj:q-birch-swinnerton-dyer",
  uses: [
    "conj:q-birch-swinnerton-dyer",
    "thm:quantum-gap-collapse",
    "lem:surreal-squeeze",
    "def:reeb-epsilon",
    "def:q-from-epsilon",
    "prop:surreal-rate-calculus",
    "rem:rh-surreal-bound",
    "rem:adelic-tate-squeeze",
    "rem:conway-normal-form",
    "rem:calculus-up-to-epsilon",
  ],
  tags: [
    "birch-swinnerton-dyer",
    "millennium-problem",
    "surreal",
    "squeeze",
    "l-function",
    "elliptic-curve",
    "classical-limit",
  ],
  cites: ["conway1976"],
});
