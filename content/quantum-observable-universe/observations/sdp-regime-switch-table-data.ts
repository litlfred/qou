import { table } from "../../schema/builders";
export default table({
  label: "tbl:sdp-regime-switch-table-data",
  title: "Data table from prop:sdp-regime-switch",
  uses: ["prop:sdp-regime-switch"],
  tags: ["extracted-table"],
});
