import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:brings-smoothness-resolution",
  title:
    "Smoothness of the Bring's surface and intrinsic resolution of projection singularities",
  tags: ["brings-surface", "smooth", "resolution", "branch-point", "coral"],
  lean: { ref: "qou:QOU.BringsSurface.brings_smoothness_resolution",
    validation: "not_checked",
  },
  uses: [
    "rem:coral-bundles",
    "def:briggs-klein-chart",
  ],
});
