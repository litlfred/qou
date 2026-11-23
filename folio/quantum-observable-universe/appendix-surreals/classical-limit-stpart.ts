import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:classical-limit-stpart",
  title:
    "Classical-limit functor as standard-part of evaluation at $q = 1 + \\varepsilon$",
  tags: [
    "tier:P",
    "surreal-numbers",
    "classical-limit",
    "standard-part",
    "nonstandard-analysis",
    "substrate-parameter",
    "open-problem",
  ],
  uses: [
    "def:classical-limit-functor",
    "def:substrate-parameter",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): | [archimedean QOU is standard-part of surreal](#conj:archimedean-stpart) | Whole-tuple surreal replacement on $(\\mathbf{C}, \\varTheta, G, \\mathcal{S})$ | Conjecture (open) |" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The current block provides the single-functor version; the whole-tuple version is the appendix companion. Both are likely equivalent modulo functoriality." },
  ],
  cites: ["robinson1966", "berarducci-mantova2018"],
  lean: {
    ref: "qou:QOU.AppendixSurreals.ClassicalLimitStpart",
    validation: "not_checked",
  },
});
