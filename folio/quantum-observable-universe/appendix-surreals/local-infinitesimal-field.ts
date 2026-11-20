import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:local-infinitesimal-field",
  title:
    "Substrate parameter as a local infinitesimal field $\\varepsilon(x)$",
  lean: { ref: "qou:QOU.AppendixSurreals.LocalInfinitesimalField", validation: "stub" },
  tags: [
    "tier:P",
    "surreal-numbers",
    "substrate-parameter",
    "local-field",
    "infinitesimal",
    "points-and-topology",
    "sheaf",
    "open-problem",
  ],
  uses: [
    "rem:valuation-ring-finite-surreals",
  ],
  cites: [
    "conway1976",
    "ehrlich2012",
    "berarducci-mantova2018",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Open and speculative.** This is the most strongly\nconjectural of the appendix's conjectures: it assumes a\ngeometric-scheme picture of $X$ that the main paper does not\nrequire, and interprets the substrate parameter in a way that\ngoes beyond the main-paper physics. Included here to record the\nnatural connection between the paper's points-and-topology\nframework and the surreal lift.",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): up to the\n $\\varepsilon$-relaxations of\n [infinitesimal-frobenius](#conj:infinitesimal-frobenius) etc" },
  ],
});
