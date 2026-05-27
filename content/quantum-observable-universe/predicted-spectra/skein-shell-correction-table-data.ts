import { table } from "../../schema/builders";
export default table({
  label: "tbl:skein-shell-correction-table-data",
  title: "Data table from rem:skein-shell-correction",
  uses: ["rem:skein-shell-correction"],
  tags: ["extracted-table"],
});
