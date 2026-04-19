import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-turbulence-spectrum",
  lean: {
    decl: "QOU.FluidDynamics.q_turbulence_spectrum",
    file: "QOU/FluidDynamics.lean",
    validation: "not_checked",
  },
  title: "$q$-deformed energy cascade and modified Kolmogorov spectrum",
  uses: [
    "rem:planck-reynolds",
    "prop:discrete-vortex-spectrum",
    "rem:vortex-intensity-modes",
    "def:substrate-parameter",
  ],
  tags: ["turbulence", "kolmogorov", "energy-cascade", "fluid-dynamics", "prediction"],
});
