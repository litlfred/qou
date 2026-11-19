import { remark } from "../../schema/builders";

export default remark({
  label: "rem:two-row-stratum-remark",
  title: "Structural significance and scope of the two-row stratum",
  interprets: "def:two-row-stratum",
  uses: [
    "def:two-row-stratum",
    "prop:wedderburn-weight-canonical",
    "def:two-row-projection",
  ],
});
