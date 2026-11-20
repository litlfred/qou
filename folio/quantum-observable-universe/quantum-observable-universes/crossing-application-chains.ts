import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:crossing-application-chains",
  title: "Closed chains of crossing applications on words and on states",
  lean: {
    ref: "qou:QOU.Chronology.not_closedChainAt_tick",
    sorryFree: true,
    validation: "not_checked",
  },
  uses: ["prop:braiding-induced-ordering"],
  tags: [
    "arrow-of-time",
    "well-ordering",
    "braid-group",
    "writhe",
    "symmetric-braiding",
    "closed-chains",
  ],
});
