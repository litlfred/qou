import { table } from "../../schema/builders";
export default table({
  label: "tbl:skein-shell-correction-table-data",
  title: "Data table from conj:skein-shell-correction",
  uses: ["conj:skein-shell-correction"],
  tags: ["extracted-table"],
});
