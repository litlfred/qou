import { definition } from "../../schema/builders";

export default definition({
  label: "def:big-bang-state",
  title: "Big bang state (degree-$0$ trivial configuration)",
  tags: [
    "big-bang-state", "jet-horizon", "initial-conditions",
    "degree-zero", "deep-quantum",
  ],
  lean: { ref: "qou:QOU.BigBangState",
    validation: "not_checked",
  },
  uses: [],
});
