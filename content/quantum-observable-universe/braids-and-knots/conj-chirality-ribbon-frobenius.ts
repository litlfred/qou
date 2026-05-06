import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:chirality-ribbon-frobenius",
  title:
    "Exact chirality factor from Frobenius ribbon twist: $a_K = \\sum_\\lambda w_\\lambda q^{2w(K)c(\\lambda)}\\chi_\\lambda / \\sum_\\lambda w_\\lambda \\chi_\\lambda$",
  uses: [
    "prop:chirality-writhe-ribbon-derivation",
    "prop:chirality-from-frobenius-self-pairing",
    "thm:knot-mass-formula-unified",
    "prop:alpha-k-derivation-procedure",
  ],
  tags: [
    "chirality",
    "ribbon-twist",
    "frobenius",
    "writhe",
    "kauffman",
    "gap-a",
    "audit",
  ],
});
