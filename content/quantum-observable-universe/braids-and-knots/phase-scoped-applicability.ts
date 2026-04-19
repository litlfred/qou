import { remark } from "../../schema/builders";

export default remark({
  label: "rem:phase-scoped-applicability",
  title:
    "Phase-scoped applicability: confinement theorems hold on open strata only",
  tags: [
    "phase",
    "phase-boundary",
    "scope",
    "deconfinement",
    "regime-switch",
    "open-set",
  ],
  uses: [
    "prop:confinement-phase-stratification",
    "def:confined-particle",
    "def:confinement-category",
    "prop:confinement-sdp",
    "prop:level-sufficiency",
    "prop:shell-closure-stability",
    "def:electron-shell",
    "def:dressed-particle",
    "def:deconfinement-golden-threshold",
    "prop:parity-regime-selection",
  ],
  interprets: "prop:confinement-phase-stratification",
});
