import { prose } from "../../schema/builders";

export default prose({
  label: "prose:derivation-audit-report",
  title: "Derivation Audit Report: Mass, Beta-Decay, and Binding-Energy Computations",
  uses: [
    "prop:atom-knot-mass-derivation",
    "prop:chirality-writhe-ribbon-derivation",
    "prop:chirality-from-frobenius-self-pairing",
    "prop:alpha-k-derivation-procedure",
    "rem:calibration-inputs",
    "conj:brane-tower-z-habiro",
    "conj:canonical-knot-id-sdp",
    "conj:chirality-ribbon-frobenius",
    "conj:brane-level-selection",
    "conj:rho-prefactor-structural",
  ],
  tags: [
    "audit",
    "gaps",
    "empirical-fitting",
    "derivation-chain",
    "gap-a",
    "gap-b",
    "gap-c",
    "gap-d",
    "mass-formula",
    "beta-decay",
    "binding-energy",
  ],
});
