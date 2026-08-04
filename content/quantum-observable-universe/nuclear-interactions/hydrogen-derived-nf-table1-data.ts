import { table } from "../../schema/builders";
export default table({
  label: "tbl:hydrogen-derived-nf-table1-data",
  title: "Data table 1 from ex:hydrogen-derived-nf",
  uses: ["ex:hydrogen-derived-nf"],
  tags: ["extracted-table"],
});
