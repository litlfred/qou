import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:joint-galois-braid-action",
  title:
    "Joint motivic-Galois $\\times$ braid-group action on the bi-filtration $\\mathcal{H}_q^{(n, K)}$",
  lean: { ref: "qou:QOU.BraidKnot.JointGaloisBraidAction", validation: "stub" },
  uses: ["def:hq-bi-filtration"],
  cites: ["kontsevich1995", "bloch2000"],
  tags: [
    "tier:S",
    "joint-action",
    "motivic-galois",
    "braid-group",
    "bi-filtration",
    "graded-mikusinski",
    "open-problem",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Open.** The joint commutativity is conjectural but mathematically\nnatural: motivic-Galois acts on the period side; braid-group acts\non the algebraic-cell side; they should commute since they touch\ndisjoint structure.\n\n**Discharge target.** Verify on a non-trivial $(n, K)$ pair where\nboth actions are non-trivial. The simplest candidate: $5_2$ (chiral\nhyperbolic, 4-strand braid, depth-2 grouplike pairing) — bar action\non $5_2$ swaps the chiral cell pair, braid action on $H_4(q)$\npermutes Wedderburn blocks; commutativity prediction is testable.",
    },
  ],
});
