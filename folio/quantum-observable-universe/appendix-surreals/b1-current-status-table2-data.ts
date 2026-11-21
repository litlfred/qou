import { table } from "../../schema/builders";
export default table({
  label: "tbl:b1-current-status-table2-data",
  title: "Data table 2 from rem:b1-current-status",
  uses: ["rem:b1-current-status"],
  tags: ["extracted-table"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Witness column dropped from the table (rows in order): [`gb-depth-period-bring-fig8.witness.json`](https://github.com/litlfred/qou/blob/main/computations/gb-depth-period-bring-fig8.witness.json); [`bring-trilog-zeta5-depth-3.witness.json`](https://github.com/litlfred/qou/blob/main/computations/bring-trilog-zeta5-depth-3.witness.json); [`kummer-reflection-zeta5.witness.json`](https://github.com/litlfred/qou/blob/main/computations/kummer-reflection-zeta5.witness.json); [`cl3-zeta5-orbit-sum.witness.json`](https://github.com/litlfred/qou/blob/main/computations/cl3-zeta5-orbit-sum.witness.json)" },
  ],
});
