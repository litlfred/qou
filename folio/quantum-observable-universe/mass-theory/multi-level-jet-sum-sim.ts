import { simulator } from "../../schema/builders";

export default simulator({
  label: "sim:multi-level-jet-sum",
  title: "Multi-level jet-sum visualiser",
  html: "simulators/multi_level_jet_sum.html",
  uses: ["rem:mass-tower-syt-cells"],
  tags: ["jet-sum", "atomic-mass", "tower", "interactive"],
  defaultView: {
    name: "default",
    title: "Jet-sum levels for light atoms",
    params: { atom: "deuteron", levels: 6 },
  },
});
