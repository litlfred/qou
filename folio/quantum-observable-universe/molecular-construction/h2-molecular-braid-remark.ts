import { remark } from "../../schema/builders";

export default remark({
  label: "rem:h2-molecular-braid-remark",
  title: "Staged construction of the hydrogen molecule",
  interprets: "def:h2-molecular-braid",
  tags: ["definition-commentary"],
  uses: [
    "def:h2-molecular-braid",
    "def:atomic-braid",
    "tbl:h2-molecular-braid-table-data",
  ],
});
