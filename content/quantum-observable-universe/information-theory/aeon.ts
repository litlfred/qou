import { definition } from "../../schema/builders";

export default definition({
  label: "def:aeon",
  title: "Aeon",
  tags: [
    "aeon", "jet-horizon", "affine-chart",
    "light-cone", "cyclic-cosmology",
  ],
  lean: { ref: "qou:QOU.Aeon",
    validation: "not_checked",
  },
  uses: [
    "def:observable-subcategory",
    "def:jet-horizon",
  ],
});
