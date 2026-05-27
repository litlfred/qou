import { conjecture } from "../../schema/builders";

export default proposition({
  label: "prop:regularity-breakdown",
  title: "Regularity breakdown at $q = 1$: the classical limit as a phase transition",
  uses: [
    "thm:q-ns-wellposedness",
    "prop:q-turbulence-spectrum",
    "rem:hamilton-jacobi-phase",
  ],
  tags: [
    "navier-stokes",
    "millennium-problem",
    "regularity",
    "phase-transition",
    "critical-exponent",
    "blowup",
  ],
});
