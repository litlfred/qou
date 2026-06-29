import { remark } from "../../schema/builders";

/**
 * Interpretive follow-on to prop:co2-lp-dual-binding: the braid-theoretic VSEPR
 * reading (Φ₁ minimisation = electron-pair repulsion minimisation) and the
 * CO-triple vs CO₂-double per-shared-pair energy comparison. Carries the two
 * witnesses consumed by the :val directives.
 */
export default remark({
  label: "rem:co2-vsepr-and-per-bond-energy",
  title: "VSEPR as $\\Phi_1$ minimisation; per-bond energy by bond order",
  interprets: "prop:co2-lp-dual-binding",
  uses: ["def:co2-molecular-braid"],
  computation: {
    engine: "python",
    script: "computations/co_bond_order_active_set.py",
    witness: [
      "computations/co-bond-order-active-set.witness.json",
      "computations/molecular-experimental-refs.witness.json",
    ],
    status: "experimental",
  },
  tags: ["CO2", "VSEPR", "per-bond-energy", "bond-order", "LP-dual"],
});
