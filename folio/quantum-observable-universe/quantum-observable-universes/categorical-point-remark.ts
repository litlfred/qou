import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-point-remark",
  title: "Categorical points in the archimedean realisation",
  interprets: "def:categorical-point",
  uses: ["def:categorical-point"],
  tags: ["point", "categorical"],
});
