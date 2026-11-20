import { remark } from "../../schema/builders";

/**
 * The Gödel reading of lem:crossing-application-chains. The mathematics is
 * in the lemma; this block only interprets it, under the stated modelling
 * choice that one tick is one crossing application.
 */
export default remark({
  interprets: "prop:braiding-induced-ordering",
  label: "rem:no-goedel-closed-chains",
  title: "No closed causal chains under the tick definition: the Gödel universe",
  lean: {
    ref: "qou:QOU.word_no_closedChainAt",
    sorryFree: true,
    validation: "not_checked",
  },
  uses: [
    "prop:braiding-induced-ordering",
    "prf:braiding-induced-ordering",
    "lem:crossing-application-chains",
  ],
  cites: ["goedel1949"],
  tags: [
    "arrow-of-time",
    "causality",
    "well-ordering",
    "closed-timelike-curves",
    "goedel-universe",
    "scope-limit",
    "writhe",
    "symmetric-braiding",
  ],
});
