import { remark } from "../../schema/builders";

export default remark({
  label: "rem:pair-creation-energy",
  title: "Energy cost of electron--positron conversion",
  interprets: "def:crossing-energy",
  uses: [
    "rem:trefoil-vortex-chirality-flip",
    "rem:mass-comparison-table",
  ],
  tags: [
    "pair-creation", "crossing-energy", "electron", "positron",
    "energy-budget", "exceptional-divisor", "chirality",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
});
