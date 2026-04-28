import { proof } from "../../schema/builders";

export default proof({
  label: "prf:c6-energy-comparison",
  title: "Linear C${}_{6}$ vs. benzene ring (sympy)",
  tags: [
    "carbon-chain",
    "benzene",
    "energy-comparison",
    "verification",
    "computation",
    "sympy",
  ],
  uses: ["lem:c6-energy-comparison"],
  computation: {
    engine: "sympy",
    script: "computations/chain_vs_ring_energy_N6.py",
    witness: "computations/chain-vs-ring-energy-N6.witness.json",
    status: "verified",
  },
});
