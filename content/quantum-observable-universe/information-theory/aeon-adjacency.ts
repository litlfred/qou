import { definition } from "../../schema/builders";

export default definition({
  label: "def:aeon-adjacency",
  title: "Aeon adjacency",
  tags: [
    "aeon", "jet-horizon", "adjacency",
    "cyclic-cosmology", "big-bang",
  ],
  lean: { ref: "qou:QOU.aeonAdjacent",
    validation: "not_checked",
  },
  uses: [
    "def:aeon",
    "def:aeon-boundary",
  ],
});
