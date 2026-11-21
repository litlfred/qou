import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chirality-period-pairing",
  title:
    "Chirality structure on Goncharov period classes via the bar involution",
  interprets: "prop:hecke-baer-star-generic",
  uses: ["conj:bring-trilog-depth-3-witness"],
  cites: ["bloch2000"],
  tags: [
    "chirality",
    "amphichirality",
    "bar-involution",
    "period-pairing",
    "chern-simons",
    "tate-twist",
    "graded-mikusinski",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): See [Bring trilog at $\\zeta_5$ as depth-3 grouplike value (50-digit functional-equation cross-validated witness)](#conj:bring-trilog-depth-3-witness) for a Bring-natural depth-$3$ witness." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): This categorifies the amphichirality construction introduced in the figure-$8$ block ([Figure-8 knot $4_1$ as illustration of the algebraic / archimedean dichotomy](#rem:figure-8-archimedean-illustration)). One recasts it as a period-theoretic structure on $\\mathcal{P}_\\bullet$." },
  ],
});
