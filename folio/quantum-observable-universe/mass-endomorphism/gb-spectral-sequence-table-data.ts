import { table } from "../../schema/builders";
export default table({
  label: "tbl:gb-spectral-sequence-table-data",
  title: "Data table from prop:gb-spectral-sequence",
  uses: ["prop:gb-spectral-sequence"],
  tags: ["extracted-table"],
});
