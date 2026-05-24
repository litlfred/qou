import { table } from "../../schema/builders";
export default table({
  label: "tbl:jet-planck-steps-table1-data",
  title: "Data table 1 from rem:jet-planck-steps",
  uses: ["rem:jet-planck-steps"],
  tags: ["extracted-table"],
});
