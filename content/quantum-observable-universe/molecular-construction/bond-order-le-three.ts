import { proposition } from "../../schema/builders";

/**
 * Spatial-dimension bound on bond order: pairwise-orthogonal nonzero channels
 * in ℝ³ number at most 3, so no p-block bond exceeds order three. Resolves to
 * the library theorem QOU.Molecular.orthogonal_channels_le_dim (sorry-free).
 */
export default proposition({
  label: "prop:bond-order-le-three",
  title: "Bond order bounded by spatial dimension",
  lean: {
    ref: "qou:QOU.Molecular.orthogonal_channels_le_dim",
    validation: "not_checked",
  },
  uses: ["def:embeddable-knot-operator"],
  tags: [
    "bond-order",
    "spatial-dimension",
    "orthogonal-channels",
    "p-block",
    "sigma-pi",
  ],
});
