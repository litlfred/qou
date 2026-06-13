import { proposition } from "../../schema/builders";

/**
 * ILP derivation of the covalent bond operator.
 *
 * The covalent bond is the minimum-crossing knot operator with
 * positive binding energy between two atoms.
 */
export default proposition({
  label: "prop:ilp-covalent-bond",
  lean: { ref: "qou:QOU.Molecular.covalent_bond_is_ilp_optimal" },
  title: "The covalent bond is the inverse trefoil $T_{2,3}^{-1}$",
  tags: [
    "covalent-bond",
    "inverse-trefoil",
    "ILP",
    "knot-operator",
    "molecular",
    "zero-parameters",
  ],
});
