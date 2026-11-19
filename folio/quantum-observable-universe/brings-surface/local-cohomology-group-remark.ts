import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:local-cohomology-group",
  label: "rem:local-cohomology-group-remark",
  title: "Local cohomology as an extension obstruction",
  uses: ["def:local-cohomology-group"],
});
