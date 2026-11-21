import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:gb-spectral-sequence",
  label: "rem:gb-spectral-sequence-interpretation",
  title:
    "Open questions, structural value, and the Picard–Lefschetz archimedean realisation",
  tags: [
    "spectral-sequence",
    "cohomology",
    "hochschild",
    "gb-filtration",
    "picard-lefschetz",
    "derivation-chain",
  ],
  uses: [
    "prop:gb-spectral-sequence",
    "thm:frobenius-codim-universal",
    "conj:mass-formula-regime-switching",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): At $p = 0$ (descended $\\mathrm{tr}_M$), this yields the Frobenius co-Casimir ([Universal Frobenius co-dimension trace: $\\tau(C_{\\dim_q}) = \\sum_\\lambda 1/\\dim_q(\\lambda)$](#thm:frobenius-codim-universal))." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): 3. If different pages dominated for different $A$, that would explain the regime switching of [Mass formula regime switch](#conj:mass-formula-regime-switching). This is conjectural: in the corpus the regime of each $A$ is selected against AME data, which is an ad-hoc per-$A$ choice. Only the location of the boundaries ($A = 2\\mid3$ and $4\\mid5$) is derived, from $A$ alone, in [Pair-graph regimes of $A$](#prop:pair-graph-regime-trichotomy)." },
  ],
});
