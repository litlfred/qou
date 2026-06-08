import { proposition } from "../../schema/builders";

/**
 * LP dual binding for CO: optimal triple bond.
 */
export default proposition({
  label: "prop:co-lp-dual-binding",
  lean: { ref: "qou:QOU.Molecular.co_lp_dual_binding", validation: "not_started" },
  title: "LP dual selects the triple bond as optimal for $CO$",
  computation: {
    engine: "python",
    script: "folio-assistant/computations/co_bond_order_active_set.py",
    witness: [
      "folio-assistant/computations/co-bond-order-active-set.witness.json",
    ],
  },
  uses: [
    "def:co-molecular-braid",
    "prop:h2-lp-dual-binding",
  ],
  tags: ["CO", "LP-dual", "triple-bond", "optimal"],
});
