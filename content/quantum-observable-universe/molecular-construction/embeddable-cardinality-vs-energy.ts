import { remark } from "../../schema/builders";

/**
 * Interpretive follow-on to def:embeddable-knot-operator: overlap weighting
 * changes the binding energy, not the channel count (active-set cardinality =
 * bond order is weight-independent); the equal-channel model overbinds N₂.
 */
export default remark({
  label: "rem:embeddable-cardinality-vs-energy",
  title: "Overlap weighting changes energy, not channel count",
  interprets: "def:embeddable-knot-operator",
  uses: ["def:embeddable-knot-operator"],
  tags: ["cardinality", "bond-order", "overlap-weight", "N2", "active-set"],
});
