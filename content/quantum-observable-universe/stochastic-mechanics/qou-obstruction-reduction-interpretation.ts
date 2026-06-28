import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:qou-obstruction-reduction",
  label: "rem:qou-obstruction-reduction-interpretation",
  title:
    "The obstruction over $\\mathbb{P}^1$ and the three millennium problems as specializations",
  uses: [
    "thm:qou-obstruction-reduction",
    "tbl:qou-obstruction-reduction-table3-data",
    "tbl:qou-obstruction-reduction-table4-data",
  ],
});
