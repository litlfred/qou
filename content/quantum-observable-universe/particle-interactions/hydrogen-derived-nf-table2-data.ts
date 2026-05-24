import { table } from "../../schema/builders";
export default table({
  label: "tbl:hydrogen-derived-nf-table2-data",
  title: "Data table 2 from ex:hydrogen-derived-nf",
  uses: ["ex:hydrogen-derived-nf"],
  tags: ["extracted-table"],
});
