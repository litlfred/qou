import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:classical-limit-stpart",
  title:
    "Classical-limit functor as standard-part of evaluation at $q = 1 + \\varepsilon$",
  tags: [
    "tier:P",
    "surreal-numbers",
    "classical-limit",
    "standard-part",
    "nonstandard-analysis",
    "substrate-parameter",
    "open-problem",
  ],
  uses: [
    "def:classical-limit-functor",
    "def:substrate-parameter",
  ],
  cites: ["robinson1966", "berarducci-mantova2018"],
  lean: {
    ref: "qou:QOU.AppendixSurreals.ClassicalLimitStpart",
    validation: "not_checked",
  },
});
