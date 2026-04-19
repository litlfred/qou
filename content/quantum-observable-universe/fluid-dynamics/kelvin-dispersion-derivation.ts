import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:kelvin-dispersion-derivation",
  lean: {
    decl: "QOU.FluidDynamics.kelvin_dispersion_derivation",
    file: "QOU/FluidDynamics.lean",
    validation: "not_checked",
  },
  title: "Kelvin wave dispersion from the $q$-Laplacian eigenvalue problem",
  uses: [
    "prop:discrete-vortex-spectrum",
    "rem:vortex-intensity-modes",
    "def:q-navier-stokes",
    "rem:geodesic-vortices",
  ],
  tags: ["kelvin-wave", "dispersion", "q-laplacian", "eigenvalue", "derivation"],
});
