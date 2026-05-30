import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:joint-galois-braid-action",
  title:
    "Joint motivic-Galois $\\times$ braid-group action on the bi-filtration $\\mathcal{H}_q^{(n, K)}$",
  lean: { ref: "qou:QOU.BraidKnot.JointGaloisBraidAction", validation: "stub" },
  uses: ["def:hq-bi-filtration"],
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
