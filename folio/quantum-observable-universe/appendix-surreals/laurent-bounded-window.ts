import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:laurent-bounded-window",
  lean: {
    ref: "qou:QOU.AppendixSurreals.CollatzBoundedWindow.reaches_cycle_of_bounded_window",
    validation: "leanok",
  },
  title: "Bounded-support $\\mathcal{C}_q$-orbits enter a finite cycle via $\\mathbb{F}_2[q]$ pigeonhole",
  uses: [
    "prop:balanced-holonomy-exclusion",
    "prop:q-syracuse-lift",
  ],
  tags: ["laurent-polynomial", "pigeonhole", "mod-2-reduction", "periodic-cycle"],
});
