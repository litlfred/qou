import { table } from "../../schema/builders";
export default table({
  label: "tbl:hecke-markov-interpretation-table-data",
  title: "Data table from rem:hecke-markov-interpretation",
  uses: ["rem:hecke-markov-interpretation"],
  tags: ["extracted-table"],
});
