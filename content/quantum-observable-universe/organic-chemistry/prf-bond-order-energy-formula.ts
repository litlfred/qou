import { proof } from "../../schema/builders";

export default proof({
  label: "prf:bond-order-energy-formula",
  title: "Linear bond-order energy formula vs. experimental BDEs",
  tags: [
    "bond-order",
    "BDE",
    "verification",
    "computation",
    "experimental-comparison",
  ],
  uses: ["prop:bond-order-energy-formula"],
  computation: {
    engine: "python",
    script: "computations/bond_order_energy.py",
    witness: "computations/bond-order-energy.witness.json",
    status: "verified",
  },
});
