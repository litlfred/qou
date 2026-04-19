import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:knot-operator-selection",
  lean: {
    decl: "QOU.DescartesUniverse.knot_operator_selection",
    validation: "not_checked",
  },
  title: "Knot operator selection via Frobenius dual",
  uses: [
    "def:categorical-action",
    "def:breit-wheeler-pair-production",
    "prop:rj-canonical-inner-product",
    "prop:cohomological-embedding",
    "prop:fiber-adjoint-involution",
  ],
  tags: [
    "knot-operator",
    "pair-production",
    "frobenius-dual",
    "operator-selection",
    "hecke-algebra",
    "categorical-action",
    "rigid-duality",
    "multi-channel",
  ],
});
