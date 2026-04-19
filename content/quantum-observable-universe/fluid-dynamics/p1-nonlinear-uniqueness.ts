import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-ns-nonlinear-uniqueness",
  lean: {
    decl: "QOU.FluidDynamics.q_ns_nonlinear_uniqueness",
    validation: "not_checked",
  },
  title:
    "Nonlinear estimates and uniqueness for the $q$-Navier--Stokes system",
  uses: [
    "prop:q-spectral-sobolev",
    "def:q-navier-stokes",
    "thm:q-ns-wellposedness",
    "def:frobenius-pairing",
    "rem:planck-reynolds",
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
