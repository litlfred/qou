import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:q-turbulence-spectrum",
  label: "rem:q-turbulence-prediction",
  title: "Testable prediction: high-wavenumber deviations from Kolmogorov scaling",
  uses: ["prop:q-turbulence-spectrum", "rem:bec-vortex-data"],
  tags: ["prediction", "turbulence", "BEC", "falsifiable"],
});
