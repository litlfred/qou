import { remark } from "../../schema/builders";

export default remark({
  label: "rem:b1-current-status",
  title:
    "Canonical B1 current-status synthesis — what is theorem, what is open, after eleven rounds",
  interprets: "conj:gb-depth-period-correspondence",
  uses: [
    "prop:b1-hyperbolic-rows-theorem",
    "prop:joint-galois-braid-discharged",
    "prop:cl3-zeta5-orbit-sum-identity",
    "rem:jones-faithfulness-crossing-8",
  ],
  cites: [
    "murakami-murakami2001",
    "bloch2000",
    "suslin1991",
    "kashaev1997",
    "thurston1978",
  ],
  tags: [
    "B1-status",
    "synthesis",
    "current-status",
    "theorem-vs-open",
    "graded-mikusinski",
    "exposition",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "See [Table 1](#tbl:b1-current-status-table1-data).",
    },
  ],
});
