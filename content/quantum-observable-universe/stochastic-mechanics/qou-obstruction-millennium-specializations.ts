import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:qou-obstruction-reduction",
  label: "rem:qou-obstruction-millennium-specializations",
  title:
    "RH, NS and BSD as proportional specializations of the single obstruction class",
  uses: [
    "thm:qou-obstruction-reduction",
    "tbl:qou-obstruction-reduction-table4-data",
  ],
});
