import { proof } from "../../schema/builders";

export default proof({
  label: "prf:calibration-cohomology-alignment",
  title: "Proof of the calibration–cohomology alignment",
  uses: ["prop:calibration-cohomology-alignment", "prop:meson-scale-independence"],
});
