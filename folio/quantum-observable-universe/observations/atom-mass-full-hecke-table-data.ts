import { table } from "../../schema/builders";
export default table({
  label: "tbl:atom-mass-full-hecke-table-data",
  title: "Three-channel $H_3(q)$ Markov traces and binding energies per nucleon for light atoms ($Z = 1$ to $10$)",
  uses: ["rem:atom-mass-full-hecke"],
  tags: ["extracted-table"],
});
