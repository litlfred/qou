import { remark } from "../../../schema/builders";

export default remark({
  label: "rem:embeddability-closure-audit",
  title: "Audit of embeddability closure for the particle dictionary",
  tags: [
    "audit",
    "embeddability",
    "particle-dictionary",
  ],
  uses: ["tbl:embeddability-closure-table-data"],
});
