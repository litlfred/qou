import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:rho-prefactor-structural",
  lean: { ref: "qou:QOU.BraidKnot.RhoPrefactorStructural" },
  title:
    "Structural prefactor rule: $\\rho(\\mathfrak{H}) = \\dim_q(\\lambda^*(T_w))$",
  uses: ["prop:atom-knot-mass-derivation"],
  tags: [
    "tier:E",
    "sdp-multiplicity",
    "wedderburn",
    "prefactor",
    "structural-rule",
    "gap-a",
    "audit",
  ],
});
