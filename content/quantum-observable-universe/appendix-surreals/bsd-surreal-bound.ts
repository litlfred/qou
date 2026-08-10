import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bsd-surreal-bound",
  title:
    "Surreal bound for Birch--Swinnerton-Dyer: rank--order matches $\\omega$-order of $L$-series",
  interprets: "conj:q-birch-swinnerton-dyer",
  uses: [
    "def:reeb-epsilon",
    "lem:surreal-squeeze",
    "prop:surreal-rate-calculus",
    "rem:calculus-up-to-epsilon",
    "rem:conway-normal-form",
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
