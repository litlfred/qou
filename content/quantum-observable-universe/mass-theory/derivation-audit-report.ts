import { prose } from "../../schema/builders";

export default prose({
  label: "prose:derivation-audit-report",
  title: "Derivation Audit Report: Mass, Beta-Decay, and Binding-Energy Computations",
  uses: [
    "prop:atom-knot-mass-derivation",
    "prop:chirality-writhe-ribbon-derivation",
    "prop:brane-tower-z-habiro",
    "prop:canonical-knot-id-sdp",
    "prop:chirality-ribbon-frobenius",
    "conj:brane-level-selection",
    "prop:rho-prefactor-structural",
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
