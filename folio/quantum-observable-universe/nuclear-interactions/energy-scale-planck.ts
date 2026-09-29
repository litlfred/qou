import { remark } from "../../schema/builders";

export default remark({
  label: "rem:energy-scale-planck",
  title: "Energy scale $E_0$ and the Planck time",
  interprets: "rem:beta-decay-energy-scale",
  uses: [
    "rem:beta-decay-energy-scale",
    "def:information-speed-of-light",
  ],
  tags: [
    "energy-scale",
    "planck-time",
    "calibration",
    "speed-of-light",
    "hecke-step",
  ],
});
