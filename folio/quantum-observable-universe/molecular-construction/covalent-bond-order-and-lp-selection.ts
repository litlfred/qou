import { remark } from "../../schema/builders";

/**
 * Follow-on to def:covalent-bond-shared-trefoil: the lone-vs-shared crossing
 * comparison table, the 2k-attractive-crossing count, the single/double/triple
 * bond-order enumeration, and the LP-dual minimisation of Φ₁ that assigns
 * electrons to bonding positions.
 */
export default remark({
  label: "rem:covalent-bond-order-and-lp-selection",
  title: "Covalent bond orders and LP-dual electron assignment",
  interprets: "def:covalent-bond-shared-trefoil",
  uses: ["def:covalent-bond-shared-trefoil"],
  tags: ["covalent-bond", "bond-order", "LP-dual", "Phi1", "electron-assignment"],
});
