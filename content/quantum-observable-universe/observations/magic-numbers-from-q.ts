import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:magic-numbers-from-q",
  title:
    "Magic numbers emerge from per-partition nuclear character at $q_0$",
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
  uses: [
    "conj:shell-closure-nf-term-count",
    "prop:nuclear-knot-classification",
    "prop:mass-coefficient-shadow-price",
  ],
});
