import { remark } from "../../schema/builders";

export default remark({
  label: "rem:surreal-bounds-graded-mikusinski",
  title: "Speculative graded-Mikusiński depth assignment across four surreal heuristics",
  interprets: "conj:q-birch-swinnerton-dyer",
  uses: [
    "rem:bsd-surreal-bound",
    "rem:rh-surreal-bound",
    "rem:p-vs-np-surreal-bound",
    "rem:collatz-surreal-bound",
    "quantum-observable-universe:lem:surreal-squeeze",
    "quantum-observable-universe:conj:gb-depth-period-correspondence",
  ],
  cites: ["conway1976"],
  tags: ["surreal", "mikusinski", "analogy"],
});
