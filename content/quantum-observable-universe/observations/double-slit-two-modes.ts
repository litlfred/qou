import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:double-slit-massive-pattern",
  label: "rem:double-slit-two-modes",
  title: "Two scattering modes and band-width anomalies",
  uses: [
    "prop:double-slit-massive-pattern",
    "def:observation",
    "rem:knot-basis-color-content",
  ],
  tags: ["double-slit", "scattering", "band-width", "observation", "anomaly", "color-content"],
  simulator: { ref: "sim:double-slit-analytical" },
});
