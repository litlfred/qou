import { definition } from "../../schema/builders";

export default definition({
  label: "def:aeon",
  title: "Aeon",
  tags: [
    "aeon", "jet-horizon", "affine-chart",
    "light-cone", "cyclic-cosmology",
  ],
  lean: {
    decl: "QOU.Aeon",
    validation: "not_checked",
  },
  uses: [
    "def:jet-horizon",
    "def:big-bang-state",
    "def:bundle-initial-conditions",
    "def:information-theoretic-time",
  ],
});
