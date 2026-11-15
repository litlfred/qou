import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:two-filtration-bridge-small-cases",
  title:
    "Two-filtration bridge map verified at small partitions ($n \\leq 4$)",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.TwoFiltrationBridgeSmallCases.bridge_small_cases",
    validation: "not_checked",
  },
  uses: ["prop:b1-torus-knot-rows-theorem"],
  cites: ["thurston1978"],
  computation: {
    engine: "python",
    script: "computations/two_filtration_bridge_small_cases.py",
    witness: "computations/two-filtration-bridge-small-cases.witness.json",
    status: "verified",
  },
  tags: [
    "two-filtration-bridge",
    "bridge-verification",
    "small-partitions",
    "figure-8-knot",
    "trefoil",
    "self-conjugate-cells",
    "graded-mikusinski",
  ],
});
