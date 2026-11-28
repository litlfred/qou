import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-syracuse-lift",
  lean: {
    ref: "qou:QOU.AppendixSurreals.CollatzSyracuseLift.syracuse_of_step",
    validation: "leanok",
  },
  title: "Evaluation at $q = 1$ projects $\\mathcal{C}_q$-orbits to Syracuse trajectories and lifts periodicity",
  uses: [
    "prop:balanced-holonomy-exclusion",
  ],
  cites: ["lagarias2010"],
  tags: ["laurent-polynomial", "syracuse", "periodic-cycle", "coprimality"],
});
