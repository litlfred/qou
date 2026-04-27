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
  lean: { ref: "qou:QOU.Information.crossing_parity_eq_Z",
    validation: "not_checked",
  },
  uses: [
    "prop:shell-structure-eigenvalues",
    "prop:noble-gas-characterization",
  ],
});
