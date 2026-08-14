import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hadron-operations-closure",
  title:
    "Closure of hadron operations under braiding, Hopf linking, skein action, and fusion",
  tags: ["hadron", "braiding", "hopf-link", "skein", "fusion", "closure"],
  lean: { ref: "qou:QOU.Hadron.hadron_operations_closure",
    validation: "not_checked",
  },
  uses: [
    "def:hadron",
    // Closure is stated for the *binary* braiding. No separate closure
    // clause is needed for many-body interactions, because every such
    // interaction is a word in binary crossings.
    "prop:pairwise-interaction-decomposition",
  ],
});
