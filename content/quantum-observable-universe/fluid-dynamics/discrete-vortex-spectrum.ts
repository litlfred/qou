import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:discrete-vortex-spectrum",
  lean: {
    decl: "QOU.FluidDynamics.discrete_vortex_spectrum",
    file: "QOU/FluidDynamics.lean",
    validation: "not_checked",
  },
  title: "Discrete vortex mode spectrum",
  uses: ["rem:vortex-intensity-modes"],
  tags: ["vortex", "quantization", "spectral"],
});
