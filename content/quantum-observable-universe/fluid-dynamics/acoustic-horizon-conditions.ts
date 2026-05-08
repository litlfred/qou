import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:acoustic-horizon-conditions",
  lean: { ref: "qou:QOU.FluidDynamics.acoustic_horizon_conditions", validation: "not_started" },
  title: "Acoustic horizon formation and gravitational emergence",
  uses: ["def:q-navier-stokes"],
  tags: ["acoustic-metric", "horizon", "analogue-gravity", "black-hole", "hawking"],
});
