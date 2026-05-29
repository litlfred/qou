import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:rho-prefactor-structural",
  lean: { ref: "qou:QOU.BraidKnot.RhoPrefactorStructural" },
  title:
    "Structural prefactor rule: $\\rho(\\mathfrak{H}) = \\dim_q(\\lambda^*(T_w))$",
  uses: ["prop:atom-knot-mass-derivation"],
  tags: [
    "sdp-multiplicity",
    "wedderburn",
    "prefactor",
    "structural-rule",
    "gap-a",
    "audit",
  ],
});
