import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:two-filtration-bridge-general",
  proofs: ["prf:two-filtration-bridge-general"],
  title:
    "Two-filtration bridge map in full generality: bar-class determines iterated-integral depth (self-conj $\\to$ 2, chiral pair $\\to$ 3) for all partitions",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.TwoFiltrationBridgeGeneral.bridge_map_general",
    validation: "not_checked",
  },
  uses: ["prop:cyclotomic-cl3-orbit-sum-general"],
  cites: ["bloch2000"],
  tags: [
    "two-filtration-bridge",
    "general-partitions",
    "bar-eigenspace",
    "self-conjugate",
    "chiral-pair",
    "graded-mikusinski",
    "theorem-level",
  ],
});
