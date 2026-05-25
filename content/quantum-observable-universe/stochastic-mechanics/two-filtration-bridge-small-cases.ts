import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:two-filtration-bridge-small-cases",
  title:
    "Two-filtration bridge map verified at small partitions ($n \\leq 4$)",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.TwoFiltrationBridgeSmallCases.bridge_small_cases",
    validation: "not_checked",
  },
  uses: [
    "conj:two-filtration-bridge",
    "rem:chirality-period-pairing",
    "prop:b1-figure-8-row-theorem",
    "prop:b1-torus-knot-rows-theorem",
    "prop:explicit-central-idempotent",
    "rem:figure-8-archimedean-illustration",
  ],
  cites: ["thurston1978"],
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
