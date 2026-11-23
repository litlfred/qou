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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean sibling proves, kernel-checked without `sorry`:" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean carries its own executable Littlewood–Richardson positivity (skew ballot tableaux) and independently reproduces the counts of the computational probe, so the two implementations cross-validate." },
  ],
});
