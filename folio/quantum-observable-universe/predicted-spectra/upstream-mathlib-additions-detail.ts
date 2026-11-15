import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:upstream-mathlib-additions",
  label: "rem:upstream-mathlib-additions-detail",
  title: "Details of the three Mathlib additions and their upstreaming targets",
  uses: ["prop:upstream-mathlib-additions"],
});
