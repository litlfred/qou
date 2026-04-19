import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:q-ns-wellposedness",
  lean: {
    decl: "QOU.FluidDynamics.q_ns_wellposedness",
    validation: "not_checked",
  },
  title: "Global regularity of the $q$-deformed Navier--Stokes equation",
  uses: [
    "def:q-navier-stokes",
    "def:quantum-observable-universe",
    "def:categorical-q-ext-deriv",
    "rem:q-laplacian-interpretation",
    "def:frobenius-pairing",
    "rem:planck-reynolds",
    "prop:discrete-vortex-spectrum",
    "prop:kelvin-dispersion-derivation",
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
