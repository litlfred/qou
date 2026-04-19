import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:acoustic-horizon-conditions",
  lean: {
    decl: "QOU.FluidDynamics.acoustic_horizon_conditions",
    file: "QOU/FluidDynamics.lean",
    validation: "not_checked",
  },
  title: "Acoustic horizon formation and gravitational emergence",
  uses: [
    "rem:madelung-fluid",
    "rem:gr-substrate-geometry",
    "def:q-navier-stokes",
    "rem:planck-reynolds",
  ],
  tags: ["acoustic-metric", "horizon", "analogue-gravity", "black-hole", "hawking"],
});
