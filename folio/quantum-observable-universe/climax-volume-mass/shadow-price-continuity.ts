import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:shadow-price-continuity",
  title: "Continuity of shadow prices on the generic locus",
  lean: { ref: "qou:QOU.BraidKnot.ShadowPriceContinuity",
    validation: "not_checked",
  },
  uses: ["def:local-shadow-ordering"],
  tags: [
    "shadow-price",
    "continuity",
    "rational-function",
    "generic-locus",
  ],
});
