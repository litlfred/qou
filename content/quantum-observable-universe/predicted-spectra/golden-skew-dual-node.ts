import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:golden-skew-dual-node",
  proofs: ["prf:golden-skew-dual-node"],
  title:
    "Skew-dual golden node at $q = \\varphi^2$ under the bar involution $q \\leftrightarrow q^{-1}$",
  tags: [
    "golden-ratio",
    "bar-involution",
    "skew-symmetry",
    "elliptic-degeneration",
    "stability-margin",
    "substrate-parameter",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.golden_skew_dual_node",
    validation: "not_checked",
  },
  uses: ["rem:golden-ratio-degeneration"],
});
