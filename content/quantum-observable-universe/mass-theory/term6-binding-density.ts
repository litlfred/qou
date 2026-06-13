import { remark } from "../../schema/builders";

export default remark({
  label: "rem:term6-binding-density",
  title:
    "Term 6 binding density: $B(Z,N)/A \\approx \\alpha \\cdot T_6(Z,N)/A^3 + \\beta + \\delta_M(Z,N)$",
  interprets: "prop:gb-spectral-sequence",
  tags: [
    "binding-energy",
    "derivation-chain",
    "gs-filtration",
    "spectral-sequence",
    "term-6",
    "level-3-stratum",
    "calibrated-fit",
    "magic-shell-correction",
  ],
  uses: [
    "prop:wigner-np-pairing",
    "prop:categorical-neutrality-saturated-shells",
  ],
  cites: ["bethe1936", "weizsacker1935", "geckpfeiffer2000"],
});
