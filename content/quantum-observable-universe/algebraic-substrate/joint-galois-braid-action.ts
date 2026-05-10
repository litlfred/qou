import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:joint-galois-braid-action",
  title:
    "Joint motivic-Galois $\\times$ braid-group action on the bi-filtration $\\mathcal{H}_q^{(n, K)}$",
  uses: [
    "def:hq-bi-filtration",
    "conj:gb-depth-period-correspondence",
    "rem:chirality-period-pairing",
    "conj:bring-trilog-depth-3-witness",
    "conj:bring-figure-eight-depth-2-witness",
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
