import { table } from "../../schema/builders";
export default table({
  label: "tbl:unified-iterative-correction-table-data",
  title: "Data table from prop:unified-iterative-correction",
  uses: ["prop:unified-iterative-correction"],
  tags: ["extracted-table"],
});
