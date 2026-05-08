import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:q-ns-wellposedness",
  lean: { ref: "qou:QOU.FluidDynamics.q_ns_wellposedness", validation: "not_started" },
  title: "Global regularity of the $q$-deformed Navier--Stokes equation",
  uses: ["prop:kelvin-dispersion-derivation"],
  tags: [
    "navier-stokes",
    "well-posedness",
    "regularity",
    "millennium-problem",
    "q-deformation",
    "global-existence",
    "categorical",
  ],
});
