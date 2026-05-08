import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:kelvin-dispersion-derivation",
  lean: { ref: "qou:QOU.FluidDynamics.kelvin_dispersion_derivation", validation: "not_started" },
  title: "Kelvin wave dispersion from the $q$-Laplacian eigenvalue problem",
  uses: ["def:q-navier-stokes"],
  tags: ["kelvin-wave", "dispersion", "q-laplacian", "eigenvalue", "derivation"],
});
