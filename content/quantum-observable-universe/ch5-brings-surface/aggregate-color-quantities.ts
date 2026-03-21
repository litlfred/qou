import { remark } from "../../schema/builders";

export default remark({
  label: "rem:aggregate-color-quantities",
  title: "Aggregate color quantities",
  uses: ["def:color-tube-coordinates", "rem:lagrange-resolvents"],
});
