import { proof } from "../../schema/builders";

export default proof({
  label: "prf:beta-decay-transfer-matrix",
  title: "Proof of beta decay transfer matrix",
  uses: ["prop:beta-decay-transfer-matrix"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Form B is **not a separate observable** from the NF-counit form\n$\\mathfrak{Q}_\\beta^{\\mathrm{A}} = |\\Delta(\\mathrm{net})| \\cdot E_0$ of\n[prop:neutron-qvalue-symbolic](#prop:neutron-qvalue-symbolic);\nthe two are basis-change equivalent at leading order, with the\nexplicit bridge identity given in\n[conj:q-beta-spectral-bridge](#conj:q-beta-spectral-bridge):\n\n$$\n  \\mathfrak{Q}_\\beta^{\\mathrm{A}}\n  \\;=\\;\n  \\mathfrak{Q}_\\beta^{\\mathrm{B}} \\cdot \\bigl(1 + \\tfrac{(z - 1)\\,h}{2} + O(h^2)\\bigr).\n$$" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([transition energy](#def:Q-value-transition))" },
  ],
});
