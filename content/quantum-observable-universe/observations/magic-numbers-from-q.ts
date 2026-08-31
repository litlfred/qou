import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:magic-numbers-from-q",
  title:
    "Wedderburn nuclear character signal at $q_0$ is elevated at the magic numbers",
  tags: [
    "magic-numbers",
    "shell-closure",
    "hoefsmit",
    "wedderburn",
    "seminormal-form",
    "block-diagonal",
  ],
  lean: {
    ref: "qou:QOU.AtomicMass.magic_numbers_from_q",
    validation: "not_checked",
  },
  uses: [],
});
