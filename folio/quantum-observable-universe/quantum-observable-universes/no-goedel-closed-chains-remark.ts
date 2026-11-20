import { remark } from "../../schema/builders";

/**
 * Why a Gödel-type universe has no place under the arrow-of-time reading
 * of the braiding-induced ordering.
 *
 * The exclusion is an order-theoretic theorem (a well-founded relation has no
 * closed chains); applying it to spacetime causality is an interpretation,
 * and the block keeps the two apart.
 */
export default remark({
  interprets: "prop:braiding-induced-ordering",
  label: "rem:no-goedel-closed-chains",
  title: "No closed causal chains: why a Gödel universe is excluded",
  lean: {
    ref: "qou:QOU.Chronology.not_totalChronology_of_wellFounded",
    sorryFree: true,
    validation: "not_checked",
  },
  uses: ["prop:braiding-induced-ordering"],
  tags: [
    "arrow-of-time",
    "causality",
    "well-ordering",
    "closed-timelike-curves",
    "goedel-universe",
    "scope-limit",
  ],
});
