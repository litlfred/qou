import { remark } from "../../schema/builders";

export default remark({
  label: "rem:p-vs-np-boundary-interpretation",
  title: "Geometric dictionary reading of the skein computational boundary",
  interprets: "conj:p-vs-np-boundary",
  uses: [
    "conj:p-vs-np-boundary",
    "tbl:p-vs-np-boundary-table1-data",
    "tbl:p-vs-np-boundary-table2-data",
    "quantum-observable-universe:prop:p-bandwidth-bound",
  ],
  tags: ["P-vs-NP", "interpretation", "computational-horizon"],
});
