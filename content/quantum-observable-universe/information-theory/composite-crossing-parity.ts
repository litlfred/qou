import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:composite-crossing-parity",
  title: "Sublimation from shell-filling representation theory",
  tags: [
    "sublimation",
    "shell-structure",
    "young-diagram",
    "hecke-representation",
    "phase-transition",
    "magic-numbers",
  ],
  lean: {
    decl: "QOU.Information.compositeCrossingParity",
    validation: "not_checked",
  },
  uses: [
    "prop:phase-transition-boundary",
    "prop:knot-eigenbasis-complete",
    "prop:shell-structure-eigenvalues",
    "prop:noble-gas-characterization",
    "def:stable-nucleus",
  ],
});
