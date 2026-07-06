import { remark } from "../../schema/builders";

/**
 * CO triple bond energy interpretation.
 */
export default remark({
  label: "rem:co-triple-bond-energy",
  title: "$CO$ triple bond energy from the Wedderburn invariants",
  interprets: "prop:co-lp-dual-binding",
  uses: ["def:co-molecular-braid"],
  tags: ["CO", "triple-bond", "binding-energy", "prediction"],
  computation: {
    engine: "python",
    script: "computations/co_bond_order_active_set.py",
    witness: [
      "computations/co-bond-order-active-set.witness.json"
    ],
    status: "experimental",
  },
});
