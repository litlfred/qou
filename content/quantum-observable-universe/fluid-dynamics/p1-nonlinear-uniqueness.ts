import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-ns-nonlinear-uniqueness",
  lean: { ref: "qou:QOU.FluidDynamics.p1_nonlinear_uniqueness", validation: "not_started" },
  title:
    "Nonlinear estimates and uniqueness for the $q$-Navier--Stokes system",
  uses: [
    "prop:q-spectral-sobolev",
    "thm:q-ns-wellposedness",
  ],
  tags: [
    "nonlinear-estimate",
    "uniqueness",
    "enstrophy",
    "gronwall",
    "energy-method",
    "regularity",
  ],
});
