import { table } from "../../schema/builders";
export default table({
  label: "tbl:hadron-q-self-correction-table-data",
  title: "Data table from prop:hadron-q-self-correction",
  uses: ["prop:hadron-q-self-correction"],
  tags: ["extracted-table"],
});
