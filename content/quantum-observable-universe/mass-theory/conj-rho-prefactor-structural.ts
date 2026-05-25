import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:rho-prefactor-structural",
  title:
    "Structural prefactor rule: $\\rho(\\mathfrak{H}) = \\dim_q(\\lambda^*(T_w))$",
  uses: [
    "prop:atom-knot-mass-derivation",
    "prop:alpha-k-derivation-procedure",
    "prop:wedderburn-trace-identity",
    "def:confined-particle",
  ],
  tags: [
    "sdp-multiplicity",
    "wedderburn",
    "prefactor",
    "structural-rule",
    "gap-a",
    "audit",
  ],
});
