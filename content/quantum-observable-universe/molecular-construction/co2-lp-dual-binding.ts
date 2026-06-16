import { proposition } from "../../schema/builders";

/**
 * LP dual binding for CO₂: linear geometry emerges from optimization.
 */
export default proposition({
  label: "prop:co2-lp-dual-binding",
  lean: { ref: "qou:QOU.Molecular.co2_lp_dual_binding", validation: "not_checked" },
  title: "LP dual selects linear $O{=}C{=}O$ geometry",
  uses: [
    "def:co2-molecular-braid",
    "prop:co-lp-dual-binding",
  ],
  tags: ["CO2", "LP-dual", "linear", "geometry", "double-bond"],
  computation: {
    engine: "python",
    script: "computations/co_bond_order_active_set.py",
    witness: [
      "computations/co-bond-order-active-set.witness.json",
      "computations/molecular-experimental-refs.witness.json"
    ],
    status: "experimental",
  },
});
