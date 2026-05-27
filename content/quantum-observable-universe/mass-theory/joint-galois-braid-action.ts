import { conjecture } from "../../schema/builders";

export default proposition({
  label: "prop:joint-galois-braid-action",
  title:
    "Joint motivic-Galois $\\times$ braid-group action on the bi-filtration $\\mathcal{H}_q^{(n, K)}$",
  lean: { ref: "qou:QOU.BraidKnot.JointGaloisBraidAction", validation: "stub" },
  uses: [
    "def:hq-bi-filtration",
    "prop:gb-depth-period-correspondence",
    "rem:chirality-period-pairing",
    "prop:bring-trilog-depth-3-witness",
    "prop:bring-figure-eight-depth-2-witness",
  ],
  cites: ["kontsevich1995", "bloch2000"],
  tags: [
    "joint-action",
    "motivic-galois",
    "braid-group",
    "bi-filtration",
    "graded-mikusinski",
    "open-problem",
  ],
});
