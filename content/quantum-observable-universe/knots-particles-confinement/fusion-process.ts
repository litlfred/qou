import { definition } from "../../schema/builders";

export default definition({
  label: "def:fusion-process",
  title: "Fusion process",
  lean: { ref: "qou:QOU.Interactions.FusionProcessBlock.Process.isRearrangement" },
  uses: ["def:atom-knot"],
  computation: {
    engine: "python",
    script: "computations/probes/fusion_process_lr_support_probe.py",
    status: "verified",
  },
  tags: [
    "fusion",
    "process",
    "strong-sector",
    "strand-conservation",
    "littlewood-richardson",
    "support-contraction",
  ],
});
