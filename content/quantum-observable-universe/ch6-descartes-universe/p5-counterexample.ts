import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:ns-counterexample",
  title:
    "Counter-example to Navier--Stokes regularity via $q \\to 1$ degeneration",
  uses: [
    "prop:blowup-yekutieli",
    "prop:critical-exponent",
    "prop:universality",
    "prop:q-ns-nonlinear-uniqueness",
    "thm:q-ns-wellposedness",
    "def:yekutieli-lifting-condition",
    "def:quantum-characteristic-classes",
    "def:local-cohomology-group",
    "rem:vortex-reconnection",
    "prop:acoustic-horizon-conditions",
    "rem:geodesic-vortices",
    "def:recursive-brane-tower",
    "prop:descent-condition",
  ],
  tags: [
    "counter-example",
    "millennium-problem",
    "navier-stokes",
    "blowup",
    "yekutieli",
    "homological",
    "vortex-collision",
  ],
});
