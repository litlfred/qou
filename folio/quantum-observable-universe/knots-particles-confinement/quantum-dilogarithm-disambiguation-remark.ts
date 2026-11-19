import { remark } from "../../schema/builders";

export default remark({
  label: "rem:quantum-dilogarithm-disambiguation-remark",
  title: "The false identity $\\Phi_q = -\\mathrm{Li}_2^q(-z)$ and the mass-formula discipline",
  interprets: "def:quantum-dilogarithm-disambiguation",
  tags: ["dilogarithm"],
  uses: [
    "def:quantum-dilogarithm-disambiguation",
  ],
});
