import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:color-tube-coordinates",
  label: "rem:color-tube-interpretation",
  title: "Interpretation of the color tube",
  uses: [
    "def:color-tube-coordinates",
    "rem:brings-qou-4tuple",
    "rem:spectral-dynamics",
  ],
});
