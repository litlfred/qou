import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:vorticity-lower-bound",
  label: "rem:core-levi-form",
  title: "Core aspect ratio as Levi form condition number",
  uses: [
    "prop:vorticity-lower-bound",
    "prop:root-of-unity-truncation",
    "rem:levi-form-defect",
    "rem:c-substrate-via-levi",
    "rem:geodesic-vortices",
    "def:substrate-parameter",
  ],
  tags: [
    "levi-form",
    "contact-structure",
    "integrability",
    "core-shape",
    "millennium-problem",
  ],
});
