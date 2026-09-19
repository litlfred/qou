import { simulator } from "../../../folio-assistant/schemas/builders";

// Stub simulator block: multi-level jet-sum visualisation on the
// atomic mass formula. Used by mass-tower-syt-cells.md to display
// the converged tower for D, T, ³He, ⁴He at q_0. HTML implementation
// deferred.
export default simulator({
  label: "sim:multi-level-jet-sum",
  title: "Multi-level jet-sum visualiser",
  html: "simulators/multi_level_jet_sum.html",
  uses: ["rem:mass-tower-syt-cells"],
  tags: ["jet-sum", "atomic-mass", "tower", "todo-html", "interactive"],
  defaultView: {
    name: "default",
    title: "Jet-sum levels for light atoms",
    params: { atom: "deuteron", levels: 6 },
  },
});
