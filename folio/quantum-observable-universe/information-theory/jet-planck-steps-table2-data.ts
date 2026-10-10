import { table } from "../../schema/builders";
export default table({
  label: "tbl:jet-planck-steps-table2-data",
  title: "Data table 2 from rem:jet-planck-steps",
  uses: ["rem:jet-planck-steps"],
  tags: ["extracted-table"],
});
