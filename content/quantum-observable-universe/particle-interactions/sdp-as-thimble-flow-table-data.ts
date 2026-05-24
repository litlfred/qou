import { table } from "../../schema/builders";
export default table({
  label: "tbl:sdp-as-thimble-flow-table-data",
  title: "Data table from rem:sdp-as-thimble-flow",
  uses: ["rem:sdp-as-thimble-flow"],
  tags: ["extracted-table"],
});
