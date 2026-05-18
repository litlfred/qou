import { remark } from "../../schema/builders";

export default remark({
  label: "rem:surreal-bounds-graded-mikusinski",
  title:
    "Surreal-bound family as graded-Mikusiński std-collapse instances",
  interprets: "lem:surreal-squeeze",
  uses: [
    "lem:surreal-squeeze",
    "conj:gb-depth-period-correspondence",
    "rem:bsd-surreal-bound",
    "rem:rh-surreal-bound",
    "rem:p-vs-np-surreal-bound",
    "rem:collatz-surreal-bound",
    "rem:algebraic-core-survives",
  ],
  cites: ["zagier1986", "bloch2000"],
  tags: [
    "graded-mikusinski",
    "surreal-bounds",
    "millennium-problems",
    "std-collapse",
    "depth-filtration",
    "unification",
    "interpretation",
  ],
});
