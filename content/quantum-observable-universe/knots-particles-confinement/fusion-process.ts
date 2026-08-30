import { definition } from "../../schema/builders";

export default definition({
  label: "def:fusion-process",
  title: "Fusion process",
  lean: { ref: "qou:QOU.Interactions.FusionProcessBlock.Process.isRearrangement" },
  uses: ["def:atom-knot"],
  tags: [
    "fusion",
    "process",
    "strong-sector",
    "strand-conservation",
    "littlewood-richardson",
    "support-contraction",
  ],
});
