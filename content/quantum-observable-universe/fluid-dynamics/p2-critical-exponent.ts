import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:critical-exponent",
  lean: {
    decl: "QOU.FluidDynamics.critical_exponent",
    validation: "not_checked",
  },
  title: "Critical exponent of the enstrophy divergence at $q = 1$",
  uses: [
    "prop:q-ns-nonlinear-uniqueness",
    "conj:regularity-breakdown",
    "rem:planck-reynolds",
    "prop:q-turbulence-spectrum",
  ],
  tags: ["critical-exponent", "enstrophy", "phase-transition", "scaling"],
});
