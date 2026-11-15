import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:q-ns-wellposedness",
  lean: { ref: "qou:QOU.FluidDynamics.q_ns_wellposedness", validation: "not_checked" },
  title: "Global regularity of the $q$-deformed Navier--Stokes equation",
  uses: [
    "prop:kelvin-dispersion-derivation",
    // Introduced in the setup and carried into the statement: the spectral
    // decay clause is stated over the Delta_q eigencomponents.
    "rem:q-laplacian-interpretation",
  ],
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
