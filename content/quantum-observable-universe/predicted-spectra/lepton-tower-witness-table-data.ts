import { table } from "../../schema/builders";
export default table({
  label: "tbl:lepton-tower-witness-table-data",
  title: "Data table from rem:lepton-tower-witness",
  uses: ["rem:lepton-tower-witness"],
  tags: ["extracted-table"],
});
