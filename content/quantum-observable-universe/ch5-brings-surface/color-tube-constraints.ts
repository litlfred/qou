import { remark } from "../../schema/builders";

export default remark({
  label: "rem:color-tube-constraints",
  title: "Constraint equations in color tube coordinates",
  uses: [
    "rem:lagrange-resolvents",
    "rem:aggregate-color-quantities",
  ],
});
