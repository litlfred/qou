import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-turbulence-spectrum",
  lean: { ref: "qou:QOU.FluidDynamics.q_turbulence_spectrum", validation: "not_checked" },
  title: "$q$-deformed energy cascade and modified Kolmogorov spectrum",
  tags: ["turbulence", "kolmogorov", "energy-cascade", "fluid-dynamics", "prediction"],
});
