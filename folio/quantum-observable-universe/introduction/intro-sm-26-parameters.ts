import { table } from "../../schema/builders";

/**
 * Reader-facing summary of all 26 Standard Model + massive-neutrino parameters
 * grouped by sector (3 + 6 + 3 + 4 + 4 + 3 + 2 + 1 = 26) at proton-pinned
 * q_0 = 1.109978582751380808 (bean qou-intr). Grounded in ACCURACY.md,
 * docs/audits/2026-11-28-accuracy-conditional-discharge-ledger.md,
 * docs/audits/2026-11-28-muon-mass-relation.md,
 * QOU/StandardModel/AlphaEmConditionalReduction.lean,
 * QOU/StandardModel/ElectroweakConditionalDischarge.lean,
 * QOU/StandardModel/KoideSingletDoubletEquipartition.lean, and
 * folio/quantum-observable-universe/appendix-standard-model/sm-params-*.md.
 */
export default table({
  label: "tbl:intro-sm-26-parameters",
  title: "Summary of the 26 Standard Model parameters (including massive neutrinos)",
  uses: [
    "app:standard-model",
    "prose:sm-params-intro",
    "def:three-calibration-discipline",
    "rem:epistemic-status-of-calibrations",
    "prop:em-coupling-fixed-point",
    "conj:weinberg-angle-categorical",
    "conj:electroweak-higgs-torus-link-triplet",
    "chap:observations",
  ],
  cites: ["codata2022", "pdg2024"],
  tags: ["introduction", "standard-model", "parameters", "summary-table"],
});
