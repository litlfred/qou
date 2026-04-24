import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bsd-surreal-bound",
  title:
    "Surreal bound for Birch--Swinnerton-Dyer: rank--order matches $\\omega$-order of $L$-series",
  interprets: "conj:q-birch-swinnerton-dyer",
  uses: [
    "conj:q-birch-swinnerton-dyer",
    "rem:rh-surreal-bound",
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
