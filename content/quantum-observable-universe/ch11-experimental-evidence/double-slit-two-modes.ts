import { remark } from "../../schema/builders";

export default remark({
  label: "rem:double-slit-two-modes",
  title: "Two scattering modes and band-width anomalies",
  uses: [
    "prop:double-slit-massive-pattern",
    "def:observation",
    "def:substrate-parameter",
  ],
  tags: ["double-slit", "scattering", "band-width", "observation", "anomaly"],
  simulator: { ref: "sim:double-slit-analytical" },
});
