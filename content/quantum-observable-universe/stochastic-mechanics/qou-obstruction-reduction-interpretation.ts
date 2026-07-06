import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:qou-obstruction-reduction",
  label: "rem:qou-obstruction-reduction-interpretation",
  title:
    "The obstruction as a function on $\\mathbb{P}^1$",
  uses: [
    "thm:qou-obstruction-reduction",
    "tbl:qou-obstruction-reduction-table3-data",
  ],
});
