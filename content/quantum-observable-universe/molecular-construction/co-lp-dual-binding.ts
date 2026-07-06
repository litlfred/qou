import { proposition } from "../../schema/builders";

/**
 * LP dual binding for CO: optimal triple bond.
 */
export default proposition({
  label: "prop:co-lp-dual-binding",
  lean: { ref: "qou:QOU.Molecular.co_lp_dual_binding", validation: "not_checked" },
  title: "LP dual for $CO$: covalent active-set $2$ ($+$ dative $=$ triple)",
  computation: {
    engine: "python",
    status: "verified",
    script: "computations/co_bond_order_active_set.py",
    witness: [
      "computations/co-bond-order-active-set.witness.json",
    ],
  },
  uses: [
    "def:co-molecular-braid",
    "prop:h2-lp-dual-binding",
  ],
  tags: ["CO", "LP-dual", "triple-bond", "optimal"],
});
