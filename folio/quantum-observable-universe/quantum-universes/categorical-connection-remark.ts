import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-connection-remark",
  title: "Classical connections and $A$-linearity of curvature",
  interprets: "def:categorical-connection",
  uses: ["def:categorical-connection", "ex:categorical-connection-su2"],
  tags: ["connection", "curvature"],
});
