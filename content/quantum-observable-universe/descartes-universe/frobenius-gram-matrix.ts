import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:frobenius-gram-matrix",
  lean: {
    decl: "QOU.DescartesUniverse.frobenius_gram_matrix",
    validation: "not_checked",
  },
  title: "Frobenius Gram matrix and dual construction in $H_3(q)$",
  uses: [
    "def:categorical-action",
    "prop:fiber-adjoint-involution",
    "prop:rj-canonical-inner-product",
    "prop:knot-operator-selection",
  ],
  tags: [
    "gram-matrix",
    "frobenius-dual",
    "hecke-algebra",
    "markov-trace",
    "knot-operator",
    "pair-production",
    "annihilation",
  ],
});
